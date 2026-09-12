"""Read-only solar diagnostics; header evidence is distinct from physical verification."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import pandas as pd

from ml.data_processing.data_inspector import (
    discover_data_files, inspect_dataset, read_dataset,
)


def discover_solar_files(root: Path) -> list[Path]:
    """Find named solar/PV tables; the runner also screens unnamed table headers."""
    return [p for p in discover_data_files(root)
            if re.search(r"solar|photovoltaic|(?:^|[/_ -])pv(?:[/_ .-]|$)", p.as_posix(), re.I)]


def feature_groups(columns: list[str]) -> dict[str, list[str]]:
    """Group actual header terms without treating inferred sensor meaning as verified."""
    patterns = {"irradiance": r"irradiance|irradiation|radiation|\bghi\b|\bdni\b|\bdhi\b",
                "temperature": r"temperature", "humidity": r"humidity",
                "pressure": r"pressure|atmosphere", "wind": r"wind",
                "cloud": r"cloud", "solar_angle": r"zenith|azimuth|solar angle",
                "site_metadata": r"site|latitude|longitude|capacity|plant"}
    return {group: [c for c in columns if re.search(pattern, c, re.I)]
            for group, pattern in patterns.items()}


def inspect_solar_dataset(path: str | Path, *, data: pd.DataFrame | None = None,
                          sheet_name: str | int = 0, size_bytes: int | None = None) -> dict[str, Any]:
    """Compute full-table diagnostics without cleaning, converting units or fitting."""
    frame = read_dataset(path, sheet_name=sheet_name) if data is None else data
    report = inspect_dataset(path, data=frame, sheet_name=sheet_name,
                             size_bytes=Path(path).stat().st_size if size_bytes is None else size_bytes)
    report["feature_groups"] = feature_groups(list(map(str, frame.columns)))
    report["targets"] = {}
    report["suspicious"] = {}
    for c, stats in report["numeric"].items():
        s = frame[c]
        flags = {"sentinel_counts": {str(v): int(s.eq(v).sum()) for v in (-99, -999)},
                 "zero_percent": float(s.eq(0).mean() * 100) if len(s) else 0,
                 "status": "REQUIRES SEMANTIC VERIFICATION",
                 "negative_physical_candidate": 0}
        if re.search(r"irradiance|wind speed|humidity|pressure|atmosphere", c, re.I):
            flags["negative_physical_candidate"] = stats["negative"]
            if stats["negative"]:
                flags["status"] = "LIKELY ISSUE; sensor offsets/sentinels require verification"
        if "humidity" in c.lower() and "%" in c:
            flags["outside_header_percent_range"] = int(((s < 0) | (s > 100)).sum())
        report["suspicious"][c] = flags
    for c in frame.columns:
        if not re.search(r"\bpower\b|\benergy\b|\bgeneration\b", str(c), re.I):
            continue
        unit = re.search(r"\b(MWh|kWh|Wh|MW|kW|W)\b", str(c))
        report["targets"][str(c)] = {
            "dtype": str(frame[c].dtype), "unit_in_header": unit[0] if unit else None,
            "measurement": ("ENERGY" if "Wh" in unit[0] else "POWER") if unit else "UNRESOLVED",
            "evidence": "VERIFIED header label only; metering, AC/DC and averaging convention UNRESOLVED",
            "statistics": report["numeric"].get(str(c)), "missing": report["missing"][str(c)],
            "ml_suitability": "candidate after quality review" if str(c) in report["numeric"] else "UNRESOLVED nonnumeric target",
        }
    for c, timing in report["time"].items():
        timing["missing_intervals_on_modal_grid"] = None
        if timing.get("unique_timestamps", 0) > 1:
            t = pd.to_datetime(frame[c], errors="coerce", format="mixed", utc=True).dropna().drop_duplicates().sort_values()
            step = t.diff().dropna().mode().iloc[0]
            if step > pd.Timedelta(0) and ((t - t.iloc[0]) % step == pd.Timedelta(0)).all():
                timing["missing_intervals_on_modal_grid"] = int((t.iloc[-1] - t.iloc[0]) / step) + 1 - len(t)
    report["solar_checks"] = {"day_night": "UNRESOLVED: no verified coordinates/timezone; clock hours and zero irradiance do not prove night",
                              "irradiance_conditions": [], "hourly_target_summary": {}}
    irradiance = [c for c in report["feature_groups"]["irradiance"] if c in report["numeric"]]
    for target in report["targets"]:
        if target not in report["numeric"]:
            continue
        for c in irradiance:
            mask = frame[c].eq(0) & frame[target].notna()
            report["solar_checks"]["irradiance_conditions"].append({
                "irradiance": c, "target": target, "zero_irradiance_target_observations": int(mask.sum()),
                "zero_target": int((mask & frame[target].eq(0)).sum()),
                "positive_target": int((mask & frame[target].gt(0)).sum()),
                "negative_target": int((mask & frame[target].lt(0)).sum()),
                "note": "Observed zero-irradiance association, not an astronomical night classification"})
        for c, timing in report["time"].items():
            if timing.get("parsed", 0):
                hours = pd.to_datetime(frame[c], errors="coerce", format="mixed", utc=True).dt.hour
                report["solar_checks"]["hourly_target_summary"][f"{target} / {c}"] = [
                    {"hour": int(hour), "non_null": int(s.count()), "zero": int(s.eq(0).sum()),
                     "mean": float(s.mean()) if s.count() else None}
                    for hour, s in frame[target].groupby(hours)]
    capacity = re.search(r"Nominal capacity\s*-\s*([\d.]+)\s*MW", str(path), re.I)
    report["filename_capacity_label_mw"] = float(capacity[1]) if capacity else None
    report["capacity_evidence"] = "Filename label only; installed capacity and site identity require verification"
    for c, target in report["targets"].items():
        if capacity and target["unit_in_header"] == "MW" and target["statistics"]:
            target["above_filename_capacity_label"] = int(frame[c].gt(float(capacity[1])).sum())
    return report
