# GridCast AI Dashboard

## Run and purpose

From the repository root, activate the existing environment and run:

```sh
python -m uvicorn backend.app.main:app --reload
```

Open **http://127.0.0.1:8000/**. Static HTML, CSS and vanilla JavaScript are served
by the same FastAPI app under `/static`. There are no frontend packages, external
assets or internet requirements. Existing API and documentation routes remain.

## Inputs and flow

The page requests `/project/status` and `/model/info`. Wind and solar fields are
generated from exact `required_features` names in metadata order; labels retain
the original units and requests retain whitespace/Unicode. No feature list is
duplicated in UI code. Model information and limitations appear in native details.
Unavailable contracts disable analysis until a successful refresh.

The user supplies a timezone-naive recorded timestamp, all prepared weather/calendar
and direction fields, demand in MW and an explicit interval in hours. Editing the
timestamp does not recalculate prepared features; users must keep them consistent.
The form sends nested wind, solar, grid and impact objects to **POST /analyze**.
All estimates, aggregation, gap, mix, recommendations and impact calculations come
from the backend. JavaScript only formats returned values and bar widths.

## Illustrative example

The inspected API fixtures use stand-in two-feature models; the documented complete
example has structural zeros, including invalid physical/calendar interpretations.
Neither is a real-observation example. `static/example.json` therefore reuses the
documented exact schema with explicitly illustrative values: 5 m/s wind, 180°
direction, 15°C temperature, 920 hPa pressure, 50% humidity and zero solar irradiance
for 2020-01-01 at midnight. Calendar fields use January/day 1/quarter 1/Wednesday;
hour encodings are 0/1, annual encodings 0/1, and illustrative wind day-of-year
encodings use sine/cosine of 2π/365. Direction encodings are 0/−1.
Demand is 50 MW and the visible interval is 0.25 hours.

These are hand-selected scenario values, not measurements, not drawn from datasets,
and not a guarantee of model validity or sensor semantics. Load Example checks that
every required feature has a finite sample value; a changed contract fails clearly.
It labels the inputs illustrative and never submits automatically.

## Results and errors

Results separate six primary cards, grid status with text/symbol/color, renewable
mix, gap/percentage, explanation, rule-based actions with reasons, economic energy
and cost estimates, environmental estimates, demand coverage and potential surplus.
Returned factors, interval, currency basis and impact limitations remain visible.
Null values display Unavailable, including zero-total mix percentages. No fabricated
zeros, changing demo outputs or business calculations are generated client-side.

Buttons prevent duplicate submissions and show an analysis loading state. Network
failures, 422 validation responses, 503 model errors and unexpected errors receive
readable messages. A 60-second client timeout clears loading; it does not cancel
server execution. Failed submissions hide prior results; edited inputs mark prior
results stale. Refresh handles status and metadata failures independently.

## Limits and verification

Models estimate contemporaneous weather-to-power relationships, not future forecasts.
Dataset coverage is limited and some source/sensor semantics are unresolved. Grid
recommendations are conditional decision support and never execute actions. Impact
values assume interval power and hypothetical displaced generation; they are not
verified savings, utilisation or real-world emissions. No real grid infrastructure,
weather feed, demand feed or autonomous control is connected.

Tests cover static route/assets, example request schema, health and unchanged API
paths. Existing API tests cover the service flow. No browser automation or new test
framework is added; responsive styling uses native grid/flex layouts.
