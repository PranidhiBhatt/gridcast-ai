"""Small synthetic decision-support tests using the real Milestone 6 contract."""

import copy
import json

import pytest

from ml.services.grid_intelligence import analyze_grid
from ml.services.renewable_aggregator import aggregate_renewable_power

TIME = "2020-01-01T12:00:00+05:30"


def supply(wind=30, solar=10):
    return aggregate_renewable_power(TIME, wind, solar)


@pytest.mark.parametrize("demand,status,gap,percentage,action", [
    (20, "SURPLUS", 20, 100, "Consider storage charging"),
    (40, "BALANCED", 0, 0, "Continue monitoring supply and demand"),
    (50, "DEFICIT", -10, -20, "Consider storage discharge"),
])
def test_calculations_recommendations_and_determinism(demand, status, gap, percentage, action):
    source = supply()
    original = copy.deepcopy(source)
    r = analyze_grid(source, demand)
    assert r == analyze_grid(source, demand)
    assert source == original
    assert r["grid_status"] == status and r["analysis_status"] == "COMPLETE"
    assert r["supply_gap_mw"] == gap and r["supply_gap_percentage"] == percentage
    assert action in [x["action"] for x in r["recommendations"]]
    assert all(x["reason"] for x in r["recommendations"])
    assert status in r["explanation"]
    assert r["timestamp"] is source["timestamp"]
    json.dumps(r, allow_nan=False)


@pytest.mark.parametrize("gap,status", [(-1.01, "DEFICIT"), (-1, "BALANCED"), (1, "BALANCED"), (1.01, "SURPLUS")])
def test_symmetric_inclusive_boundaries(gap, status):
    assert analyze_grid(supply(10 + gap, 0), 10)["grid_status"] == status
    assert analyze_grid(supply(10 + gap, 0), 10, balance_tolerance_mw=2)["grid_status"] == "BALANCED"


@pytest.mark.parametrize("generation,demand,status,gap,percentage", [
    (0, 0, "BALANCED", 0, None), (0.5, 0, "BALANCED", 0.5, None),
    (2, 0, "SURPLUS", 2, None), (0, 5, "DEFICIT", -5, -100),
])
def test_zero_policies(generation, demand, status, gap, percentage):
    r = analyze_grid(supply(generation, 0), demand)
    assert (r["grid_status"], r["supply_gap_mw"], r["supply_gap_percentage"]) == (status, gap, percentage)
    json.dumps(r, allow_nan=False)
    assert analyze_grid(supply(0.5, 0), 0, balance_tolerance_mw=0)["grid_status"] == "SURPLUS"


@pytest.mark.parametrize("wind,solar", [(None, 5), (5, None), (None, None)])
def test_incomplete_supply(wind, solar):
    r = analyze_grid(supply(wind, solar), 20)
    assert r["analysis_status"] == "UNAVAILABLE"
    assert r["aggregation_status"] == ("UNAVAILABLE" if wind is solar is None else "PARTIAL")
    assert all(r[k] is None for k in ("renewable_supply_mw", "grid_status", "supply_gap_mw", "supply_gap_percentage"))
    assert r["recommendations"] == []


@pytest.mark.parametrize("bad", [-1, float("nan"), float("inf"), -float("inf"), "5", True, None])
def test_invalid_demand_and_tolerance(bad):
    with pytest.raises(ValueError):
        analyze_grid(supply(), bad)
    with pytest.raises(ValueError):
        analyze_grid(supply(None, None), bad)
    with pytest.raises(ValueError):
        analyze_grid(supply(), 10, balance_tolerance_mw=bad)


@pytest.mark.parametrize("field,value", [("aggregation_status", "PARTIAL"), ("total_renewable_power_mw", 999),
    ("total_renewable_power_mw", True), ("wind_power_mw", -1), ("available_sources", []), ("missing_sources", ["solar"])])
def test_inconsistent_records_rejected(field, value):
    r = supply()
    r[field] = value
    with pytest.raises(ValueError):
        analyze_grid(r, 10)


def test_missing_contract_and_overflow():
    for bad in [{}, None, {"aggregation_status": "COMPLETE"}]:
        with pytest.raises(ValueError):
            analyze_grid(bad, 10)
    with pytest.raises(ValueError, match="finite"):
        analyze_grid(supply(1e308, 0), 1e-308)
