# Rule-based Grid Intelligence

## Purpose and inputs

Milestone 7 provides explainable decision support comparing renewable estimates
with reported demand. `ml.services.grid_intelligence.analyze_grid` accepts the
Milestone 6 aggregation dictionary and `demand_mw`, plus optional
`balance_tolerance_mw` (default **1.0 MW**). No models are loaded or trained.

Required aggregation fields are `timestamp`, `wind_power_mw`, `solar_power_mw`,
`total_renewable_power_mw`, `aggregation_status`, `available_sources` and
`missing_sources`. Mix percentages and model labels do not influence analysis.
The original timestamp is preserved. Caller must verify demand is in MW and
shares supply's time basis, measurement interval and portfolio scope.

## Validation

Demand and tolerance must be finite, non-negative real numbers. None, booleans,
numeric strings, negative numbers, NaN and infinity raise `ValueError`.
Source values and timestamp reuse Milestone 6 validation. Source lists, status
and total must agree with those values; inconsistent records are rejected rather
than repaired. There is no clipping, filling, unit conversion or input mutation.
Percentages that overflow finite floating-point representation also raise
`ValueError`, so no successful result contains calculated NaN or infinity.

## Calculations and classification

For COMPLETE aggregation:

- `supply_gap_mw = total_renewable_power_mw - demand_mw`.
- When demand > 0, `supply_gap_percentage = supply_gap_mw / demand_mw * 100`.
- `abs(gap) <= balance_tolerance_mw`: **BALANCED** (inclusive boundaries).
- `gap > balance_tolerance_mw`: **SURPLUS**.
- `gap < -balance_tolerance_mw`: **DEFICIT**.

The default absolute 1 MW tolerance is a simple demonstration setting, not a
validated grid operating limit. It is symmetric and configurable per call;
zero tolerance requires exact equality for BALANCED. No hidden relative tolerance
or rounding is used to classify values. Returned gaps retain their actual sign
even when classified BALANCED.

## Recommendation policy

Fixed rules return dictionaries with `action` and `reason`:

| Grid status | Conditional recommendations |
|---|---|
| SURPLUS | Consider charging storage, exports/flexible loads, and feasible conventional generation reduction |
| BALANCED | Maintain the current plan subject to operator review; continue monitoring |
| DEFICIT | Consider storage discharge, available reserves/imports, and demand response |

These are options for review, not instructions executed by the component. Storage
state, network capacity, reserves and operating constraints are not known. The
explanation separates calculated gap, tolerance-based classification and advice.
No LLM or external API produces the recommendations.

## Partial/unavailable policy

Both PARTIAL and UNAVAILABLE aggregation produce `analysis_status=UNAVAILABLE`,
`grid_status=None`, null supply/gap/percentage, an empty recommendation list and
an explanation. `aggregation_status` preserves the distinction between partial
and wholly unavailable supply. Missing generation never becomes zero. Invalid
demand still fails validation even if supply is unavailable.

## Zero demand

With complete supply and zero demand, the gap equals supply and percentage is
None. The same absolute tolerance applies: zero supply is BALANCED; positive
supply up to and including tolerance is BALANCED; supply above it is SURPLUS.
No division by zero occurs.

## Output and example

The result contains `timestamp`, `renewable_supply_mw`, `demand_mw`,
`supply_gap_mw`, `supply_gap_percentage`, `grid_status`, `analysis_status`,
`recommendations`, `explanation`, `aggregation_status` and `balance_tolerance_mw`.
Analysis status describes data availability; grid status describes the rule's
classification. Python None corresponds to JSON null. Datetime timestamps need
caller serialization, as in Milestone 6.

```python
from ml.services.renewable_aggregator import aggregate_renewable_power
from ml.services.grid_intelligence import analyze_grid

supply = aggregate_renewable_power("2020-01-01T12:00:00+00:00", 30, 10)
result = analyze_grid(supply, demand_mw=50)
assert result["grid_status"] == "DEFICIT"
assert result["supply_gap_mw"] == -10
assert result["supply_gap_percentage"] == -20
```

## Limitations

This is an explainable decision-support component. It does NOT control the grid,
execute dispatch, guarantee operational safety, replace grid operators or
integrate with real grid infrastructure. Renewable-versus-demand DEFICIT means a
renewable shortfall, not proof of a total-grid shortage: conventional supply,
imports, storage, losses and network constraints are not part of this calculation.
BALANCED does not establish frequency stability or adequate reserves. Existing
estimates use contemporaneous weather and do not establish future forecasting.
No demand forecasting, economic/environmental calculations, API or UI is added.
