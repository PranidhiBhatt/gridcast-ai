"""Inexpensive static delivery checks; no browser automation or model training."""

from fastapi.testclient import TestClient

from backend.app.main import app
from backend.app.schemas import AnalyzeRequest


def test_dashboard_assets_and_existing_contracts():
    with TestClient(app) as client:
        page = client.get("/")
        assert page.status_code == 200 and "text/html" in page.headers["content-type"]
        assert "Run Grid Analysis" in page.text and 'id="analysis-form"' in page.text
        for path, kind in [("styles.css", "text/css"), ("app.js", "javascript"), ("example.json", "application/json")]:
            asset = client.get("/static/" + path)
            assert asset.status_code == 200 and kind in asset.headers["content-type"]
        sample = client.get("/static/example.json").json()
        request = AnalyzeRequest.model_validate(sample)
        assert len(request.wind.features) == 25 and len(request.solar.features) == 14
        assert request.impact.interval_hours == 0.25
        assert client.get("/health").json() == {"status": "ok", "service": "GridCast AI"}
        schema = client.get("/openapi.json").json()
        expected = {"/health", "/estimate/wind", "/estimate/solar", "/estimate/renewable", "/grid/analyze",
                    "/impact/analyze", "/analyze", "/model/info", "/project/status"}
        assert set(schema["paths"]) == expected
        assert set(schema["components"]["schemas"]["AnalyzeRequest"]["required"]) == {"timestamp", "wind", "solar", "grid", "impact"}
