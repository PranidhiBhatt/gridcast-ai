"""Synthetic solar policy tests; downloaded workbooks are never test dependencies."""

import hashlib

import numpy as np
import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from ml.data_processing.solar_preprocessor import (
    CALENDAR, EXPECTED, FEATURES, GHI, HUMIDITY, IRRADIANCE, ORIGINAL_FEATURES,
    PRESSURE, TARGET, TEMPERATURE, TIME, TOTAL, WEATHER, calendar_features,
    chronological_split_plan, load_solar_dataset, parse_timestamps,
    prepare_solar_dataset, semantic_diagnostics, validate_feature_list, validate_schema,
)
from ml.data_processing.run_solar_preprocessing import verify_hashes


@pytest.fixture
def frame():
    data = pd.DataFrame({TIME: pd.date_range("2019-12-31 23:15:00", periods=8, freq="15min")})
    for c in IRRADIANCE:
        data[c] = 10.
    data[TEMPERATURE] = -5.
    data[PRESSURE] = 910.
    data[HUMIDITY] = 40.
    data[TARGET] = [0., 0., .03, 1., 2., 3., 4., 5.]
    return data[EXPECTED]


def test_schema_preserves_exact_headers(frame):
    assert validate_schema(frame)["rows"] == 8
    for bad in [frame.rename(columns={TEMPERATURE: TEMPERATURE.strip()}), frame.assign(future_power=1), frame.iloc[0:0]]:
        with pytest.raises(ValueError):
            validate_schema(bad)
    with pytest.raises(ValueError, match="numeric"):
        validate_schema(frame.assign(**{GHI: "10"}))


@pytest.mark.parametrize("values", [
    ["2020-01-01 00:00:00", "bad"],
    ["01/02/2020 00:00:00", "02/02/2020 00:00:00"],
    ["2020-01-01 00:00:00Z", "2020-01-02 00:00:00Z"],
    ["2020-01-02 00:00:00", "2020-01-01 00:00:00"],
    ["2020-01-01 00:00:00", "2020-01-01 00:00:00"], [2020, 2021],
])
def test_timestamp_failures(values):
    with pytest.raises(ValueError):
        parse_timestamps(pd.Series(values))


def test_timezone_and_naive_clock():
    with pytest.raises(ValueError, match="Timezone-aware"):
        parse_timestamps(pd.Series(pd.date_range("2020-01-01", periods=2, tz="UTC")))
    values = pd.Series(["2020-02-29 06:15:00", "2020-02-29 06:30:00"])
    parsed = parse_timestamps(values)
    assert parsed.dt.tz is None
    assert parsed.iloc[0] == pd.Timestamp("2020-02-29 06:15:00")


def test_sentinel_omission_ledger_and_raw_preservation(frame):
    frame.loc[1, WEATHER] = -99
    before = frame.copy(deep=True)
    output, audit, log = prepare_solar_dataset(frame)
    assert len(output) == 7 and len(log) == 1
    assert log.iloc[0].source_excel_row == 3
    assert "likely -99 sentinel" in log.iloc[0].reason
    assert HUMIDITY not in log.iloc[0].affected_columns
    assert audit["missing_after_handling"][HUMIDITY]["count"] == 1
    assert audit["zero_targets_omitted_for_missing_inputs"] == 1
    assert (output[TEMPERATURE] == -5).all()
    assert_frame_equal(frame, before)


def test_humidity_exclusion_does_not_delete_otherwise_usable_rows(frame):
    frame[HUMIDITY] = [-99, 6553.5, -1, 101, np.nan, 0, 100, np.inf]
    output, _, log = prepare_solar_dataset(frame)
    assert len(output) == 8 and log.empty
    assert HUMIDITY not in output
    assert output[TARGET].equals(frame[TARGET])


def test_zeros_high_power_and_zero_ghi_retained(frame):
    frame.loc[2, GHI] = 0
    frame.loc[7, TARGET] = 51.0
    output, audit, _ = prepare_solar_dataset(frame)
    assert audit["zero_generation_after"]["zero_count"] == 2
    assert audit["positive_power_zero_ghi_retained"] == 1
    assert output.loc[7, TARGET] == 51
    assert output.loc[2, TARGET] == .03


def test_missing_policy_and_no_fill(frame):
    frame.loc[1:2, TOTAL] = np.nan
    frame.loc[4, PRESSURE] = np.inf
    frame.loc[5, TARGET] = np.nan
    output, audit, log = prepare_solar_dataset(frame)
    assert list(output.index) == [0, 3, 6, 7]
    assert len(log) == audit["omitted_rows"] == 4
    assert "non-finite measurement" in log.loc[log.source_excel_row.eq(6), "reason"].iloc[0]
    assert "original missing target" in log.iloc[-1].reason
    assert not output.isna().any().any()
    assert output[TIME].diff().iloc[1].total_seconds() == 2700


@pytest.mark.parametrize("column,value", [(TARGET, -99.), (GHI, -1.), (PRESSURE, 0.)])
def test_unreviewed_values_fail_without_correction(frame, column, value):
    frame.loc[0, column] = value
    with pytest.raises(ValueError, match="review"):
        prepare_solar_dataset(frame)
    assert frame.loc[0, column] == value


def test_calendar_leap_year_fractional_clock():
    dates = pd.to_datetime(["2019-03-01 06:00:00", "2020-02-29 06:00:00", "2020-03-01 00:15:00"])
    result = calendar_features(pd.DataFrame({TIME: dates}))
    assert result.loc[1, "day_of_year"] == 60
    assert result.loc[1, "day_of_week"] == 5
    assert result.loc[1, "hour_sin"] == pytest.approx(1)
    assert result.loc[0, "annual_sin"] == pytest.approx(np.sin(2*np.pi*(59+.25)/365))
    assert result.loc[1, "annual_sin"] == pytest.approx(np.sin(2*np.pi*(59+.25)/366))
    assert result.loc[2, "hour_sin"] == pytest.approx(np.sin(2*np.pi*.25/24))
    assert set(result) == {TIME, *CALENDAR}


def test_target_independence_and_future_independence(frame):
    first, _, _ = prepare_solar_dataset(frame)
    changed = frame.copy()
    changed[TARGET] = 40.
    changed.loc[6:, ORIGINAL_FEATURES] = 100.
    second, _, _ = prepare_solar_dataset(changed)
    assert_frame_equal(first[FEATURES].iloc[:6], second[FEATURES].iloc[:6])
    assert list(first) == [TIME, *FEATURES, TARGET]
    for features in [FEATURES + [TARGET], FEATURES + ["Power_lag"], FEATURES + [HUMIDITY], FEATURES[:-1]]:
        with pytest.raises(ValueError, match="allowlist"):
            validate_feature_list(features)


def test_chronological_splits():
    frame = pd.DataFrame({TIME: pd.to_datetime(["2019-12-31 23:45:00", "2020-01-01 00:00:00", "2020-06-30 23:45:00", "2020-07-01 00:00:00"])})
    plan = chronological_split_plan(frame)
    assert [plan[k]["rows"] for k in ["train", "validation", "test"]] == [1, 2, 1]
    assert plan["validation"]["percent"] == 50
    with pytest.raises(ValueError, match="coverage"):
        chronological_split_plan(pd.DataFrame({TIME: pd.to_datetime(["2021-01-01"])}))


def test_file_integrity_and_repeatable_preparation(tmp_path, frame):
    path = tmp_path / "solar.xlsx"
    frame.to_excel(path, index=False, sheet_name="sheet1")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    data = load_solar_dataset(path)
    first, _, ledger = prepare_solar_dataset(data)
    second, _, second_ledger = prepare_solar_dataset(load_solar_dataset(path))
    assert_frame_equal(first, second)
    assert_frame_equal(ledger, second_ledger)
    verify_hashes(tmp_path, {"solar.xlsx": digest})
    path.write_bytes(b"changed fixture")
    with pytest.raises(ValueError, match="SHA-256"):
        verify_hashes(tmp_path, {"solar.xlsx": digest})


def test_semantic_diagnostics_do_not_impose_formula(frame):
    frame.loc[1, WEATHER] = -99
    frame.loc[3, HUMIDITY] = 6553.5
    before = frame.copy(deep=True)
    result = semantic_diagnostics(frame)
    assert result["sentinels"]["all_six_coincident_rows"] == 1
    assert result["humidity"]["outside_0_100"] == 2
    assert result["humidity"]["above100"] == 1
    assert_frame_equal(frame, before)
