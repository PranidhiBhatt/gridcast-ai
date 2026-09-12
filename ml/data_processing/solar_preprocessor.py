"""Site 1 solar preparation: fixed semantic policies, no fitted transformations."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from ml.data_processing.data_inspector import analyze_missing_values, analyze_numeric_columns

TIME = "Time(year-month-day h:m:s)"
TOTAL = "Total solar irradiance (W/m2)"
DNI = "Direct normal irradiance (W/m2)"
GHI = "Global horizontal irradiance (W/m2)"
TEMPERATURE = "Air temperature  (°C) "
PRESSURE = "Atmosphere (hpa)"
HUMIDITY = "Relative humidity (%)"
TARGET = "Power (MW)"
IRRADIANCE = [TOTAL, DNI, GHI]
ORIGINAL_FEATURES = [*IRRADIANCE, TEMPERATURE, PRESSURE]
WEATHER = [*ORIGINAL_FEATURES, HUMIDITY]
EXPECTED = [TIME, *WEATHER, TARGET]
CALENDAR = ["hour", "day_of_week", "month", "day_of_year", "quarter",
            "hour_sin", "hour_cos", "annual_sin", "annual_cos"]
FEATURES = [*ORIGINAL_FEATURES, *CALENDAR]
SPLIT_BOUNDARIES = {
    "train": ("2019-01-01", "2020-01-01"),
    "validation": ("2020-01-01", "2020-07-01"),
    "test": ("2020-07-01", "2021-01-01"),
}


def load_solar_dataset(path: Path) -> pd.DataFrame:
    """Read the selected sheet only; errors identify the source and sheet."""
    try:
        return pd.read_excel(path, sheet_name="sheet1", engine="openpyxl")
    except (OSError, ValueError) as exc:
        raise ValueError(f"Cannot read solar workbook {path} [sheet1]: {exc}") from exc


def parse_timestamps(series: pd.Series) -> pd.Series:
    """Accept ISO recorded-clock strings or naive datetimes; never guess a timezone."""
    if pd.api.types.is_numeric_dtype(series):
        raise ValueError("Numeric timestamps require an explicitly reviewed encoding")
    if not pd.api.types.is_datetime64_any_dtype(series):
        iso = series.astype(str).str.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}(?:\.\d{1,9})?")
        if not iso.all():
            raise ValueError("Timestamp must be a naive ISO date and time; malformed/ambiguous/offset values require review")
    try:
        parsed = pd.to_datetime(series, errors="raise", format="mixed")
    except (ValueError, TypeError) as exc:
        raise ValueError(f"Timestamp parsing failed: {exc}") from exc
    if parsed.isna().any() or not pd.api.types.is_datetime64_any_dtype(parsed):
        raise ValueError("Missing or mixed timestamp types require review")
    if parsed.dt.tz is not None:
        raise ValueError("Timezone-aware timestamps require review; no timezone conversion permitted")
    if parsed.duplicated().any() or not parsed.is_monotonic_increasing:
        raise ValueError("Timestamps must be unique and chronologically increasing; no automatic sorting")
    return parsed


def validate_schema(data: pd.DataFrame) -> dict[str, Any]:
    """Fail on schema/type drift rather than renaming columns or coercing measurements."""
    if list(data.columns) != EXPECTED:
        raise ValueError(f"Solar schema mismatch: expected {EXPECTED!r}, got {list(data.columns)!r}")
    if data.empty or not data.index.is_unique:
        raise ValueError("Solar table must be nonempty with unique row indices")
    for c in WEATHER + [TARGET]:
        if not pd.api.types.is_numeric_dtype(data[c]) or pd.api.types.is_bool_dtype(data[c]):
            raise ValueError(f"Expected numeric measurements in {c!r}")
    times = parse_timestamps(data[TIME])
    return {"rows": len(data), "columns": len(data.columns),
            "schema": [{"column": c, "dtype": str(data[c].dtype), "missing": int(data[c].isna().sum())} for c in data],
            "start": str(times.min()), "end": str(times.max()), "timezone": "UNRESOLVED; naive recorded clock",
            "regular_15_minutes": bool(len(times) > 1 and times.diff().dropna().dt.total_seconds().eq(900).all())}


def calendar_features(data: pd.DataFrame) -> pd.DataFrame:
    """Encode recorded-clock calendar using fractional days and each year's length."""
    result = data.copy(deep=True)
    t = parse_timestamps(result[TIME])
    result[TIME] = t
    result["hour"] = t.dt.hour
    result["day_of_week"] = t.dt.dayofweek
    result["month"] = t.dt.month
    result["day_of_year"] = t.dt.dayofyear
    result["quarter"] = t.dt.quarter
    fraction = (t - t.dt.normalize()).dt.total_seconds() / 86400
    result["hour_sin"] = np.sin(2 * np.pi * fraction)
    result["hour_cos"] = np.cos(2 * np.pi * fraction)
    annual = (t.dt.dayofyear - 1 + fraction) / np.where(t.dt.is_leap_year, 366, 365)
    result["annual_sin"] = np.sin(2 * np.pi * annual)
    result["annual_cos"] = np.cos(2 * np.pi * annual)
    return result


def validate_feature_list(features: list[str]) -> None:
    """Reject target, timestamp, excluded humidity and all unreviewed predictors."""
    if len(features) != len(set(features)) or set(features) != set(FEATURES):
        raise ValueError("Feature allowlist mismatch: no target-derived, humidity or unknown features permitted")


def chronological_split_plan(data: pd.DataFrame) -> dict[str, Any]:
    """Partition only the documented two-year coverage; reject unassigned timestamps."""
    t = parse_timestamps(data[TIME])
    if t.empty or t.min() < pd.Timestamp("2019-01-01") or t.max() >= pd.Timestamp("2021-01-01"):
        raise ValueError("Split coverage must be within 2019 and 2020")
    result = {}
    for name, (start, end) in SPLIT_BOUNDARIES.items():
        mask = t.ge(start) & t.lt(end)
        result[name] = {"boundary_start_inclusive": start, "boundary_end_exclusive": end,
                        "rows": int(mask.sum()), "percent": float(mask.mean() * 100),
                        "start": str(t[mask].min()) if mask.any() else None,
                        "end": str(t[mask].max()) if mask.any() else None}
    if sum(r["rows"] for r in result.values()) != len(data):
        raise ValueError("Split row accounting failed")
    return result


def zero_generation_analysis(data: pd.DataFrame) -> dict[str, Any]:
    """Describe zeros and irradiance relationships; these diagnostics never filter rows."""
    times = parse_timestamps(data[TIME])
    def grouped(key: pd.Series) -> list[dict[str, Any]]:
        return [{"group": str(label), "rows": len(s), "non_null_targets": int(s.count()),
                 "zero_targets": int(s.eq(0).sum()),
                 "zero_percent_of_non_null": float(s.eq(0).sum() / s.count() * 100) if s.count() else None}
                for label, s in data[TARGET].groupby(key)]
    return {"zero_count": int(data[TARGET].eq(0).sum()), "by_hour": grouped(times.dt.hour),
            "by_month": grouped(times.dt.strftime("%Y-%m")),
            "irradiance_associations": {c: {
                "zero_irradiance": int(data[c].eq(0).sum()),
                "zero_irradiance_zero_power": int((data[c].eq(0) & data[TARGET].eq(0)).sum()),
                "zero_irradiance_positive_power": int((data[c].eq(0) & data[TARGET].gt(0)).sum())}
                for c in IRRADIANCE},
            "interpretation": "Recorded-clock/measurement associations only; no astronomical night classification"}


def semantic_diagnostics(data: pd.DataFrame) -> dict[str, Any]:
    """Collect unfitted evidence; no correlation or target statistic selects predictors."""
    t = parse_timestamps(data[TIME])
    sent = data[WEATHER].eq(-99)
    without_sentinels = data[WEATHER].mask(sent)
    h = data[HUMIDITY]
    bad = h.lt(0) | h.gt(100)
    high = h[h.gt(100)]
    anomaly = data[TARGET].gt(0) & data[GHI].eq(0)
    return {
        "raw_numeric": analyze_numeric_columns(data),
        "numeric_without_weather_minus99": analyze_numeric_columns(without_sentinels),
        "sentinels": {"counts": {c: int(sent[c].sum()) for c in WEATHER},
                      "all_six_coincident_rows": int(sent.all(axis=1).sum()),
                      "any_weather_sentinel_rows": int(sent.any(axis=1).sum())},
        "humidity": {"outside_0_100": int(bad.sum()), "minus99": int(h.eq(-99).sum()),
                     "negative_other": int((h.lt(0) & h.ne(-99)).sum()), "above100": len(high),
                     "high_quantiles": {str(q): float(v) if pd.notna(v) else None
                                        for q, v in high.quantile([0, .25, .5, .75, 1]).items()},
                     "most_common_high_values": {str(k): int(v) for k, v in high.value_counts().head(10).items()},
                     "bad_by_month": {str(k): int(v) for k, v in bad.groupby(t.dt.strftime("%Y-%m")).sum().items()},
                     "bad_with_other_weather_sentinel": int((bad & sent.drop(columns=HUMIDITY).any(axis=1)).sum()),
                     "weather_pearson_without_minus99": {c: float(v) if pd.notna(v) else None for c, v in
                                                         without_sentinels.corr()[HUMIDITY].items()},
                     "interpretation": "Large high-value cluster suggests an encoding/sensor problem, but neither scaling nor offset correction is verified. Correlations are descriptive, not evidence of a correction formula."},
        "positive_power_zero_ghi": {"classification": "UNRESOLVED; retain", "rows": int(anomaly.sum()),
                                    "numeric": analyze_numeric_columns(data.loc[anomaly]),
                                    "by_hour": {str(k): int(v) for k, v in t[anomaly].dt.hour.value_counts().sort_index().items()},
                                    "with_weather_sentinel": int((anomaly & sent.any(axis=1)).sum()),
                                    "with_invalid_humidity": int((anomaly & bad).sum()),
                                    "interpretation": "Rounding, timing alignment or low-light response are possibilities, not verified causes. No deletion or nighttime correction."},
    }


def prepare_solar_dataset(data: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any], pd.DataFrame]:
    """Apply fixed policies and return prepared data, summary and complete omission ledger."""
    schema = validate_schema(data)
    cleaned = data.copy(deep=True)
    cleaned[TIME] = parse_timestamps(data[TIME])
    causes: dict[str, pd.Series] = {}
    for c in WEATHER:
        cause = pd.Series("", index=data.index, dtype=object)
        cause.loc[data[c].isna()] = "original missing"
        cause.loc[data[c].notna() & ~np.isfinite(data[c])] = "non-finite measurement"
        cause.loc[data[c].eq(-99)] = "likely -99 sentinel"
        cleaned.loc[cause.ne(""), c] = np.nan
        causes[c] = cause
    # Exclusion avoids an unverified humidity repair and humidity-only row loss.
    for c in IRRADIANCE:
        if cleaned[c].lt(0).any():
            raise ValueError(f"Unreviewed non-sentinel negative irradiance in {c!r}")
    if cleaned[PRESSURE].le(0).any():
        raise ValueError("Unreviewed nonpositive pressure; stop rather than invent a correction")
    if data[TARGET].lt(0).any():
        raise ValueError("Negative target requires semantic review; never apply weather sentinel rules to power")
    cause = pd.Series("", index=data.index, dtype=object)
    cause.loc[data[TARGET].isna()] = "original missing target"
    cause.loc[data[TARGET].notna() & ~np.isfinite(data[TARGET])] = "non-finite target"
    cleaned.loc[cause.ne(""), TARGET] = np.nan
    causes[TARGET] = cause
    required = [*ORIGINAL_FEATURES, TARGET]
    missing = cleaned[required].isna()
    omit = missing.any(axis=1)
    records = []
    for position in np.flatnonzero(omit.to_numpy()):
        affected = missing.columns[missing.iloc[position]].tolist()
        records.append({"source_excel_row": int(position + 2), "timestamp": str(cleaned[TIME].iloc[position]),
                        "affected_columns": " | ".join(affected),
                        "reason": " | ".join(f"{c}: {causes[c].iloc[position]}" for c in affected)})
    ledger = pd.DataFrame(records, columns=["source_excel_row", "timestamp", "affected_columns", "reason"])
    retained = cleaned.loc[~omit].copy()
    if retained.empty:
        raise ValueError("No complete solar observations remain")
    validate_feature_list(FEATURES)
    output = calendar_features(retained)[[TIME, *FEATURES, TARGET]]
    if output.isna().any().any() or not np.isfinite(output[FEATURES + [TARGET]].to_numpy()).all():
        raise ValueError("Prepared output contains missing/non-finite values")
    if not output[TARGET].equals(data.loc[~omit, TARGET]):
        raise ValueError("Target values changed unexpectedly")
    audit = {"schema": schema, "input_rows": len(data), "omitted_rows": int(omit.sum()),
             "output_rows": len(output), "output_columns": len(output.columns),
             "missing_before": analyze_missing_values(data), "missing_after_handling": analyze_missing_values(cleaned),
             "missing_output": analyze_missing_values(output),
             "conversions": {c: {"minus99_to_missing": int(data[c].eq(-99).sum()),
                                  "nonfinite_to_missing": int((data[c].notna() & ~np.isfinite(data[c])).sum())} for c in WEATHER},
             "zero_generation_before": zero_generation_analysis(data),
             "zero_generation_after": zero_generation_analysis(output),
             "zero_targets_omitted_for_missing_inputs": int((omit & data[TARGET].eq(0)).sum()),
             "positive_power_zero_ghi_retained": int((output[TARGET].gt(0) & output[GHI].eq(0)).sum()),
             "splits": chronological_split_plan(output),
             "output_interval_counts": {str(k): int(v) for k, v in output[TIME].diff().dropna().value_counts().items()}}
    return output, audit, ledger
