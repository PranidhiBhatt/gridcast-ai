"""Synthetic solar model contract and chronology checks; no downloaded data needed."""

import copy
import json

import joblib
import numpy as np
import pandas as pd
import pytest
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from ml.data_processing.run_wind_analysis import sha256
from ml.models.solar_baseline import (
    RF_CONFIG, calculate_metrics, create_models, diagnostics, forest_importance,
    load_contract, load_dataset, model_parameters, ordered_features, power_boundaries,
    power_groups, select_model, split_dataset, validate_contract, validate_dataset,
)
from ml.training.train_solar_baseline import build_metadata


@pytest.fixture
def fixture(tmp_path):
    times = pd.DatetimeIndex([*pd.date_range("2019-12-01", periods=16, freq="15min"),
                              *pd.date_range("2020-01-01", periods=8, freq="15min"),
                              *pd.date_range("2020-07-01", periods=8, freq="15min")])
    weather = np.arange(32, dtype=float) % 9
    data = pd.DataFrame({"timestamp": times, "Irradiance (W/m2)": weather,
                         "hour": times.hour, "Power (MW)": np.maximum(0, 2*weather-3)})
    csv = tmp_path / "data.csv"
    data.to_csv(csv, index=False)
    boundaries = {"train": ("2019-01-01", "2020-01-01"),
                  "validation": ("2020-01-01", "2020-07-01"), "test": ("2020-07-01", "2021-01-01")}
    splits = {}
    for name, (start, end) in boundaries.items():
        t = times[(times >= start) & (times < end)]
        splits[name] = {"boundary_start_inclusive": start, "boundary_end_exclusive": end,
                        "rows": len(t), "start": str(t.min()), "end": str(t.max()), "percent": 100*len(t)/len(times)}
    m = {"features": ["Irradiance (W/m2)", "hour"], "original_features": ["Irradiance (W/m2)"], "engineered_features": ["hour"],
         "target_column": "Power (MW)", "timestamp_column": "timestamp", "excluded_features": {"humidity": "unresolved"},
         "feature_review": {"Irradiance (W/m2)": {"included": True, "source_column": "Irradiance (W/m2)", "category": "irradiance"},
                            "hour": {"included": True, "source_column": "timestamp", "category": "calendar"}},
         "audit": {"splits": splits}, "output": {"path": "data.csv", "rows": 32, "columns": 4, "sha256": sha256(csv)},
         "source": "synthetic", "policy_version": "synthetic-v1"}
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(m))
    return data, load_contract(manifest), csv


def test_loading_validation_and_zero_preservation(fixture):
    data, contract, path = fixture
    loaded = load_dataset(path, contract)
    assert len(loaded) == 32
    assert loaded[contract["target"]].eq(0).sum() == data[contract["target"]].eq(0).sum()
    path.write_text("corrupted")
    with pytest.raises(ValueError, match="SHA-256"):
        load_dataset(path, contract)


def test_feature_order_and_invalid_schema(fixture):
    data, c, _ = fixture
    assert list(ordered_features(data.iloc[:, ::-1], c)) == c["features"]
    for bad in [data.iloc[:, ::-1], data.drop(columns=c["target"]), data.assign(future_power=1)]:
        with pytest.raises(ValueError, match="schema"):
            validate_dataset(bad, c)
    bad = data.copy()
    bad.loc[0, c["features"][0]] = np.nan
    with pytest.raises(ValueError, match="non-finite"):
        validate_dataset(bad, c)
    bad = data.copy()
    bad[c["features"][0]] = bad[c["target"]]
    with pytest.raises(ValueError, match="target-copy"):
        validate_dataset(bad, c)


def test_contract_role_conflicts_and_lineage(fixture):
    _, c, _ = fixture
    for forbidden in [c["target"], c["timestamp"], "humidity"]:
        bad = copy.deepcopy(c)
        bad["features"].append(forbidden)
        bad["manifest"]["original_features"].append(forbidden)
        with pytest.raises(ValueError):
            validate_contract(bad)
    bad = copy.deepcopy(c)
    bad["manifest"]["feature_review"]["hour"]["source_column"] = c["target"]
    with pytest.raises(ValueError, match="lineage"):
        validate_contract(bad)


def test_chronological_split_integrity(fixture):
    data, c, _ = fixture
    parts = split_dataset(data, c)
    assert [len(p) for p in parts.values()] == [16, 8, 8]
    sets = [set(p[c["timestamp"]]) for p in parts.values()]
    assert not sets[0] & sets[1] and not sets[0] & sets[2] and not sets[1] & sets[2]
    assert max(sets[0]) < min(sets[1]) and max(sets[1]) < min(sets[2])
    with pytest.raises(ValueError, match="chronologically"):
        split_dataset(data.iloc[::-1], c)
    bad = copy.deepcopy(c)
    bad["splits"]["test"]["boundary_start_inclusive"] = "2020-06-01"
    with pytest.raises(ValueError, match="overlap"):
        split_dataset(data, bad)


def test_training_only_dummy_scaler_and_predictions(fixture, tmp_path):
    data, c, _ = fixture
    train = split_dataset(data, c)["train"]
    models = create_models()
    X, y = ordered_features(train, c), train[c["target"]]
    for model in models.values():
        model.fit(X, y)
        assert np.isfinite(model.predict(X)).all()
    assert models["dummy"].constant_[0, 0] == pytest.approx(y.mean())
    assert models["dummy"].constant_[0, 0] != pytest.approx(data[c["target"]].mean())
    assert np.allclose(models["linear_regression"].named_steps["scaler"].mean_, X.mean())
    assert models["random_forest"].random_state == RF_CONFIG["random_state"] == 42
    imp = forest_importance(models["random_forest"], c["features"])
    assert sum(r["importance"] for r in imp) == pytest.approx(1)
    assert [r["importance"] for r in imp] == sorted([r["importance"] for r in imp], reverse=True)
    path = tmp_path / "linear.joblib"
    joblib.dump(models["linear_regression"], path)
    assert np.array_equal(joblib.load(path).predict(X), models["linear_regression"].predict(X))


def test_standard_metrics_and_empty_groups():
    y, p = np.array([0., 2., 6.]), np.array([1., 3., 5.])
    m = calculate_metrics(y, p)
    assert m["mae_mw"] == mean_absolute_error(y, p)
    assert m["rmse_mw"] == np.sqrt(mean_squared_error(y, p))
    assert m["r2"] == r2_score(y, p)
    assert calculate_metrics([], [])["mae_mw"] is None
    with pytest.raises(ValueError, match="finite"):
        calculate_metrics([np.nan], [1])


def test_selection_priorities_and_test_rejection():
    def m(mae, rmse, r2):
        return {"rows": 10, "mae_mw": mae, "rmse_mw": rmse, "r2": r2}
    assert select_model({"a": m(1, 5, .1), "b": m(2, 2, .9)}) == "a"
    assert select_model({"a": m(1, 3, .9), "b": m(1, 2, .1)}) == "b"
    assert select_model({"a": m(1, 2, .8), "b": m(1, 2, .9)}) == "b"
    with pytest.raises(ValueError, match="test"):
        select_model({"a": {**m(1, 2, .9), "test": {"mae_mw": 0}}})


def test_training_quantile_bins_and_diagnostics():
    bounds = power_boundaries(pd.Series([0, 1, 2, 3, 4, 5, 6]))
    assert bounds == pytest.approx([8/3, 13/3])
    y = pd.Series([0., 1., 4., 100.])
    assert power_groups(y, bounds).tolist() == ["zero", "low positive", "medium positive", "high positive"]
    frame = pd.DataFrame({"timestamp": pd.date_range("2020-07-01", periods=4, freq="h"),
                          "actual_power_mw": y, "predicted_power_mw": [1., 1., 3., 90.], "residual_mw": [-1., 0., 1., 10.]})
    d = diagnostics(frame, bounds)
    assert sum(r["rows"] for r in d["zero_positive"]) == 4
    assert sum(r["rows"] for r in d["power_ranges"]) == 4
    assert d["residual"]["overpredictions"] == 1
    assert d["residual"]["underpredictions"] == 2


def test_metadata_generation_reproducible(fixture):
    _, c, _ = fixture
    scores = {"dummy": {s: calculate_metrics([0., 1.], [.5, .5]) for s in ("train", "validation", "test")}}
    params = model_parameters(create_models())
    first = build_metadata(c, "dummy", params, scores)
    second = build_metadata(c, "dummy", params, scores)
    assert json.dumps(first, sort_keys=True) == json.dumps(second, sort_keys=True)
    assert first["feature_order"] == c["features"]
    assert "not true future forecasting" in first["task"]
