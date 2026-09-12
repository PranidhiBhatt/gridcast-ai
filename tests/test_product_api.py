"""Product API tests with tiny stand-in estimators; no datasets or training."""

import hashlib
import json

import pytest
from fastapi.testclient import TestClient

from backend.app import main
from backend.app.model_loader import ModelStore

TIME = "2020-01-01T12:00:00+05:30"


class Predictor:
    def __init__(self, power):
        self.power = power

    def predict(self, frame):
        assert list(frame.columns) == ["second", "first"]
        assert frame.iloc[0].tolist() == [2, 1]
        return [self.power]


@pytest.fixture
def client(monkeypatch, tmp_path):
    store = ModelStore(tmp_path)
    store.cache = {"wind": (Predictor(30), ("second", "first"), "synthetic_wind"),
                   "solar": (Predictor(10), ("second", "first"), "synthetic_solar")}
    monkeypatch.setattr(main, "models", store)
    with TestClient(main.app, raise_server_exceptions=False) as c:
        yield c


def features():
    return {"features": {"first": 1, "second": 2}}


def renewable():
    return {"timestamp": TIME, "wind_power_mw": 30, "solar_power_mw": 10}


def pipeline():
    return {"timestamp": TIME, "wind": features(), "solar": features(),
            "grid": {"demand_mw": 50}, "impact": {"interval_hours": 0.25}}


@pytest.mark.parametrize("source,power", [("wind", 30), ("solar", 10)])
def test_estimation_and_exact_feature_validation(client, source, power):
    response = client.post(f"/estimate/{source}", json={**features(), "timestamp": TIME})
    assert response.status_code == 200
    assert response.json()[f"{source}_power_mw"] == power
    assert response.json()["timestamp"] == TIME
    for values in [{"first": 1}, {"first": 1, "second": 2, "extra": 0}]:
        r = client.post(f"/estimate/{source}", json={"features": values})
        assert r.status_code == 422 and r.json()["error"]["code"] == "INVALID_FEATURE_INPUT"


def test_service_endpoints(client):
    r = client.post("/estimate/renewable", json=renewable())
    assert r.status_code == 200 and r.json()["total_renewable_power_mw"] == 40
    r = client.post("/grid/analyze", json={"renewable": renewable(), "demand_mw": 50})
    assert r.status_code == 200 and r.json()["grid_status"] == "DEFICIT"
    r = client.post("/impact/analyze", json={"renewable_power_mw": 40, "interval_hours": 0.25})
    assert r.status_code == 200 and r.json()["renewable_energy_mwh"] == 10


def test_pipeline_and_information(client):
    r = client.post("/analyze", json=pipeline())
    assert r.status_code == 200
    body = r.json()
    assert set(body) == {"timestamp", "wind", "solar", "renewable", "grid", "impact"}
    assert body["timestamp"] == TIME
    assert body["grid"]["supply_gap_mw"] == -10
    assert body["impact"]["estimated_avoided_generation_cost"] == 500
    assert body["impact"]["grid_status"] == "DEFICIT"
    info = client.get("/model/info").json()
    assert info["wind"]["required_features"] == ["second", "first"]
    assert "artifact" not in json.dumps(info)
    assert client.get("/project/status").json()["wind_model"] == "AVAILABLE"
    assert client.get("/health").json() == {"status": "ok", "service": "GridCast AI"}


@pytest.mark.parametrize("bad", [-1, "2", True, None])
def test_invalid_demand_and_interval(client, bad):
    p = pipeline()
    p["grid"]["demand_mw"] = bad
    assert client.post("/analyze", json=p).status_code == 422
    p = pipeline()
    p["impact"]["interval_hours"] = bad
    assert client.post("/analyze", json=p).status_code == 422


def test_finite_numbers_zero_interval_and_required_fields(client):
    for literal in ["NaN", "Infinity", "-Infinity"]:
        r = client.post("/estimate/wind", content='{"features":{"first":' + literal + ',"second":2}}',
                        headers={"content-type": "application/json"})
        assert r.status_code == 422 and r.json()["error"]["code"] == "INVALID_INPUT"
    p = pipeline()
    p["impact"]["interval_hours"] = 0
    assert client.post("/analyze", json=p).status_code == 422
    assert client.post("/analyze", json={}).status_code == 422


def test_unavailable_and_services_independent(client):
    main.models.cache.clear()
    for source in ("wind", "solar"):
        r = client.post(f"/estimate/{source}", json=features())
        assert r.status_code == 503 and r.json()["error"]["code"] == "MODEL_UNAVAILABLE"
    assert client.post("/analyze", json=pipeline()).status_code == 503
    assert client.get("/project/status").json()["wind_model"] == "UNAVAILABLE"
    assert client.get("/model/info").json()["solar"]["availability"] == "UNAVAILABLE"
    assert client.post("/estimate/renewable", json=renewable()).status_code == 200
    r = client.post("/grid/analyze", json={"renewable": {**renewable(), "solar_power_mw": None}, "demand_mw": 50})
    assert r.json()["analysis_status"] == "UNAVAILABLE"


def test_invalid_model_output_and_internal_errors(client, monkeypatch):
    main.models.cache["wind"][0].power = -1
    r = client.post("/estimate/wind", json=features())
    assert r.status_code == 500 and r.json()["error"]["code"] == "INVALID_MODEL_OUTPUT"
    def fail(*args, **kwargs):
        raise RuntimeError("private path or stack")
    monkeypatch.setattr(main, "aggregate_renewable_power", fail)
    r = client.post("/estimate/renewable", json=renewable())
    assert r.status_code == 500 and "private" not in r.text


def test_loader_checksum_order_and_cache(tmp_path, monkeypatch):
    directory = tmp_path / "ml/artifacts"
    directory.mkdir(parents=True)
    path = directory / "wind_best_model.joblib"
    path.write_bytes(b"synthetic")
    metadata = {"feature_names": ["second", "first"], "experiment": "test", "target": "Power (MW)",
                "result_hashes": {"ml/artifacts/wind_best_model.joblib": hashlib.sha256(b"synthetic").hexdigest()}}
    (directory / "wind_best_model_metadata.json").write_text(json.dumps(metadata))
    model = Predictor(5)
    model.feature_names_in_ = ["second", "first"]
    calls = []
    def load(path):
        calls.append(path)
        return model
    monkeypatch.setattr("backend.app.model_loader.joblib.load", load)
    store = ModelStore(tmp_path)
    assert store.estimate("wind", features()["features"])["wind_power_mw"] == 5
    store.info("wind")
    assert len(calls) == 1
    path.write_bytes(b"changed")
    assert ModelStore(tmp_path).info("wind")["availability"] == "UNAVAILABLE"
