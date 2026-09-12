"""Read-only tabular discovery and diagnostics; never clean or rewrite input data."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import pandas as pd
from pandas.api.types import is_datetime64_any_dtype, is_numeric_dtype

SUPPORTED_EXTENSIONS = {".csv", ".tsv", ".txt", ".json", ".jsonl", ".ndjson", ".xlsx", ".xls", ".parquet", ".feather"}
SKIP_DIRECTORIES = {".git", ".venv", "venv", "node_modules", "__pycache__", ".pytest_cache"}


def discover_data_files(root: str | Path) -> list[Path]:
    """Find supported tabular files recursively, excluding tool environments."""
    root = Path(root)
    if not root.is_dir():
        raise ValueError(f"Dataset directory does not exist: {root}")
    return sorted(p for p in root.rglob("*") if p.is_file()
                  and p.suffix.lower() in SUPPORTED_EXTENSIONS
                  and not SKIP_DIRECTORIES.intersection(p.relative_to(root).parts))


def read_dataset(path: str | Path, *, sheet_name: str | int = 0) -> pd.DataFrame:
    """Read one table; Excel defaults to its first sheet. Optional formats need engines."""
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"Dataset not found: {path}")
    suffix = path.suffix.lower()
    try:
        if suffix in {".csv", ".txt"}:
            return pd.read_csv(path, sep=None, engine="python")
        if suffix == ".tsv":
            return pd.read_csv(path, sep="\t")
        if suffix in {".xlsx", ".xls"}:
            return pd.read_excel(path, sheet_name=sheet_name)
        if suffix in {".json", ".jsonl", ".ndjson"}:
            return pd.read_json(path, lines=suffix != ".json")
        if suffix == ".parquet":
            return pd.read_parquet(path)
        if suffix == ".feather":
            return pd.read_feather(path)
    except Exception as exc:
        raise ValueError(f"Cannot read {path}: {exc}. Check format, encoding and reader dependencies.") from exc
    raise ValueError(f"Unsupported dataset format: {suffix or '(none)'} ({path})")


def analyze_missing_values(data: pd.DataFrame) -> dict[str, Any]:
    """Count nulls and null percentages; empty strings are not silently cleaned."""
    return {str(c): {"count": int(data[c].isna().sum()),
                     "percent": float(data[c].isna().mean() * 100) if len(data) else 0.0}
            for c in data.columns}


def analyze_duplicates(data: pd.DataFrame) -> dict[str, int]:
    """Report excess duplicate rows and all rows participating in duplicates."""
    # Canonical JSON permits nested JSON cells without changing the input frame.
    comparable = data.map(lambda x: json.dumps(x, sort_keys=True) if isinstance(x, (dict, list)) else x)
    return {"duplicate_rows": int(comparable.duplicated().sum()),
            "rows_in_duplicate_groups": int(comparable.duplicated(keep=False).sum())}


def detect_time_columns(data: pd.DataFrame) -> list[str]:
    """Find typed dates or time-related names; candidates are not verified timestamps."""
    return [str(c) for c in data.columns if is_datetime64_any_dtype(data[c])
            or re.search(r"(?:^|[^a-z])(timestamp|datetime|date|time|year|month|day|hour)(?:$|[^a-z])", str(c).lower())]


def analyze_time_series(series: pd.Series) -> dict[str, Any]:
    """Parse a diagnostic copy. Do not guess numeric epochs or combine calendar parts.

    Explicit offsets are normalized to UTC only for comparison in this report.
    Naive timestamps remain semantically timezone-unknown. Ambiguous day/month
    strings are flagged and require a documented format in preprocessing.
    """
    present = series.dropna()
    if is_numeric_dtype(series):
        return {"column": str(series.name), "status": "numeric time candidate; unit/calendar assembly required",
                "missing": int(series.isna().sum())}
    values = present.astype(str)
    ambiguous = values.str.match(r"^(?:0?[1-9]|1[0-2])[/\-](?:0?[1-9]|1[0-2])[/\-]\d{2,4}(?:\s|$)")
    time_only = values.str.match(r"^\d{1,2}:\d{2}(?::\d{2}(?:\.\d+)?)?$")
    if len(values) and time_only.all():
        return {"column": str(series.name), "status": "time-only candidate; date required",
                "missing": int(series.isna().sum())}
    parsed = pd.to_datetime(series, errors="coerce", format="mixed", utc=True)
    valid = parsed.dropna()
    unique = valid.drop_duplicates().sort_values()
    deltas = unique.diff().dropna()
    modes = deltas.mode()
    step = modes.iloc[0] if len(modes) else None
    offsets = values.str.contains(r"(?:Z|[+-]\d{2}:?\d{2})$", regex=True)
    timezone = "explicit offset on all non-null values" if len(values) and offsets.all() else (
        "mixed explicit offsets and naive values" if offsets.any() else "not documented in values (naive)")
    return {
        "column": str(series.name), "status": "parsed diagnostic copy",
        "non_null": len(present), "parsed": len(valid),
        "parse_failures": int((series.notna() & parsed.isna()).sum()),
        "ambiguous_day_month_values": int(ambiguous.sum()),
        "missing": int(series.isna().sum()),
        "earliest": str(valid.min()) if len(valid) else None,
        "latest": str(valid.max()) if len(valid) else None,
        "unique_timestamps": len(unique), "duplicate_timestamps": int(valid.duplicated().sum()),
        "ascending_valid_values": bool(valid.is_monotonic_increasing),
        "descending_valid_values": bool(valid.is_monotonic_decreasing),
        "timezone": timezone,
        "estimated_frequency": str(step) if step is not None else "insufficient timestamps",
        "regular_unique_spacing": bool(len(deltas) and deltas.nunique() == 1),
        "interval_counts": {str(k): int(v) for k, v in deltas.value_counts().items()},
        "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values.",
    }


def analyze_numeric_columns(data: pd.DataFrame) -> dict[str, Any]:
    """Summarize numeric columns and flag infinities and statistical outliers."""
    result = {}
    for c in data.select_dtypes(include="number").columns:
        s = data[c]
        finite = s.replace([float("inf"), float("-inf")], float("nan")).dropna()
        q1, q3 = finite.quantile([0.25, 0.75])
        iqr = q3 - q1
        result[str(c)] = {
            "min": float(finite.min()) if len(finite) else None,
            "max": float(finite.max()) if len(finite) else None,
            "mean": float(finite.mean()) if len(finite) else None,
            "median": float(finite.median()) if len(finite) else None,
            "missing": int(s.isna().sum()), "non_finite_non_null": int(s.notna().sum() - len(finite)),
            "negative": int((finite < 0).sum()), "zero": int((finite == 0).sum()),
            "iqr_outliers": int(((finite < q1 - 1.5 * iqr) | (finite > q3 + 1.5 * iqr)).sum()),
        }
    return result


def analyze_columns(data: pd.DataFrame) -> list[dict[str, Any]]:
    """Describe inferred types, constants, sparse columns and numeric-looking text."""
    result = []
    for c in data.columns:
        s = data[c]
        text = s.dropna().map(str)
        numeric = pd.to_numeric(text, errors="coerce")
        result.append({"name": str(c), "dtype": str(s.dtype), "missing": int(s.isna().sum()),
                       "unique_non_null": int(text.nunique()), "constant": bool(text.nunique() == 1),
                       "sparse_over_50_percent_missing": bool(len(s) and s.isna().mean() > 0.5),
                       "numeric_text_values": int(numeric.notna().sum()) if not is_numeric_dtype(s) else 0,
                       "non_numeric_text_values": int(numeric.isna().sum()) if not is_numeric_dtype(s) else 0})
    return result


def inspect_dataset(path: str | Path, *, sheet_name: str | int = 0,
                    data: pd.DataFrame | None = None, size_bytes: int | None = None) -> dict[str, Any]:
    """Inspect a file or an already loaded archive table without modifying it."""
    path = Path(path)
    frame = read_dataset(path, sheet_name=sheet_name) if data is None else data
    return {"file": path.as_posix(), "format": path.suffix.lower(), "sheet": sheet_name,
            "size_bytes": path.stat().st_size if size_bytes is None else size_bytes,
            "rows": len(frame), "columns_count": len(frame.columns),
            "schema": analyze_columns(frame),
            "sample": json.loads(frame.head(5).to_json(orient="records", date_format="iso")),
            "missing": analyze_missing_values(frame), "duplicates": analyze_duplicates(frame),
            "time": {c: analyze_time_series(frame[c]) for c in detect_time_columns(frame)},
            "numeric": analyze_numeric_columns(frame)}


def generate_dataset_report(inspection: dict[str, Any]) -> str:
    """Render exact diagnostic results as Markdown with a JSON block."""
    return f"### {inspection['file']} — {inspection['sheet']}\n\n```json\n" + json.dumps(
        inspection, ensure_ascii=False, indent=2, allow_nan=False) + "\n```\n"
