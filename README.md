# GridCast AI

**AI-powered Hyperlocal Weather-to-Energy Intelligence for Renewable Grid Optimisation**

## Project Overview

GridCast AI is a hackathon and portfolio project exploring how hyperlocal weather
information can support renewable energy planning. The long-term goal is to
forecast solar and wind generation, compare supply with demand, identify grid
imbalances, and recommend actions with economic and environmental context.

Only the project foundation is implemented at this stage.

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

These features are planned and are not implemented in Milestone 0.

## Technology Stack

| Area | Technology | Status |
| --- | --- | --- |
| Backend | Python 3.10+, FastAPI, Uvicorn | Implemented minimal API |
| Testing | pytest, HTTPX, FastAPI TestClient | Health endpoint test |
| Machine learning and data | Pandas, NumPy, scikit-learn, XGBoost | Planned |
| Database | PostgreSQL | Planned |
| Frontend | React | Planned |

Only backend runtime and test dependencies are included in `requirements.txt`.

## Project Structure

```text
gridcast-ai/
├── backend/
│   └── app/
│       ├── __init__.py
│       └── main.py
├── ml/
│   ├── data/
│   │   ├── raw/.gitkeep
│   │   └── processed/.gitkeep
│   ├── data_processing/.gitkeep
│   ├── models/.gitkeep
│   ├── training/.gitkeep
│   └── artifacts/.gitkeep
├── tests/
│   ├── __init__.py
│   └── test_health.py
├── docs/.gitkeep
├── .gitignore
├── .env.example
├── README.md
└── requirements.txt
```

A single root dependency file avoids duplicating backend dependencies.
The empty ML and documentation directories are retained with `.gitkeep` files;
they contain no placeholder implementations. Raw and processed datasets and
serialized `.joblib`/`.pkl` models are excluded from Git.

## Current Development Status

**Milestone 0 — Project Foundation**

Implemented: project structure, a minimal FastAPI application with API metadata,
the health endpoint, and its test.

No ML models, dataset preprocessing, forecasting, grid decision engine, economic
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

The test checks the health endpoint's HTTP status and both response fields.
It runs in process and does not require a running server.

## API Documentation

While the server is running, FastAPI provides:

- Swagger UI: <http://127.0.0.1:8000/docs>
- ReDoc: <http://127.0.0.1:8000/redoc>
- OpenAPI schema: <http://127.0.0.1:8000/openapi.json>

API title: **GridCast AI**. API version: **0.1.0**.
