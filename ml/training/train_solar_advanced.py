"""Run the bounded 5D experiment once; verify and reuse saved results on reruns."""

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

from ml.data_processing.run_solar_preprocessing import require_ignored, verify_hashes
from ml.data_processing.run_wind_analysis import sha256, table
from ml.models.solar_advanced import baseline_reference, create_models, select_overall
from ml.models.solar_baseline import (
    TASK, calculate_metrics, diagnostics, forest_importance, load_contract,
    load_dataset, model_parameters, ordered_features, power_boundaries, split_dataset,
)
from ml.training.train_solar_baseline import LIMITATIONS, dump

ROOT = Path(__file__).resolve().parents[2]
MODEL_FILES = {"hist_gradient_boosting": "solar_hist_gradient_boosting.joblib",
               "extra_trees": "solar_extra_trees.joblib"}
METRICS = "solar_advanced_metrics.json"
METADATA = "solar_best_model_metadata.json"
RECEIPT = "solar_advanced_model_metadata.json"
REPORT = "docs/solar_advanced_model_report.md"


def focused_diagnostics(part: pd.DataFrame, predicted: Any,
                        contract: dict[str, Any], boundaries: list[float]) -> dict[str, Any]:
    """Reuse 5C groups; keep only aggregate diagnostics, without prediction files."""
    actual = part[contract["target"]].to_numpy()
    frame = pd.DataFrame({"timestamp": part[contract["timestamp"]].to_numpy(),
                          "actual_power_mw": actual, "predicted_power_mw": predicted,
                          "residual_mw": actual - predicted})
    result = diagnostics(frame, boundaries)
    residual = result["residual"]
    result["residual"] = {k: residual[k] for k in
                          ("definition", "mean_mw", "median_mw", "std_population_mw")}
    result["residual"]["largest_absolute_error_mw"] = float(frame.residual_mw.abs().max())
    return result


def render_report(result: dict[str, Any]) -> str:
    """Produce a concise report directly from the frozen experiment."""
    r = result
    def block(value: Any) -> str:
        return "```json\n" + json.dumps(value, ensure_ascii=False, indent=2) + "\n```\n"
    def scores(values: dict[str, Any]) -> str:
        return table(["Model", "Rows", "MAE MW", "RMSE MW", "R²"],
                     [[name, m["rows"], *[round(m[k], 6) for k in ("mae_mw", "rmse_mw", "r2")]]
                      for name, m in values.items()])
    selected = r["selection"]["selected_model"]
    sections = ["# Solar Advanced Model Evaluation\n", "## 1. Objective\n", TASK + ".\n",
        "## 2. Dataset and Fixed Feature Set\n", block(r["dataset"]), block(r["feature_order"]),
        "Unchanged 5B data and policies, including humidity exclusion, sentinel handling and retained zeros. No preprocessing or feature changes.\n",
        "## 3. Chronological Evaluation Protocol\n",
        "TRAIN: 2019 (34,987); VALIDATION: January–June 2020 (17,472); TEST: July–December 2020 (17,657). Manifest boundaries, counts, order and hashes are checked. TRAIN alone fits both candidates; no refit, shuffle, CV, parameter search or internal early stopping. Selection is saved before a single selected-model test prediction. Reruns verify hashes and reuse results.\n",
        "## 4. Baseline Random Forest Reference\n", scores({"random_forest": r["validation"]["random_forest"]}),
        "Existing 5C artifact and metrics are reused, without baseline retraining. Metadata must match the same dataset, feature order, target and splits.\n",
        "## 5. Two Advanced Candidates\n",
        "HistGradientBoosting uses shallow leaf-limited boosting with shrinkage and L2 regularization. ExtraTrees uses randomized tree thresholds with bounded depth/leaf size. Exactly one configuration per family was declared before training.\n",
        "## 6. Actual Model Parameters\n", block(r["parameters"]),
        "One native thread; seed 42. Histogram early_stopping=False prevents a random internal validation split.\n",
        "## 7. Validation Comparison\n", scores(r["validation"]),
        "## 8. Model Selection Decision\n", block(r["selection"]),
        "## 9. Held-Out Test Results\n", scores({selected: r["test"]}),
        "Only the frozen overall winner receives a test prediction in 5D. All diagnostics reuse it; losing candidates are not scored on test. The period was already reported in 5C, so it is held out from fitting/selection but is not a previously unseen benchmark.\n",
        "## 10. Comparison with Baseline\n", scores({"5C random_forest (historical test)": r["baseline_test"], selected + " (5D test)": r["test"]}),
        "Signed error reductions (baseline minus selected; negative means deterioration):\n", block(r["comparison"]),
        "These retrospective test differences do not change selection.\n", "## 11. Focused Diagnostics\n",
        f"Positive TRAIN tertiles reused from 5C: {r['power_boundaries_mw']}; zero separate; positive ranges open-left/closed-right. Recorded hours do not imply verified local solar time.\n"]
    for split, diag in r["diagnostics"].items():
        sections.append(f"### {split.capitalize()}\n")
        for group in ("zero_positive", "power_ranges", "recorded_hour", "month"):
            sections += [group.replace("_", " ") + ":\n",
                table(["Group", "Rows", "MAE MW", "RMSE MW"],
                      [[x["group"], x["rows"], round(x["mae_mw"], 6) if x["mae_mw"] is not None else None,
                        round(x["rmse_mw"], 6) if x["rmse_mw"] is not None else None] for x in diag[group]])]
        sections += [block(diag["residual"]), block(diag["prediction_range"])]
    sections += ["Feature importance:\n", block(r["feature_importance"]),
        "Native impurity importance is model-specific and affected by correlated features; it is not causal evidence. Histogram boosting has no native importance; no permutation computation is added.\n",
        "## 12. Important Limitations\n", "\n".join("- " + x for x in LIMITATIONS),
        "\nSingle chronological comparison; no confidence intervals or statistical significance claim. Previously observed test results limit independent confirmation. Future adaptations need a fresh untouched period. Predictions are not clipped; small negative boosting estimates may occur.\n",
        "The model performs weather-to-solar-power estimation using observed contemporaneous weather and irradiance measurements. It is NOT true future solar forecasting.\n",
        "## 13. Final Model Recommendation\n", f"**{selected}**, under the predeclared validation rule. No operational readiness claim.\n",
        "Reproduce/verify: `python -m ml.training.train_solar_advanced`. Models and JSON artifacts remain Git-ignored. No prediction CSV, new dependency, API integration or future milestone component was added.\n"]
    return "\n".join(sections)


def run_training(root: Path = ROOT) -> dict[str, Any]:
    """Train two candidates, freeze validation selection, then score only its winner."""
    root = root.resolve()
    artifacts = root / "ml/artifacts"
    contract = load_contract(root / "docs/solar_feature_manifest.json")
    baseline = json.loads((artifacts / "solar_baseline_metrics.json").read_text(encoding="utf-8"))
    metadata = json.loads((artifacts / "solar_best_baseline_metadata.json").read_text(encoding="utf-8"))
    reference = baseline_reference(contract, baseline, metadata)
    protected = {**baseline["protected_input_hashes"], **baseline["code_hashes"]}
    verify_hashes(root, protected)
    for path in ["docs/solar_baseline_model_report.md", "ml/artifacts/solar_baseline_metrics.json",
                 "ml/artifacts/solar_best_baseline_metadata.json", "ml/artifacts/solar_random_forest.joblib",
                 "ml/models/solar_advanced.py", "ml/training/train_solar_advanced.py"]:
        protected[path] = sha256(root / path)
    for name in [*MODEL_FILES.values(), METRICS, METADATA, RECEIPT]:
        path = artifacts / name
        if path.resolve() != path or path.is_symlink():
            raise ValueError(f"Artifact path redirects: {path}")
        require_ignored(root, path.relative_to(root).as_posix())
    if (artifacts / METADATA).exists():
        saved = json.loads((artifacts / METADATA).read_text(encoding="utf-8"))
        if saved["protected_hashes"] != protected:
            raise ValueError("Inputs or code differ from completed 5D experiment; refusing reevaluation")
        verify_hashes(root, saved["result_hashes"])
        print(f"Verified completed 5D experiment: {saved['selected_model']}; no retraining or test reevaluation.")
        return json.loads((artifacts / METRICS).read_text(encoding="utf-8"))
    if (artifacts / RECEIPT).exists():
        raise ValueError("Final evaluation already started; inspect saved results before repeating")
    data = load_dataset(root / contract["dataset"]["path"], contract)
    parts = split_dataset(data, contract)
    boundaries = baseline["power_bins"]["cutpoints_mw"]
    if boundaries != power_boundaries(parts["train"][contract["target"]]):
        raise ValueError("5C positive-training range boundaries differ")
    models = create_models()
    parameters = model_parameters(models)
    validation, predictions = {}, {}
    with threadpool_limits(limits=1):
        for name, model in models.items():
            print(f"Training {name} on TRAIN only", flush=True)
            model.fit(ordered_features(parts["train"], contract), parts["train"][contract["target"]])
            predictions[name] = model.predict(ordered_features(parts["validation"], contract))
            validation[name] = calculate_metrics(parts["validation"][contract["target"]], predictions[name])
            print(f"{name}: {validation[name]}", flush=True)
        decision = select_overall(validation, reference)
        selected = decision["selected_model"]
        if selected == "random_forest":
            model = joblib.load(artifacts / "solar_random_forest.joblib")
            if list(model.feature_names_in_) != contract["features"] or model.get_params() != metadata["parameters"]:
                raise ValueError("Saved baseline estimator differs from metadata")
            predictions[selected] = model.predict(ordered_features(parts["validation"], contract))
            checked = calculate_metrics(parts["validation"][contract["target"]], predictions[selected])
            if not np.allclose([checked[k] for k in ("mae_mw", "rmse_mw", "r2")],
                               [reference[k] for k in ("mae_mw", "rmse_mw", "r2")], rtol=1e-12, atol=1e-12):
                raise ValueError("Saved baseline validation scores do not reproduce")
        else:
            model = models[selected]
        validation = {"random_forest": reference, **validation}
        for name, candidate in models.items():
            joblib.dump(candidate, artifacts / MODEL_FILES[name], compress=3)
        dump(artifacts / RECEIPT, {"selection": decision, "validation": validation,
                                  "parameters": parameters, "protected_hashes": protected,
                                  "status": "Selection frozen; single selected-model test evaluation about to start"})
        print(f"Frozen selection: {selected}. Evaluating only this model on TEST.", flush=True)
        test_prediction = model.predict(ordered_features(parts["test"], contract))
    test = calculate_metrics(parts["test"][contract["target"]], test_prediction)
    baseline_test = baseline["metrics"]["random_forest"]["test"]
    result = {"task": TASK, "dataset": contract["dataset"], "feature_order": contract["features"],
              "target": contract["target"], "timestamp": contract["timestamp"], "splits": contract["splits"],
              "parameters": parameters, "selection": decision, "validation": validation, "test": test,
              "baseline_test": baseline_test, "power_boundaries_mw": boundaries,
              "comparison": {split: {"mae_reduction_mw": base["mae_mw"] - score["mae_mw"],
                                       "rmse_reduction_mw": base["rmse_mw"] - score["rmse_mw"],
                                       "r2_increase": score["r2"] - base["r2"]}
                             for split, base, score in [("validation", reference, validation[selected]), ("test", baseline_test, test)]},
              "diagnostics": {split: focused_diagnostics(parts[split], prediction, contract, boundaries)
                              for split, prediction in [("validation", predictions[selected]), ("test", test_prediction)]},
              "feature_importance": forest_importance(model, contract["features"]) if hasattr(model, "feature_importances_")
                                    else {"available": False, "reason": "No native importance; permutation importance not computed"},
              "runtime": {"python": platform.python_version(), "sklearn": sklearn.__version__,
                          "numpy": np.__version__, "pandas": pd.__version__, "joblib": joblib.__version__, "native_threads": 1}}
    dump(artifacts / METRICS, result)
    (root / REPORT).write_text(render_report(result), encoding="utf-8")
    verify_hashes(root, protected)
    outputs = ["ml/artifacts/" + name for name in [*MODEL_FILES.values(), METRICS, RECEIPT]] + [REPORT]
    dump(artifacts / METADATA, {"selected_model": selected,
          "model_path": "ml/artifacts/" + MODEL_FILES.get(selected, "solar_random_forest.joblib"),
          "parameters": model.get_params(), "feature_order": contract["features"], "target": contract["target"],
          "dataset": contract["dataset"], "splits": contract["splits"], "selection": decision,
          "validation_metrics": validation[selected], "test_metrics": test, "test_evaluation_count": 1,
          "protected_hashes": protected, "result_hashes": {p: sha256(root / p) for p in outputs},
          "runtime": result["runtime"]})
    print(json.dumps({"selection": decision, "validation": validation, "test": test}, indent=2), flush=True)
    return result


if __name__ == "__main__":
    try:
        run_training()
    except (OSError, ValueError, KeyError) as exc:
        raise SystemExit(f"Advanced solar evaluation failed: {exc}") from exc
