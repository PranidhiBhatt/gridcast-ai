"""Deterministic renewable-versus-demand decision support; no dispatch execution."""

from __future__ import annotations

import math
from collections.abc import Mapping
from numbers import Real
from typing import Any

from ml.services.renewable_aggregator import aggregate_renewable_power

DEFAULT_BALANCE_TOLERANCE_MW = 1.0

RECOMMENDATIONS = {
    "SURPLUS": (
        ("Consider storage charging", "Excess renewable power could be stored if charging capacity is available."),
        ("Consider export or flexible loads", "Excess supply could serve other demand where interconnection and load flexibility permit."),
        ("Review conventional generation reduction", "Renewable surplus may permit reduction where operating constraints allow."),
    ),
    "BALANCED": (
        ("Maintain the current plan subject to operator review", "The calculated renewable-demand gap is within the configured tolerance."),
        ("Continue monitoring supply and demand", "Estimates and reported demand may change."),
    ),
    "DEFICIT": (
        ("Consider storage discharge", "Storage could cover some renewable shortfall if sufficient stored energy and discharge capacity exist."),
        ("Review available reserves or imports", "Other supply may cover the renewable shortfall where capacity and operating constraints permit."),
        ("Consider demand response", "Flexible demand reduction may reduce the renewable shortfall where permitted."),
    ),
}


def _nonnegative(value: Any, name: str) -> float:
    """Reject absent, non-real, non-finite or negative values without correction."""
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{name} must be a finite non-negative number")
    try:
        number = float(value)
    except (OverflowError, ValueError) as exc:
        raise ValueError(f"{name} must be finite") from exc
    if not math.isfinite(number) or number < 0:
        raise ValueError(f"{name} must be finite and non-negative")
    return number


def analyze_grid(renewable_result: Mapping[str, Any], demand_mw: Real, *,
                 balance_tolerance_mw: Real = DEFAULT_BALANCE_TOLERANCE_MW) -> dict[str, Any]:
    """Compare complete Milestone 6 supply with aligned reported demand in MW.

    Incomplete supply returns UNAVAILABLE analysis and no operational suggestions.
    Invalid input raises ValueError; zero demand yields a null gap percentage.
    Caller must verify demand time, units and portfolio scope match the supply.
    """
    demand = _nonnegative(demand_mw, "demand_mw")
    tolerance = _nonnegative(balance_tolerance_mw, "balance_tolerance_mw")
    required = {"timestamp", "wind_power_mw", "solar_power_mw", "total_renewable_power_mw",
                "aggregation_status", "available_sources", "missing_sources"}
    if not isinstance(renewable_result, Mapping) or not required.issubset(renewable_result):
        raise ValueError("Expected Milestone 6 aggregation result with source values, total, status and source lists")
    # Reuse existing validation without changing or repairing the supplied record.
    expected = aggregate_renewable_power(renewable_result["timestamp"],
                                        renewable_result["wind_power_mw"], renewable_result["solar_power_mw"])
    total = renewable_result["total_renewable_power_mw"]
    if total is not None:
        _nonnegative(total, "total_renewable_power_mw")
    for key in ("aggregation_status", "total_renewable_power_mw", "available_sources", "missing_sources"):
        if renewable_result[key] != expected[key]:
            raise ValueError(f"Inconsistent Milestone 6 aggregation field: {key}")
    aggregation_status = expected["aggregation_status"]
    result = {"timestamp": renewable_result["timestamp"], "renewable_supply_mw": expected["total_renewable_power_mw"],
              "demand_mw": demand, "supply_gap_mw": None, "supply_gap_percentage": None,
              "grid_status": None, "analysis_status": "UNAVAILABLE", "recommendations": [],
              "explanation": f"Renewable aggregation is {aggregation_status}; complete supply is unavailable. No gap or grid classification calculated.",
              "aggregation_status": aggregation_status, "balance_tolerance_mw": tolerance}
    if aggregation_status != "COMPLETE":
        return result
    supply = expected["total_renewable_power_mw"]
    gap = supply - demand
    percentage = (gap / demand) * 100 if demand > 0 else None
    if percentage is not None and not math.isfinite(percentage):
        raise ValueError("Supply gap percentage exceeds finite representation")
    status = "BALANCED" if abs(gap) <= tolerance else "SURPLUS" if gap > tolerance else "DEFICIT"
    explanation = (f"Renewable supply {supply:g} MW minus reported demand {demand:g} MW gives a gap of {gap:g} MW. "
                   f"The symmetric ±{tolerance:g} MW balance rule classifies this as {status}. "
                   "Recommendations are conditional decision support, not executed actions.")
    if demand == 0:
        explanation += " Gap percentage is unavailable because reported demand is zero."
    result.update(supply_gap_mw=gap, supply_gap_percentage=percentage, grid_status=status,
                  analysis_status="COMPLETE", explanation=explanation,
                  recommendations=[{"action": action, "reason": reason} for action, reason in RECOMMENDATIONS[status]])
    return result
