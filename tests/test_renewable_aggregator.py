"""Synthetic aggregation tests; no datasets or model loading."""

from datetime import datetime, timezone
import json

import pytest

from ml.services.renewable_aggregator import aggregate_renewable_power, load_selected_model_names

TIME = "2020-01-01T12:00:00+05:30"


def test_complete_total_and_mix():
    result = aggregate_renewable_power(TIME, 30, 10, wind_model_name="wind")
    assert result["total_renewable_power_mw"] == 40
    assert result["wind_mix_percentage"] == 75
    assert result["solar_mix_percentage"] == 25
    assert result["aggregation_status"] == "COMPLETE"
    assert result["available_sources"] == ["wind", "solar"]
    assert result["missing_sources"] == []
    assert result["wind_model_name"] == "wind"
    assert "solar_model_name" not in result


@pytest.mark.parametrize("wind,solar,status,available,missing", [
    (0, 0, "COMPLETE", ["wind", "solar"], []),
    (0, None, "PARTIAL", ["wind"], ["solar"]),
    (None, 12, "PARTIAL", ["solar"], ["wind"]),
    (None, None, "UNAVAILABLE", [], ["wind", "solar"]),
])
def test_zero_and_missing_policy(wind, solar, status, available, missing):
    r = aggregate_renewable_power(TIME, wind, solar)
    assert r["aggregation_status"] == status
    assert r["wind_power_mw"] == wind and r["solar_power_mw"] == solar
    assert r["available_sources"] == available and r["missing_sources"] == missing
    assert r["total_renewable_power_mw"] == (0 if status == "COMPLETE" else None)
    assert r["wind_mix_percentage"] is None and r["solar_mix_percentage"] is None


@pytest.mark.parametrize("bad", [-1, "3", True, float("nan"), float("inf"), -float("inf"), complex(1, 2)])
@pytest.mark.parametrize("source", ["wind", "solar"])
def test_invalid_power(bad, source):
    with pytest.raises(ValueError):
        aggregate_renewable_power(TIME, bad if source == "wind" else 1, bad if source == "solar" else 1)


@pytest.mark.parametrize("timestamp", [TIME, datetime(2020, 1, 1, tzinfo=timezone.utc)])
def test_timestamp_preserved(timestamp):
    assert aggregate_renewable_power(timestamp, 1, 2)["timestamp"] is timestamp


def test_units_timestamp_and_overflow_validation():
    for unit in ["kW", "MWh", None]:
        with pytest.raises(ValueError, match="units"):
            aggregate_renewable_power(TIME, 1, 2, wind_unit=unit)
    for timestamp in [None, 123, "not a date"]:
        with pytest.raises(ValueError, match="timestamp"):
            aggregate_renewable_power(timestamp, 1, 2)
    with pytest.raises(ValueError, match="overflows"):
        aggregate_renewable_power(TIME, 1e308, 1e308)
    assert aggregate_renewable_power(TIME, 1e307, 1e307)["wind_mix_percentage"] == 50


def test_metadata_optional_and_malformed(tmp_path):
    assert load_selected_model_names(tmp_path) == {}
    (tmp_path / "wind_best_model_metadata.json").write_text(json.dumps({"model_type": "ExampleWind"}))
    solar = tmp_path / "solar_best_model_metadata.json"
    solar.write_text(json.dumps({"selected_model": "example_solar"}))
    names = load_selected_model_names(tmp_path)
    assert names == {"wind_model_name": "ExampleWind", "solar_model_name": "example_solar"}
    assert aggregate_renewable_power(TIME, None, None, **names)["aggregation_status"] == "UNAVAILABLE"
    for malformed in ["{", "[]", '{}']:
        solar.write_text(malformed)
        with pytest.raises(ValueError, match="metadata"):
            load_selected_model_names(tmp_path)
