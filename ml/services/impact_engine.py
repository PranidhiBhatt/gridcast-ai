"""Assumption-driven impact scenarios, not measured savings or carbon accounting."""

from __future__ import annotations

import math
from collections.abc import Mapping
from dataclasses import asdict, dataclass
from datetime import datetime
from numbers import Real
from typing import Any

from ml.services.grid_intelligence import _nonnegative


@dataclass(frozen=True)
class ImpactAssumptions:
    """Illustrative factors; replace with sourced factors for the intended scenario."""

    emission_factor_kg_co2_per_mwh: float = 500.0
    avoided_generation_cost_per_mwh: float = 50.0
    currency_unit: str = "generic currency units"
    factor_basis: str = "Illustrative, unsourced scenario factors; not location-specific"

    def __post_init__(self) -> None:
        for field in ("emission_factor_kg_co2_per_mwh", "avoided_generation_cost_per_mwh"):
            object.__setattr__(self, field, _nonnegative(getattr(self, field), field))
        for field in ("currency_unit", "factor_basis"):
            if not isinstance(getattr(self, field), str) or not getattr(self, field).strip():
                raise ValueError(f"{field} must be a nonempty string")


LIMITATIONS = (
    "Calculated scenario estimates, not real-world measurements, market savings, profit or carbon accounting records.",
    "Power is assumed representative of the entire explicit interval; no time-series integration is performed.",
    "All calculated renewable energy is assumed to displace conventional generation at the supplied factors, including potential surplus; actual use and displacement are unverified.",
    "No verified marginal emissions, lifecycle accounting, losses, storage/export revenue or curtailment measurement.",
)


def estimate_impact(renewable_power_mw: float | None, interval_hours: float, *,
                    demand_mw: float | None = None, timestamp: str | datetime | None = None,
                    assumptions: ImpactAssumptions = ImpactAssumptions()) -> dict[str, Any]:
    """Calculate a constant-power scenario; None power yields unavailable impacts.

    Demand is optional context, not a cap on displacement. COMPLETE describes the
    core estimate's availability, not operational utilisation or optional context.
    """
    interval = _nonnegative(interval_hours, "interval_hours")
    if interval == 0:
        raise ValueError("interval_hours must be greater than zero")
    if not isinstance(assumptions, ImpactAssumptions):
        raise ValueError("assumptions must be ImpactAssumptions")
    if timestamp is not None:
        if isinstance(timestamp, str):
            try:
                datetime.fromisoformat(timestamp)
            except ValueError as exc:
                raise ValueError("timestamp must be ISO-8601 or datetime") from exc
        elif not isinstance(timestamp, datetime):
            raise ValueError("timestamp must be ISO-8601 or datetime")
    power = None if renewable_power_mw is None else _nonnegative(renewable_power_mw, "renewable_power_mw")
    demand = None if demand_mw is None else _nonnegative(demand_mw, "demand_mw")
    energy = None if power is None else power * interval
    emissions = None if energy is None else energy * assumptions.emission_factor_kg_co2_per_mwh
    cost = None if energy is None else energy * assumptions.avoided_generation_cost_per_mwh
    if any(value is not None and not math.isfinite(value) for value in (energy, emissions, cost)):
        raise ValueError("Impact calculation exceeds finite representation")
    return {"timestamp": timestamp, "renewable_power_mw": power, "interval_hours": interval,
            "renewable_energy_mwh": energy, "estimated_avoided_emissions_kg_co2": emissions,
            "estimated_avoided_generation_cost": cost,
            "emission_factor_kg_co2_per_mwh": assumptions.emission_factor_kg_co2_per_mwh,
            "avoided_generation_cost_per_mwh": assumptions.avoided_generation_cost_per_mwh,
            "currency_unit": assumptions.currency_unit, "demand_mw": demand,
            "renewable_demand_coverage_percentage": min(power, demand) / demand * 100
                if power is not None and demand is not None and demand > 0 else None,
            "potential_surplus_mw": max(power - demand, 0.0) if power is not None and demand is not None else None,
            "grid_status": None, "impact_status": "UNAVAILABLE" if power is None else "COMPLETE",
            "assumptions_used": {**asdict(assumptions), "interval_hours": interval,
                "energy_basis": "Power held constant over the supplied interval",
                "displacement_basis": "All estimated energy hypothetically displaces conventional generation; not verified utilisation"},
            "limitations": list(LIMITATIONS), "grid_context": None}


def estimate_grid_impact(grid_result: Mapping[str, Any], interval_hours: float, *,
                         assumptions: ImpactAssumptions = ImpactAssumptions()) -> dict[str, Any]:
    """Adapt the actual Milestone 7 contract without loading models or fabricating supply."""
    required = {"renewable_supply_mw", "demand_mw", "supply_gap_mw", "grid_status",
                "analysis_status", "aggregation_status", "balance_tolerance_mw"}
    if not isinstance(grid_result, Mapping) or not required.issubset(grid_result):
        raise ValueError("Expected Milestone 7 result")
    g = grid_result
    demand = _nonnegative(g["demand_mw"], "demand_mw")
    tolerance = _nonnegative(g["balance_tolerance_mw"], "balance_tolerance_mw")
    if g["analysis_status"] == "COMPLETE" and g["aggregation_status"] == "COMPLETE":
        power = _nonnegative(g["renewable_supply_mw"], "renewable_supply_mw")
        gap = power - demand
        status = "BALANCED" if abs(gap) <= tolerance else "SURPLUS" if gap > tolerance else "DEFICIT"
        supplied_gap = g["supply_gap_mw"]
        # Signed gaps are validated by their magnitude, then checked against supply/demand.
        if isinstance(supplied_gap, bool) or not isinstance(supplied_gap, Real):
            raise ValueError("Invalid supply_gap_mw")
        try:
            _nonnegative(abs(supplied_gap), "supply_gap_mw magnitude")
        except TypeError as exc:
            raise ValueError("Invalid supply_gap_mw") from exc
        if supplied_gap != gap or g["grid_status"] != status:
            raise ValueError("Inconsistent Milestone 7 gap or classification")
    elif g["analysis_status"] == "UNAVAILABLE" and g["aggregation_status"] in ("PARTIAL", "UNAVAILABLE"):
        if any(g[key] is not None for key in ("renewable_supply_mw", "supply_gap_mw", "grid_status")):
            raise ValueError("Unavailable analysis must not carry complete supply or grid calculations")
        power = None
    else:
        raise ValueError("Inconsistent Milestone 7 availability statuses")
    result = estimate_impact(power, interval_hours, demand_mw=demand,
                             timestamp=g.get("timestamp"), assumptions=assumptions)
    contexts = {"SURPLUS": "Renewable surplus may present storage or export opportunities; no revenue is estimated.",
                "DEFICIT": "Available renewable supply does not fully meet reported demand.",
                "BALANCED": "Renewable supply is within the configured balance tolerance."}
    result.update(grid_status=g["grid_status"], aggregation_status=g["aggregation_status"],
                  analysis_status=g["analysis_status"], grid_context=contexts.get(g["grid_status"]))
    return result
