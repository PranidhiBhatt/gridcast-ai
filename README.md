# GridCast AI

**AI-powered Hyperlocal Weather-to-Energy Intelligence for Renewable Grid Optimisation**

## Project Overview

GridCast AI is a hackathon and portfolio project exploring how hyperlocal weather
information can support renewable energy planning. The long-term goal is to
forecast solar and wind generation, compare supply with demand, identify grid
imbalances, and recommend actions with economic and environmental context.

The project foundation, dataset inspection, Site 1 wind preparation, baseline
estimation and advanced wind model comparison are implemented. These models
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
engineering, same-timestamp wind power estimation and controlled model comparison
are implemented.

## Technology Stack

| Area | Technology | Status |
| --- | --- | --- |
| Backend | Python 3.10+, FastAPI, Uvicorn | Implemented minimal API |
| Testing | pytest, HTTPX, FastAPI TestClient | Health, data preparation and model comparison tests |
| Data preparation | Pandas, NumPy, openpyxl | Inspection, cleaning and feature engineering |
| Wind estimation | scikit-learn, joblib, threadpoolctl | Baselines plus HistGradientBoosting and GradientBoosting comparison |
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
│   │   └── run_wind_preprocessing.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── wind_baseline.py
│   │   └── wind_advanced.py
│   ├── training/
│   │   ├── __init__.py
│   │   ├── train_wind_baseline.py
│   │   └── train_wind_advanced.py
│   └── artifacts/              # Ignored generated models, predictions and metrics
├── tests/
│   ├── __init__.py
│   ├── test_health.py
│   ├── test_data_inspector.py
│   ├── test_wind_preprocessor.py
│   ├── test_wind_baseline.py
│   └── test_wind_advanced.py
├── docs/
│   ├── .gitkeep
│   ├── dataset_sources.json
│   ├── wind_dataset_analysis.md
│   ├── wind_feature_manifest.json
│   ├── wind_preprocessing_report.md
│   ├── wind_baseline_model_report.md
│   └── wind_advanced_model_report.md
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

**Milestone 4 — Advanced Wind Power Model Comparison**

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

No true future forecasting, solar/demand models, grid decision engine, economic
or environmental calculations, database integration, frontend, or Docker setup
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

## API Documentation

See the unchanged API instructions below. Dataset preparation does not change FastAPI.

While the server is running, FastAPI provides:

- Swagger UI: <http://127.0.0.1:8000/docs>
- ReDoc: <http://127.0.0.1:8000/redoc>
- OpenAPI schema: <http://127.0.0.1:8000/openapi.json>

API title: **GridCast AI**. API version: **0.1.0**.
