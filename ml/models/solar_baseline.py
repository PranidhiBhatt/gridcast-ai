"""Manifest-driven same-timestamp solar estimation baselines; no future forecasting."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from ml.data_processing.run_wind_analysis import sha256
from ml.data_processing.solar_preprocessor import parse_timestamps

RF_CONFIG = {"n_estimators": 100, "max_depth": 12, "min_samples_leaf": 5,
             "min_samples_split": 2, "max_features": 1.0, "bootstrap": True,
             "criterion": "squared_error", "random_state": 42, "n_jobs": 1}
TASK = "Weather-to-Solar-Power Estimation: observed weather/irradiance and calendar at T estimate power at T; not true future forecasting"


def load_contract(path: Path) -> dict[str, Any]:
    """Load exact feature order, lineage, exclusions and splits from Milestone 5B."""
    manifest = json.loads(path.read_text(encoding="utf-8"))
    contract = {"task": TASK, "features": manifest["features"], "target": manifest["target_column"],
                "timestamp": manifest["timestamp_column"], "splits": manifest["audit"]["splits"],
                "dataset": manifest["output"], "source": manifest["source"],
                "policy_version": manifest["policy_version"], "manifest": manifest}
    validate_contract(contract)
    return contract


def validate_contract(contract: dict[str, Any]) -> None:
    """Fail closed on role conflicts and unreviewed or suspicious feature provenance."""
    m, features = contract["manifest"], contract["features"]
    if not features or len(features) != len(set(features)):
        raise ValueError("Feature order must be nonempty and unique")
    if features != m["original_features"] + m["engineered_features"]:
        raise ValueError("Feature order differs from the preprocessing manifest")
    if set(features) & {contract["target"], contract["timestamp"], *m["excluded_features"]}:
        raise ValueError("Target, timestamp or excluded feature cannot be a predictor")
    for c in features:
        if re.search(r"power|target|future|lag|rolling|lead|prediction", c, re.I):
            raise ValueError(f"Potential target/future leakage: {c}")
        review = m["feature_review"].get(c, {})
        if not review.get("included"):
            raise ValueError(f"Unreviewed feature: {c}")
        if c in m["original_features"]:
            valid = review.get("source_column") == c and review.get("category") in {"irradiance", "temperature", "pressure"}
        else:
            valid = review.get("source_column") == contract["timestamp"] and review.get("category") == "calendar"
        if not valid:
            raise ValueError(f"Unreviewed feature lineage: {c}")


def validate_dataset(data: pd.DataFrame, contract: dict[str, Any]) -> None:
    """Reject drift without cleaning, clipping, reordering or removing zeros."""
    validate_contract(contract)
    expected = [contract["timestamp"], *contract["features"], contract["target"]]
    if data.empty or list(data.columns) != expected:
        raise ValueError("Prepared schema differs from manifest, including feature order")
    parse_timestamps(data[contract["timestamp"]])
    for c in contract["features"] + [contract["target"]]:
        if not pd.api.types.is_numeric_dtype(data[c]) or pd.api.types.is_bool_dtype(data[c]) or not np.isfinite(data[c]).all():
            raise ValueError(f"Missing, non-finite or nonnumeric prepared values: {c}")
    if data[contract["target"]].lt(0).any():
        raise ValueError("Negative target violates preprocessing contract; no silent repair")
    if data[contract["manifest"]["original_features"]].eq(-99).any().any():
        raise ValueError("Unexpected -99 sentinel in prepared original features")
    for c in contract["features"]:
        if np.array_equal(data[c].to_numpy(), data[contract["target"]].to_numpy()):
            raise ValueError(f"Exact target-copy leakage in {c}")


def load_dataset(path: Path, contract: dict[str, Any]) -> pd.DataFrame:
    """Verify prepared bytes and dimensions before reading exact floating-point values."""
    if not path.is_file():
        raise FileNotFoundError(f"Prepared solar dataset missing: {path}")
    if sha256(path) != contract["dataset"]["sha256"]:
        raise ValueError("Prepared dataset SHA-256 differs from Milestone 5B")
    data = pd.read_csv(path, float_precision="round_trip")
    validate_dataset(data, contract)
    if data.shape != (contract["dataset"]["rows"], contract["dataset"]["columns"]):
        raise ValueError("Dataset dimensions differ from Milestone 5B")
    data[contract["timestamp"]] = parse_timestamps(data[contract["timestamp"]])
    return data


def split_dataset(data: pd.DataFrame, contract: dict[str, Any]) -> dict[str, pd.DataFrame]:
    """Use manifest half-open boundaries; verify coverage, counts, order and disjointness."""
    validate_dataset(data, contract)
    t = parse_timestamps(data[contract["timestamp"]])
    assignment = pd.Series(0, index=data.index)
    parts = {}
    previous_end = None
    for name in ("train", "validation", "test"):
        spec = contract["splits"][name]
        start, end = pd.Timestamp(spec["boundary_start_inclusive"]), pd.Timestamp(spec["boundary_end_exclusive"])
        if start >= end or (previous_end is not None and start < previous_end):
            raise ValueError("Split boundaries overlap or are out of order")
        previous_end = end
        mask = t.ge(start) & t.lt(end)
        assignment += mask.astype(int)
        part = data.loc[mask].copy()
        if part.empty or len(part) != spec["rows"]:
            raise ValueError(f"Split row count differs from manifest: {name}")
        if str(t[mask].min()) != spec["start"] or str(t[mask].max()) != spec["end"]:
            raise ValueError(f"Split time coverage differs from manifest: {name}")
        parts[name] = part
    if not assignment.eq(1).all():
        raise ValueError("Every row must belong to exactly one chronological split")
    return parts


def ordered_features(data: pd.DataFrame, contract: dict[str, Any]) -> pd.DataFrame:
    """Use the same manifest order during fitting and every prediction."""
    return data.loc[:, contract["features"]]


def create_models() -> dict[str, Any]:
    """Three fixed baselines; scaler fits inside the linear training pipeline only."""
    return {"dummy": DummyRegressor(strategy="mean"),
            "linear_regression": Pipeline([("scaler", StandardScaler()), ("regression", LinearRegression())]),
            "random_forest": RandomForestRegressor(**RF_CONFIG)}


def model_parameters(models: dict[str, Any]) -> dict[str, Any]:
    """Serialize actual estimator parameters without volatile object representations."""
    return {name: ({step: estimator.get_params() for step, estimator in model.steps}
                  if isinstance(model, Pipeline) else model.get_params()) for name, model in models.items()}


def calculate_metrics(actual: Any, prediction: Any) -> dict[str, Any]:
    """Standard sklearn errors; undefined R² for <2 rows is represented by null."""
    y, p = np.asarray(actual, dtype=float), np.asarray(prediction, dtype=float)
    if y.ndim != 1 or y.shape != p.shape or not np.isfinite(y).all() or not np.isfinite(p).all():
        raise ValueError("Metrics need aligned finite one-dimensional observations")
    if not len(y):
        return {"rows": 0, "mae_mw": None, "rmse_mw": None, "r2": None}
    return {"rows": len(y), "mae_mw": float(mean_absolute_error(y, p)),
            "rmse_mw": float(np.sqrt(mean_squared_error(y, p))),
            "r2": float(r2_score(y, p)) if len(y) >= 2 else None}


def select_model(validation: dict[str, dict[str, Any]]) -> str:
    """Accept only validation metric records; MAE, RMSE, descending R² in that order."""
    if not validation:
        raise ValueError("No validation metrics")
    for metrics in validation.values():
        if set(metrics) != {"rows", "mae_mw", "rmse_mw", "r2"}:
            raise ValueError("Only validation metrics allowed; test records are forbidden")
        if any(metrics[k] is None for k in ("mae_mw", "rmse_mw", "r2")) or not np.isfinite([metrics[k] for k in ("mae_mw", "rmse_mw", "r2")]).all():
            raise ValueError("Selection requires finite validation scores")
    return min(validation, key=lambda name: (validation[name]["mae_mw"], validation[name]["rmse_mw"], -validation[name]["r2"]))


def power_boundaries(train_target: pd.Series) -> list[float]:
    """Freeze positive-training-target tertiles; no capacity or held-out quantiles."""
    positive = train_target[train_target > 0]
    return sorted(set(map(float, positive.quantile([1/3, 2/3]).dropna()))) if len(positive) else []


def power_groups(actual: pd.Series, boundaries: list[float]) -> pd.Series:
    """Zero is separate; positive groups use open-left, closed-right training cutpoints."""
    if actual.lt(0).any():
        raise ValueError("Power groups require nonnegative target values")
    result = pd.Series("zero", index=actual.index)
    positive = actual > 0
    if len(boundaries) == 2:
        names = ["low positive", "medium positive", "high positive"]
    else:
        names = [f"positive group {i+1}" for i in range(len(boundaries)+1)]
    codes = np.searchsorted(boundaries, actual[positive].to_numpy(), side="left")
    result.loc[positive] = [names[i] for i in codes]
    return result


def diagnostics(predictions: pd.DataFrame, boundaries: list[float]) -> dict[str, Any]:
    """Describe one frozen prediction array; never refit or influence model selection."""
    data = predictions.copy()
    data["power_group"] = power_groups(data.actual_power_mw, boundaries)
    t = pd.to_datetime(data.timestamp)
    def groups(key: Any) -> list[dict[str, Any]]:
        result = []
        for label, part in data.groupby(key, sort=True):
            metrics = calculate_metrics(part.actual_power_mw, part.predicted_power_mw)
            metrics.pop("r2")  # Constant-zero groups have no useful R² interpretation.
            result.append({"group": str(label), **metrics, "mean_residual_mw": float(part.residual_mw.mean())})
        return result
    zero_positive = np.where(data.actual_power_mw.eq(0), "zero", "positive")
    r = data.residual_mw
    return {"zero_positive": groups(zero_positive), "power_ranges": groups("power_group"),
            "recorded_hour": groups(t.dt.hour), "month": groups(t.dt.strftime("%Y-%m")),
            "residual": {"definition": "actual minus predicted; positive means underprediction",
                         "mean_mw": float(r.mean()), "median_mw": float(r.median()),
                         "std_population_mw": float(r.std(ddof=0)), "min_mw": float(r.min()), "max_mw": float(r.max()),
                         "overpredictions": int(r.lt(0).sum()), "underpredictions": int(r.gt(0).sum()),
                         "exact_predictions": int(r.eq(0).sum()),
                         "largest_absolute_errors": json.loads(data.assign(absolute_error_mw=r.abs()).nlargest(10, "absolute_error_mw").to_json(orient="records", date_format="iso"))},
            "prediction_range": {"min_mw": float(data.predicted_power_mw.min()), "max_mw": float(data.predicted_power_mw.max()),
                                 "negative_predictions": int(data.predicted_power_mw.lt(0).sum())}}


def forest_importance(model: RandomForestRegressor, features: list[str]) -> list[dict[str, Any]]:
    """Return model-specific impurity importance in descending order; not causal evidence."""
    if len(model.feature_importances_) != len(features):
        raise ValueError("Feature importance dimension mismatch")
    return sorted([{"feature": c, "importance": float(v)} for c, v in zip(features, model.feature_importances_)],
                  key=lambda row: (-row["importance"], row["feature"]))
