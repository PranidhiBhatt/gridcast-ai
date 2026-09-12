# Economic and Environmental Impact Estimation

## Purpose and physical basis

Milestone 8 calculates transparent scenarios, not measurements. Power in MW is
not energy in MWh: an explicit positive `interval_hours` is required, without a
one-hour default. Power is assumed representative and constant over that interval.
An instantaneous prediction alone does not verify the interval's generated energy.

## Input contract

`ml.services.impact_engine.estimate_impact(renewable_power_mw, interval_hours)`
accepts optional `demand_mw`, `timestamp` and `ImpactAssumptions`. Numeric power,
demand and factors must be finite, real and non-negative; duration must be finite
and strictly positive. Booleans, numeric strings and invalid numbers fail with
ValueError, as do calculated overflows. No clipping or filling occurs.

None power means unavailable and produces null energy/impact/coverage/surplus.
Zero power is valid and produces zero energy and impacts. COMPLETE means the core
scenario can be calculated, not that optional demand context or real-world
displacement is known. Invalid duration still fails when power is unavailable.

`estimate_grid_impact(grid_result, interval_hours)` adapts actual Milestone 7 fields:
`renewable_supply_mw`, `demand_mw`, `supply_gap_mw`, `grid_status`, `analysis_status`,
`aggregation_status`, `balance_tolerance_mw`, and optional timestamp. It rejects
inconsistent status/gap/classification. PARTIAL or UNAVAILABLE aggregation with
UNAVAILABLE analysis remains unavailable; it does not recover a partial total.
Timestamp is preserved without timezone conversion. Direct estimates without grid
context return a null grid status rather than inventing one.

## Formulas

- `renewable_energy_mwh = renewable_power_mw * interval_hours`
- `estimated_avoided_emissions_kg_co2 = renewable_energy_mwh * emission_factor_kg_co2_per_mwh`
- `estimated_avoided_generation_cost = renewable_energy_mwh * avoided_generation_cost_per_mwh`

## Explicit assumptions

No factors are established by the inspected Milestone 6/7 contracts. Defaults are
illustrative, unsourced and not country-specific:

| Assumption | Default |
|---|---|
| Displaced emission factor | 500 kg CO₂/MWh |
| Avoided conventional generation cost | 50 generic currency units/MWh |
| Currency label | generic currency units (not INR, USD or a tariff) |

`ImpactAssumptions` is an immutable dataclass. Both factors, currency label and
`factor_basis` can be supplied explicitly; zero factors are allowed. Replace
defaults with appropriate sourced scenario factors for real-world evaluation.
Outputs echo factors, labels, interval, energy basis and displacement assumption.

**The scenario assumes all calculated renewable energy displaces conventional
generation at the supplied factors, including potential surplus.** It does not
establish that the energy was used, exported, stored or displaced fossil output.
Demand is context, not a cap on energy used in these scenario formulas. This is
not a claim of 100% actual utilisation. Unknown utilisation, curtailment and
displacement can make actual impact much lower, including zero.

## Demand coverage and potential surplus

For known power and positive demand, coverage is
`min(power, demand) / demand * 100`: percentage of reported demand covered by
available renewable supply in this arithmetic comparison. It is not measured grid
utilisation. Unknown/zero demand yields null coverage.

For known power and demand, `potential_surplus_mw = max(power - demand, 0)`.
Unknown demand yields null surplus. Surplus is not measured curtailment. A small
positive surplus can coexist with Milestone 7 BALANCED because its tolerance is
inclusive. SURPLUS context mentions possible storage/export; DEFICIT indicates
renewable shortfall; BALANCED references the supplied tolerance. No money is
assigned to these opportunities or shortfalls.

## Output and example

Results contain timestamp, power, explicit duration, MWh energy, estimated cost
and emissions, both factors, currency label, coverage, potential surplus, grid
status, impact status, assumptions_used and limitations. The grid adapter also
preserves aggregation/analysis statuses and adds descriptive grid_context.
Unavailable quantities are None (JSON null); datetime serialization is the caller's
responsibility.

```python
from ml.services.impact_engine import estimate_impact

result = estimate_impact(40, interval_hours=0.25, demand_mw=50)
assert result["renewable_energy_mwh"] == 10
assert result["estimated_avoided_emissions_kg_co2"] == 5000
assert result["estimated_avoided_generation_cost"] == 500
assert result["renewable_demand_coverage_percentage"] == 80
```

## Limitations and exclusions

Economic and environmental outputs are assumption-driven estimates. They are not
actual electricity market savings, verified emissions reductions, live grid
measurements or carbon accounting records. No lifecycle/marginal emissions claim,
profit, tariff savings, storage/export revenue, import cost, financial curtailment
loss or actual curtailment is calculated. Measurement intervals, sites and units
must be aligned by callers. There are no live prices, APIs, model changes, grid
control, forecasting, database, dashboard or FastAPI endpoints in this milestone.
