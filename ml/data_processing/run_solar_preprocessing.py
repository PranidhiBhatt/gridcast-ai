"""Milestone 5B CLI: python -m ml.data_processing.run_solar_preprocessing."""

from __future__ import annotations

import json
import subprocess
import zipfile
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from ml.data_processing.run_wind_analysis import sha256, table
from ml.data_processing.solar_preprocessor import (
    CALENDAR, DNI, EXPECTED, FEATURES, GHI, HUMIDITY, IRRADIANCE, ORIGINAL_FEATURES,
    PRESSURE, TARGET, TEMPERATURE, TIME, TOTAL, WEATHER, load_solar_dataset,
    prepare_solar_dataset, semantic_diagnostics, validate_schema,
)

ROOT = Path(__file__).resolve().parents[2]
INPUT_NAME = "Solar station site 1 (Nominal capacity-50MW).xlsx"
OUTPUT = "ml/data/processed/solar_site_1_prepared.csv"
OMISSIONS = "ml/data/processed/solar_site_1_omissions.csv"


def verify_hashes(root: Path, expected: dict[str, str]) -> None:
    """Verify all recorded sources; changed or missing files fail before outputs."""
    for label, digest in expected.items():
        path = root / label
        if not path.is_file() or sha256(path) != digest:
            raise ValueError(f"Source SHA-256 mismatch or missing file: {label}")


def require_ignored(root: Path, relative: str) -> None:
    """Refuse to create a tracked or unignored generated dataset or omission log."""
    ignored = subprocess.run(["git", "check-ignore", "-q", "--", relative], cwd=root)
    tracked = subprocess.run(["git", "ls-files", "--error-unmatch", "--", relative], cwd=root, capture_output=True)
    if ignored.returncode != 0 or tracked.returncode == 0:
        raise ValueError(f"Generated output must be Git-ignored and untracked: {relative}")


def semantic_decisions() -> dict[str, Any]:
    """Fixed local-evidence policies; no performance-based feature selection."""
    return {
        "minus99": {"confidence": "LIKELY", "evidence": "All six weather columns have identical -99 rows; negative irradiance/pressure/relative humidity contradict header-supported ranges. No codebook defines the code.",
                    "policy": "Convert exactly -99 in the six explicitly named weather columns to missing in memory, including temperature based on synchronized evidence. Never blanket-replace negatives or power values."},
        "humidity": {"confidence": "UNRESOLVED", "evidence": "Non-sentinel out-of-range values form a narrow high-valued cluster. The percent header does not explain its encoding. Metadata contains no scaling/offset specification.",
                     "policy": "Exclude the entire humidity column from initial predictors. Do not rescale/clip or omit rows solely for humidity; preserve raw values. This semantic decision is not selected using model/test performance."},
        "power": {"confidence": "VERIFIED header; UNRESOLVED metering", "evidence": "Power (MW) explicitly labels power, not energy; AC/DC and instantaneous versus interval-average conventions are absent.",
                  "policy": "Preserve finite nonnegative targets, all zeros and statistical extremes. No capacity clipping, scaling or energy conversion. Missing/non-finite targets are unavailable and cause auditable omission. New negative targets fail for semantic review rather than silent correction."},
        "irradiance": {"confidence": "VERIFIED header units; UNRESOLVED geometry/calibration", "evidence": "Three separate headers name Total, Direct normal and Global horizontal irradiance in W/m2; total measurement plane is not specified.",
                       "policy": "Retain all three as separately labelled contemporaneous measurements, conditional on unknown calibration/geometry. No plane conversion, relabelling, upper clipping, cross-sensor formula or nighttime correction. New non-sentinel negative irradiance fails for review."},
        "temperature": {"confidence": "VERIFIED header; LIKELY sentinel", "evidence": "Air temperature is labelled degrees Celsius. The -99 rows coincide with all other weather codes.",
                        "policy": "Replace exactly the documented likely sentinel. Preserve other finite temperatures, including negatives; no unsupported range correction."},
        "pressure": {"confidence": "LIKELY", "evidence": "Atmosphere (hpa) suggests atmospheric pressure; non-sentinel measurements form a narrow plausible range. No sensor or altitude metadata verifies the interpretation.",
                     "policy": "Retain the original header/values after sentinel handling. No unit conversion or altitude adjustment. Newly encountered nonpositive values fail for review; none occur outside -99 in the inspected source."},
        "timezone": {"confidence": "UNRESOLVED", "evidence": "Recorded timestamps are naive. Workbook document creation/modification UTC stamps describe the document, not observation timezone.",
                     "policy": "Keep the recorded clock. Do not localize, convert, calculate astronomy or label physical solar time."},
        "capacity": {"confidence": "VERIFIED filename label; UNRESOLVED installed capacity", "evidence": "Filename states Nominal capacity-50MW only.",
                     "policy": "Document the label without treating it as independently verified installed capacity. Never use it to clip, normalize or reject observations."},
    }


def build_manifest(audit: dict[str, Any], diagnostics: dict[str, Any], context: dict[str, Any],
                   digest: str) -> dict[str, Any]:
    """Record exact predictor provenance, availability, policies and unfitted diagnostics."""
    decisions = semantic_decisions()
    units = {TOTAL: "W/m2", DNI: "W/m2", GHI: "W/m2", TEMPERATURE: "°C", PRESSURE: "hpa", HUMIDITY: "%"}
    review = {}
    for c in WEATHER:
        category = "irradiance" if c in IRRADIANCE else "temperature" if c == TEMPERATURE else "pressure" if c == PRESSURE else "humidity"
        review[c] = {"source_column": c, "category": category, "unit_from_header": units[c],
                     "semantic_confidence": decisions[category]["confidence"],
                     "included": c in ORIGINAL_FEATURES,
                     "missing_policy": "excluded column; never determines omission" if c == HUMIDITY else "-99/non-finite to missing; omit only incomplete required rows",
                     "availability_at_T": "co-recorded observation at T; delivery latency unverified",
                     "estimation_suitability": "excluded pending semantic verification" if c == HUMIDITY else "conditional contemporaneous empirical predictor; preserve label and uncertainties",
                     "future_availability": "NOT VERIFIED; future forecasting requires as-issued/available inputs and an explicit origin/horizon"}
    for c in CALENDAR:
        review[c] = {"source_column": TIME, "category": "calendar", "unit_from_header": None,
                     "semantic_confidence": "VERIFIED recorded-calendar arithmetic; timezone UNRESOLVED",
                     "included": True, "missing_policy": "invalid timestamp fails before feature generation",
                     "availability_at_T": "known from supplied timestamp T", "estimation_suitability": "approved",
                     "future_availability": "calendar known if target timestamp and source clock convention are defined"}
    return {"milestone": "5B", "policy_version": "solar-site-1-v1", "task": "WEATHER-TO-SOLAR-POWER ESTIMATION",
            "source": INPUT_NAME, "sheet": "sheet1", "source_manifest": "docs/solar_dataset_sources.json",
            "raw_sha256": digest, "timestamp_column": TIME, "target_column": TARGET,
            "original_features": ORIGINAL_FEATURES, "engineered_features": CALENDAR, "features": FEATURES,
            "excluded_features": {HUMIDITY: decisions["humidity"]["policy"], TIME: "split/index key only; use approved calendar encodings as predictors",
                                  TARGET: "target only; never a predictor or source of engineered features"},
            "semantic_decisions": decisions, "feature_review": review,
            "missing_value_policy": "Fixed complete-case omission for five original features and target only. No interpolation, forward/back fill, learned imputation or scaling. Humidity never drives omission.",
            "split_policy": "Fixed chronological boundaries independently verified against retained solar rows: train 2019; validation Jan-Jun 2020; test Jul-Dec 2020. No shuffle, fitting, target tuning or test-based feature selection; future learned transforms must fit train only.",
            "calendar_definitions": {"hour": "integer 0-23", "day_of_week": "Monday=0 through Sunday=6", "month": "1-12",
                                     "day_of_year": "1-365/366", "quarter": "1-4",
                                     "hour_sin/hour_cos": "sin/cos(2*pi*fraction_of_recorded_day), including minutes/seconds/subseconds",
                                     "annual_sin/annual_cos": "sin/cos(2*pi*(day_of_year-1+fraction_of_day)/days_in_current_year); 366 for leap years, otherwise 365"},
            "context": context, "diagnostics": diagnostics, "audit": audit,
            "output": {"path": OUTPUT, "rows": audit["output_rows"], "columns": audit["output_columns"], "predictors": len(FEATURES),
                       "float_serialization": "17 significant digits; pd.read_csv(float_precision='round_trip') preserves binary measurement values exactly"},
            "omission_log": {"path": OMISSIONS, "rows": audit["omitted_rows"], "columns": ["source_excel_row", "timestamp", "affected_columns", "reason"]},
            "limitations": ["Observed contemporaneous inputs do not establish true future forecasting", "Unknown timezone, site coordinates, calibration and input delivery latency",
                            "Unverified capacity, total irradiance plane and AC/DC or interval averaging convention", "Humidity excluded without an invented correction formula",
                            "Complete-case omission may bias coverage; retained neighboring rows may be separated by gaps", "Full-period quality summaries are diagnostic, not model-selection scores"],
            "runtime": {"pandas": pd.__version__, "numpy": np.__version__}}


def build_report(m: dict[str, Any]) -> str:
    """Render the requested sections from the actual data and fixed policy manifest."""
    def block(value: Any) -> str:
        return "```json\n" + json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n```\n"
    a, d = m["audit"], m["diagnostics"]
    parts = ["# Solar Data Preprocessing\n", "## Dataset\n",
             f"WEATHER-TO-SOLAR-POWER ESTIMATION. `{m['source']}` [sheet1]; {a['input_rows']:,} rows before preparation. Source remains at its discovered root location.\n",
             "## Raw Integrity\n", f"SHA-256: `{m['raw_sha256']}`. Checked against Milestone 5A before reading and again after writing separate outputs. All 5A source hashes are also checked; no raw rename, overwrite or copy.\n",
             "## Schema Validation\n", block(a["schema"]),
             "Exact eight-column order and numeric types required. ISO naive timestamps parse without localization; malformed, offset-bearing, duplicate or unordered timestamps fail for review. The production runner additionally checks 5A rows, coverage, cadence, sentinel and target findings.\n",
             "## Semantic Decisions\n", block(m["semantic_decisions"]), block(m["context"]),
             "VERIFIED refers to header/file evidence, not independent sensor certification. No internet sources were used. Document metadata provides no observation timezone or sensor codebook.\n",
             "## Sentinel Handling\n", block(d["sentinels"]), block(a["conversions"]), m["semantic_decisions"]["minus99"]["policy"] + "\n",
             "## Humidity Policy\n", block(d["humidity"]), m["semantic_decisions"]["humidity"]["policy"] + "\n",
             "The narrow high-value cluster could reflect encoding/sensor corruption; neither dividing by a constant nor subtracting an offset is evidenced. Exclusion avoids both invented repairs and loss of otherwise usable rows.\n",
             "## Irradiance Policy\n", block({c: d["numeric_without_weather_minus99"][c] for c in IRRADIANCE}),
             m["semantic_decisions"]["irradiance"]["policy"] + "\n",
             "Total and Global horizontal must not be assumed interchangeable. Header-supported separate empirical measurements are retained without asserting geometry or physical consistency formulas.\n",
             "## Temperature Policy\n", block(d["numeric_without_weather_minus99"][TEMPERATURE]), m["semantic_decisions"]["temperature"]["policy"] + "\n",
             "## Pressure Policy\n", block(d["numeric_without_weather_minus99"][PRESSURE]), m["semantic_decisions"]["pressure"]["policy"] + "\n",
             "## Target Policy\n", block(d["raw_numeric"][TARGET]), m["semantic_decisions"]["power"]["policy"] + "\n",
             "## Zero Generation Policy\n", "Zeros are retained; no row is omitted merely for zero power. Zero-target rows may still lack required weather, and those omissions are separately counted. Clock-hour patterns are not verified astronomical night.\n",
             block({"before": a["zero_generation_before"], "after": a["zero_generation_after"],
                    "zero_targets_omitted_only_for_missing_inputs": a["zero_targets_omitted_for_missing_inputs"]}),
             "## Positive Power / Zero GHI Analysis\n", block(d["positive_power_zero_ghi"]),
             f"Retained {a['positive_power_zero_ghi_retained']} such observations. Small positive output alongside very low irradiance may reflect rounding, sampling alignment or response characteristics; none is verified. No rule learned from these target diagnostics alters rows or predictors.\n",
             "## Missing Data Policy\n", m["missing_value_policy"] + "\n",
             block({"before": a["missing_before"], "after_handling_before_exclusion": a["missing_after_handling"], "output": a["missing_output"]}),
             "## Omitted Rows\n", block(m["omission_log"]),
             "The Git-ignored CSV records each original Excel row number, timestamp, affected required columns and per-column reason. No row is silently deduplicated or resampled.\n",
             "## Original Features\n", table(["Exact column", "Category", "Header unit", "Confidence", "Availability at T"],
                                             [[c, m["feature_review"][c]["category"], m["feature_review"][c]["unit_from_header"],
                                               m["feature_review"][c]["semantic_confidence"], m["feature_review"][c]["availability_at_T"]] for c in ORIGINAL_FEATURES]),
             "## Engineered Features\n", block(m["engineered_features"]), block(m["calendar_definitions"]),
             "Deterministic recorded-clock arithmetic only. No sunrise/sunset, solar elevation, power lag, rolling target, future observation, aggregation or learned feature.\n",
             "## Excluded Features\n", block(m["excluded_features"]),
             "## Chronological Splits\n", m["split_policy"] + "\n", block(a["splits"]),
             "All three partitions have retained observations; counts sum to output rows. Test remains held out from all model fitting/tuning. This milestone computes quality summaries only.\n",
             "## Final Dataset\n", block(m["output"]), block(a["output_interval_counts"]),
             "Output has no missing/non-finite predictor or target values. Raw target values in retained rows remain identical. CSV has no extra index column.\n",
             "## Limitations\n", block(m["limitations"]),
             "## Future Forecasting Limitation\n",
             "This dataset currently supports weather-to-solar-power estimation using observed contemporaneous measurements at timestamp T to estimate Power (MW) at T. It does not yet establish true future solar power forecasting. Future forecasting requires prediction-time available inputs, forecast origin, horizon and an availability/latency policy.\n",
             "Reproduce: `python -m ml.data_processing.run_solar_preprocessing`. No solar model, API integration or Milestone 5C work is included.\n"]
    return "\n".join(parts)


def run_preprocessing(root: Path = ROOT) -> dict[str, Any]:
    """Verify 5A provenance, prepare only solar outputs, then verify integrity again."""
    root = root.resolve()
    source_manifest = json.loads((root / "docs/solar_dataset_sources.json").read_text(encoding="utf-8"))
    if source_manifest["selected_dataset"] != INPUT_NAME:
        raise ValueError("Solar primary candidate changed; review before preparing")
    sources = source_manifest["source_hashes"]
    verify_hashes(root, sources)
    raw = root / INPUT_NAME
    digest = sha256(raw)
    selected = next(r for r in source_manifest["datasets"] if r["file"] == INPUT_NAME and r["sheet"] == "sheet1")
    if digest != selected["sha256"] or digest != sources[INPUT_NAME]:
        raise ValueError("Selected solar workbook differs from the 5A dataset record")
    data = load_solar_dataset(raw)
    schema = validate_schema(data)
    if data.shape != (selected["rows"], selected["columns_count"]):
        raise ValueError("Solar dimensions differ from 5A")
    # Production source is byte-identified; record-level assertions make drift errors explicit.
    if data.shape != (70176, 8) or not schema["regular_15_minutes"] or (schema["start"], schema["end"]) != (
            "2019-01-01 00:00:00", "2020-12-31 23:45:00"):
        raise ValueError("Solar coverage/cadence differs from reviewed Site 1")
    diagnostics = semantic_diagnostics(data)
    if any(data[c].isna().any() for c in EXPECTED) or diagnostics["sentinels"]["all_six_coincident_rows"] != 60 or any(
            v != 60 for v in diagnostics["sentinels"]["counts"].values()):
        raise ValueError("Solar null/sentinel findings differ from 5A")
    if diagnostics["humidity"]["outside_0_100"] != 6807 or diagnostics["positive_power_zero_ghi"]["rows"] != 56:
        raise ValueError("Solar humidity/zero-GHI findings differ from 5A")
    with zipfile.ZipFile(raw) as workbook:
        names = [n for n in workbook.namelist() if n.startswith("docProps/") or "comments" in n.lower()]
        metadata = {n: workbook.read(n).decode("utf-8") for n in names}
    context = {"evidence_sources": ["docs/solar_dataset_analysis.md", "docs/solar_dataset_sources.json", INPUT_NAME],
               "workbook_metadata": metadata,
               "local_document_review": "Repository root, existing docs, and both archive member listings reviewed: archives contain solar/wind workbooks and folders only; no supplied codebook or observation timezone documentation found. Document creation UTC stamps are not measurement timezone evidence.",
               "external_sources": "None; no internet used"}
    output, audit, ledger = prepare_solar_dataset(data)
    if not all(part["rows"] > 0 for part in audit["splits"].values()):
        raise ValueError("Prepared solar coverage cannot support all three planned splits")
    manifest = build_manifest(audit, diagnostics, context, digest)
    for relative in [OUTPUT, OMISSIONS, "docs/solar_feature_manifest.json", "docs/solar_preprocessing_report.md"]:
        path = root / relative
        if path.is_symlink() or path.resolve() != path:
            raise ValueError(f"Output path must not redirect through symlinks: {path}")
    for relative in [OUTPUT, OMISSIONS]:
        require_ignored(root, relative)
    verify_hashes(root, sources)
    (root / OUTPUT).parent.mkdir(parents=True, exist_ok=True)
    output.to_csv(root / OUTPUT, index=False, date_format="%Y-%m-%d %H:%M:%S", float_format="%.17g")
    ledger.to_csv(root / OMISSIONS, index=False)
    manifest["output"]["sha256"] = sha256(root / OUTPUT)
    manifest["omission_log"]["sha256"] = sha256(root / OMISSIONS)
    (root / "docs/solar_feature_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    (root / "docs/solar_preprocessing_report.md").write_text(build_report(manifest), encoding="utf-8")
    verify_hashes(root, sources)
    print(json.dumps({"rows": len(output), "columns": len(output.columns), "omitted": len(ledger),
                      "zero_before": audit["zero_generation_before"]["zero_count"],
                      "zero_after": audit["zero_generation_after"]["zero_count"], "splits": audit["splits"],
                      "raw_sha256": digest, "raw_integrity": "verified unchanged"}, indent=2))
    return manifest


if __name__ == "__main__":
    try:
        run_preprocessing()
    except (OSError, ValueError, KeyError, StopIteration) as exc:
        raise SystemExit(f"Solar preprocessing failed: {exc}") from exc
