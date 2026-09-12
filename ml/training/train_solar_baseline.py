"""Fixed chronological solar baselines: python -m ml.training.train_solar_baseline."""

from __future__ import annotations

import json
import platform
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
import sklearn
from threadpoolctl import threadpool_limits

from ml.data_processing.run_wind_analysis import sha256, table
from ml.data_processing.run_solar_preprocessing import require_ignored, verify_hashes
from ml.models.solar_baseline import (
    TASK, calculate_metrics, create_models, diagnostics, forest_importance,
    load_contract, load_dataset, model_parameters, ordered_features,
    power_boundaries, select_model, split_dataset,
)

ROOT = Path(__file__).resolve().parents[2]
MODEL_FILES = {"dummy": "solar_dummy_baseline.joblib", "linear_regression": "solar_linear_regression.joblib",
               "random_forest": "solar_random_forest.joblib"}
LIMITATIONS = ["Single site, two years, observed contemporaneous inputs; no future forecast input or horizon",
               "Unresolved observation timezone, total irradiance plane, AC/DC and interval-averaging semantics",
               "Filename nominal capacity is not verified; no capacity normalization or clipping",
               "Humidity remains excluded; complete-case omission can bias coverage; gaps remain",
               "Native forest importance is model-specific and affected by correlated predictors, not causal evidence",
               "Diagnostic test analysis must not drive additional tuning against this same test period"]


def dump(path: Path, payload: Any) -> None:
    """Write stable finite JSON without wall-clock timestamps or estimator repr strings."""
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def build_metadata(contract: dict[str, Any], selected: str, parameters: dict[str, Any],
                   scores: dict[str, Any]) -> dict[str, Any]:
    """Build deterministic metadata from frozen results and the manifest contract."""
    return {"task": TASK, "dataset": contract["dataset"], "dataset_source": contract["source"],
            "dataset_version": contract["policy_version"], "target": contract["target"],
            "timestamp": contract["timestamp"], "feature_order": contract["features"],
            "splits": contract["splits"], "selected_model": selected, "parameters": parameters[selected],
            "selection": "Validation MAE ascending, validation RMSE ascending, validation R2 descending. Exact ties retain declared model order; no test input.",
            "train_metrics": scores[selected]["train"], "validation_metrics": scores[selected]["validation"],
            "test_metrics": scores[selected]["test"], "limitations": LIMITATIONS}


def render_report(experiment: dict[str, Any], importance: dict[str, Any]) -> str:
    """Render all requested report sections from actual frozen results."""
    e = experiment
    meta, scores, diags = e["metadata"], e["metrics"], e["selected_diagnostics"]
    def block(value: Any) -> str:
        return "```json\n" + json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n```\n"
    def metrics_table(split: str) -> str:
        return table(["Model", "Rows", "MAE MW", "RMSE MW", "R²"],
                     [[name, m[split]["rows"], *[round(m[split][k], 7) for k in ["mae_mw", "rmse_mw", "r2"]]] for name, m in scores.items()])
    def extrema(rows: list[dict[str, Any]]) -> dict[str, Any]:
        return {"lowest_mae": min(rows, key=lambda row: row["mae_mw"]), "highest_mae": max(rows, key=lambda row: row["mae_mw"])}
    selected = meta["selected_model"]
    validation_gain = scores["dummy"]["validation"]["mae_mw"] - scores[selected]["validation"]["mae_mw"]
    next_step = ("Milestone 5D — Advanced Solar Model Evaluation is justified as a bounded experiment: the selected baseline improves validation MAE over the constant benchmark, while train/validation gaps and the reported residuals leave questions about nonlinear generalisation. Improvement from advanced models is not guaranteed. Predeclare candidates and validation criteria; do not use the test diagnostics to tune. A fresh untouched period is preferable for confirming any adaptation."
                 if selected != "dummy" and validation_gain > 0 else
                 "The baseline results do not justify advanced models yet. Review input semantics and the lack of improvement over the constant benchmark before adding complexity. No operational sufficiency threshold was provided.")
    sections = ["# Solar Baseline Model Evaluation\n", "## 1. Objective\n", TASK + ".\n",
        "## 2. Dataset\n", block(meta["dataset"]),
        f"Unchanged Milestone 5B data, policy `{meta['dataset_version']}`. {e['omitted_rows']} rows were omitted during preprocessing; no new row removal, cleaning, shuffle or imputation. Raw/prepared bytes and preprocessing source hashes are checked before and after training.\n",
        "## 3. Target\n", f"`{meta['target']}`. Header-labelled power in MW; AC/DC and averaging convention unresolved. Zeros and high values retained. Predictions remain unclipped, including negative linear outputs. Nominal capacity is not used as a verified normalization denominator.\n",
        "## 4. Features\n", block(meta["feature_order"]), block(e["feature_review"]),
        "Feature order is loaded from the manifest and used identically for fitting and prediction. Target/raw timestamp/humidity are excluded. No target-derived or future-observation features. Hash and lineage checks support reproducibility but cannot certify undocumented upstream sensor provenance.\n",
        "## 5. Chronological Split\n", block(meta["splits"]),
        "Manifest half-open boundaries, counts and actual date ranges are verified. Each unique timestamp is assigned once; no overlap or train+validation refit. Equal solar measurement values at different times are not automatically duplicate observations.\n",
        "## 6. Models Evaluated\n",
        "DummyRegressor predicts the training-only mean. LinearRegression uses a training-fitted StandardScaler pipeline as an interpretable additive baseline; it cannot represent all nonlinear behavior. RandomForestRegressor uses 100 trees, depth 12 and minimum leaf size 5 to bound baseline cost and leaf variance. Settings were fixed before fitting, not searched.\n",
        "## 7. Model Parameters\n", block(e["model_parameters"]),
        "Forest random_state=42; one worker and one native thread. No GridSearchCV, RandomizedSearchCV, random CV or advanced solar model. Saved linear artifact includes its scaler.\n",
        "## 8. Evaluation Metrics\n",
        "MAE is sklearn mean absolute error (MW); RMSE is sqrt(mean squared error) (MW); R² uses sklearn r2_score against the evaluated split's mean. Stored scores retain full precision. Subsets report counts/MAE/RMSE; zero-only R² is intentionally omitted as uninformative. Empty subsets have no metrics; overall errors remain primary.\n",
        "Training results:\n", metrics_table("train"),
        "## 9. Validation Results\n", metrics_table("validation"),
        "Train-to-validation MAE gaps (descriptive; could reflect overfitting and/or temporal shift):\n",
        block({name: m["validation"]["mae_mw"] - m["train"]["mae_mw"] for name, m in scores.items()}),
        "## 10. Model Selection\n", f"**Selected using validation data only: {selected}.**\n", meta["selection"] + "\n",
        "Overall validation MAE is primary; zero/positive subset diagnostics and test scores do not select the model. No additional close-score heuristics.\n",
        "## 11. Held-Out Test Evaluation\n", metrics_table("test"),
        "Selection was frozen and logged before any test prediction. All three fixed baselines are scored on test afterward for transparent comparison; none is reselected or tuned. Selected predictions are reused for all diagnostics.\n",
        "## 12. Zero vs Positive Generation Analysis\n", block(e["zero_positive_all_models"]),
        "No zero target rows were discarded to improve performance. Selected-model residual mean is actual minus predicted.\n",
        "## 13. Power-Range Error Analysis\n", block(e["power_bins"]),
        "Zero is its own bin. Positive-training-target tertiles define low/medium/high; positive bins are open-left and closed-right with an unbounded upper bin. Held-out target distribution and filename capacity did not set boundaries.\n",
        block({split: diags[split]["power_ranges"] for split in diags}),
        "## 14. Time-Based Error Analysis\n",
        "Recorded timestamp hour is not verified local solar time. Monthly groups use year-month; no astronomical interpretation or seasonal attribution.\n",
        block({split: {key: diags[split][key] for key in ["recorded_hour", "month"]} for split in diags}),
        block({split: {key: extrema(diags[split][key]) for key in ["recorded_hour", "month"]} for split in diags}),
        "## 15. Feature Importance\n", table(["Feature", "Random forest importance"], [[r["feature"], r["importance"]] for r in importance["random_forest"]]),
        block(importance["linear_regression"]),
        "Forest impurity importance indicates model-specific relative usage, not causation or physical proof. Correlated irradiance/calendar predictors may share or mask importance. Linear coefficients use training-standardized inputs (MW per training standard deviation), not raw-unit or causal importance; collinearity remains relevant.\n",
        "## 16. Residual Analysis\n", block({split: {"residual": diags[split]["residual"], "prediction_range": diags[split]["prediction_range"]} for split in diags}),
        "Residual standard deviation uses population ddof=0. Positive mean suggests average underprediction; negative mean suggests overprediction. Largest errors and group means are descriptive and not proof of operational causes.\n",
        "## 17. Limitations\n", block(LIMITATIONS),
        "No deployment accuracy threshold or confidence interval is established; one site and two years cannot demonstrate wider generalisation.\n",
        "## 18. Future Forecasting Limitation\n",
        "This model performs weather-to-solar-power estimation using observed contemporaneous inputs. It is not yet a true future solar forecasting model. Future forecasting requires weather and irradiance forecasts or forecastable substitutes, forecast origin/horizon and verified prediction-time availability.\n",
        "## 19. Recommended Next Step\n", next_step + "\n",
        "Reproduce from the repository root: `python -m ml.training.train_solar_baseline`. Models, metrics, predictions, diagnostics and best-model metadata are Git-ignored under ml/artifacts. No Milestone 5D/6, model API, aggregation or control is implemented.\n"]
    return "\n".join(sections)


def run_training(root: Path = ROOT) -> dict[str, Any]:
    """Fit training only, freeze validation selection, then evaluate held-out test."""
    root = root.resolve()
    contract = load_contract(root / "docs/solar_feature_manifest.json")
    sources = json.loads((root / "docs/solar_dataset_sources.json").read_text(encoding="utf-8"))["source_hashes"]
    verify_hashes(root, sources)
    protected = dict(sources)
    for p in [*list((root / "ml/data_processing").glob("*.py")),
              *list((root / "ml/models").glob("wind*.py")), *list((root / "ml/training").glob("*wind*.py")),
              *list((root / "ml/artifacts").glob("*")),
              root / "docs/solar_feature_manifest.json", root / "docs/solar_preprocessing_report.md",
              root / contract["dataset"]["path"], root / contract["manifest"]["omission_log"]["path"]]:
        if p.is_file() and (p.parent != root / "ml/artifacts" or not p.name.startswith("solar_")):
            protected[p.relative_to(root).as_posix()] = sha256(p)
    data = load_dataset(root / contract["dataset"]["path"], contract)
    parts = split_dataset(data, contract)
    artifact_dir = root / "ml/artifacts"
    extra_files = ["solar_baseline_metrics.json", "solar_feature_importance.json", "solar_baseline_predictions.csv", "solar_best_baseline_metadata.json"]
    for filename in [*MODEL_FILES.values(), *extra_files]:
        path = artifact_dir / filename
        if path.resolve() != path or path.is_symlink():
            raise ValueError(f"Artifact path redirects: {path}")
        require_ignored(root, path.relative_to(root).as_posix())
    models = create_models()
    params = model_parameters(models)
    predictions: dict[str, dict[str, np.ndarray]] = {name: {} for name in models}
    metrics: dict[str, dict[str, Any]] = {name: {} for name in models}
    boundaries = power_boundaries(parts["train"][contract["target"]])
    with threadpool_limits(limits=1):
        for name, model in models.items():
            print(f"Fitting solar {name} on {len(parts['train']):,} training rows", flush=True)
            model.fit(ordered_features(parts["train"], contract), parts["train"][contract["target"]])
            for split in ("train", "validation"):
                prediction = model.predict(ordered_features(parts[split], contract))
                predictions[name][split] = prediction
                metrics[name][split] = calculate_metrics(parts[split][contract["target"]], prediction)
        selected = select_model({name: result["validation"] for name, result in metrics.items()})
        print(f"Validation selection frozen: {selected}. Test evaluation begins now.", flush=True)
        for name, model in models.items():
            prediction = model.predict(ordered_features(parts["test"], contract))
            predictions[name]["test"] = prediction
            metrics[name]["test"] = calculate_metrics(parts["test"][contract["target"]], prediction)
    prediction_tables = []
    zero_positive = {}
    selected_diagnostics = {}
    for name in models:
        zero_positive[name] = {}
        for split, part in parts.items():
            actual = part[contract["target"]].to_numpy()
            predicted = predictions[name][split]
            if split in ("validation", "test"):
                zero_positive[name][split] = {}
                for label, mask in {"zero": actual == 0, "positive": actual > 0}.items():
                    subset = calculate_metrics(actual[mask], predicted[mask])
                    subset.pop("r2")
                    zero_positive[name][split][label] = subset
            if name == selected:
                frame = pd.DataFrame({"timestamp": part[contract["timestamp"]].to_numpy(), "split": split,
                                      "actual_power_mw": actual, "predicted_power_mw": predicted,
                                      "residual_mw": actual - predicted, "model_name": selected})
                prediction_tables.append(frame)
                if split in ("validation", "test"):
                    selected_diagnostics[split] = diagnostics(frame, boundaries)
    linear = models["linear_regression"].named_steps["regression"]
    importance = {"random_forest": forest_importance(models["random_forest"], contract["features"]),
                  "linear_regression": {"scale": "MW per training-standardized input; not causal importance",
                                        "coefficients": [{"feature": c, "coefficient": float(v)} for c, v in zip(contract["features"], linear.coef_)],
                                        "intercept_mw": float(linear.intercept_)}}
    metadata = build_metadata(contract, selected, params, metrics)
    experiment = {"metadata": metadata, "metrics": metrics, "model_parameters": params,
                  "feature_review": contract["manifest"]["feature_review"],
                  "omitted_rows": contract["manifest"]["audit"]["omitted_rows"],
                  "power_bins": {"source": "positive TRAINING targets only", "quantiles": [1/3, 2/3], "cutpoints_mw": boundaries},
                  "zero_positive_all_models": zero_positive, "selected_diagnostics": selected_diagnostics,
                  "protected_input_hashes": protected,
                  "code_hashes": {p: sha256(root / p) for p in ["ml/models/solar_baseline.py", "ml/training/train_solar_baseline.py"]},
                  "runtime": {"python": platform.python_version(), "numpy": np.__version__, "pandas": pd.__version__,
                              "scikit_learn": sklearn.__version__, "joblib": joblib.__version__, "native_threads": 1}}
    verify_hashes(root, protected)
    artifact_dir.mkdir(parents=True, exist_ok=True)
    for name, model in models.items():
        joblib.dump(model, artifact_dir / MODEL_FILES[name], compress=3)
    pd.concat(prediction_tables, ignore_index=True).to_csv(artifact_dir / "solar_baseline_predictions.csv", index=False, float_format="%.17g")
    dump(artifact_dir / "solar_baseline_metrics.json", experiment)
    dump(artifact_dir / "solar_feature_importance.json", importance)
    dump(artifact_dir / "solar_best_baseline_metadata.json", {**metadata, "protected_input_hashes": protected, "code_hashes": experiment["code_hashes"], "runtime": experiment["runtime"]})
    (root / "docs/solar_baseline_model_report.md").write_text(render_report(experiment, importance), encoding="utf-8")
    verify_hashes(root, protected)
    print(json.dumps({"selected": selected, "metrics": metrics, "power_bins": boundaries}, indent=2), flush=True)
    print("Saved solar models, metrics, selected predictions, importance, metadata and report; protected inputs unchanged.", flush=True)
    return experiment


if __name__ == "__main__":
    try:
        run_training()
    except (OSError, ValueError, KeyError) as exc:
        raise SystemExit(f"Solar baseline training failed: {exc}") from exc
