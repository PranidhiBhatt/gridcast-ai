"""Run fixed, chronological weather-to-wind-power estimation baselines."""

from __future__ import annotations

import json
import platform
import subprocess
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
import sklearn

from ml.data_processing.run_wind_analysis import sha256, table
from ml.models.wind_baseline import (
    RF_CONFIG, SEED, evaluate_models, load_feature_configuration, load_prepared_dataset,
    prediction_output, review_feature_configuration, review_split_overlap,
    select_best_model, split_chronologically, train_models, validate_prepared_dataset,
)

ROOT = Path(__file__).resolve().parents[2]
MODEL_FILES = {"mean_baseline": "dummy_baseline.joblib", "linear_regression": "linear_regression.joblib",
               "random_forest": "random_forest_baseline.joblib"}


def overfitting_review(metrics: dict[str, Any]) -> dict[str, Any]:
    """Report numerical gaps and cautious interpretation, never tune from test scores."""
    result = {}
    for name, scores in metrics.items():
        train, val, test = (scores[s]["mae_mw"] for s in ("train","validation","test"))
        if name == "mean_baseline":
            interpretation = "UNDERFITTING benchmark by construction: constant output ignores all weather; not a production model."
        elif val > 1.25*train:
            interpretation = "Possible OVERFITTING and/or temporal distribution shift: validation MAE exceeds training by >25%. This descriptive threshold is not a tuning or model-selection rule."
        else:
            interpretation = "Train/validation gap does not show strong overfitting under the descriptive 25% MAE-gap rule; absolute errors and held-out behavior still matter."
        result[name] = {"train_mae_mw": train, "validation_mae_mw": val, "test_mae_mw": test,
                        "validation_minus_train_mae_mw": val-train, "test_minus_validation_mae_mw": test-val,
                        "interpretation": interpretation}
    return result


def render_report(experiment: dict[str, Any], importance: list[dict[str, Any]]) -> str:
    """Generate the complete evidence report from this experiment's actual results."""
    e = experiment
    def block(value: Any) -> str:
        return "```json\n"+json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+"\n```\n"
    rows = [[name, split, *(round(m[k],6) for k in ("mae_mw","rmse_mw","r2","mae_capacity_percent","rmse_capacity_percent"))]
            for name,scores in e["metrics"].items() for split,m in scores.items()]
    parts = ["# GridCast AI Wind Power Baseline Model Report\n",
        "## 1. Prediction Task Definition\n", "**Weather-to-Wind-Power Estimation — Not True Future Forecasting.** "
        "Input observed weather and calendar variables at timestamp T; estimate wind power in MW at the same T. "
        "There is no prediction horizon, lag construction or external weather forecast input in this experiment.\n",
        "## 2. Dataset\n", block(e["dataset"]),
        "Input is the unchanged Milestone 2 CSV. Shape, exact headers, missingness, ordering and split counts "
        "match its report/manifest. Nominal cadence is 15 minutes, with 140 documented omissions causing gaps. "
        "No new cleaning, random shuffle, resampling or imputation is performed.\n",
        "## 3. Target\n", f"`{e['target']}`; MW power, nominal capacity {e['nominal_capacity_mw']} MW. "
        "Target is never a predictor. Zero power is retained. Estimator outputs are not clipped; all metrics "
        "reflect raw predictions, including any physically implausible linear outputs.\n",
        "## 4. Feature Set\n", f"{e['feature_count']} predictors loaded from `docs/wind_feature_manifest.json`.\n",
        block(e["feature_groups"]),
        table(["Exact feature", "Why included", "Same-time classification", "Future use"],
              [[json.dumps(c,ensure_ascii=False), e["leakage_review"][c]["inclusion_reason"],
                e["leakage_review"][c]["estimation"],e["leakage_review"][c]["future_use"]] for c in e["feature_names"]]),
        "Excluded predictors:\n", block(e["excluded_predictors"]),
        "## 5. Feature Availability and Leakage Considerations\n",
        "Observed weather and its deterministic direction encodings are **SAFE FOR SAME-TIMESTAMP ESTIMATION** "
        "when all inputs at T are available. They are **CONDITIONAL FOR FUTURE FORECASTING**: replace them with "
        "as-issued forecast weather and define origin/horizon before claiming future prediction. Calendar "
        "variables are known in advance but require a consistent timezone convention. The source timezone is unknown.\n"
        "Raw timestamp and target are excluded. Exact-schema validation rejects extra columns; feature provenance "
        "is checked against Milestone 2 roles and reviewed deterministic engineering. Obvious target/future feature "
        "names and exact copies of the target are rejected. These checks cannot prove absence of an undisclosed "
        "upstream target-derived transformation; the unchanged preprocessing code supplies the reviewed lineage. "
        "Linear scaling fits only training rows, inside the saved pipeline. No feature selection or tuning uses test.\n",
        block(e["split_overlap_review"]),
        "Exact feature/target signatures excluding timestamps were also checked across partitions; rounded "
        "or near-duplicate measurements are not the same as proven duplicated records.\n",
        "## 6. Chronological Split\n", table(["Split","Start","End","Rows","Dataset %"],
            [[s,m["start"],m["end"],m["rows"],round(m["percent"],5)] for s,m in e["splits"].items()]),
        "The existing 2019 / January–June 2020 / July–December 2020 plan is unchanged. All models fit training "
        "only; there is no train+validation refit. Test metrics are computed after selection is frozen.\n",
        "## 7. Models Evaluated\n", "### Mean Baseline\n",
        "DummyRegressor predicts the training-set mean. This is a constant benchmark, not a useful production model.\n",
        "### Linear Regression\n", "StandardScaler followed by ordinary least squares with an intercept. "
        "Both stages fit training only. Named features are preserved through the scaler. The saved pipeline "
        "contains its scaler, so no separate scaler artifact is needed.\n",
        "### Random Forest\n", "Fixed lightweight configuration selected before results; no hyperparameter search. "
        "One worker and a fixed seed aid reproducibility. Correlated original/cyclic predictors are retained "
        "for this baseline rather than tuned feature selection.\n", block(e["model_configurations"]),
        "## 8. Evaluation Metrics\n", "MAE is mean absolute prediction error in MW. RMSE is the square root "
        "of mean squared error in MW and weights large errors more heavily. R² compares squared error with "
        "the evaluation split's own mean benchmark; 1 is perfect, 0 matches that benchmark, and negative values "
        "are possible. Capacity-normalized errors are 100 × error / 99; they are not MAPE.\n",
        "## 9. Model Results\n", table(["Model","Split","MAE MW","RMSE MW","R²","MAE % capacity","RMSE % capacity"],rows),
        "Full-precision metrics are saved locally in `ml/artifacts/wind_baseline_metrics.json`.\n",
        "## 10. Best Baseline Model\n", f"**BEST BASELINE MODEL: {e['best_baseline_model']}**. "
        "Selection criterion: lowest validation MAE; ties use validation RMSE, then model name. "
        "The selection function receives validation metrics only. No test data is used for fitting or selection.\n",
        "## 11. Test Evaluation\n", block(e["metrics"][e["best_baseline_model"]]["test"]),
        "All three predeclared candidates have held-out scores in section 9. The selected model was fixed first; "
        "these results trigger no tuning, changes to features, refitting or reselection. Prediction CSVs store only "
        "the selected model's validation/test outputs to avoid redundant copies of the actual values.\n",
        "Prediction-range diagnostics (no clipping):\n", block(e["prediction_range_checks"]),
        "## 12. Overfitting Review\n", block(e["overfitting_review"]),
        "A train-to-validation gap can reflect overfitting, temporal distribution shift or both. A single "
        "chronological holdout cannot establish causality or multi-site generalisation. Compare absolute errors "
        "against the mean benchmark as well as gaps; similar poor scores can indicate underfitting.\n",
        "## 13. Feature Importance\n", table(["Rank","Feature","Importance"],
            [[r["rank"],json.dumps(r["feature"],ensure_ascii=False),round(r["importance"],8)] for r in importance]),
        "Random forest impurity-based importance reflects model usage, not causation. Correlated heights, "
        "raw directions and their encodings can share importance. No test-based permutation or feature tuning "
        "is performed. Full values are in `wind_baseline_feature_importance.json`.\n",
        "## 14. Limitations\n", "Single wind farm; site-specific model; observed weather inputs; not yet true "
        "future forecasting; no external weather forecast data; no multi-site generalisation demonstrated. "
        "Missingness-based row omission can bias evaluation. Calendar cycles and correlated features may "
        "complicate linear interpretation. Unbounded linear output can be physically invalid. Source metadata "
        "and timezone remain incomplete. Baselines are fixed and untuned; no confidence intervals or deployment "
        "claims are made. Model serialization is intended for trusted local artifacts in this environment.\n",
        "Reproduce from the repository root:\n\n```powershell\npython -m ml.training.train_wind_baseline\n```\n",
        "Experiment versions and input/code hashes are saved in the metrics artifact. No wall-clock timestamp "
        "or elapsed-time field contaminates deterministic result comparison. Different library/BLAS/platform "
        "versions can produce numerical differences.\n",
        "## 15. Next Steps\n", "Recommendations only: compare additional models in a later milestone; define "
        "forecast origin and horizon; integrate as-issued weather forecasts; evaluate additional sites. "
        "Preserve a new untouched holdout if future experiments adapt to these test results. None of these "
        "next steps is implemented here.\n"]
    return "\n".join(parts)


def main() -> None:
    """Run train→validation→selection→test in that order; save ignored artifacts."""
    config = load_feature_configuration(ROOT/"docs/wind_feature_manifest.json")
    manifest = config["manifest"]
    dataset_path = ROOT/manifest["output"]["path"]
    source_manifest = json.loads((ROOT/"docs/dataset_sources.json").read_text(encoding="utf-8"))
    protected = [dataset_path, ROOT/manifest["source"], ROOT/"docs/wind_feature_manifest.json",
                 ROOT/"ml/data_processing/wind_preprocessor.py", ROOT/"ml/data_processing/run_wind_preprocessing.py"]
    protected += [ROOT/item["relative_path"] for item in source_manifest["sources"]]
    hashes = {p.relative_to(ROOT).as_posix(): sha256(p) for p in protected}
    if hashes[manifest["source"]] != manifest["raw_sha256"]:
        raise ValueError("Raw workbook hash differs from Milestone 2")
    data = load_prepared_dataset(dataset_path,config)
    info = validate_prepared_dataset(data,config)
    if data.shape != (manifest["output"]["rows"], manifest["output"]["columns"]):
        raise ValueError("Prepared shape differs from Milestone 2 report/manifest")
    splits = split_chronologically(data,config["timestamp"])
    overlap = review_split_overlap(splits,config)
    split_info = {s: {"start": str(d[config["timestamp"]].min()), "end": str(d[config["timestamp"]].max()),
                      "rows":len(d), "percent":100*len(d)/len(data)} for s,d in splits.items()}
    if any(any(split_info[s][k] != manifest["audit"]["split_plan"][s][k] for k in ("start","end","rows")) for s in splits):
        raise ValueError("Chronological split discrepancy from Milestone 2; review before training")
    print(f"Verified {len(data):,} rows, {len(config['features'])} predictors and disjoint chronological splits.",flush=True)
    print("Fitting three fixed same-timestamp estimation models on 2019 only...",flush=True)
    models = train_models(splits["train"],config)
    train_scores = evaluate_models(models,splits["train"],config)
    validation_scores = evaluate_models(models,splits["validation"],config)
    selected = select_best_model(validation_scores)
    print(f"Validation selection frozen: {selected}. Evaluating held-out test now.",flush=True)
    test_scores = evaluate_models(models,splits["test"],config)
    scores = {name: {"train":train_scores[name],"validation":validation_scores[name],"test":test_scores[name]} for name in models}
    importance = sorted([{"feature":c,"importance":float(v)} for c,v in zip(config["features"],models["random_forest"].feature_importances_)],key=lambda r:(-r["importance"],r["feature"]))
    importance = [dict(rank=i+1,**r) for i,r in enumerate(importance)]
    range_checks = {name: {s: {"below_zero":int((p<0).sum()), "above_99_mw":int((p>99).sum()),
                              "min_mw":float(p.min()),"max_mw":float(p.max())}
                           for s,d in splits.items() for p in [model.predict(d[config["features"]])]} for name,model in models.items()}
    experiment = {"task":"Weather-to-Wind-Power Estimation at T; not true future forecasting", "seed":SEED,
        "dataset":{"path":dataset_path.relative_to(ROOT).as_posix(),"sha256":hashes[dataset_path.relative_to(ROOT).as_posix()],**info},
        "target":config["target"],"nominal_capacity_mw":config["capacity_mw"],"feature_count":len(config["features"]),
        "feature_names":config["features"],"feature_groups":{k:config[k] for k in ("weather","time","engineered_wind")},
        "excluded_predictors":{**config["excluded"],config["timestamp"]:"Split/index key only",config["target"]:"Response only"},
        "leakage_review":review_feature_configuration(config),"splits":split_info,"split_overlap_review":overlap,
        "model_configurations":{"mean_baseline":{"strategy":"mean"},"linear_regression":{"scaler":"StandardScaler, fit train only, with_mean=True, with_std=True","fit_intercept":True,"positive":False},"random_forest":RF_CONFIG},
        "metrics":scores,"best_baseline_model":selected,"selection_criterion":"Validation MAE ascending, then validation RMSE, then name; selection frozen before test evaluation",
        "overfitting_review":overfitting_review(scores),"prediction_range_checks":range_checks,
        "protected_input_hashes":hashes,
        "code_hashes":{p:sha256(ROOT/p) for p in ("ml/models/wind_baseline.py","ml/training/train_wind_baseline.py")},
        "runtime":{"python":platform.python_version(),"scikit_learn":sklearn.__version__,"pandas":pd.__version__,"numpy":np.__version__,"joblib":joblib.__version__}}
    artifact_dir = ROOT/"ml/artifacts"
    files = [*MODEL_FILES.values(),"wind_baseline_metrics.json","wind_baseline_feature_importance.json",
             "wind_validation_predictions.csv","wind_test_predictions.csv"]
    for filename in files:
        relative = (artifact_dir/filename).relative_to(ROOT).as_posix()
        if subprocess.run(["git","check-ignore","-q",relative],cwd=ROOT).returncode:
            raise ValueError(f"Artifact not ignored: {relative}")
    for path,digest in hashes.items():
        if sha256(ROOT/path) != digest:
            raise ValueError(f"Protected input changed: {path}")
    artifact_dir.mkdir(parents=True,exist_ok=True)
    for name,model in models.items():
        joblib.dump(model,artifact_dir/MODEL_FILES[name],compress=3)
    for s in ("validation","test"):
        prediction_output(models[selected],selected,splits[s],config).to_csv(artifact_dir/f"wind_{s}_predictions.csv",index=False,float_format="%.15g")
    for name,payload in (("wind_baseline_metrics.json",experiment),("wind_baseline_feature_importance.json",importance)):
        (artifact_dir/name).write_text(json.dumps(payload,ensure_ascii=False,indent=2,allow_nan=False)+"\n",encoding="utf-8")
    (ROOT/"docs/wind_baseline_model_report.md").write_text(render_report(experiment,importance),encoding="utf-8")
    for path,digest in hashes.items():
        if sha256(ROOT/path) != digest:
            raise ValueError(f"Protected input changed after writing: {path}")
    print(json.dumps({"best_baseline":selected,"validation":validation_scores[selected],"test":test_scores[selected]},indent=2))
    print("Saved three models (linear scaler included), selected-model predictions, metrics, importance and report; inputs unchanged.")


if __name__ == "__main__":
    try:
        main()
    except (OSError,ValueError,KeyError) as exc:
        raise SystemExit(f"Baseline estimation failed: {exc}") from exc
