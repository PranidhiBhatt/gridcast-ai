"""Two fixed advanced solar estimators and validation-only baseline comparison."""

from __future__ import annotations

from typing import Any

from sklearn.ensemble import ExtraTreesRegressor, HistGradientBoostingRegressor

from ml.models.solar_baseline import select_model

MIN_RELATIVE_MAE_GAIN = 0.01


def create_models() -> dict[str, Any]:
    """Bound tree complexity; disable histogram boosting's random early-stop split."""
    return {
        "hist_gradient_boosting": HistGradientBoostingRegressor(
            max_iter=150, learning_rate=0.08, max_leaf_nodes=15,
            min_samples_leaf=30, l2_regularization=1.0,
            early_stopping=False, random_state=42),
        "extra_trees": ExtraTreesRegressor(
            n_estimators=100, max_depth=12, min_samples_leaf=5,
            max_features=1.0, bootstrap=False, random_state=42, n_jobs=1),
    }


def baseline_reference(contract: dict[str, Any], experiment: dict[str, Any],
                       metadata: dict[str, Any]) -> dict[str, Any]:
    """Validate the 5C comparison contract and return only its validation scores."""
    expected = {"dataset": contract["dataset"], "feature_order": contract["features"],
                "target": contract["target"], "timestamp": contract["timestamp"],
                "splits": contract["splits"], "dataset_version": contract["policy_version"],
                "selected_model": "random_forest"}
    for key, value in expected.items():
        if metadata.get(key) != value or experiment["metadata"].get(key) != value:
            raise ValueError(f"Baseline metadata differs from solar contract: {key}")
    validation = experiment["metrics"]["random_forest"]["validation"]
    if (validation != metadata["validation_metrics"]
            or validation != experiment["metadata"]["validation_metrics"]
            or validation["rows"] != contract["splits"]["validation"]["rows"]):
        raise ValueError("Baseline validation metrics disagree")
    select_model({"random_forest": validation})
    return dict(validation)


def select_overall(validation: dict[str, dict[str, Any]],
                   baseline: dict[str, Any]) -> dict[str, Any]:
    """Rank advanced validation MAE/RMSE/R²; retain RF unless MAE improves >=1%."""
    if set(validation) != {"hist_gradient_boosting", "extra_trees"}:
        raise ValueError("Exactly the two declared advanced candidates are required")
    best = select_model(validation)
    select_model({"random_forest": baseline})
    if any(m["rows"] != baseline["rows"] for m in validation.values()):
        raise ValueError("Validation row counts differ")
    gain = baseline["mae_mw"] - validation[best]["mae_mw"]
    relative = gain / baseline["mae_mw"] if baseline["mae_mw"] > 0 else 0.0
    selected = best if gain > 0 and relative >= MIN_RELATIVE_MAE_GAIN else "random_forest"
    return {"best_advanced": best, "selected_model": selected,
            "advanced_mae_gain_mw": gain, "advanced_relative_mae_gain": relative,
            "minimum_relative_mae_gain": MIN_RELATIVE_MAE_GAIN,
            "rule": "Advanced: validation MAE, RMSE, descending R2; exact ties retain declared order. Replace RF only with >=1% validation MAE reduction. No test input.",
            "threshold_note": "Predeclared experiment threshold, not statistical significance or an operational accuracy requirement."}
