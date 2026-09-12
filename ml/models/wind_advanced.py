"""Small validation-selected boosting experiments for same-timestamp estimation."""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor, HistGradientBoostingRegressor

from ml.models.wind_baseline import SEED, calculate_metrics, review_feature_configuration

NEAR_TIE_MW = 0.01
POWER_LABELS = ["0–10%", "10–25%", "25–50%", "50–75%", "75–100%"]


def get_model_candidates() -> list[dict[str, Any]]:
    """Four predeclared configurations; no auto/random validation split or search."""
    return [
        {"name":"hist_150", "model":"HistGradientBoostingRegressor", "parameters":{
            "max_iter":150,"learning_rate":0.08,"max_leaf_nodes":15,"min_samples_leaf":30,
            "l2_regularization":1.0,"early_stopping":False,"random_state":SEED}},
        {"name":"hist_250", "model":"HistGradientBoostingRegressor", "parameters":{
            "max_iter":250,"learning_rate":0.05,"max_leaf_nodes":15,"min_samples_leaf":50,
            "l2_regularization":5.0,"early_stopping":False,"random_state":SEED}},
        {"name":"gradient_120", "model":"GradientBoostingRegressor", "parameters":{
            "n_estimators":120,"learning_rate":0.05,"max_depth":3,"min_samples_leaf":20,
            "subsample":1.0,"loss":"squared_error","random_state":SEED}},
        {"name":"gradient_180", "model":"GradientBoostingRegressor", "parameters":{
            "n_estimators":180,"learning_rate":0.05,"max_depth":3,"min_samples_leaf":40,
            "subsample":1.0,"loss":"squared_error","random_state":SEED}},
    ]


def create_hist_gradient_boosting_model(**parameters: Any) -> HistGradientBoostingRegressor:
    """Disable random internal early stopping; external chronological validation selects."""
    return HistGradientBoostingRegressor(**{"random_state":SEED,"early_stopping":False,**parameters})


def create_gradient_boosting_model(**parameters: Any) -> GradientBoostingRegressor:
    """Create deterministic squared-error boosting without random subsampling."""
    return GradientBoostingRegressor(**{"random_state":SEED,"subsample":1.0,**parameters})


def create_model(candidate: dict[str, Any]) -> Any:
    """Dispatch only the two reviewed model families."""
    factories = {"HistGradientBoostingRegressor":create_hist_gradient_boosting_model,
                 "GradientBoostingRegressor":create_gradient_boosting_model}
    if candidate["model"] not in factories:
        raise ValueError(f"Unsupported advanced model: {candidate['model']}")
    return factories[candidate["model"]](**candidate["parameters"])


def feature_experiments(config: dict[str, Any]) -> dict[str, list[str]]:
    """A keeps measured weather/calendar; B additionally keeps engineered directions."""
    review_feature_configuration(config)
    groups = {"A":config["weather"]+config["time"],"B":list(config["features"])}
    if set(groups["B"])-set(groups["A"]) != set(config["engineered_wind"]):
        raise ValueError("Feature experiments do not match manifest direction encodings")
    return groups


def calculate_capacity_metrics(actual: Any, predicted: Any, capacity: float = 99.0) -> dict[str,float]:
    """Reuse the baseline metric definitions exactly."""
    return calculate_metrics(actual,predicted,capacity)


def evaluate_model(model: Any, data: pd.DataFrame, features: list[str], target: str,
                   capacity: float = 99.0) -> dict[str,float]:
    """Score a supplied training/validation partition, without fitting or clipping."""
    return calculate_capacity_metrics(data[target],model.predict(data[features]),capacity)


def compare_experiments(records: list[dict[str,Any]]) -> str:
    """Validation-only selection; test-bearing records are rejected.

    Within 0.01 MW of minimum validation MAE prefer a smaller tree-leaf budget,
    then fewer features, validation RMSE, higher R², MAE and stable experiment id.
    Leaf budget is a structural proxy, not measured inference latency.
    """
    if not records:
        raise ValueError("No experiment results")
    for r in records:
        if any("test" in k.lower() for k in r):
            raise ValueError("Test results must not enter model selection")
        if not np.isfinite([r["validation"][k] for k in ("mae_mw","rmse_mw","r2")]).all():
            raise ValueError("Non-finite validation metrics")
    best = min(r["validation"]["mae_mw"] for r in records)
    near = [r for r in records if r["validation"]["mae_mw"] <= best+NEAR_TIE_MW]
    return min(near,key=lambda r:(r["leaf_budget"],r["feature_count"],r["validation"]["rmse_mw"],
                                -r["validation"]["r2"],r["validation"]["mae_mw"],r["experiment"]))["experiment"]


def assign_power_bins(actual: Any, capacity: float = 99.0) -> pd.Categorical:
    """Bin actual power: [0,10), [10,25), [25,50), [50,75), [75,100] percent."""
    percentage = np.asarray(actual,dtype=float)*100/capacity
    if capacity <= 0 or not np.isfinite(percentage).all() or ((percentage < 0)|(percentage > 100)).any():
        raise ValueError("Power-bin inputs must be finite and within nominal capacity")
    indices = np.searchsorted([10,25,50,75],percentage,side="right")
    return pd.Categorical.from_codes(indices,categories=POWER_LABELS,ordered=True)


def prediction_frame(times: Any, actual: Any, predicted: Any, model_name: str,
                     capacity: float = 99.0) -> pd.DataFrame:
    """Create the single prediction table reused for all held-out diagnostics."""
    actual, predicted = np.asarray(actual,dtype=float), np.asarray(predicted,dtype=float)
    calculate_capacity_metrics(actual,predicted,capacity)
    residual = actual-predicted
    return pd.DataFrame({"timestamp":pd.to_datetime(times).to_numpy(),"actual_power_mw":actual,
        "predicted_power_mw":predicted,"residual_mw":residual,"absolute_error_mw":np.abs(residual),
        "capacity_percentage":100*actual/capacity,"power_bin":assign_power_bins(actual,capacity),"model_name":model_name})


def analyze_residuals(predictions: pd.DataFrame) -> dict[str,Any]:
    """Descriptive post-selection errors; never return new fitting/selection settings."""
    r = predictions["residual_mw"]
    counts, edges = np.histogram(r,bins=30)
    def groups(key: Any) -> list[dict[str,Any]]:
        rows = []
        for label, part in predictions.groupby(key,observed=True,sort=True):
            rows.append({"group":str(label),"rows":len(part),"mae_mw":float(part.absolute_error_mw.mean()),
                         "rmse_mw":float(np.sqrt(np.mean(part.residual_mw**2))),
                         "mean_residual_mw":float(part.residual_mw.mean())})
        return rows
    times = pd.to_datetime(predictions["timestamp"])
    return {"residual_definition":"actual minus predicted; positive means underestimation",
        "summary":{"mean":float(r.mean()),"median":float(r.median()),"std_population":float(r.std(ddof=0)),
                   "min":float(r.min()),"max":float(r.max())},
        "absolute_error_quantiles":{str(q):float(v) for q,v in predictions.absolute_error_mw.quantile([0,.25,.5,.75,.9,.95,.99,1]).items()},
        "residual_histogram":{"counts":counts.tolist(),"edges_mw":edges.tolist(),"bins":30},
        "by_power_range":groups("power_bin"),"by_hour":groups(times.dt.hour),"by_month":groups(times.dt.strftime("%Y-%m")),
        "season_decision":"No seasons inferred: site hemisphere/location metadata absent; test covers only July–December 2020."}


def baseline_improvement(baseline: dict[str,float], advanced: dict[str,float]) -> dict[str,Any]:
    """Signed changes; negative improvement transparently indicates deterioration."""
    return {k:{"baseline":baseline[k],"advanced":advanced[k],"absolute_improvement":baseline[k]-advanced[k],
               "percent_improvement":100*(baseline[k]-advanced[k])/baseline[k] if baseline[k] else None}
            for k in ("mae_mw","rmse_mw")} | {"r2":{"baseline":baseline["r2"],"advanced":advanced["r2"],
                                                       "change":advanced["r2"]-baseline["r2"]}}
