# GridCast AI Product API

Run from the repository root with existing dependencies and the virtual environment:

```sh
python -m uvicorn backend.app.main:app --reload
```

Swagger UI: `/docs`; ReDoc: `/redoc`; OpenAPI: `/openapi.json`.

## Endpoints

| Method/path | Input and behavior |
|---|---|
| GET /health | Existing health response, independent of artifact availability |
| POST /estimate/wind | `features` dictionary, optional timestamp; wind MW estimate |
| POST /estimate/solar | `features` dictionary, optional timestamp; solar MW estimate |
| POST /estimate/renewable | Timestamp, wind_power_mw and solar_power_mw (each nullable); Milestone 6 |
| POST /grid/analyze | `renewable` object with those three fields, demand_mw, optional balance_tolerance_mw; Milestone 7 |
| POST /impact/analyze | renewable_power_mw (nullable), required interval_hours, optional demand_mw, timestamp and assumptions; Milestone 8 |
| POST /analyze | Nested wind, solar, grid and impact inputs; complete pipeline |
| GET /model/info | Loadability, model names, exact ordered feature names, task, unit and limitations |
| GET /project/status | Actual model loadability and availability of the three local services |

`/analyze` returns separate `wind`, `solar`, `renewable`, `grid` and `impact`
objects plus the original timestamp. It calls the existing services in order;
no business formulas are copied into endpoints. Missing/unloadable models fail the
whole pipeline clearly rather than fabricating a partial estimate. Numeric-only
aggregation, grid and impact endpoints need no trained artifacts.

## Features and loading

Wind selects `B_hist_150` from final wind metadata (HistGradientBoostingRegressor,
25 predictors). Solar selects `extra_trees` from final solar metadata
(ExtraTreesRegressor, 14 predictors). `/model/info` supplies authoritative exact
names. Feature maps must contain exactly those names, including whitespace and
Unicode degree symbols; input key order does not matter. The model receives
metadata order. All values must be finite numbers, not strings or booleans.

Callers supply prepared weather, direction encodings and calendar features. No
feature generation, timestamp conversion, cleaning or input clipping occurs.
The timestamp is a preserved label: consistency between it and supplied calendar
features is the caller's responsibility. The example below shows schema only.

Models load lazily from trusted local artifacts. SHA-256 is checked against saved
metadata before deserialization, and estimator feature order must match metadata.
Successful loads are cached per process; restart the server after replacing
artifacts. Missing or corrupt artifacts are not cached as successes and may be
retried. Information/status endpoints attempt loading to report actual loadability;
they expose no artifact paths, training data or sklearn objects. No training occurs.

## Validation and errors

Unknown request fields, missing fields, invalid timestamps, nonnumeric/non-finite
features, negative demand/power and nonpositive duration fail with HTTP 422.
Missing or extra feature keys produce `INVALID_FEATURE_INPUT` (422). Units are MW
in the contracts; there is no automatic unit conversion. Service validation also
rejects overflows. Negative/non-finite predictions return `INVALID_MODEL_OUTPUT`
(500), with no clipping. Models can produce negatives; no fake fallback is used.

Unloadable models produce `MODEL_UNAVAILABLE` (503). Unexpected errors produce
500 without paths or stack traces. Errors use `{"error":{"code":...,"message":...}}`;
request validation also supplies field locations. Successful info/status responses
use HTTP 200 even when reporting a model as UNAVAILABLE.

## Assumptions and limitations

These models estimate power using observed contemporaneous features, not true
future forecasting. Callers must establish matching timestamps, units and intended
site/portfolio scope for wind, solar and reported demand. No live weather or demand
integration exists. Grid recommendations are conditional operator decision support;
no dispatch or real grid control executes.

Impact requires an explicit positive interval in hours. Optional assumptions are
`emission_factor_kg_co2_per_mwh` (illustrative 500),
`avoided_generation_cost_per_mwh` (illustrative 50), `currency_unit` (generic
currency units), and `factor_basis` (illustrative/unsourced by default). Results
assume constant interval power and hypothetical conventional displacement of all
estimated energy. They are not actual savings, verified emissions or utilisation.

## Request examples

Simple independent request to `/grid/analyze`:

```json
{"renewable":{"timestamp":"2020-01-01T12:00:00","wind_power_mw":30,"solar_power_mw":10},"demand_mw":50}
```

The following `/analyze` example enumerates exact metadata feature names. All-zero
values illustrate structure only, not a physically validated observation. Replace
them with consistent prepared measurements/calendar values before meaningful use.

```json
{
  "timestamp": "2020-01-01T00:00:00",
  "wind": {
    "features": {
      "Wind speed at height of 10 meters (m/s)": 0,
      "Wind speed at height of 30 meters (m/s)": 0,
      "Wind speed at height of 50 meters (m/s)": 0,
      "Wind speed - at the height of wheel hub(m/s)": 0,
      "Wind direction at height of 10 meters (˚)": 0,
      "Wind direction at height of 30 meters (˚)": 0,
      "Wind direction at height of 50 meters (˚)": 0,
      "Air temperature  (°C) ": 0,
      "Atmosphere (hpa)": 0,
      "Relative humidity (%)": 0,
      "hour": 0,
      "day_of_week": 0,
      "month": 0,
      "day_of_year": 0,
      "quarter": 0,
      "hour_sin": 0,
      "hour_cos": 0,
      "day_of_year_sin": 0,
      "day_of_year_cos": 0,
      "wind_direction_10m_sin": 0,
      "wind_direction_10m_cos": 0,
      "wind_direction_30m_sin": 0,
      "wind_direction_30m_cos": 0,
      "wind_direction_50m_sin": 0,
      "wind_direction_50m_cos": 0
    }
  },
  "solar": {
    "features": {
      "Total solar irradiance (W/m2)": 0,
      "Direct normal irradiance (W/m2)": 0,
      "Global horizontal irradiance (W/m2)": 0,
      "Air temperature  (°C) ": 0,
      "Atmosphere (hpa)": 0,
      "hour": 0,
      "day_of_week": 0,
      "month": 0,
      "day_of_year": 0,
      "quarter": 0,
      "hour_sin": 0,
      "hour_cos": 0,
      "annual_sin": 0,
      "annual_cos": 0
    }
  },
  "grid": {
    "demand_mw": 50
  },
  "impact": {
    "interval_hours": 0.25
  }
}
```

