"""Synthetic impact scenarios; no datasets, model loading or external services."""

import json

import pytest

from ml.services.impact_engine import ImpactAssumptions, estimate_grid_impact, estimate_impact
from ml.services.grid_intelligence import analyze_grid
from ml.services.renewable_aggregator import aggregate_renewable_power

TIME = "2020-01-01T12:00:00+05:30"


def test_energy_factors_interval_and_timestamp():
    r = estimate_impact(40, 0.25, timestamp=TIME)
    assert r["renewable_energy_mwh"] == 10
    assert r["estimated_avoided_emissions_kg_co2"] == 5000
    assert r["estimated_avoided_generation_cost"] == 500
    assert r["timestamp"] is TIME
    assert r["assumptions_used"]["interval_hours"] == 0.25
    assert "Illustrative" in r["assumptions_used"]["factor_basis"]
    assert r["renewable_demand_coverage_percentage"] is None
    assert r["potential_surplus_mw"] is None
    with pytest.raises(TypeError):
        estimate_impact(40)


def test_custom_and_zero_factors():
    factors = ImpactAssumptions(200, 30, "scenario units", "Synthetic test assumptions")
    r = estimate_impact(10, 2, assumptions=factors)
    assert r["estimated_avoided_emissions_kg_co2"] == 4000
    assert r["estimated_avoided_generation_cost"] == 600
    assert r["assumptions_used"]["emission_factor_kg_co2_per_mwh"] == 200
    assert r["currency_unit"] == "scenario units"
    assert estimate_impact(10, 2, assumptions=ImpactAssumptions(0, 0))["estimated_avoided_generation_cost"] == 0


@pytest.mark.parametrize("power,demand,coverage,surplus,status", [
    (40, 20, 100, 20, "SURPLUS"), (40, 40, 100, 0, "BALANCED"),
    (20, 40, 50, 0, "DEFICIT"), (20, 0, None, 20, "SURPLUS"), (0, 0, None, 0, "BALANCED"),
    (0, 20, 0, 0, "DEFICIT"), (20.5, 20, 100, 0.5, "BALANCED"),
])
def test_grid_context_and_coverage(power, demand, coverage, surplus, status):
    grid = analyze_grid(aggregate_renewable_power(TIME, power, 0), demand)
    r = estimate_grid_impact(grid, 0.5)
    assert r["renewable_demand_coverage_percentage"] == coverage
    assert r["potential_surplus_mw"] == surplus
    assert r["grid_status"] == status and r["grid_context"]
    assert r["renewable_energy_mwh"] == power * 0.5
    assert r["timestamp"] is TIME
    json.dumps(r, allow_nan=False)


@pytest.mark.parametrize("bad", [-1, float("nan"), float("inf"), -float("inf"), "2", True])
def test_invalid_numeric_inputs_and_assumptions(bad):
    for kwargs in ({"renewable_power_mw": bad, "interval_hours": 1},
                   {"renewable_power_mw": 1, "interval_hours": bad},
                   {"renewable_power_mw": 1, "interval_hours": 1, "demand_mw": bad}):
        with pytest.raises(ValueError):
            estimate_impact(**kwargs)
    with pytest.raises(ValueError):
        ImpactAssumptions(emission_factor_kg_co2_per_mwh=bad)
    with pytest.raises(ValueError):
        ImpactAssumptions(avoided_generation_cost_per_mwh=bad)


def test_zero_interval_and_overflow():
    with pytest.raises(ValueError):
        estimate_impact(1, 0)
    with pytest.raises(ValueError):
        estimate_impact(1, None)
    for power, interval in [(1e308, 10), (1e306, 1)]:
        with pytest.raises(ValueError, match="finite"):
            estimate_impact(power, interval)


@pytest.mark.parametrize("wind,solar", [(None, 10), (10, None), (None, None)])
def test_unavailable_no_fabrication(wind, solar):
    grid = analyze_grid(aggregate_renewable_power(TIME, wind, solar), 20)
    r = estimate_grid_impact(grid, 0.25)
    assert r["impact_status"] == "UNAVAILABLE"
    for key in ("renewable_energy_mwh", "estimated_avoided_emissions_kg_co2",
                "estimated_avoided_generation_cost", "renewable_demand_coverage_percentage", "potential_surplus_mw"):
        assert r[key] is None
    assert estimate_impact(None, 1)["impact_status"] == "UNAVAILABLE"


def test_inconsistent_grid_input():
    grid = analyze_grid(aggregate_renewable_power(TIME, 30, 10), 20)
    for key, value in [("grid_status", "DEFICIT"), ("supply_gap_mw", 999), ("analysis_status", "UNAVAILABLE")]:
        with pytest.raises(ValueError):
            estimate_grid_impact({**grid, key: value}, 1)
    with pytest.raises(ValueError):
        estimate_grid_impact({}, 1)
