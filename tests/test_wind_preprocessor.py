"""Synthetic data only; no downloaded workbook required."""

import numpy as np
import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from ml.data_processing.wind_preprocessor import (
    AMBIGUOUS, DIRECTIONS, DIRECTION_FEATURES, EXPECTED, HUMIDITY, PRESSURE,
    PRIMARY, SECONDARY, SPEEDS, TARGET, TEMPERATURE, TIME, TIME_FEATURES, WEATHER,
    analyze_missingness, analyze_sentinel_values, check_feature_leakage,
    chronological_split_plan, create_time_features, create_wind_features,
    handle_missing_values, prepare_wind_dataset, replace_invalid_values,
    select_features, validate_schema, validate_target,
)


@pytest.fixture
def frame() -> pd.DataFrame:
    data = pd.DataFrame({TIME: pd.date_range("2019-12-31 23:30", periods=8, freq="15min")})
    for c in WEATHER:
        data[c] = 5.0
    data[PRESSURE] = 890.0
    data[HUMIDITY] = 40.0
    data[TARGET] = [0., 10., 20., 30., 40., 50., 60., 70.]
    return data[EXPECTED]


def test_sentinel_decisions_and_replacement(frame):
    frame.loc[2, WEATHER] = -99
    frame.loc[3, TEMPERATURE] = -99
    before = frame.copy(deep=True)
    decisions = analyze_sentinel_values(frame)
    assert decisions[SPEEDS[0]]["classification"] == "LIKELY SENTINEL"
    assert decisions[SPEEDS[0]]["percent_rows"] == 12.5
    assert decisions[TEMPERATURE]["classification"] == "UNCERTAIN"
    assert decisions[AMBIGUOUS]["classification"] == "LIKELY SENTINEL"
    result, changes = replace_invalid_values(frame, decisions)
    assert np.isnan(result.loc[2, SPEEDS[0]])
    assert result.loc[3, TEMPERATURE] == -99
    assert changes["columns"][SPEEDS[0]]["sentinels_to_null"] == 1
    assert_frame_equal(frame, before)


def test_synchronous_temperature_sentinel_and_target_protection(frame):
    frame.loc[1, WEATHER] = -99
    frame.loc[1, TARGET] = -99
    decisions = analyze_sentinel_values(frame)
    assert decisions[TEMPERATURE]["classification"] == "LIKELY SENTINEL"
    cleaned, _ = replace_invalid_values(frame, decisions)
    assert np.isnan(cleaned.loc[1, TEMPERATURE])
    assert cleaned.loc[1, TARGET] == -99


def test_zero_pressure_only(frame):
    frame.loc[1, PRESSURE] = 0
    frame.loc[1, SPEEDS[0]] = 0
    result, audit = replace_invalid_values(frame, analyze_sentinel_values(frame))
    assert np.isnan(result.loc[1, PRESSURE])
    assert result.loc[1, SPEEDS[0]] == 0
    assert result.loc[0, TARGET] == 0
    assert audit["zero_pressure_to_null"] == 1


def test_target_validation(frame):
    frame[TARGET] = [0., -1., 100., np.nan, np.inf, 30., 40., 50.]
    result = validate_target(frame)
    assert result["missing"] == 1
    assert result["negative"] == 1
    assert result["above_nominal"] == 2
    assert result["nonfinite_nonnull"] == 1
    assert result["valid_zero_generation"] == 1
    with pytest.raises(ValueError, match="Target quality"):
        prepare_wind_dataset(frame)


def test_time_features_fractional_hours_and_leap_year():
    frame = pd.DataFrame({TIME: pd.to_datetime(["2020-01-01 00:00", "2020-02-29 06:00", "2019-01-01 00:15"])})
    out = create_time_features(frame)
    assert out.loc[0, "day_of_week"] == 2
    assert out.loc[1, "day_of_year"] == 60
    assert out.loc[1, "quarter"] == 1
    assert out.loc[1, "hour_sin"] == pytest.approx(1)
    assert out.loc[2, "hour_sin"] == pytest.approx(np.sin(2*np.pi*.25/24))
    assert out.loc[0, "day_of_year_cos"] == 1
    assert out.loc[1, "day_of_year_sin"] == pytest.approx(np.sin(2*np.pi*(59+.25)/366))
    assert_frame_equal(frame, out[[TIME]])


def test_direction_degrees_and_no_ambiguous_encoding(frame):
    frame[DIRECTIONS[0]] = [0.,90.,180.,270.,360.,0.,90.,180.]
    before = frame.copy(deep=True)
    out = create_wind_features(frame)
    assert out.loc[1, "wind_direction_10m_sin"] == pytest.approx(1)
    assert out.loc[2, "wind_direction_10m_cos"] == pytest.approx(-1)
    assert out.loc[4, "wind_direction_10m_cos"] == pytest.approx(1)
    assert len(set(out.columns)-set(frame.columns)) == 6
    assert_frame_equal(frame, before)


def test_missing_runs_row_ledger_and_excluded_null(frame):
    frame.loc[2:4, SPEEDS[0]] = np.nan
    frame.loc[0, AMBIGUOUS] = np.nan
    report = analyze_missingness(frame, [SPEEDS[0]])[SPEEDS[0]]
    assert report["missing"] == 3
    assert report["max_run"] == 3
    assert report["run_count"] == 1
    assert report["pattern"] == "clustered"
    out, ledger = handle_missing_values(frame)
    assert len(out) == 5 and len(ledger) == 3
    assert 0 in out.index
    assert ledger[0]["missing_columns"] == [SPEEDS[0]]
    assert not out[SPEEDS[0]].isna().any()


def test_selection_and_leakage_fail_closed(frame):
    out = select_features(create_wind_features(create_time_features(frame)))
    assert AMBIGUOUS not in out
    assert len(out.columns) == 27
    assert set(PRIMARY+SECONDARY+TIME_FEATURES+DIRECTION_FEATURES+[TIME,TARGET]) == set(out.columns)
    review = check_feature_leakage([*out.columns, "future_power", AMBIGUOUS])
    assert review["hour_sin"]["classification"] == "SAFE FOR FORECASTING"
    assert review[SPEEDS[0]]["classification"] == "POTENTIAL LEAKAGE"
    assert review["wind_direction_10m_sin"]["classification"] == "POTENTIAL LEAKAGE"
    for c in (TARGET, AMBIGUOUS, "future_power"):
        assert review[c]["classification"] == "EXCLUDE"


def test_prepare_deterministic_no_input_mutation(frame):
    frame.loc[2, WEATHER] = -99
    frame.loc[3, PRESSURE] = 0
    before = frame.copy(deep=True)
    first, audit = prepare_wind_dataset(frame)
    second, _ = prepare_wind_dataset(frame)
    assert first.shape == (6,27)
    assert not first.isna().any().any()
    assert audit["input_rows"] == audit["output_rows"] + len(audit["removed_rows"])
    assert_frame_equal(first, second)
    assert_frame_equal(frame, before)
    assert first.iloc[0][TARGET] == 0


def test_past_output_independent_of_future_values(frame):
    first, _ = prepare_wind_dataset(frame)
    changed = frame.copy()
    changed.loc[5:, PRIMARY+SECONDARY] = 10.0
    second, _ = prepare_wind_dataset(changed)
    assert_frame_equal(first.iloc[:5], second.iloc[:5])


def test_split_boundaries():
    data = pd.DataFrame({TIME: pd.to_datetime(["2019-12-31 23:45", "2020-01-01", "2020-06-30 23:45", "2020-07-01"], format="mixed")})
    plan = chronological_split_plan(data)
    assert [plan[k]["rows"] for k in ("train","validation","test")] == [1,2,1]
    assert plan["validation"]["percent"] == 50


def test_schema_and_unresolved_invalid_values(frame):
    with pytest.raises(ValueError, match="schema mismatch"):
        validate_schema(frame.drop(columns=AMBIGUOUS))
    bad = frame.copy()
    bad.loc[1, TIME] = bad.loc[0, TIME]
    with pytest.raises(ValueError, match="unique"):
        validate_schema(bad)
    bad = frame.copy()
    bad.loc[1, HUMIDITY] = 101
    with pytest.raises(ValueError, match="Unresolved invalid"):
        prepare_wind_dataset(bad)
