# Renewable Generation Aggregation

## Purpose

Milestone 6 combines already-produced wind and solar power estimates. It uses
only the Python standard library and does not load or train models.

## Input contract

`ml.services.renewable_aggregator.aggregate_renewable_power` requires `timestamp`,
`wind_power_mw` and `solar_power_mw`. Timestamp is an ISO-8601 string or Python
datetime, preserved exactly. Each power is a finite non-negative real number or
`None`. Zero is an available measurement. Booleans and numeric strings are rejected.

Optional `wind_unit` and `solar_unit` default to `MW`; any other declared unit is
rejected. No conversion occurs. Callers must verify the actual measurement units:
numeric values alone cannot establish them. Optional nonempty `wind_model_name`
and `solar_model_name` are labels only, independent of estimate availability.

Both estimates must already refer to the same time basis, compatible measurement
intervals and an explicitly intended portfolio. This scalar contract does not join
timestamps, verify site relationships or establish timezone compatibility.

## Output contract and statuses

The returned dictionary contains `timestamp`, `wind_power_mw`, `solar_power_mw`,
`total_renewable_power_mw`, `aggregation_status`, `available_sources`,
`missing_sources`, `wind_mix_percentage` and `solar_mix_percentage`.
Model-name keys appear only when supplied. Source lists use the order wind, solar.
Python `None` corresponds to JSON null; datetime inputs need caller serialization.

| Status | Available estimates | Total | Mix |
|---|---|---|---|
| COMPLETE | Both | Wind + solar | Percentages when total > 0 |
| PARTIAL | Exactly one | None | None |
| UNAVAILABLE | Neither | None | None |

## Complete behavior and renewable mix

The total is power in MW, not energy in MWh. For a positive complete total,
each percentage is `source / total * 100`. A complete zero total returns zero
power and null percentages. No division by zero occurs.

## Partial and unavailable behavior

Partial results retain the available source value explicitly and list the missing
source. They never present it as a complete total. Neither missing estimates nor
missing model artifacts are replaced with zero. If both estimates are None, both
sources are missing and the total is None. Model loading is the caller's concern.

## Validation rules

Invalid timestamps, nonnumeric values, booleans, NaN/infinity, negative estimates,
non-MW declarations and overflowing sums raise `ValueError`. No clipping, filling,
rounding policy or capacity normalization is applied. Models producing negative
estimates must have those outputs reviewed upstream rather than silently repaired.

## Existing model metadata

Inspected metadata and reports identify:

- Wind: `ml/artifacts/wind_best_model_metadata.json`, `experiment=B_hist_150`,
  `model_type=HistGradientBoostingRegressor`. The report identifies
  `ml/artifacts/wind_best_model.joblib`. Target is `Power (MW)`.
  Its ordered `feature_names` contains 25 predictors: four wind speeds (10 m,
  30 m, 50 m, hub), three measured directions (10 m, 30 m, 50 m), temperature,
  pressure, humidity, nine calendar predictors and six direction sine/cosine
  predictors. Exact names/order remain in that metadata.
- Solar: `ml/artifacts/solar_best_model_metadata.json`,
  `selected_model=extra_trees` (ExtraTreesRegressor),
  `model_path=ml/artifacts/solar_extra_trees.joblib`, target `Power (MW)`.
  Its ordered `feature_order` contains 14 predictors: total irradiance, DNI,
  GHI, temperature, pressure and nine calendar predictors.

`load_selected_model_names(Path("ml/artifacts"))` reads only the existing JSON
`model_type` (wind) and `selected_model` (solar) fields. Missing metadata files omit
the corresponding label; malformed files fail clearly. Metadata presence does
not prove an artifact is loadable or that an estimate is available. Aggregation
works without this helper or any metadata.

## Example

```python
from ml.services.renewable_aggregator import aggregate_renewable_power

result = aggregate_renewable_power("2020-01-01T12:00:00+00:00", 30.0, 10.0)
assert result["total_renewable_power_mw"] == 40.0
assert result["wind_mix_percentage"] == 75.0
assert result["aggregation_status"] == "COMPLETE"
```

## Limitations

This component aggregates generation estimates. It does not forecast weather,
forecast future generation, estimate demand, control the grid or make dispatch
decisions. Existing models use contemporaneous observed weather. Their datasets'
timezone, site relationship and some measurement semantics remain unresolved;
matching recorded clock values alone does not verify a physically aligned
renewable portfolio. No real dataset merge or aggregate accuracy claim is made.
There is no API, grid intelligence or economic/environmental calculation here.
