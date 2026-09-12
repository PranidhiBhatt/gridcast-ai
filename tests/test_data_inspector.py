"""Synthetic fixtures only: tests never depend on downloaded energy datasets."""

import hashlib
import json
from shutil import copyfile

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from ml.data_processing.data_inspector import (
    analyze_columns,
    analyze_duplicates,
    analyze_missing_values,
    analyze_numeric_columns,
    analyze_time_series,
    detect_time_columns,
    discover_data_files,
    generate_dataset_report,
    inspect_dataset,
    read_dataset,
)


def test_discovery(tmp_path):
    (tmp_path / "nested").mkdir()
    (tmp_path / "nested/a.csv").write_text("x\n1\n")
    (tmp_path / "book.XLSX").touch()
    (tmp_path / "notes.md").touch()
    (tmp_path / ".venv").mkdir()
    (tmp_path / ".venv/skip.csv").touch()
    assert {p.name for p in discover_data_files(tmp_path)} == {"a.csv", "book.XLSX"}
    with pytest.raises(ValueError, match="does not exist"):
        discover_data_files(tmp_path / "absent")


def test_inspection_preserves_file(tmp_path):
    path = tmp_path / "wind.csv"
    path.write_text("timestamp,speed,power\n2024-01-01 00:00:00,2,1\n2024-01-01 00:15:00,4,3\n")
    before = hashlib.sha256(path.read_bytes()).hexdigest()
    report = inspect_dataset(path)
    assert report["rows"] == 2
    assert report["columns_count"] == 3
    assert report["schema"][1]["name"] == "speed"
    assert report["numeric"]["speed"]["mean"] == 3
    assert '"rows": 2' in generate_dataset_report(report)
    assert hashlib.sha256(path.read_bytes()).hexdigest() == before


def test_missing_constants_and_sparse():
    frame = pd.DataFrame({"a": [1, None, None], "constant": [2, 2, 2], "text": ["1", "bad", None]})
    before = frame.copy(deep=True)
    assert analyze_missing_values(frame)["a"]["count"] == 2
    assert analyze_missing_values(frame)["a"]["percent"] == pytest.approx(200 / 3)
    columns = analyze_columns(frame)
    assert columns[0]["sparse_over_50_percent_missing"]
    assert columns[1]["constant"]
    assert columns[2]["numeric_text_values"] == 1
    assert_frame_equal(frame, before)


def test_duplicates():
    frame = pd.DataFrame({"a": [1, 1, 2, 1], "b": [None, None, "x", None]})
    assert analyze_duplicates(frame) == {"duplicate_rows": 2, "rows_in_duplicate_groups": 3}
    assert analyze_duplicates(pd.DataFrame({"nested": [[1], [1]]}))["duplicate_rows"] == 1


def test_time_detection_and_numeric_calendar_parts():
    frame = pd.DataFrame({"Time(year-month-day h:m:s)": ["2024-01-01"], "year": [2024],
                          "runtime_seconds": [5], "typed": pd.to_datetime(["2024-01-01"])})
    assert detect_time_columns(frame) == ["Time(year-month-day h:m:s)", "year", "typed"]
    assert "unit/calendar" in analyze_time_series(frame["year"])["status"]


def test_time_quality():
    series = pd.Series(["2024-01-01 00:30:00", "2024-01-01 00:00:00", "bad", None,
                        "2024-01-01 00:15:00", "2024-01-01 00:15:00"], name="timestamp")
    result = analyze_time_series(series)
    assert result["parse_failures"] == 1
    assert result["missing"] == 1
    assert result["unique_timestamps"] == 3
    assert result["duplicate_timestamps"] == 1
    assert not result["ascending_valid_values"]
    assert result["estimated_frequency"] == "0 days 00:15:00"
    assert result["regular_unique_spacing"]
    assert "naive" in result["timezone"]


def test_timezone_offsets_and_ambiguous_dates():
    result = analyze_time_series(pd.Series(["2024-01-01T00:00:00Z", "2024-01-01T01:00:00+01:00"]))
    assert result["duplicate_timestamps"] == 1
    assert "explicit offset" in result["timezone"]
    assert analyze_time_series(pd.Series(["01/02/2024"]))["ambiguous_day_month_values"] == 1
    assert "date required" in analyze_time_series(pd.Series(["12:30:00"]))["status"]


def test_numeric_statistics_and_empty_data():
    result = analyze_numeric_columns(pd.DataFrame({"x": [1, 2, 9, None, float("inf")]}))["x"]
    assert result["min"] == 1
    assert result["max"] == 9
    assert result["mean"] == 4
    assert result["median"] == 2
    assert result["missing"] == 1
    assert result["non_finite_non_null"] == 1
    assert analyze_missing_values(pd.DataFrame({"x": []}))["x"]["percent"] == 0
    assert analyze_numeric_columns(pd.DataFrame({"x": [float("nan")]}))["x"]["min"] is None


@pytest.mark.parametrize("extension,content", [
    (".tsv", "a\tb\n1\t2\n"), (".txt", "a;b\n1;2\n"),
    (".json", '[{"a":1,"b":2}]'), (".jsonl", '{"a":1,"b":2}\n'),
])
def test_tabular_formats(tmp_path, extension, content):
    path = tmp_path / f"data{extension}"
    path.write_text(content)
    assert read_dataset(path).to_dict("records") == [{"a": 1, "b": 2}]


def test_excel_sheets(tmp_path):
    path = tmp_path / "data.xlsx"
    # Synthetic workbook creation is confined to the test's temporary directory.
    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        pd.DataFrame({"a": [1]}).to_excel(writer, index=False, sheet_name="first")
        pd.DataFrame({"b": [2, 3]}).to_excel(writer, index=False, sheet_name="second")
    assert inspect_dataset(path, sheet_name="second")["rows"] == 2


def test_clear_read_errors(tmp_path):
    with pytest.raises(FileNotFoundError, match="Dataset not found"):
        read_dataset(tmp_path / "missing.csv")
    path = tmp_path / "bad.bin"
    path.touch()
    with pytest.raises(ValueError, match="Unsupported dataset format"):
        read_dataset(path)
    path = tmp_path / "bad.json"
    path.write_text("not json")
    with pytest.raises(ValueError, match="Cannot read"):
        read_dataset(path)


def test_reproducible_runner_and_integrity_guard(tmp_path):
    from ml.data_processing.run_wind_analysis import run_analysis, sha256

    (tmp_path / "docs").mkdir()
    raw = tmp_path / "ml/data/raw/wind"
    raw.mkdir(parents=True)
    source = tmp_path / "Wind farm site 1 (Nominal capacity-99MW).xlsx"
    pd.DataFrame({"Time(year-month-day h:m:s)": pd.date_range("2024-01-01", periods=3, freq="15min"),
                  "Wind speed at height of 10 meters (m/s)": [1, 2, 3],
                  "Power (MW)": [0, 1, 2]}).to_excel(source, index=False)
    destination = raw / source.name
    copyfile(source, destination)
    baseline = sha256(source)
    manifest = {"sources": [{"relative_path": source.name, "sha256": baseline}],
                "selected_copies": [{"source": source.name, "destination": destination.relative_to(tmp_path).as_posix()}]}
    (tmp_path / "docs/dataset_sources.json").write_text(json.dumps(manifest))
    report = tmp_path / "docs/wind_dataset_analysis.md"
    run_analysis(tmp_path, report)
    first = report.read_bytes()
    run_analysis(tmp_path, report)
    assert report.read_bytes() == first
    assert sha256(source) == sha256(destination) == baseline
    assert b"ACTUAL VERIFIED TARGET" in first
    assert b"## 14. Limitations" in first
    with pytest.raises(ValueError, match="directly inside docs"):
        run_analysis(tmp_path, tmp_path / "ml/data/raw/unsafe.md")
    destination.write_bytes(b"changed fixture")
    with pytest.raises(ValueError, match="does not match original"):
        run_analysis(tmp_path, report)
    assert report.read_bytes() == first


def test_target_coverage_mixed_excel_types():
    from datetime import datetime
    from ml.data_processing.run_wind_analysis import target_coverage

    frame = pd.DataFrame({"Time(year-month-day h:m:s)": ["2024-01-01 00:00:00", datetime(2024, 1, 2), "bad"],
                          "Power (MW)": [1, 2, 3]})
    coverage = target_coverage(frame)
    assert "2024-01-01" in coverage
    assert "2024-01-02" in coverage
    assert "1 parse failures" in coverage
