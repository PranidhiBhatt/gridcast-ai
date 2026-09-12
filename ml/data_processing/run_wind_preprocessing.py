"""Reproduce Milestone 2: python -m ml.data_processing.run_wind_preprocessing."""

from __future__ import annotations

import json
import subprocess
import zipfile
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from ml.data_processing.run_wind_analysis import sha256, table
from ml.data_processing.wind_preprocessor import (
    AMBIGUOUS, DIRECTIONS, DIRECTION_FEATURES, EXPECTED, PRIMARY, PRESSURE,
    SECONDARY, TARGET, TIME, TIME_FEATURES, WEATHER, load_wind_dataset,
    prepare_wind_dataset, validate_schema,
)

ROOT = Path(__file__).resolve().parents[2]
INPUT_NAME = "Wind farm site 1 (Nominal capacity-99MW).xlsx"


def verify_milestone_one(data: pd.DataFrame, report: str) -> None:
    """Compare actual schema/types/null counts with the selected-table Milestone 1 section."""
    section = report.split("## 4. Dataset Schema", 1)[1].split("## 5.", 1)[0]
    section = section.split(f"### ml/data/raw/wind/{INPUT_NAME} [sheet1]", 1)[1]
    entries = [line.split("|")[1:-1] for line in section.splitlines() if line.startswith('| "')]
    expected = [(json.loads(row[0].strip()), row[1].strip(), int(row[2].strip())) for row in entries]
    actual = [(c, str(data[c].dtype), int(data[c].isna().sum())) for c in data]
    schema = validate_schema(data)
    if actual != expected or data.shape != (70176, 13) or not schema["regular_15_minutes"] or (
            schema["earliest"], schema["latest"]) != ("2019-01-01 00:00:00", "2020-12-31 23:45:00"):
        raise ValueError("Discrepancy from Milestone 1 schema, missingness, row count or coverage; review before proceeding")


def inspect_context(data: pd.DataFrame, path: Path) -> dict[str, Any]:
    """Collect supporting diagnostics; correlations never determine semantic verification."""
    diagnostic = data[WEATHER].replace(-99, np.nan)
    zero_indices = data.index[data[PRESSURE].eq(0)]
    surrounding = sorted({j for i in zero_indices for j in range(max(0,i-1), min(len(data),i+2))})
    with zipfile.ZipFile(path) as book:
        metadata_parts = [n for n in book.namelist() if n.startswith("docProps/") or "comments" in n.lower()]
        metadata = {n: book.read(n).decode("utf-8") for n in metadata_parts}
    return {"ambiguous_column": AMBIGUOUS, "classification": "UNRESOLVED",
            "decision": "EXCLUDED PENDING SEMANTIC VERIFICATION",
            "raw_min": float(data[AMBIGUOUS].min()), "raw_max": float(data[AMBIGUOUS].max()),
            "original_nulls": int(data[AMBIGUOUS].isna().sum()),
            "quantiles_excluding_minus99": diagnostic[AMBIGUOUS].quantile([0,.25,.5,.75,1]).to_dict(),
            "pearson_correlations_excluding_minus99": diagnostic.corr()[AMBIGUOUS].to_dict(),
            "interpretation": "Degree unit, range and stronger association with directions suggest direction, but contradictory header and absent semantic definition prevent verification. Pearson correlation of circular variables is descriptive only.",
            "pressure_zero_context": json.loads(data.iloc[surrounding].to_json(orient="records", date_format="iso")),
            "synchronous_zero_weather_rows": int(data[WEATHER].eq(0).all(axis=1).sum()),
            "zero_weather_decision": "Other zeros remain plausible individually and are not blanket-replaced. The two synchronous-zero rows are omitted due to invalid pressure regardless.",
            "workbook_metadata": metadata}


def build_manifest(audit: dict[str, Any], context: dict[str, Any], digest: str) -> dict[str, Any]:
    """Record decisions, predictor availability and the complete omission ledger."""
    classifications = {c: "TIME SOURCE" if c == TIME else "TARGET" if c == TARGET else
                       "PRIMARY FEATURE" if c in PRIMARY else "SECONDARY FEATURE" if c in SECONDARY else "EXCLUDE" for c in EXPECTED}
    strategies = {c: {"strategy": "DROP COLUMN" if c == AMBIGUOUS else "DROP ROW",
                      "reason": "Semantic ambiguity, not missing rate." if c == AMBIGUOUS else
                      "No inferred values. Simultaneous weather gaps reach 78 samples (19.5 hours); omit incomplete observations with an explicit ledger. Two isolated pressure errors are omitted instead of introducing a separate fill assumption.",
                      "learned_parameters": None} for c in WEATHER}
    return {"dataset_name": INPUT_NAME, "dataset_version": "Site 1 original; preparation policy milestone-2-v1",
            "source": f"ml/data/raw/wind/{INPUT_NAME}", "raw_sha256": digest,
            "source_manifest": "docs/dataset_sources.json", "target_column": TARGET, "nominal_capacity_MW": 99,
            "timestamp_column": TIME, "original_column_classifications": classifications,
            "primary_features": PRIMARY, "secondary_features": SECONDARY,
            "engineered_features": TIME_FEATURES + DIRECTION_FEATURES,
            "excluded_columns": {AMBIGUOUS: "EXCLUDED PENDING SEMANTIC VERIFICATION"},
            "sentinel_value_decisions": audit["sentinels"], "missing_value_strategies": strategies,
            "leakage_decisions": audit["leakage"], "forecast_safe_predictors": TIME_FEATURES,
            "forecast_horizon": "not established; output is a contemporaneous observation table",
            "forecasting_gate": "Do not use same-target-time observations for future forecasting. Define forecast origin/horizon, weather availability and lag/as-issued alignment first. No model is trained here.",
            "context": context, "audit": audit,
            "output": {"path": "ml/data/processed/wind_site_1_prepared.csv", "rows": audit["output_rows"], "columns": audit["output_columns"]},
            "split_boundaries": {"train": "2019-01-01 <= t < 2020-01-01", "validation": "2020-01-01 <= t < 2020-07-01", "test": "2020-07-01 <= t < 2021-01-01"},
            "split_policy": "No shuffle, no fitted imputation/scaling, no cross-split fill. Any future fitted preprocessing must fit on train only; purge overlapping labels once a horizon is defined.",
            "runtime": {"pandas": pd.__version__, "numpy": np.__version__}}


def build_report(manifest: dict[str, Any]) -> str:
    """Render facts separately from transformation decisions and future limitations."""
    a, context = manifest["audit"], manifest["context"]
    def block(value: Any) -> str:
        return "```json\n" + json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n```\n"
    sections = ["# GridCast AI Wind Data Preprocessing Report\n",
        "## 1. Input Dataset\n", f"**FACTS FOUND.** `{manifest['source']}`. SHA-256 `{manifest['raw_sha256']}`. "
        "Verified against the Milestone 1 hash and analysis. Source rows: 70,176; columns: 13; "
        "2019-01-01 00:00 through 2020-12-31 23:45, regular 15 minutes. No schema discrepancy found.\n",
        "## 2. Schema Verification\n", block(a["schema"]),
        "## 3. Sentinel Value Analysis\n", "**FACTS FOUND.** All 11 weather columns contain -99 on the same 138 rows "
        "(0.19665% of observations). No supplied codebook defines it. Negative speed, direction, pressure and humidity "
        "violate header-supported ranges. The temperature and ambiguous-column codes coincide with the same "
        "multi-sensor outage, supporting context-based interpretation rather than a universal temperature cutoff.\n"
        "**TRANSFORMATION DECISION.** LIKELY SENTINEL, not VERIFIED SENTINEL: replace these weather codes with null "
        "in memory. Never apply a blanket replacement to power.\n", block(a["sentinels"]),
        "## 4. Invalid Value Analysis\n", "**FACTS FOUND.** Two zero readings in `Atmosphere (hpa)` coincide with "
        "all-zero weather rows; neighboring pressures are near 889–890 hPa. Zero terrestrial ambient pressure is "
        "invalid.\n**TRANSFORMATION DECISION.** Convert exactly these two pressure values to null. Other weather zeros "
        "are not blanket-changed. Both rows will be accounted for by complete-case selection.\n",
        block(a["transformations"]), block(context["pressure_zero_context"]),
        "## 5. Ambiguous Column Analysis\n", "**FACTS FOUND.** The hub degree column retains a contradictory speed "
        "label and one original null. Its non-sentinel range is 0–358.5; descriptive associations are stronger with "
        "direction than speed. Correlation cannot establish meaning, particularly for circular variables.\n"
        "**TRANSFORMATION DECISION.** UNRESOLVED; **EXCLUDED PENDING SEMANTIC VERIFICATION**. No direction encoding "
        "is applied. Raw data remains intact. Workbook metadata inspected is recorded below and in the manifest.\n",
        block({k: v for k,v in context.items() if k != "pressure_zero_context"}),
        "## 6. Target Validation\n", "**FACTS FOUND.** Target is labelled power in MW, not energy. Nominal 99 MW "
        "is a filename/user-provided rating.\n**TRANSFORMATION DECISION.** Retain valid zero generation and statistical "
        "extremes. No target filling, clipping, scaling or future target features. Rows with missing weather can still "
        "have valid targets; their omission is recorded separately.\n", block({"before": a["target_before"], "after": a["target_after"]}),
        "## 7. Missing Value Strategy\n", "**FACTS FOUND.** Per-column runs below are measured after invalid-value "
        "conversion and before omission. The seven synchronized sentinel runs contain 11, 1, 4, 78, 1, 40 and 3 "
        "observations in chronological order.\n**TRANSFORMATION DECISION.** Drop the unresolved column for semantic "
        "reasons. For retained weather features, omit incomplete rows instead of fabricating long outages. The two "
        "short pressure gaps could support causal filling, but omitting two rows avoids an additional assumption. "
        "Do not interpolate, forward-fill or learn a median. Target values are never imputed. No omission depends "
        "on the excluded hub column's lone null.\n", block(a["missingness"]),
        f"Omitted {len(a['removed_rows'])} rows ({100*len(a['removed_rows'])/a['input_rows']:.5f}%). "
        "Every omitted timestamp and missing column is recorded in `wind_feature_manifest.json` → "
        "`audit.removed_rows`. Raw observations are preserved. The prepared table has gaps; do not interpret "
        "neighboring retained rows as necessarily 15 minutes apart.\n",
        "## 8. Feature Selection\n", table(["Exact original column", "Classification"],
            [[json.dumps(c,ensure_ascii=False),role] for c,role in manifest["original_column_classifications"].items()]),
        "## 9. Time Feature Engineering\n", "**TRANSFORMATION DECISIONS.** Retain the timestamp under its original "
        "header, parsed without timezone conversion. hour=0–23, day_of_week=Monday 0–Sunday 6, month=1–12, "
        "day_of_year=1–365/366 and quarter=1–4. Hour sine/cosine use fractional hours including minutes and seconds "
        "with period 24. Annual sine/cosine use (day_of_year−1+fraction_of_day)/365 or /366 for the timestamp's year. "
        "These deterministic calendars require no fitted parameters or future observations. Source timezone remains unknown.\n",
        "## 10. Wind Feature Engineering\n", "**TRANSFORMATION DECISIONS.** For verified 10/30/50 m direction "
        "headers, compute sin(degrees × π/180) and cos(degrees × π/180). Retain original directions and all four "
        "speed measurements independently. No u/v components exist: no magnitude feature is created. No inferred "
        "hub direction, height aggregation, lag features or wind-shear assumptions are introduced.\n",
        "## 11. Feature Leakage Review\n", "**FACTS FOUND.** Weather issue times and forecast horizon are absent. "
        "Observed weather at a target timestamp is not verified available before a future forecast origin.\n"
        "**TRANSFORMATION DECISIONS.** Calendar features are SAFE FOR FORECASTING; observed weather and its "
        "direction encodings are POTENTIAL LEAKAGE and must not be used as future weather observations. Target "
        "and ambiguous/unreviewed predictors are EXCLUDE. This output is a complete numerical observation table "
        "for subsequent alignment, not an approved operational future-forecast feature matrix. Only calendar "
        "predictors pass the current future-availability gate.\n", block(a["leakage"]),
        "## 12. Final ML Feature Set\n", block({"primary_observations": PRIMARY, "secondary_observations": SECONDARY,
            "engineered": TIME_FEATURES + DIRECTION_FEATURES, "forecast_safe_predictors": TIME_FEATURES,
            "target_not_a_predictor": TARGET, "time_index": TIME}),
        "## 13. Output Dataset\n", block(manifest["output"]),
        "**FACTS FOUND.** CSV has no index column, missing selected values or unexplained -99 codes. "
        "Inputs remain unchanged and output is Git-ignored. Reports and manifest can be tracked.\n"
        "**TRANSFORMATION DECISIONS: chronological split plan.** Fixed calendar boundaries, no random shuffle "
        "and no separate split files. Percentages below refer to retained rows.\n", block(manifest["split_boundaries"]), block(a["split_plan"]),
        manifest["split_policy"] + "\n",
        "Reproduce from the repository root:\n\n```powershell\npython -m ml.data_processing.run_wind_preprocessing\n```\n",
        "## 14. Remaining Limitations\n", "**FACTS FOUND / LIMITATIONS.** No source URL/license, verified sentinel "
        "codebook, site coordinates, weather availability times, hub height or angular reference is supplied. "
        "Semantic conclusions remain conservative. Full-data distributions are diagnostic summaries, never fitted "
        "imputation/scaling parameters. Sentinel and physical-range policies rely on domain validity and synchronized "
        "error evidence rather than optimized test performance. Complete-case selection can introduce missingness "
        "bias. Preserve the omission ledger and original time spacing during future lag construction. Define the "
        "forecast horizon and align available inputs before model training. No models, API changes or future "
        "milestone functionality are included.\n"]
    return "\n".join(sections)


def main() -> None:
    """Verify provenance and Git exclusions before writing separate processed artifacts."""
    source_manifest = json.loads((ROOT / "docs/dataset_sources.json").read_text(encoding="utf-8"))
    hashes = {item["relative_path"]: sha256(ROOT/item["relative_path"]) for item in source_manifest["sources"]}
    for item in source_manifest["sources"]:
        if hashes[item["relative_path"]] != item["sha256"]:
            raise ValueError(f"Original download changed: {item['relative_path']}")
    raw = ROOT / "ml/data/raw/wind" / INPUT_NAME
    digest = sha256(raw)
    if digest != hashes[INPUT_NAME]:
        raise ValueError("Raw selected copy differs from the original/Milestone 1 hash")
    data = load_wind_dataset(raw)
    verify_milestone_one(data, (ROOT/"docs/wind_dataset_analysis.md").read_text(encoding="utf-8"))
    output, audit = prepare_wind_dataset(data)
    manifest = build_manifest(audit, inspect_context(data, raw), digest)
    destination = ROOT/"ml/data/processed/wind_site_1_prepared.csv"
    if destination.resolve().is_relative_to((ROOT/"ml/data/raw").resolve()):
        raise ValueError("Processed destination resolves inside raw data")
    relative = destination.relative_to(ROOT).as_posix()
    ignored = subprocess.run(["git", "check-ignore", "-q", relative], cwd=ROOT)
    tracked = subprocess.run(["git", "ls-files", "--error-unmatch", relative], cwd=ROOT, capture_output=True)
    if ignored.returncode != 0 or tracked.returncode == 0:
        raise ValueError("Processed output must be Git-ignored and untracked before writing")
    for path, original_hash in hashes.items():
        if sha256(ROOT/path) != original_hash:
            raise ValueError(f"Source changed during preparation: {path}")
    if sha256(raw) != digest:
        raise ValueError("Raw selected copy changed during preparation")
    report = build_report(manifest)
    payload = json.dumps(manifest, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    destination.parent.mkdir(parents=True, exist_ok=True)
    output.to_csv(destination, index=False, date_format="%Y-%m-%d %H:%M:%S", float_format="%.15g")
    (ROOT/"docs/wind_feature_manifest.json").write_text(payload, encoding="utf-8")
    (ROOT/"docs/wind_preprocessing_report.md").write_text(report, encoding="utf-8")
    if sha256(raw) != digest or any(sha256(ROOT/p) != h for p,h in hashes.items()):
        raise ValueError("Source integrity changed after output writing")
    print(f"Prepared {len(output):,} rows x {len(output.columns)} columns; omitted {len(audit['removed_rows'])} rows with full ledger.")
    print(f"Saved {destination}; source hashes unchanged. No imputation, model fitting or raw writes.")
    print("Forecasting gate: calendar features safe; observed weather requires origin/horizon alignment.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, IndexError) as exc:
        raise SystemExit(f"Preprocessing failed: {exc}") from exc
