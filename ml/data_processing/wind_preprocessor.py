"""Site 1 preparation with explicit row accounting and no learned imputation."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

TIME = "Time(year-month-day h:m:s)"
TARGET = "Power (MW)"
SPEEDS = [f"Wind speed at height of {h} meters (m/s)" for h in (10, 30, 50)] + [
    "Wind speed - at the height of wheel hub(m/s)"]
DIRECTIONS = [f"Wind direction at height of {h} meters (˚)" for h in (10, 30, 50)]
AMBIGUOUS = "Wind speed - at the height of wheel hub (˚)"
TEMPERATURE = "Air temperature  (°C) "
PRESSURE = "Atmosphere (hpa)"
HUMIDITY = "Relative humidity (%)"
PRIMARY = [*SPEEDS, *DIRECTIONS]
SECONDARY = [TEMPERATURE, PRESSURE, HUMIDITY]
WEATHER = [*PRIMARY, AMBIGUOUS, *SECONDARY]
EXPECTED = [TIME, *[c for pair in zip(SPEEDS[:3], DIRECTIONS) for c in pair],
            SPEEDS[-1], AMBIGUOUS, *SECONDARY, TARGET]
TIME_FEATURES = ["hour", "day_of_week", "month", "day_of_year", "quarter",
                 "hour_sin", "hour_cos", "day_of_year_sin", "day_of_year_cos"]
DIRECTION_FEATURES = [f"wind_direction_{h}m_{component}" for h in (10, 30, 50) for component in ("sin", "cos")]


def load_wind_dataset(path: str | Path) -> pd.DataFrame:
    """Read the selected Excel workbook without modifying it."""
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"Wind workbook not found: {path}")
    try:
        return pd.read_excel(path, sheet_name="sheet1", engine="openpyxl")
    except Exception as exc:
        raise ValueError(f"Cannot read Site 1 sheet1 from {path}: {exc}") from exc


def validate_schema(data: pd.DataFrame) -> dict[str, Any]:
    """Fail on schema drift, nonnumeric observations or invalid/unsorted time keys."""
    if list(data.columns) != EXPECTED:
        raise ValueError(f"Site 1 schema mismatch. Expected {EXPECTED!r}; got {list(data.columns)!r}")
    if data.empty:
        raise ValueError("Wind dataset is empty")
    for c in WEATHER + [TARGET]:
        if not pd.api.types.is_numeric_dtype(data[c]):
            raise ValueError(f"Expected numeric dtype for {c!r}; got {data[c].dtype}")
    parsed = pd.to_datetime(data[TIME], errors="coerce", format="mixed")
    if parsed.isna().any() or not pd.api.types.is_datetime64_any_dtype(parsed):
        raise ValueError("Timestamp parsing failed; resolve format/timezone before preprocessing")
    if parsed.dt.tz is not None:
        raise ValueError("Source timezone differs from the verified naive Site 1 timestamps")
    if parsed.duplicated().any() or not parsed.is_monotonic_increasing:
        raise ValueError("Timestamps must be unique and chronologically increasing; no automatic sorting/deduplication")
    return {"rows": len(data), "columns": len(data.columns),
            "schema": [{"name": c, "dtype": str(data[c].dtype), "missing": int(data[c].isna().sum())} for c in data],
            "earliest": str(parsed.min()), "latest": str(parsed.max()),
            "regular_15_minutes": bool(parsed.diff().dropna().dt.total_seconds().eq(900).all()),
            "timezone": "unknown; source naive values preserved"}


def analyze_sentinel_values(data: pd.DataFrame) -> dict[str, Any]:
    """Classify -99 conservatively from physical ranges and synchronized outage rows.

    Temperature and the unresolved hub column need agreement with all seven
    verified speed/direction measurements. No supplied metadata verifies a code.
    """
    synchronous = data[PRIMARY].eq(-99).all(axis=1)
    result = {}
    for c in WEATHER + [TARGET]:
        mask = data[c].eq(-99)
        count = int(mask.sum())
        physically_invalid = c in PRIMARY + [PRESSURE, HUMIDITY]
        contextual = count > 0 and bool(synchronous[mask].all())
        likely = physically_invalid or (c in [TEMPERATURE, AMBIGUOUS] and contextual)
        classification = "LIKELY SENTINEL" if count and likely else "UNCERTAIN"
        result[c] = {"count": count, "percent_rows": 100 * count / len(data) if len(data) else 0,
                     "classification": classification, "documented": False,
                     "physical_plausibility": "outside header-supported physical range" if physically_invalid else
                     "not assessed as a standalone code; semantic or environmental context required",
                     "reason": "No codebook. Invalid range or exact coincidence with multi-sensor -99 outage supports sentinel interpretation."
                     if count and likely else "No automatic sentinel interpretation (including absent codes and target values).",
                     "action": "replace -99 with null in memory" if classification == "LIKELY SENTINEL" else "retain; review if present"}
    return result


def replace_invalid_values(data: pd.DataFrame, decisions: dict[str, Any]) -> tuple[pd.DataFrame, dict[str, Any]]:
    """Apply only documented sentinel decisions and physically invalid zero pressure."""
    cleaned = data.copy(deep=True)
    changes = {}
    for c, decision in decisions.items():
        if c != TARGET and decision["classification"] in {"LIKELY SENTINEL", "VERIFIED SENTINEL"}:
            mask = cleaned[c].eq(-99)
            changes[c] = {"sentinels_to_null": int(mask.sum())}
            cleaned.loc[mask, c] = np.nan
    zeros = cleaned[PRESSURE].eq(0)
    cleaned.loc[zeros, PRESSURE] = np.nan
    return cleaned, {"columns": changes, "zero_pressure_to_null": int(zeros.sum()),
                     "zero_pressure_reason": "Zero hPa is invalid for terrestrial ambient pressure; retain other zero weather values pending verification."}


def analyze_missingness(data: pd.DataFrame, columns: list[str]) -> dict[str, Any]:
    """Describe every null run in source order, including its timestamp bounds."""
    result = {}
    for c in columns:
        mask = data[c].isna().to_numpy()
        starts = np.flatnonzero(mask & ~np.r_[False, mask[:-1]])
        ends = np.flatnonzero(mask & ~np.r_[mask[1:], False])
        runs = [{"start": str(data[TIME].iloc[a]), "end": str(data[TIME].iloc[b]),
                 "observations": int(b - a + 1), "minutes_at_15min_cadence": int((b-a+1)*15)}
                for a, b in zip(starts, ends)]
        result[c] = {"missing": int(mask.sum()), "percent": float(mask.mean()*100) if len(mask) else 0,
                     "run_count": len(runs), "max_run": max((r["observations"] for r in runs), default=0),
                     "pattern": "clustered" if any(r["observations"] > 1 for r in runs) else "isolated" if runs else "none",
                     "runs": runs}
    return result


def validate_target(data: pd.DataFrame, nominal_capacity: float = 99.0) -> dict[str, Any]:
    """Audit power without treating zero generation or statistical extremes as errors."""
    s = data[TARGET]
    finite = s[np.isfinite(s)]
    q1, q3 = finite.quantile([.25, .75])
    extreme = (finite < q1-1.5*(q3-q1)) | (finite > q3+1.5*(q3-q1))
    times = pd.to_datetime(data[TIME], format="mixed", errors="coerce")
    return {"column": TARGET, "units": "MW", "measurement": "POWER", "nominal_capacity_MW": nominal_capacity,
            "missing": int(s.isna().sum()), "nonfinite_nonnull": int((s.notna() & ~np.isfinite(s)).sum()),
            "negative": int((s < 0).sum()), "above_nominal": int((s > nominal_capacity).sum()),
            "valid_zero_generation": int(s.eq(0).sum()),
            "zero_decision": "VALID ZERO GENERATION for retention; not independent verification of operating state",
            "invalid_target_value": int((s.isna() | ~np.isfinite(s) | (s < 0)).sum()),
            "suspicious_iqr_values": int(extreme.sum()), "suspicious_decision": "Retain; IQR extremes and nominal exceedances need review, not automatic clipping",
            "distribution": {str(k): float(v) for k, v in finite.quantile([0,.01,.25,.5,.75,.99,1]).items()},
            "mean": float(finite.mean()), "largest_absolute_adjacent_change_MW": float(s.diff().abs().max()),
            "time_missing": int(times.isna().sum()), "duplicate_timestamps": int(times.duplicated().sum()),
            "regular_15_minutes": bool(times.diff().dropna().dt.total_seconds().eq(900).all())}


def handle_missing_values(data: pd.DataFrame) -> tuple[pd.DataFrame, list[dict[str, Any]]]:
    """Complete-case selection with an explicit row ledger; no interpolation or fill.

    Long simultaneous outages make fabricated weather undesirable. Short pressure
    gaps could be causally filled but omitting two rows avoids adding assumptions.
    The excluded ambiguous column never determines row retention.
    """
    required = PRIMARY + SECONDARY + [TARGET]
    missing = data[required].isna()
    drop = missing.any(axis=1)
    ledger = [{"timestamp": str(data.loc[i, TIME]), "missing_columns": missing.columns[missing.loc[i]].tolist(),
               "action": "omit from prepared CSV only; raw observation preserved"} for i in data.index[drop]]
    return data.loc[~drop].copy(), ledger


def create_time_features(data: pd.DataFrame) -> pd.DataFrame:
    """Use source wall-clock time, fractional hours and leap-year-aware annual cycles."""
    result = data.copy()
    time = pd.to_datetime(result[TIME], format="mixed", errors="raise")
    result[TIME] = time
    result["hour"] = time.dt.hour
    result["day_of_week"] = time.dt.dayofweek
    result["month"] = time.dt.month
    result["day_of_year"] = time.dt.dayofyear
    result["quarter"] = time.dt.quarter
    fraction = (time.dt.hour + time.dt.minute/60 + time.dt.second/3600)/24
    result["hour_sin"] = np.sin(2*np.pi*fraction)
    result["hour_cos"] = np.cos(2*np.pi*fraction)
    annual = (time.dt.dayofyear - 1 + fraction)/np.where(time.dt.is_leap_year, 366, 365)
    result["day_of_year_sin"] = np.sin(2*np.pi*annual)
    result["day_of_year_cos"] = np.cos(2*np.pi*annual)
    return result


def create_wind_features(data: pd.DataFrame) -> pd.DataFrame:
    """Encode only explicitly labelled direction columns; preserve measured heights."""
    result = data.copy()
    for height, column in zip((10, 30, 50), DIRECTIONS):
        angle = np.deg2rad(result[column])
        result[f"wind_direction_{height}m_sin"] = np.sin(angle)
        result[f"wind_direction_{height}m_cos"] = np.cos(angle)
    return result


def select_features(data: pd.DataFrame) -> pd.DataFrame:
    """Select explicit columns; omit the unresolved hub degree column and unknowns."""
    return data[[TIME, *PRIMARY, *SECONDARY, *TIME_FEATURES, *DIRECTION_FEATURES, TARGET]].copy()


def check_feature_leakage(columns: list[str]) -> dict[str, Any]:
    """Fail closed on unknown features; observations are not verified future forecasts."""
    decisions = {}
    for c in columns:
        if c == TIME or c in TIME_FEATURES:
            label, reason = "SAFE FOR FORECASTING", "Calendar is known in advance; maintain consistent source timezone convention."
        elif c in PRIMARY + SECONDARY + DIRECTION_FEATURES:
            label, reason = "POTENTIAL LEAKAGE", "Observation at target timestamp; availability before a future forecast origin is unverified. Must lag to known observations or replace with as-issued weather forecasts before forecasting."
        else:
            label, reason = "EXCLUDE", "Target, unresolved column or unreviewed feature; not an approved predictor."
        decisions[c] = {"classification": label, "reason": reason}
    return decisions


def chronological_split_plan(data: pd.DataFrame) -> dict[str, Any]:
    """Use fixed calendar boundaries, chosen without fitting distributional parameters."""
    times = pd.to_datetime(data[TIME], format="mixed")
    masks = {"train": times < pd.Timestamp("2020-01-01"),
             "validation": (times >= pd.Timestamp("2020-01-01")) & (times < pd.Timestamp("2020-07-01")),
             "test": times >= pd.Timestamp("2020-07-01")}
    return {name: {"start": str(times[mask].min()), "end": str(times[mask].max()),
                   "rows": int(mask.sum()), "percent": float(mask.mean()*100)} for name, mask in masks.items()}


def prepare_wind_dataset(data: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    """Validate, clean and engineer a contemporaneous observation table, never a model."""
    schema = validate_schema(data)
    sentinel = analyze_sentinel_values(data)
    target = validate_target(data)
    if target["invalid_target_value"] or target["above_nominal"]:
        raise ValueError("Target quality differs from verified Site 1; review invalid/suspicious target values before continuing")
    cleaned, transformations = replace_invalid_values(data, sentinel)
    for c in PRIMARY + SECONDARY:
        remaining = cleaned[c].dropna()
        invalid = ~np.isfinite(remaining)
        if c in SPEEDS:
            invalid |= remaining < 0
        if c in DIRECTIONS:
            invalid |= (remaining < 0) | (remaining > 360)
        if c == PRESSURE:
            invalid |= remaining <= 0
        if c == HUMIDITY:
            invalid |= (remaining < 0) | (remaining > 100)
        if c == TEMPERATURE:
            invalid |= remaining == -99
        if invalid.any():
            raise ValueError(f"Unresolved invalid values in {c!r}; no undocumented correction applied")
    missing = analyze_missingness(cleaned, WEATHER)
    retained, removed = handle_missing_values(cleaned)
    output = select_features(create_wind_features(create_time_features(retained)))
    if output.empty or output.isna().any().any():
        raise ValueError("Prepared data is empty or still contains missing values")
    audit = {"schema": schema, "sentinels": sentinel, "transformations": transformations,
             "target_before": target, "target_after": validate_target(output), "missingness": missing,
             "removed_rows": removed, "input_rows": len(data), "output_rows": len(output),
             "output_columns": len(output.columns), "split_plan": chronological_split_plan(output),
             "leakage": check_feature_leakage(output.columns.tolist())}
    return output, audit
