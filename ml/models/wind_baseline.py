"""Weather-to-wind-power estimation at timestamp T, not future forecasting."""

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

SEED = 42
RF_CONFIG = {"n_estimators": 80, "max_depth": 12, "min_samples_leaf": 5,
             "min_samples_split": 2, "max_features": 1.0, "bootstrap": True,
             "criterion": "squared_error", "random_state": SEED, "n_jobs": 1}


def load_feature_configuration(path: str | Path) -> dict[str, Any]:
    """Use the Milestone 2 manifest as the feature-list source of truth."""
    manifest = json.loads(Path(path).read_text(encoding="utf-8"))
    weather = manifest["primary_features"] + manifest["secondary_features"]
    engineered = manifest["engineered_features"]
    calendar = [c for c in engineered if c in manifest["forecast_safe_predictors"]]
    wind = [c for c in engineered if c not in calendar]
    config = {"weather": weather, "time": calendar, "engineered_wind": wind,
              "features": weather + engineered, "target": manifest["target_column"],
              "timestamp": manifest["timestamp_column"], "capacity_mw": manifest["nominal_capacity_MW"],
              "excluded": manifest["excluded_columns"], "manifest": manifest}
    review_feature_configuration(config)
    return config


def review_feature_configuration(config: dict[str, Any]) -> dict[str, Any]:
    """Reject role conflicts and unreviewed feature lineage; document availability."""
    features = config["features"]
    if not features or len(features) != len(set(features)):
        raise ValueError("Predictor list must be nonempty and unique")
    forbidden = {config["target"], config["timestamp"], *config["excluded"]}
    if forbidden.intersection(features):
        raise ValueError("Target, timestamp or excluded column found among predictors")
    manifest = config["manifest"]
    result = {}
    for c in features:
        if re.search(r"power|target|future|lead|prediction", c, flags=re.I):
            raise ValueError(f"Potential target/future leakage feature: {c}")
        prior = manifest["leakage_decisions"].get(c, {}).get("classification")
        original_role = manifest["original_column_classifications"].get(c)
        if c in config["weather"]:
            valid = original_role in {"PRIMARY FEATURE", "SECONDARY FEATURE"} and prior == "POTENTIAL LEAKAGE"
            reason = "Measured weather at T supports estimating power at T; distinct height measurements remain separate."
        elif c in config["time"]:
            valid = c in manifest["engineered_features"] and prior == "SAFE FOR FORECASTING"
            reason = "Deterministic calendar or cyclic season/time-of-day information; no epoch or raw timestamp predictor."
        else:
            valid = c in manifest["engineered_features"] and prior == "POTENTIAL LEAKAGE" and c.startswith("wind_direction_")
            reason = "Circular representation of verified direction at T; deterministic and target-independent."
        if not valid:
            raise ValueError(f"Unreviewed feature provenance: {c}")
        result[c] = {"estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION", "inclusion_reason": reason,
                     "future_use": "SAFE calendar availability" if c in config["time"] else "CONDITIONAL FOR FUTURE FORECASTING",
                     "future_condition": "Maintain known calendar/timezone convention" if c in config["time"] else
                     "Replace observed weather at the future target time with as-issued forecast weather, defining origin, horizon and availability."}
    result[config["timestamp"]] = {"estimation": "EXCLUDE", "reason": "Index/split key only; avoids raw timestamp memorization"}
    result[config["target"]] = {"estimation": "EXCLUDE", "reason": "Response only; never a predictor"}
    result.update({c: {"estimation": "EXCLUDE", "reason": reason} for c, reason in config["excluded"].items()})
    return result


def verify_chronological_order(data: pd.DataFrame, timestamp: str) -> None:
    """Reject missing, malformed, duplicated, timezone-shifted or unordered time keys."""
    if timestamp not in data:
        raise ValueError(f"Missing timestamp column: {timestamp}")
    time = pd.to_datetime(data[timestamp], errors="coerce", format="mixed")
    if time.isna().any() or not pd.api.types.is_datetime64_any_dtype(time) or time.dt.tz is not None:
        raise ValueError("Invalid timestamp or unexpected timezone")
    if time.duplicated().any() or not time.is_monotonic_increasing:
        raise ValueError("Timestamps must be unique and chronologically ordered")


def validate_prepared_dataset(data: pd.DataFrame, config: dict[str, Any]) -> dict[str, Any]:
    """Validate exact manifest schema and finite values without cleaning or reordering."""
    review_feature_configuration(config)
    expected = [config["timestamp"], *config["features"], config["target"]]
    if data.empty or list(data.columns) != expected:
        raise ValueError("Prepared schema differs from the manifest; missing, extra or reordered columns")
    verify_chronological_order(data, config["timestamp"])
    for c in config["features"] + [config["target"]]:
        if not pd.api.types.is_numeric_dtype(data[c]) or not np.isfinite(data[c]).all():
            raise ValueError(f"Non-numeric, missing or non-finite values in {c}")
        if c in config["features"] and np.array_equal(data[c].to_numpy(), data[config["target"]].to_numpy()):
            raise ValueError(f"Exact target-copy leakage in {c}")
    y = data[config["target"]]
    if ((y < 0) | (y > config["capacity_mw"])).any():
        raise ValueError("Unexpected target range; do not silently clip or clean")
    if data[config["features"]].eq(-99).any().any():
        raise ValueError("Unexpected unresolved sentinel in prepared features")
    time = pd.to_datetime(data[config["timestamp"]], format="mixed")
    return {"rows": len(data), "columns": len(data.columns), "features": len(config["features"]),
            "missing_values": int(data.isna().sum().sum()), "start": str(time.min()), "end": str(time.max()),
            "duplicate_rows": int(data.duplicated().sum()), "duplicate_timestamps": int(time.duplicated().sum()),
            "interval_counts": {str(k): int(v) for k,v in time.diff().dropna().value_counts().items()},
            "cadence_note": "Nominal 15 minutes with documented gaps after complete-case selection; no resampling."}


def load_prepared_dataset(path: str | Path, config: dict[str, Any]) -> pd.DataFrame:
    """Read and validate the unchanged prepared CSV."""
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"Prepared dataset missing: {path}")
    data = pd.read_csv(path)
    validate_prepared_dataset(data, config)
    data[config["timestamp"]] = pd.to_datetime(data[config["timestamp"]], format="mixed")
    return data


def split_chronologically(data: pd.DataFrame, timestamp: str) -> dict[str, pd.DataFrame]:
    """Use the established 2019 / first-half-2020 / second-half-2020 split."""
    verify_chronological_order(data, timestamp)
    t = pd.to_datetime(data[timestamp], format="mixed")
    if not t.between(pd.Timestamp("2019-01-01"), pd.Timestamp("2020-12-31 23:59:59")).all():
        raise ValueError("Dates outside the documented 2019–2020 split window")
    splits = {"train": data.loc[t < "2020-01-01"].copy(),
              "validation": data.loc[(t >= "2020-01-01") & (t < "2020-07-01")].copy(),
              "test": data.loc[t >= "2020-07-01"].copy()}
    if any(part.empty for part in splits.values()):
        raise ValueError("Every chronological split must contain observations")
    return splits


def review_split_overlap(splits: dict[str, pd.DataFrame], config: dict[str, Any]) -> dict[str, Any]:
    """Check time overlap and exact repeated predictor/response records across splits."""
    from itertools import combinations

    result = {}
    for a,b in combinations(splits, 2):
        time_overlap = len(set(splits[a][config["timestamp"]]) & set(splits[b][config["timestamp"]]))
        columns = config["features"] + [config["target"]]
        left = set(pd.util.hash_pandas_object(splits[a][columns], index=False))
        right = set(pd.util.hash_pandas_object(splits[b][columns], index=False))
        result[f"{a}/{b}"] = {"timestamp_overlap": time_overlap,
                              "identical_predictor_target_signatures": len(left & right)}
        if time_overlap or left & right:
            raise ValueError(f"Cross-split duplicate observation detected: {a}/{b}; review before training")
    return result


def calculate_metrics(actual: Any, predicted: Any, capacity_mw: float = 99.0) -> dict[str, float]:
    """MAE/RMSE in MW and percent of nominal capacity; R² is dimensionless."""
    y, prediction = np.asarray(actual, dtype=float), np.asarray(predicted, dtype=float)
    if y.ndim != 1 or y.shape != prediction.shape or len(y) < 2 or capacity_mw <= 0:
        raise ValueError("Metrics need aligned one-dimensional arrays with >=2 rows and positive capacity")
    if not np.isfinite(y).all() or not np.isfinite(prediction).all():
        raise ValueError("Metrics require finite values")
    mae = float(mean_absolute_error(y, prediction))
    rmse = float(np.sqrt(mean_squared_error(y, prediction)))
    return {"mae_mw": mae, "rmse_mw": rmse, "r2": float(r2_score(y,prediction)),
            "mae_capacity_percent": 100*mae/capacity_mw, "rmse_capacity_percent": 100*rmse/capacity_mw}


def create_models() -> dict[str, Any]:
    """Fixed configurations, no search. Scaler stays inside the train-fitted pipeline."""
    return {"mean_baseline": DummyRegressor(strategy="mean"),
            "linear_regression": Pipeline([("scaler", StandardScaler().set_output(transform="pandas")),
                                            ("regression", LinearRegression())]),
            "random_forest": RandomForestRegressor(**RF_CONFIG)}


def train_models(train: pd.DataFrame, config: dict[str, Any]) -> dict[str, Any]:
    """Accept only the training partition; never accept validation/test to fit."""
    models = create_models()
    X, y = train[config["features"]], train[config["target"]]
    for model in models.values():
        model.fit(X,y)
    return models


def evaluate_models(models: dict[str, Any], data: pd.DataFrame, config: dict[str, Any]) -> dict[str, Any]:
    """Score all fixed candidates without changing any learned state."""
    return {name: calculate_metrics(data[config["target"]], model.predict(data[config["features"]]), config["capacity_mw"])
            for name,model in models.items()}


def select_best_model(validation_metrics: dict[str, Any]) -> str:
    """Select only from validation MAE, then validation RMSE, then name for ties."""
    if not validation_metrics:
        raise ValueError("No validation metrics")
    if any(not np.isfinite([m["mae_mw"],m["rmse_mw"]]).all() for m in validation_metrics.values()):
        raise ValueError("Non-finite validation selection metrics")
    return min(validation_metrics, key=lambda name: (validation_metrics[name]["mae_mw"], validation_metrics[name]["rmse_mw"],name))


def prediction_output(model: Any, model_name: str, data: pd.DataFrame, config: dict[str, Any]) -> pd.DataFrame:
    """Save only the selected model's predictions to avoid duplicating evaluation data."""
    prediction = model.predict(data[config["features"]])
    actual = data[config["target"]].to_numpy()
    return pd.DataFrame({"timestamp": data[config["timestamp"]].to_numpy(), "actual_power_mw": actual,
                         "predicted_power_mw": prediction, "absolute_error_mw": np.abs(actual-prediction),
                         "model_name": model_name})
