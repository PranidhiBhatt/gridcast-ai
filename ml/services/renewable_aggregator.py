"""Aggregate aligned MW estimates without loading models or altering predictions."""

from __future__ import annotations

import json
import math
from datetime import datetime
from numbers import Real
from pathlib import Path
from typing import Any


def _power(value: Real | None, name: str) -> float | None:
    """None alone denotes unavailable; invalid predictions fail without clipping."""
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{name} must be numeric MW or None")
    try:
        number = float(value)
    except (OverflowError, ValueError) as exc:
        raise ValueError(f"{name} must be finite") from exc
    if not math.isfinite(number) or number < 0:
        raise ValueError(f"{name} must be finite and non-negative; no clipping")
    return number


def aggregate_renewable_power(
    timestamp: str | datetime,
    wind_power_mw: Real | None,
    solar_power_mw: Real | None,
    *,
    wind_unit: str = "MW",
    solar_unit: str = "MW",
    wind_model_name: str | None = None,
    solar_model_name: str | None = None,
) -> dict[str, Any]:
    """Sum two aligned estimates; partial/unavailable totals and mixes are None.

    Caller must establish the same time basis and compatible measurement/portfolio
    scope. Timestamp is validated and preserved, never converted or aligned here.
    Unit arguments declare units; numeric values cannot prove their own units.
    """
    if isinstance(timestamp, str):
        try:
            datetime.fromisoformat(timestamp)
        except ValueError as exc:
            raise ValueError("timestamp must be ISO-8601 or a datetime") from exc
    elif not isinstance(timestamp, datetime):
        raise ValueError("timestamp must be ISO-8601 or a datetime")
    if wind_unit != "MW" or solar_unit != "MW":
        raise ValueError("Both declared units must be MW; no conversion is performed")
    wind = _power(wind_power_mw, "wind_power_mw")
    solar = _power(solar_power_mw, "solar_power_mw")
    sources = {"wind": wind, "solar": solar}
    available = [name for name, value in sources.items() if value is not None]
    missing = [name for name, value in sources.items() if value is None]
    status = "COMPLETE" if len(available) == 2 else "PARTIAL" if available else "UNAVAILABLE"
    total = wind + solar if wind is not None and solar is not None else None
    if total is not None and not math.isfinite(total):
        raise ValueError("Total renewable power overflows finite MW representation")
    result = {"timestamp": timestamp, "wind_power_mw": wind, "solar_power_mw": solar,
              "total_renewable_power_mw": total, "aggregation_status": status,
              "available_sources": available, "missing_sources": missing,
              "wind_mix_percentage": wind / total * 100 if total is not None and total > 0 else None,
              "solar_mix_percentage": solar / total * 100 if total is not None and total > 0 else None}
    for key, name in (("wind_model_name", wind_model_name), ("solar_model_name", solar_model_name)):
        if name is not None:
            if not isinstance(name, str) or not name.strip():
                raise ValueError(f"{key} must be a nonempty string when supplied")
            result[key] = name
    return result


def load_selected_model_names(artifact_directory: Path) -> dict[str, str]:
    """Read optional JSON labels only; missing files omit labels, malformed files fail.

    Metadata presence does not establish model or estimate availability. Wind's
    model_type and solar's selected_model are their existing metadata identifiers.
    """
    result = {}
    for source, filename, field in (
        ("wind", "wind_best_model_metadata.json", "model_type"),
        ("solar", "solar_best_model_metadata.json", "selected_model"),
    ):
        path = artifact_directory / filename
        if not path.exists():
            continue
        try:
            metadata = json.loads(path.read_text(encoding="utf-8"))
            name = metadata.get(field) if isinstance(metadata, dict) else None
            if not isinstance(name, str) or not name.strip():
                raise ValueError(f"Missing or invalid {field}")
        except (OSError, ValueError) as exc:
            raise ValueError(f"Cannot read model metadata {path}: {exc}") from exc
        result[f"{source}_model_name"] = name
    return result
