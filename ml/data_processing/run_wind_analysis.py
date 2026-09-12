"""Reproduce Milestone 1 diagnostics without extracting archives or changing data.

Run from the repository root: python -m ml.data_processing.run_wind_analysis
RAR inspection requires a libarchive-compatible `tar` executable (Windows ships one).
"""

from __future__ import annotations

import argparse
import hashlib
import io
import itertools
import json
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any

import pandas as pd

from ml.data_processing.data_inspector import analyze_time_series, inspect_dataset

ROOT = Path(__file__).resolve().parents[2]
TIME = "Time(year-month-day h:m:s)"
TARGET = "Power (MW)"


def sha256(path: Path) -> str:
    """Hash source bytes in bounded chunks."""
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def archive_members(path: Path) -> list[tuple[str, int]]:
    """List RAR file members using libarchive tar; fail rather than skip data."""
    if not shutil.which("tar"):
        raise RuntimeError("RAR discovery requires libarchive-compatible tar on PATH.")
    result = subprocess.run(["tar", "-tvf", str(path)], capture_output=True, check=True)
    members = []
    for line in result.stdout.decode("utf-8", errors="strict").splitlines():
        if not line.startswith("-"):
            continue
        match = re.match(r"^\S+\s+\S+\s+\S+\s+\S+\s+(\d+)\s+\S+\s+\d+\s+\S+\s+(.+)$", line)
        if not match:
            raise ValueError(f"Cannot parse archive listing: {line}")
        members.append((match[2], int(match[1])))
    return members


def table(headers: list[str], rows: list[list[Any]]) -> str:
    """Render Markdown without requiring an extra table library."""
    def cell(value: Any) -> str:
        return str(value).replace("|", "\\|").replace("\n", " ")
    return "\n".join(["| " + " | ".join(headers) + " |",
                      "| " + " | ".join("---" for _ in headers) + " |"] +
                     ["| " + " | ".join(cell(v) for v in row) + " |" for row in rows]) + "\n"


def feature_role(column: str) -> tuple[str, str]:
    """Recommendations based on exact observed headers, not learned feature importance."""
    lower = column.lower()
    if column == TARGET:
        return "EXCLUDE", "Prediction target; exclude from simultaneous predictors to prevent leakage."
    if column == TIME:
        return "OPTIONAL FEATURE", "Time index for future calendar features; source timezone unknown."
    if "wind speed" in lower and "(m/s)" in lower:
        return "PRIMARY FEATURE", "Wind speed at the height stated in the header; metres per second."
    if "wind direction" in lower:
        return "PRIMARY FEATURE", "Direction at the height stated in the header; degree symbol; reference convention unknown."
    if "wind speed" in lower:
        return "EXCLUDE", "Ambiguous: speed label with degree unit; verify before treating as hub direction."
    if "temperature" in lower:
        return "SECONDARY FEATURE", "Air temperature; degrees Celsius in header."
    if "atmosphere" in lower:
        return "SECONDARY FEATURE", "Inferred air pressure from hpa unit; metadata confirmation recommended."
    if "humidity" in lower:
        return "SECONDARY FEATURE", "Relative humidity; percent in header."
    return "EXCLUDE", "Meaning not verified."


def physical_flags(frame: pd.DataFrame) -> dict[str, int]:
    """Flag header-supported range concerns without deleting or correcting values."""
    flags = {}
    for c in frame.select_dtypes(include="number"):
        flags[f"{c}: values equal to -99 (possible undocumented sentinel)"] = int((frame[c] == -99).sum())
        if "wind speed" in c.lower() and "(m/s)" in c:
            flags[f"{c}: negative speed"] = int((frame[c] < 0).sum())
        if "(˚)" in c:
            flags[f"{c}: outside [0, 360]"] = int(((frame[c] < 0) | (frame[c] > 360)).sum())
        if "humidity" in c.lower():
            flags[f"{c}: outside [0, 100]"] = int(((frame[c] < 0) | (frame[c] > 100)).sum())
        if "(hpa)" in c.lower():
            flags[f"{c}: non-positive pressure"] = int((frame[c] <= 0).sum())
    if TARGET in frame:
        flags["Power (MW): negative output (investigate, not automatically invalid)"] = int((frame[TARGET] < 0).sum())
    return flags


def target_coverage(frame: pd.DataFrame) -> str:
    """Describe non-null target coverage using parsed timestamps, including mixed Excel types."""
    if TARGET not in frame or TIME not in frame:
        return "unavailable: target or timestamp absent"
    summary = analyze_time_series(frame.loc[frame[TARGET].notna(), TIME])
    return f"{summary.get('earliest')} to {summary.get('latest')}; {summary.get('parse_failures', 'unknown')} parse failures"


def run_analysis(root: Path, output: Path) -> None:
    """Inspect selected raw files and every archived wind workbook, then write Markdown."""
    manifest_path = root / "docs/dataset_sources.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    before = {}
    for item in manifest["sources"]:
        path = root / item["relative_path"]
        if not path.is_file():
            raise FileNotFoundError(f"Required original download missing: {path}")
        before[item["relative_path"]] = sha256(path)
        if before[item["relative_path"]] != item["sha256"]:
            raise ValueError(f"Original source differs from discovery SHA-256: {path}")
    inventory = []
    reports = []
    frames = {}
    selected = sorted((root / "ml/data/raw/wind").glob("*.xlsx"))
    if not selected:
        raise FileNotFoundError("No selected wind XLSX files in ml/data/raw/wind; see docs/dataset_sources.json.")
    selected_hashes = {p.relative_to(root).as_posix(): sha256(p) for p in selected}
    for copy in manifest["selected_copies"]:
        if selected_hashes.get(copy["destination"]) != before[copy["source"]]:
            raise ValueError(f"Selected copy does not match original: {copy['destination']}")

    def inspect_excel(data: Any, label: str, size: int) -> list[str]:
        columns = []
        with pd.ExcelFile(data, engine="openpyxl") as book:
            for sheet in book.sheet_names:
                frame = book.parse(sheet)
                columns.extend(map(str, frame.columns))
                report = inspect_dataset(label, data=frame, size_bytes=size, sheet_name=sheet)
                report["physical_flags"] = physical_flags(frame)
                reports.append(report)
                frames[f"{label}::{sheet}"] = frame
                print(f"Inspected {label} [{sheet}]: {len(frame):,} rows, {len(frame.columns)} columns", flush=True)
        return columns

    for item in manifest["sources"]:
        label = item["relative_path"]
        path = root / label
        columns = []
        if path.suffix == ".xlsx":
            # The selected copy is inspected below; avoid reading its original twice.
            if "Wind" not in path.name:
                with pd.ExcelFile(path) as book:
                    columns = [str(c) for sheet in book.sheet_names for c in book.parse(sheet, nrows=5).columns]
        inventory.append([label, path.name, path.suffix, path.stat().st_size,
                          "yes (filename)" if "wind" in label.lower() or label.startswith("WF_") else "unknown",
                          "yes (filename)" if "solar" in label.lower() or label.startswith("SS_") else "unknown",
                          "yes (Power header)" if TARGET in columns else "see members/selected copy" if path.suffix in {".rar", ".xlsx"} else "not tabular",
                          "yes (weather headers)" if columns else "see members/selected copy" if path.suffix in {".rar", ".xlsx"} else "not tabular"])
        if path.suffix == ".rar":
            for member, size in archive_members(path):
                wind = "wind" in member.lower()
                cols = []
                if wind and Path(member).suffix.lower() == ".xlsx":
                    content = subprocess.run(["tar", "-xOf", str(path), member], capture_output=True, check=True).stdout
                    if len(content) != size:
                        raise ValueError(f"Archive member size mismatch: {member}")
                    cols = inspect_excel(io.BytesIO(content), f"{label}!{member}", size)
                inventory.append([f"{label}!{member}", Path(member).name, Path(member).suffix, size,
                                  "yes (headers)" if wind and cols else "no indication",
                                  "yes (filename only)" if "solar" in member.lower() else "no indication",
                                  "yes (Power header)" if TARGET in cols else "unverified",
                                  "yes (wind/weather headers)" if cols else "unverified"])
    for path in selected:
        label = str(path.relative_to(root)).replace("\\", "/")
        inspect_excel(path, label, path.stat().st_size)

    selected_report = next(r for r in reports if r["file"].replace("\\", "/").startswith("ml/data/raw/wind/"))
    parts = ["# GridCast AI Wind Dataset Analysis\n",
             "## 1. Dataset Source and Discovery\n",
             f"**FACTS FROM ACTUAL DATA.** Discovery root: `{root}`. Parent `{root.parent}` contained this project only. "
             "Two extracted Excel workbooks, two RAR archives and two correlation PNGs were found at the repository root. "
             "Archive listings contain six wind and eight solar workbooks each. No external source URL, license, "
             "site coordinates, data dictionary or processing methodology was found among these local files. "
             "Archive names identify versions only; they do not prove how processing was performed.\n",
             "Every archived wind workbook and every sheet was inspected in memory. Solar headers were inspected only "
             "in the extracted site 1 file; archived solar files were inventoried by name and size. PNG contents were "
             "not used as measurement evidence. Sizes below are bytes (uncompressed for archive members).\n",
             "Source and selected-copy SHA-256 hashes are recorded in `docs/dataset_sources.json` and checked before "
             "and after every run. The source manifest is a discovery baseline, not a publisher authenticity guarantee.\n",
             "## 2. Available Dataset Files\n",
             table(["Relative path (! denotes archive member)", "File name", "Extension", "Bytes", "Wind", "Solar", "Generation", "Weather"], inventory),
             "## 3. Selected Wind Data Files\n",
             "**FACTS.** Only the extracted wind site 1 workbook was copied, without changing bytes, to "
             "`ml/data/raw/wind/Wind farm site 1 (Nominal capacity-99MW).xlsx`. Its original remains at the root. "
             "All 12 archived wind workbooks are comparison candidates, inspected without permanent extraction. "
             "No solar copy was necessary. Raw directories, root downloads and archives are ignored by Git.\n",
             table(["Inspected file", "Sheet", "Format", "Bytes", "Rows", "Columns"],
                   [[r["file"], r["sheet"], r["format"], r["size_bytes"], r["rows"], r["columns_count"]] for r in reports]),
             "## 4. Dataset Schema\n",
             "**FACTS.** Exact headers (including whitespace) are JSON-quoted below. Types are Pandas-inferred. "
             "Statistics exclude null and infinite values; missing and non-finite counts are reported separately. "
             "Samples are the first five rows in source order.\n"]
    for r in reports:
        parts += [f"### {r['file']} [{r['sheet']}]\n",
                  table(["Exact column", "dtype", "Missing", "Min", "Max", "Mean", "Median"],
                        [[json.dumps(c["name"], ensure_ascii=False), c["dtype"], c["missing"],
                          *[r["numeric"].get(c["name"], {}).get(k, "—") for k in ("min", "max", "mean", "median")]] for c in r["schema"]]),
                  "```json\n" + json.dumps(r["sample"], ensure_ascii=False, indent=2) + "\n```\n"]
    parts += ["## 5. Timestamp and Time-Series Analysis\n",
              "**FACTS.** Parsing is diagnostic only. Frequency is calculated from sorted unique valid timestamps; "
              "it does not imply the original rows are ordered or gap-free. UTC in the diagnostic output is a "
              "comparison representation, not a verified source timezone.\n"]
    for r in reports:
        parts += [f"### {r['file']} [{r['sheet']}]\n", "```json\n" + json.dumps(r["time"], indent=2) + "\n```\n"]
    parts += ["## 6. Verified Wind Generation Target\n",
              "**ACTUAL VERIFIED TARGET: `Power (MW)`** in the wind-farm workbooks. The wind-farm file context and "
              "explicit power header support wind output measured as **POWER**, in **MW**. It is not an energy "
              "measurement, capacity factor or normalized output. This verifies the column meaning from local "
              "headers, not the measurement provenance, sensor calibration, or gross/net/export convention.\n",
              table(["File", "Target", "dtype", "Min MW", "Max MW", "Missing", "Non-null target time coverage"],
                    [[r["file"], TARGET if TARGET in r["numeric"] else "NO VERIFIED WIND GENERATION TARGET FOUND",
                      next((c["dtype"] for c in r["schema"] if c["name"] == TARGET), "—"),
                      r["numeric"].get(TARGET, {}).get("min"), r["numeric"].get(TARGET, {}).get("max"),
                      r["numeric"].get(TARGET, {}).get("missing"),
                      target_coverage(frames[f"{r['file']}::{r['sheet']}"])]
                     for r in reports]),
              "## 7. Primary Feature Candidates\n", "**RECOMMENDATIONS** for the selected site 1 original, based on headers rather than model experiments.\n"]
    def feature_table(role: str) -> str:
        return table(["Exact column", "Inferred description", "dtype", "Missing", "Range", "Recommendation"],
                     [[json.dumps(c["name"], ensure_ascii=False), feature_role(c["name"])[1], c["dtype"], c["missing"],
                       f"{selected_report['numeric'].get(c['name'], {}).get('min')} to {selected_report['numeric'].get(c['name'], {}).get('max')}", role]
                      for c in selected_report["schema"] if feature_role(c["name"])[0] == role])
    parts += [feature_table("PRIMARY FEATURE"), "## 8. Secondary Feature Candidates\n", feature_table("SECONDARY FEATURE"),
              "### Optional and excluded columns\n", feature_table("OPTIONAL FEATURE"), feature_table("EXCLUDE"),
              "## 9. Potential Derived Features\n",
              "**RECOMMENDATIONS ONLY; nothing derived yet.** The timestamp supports hour, day_of_week, month and "
              "day_of_year once timezone is established. Verified direction columns support sine/cosine encodings "
              "once angular convention is confirmed. Multi-height speed measurements support investigation of "
              "speed differences or wind shear after height and sensor metadata checks. No u/v wind components "
              "were identified, so a component-based wind_speed_magnitude is not recommended. Hub height in metres "
              "is unspecified; do not assume it.\n",
              "## 10. Data Quality Analysis\n",
              "**FACTS.** Nulls and distributions are in section 4; timestamp issues are in section 5. Sparse means "
              ">50% null. IQR flags use 1.5 × IQR and are statistical candidates, not proof of invalid readings. "
              "Negative power may reflect consumption or measurement conventions; no automatic correction is justified. "
              "Negative temperature alone is not invalid. No external schema exists to conclusively validate all types. "
              "Repeated -99 values are counted as possible undocumented sentinels, not automatically converted to null. "
              "IQR flags on angles require circular interpretation; they are not physical validity tests.\n"]
    for r in reports:
        issues = {"duplicates": r["duplicates"], "constant_columns": [c["name"] for c in r["schema"] if c["constant"]],
                  "sparse_columns": [c["name"] for c in r["schema"] if c["sparse_over_50_percent_missing"]],
                  "physical_range_checks": r["physical_flags"],
                  "numeric_text_candidates": [c for c in r["schema"] if c["numeric_text_values"]],
                  "non_finite_values": {k: v["non_finite_non_null"] for k, v in r["numeric"].items()},
                  "iqr_outlier_counts": {k: v["iqr_outliers"] for k, v in r["numeric"].items()}}
        parts += [f"### {r['file']} [{r['sheet']}]\n", "```json\n" + json.dumps(issues, ensure_ascii=False, indent=2) + "\n```\n"]
    parts += ["**RECOMMENDED ACTIONS.** Validate null handling per column, review flagged ranges against source metadata, "
              "confirm the contradictory hub-speed/degree header, verify whether -99 encodes missing observations, "
              "investigate zero pressure, and decide target-quality policies before any cleaning.\n",
              "## 11. Dataset Compatibility and Merge Analysis\n",
              "**FACTS.** Wind files have a timestamp column and site identifiers in filenames, not explicit row-level "
              "plant/site keys. Same timestamps across different sites are not evidence of co-location. Identical "
              "headers imply compatible labelled units only; timezone and measurement conventions remain unverified. "
              "The table evaluates every pair of wind candidates, including the selected copy. No joins were performed.\n"]
    pairs = []
    time_keys = {key: set(pd.to_datetime(frame[TIME], format="mixed", errors="coerce", utc=True).dropna())
                 for key, frame in frames.items() if TIME in frame}
    for (a, fa), (b, fb) in itertools.combinations(frames.items(), 2):
        site_a = re.search(r"site (\d+)", a)
        site_b = re.search(r"site (\d+)", b)
        same_site = bool(site_a and site_b and site_a[1] == site_b[1])
        if fa.equals(fb):
            classification, reason = "MERGE READY", "Identical tables; redundant copy. Select one; do not append duplicates."
        elif TIME in fa and TIME in fb:
            classification = "MERGE REQUIRES PREPROCESSING"
            reason = "Same filename site; original/processed conflict policy needed." if same_site else "Different filename sites; add verified site keys; avoid timestamp-only join."
        else:
            classification, reason = "NO CLEAR MERGE KEY", "No common verified timestamp."
        overlap = len(time_keys[a].intersection(time_keys[b])) if a in time_keys and b in time_keys else 0
        pairs.append([a, b, classification, overlap, "same labelled units" if list(fa.columns) == list(fb.columns) else "schema differs", reason])
    parts += [table(["A", "B", "Classification", "Shared timestamps", "Units/schema", "Reason"], pairs),
              "Time coverage and interval distributions for each pair's inputs are in section 5. Even where 15-minute "
              "spacing matches, gaps, calendar coverage and undocumented timezone must be resolved before joining. "
              "Wind/solar site 1 identifiers belong to different naming domains; no shared physical site is established "
              "and no wind/solar join is recommended.\n",
              "## 12. Recommended Dataset for Wind Model\n",
              "**RECOMMENDATION.** Start Milestone 2 with the selected original wind site 1 workbook. It contains "
              "co-recorded weather and labelled MW power, so no cross-file join is needed for an initial single-site "
              "dataset. Keep the publisher-labelled processed variant for comparison until its transformations are "
              "documented. Other sites are potential later evaluation datasets, not automatically interchangeable rows.\n",
              "## 13. Recommended Preprocessing for Milestone 2\n",
              "**RECOMMENDATIONS; NOT IMPLEMENTED.**\n\n"
              "1. Obtain source URL, license, timezone, site/sensor metadata, hub height, direction reference and processing history.\n"
              "2. Resolve the hub degree-column label before assigning it a feature meaning.\n"
              "3. Establish timestamp format/timezone, inspect gaps and duplicates by site, and retain original values for audit.\n"
              "4. Verify possible -99 sentinels and zero pressure, then define missing-value and suspicious-output policies; "
              "do not blindly clip negative MW or replace target nulls.\n"
              "5. Validate units and ranges, preserve column mappings, and evaluate circular direction/calendar features.\n"
              "6. Establish forecast horizon and feature availability; contemporaneous weather is not proof of future forecast availability.\n"
              "7. Plan chronological train/validation/test boundaries before fitting any imputation or scaling; prevent time leakage.\n",
              "## 14. Limitations and Missing Information\n",
              "**FACTS / LIMITATIONS.** Header-based semantics do not establish measured versus simulated weather, "
              "forecast issue times, turbine availability, curtailment, capacity changes, or power metering convention. "
              "Filename nominal capacities are labels, not independently verified ratings. Solar archives are inventory-only. "
              "No model, cleaned dataset, derived features, database or API change is produced. The reproducible runner "
              "requires the original six downloads in their documented locations, the selected raw copy, Pandas, openpyxl "
              "and libarchive-compatible tar. Missing or changed sources fail explicitly.\n",
              "Reproduce from the repository root:\n\n```powershell\npython -m ml.data_processing.run_wind_analysis\n```\n"]
    for label, digest in before.items():
        if sha256(root / label) != digest:
            raise RuntimeError(f"Source changed during analysis: {label}")
    for label, digest in selected_hashes.items():
        if sha256(root / label) != digest:
            raise RuntimeError(f"Selected raw file changed during analysis: {label}")
    output = output.resolve()
    if output.suffix.lower() != ".md" or output.parent != (root / "docs").resolve():
        raise ValueError("Report output must be a Markdown file directly inside docs/.")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(parts), encoding="utf-8")
    print(f"Generated {output}; {len(reports)} wind tables; all source and raw hashes unchanged.", flush=True)


def main() -> None:
    """CLI entry point with concise actionable errors."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "docs/wind_dataset_analysis.md")
    args = parser.parse_args()
    try:
        run_analysis(ROOT, args.output)
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"Analysis failed: {exc}\n")


if __name__ == "__main__":
    main()
