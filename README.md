# GridCast AI

**AI-powered Hyperlocal Weather-to-Energy Intelligence for Renewable Grid Optimisation**

## Project Overview

GridCast AI is a hackathon and portfolio project exploring how hyperlocal weather
information can support renewable energy planning. The long-term goal is to
forecast solar and wind generation, compare supply with demand, identify grid
imbalances, and recommend actions with economic and environmental context.

The project foundation, wind and solar dataset inspection/preparation, baseline
wind and solar estimation, and advanced wind model comparison are implemented. These models
estimate power at the same timestamp as their weather inputs. True future
forecasting and grid intelligence remain planned.

## Problem Statement

Solar and wind generation depend on changing local weather conditions. When
renewable supply and energy demand do not align, grid operators need to identify
potential shortages or surpluses and assess possible responses. GridCast AI aims
to bring those signals together into an interpretable decision-support platform.

## Core Pipeline

Planned end-to-end flow:

Weather → Renewable Generation → Demand → Grid Balance → Grid Action → Economic Impact → Environmental Impact

This will involve weather data ingestion, solar and wind generation forecasting,
demand comparison, supply-demand gap and surplus/deficit detection, grid action
recommendations, and economic and environmental impact analysis.

## Planned Features

- Hyperlocal weather data ingestion and preprocessing.
- Solar and wind generation forecasting.
- Demand forecasting and comparison with renewable supply.
- Supply-demand gap detection, including surpluses and deficits.
- Grid action recommendations.
- Economic and environmental impact analysis.
- PostgreSQL persistence and a React interface.

Live ingestion and forecasting remain planned. Offline Site 1 cleaning, feature
engineering, same-timestamp wind and solar power estimation and controlled model comparison
are implemented.

## Technology Stack

| Area | Technology | Status |
| --- | --- | --- |
| Backend | Python 3.10+, FastAPI, Uvicorn | Implemented minimal API |
| Testing | pytest, HTTPX, FastAPI TestClient | Health, data preparation and model comparison tests |
| Data preparation | Pandas, NumPy, openpyxl | Inspection, cleaning and feature engineering |
| Wind estimation | scikit-learn, joblib, threadpoolctl | Baselines plus HistGradientBoosting and GradientBoosting comparison |
| Solar estimation | scikit-learn, joblib, threadpoolctl | Mean, scaled linear regression and fixed random forest baselines |
| Database | PostgreSQL | Planned |
| Frontend | React | Planned |

Backend, test, data preparation and model comparison dependencies are included in
`requirements.txt`. No deep-learning or unrelated forecasting frameworks are
installed.

## Project Structure

```text
gridcast-ai/
├── backend/
│   └── app/
│       ├── __init__.py
│       └── main.py
├── ml/
│   ├── data/
│   │   ├── raw/                 # Ignored datasets; wind/ and solar/ retain .gitkeep
│   │   └── processed/           # .gitkeep and ignored generated CSV
│   ├── data_processing/
│   │   ├── .gitkeep
│   │   ├── data_inspector.py
│   │   ├── run_wind_analysis.py
│   │   ├── wind_preprocessor.py
│   │   ├── run_wind_preprocessing.py
│   │   ├── solar_data_inspector.py
│   │   ├── run_solar_analysis.py
│   │   ├── solar_preprocessor.py
│   │   └── run_solar_preprocessing.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── wind_baseline.py
│   │   ├── wind_advanced.py
│   │   ├── solar_baseline.py
│   │   └── solar_advanced.py
│   ├── training/
│   │   ├── __init__.py
│   │   ├── train_wind_baseline.py
│   │   ├── train_wind_advanced.py
│   │   ├── train_solar_baseline.py
│   │   └── train_solar_advanced.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── renewable_aggregator.py
│   │   ├── grid_intelligence.py
│   │   └── impact_engine.py
│   └── artifacts/              # Ignored generated models, predictions and metrics
├── tests/
│   ├── __init__.py
│   ├── test_health.py
│   ├── test_data_inspector.py
│   ├── test_wind_preprocessor.py
│   ├── test_wind_baseline.py
│   ├── test_wind_advanced.py
│   ├── test_solar_data_inspector.py
│   ├── test_solar_preprocessor.py
│   ├── test_solar_baseline.py
│   ├── test_solar_advanced.py
│   ├── test_renewable_aggregator.py
│   ├── test_grid_intelligence.py
│   └── test_impact_engine.py
├── docs/
│   ├── .gitkeep
│   ├── dataset_sources.json
│   ├── wind_dataset_analysis.md
│   ├── wind_feature_manifest.json
│   ├── wind_preprocessing_report.md
│   ├── wind_baseline_model_report.md
│   ├── wind_advanced_model_report.md
│   ├── solar_dataset_analysis.md
│   ├── solar_dataset_sources.json
│   ├── solar_feature_manifest.json
│   ├── solar_preprocessing_report.md
│   ├── solar_baseline_model_report.md
│   ├── solar_advanced_model_report.md
│   ├── renewable_aggregation.md
│   ├── grid_intelligence.md
│   └── impact_engine.md
├── .gitignore
├── .env.example
├── README.md
└── requirements.txt
```

A single root dependency file avoids duplicating backend dependencies.
Empty future ML directories are retained with `.gitkeep` files;
they contain no placeholder implementations. Raw and processed datasets and
serialized `.joblib`/`.pkl` models are excluded from Git.

## Current Development Status

**Milestone 8 — Economic and Environmental Impact Estimation**

Milestone 0 remains unchanged: project structure, a minimal FastAPI application
with API metadata, the health endpoint, and its test. Milestone 1 adds reusable
read-only inspection, synthetic tests, source hashes and a reproducible wind report.
Milestone 2 adds in-memory cleaning, audited row omission, deterministic calendar
and direction features, a chronological split plan and a separate prepared CSV.
Milestone 3 adds three fixed same-timestamp estimation baselines, chronological
evaluation, validation-based model selection and reproducible local artifacts.
Milestone 4 compares fixed HistGradientBoosting and GradientBoosting configurations
with two feature sets, validation-only selection, residual/error analysis and a
single held-out test evaluation for the selected model.

Milestone 5A adds independent, read-only solar discovery and full-table quality
analysis across the extracted workbook and solar archive members. Milestone 5B
adds semantic review and reproducible Site 1 solar preparation. Milestone 5C
adds three training-only solar estimation baselines and chronological evaluation.
Milestone 5D compares one fixed HistGradientBoosting configuration and one fixed
ExtraTrees configuration, preserving the 5B data/features/splits and 5C baseline.
Milestone 6 adds a small aggregation service for already-produced wind and solar
MW estimates, with explicit complete, partial and unavailable results.
Milestone 7 compares complete renewable supply with reported demand, using a
configurable symmetric balance tolerance and deterministic decision-support advice.
Milestone 8 adds explicit-duration, assumption-driven avoided generation cost and
emissions scenarios, with demand coverage and potential surplus context.

Reproduce from the project root with existing dependencies and libarchive-compatible
`tar` on PATH:

```sh
python -m ml.data_processing.run_solar_analysis
```

The runner uses `solar_data_inspector.py` alongside the unchanged generic inspection
utilities. It reads archive members in memory and verifies SHA-256 checksums before
and after inspection, and against its previous manifest on reruns. It writes only
[the solar analysis report](docs/solar_dataset_analysis.md) and
[the solar source metadata](docs/solar_dataset_sources.json). Raw files remain at
their discovered locations. Synthetic tests are in `tests/test_solar_data_inspector.py`.

Reproduce solar preprocessing with the existing dependencies:

```sh
python -m ml.data_processing.run_solar_preprocessing
```

The runner verifies the original root workbook against the Milestone 5A SHA-256,
converts exactly `-99` in six named weather columns to missing in memory, and
excludes unresolved humidity from predictors without inventing a correction.
It omits 60 rows missing required inputs and retains 70,116 rows with five original
measurements and nine recorded-clock calendar predictors. Zero power is preserved:
31 zero-target rows are omitted only because required weather is missing; 35,233
zero targets and all 56 positive-power/zero-GHI observations remain.

Outputs are the Git-ignored `ml/data/processed/solar_site_1_prepared.csv` and
`solar_site_1_omissions.csv`, plus the small
[feature manifest](docs/solar_feature_manifest.json) and
[preprocessing report](docs/solar_preprocessing_report.md). The omission log records
source Excel row, timestamp, affected columns and reasons. No interpolation,
filling, learned scaling or model training occurs. Annual calendar encodings account
for leap years; timestamps remain on the recorded clock with no timezone conversion.

The task is **Weather-to-Solar-Power Estimation**: observed irradiance/weather at T
and calendar features estimate `Power (MW)` at T. This does not establish true
future forecasting. Source timezone, irradiance geometry, AC/DC/averaging semantics
and installed capacity remain unresolved. The independently checked solar splits
are 2019 training (34,987 rows), January–June 2020 validation (17,472), and
July–December 2020 testing (17,657); no random shuffle or test-based tuning.

No true future forecasting, demand models, autonomous dispatch, live market
integration, database integration, frontend, or Docker setup
are included.

## Setup Instructions

Install Python 3.10 or newer. From the project directory:

```sh
cd gridcast-ai
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on macOS/Linux:

```sh
source .venv/bin/activate
```

Install dependencies:

```sh
python -m pip install -r requirements.txt
```

No environment variables or secrets are required. `.env.example` documents this;
creating an `.env` file is unnecessary for this milestone, and the application
does not load one.

## How to Run FastAPI

Run from the `gridcast-ai` project root with the virtual environment active:

```sh
python -m uvicorn backend.app.main:app --reload
```

The local API runs at <http://127.0.0.1:8000>.

`GET /health` returns HTTP 200 with:

```json
{
  "status": "ok",
  "service": "GridCast AI"
}
```

## How to Run Tests

From the project root with the virtual environment active:

```sh
python -m pytest
```

Tests check the health endpoint, data utilities and modelling using synthetic temporary
datasets. They require neither downloaded datasets nor a running server.

If Windows denies access to its default temporary folder, use:

```sh
python -m pytest -q --basetemp .pytest_cache/milestone1-tests
```

## Reproduce the Wind Dataset Analysis

Read [the analysis report](docs/wind_dataset_analysis.md) for findings and
[the source manifest](docs/dataset_sources.json) for original paths, sizes and
SHA-256 hashes. The six original downloads must remain in the repository root.
The runner reads the wind members of both RAR archives in memory and checks the
selected site 1 copy under `ml/data/raw/wind/`. It never extracts, cleans, merges
or rewrites raw data. It updates only the Markdown report.

If restoring this project on another machine, obtain the original downloads
separately (they are ignored by Git), verify their manifest hashes, and copy the
wind site 1 workbook to the manifest's destination without overwriting an existing
file. The source URL and license are not present in the downloaded material.

RAR inspection requires a **libarchive-compatible `tar`** on PATH. The Windows
`tar` available during validation supported these archives; GNU tar alone may not.
From the project root with the environment active:

```sh
python -m ml.data_processing.run_wind_analysis
```

The reusable inspector supports CSV, TSV, delimited TXT, JSON records/JSON Lines
and Excel. Legacy `.xls` and Parquet/Feather readers are optional and require their
respective engines (`xlrd` / `pyarrow`); these are not installed for this milestone.
Numeric time candidates require explicit units or calendar assembly and are not
guessed as epoch timestamps. No timestamps or data values are changed.

## Reproduce Wind Preprocessing

From the project root with dependencies installed:

```sh
python -m ml.data_processing.run_wind_preprocessing
```

The runner verifies the selected workbook against the Milestone 1 source hash,
schema and missing counts. It preserves every raw file and writes:

- `ml/data/processed/wind_site_1_prepared.csv` (Git-ignored): 70,036 rows, 27 columns.
- [Feature manifest](docs/wind_feature_manifest.json): classifications, policies and every omitted row.
- [Preprocessing report](docs/wind_preprocessing_report.md): evidence, transformations and split plan.

The policy converts likely weather sentinels and two invalid zero pressures to
missing, excludes the unresolved hub degree column, and omits 140 incomplete rows
with a full audit ledger. It performs no filling or learned transformations and
retains all 206 zero-power observations. The resulting timestamps have gaps.

Calendar and direction encodings are deterministic. Observed weather remains a
potential leakage risk for future forecasting: define forecast origin, horizon
and available weather inputs before using it. The CSV is a prepared observation
table, not a verified operational forecasting matrix. No model is trained.

Fixed chronological splits are 2019 for training, January–June 2020 for validation,
and July–December 2020 for testing. No split files or random shuffle are created.
Rerunning updates only the generated CSV, feature manifest and preprocessing report.

## Reproduce Baseline Wind Power Estimation

From the project root with dependencies installed:

```sh
python -m ml.training.train_wind_baseline
```

The task is **Weather-to-Wind-Power Estimation**: weather and calendar features at
timestamp T estimate `Power (MW)` at T. This is not true future forecasting.
Observed weather would need replacement with as-issued forecast weather for a
future target time, with a defined origin, horizon and availability policy.

The runner loads 25 predictors from the existing feature manifest and uses the
unchanged 70,036-row prepared dataset. It fits a training-mean benchmark, a
StandardScaler/LinearRegression pipeline, and a random forest with 80 trees,
depth 12, minimum leaf size 5, seed 42 and one worker. There is no parameter search.

Training uses 2019; validation uses January–June 2020; held-out testing uses
July–December 2020. Best baseline selection uses validation MAE, then validation
RMSE for ties, and is frozen before test evaluation. No model is refitted on
validation or test, and no predictions are clipped to improve metrics.

Read [the model report](docs/wind_baseline_model_report.md) for all train,
validation and test metrics, feature availability, overfitting observations and
random forest importance. Importance describes model usage, not causation.

Generated artifacts under `ml/artifacts/` are Git-ignored:

- `dummy_baseline.joblib`, `linear_regression.joblib`, `random_forest_baseline.joblib`.
- `wind_baseline_metrics.json`, `wind_baseline_feature_importance.json`.
- `wind_validation_predictions.csv`, `wind_test_predictions.csv` (selected model only).

The linear model artifact includes its training-fitted scaler. The runner records
input/code hashes, library versions and fixed settings without volatile timestamps.
It preserves the input datasets and preprocessing code. Reproducibility is assessed
within the same software environment; other versions can differ numerically.

## Reproduce Advanced Wind Model Comparison

From the project root with dependencies installed:

```sh
python -m ml.training.train_wind_advanced
```

This milestone keeps the same **Weather-to-Wind-Power Estimation** task and
chronological 2019 / January–June 2020 / July–December 2020 split. It compares
four fixed configurations each for two feature experiments: set A uses the 19
weather and safe calendar fields from the manifest, while set B uses all 25
available predictors including engineered direction encodings. No random
cross-validation or hyperparameter search is used. The selected configuration is
chosen by validation MAE, with documented tie-breakers, before the held-out test
metrics are read.

The validation winner is `B_hist_150`, a
`HistGradientBoostingRegressor` using all 25 predictors. Its held-out test metrics
are MAE 6.7198 MW, RMSE 11.8563 MW and R² 0.7878. Relative to the Milestone 3
random-forest baseline, RMSE improves by 1.72% and R² improves by 0.0075, while
MAE is 0.0023 MW higher (0.03% worse). The test period is kept out of advanced
model fitting, while its baseline result was already reported in Milestone 3.

Read [the advanced model report](docs/wind_advanced_model_report.md) for the
complete experiment ledger, residual and time-based errors, power-range errors,
validation permutation importance and final model metadata. Generated models,
metrics, predictions and analysis JSON files under `ml/artifacts/` are ignored by
Git.

## Reproduce Baseline Solar Power Estimation

From the repository root with the existing dependencies installed:

```sh
python -m ml.training.train_solar_baseline
```

The runner verifies the Milestone 5B dataset hash, schema, ordered 14-feature
contract and chronological splits. It fits a training-mean DummyRegressor,
a StandardScaler/LinearRegression pipeline, and a fixed RandomForestRegressor
(100 trees, depth 12, minimum leaf size 5, seed 42, one worker).
Only training data fits models or scaling. Selection uses overall validation MAE,
then RMSE, then R². All three baselines receive test scores after selection is frozen;
no random cross-validation, tuning or train+validation refit occurs.

Random forest wins validation MAE (2.1026 MW). Its test MAE is 1.7823 MW,
RMSE 4.4688 MW and R² 0.8922. Linear regression has slightly better test RMSE
(4.4117 MW), but test results do not change the validation-selected model.
All prepared zero targets remain in evaluation. Power-range diagnostics use
positive training-target tertiles; recorded-hour/month diagnostics do not imply
verified local solar time.

Read [the solar baseline report](docs/solar_baseline_model_report.md) for full
train/validation/test metrics, zero/positive subsets, residuals and importance.
Generated models, metrics, selected-model predictions and best-model metadata
remain Git-ignored in `ml/artifacts/`, with names beginning `solar_`. The saved
linear pipeline includes its training-fitted scaler. Repeated runs use identical
fixed settings; reproducibility depends on the recorded software environment.

These are **Weather-to-Solar-Power Estimation** models using observed inputs at T.
Future forecasting still requires future-available weather/irradiance inputs,
an origin, a horizon and an availability policy.

## Reproduce Advanced Solar Model Evaluation

```sh
python -m ml.training.train_solar_advanced
```

Exactly two candidates use the unchanged 14-feature manifest and training-only
fits. Selection ranks validation MAE, RMSE, then R². The predeclared replacement
threshold requires at least 1% validation MAE improvement over Random Forest;
this is an experiment rule, not statistical or operational significance.

ExtraTrees is selected: validation MAE 2.0506 MW versus Random Forest's 2.1026 MW
(2.47% reduction). Only ExtraTrees receives a test evaluation in 5D: MAE 1.7488 MW,
RMSE 4.1004 MW, R² 0.9093. The test period was already reported in 5C and is not
a previously unseen benchmark. No test-based reselection, tuning, random CV,
preprocessing change or new dependency is introduced.

Read [the advanced solar report](docs/solar_advanced_model_report.md) for fixed
parameters, both validation results and focused diagnostics. Positive-generation
test MAE remains 3.5738 MW, versus 0.0303 MW on zero-generation observations.
Observed contemporaneous weather/irradiance estimation is not future forecasting.

Two candidate models and three small JSON artifacts remain Git-ignored under
`ml/artifacts/`. The best-model metadata points to the selected saved estimator.
Reruns verify input, code and output hashes and reuse the completed evaluation;
an interrupted final evaluation fails clearly rather than silently repeating it.
No prediction CSV or plots are generated for 5D.

## Renewable Generation Aggregation

`ml.services.renewable_aggregator.aggregate_renewable_power` accepts a timestamp
and aligned `wind_power_mw` / `solar_power_mw` estimates. Both available values
produce a complete total; missing values remain `None` and make the total
unavailable. Renewable mix percentages are returned only for positive complete
totals. Negative, non-finite and nonnumeric estimates are rejected without clipping.

See [the aggregation contract and example](docs/renewable_aggregation.md).
An optional JSON-only helper reads model labels. No model loading, training,
preprocessing, dataset alignment, API integration or grid decisions are performed.
Callers must establish compatible time, units and portfolio scope before aggregation.

## Rule-based Grid Intelligence

`ml.services.grid_intelligence.analyze_grid` accepts the aggregation result and
reported `demand_mw`. It calculates renewable supply minus demand and classifies
SURPLUS, BALANCED or DEFICIT using an inclusive, symmetric 1 MW default tolerance,
configurable per call. Percentages use demand as denominator; zero demand returns
a null percentage. Incomplete supply yields unavailable analysis without a gap.

See [the rules, input contract and example](docs/grid_intelligence.md).
Recommendations are fixed conditional options for operator review. This component
does not execute dispatch, establish total-grid adequacy or guarantee safety.
No API integration, model training or economic/environmental calculations are added.

## Economic and Environmental Impact Estimation

`ml.services.impact_engine.estimate_impact` requires renewable MW and explicit
`interval_hours` to calculate MWh. `estimate_grid_impact` accepts the Milestone 7
result and preserves unavailable supply. Configurable illustrative defaults are
500 kg CO₂/MWh and 50 generic currency units/MWh, echoed in each result.

Read [the impact formulas, assumptions and example](docs/impact_engine.md).
The scenario assumes all estimated energy displaces conventional generation;
actual use and displacement are unverified, including for surplus. These outputs
are not measured savings, verified emissions reductions or carbon accounts.
No live prices, external services or grid control are introduced.

## API Documentation

See the unchanged API instructions below. Dataset preparation does not change FastAPI.

While the server is running, FastAPI provides:

- Swagger UI: <http://127.0.0.1:8000/docs>
- ReDoc: <http://127.0.0.1:8000/redoc>
- OpenAPI schema: <http://127.0.0.1:8000/openapi.json>

API title: **GridCast AI**. API version: **0.1.0**.
