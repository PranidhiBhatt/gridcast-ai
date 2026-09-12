"""Fast synthetic checks for chronological estimation baselines."""

import copy
import hashlib
import json

import joblib
import numpy as np
import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from ml.models.wind_baseline import (
    calculate_metrics, evaluate_models, load_feature_configuration, load_prepared_dataset,
    prediction_output, review_feature_configuration, review_split_overlap, select_best_model,
    split_chronologically, train_models, validate_prepared_dataset, verify_chronological_order,
)


@pytest.fixture
def config(tmp_path):
    manifest = {"primary_features":["Wind speed (m/s)"],"secondary_features":[],
        "engineered_features":["hour","wind_direction_10m_sin"],"forecast_safe_predictors":["hour"],
        "target_column":"Power (MW)","timestamp_column":"timestamp","nominal_capacity_MW":99,
        "excluded_columns":{"ambiguous_hub":"unresolved"},
        "original_column_classifications":{"Wind speed (m/s)":"PRIMARY FEATURE"},
        "leakage_decisions":{"Wind speed (m/s)":{"classification":"POTENTIAL LEAKAGE"},
            "hour":{"classification":"SAFE FOR FORECASTING"},
            "wind_direction_10m_sin":{"classification":"POTENTIAL LEAKAGE"}}}
    path = tmp_path/"manifest.json"
    path.write_text(json.dumps(manifest))
    return load_feature_configuration(path)


@pytest.fixture
def data():
    times = pd.DatetimeIndex([*pd.date_range("2019-12-01",periods=32,freq="15min"),
                             *pd.date_range("2020-01-01",periods=16,freq="15min"),
                             *pd.date_range("2020-07-01",periods=16,freq="15min")])
    rng = np.random.default_rng(123)
    wind = rng.uniform(1,15,len(times))
    angle = np.sin(np.arange(len(times)))
    return pd.DataFrame({"timestamp":times,"Wind speed (m/s)":wind,"hour":times.hour,
                         "wind_direction_10m_sin":angle,"Power (MW)":2*wind+5+angle})


def test_load_and_schema_validation(tmp_path,data,config):
    path = tmp_path/"prepared.csv"
    data.to_csv(path,index=False)
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    loaded = load_prepared_dataset(path,config)
    assert loaded.shape == (64,5)
    assert validate_prepared_dataset(loaded,config)["missing_values"] == 0
    assert hashlib.sha256(path.read_bytes()).hexdigest() == digest
    for bad in (data.drop(columns="Power (MW)"),data.assign(future_power=data["Power (MW)"])):
        with pytest.raises(ValueError,match="schema"):
            validate_prepared_dataset(bad,config)
    bad = data.copy()
    bad.loc[0,"Wind speed (m/s)"] = np.nan
    with pytest.raises(ValueError,match="non-finite"):
        validate_prepared_dataset(bad,config)


def test_chronology_and_boundaries(data,config):
    splits = split_chronologically(data,"timestamp")
    assert [len(splits[s]) for s in ("train","validation","test")] == [32,16,16]
    assert max(splits["train"]["timestamp"]) < min(splits["validation"]["timestamp"])
    assert max(splits["validation"]["timestamp"]) < min(splits["test"]["timestamp"])
    review = review_split_overlap(splits,config)
    assert all(v["timestamp_overlap"] == v["identical_predictor_target_signatures"] == 0 for v in review.values())
    with pytest.raises(ValueError,match="chronologically"):
        verify_chronological_order(data.iloc[::-1],"timestamp")
    bad = data.copy()
    bad.loc[1,"timestamp"] = bad.loc[0,"timestamp"]
    with pytest.raises(ValueError,match="unique"):
        split_chronologically(bad,"timestamp")


def test_duplicate_records_across_splits(data,config):
    splits = split_chronologically(data,"timestamp")
    columns = config["features"]+[config["target"]]
    splits["test"].loc[splits["test"].index[0],columns] = splits["train"].iloc[0][columns].values
    with pytest.raises(ValueError,match="Cross-split duplicate"):
        review_split_overlap(splits,config)


def test_feature_target_separation_and_leakage(data,config):
    assert config["target"] not in config["features"]
    review = review_feature_configuration(config)
    assert review["Wind speed (m/s)"]["estimation"] == "SAFE FOR SAME-TIMESTAMP ESTIMATION"
    assert review["Wind speed (m/s)"]["future_use"] == "CONDITIONAL FOR FUTURE FORECASTING"
    assert review["timestamp"]["estimation"] == "EXCLUDE"
    for column in ("Power (MW)","timestamp","ambiguous_hub","future_power"):
        altered = copy.deepcopy(config)
        altered["features"].append(column)
        with pytest.raises(ValueError):
            review_feature_configuration(altered)
    bad = data.copy()
    bad["Wind speed (m/s)"] = bad["Power (MW)"]
    with pytest.raises(ValueError,match="target-copy"):
        validate_prepared_dataset(bad,config)


def test_metrics_known_values():
    result = calculate_metrics([0,2],[1,1],99)
    assert result["mae_mw"] == 1
    assert result["rmse_mw"] == 1
    assert result["r2"] == 0
    assert result["mae_capacity_percent"] == pytest.approx(100/99)
    with pytest.raises(ValueError):
        calculate_metrics([1,2],[1])
    with pytest.raises(ValueError):
        calculate_metrics([1,2],[np.nan,1])


def test_model_fit_train_only_and_predictions(tmp_path,data,config):
    before = data.copy(deep=True)
    splits = split_chronologically(data,"timestamp")
    models = train_models(splits["train"],config)
    assert set(models) == {"mean_baseline","linear_regression","random_forest"}
    assert models["mean_baseline"].constant_[0,0] == pytest.approx(splits["train"][config["target"]].mean())
    scaler = models["linear_regression"].named_steps["scaler"]
    np.testing.assert_allclose(scaler.mean_,splits["train"][config["features"]].mean())
    assert scaler.n_samples_seen_ == len(splits["train"])
    assert list(models["linear_regression"].feature_names_in_) == config["features"]
    scores = evaluate_models(models,splits["validation"],config)
    best = select_best_model(scores)
    out = prediction_output(models[best],best,splits["test"],config)
    assert out.shape == (16,5)
    assert out.model_name.eq(best).all()
    assert out.absolute_error_mw.ge(0).all()
    path = tmp_path/"linear.joblib"
    joblib.dump(models["linear_regression"],path)
    np.testing.assert_array_equal(joblib.load(path).predict(splits["test"][config["features"]]),models["linear_regression"].predict(splits["test"][config["features"]]))
    again = train_models(splits["train"],config)
    np.testing.assert_array_equal(models["random_forest"].predict(splits["test"][config["features"]]),again["random_forest"].predict(splits["test"][config["features"]]))
    assert_frame_equal(data,before)


def test_selection_uses_only_validation():
    # Candidate b would win on test; selection receives validation entries only.
    scores = {"a":{"validation":{"mae_mw":1.,"rmse_mw":2.},"test":{"mae_mw":50.}},
              "b":{"validation":{"mae_mw":2.,"rmse_mw":3.},"test":{"mae_mw":0.}}}
    assert select_best_model({k:v["validation"] for k,v in scores.items()}) == "a"
    assert select_best_model({"a":{"mae_mw":1.,"rmse_mw":3.},"b":{"mae_mw":1.,"rmse_mw":2.}}) == "b"
