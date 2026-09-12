"""Synthetic, fast advanced-estimation checks; no large datasets or held-out files."""

from pathlib import Path

import numpy as np
import pandas as pd
import pytest
from threadpoolctl import threadpool_limits

from ml.models.wind_baseline import load_feature_configuration
from ml.models.wind_advanced import (analyze_residuals,assign_power_bins,baseline_improvement,
    calculate_capacity_metrics,compare_experiments,create_model,evaluate_model,
    feature_experiments,get_model_candidates,prediction_frame)
from ml.training.train_wind_advanced import render_report


def test_candidates_and_configurations():
    candidates = get_model_candidates()
    assert len(candidates)==4
    assert {c["model"] for c in candidates}=={"HistGradientBoostingRegressor","GradientBoostingRegressor"}
    for candidate in candidates:
        model = create_model(candidate)
        for k,v in candidate["parameters"].items():
            assert model.get_params()[k]==v
        if "early_stopping" in model.get_params():
            assert model.early_stopping is False
        assert model.random_state==42
    with pytest.raises(ValueError,match="Unsupported"):
        create_model({"model":"XGBoost","parameters":{}})


def test_models_fit_and_evaluate_small_data():
    x = np.linspace(0,10,100)
    data = pd.DataFrame({"wind":x,"power":x*x/2})
    with threadpool_limits(limits=1):
        for candidate in (get_model_candidates()[0],get_model_candidates()[2]):
            candidate["parameters"].update({"max_iter":5} if "max_iter" in candidate["parameters"] else {"n_estimators":5})
            model = create_model(candidate)
            model.fit(data[["wind"]],data.power)
            result = evaluate_model(model,data,["wind"],"power")
            assert np.isfinite(list(result.values())).all()
            assert len(model.predict(data[["wind"]]))==100


def test_capacity_metrics_and_signed_improvement():
    m = calculate_capacity_metrics([0,2],[1,1])
    assert m["mae_mw"]==m["rmse_mw"]==1
    assert m["r2"]==0
    assert m["mae_capacity_percent"]==pytest.approx(100/99)
    change = baseline_improvement({"mae_mw":2,"rmse_mw":4,"r2":.5},{"mae_mw":3,"rmse_mw":2,"r2":.6})
    assert change["mae_mw"]["percent_improvement"]==-50
    assert change["rmse_mw"]["absolute_improvement"]==2


def record(name,mae,complexity=100):
    return {"experiment":name,"leaf_budget":complexity,"feature_count":19,
            "validation":{"mae_mw":mae,"rmse_mw":mae+1,"r2":.8}}


def test_selection_validation_only_and_near_ties():
    assert compare_experiments([record("a",2),record("b",1)])=="b"
    assert compare_experiments([record("complex",1,200),record("simple",1.005,100)])=="simple"
    assert compare_experiments([record("complex",1,200),record("simple",1.02,100)])=="complex"
    with pytest.raises(ValueError,match="Test results"):
        compare_experiments([{**record("a",2),"test":{"mae_mw":0}}])
    with pytest.raises(ValueError,match="No experiment"):
        compare_experiments([])


def test_power_bins_boundaries():
    assert list(assign_power_bins([0,9.9,24.75,49.5,74.25,99]))==["0–10%","10–25%","25–50%","50–75%","75–100%","75–100%"]
    with pytest.raises(ValueError):
        assign_power_bins([-1,100])


def test_residuals_histogram_and_group_accounting():
    times = pd.to_datetime(["2020-07-01 00:00","2020-07-01 01:00","2020-08-01 00:00"])
    predictions = prediction_frame(times,[0,20,80],[1,18,77],"selected")
    np.testing.assert_array_equal(predictions.residual_mw,[-1,2,3])
    result = analyze_residuals(predictions)
    assert result["summary"]["mean"]==pytest.approx(4/3)
    assert result["summary"]["std_population"]==pytest.approx(np.std([-1,2,3]))
    assert sum(result["residual_histogram"]["counts"])==3
    for group in ("by_power_range","by_hour","by_month"):
        assert sum(r["rows"] for r in result[group])==3
    assert len(predictions.columns)==8


def test_feature_groups_from_existing_manifest():
    config = load_feature_configuration(Path(__file__).resolve().parents[1]/"docs/wind_feature_manifest.json")
    groups = feature_experiments(config)
    assert len(groups["A"])==19 and len(groups["B"])==25
    assert set(groups["B"])-set(groups["A"])==set(config["engineered_wind"])
    assert config["target"] not in groups["B"]
    assert config["timestamp"] not in groups["A"]
