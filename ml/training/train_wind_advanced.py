"""Eight predeclared validation experiments; one final test evaluation."""

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
from sklearn.inspection import permutation_importance
from threadpoolctl import threadpool_limits

from ml.data_processing.run_wind_analysis import sha256, table
from ml.models.wind_baseline import (load_feature_configuration,load_prepared_dataset,
    review_feature_configuration,review_split_overlap,split_chronologically)
from ml.models.wind_advanced import (NEAR_TIE_MW,analyze_residuals,baseline_improvement,
    calculate_capacity_metrics,compare_experiments,create_model,evaluate_model,
    feature_experiments,get_model_candidates,prediction_frame)

ROOT = Path(__file__).resolve().parents[2]
ARTIFACTS = ROOT/"ml/artifacts"
FILES = ["wind_best_model.joblib","wind_best_model_metadata.json","wind_advanced_experiments.json",
         "wind_advanced_feature_importance.json","wind_best_model_test_predictions.csv","wind_advanced_error_analysis.json"]


def dump(path: Path, data: Any) -> None:
    """Write finite JSON; never silently emit non-standard NaN values."""
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2,allow_nan=False)+"\n",encoding="utf-8")


def render_report(meta: dict[str,Any], experiments: dict[str,Any], importance: dict[str,Any], errors: dict[str,Any]) -> str:
    """Render the complete report from frozen experiments and one prediction array."""
    def block(x: Any) -> str:
        return "```json\n"+json.dumps(x,ensure_ascii=False,indent=2,allow_nan=False)+"\n```\n"
    records = experiments["experiments"]
    result_rows = [[r["experiment"],r["feature_count"],s,*[round(r[s][k],6) for k in
        ("mae_mw","rmse_mw","r2","mae_capacity_percent","rmse_capacity_percent")]] for r in records for s in ("train","validation")]
    pair_rows = []
    for candidate in get_model_candidates():
        a,b = (next(r for r in records if r["experiment"] == f"{group}_{candidate['name']}") for group in ("A","B"))
        pair_rows.append([candidate["name"],a["validation"]["mae_mw"],b["validation"]["mae_mw"],
                          a["validation"]["mae_mw"]-b["validation"]["mae_mw"],a["leaf_budget"]])
    def extrema(rows: list[dict[str,Any]]) -> dict[str,Any]:
        return {"lowest_mae":min(rows,key=lambda r:r["mae_mw"]),"highest_mae":max(rows,key=lambda r:r["mae_mw"])}
    return "\n".join([
        "# GridCast AI Advanced Wind Power Model Report\n",
        "## 1. Prediction Task\n", "**Weather-to-Wind-Power Estimation — Not True Future Forecasting.** "
        "Observed weather plus calendar at T estimates Power (MW) at T. No forecast-weather service, horizon, "
        "lagged target or multi-step prediction is implemented.\n",
        "## 2. Baseline Performance\n", block(meta["baseline"]),
        "The existing random forest wins Milestone 3 validation but has training MAE 3.1955 versus validation "
        "6.0355 MW. Hub speed dominates native importance (76.45%), followed by 50 m speed (12.99%). "
        "This motivates shrinkage and smaller boosting trees rather than expanding the random forest blindly. "
        "Baseline artifacts were read and hashed; no baseline retraining occurred.\n",
        "## 3. Advanced Model Candidates\n", "HistGradientBoostingRegressor provides efficient binned nonlinear "
        "interactions with L2 regularization. GradientBoostingRegressor supplies conventional shallow-tree "
        "boosting without histogram binning. ExtraTrees is omitted because the existing forest already supplies "
        "a bagged-tree comparator. No additional ML framework is used.\n",
        "## 4. Feature Experiments\n", block(experiments["feature_experiments"]),
        "A has 10 original weather plus 9 calendar features (19 total). B adds the six engineered direction "
        "encodings (25 total). Both retain original measured directions and separate wind heights. "
        "All names come from the unchanged Milestone 2 manifest. No hidden feature search occurs.\n",
        block(meta["feature_availability"]),
        "All included predictors are SAFE FOR SAME-TIMESTAMP ESTIMATION. Observed weather and direction "
        "encodings are CONDITIONAL FOR FUTURE FORECASTING: replace them with as-issued weather forecasts and "
        "define forecast origin/horizon. Target and timestamp are EXCLUDE from predictors; timestamp remains "
        "a split key. The ambiguous hub degree column remains excluded.\n",
        "## 5. Chronological Validation Strategy\n", block(meta["periods"]),
        "Training: 2019; validation: January–June 2020; test: July–December 2020. No shuffle, random CV or "
        "internal random validation is used; histogram early stopping is explicitly disabled. All fits use "
        "training only. No train+validation refit. Existing gaps after cleaning are preserved.\n",
        "**Holdout limitation:** this period's baseline scores were already reported in Milestone 3. It is "
        "held out from advanced fitting/selection, but is not a never-before-observed benchmark. The experiment "
        "plan was fixed before advanced test predictions. Only the selected model was evaluated once on it; "
        "all subsequent error summaries reuse that prediction array and never alter selection.\n",
        "## 6. Parameter Experiments\n", block(experiments["candidate_plan"]),
        "All four configurations are crossed with A/B: eight total, including unsuccessful candidates. "
        "One native thread is used throughout; random_state=42. No stochastic subsampling or random "
        "validation fraction. No timing fields are used in selection or deterministic metadata.\n",
        "## 7. Model Comparison\n",table(["Experiment","Features","Split","MAE MW","RMSE MW","R²","MAE %","RMSE %"],result_rows),
        "Feature-pair comparison (positive A−B means engineered directions improved MAE):\n",
        table(["Configuration","A validation MAE","B validation MAE","A−B MAE MW","Tree-leaf budget"],pair_rows),
        "Direction-feature benefit is configuration-dependent. The final feature group is selected on the "
        "same predeclared validation criteria; engineered features are not retained simply because they exist.\n",
        "## 8. Best Model Selection\n", f"**Selected advanced experiment: {meta['experiment']}**.\n",
        meta["selection_criteria"]+"\n",
        "The comparison function rejects records containing test metrics. The selected model and experiment "
        "ledger are saved before final evaluation. Structural leaf budget proxies complexity; it is not a "
        "measurement of inference speed. The final advanced candidate is saved even if it fails to improve "
        "on the baseline; signed comparisons below disclose that outcome.\n",
        "## 9. Held-Out Test Evaluation\n",block(meta["test_metrics"]),
        "MAE/RMSE are MW; percentages use 99 MW, not MAPE. R² is dimensionless. Predictions are not clipped.\n",
        "## 10. Baseline vs Advanced Comparison\n",block(meta["baseline_comparison"]),
        "Positive error improvement means reduction; negative means deterioration. These retrospective "
        "comparisons do not trigger model reselection or additional tuning.\n",
        "## 11. Overfitting Analysis\n",table(["Experiment","Train MAE","Validation MAE","Gap MW"],
            [[r["experiment"],r["train"]["mae_mw"],r["validation"]["mae_mw"],r["validation"]["mae_mw"]-r["train"]["mae_mw"]] for r in records]),
        block(meta["generalisation"]),
        "Large positive train/validation gaps are consistent with overfitting and/or temporal shift, not proof "
        "of one cause. Similar poor errors may indicate underfitting. Compare actual magnitudes against the "
        "baseline; no model is declared generally reliable from a single site and two years.\n",
        "## 12. Residual Analysis\n",block({k:errors[k] for k in ("residual_definition","summary","absolute_error_quantiles")}),
        "Population standard deviation uses ddof=0. A 30-bin residual histogram is saved in the error-analysis "
        "JSON. The prediction CSV also supplies actual-vs-predicted data, avoiding a duplicate output file.\n",
        "## 13. Error by Power Range\n",block(errors["by_power_range"]),block(extrema(errors["by_power_range"])),
        "Groups use actual power divided by 99 MW: [0,10), [10,25), [25,50), [50,75), [75,100] percent. "
        "Best/worst here mean lowest/highest group MAE, not confidence-adjusted rankings. Counts matter.\n",
        "## 14. Time-Based Error Analysis\n",block({"by_hour":errors["by_hour"],"by_month":errors["by_month"]}),
        block({"hour_extrema":extrema(errors["by_hour"]),"month_extrema":extrema(errors["by_month"])}),
        "**OBSERVED PATTERN:** the tables identify higher/lower errors only in the evaluated period. "
        "**POSSIBLE EXPLANATION:** changes in weather/power mix, operating conditions or temporal shift could "
        "contribute; these causes are not established by available metadata. No strong daily pattern is assumed. "
        +errors["season_decision"]+"\n",
        "## 15. Feature Importance\n",block({k:v for k,v in importance.items() if k != "features"}),
        table(["Permutation rank","Feature","Native importance","Validation MAE increase MW","Repeat std MW"],
            [[r["rank"],r["feature"],r["native_importance"],r["permutation_mean_mw"],r["permutation_std_mw"]] for r in importance["features"]]),
        "Permutation importance uses the full validation split, three repeats, negative MAE scoring, "
        "seed 42 and one worker. It is computed after selection and does not feed selection. Native importance "
        "is null when unavailable (histogram boosting); all gradient-boosting candidates' native values are "
        "also retained in the experiment ledger. Importance is not causation. Correlated heights/encodings "
        "can share or mask importance; small negative values can reflect noise.\n",
        "## 16. Final Model\n",block({k:meta[k] for k in ("model_type","parameters","feature_names","feature_count","target","nominal_capacity_mw","dataset")}),
        "Saved `ml/artifacts/wind_best_model.joblib` with `wind_best_model_metadata.json`. All generated local "
        "artifacts are Git-ignored. Raw/prepared data, preprocessing, baseline code and baseline artifacts remain "
        "unchanged. Rerunning verifies saved results and reuses them rather than reevaluating the test set.\n",
        "```powershell\npython -m ml.training.train_wind_advanced\n```\n",
        "## 17. Limitations\n", "Single wind farm; site-specific model; observed weather; same-timestamp "
        "estimation; not true future forecasting; no weather forecast integration; limited temporal coverage; "
        "no demonstrated multi-site generalisation. Source timezone/location and operational metadata are "
        "incomplete. Complete-case row omission can bias results. Repeated validation comparison can overfit "
        "that period. Test residual analysis is descriptive only; any future adaptation needs a new untouched "
        "evaluation period. No confidence intervals or causal claims.\n",
        "## 18. Recommended Next Steps\n", "Recommendations only: collect additional sites/years, retain a "
        "new untouched holdout, investigate documented operating regimes, and define forecast inputs/horizon "
        "before future forecasting. No solar, demand, grid, API, UI or Milestone 5 work is implemented.\n"])


def main() -> None:
    """Run once, or verify/reuse the frozen completed experiment on subsequent calls."""
    baseline_path = ARTIFACTS/"wind_baseline_metrics.json"
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    config = load_feature_configuration(ROOT/"docs/wind_feature_manifest.json")
    protected = {p:sha256(ROOT/p) for p in baseline["protected_input_hashes"]}
    for p,digest in baseline["protected_input_hashes"].items():
        if protected[p] != digest:
            raise ValueError(f"Input differs from Milestone 3: {p}")
    for p in list(ARTIFACTS.glob("*baseline*"))+[ARTIFACTS/"linear_regression.joblib",ARTIFACTS/"wind_test_predictions.csv",ARTIFACTS/"wind_validation_predictions.csv",ROOT/"ml/models/wind_baseline.py",ROOT/"ml/training/train_wind_baseline.py"]:
        if p.is_file():
            protected[p.relative_to(ROOT).as_posix()] = sha256(p)
    metadata_path = ARTIFACTS/"wind_best_model_metadata.json"
    if metadata_path.exists():
        saved = json.loads(metadata_path.read_text(encoding="utf-8"))
        if saved["protected_hashes"] != protected:
            raise ValueError("Inputs differ from completed experiment; do not silently repeat test evaluation")
        for path,digest in saved["result_hashes"].items():
            if sha256(ROOT/path) != digest:
                raise ValueError(f"Saved result changed: {path}")
        print(f"Verified completed experiment {saved['experiment']}; reusing its single test evaluation.")
        return
    receipt = ARTIFACTS/"wind_advanced_test_started.json"
    if receipt.exists():
        raise ValueError("A final evaluation was already started; inspect saved results before any repeat")
    for name in FILES+[receipt.name]:
        if subprocess.run(["git","check-ignore","-q",f"ml/artifacts/{name}"],cwd=ROOT).returncode:
            raise ValueError(f"Output must be Git-ignored: {name}")
    data = load_prepared_dataset(ROOT/config["manifest"]["output"]["path"],config)
    splits = split_chronologically(data,config["timestamp"])
    review_split_overlap(splits,config)
    if data.shape != (70036,27):
        raise ValueError("Unexpected prepared shape")
    for name,part in splits.items():
        expected = baseline["splits"][name]
        if (len(part),str(part[config["timestamp"]].min()),str(part[config["timestamp"]].max())) != (expected["rows"],expected["start"],expected["end"]):
            raise ValueError("Chronological split differs from baseline")
    groups, candidates = feature_experiments(config), get_model_candidates()
    records, models = [], {}
    with threadpool_limits(limits=1):
        for group,features in groups.items():
            for candidate in candidates:
                name = f"{group}_{candidate['name']}"
                model = create_model(candidate)
                print(f"Training {name}: {len(features)} features, 2019 only",flush=True)
                model.fit(splits["train"][features],splits["train"][config["target"]])
                params = candidate["parameters"]
                leaf_budget = params.get("max_iter",params.get("n_estimators"))*params.get("max_leaf_nodes",2**params.get("max_depth",3))
                record = {"experiment":name,"model":candidate["model"],"parameters":params,
                    "feature_experiment":group,"feature_names":features,"feature_count":len(features),"leaf_budget":leaf_budget,
                    "train":evaluate_model(model,splits["train"],features,config["target"]),
                    "validation":evaluate_model(model,splits["validation"],features,config["target"]),
                    "native_importance":dict(zip(features,map(float,model.feature_importances_))) if hasattr(model,"feature_importances_") else None}
                records.append(record)
                models[name] = model
                print(f"{name}: validation MAE {record['validation']['mae_mw']:.6f} MW",flush=True)
        selected = compare_experiments(records)
        record = next(r for r in records if r["experiment"]==selected)
        model, features = models[selected], record["feature_names"]
        for r in records:
            r["selection_status"] = "selected" if r["experiment"]==selected else "not selected"
        experiments = {"candidate_plan":candidates,"feature_experiments":groups,"experiments":records,"selected":selected}
        dump(ARTIFACTS/"wind_advanced_experiments.json",experiments)
        joblib.dump(model,ARTIFACTS/"wind_best_model.joblib",compress=3)
        print(f"Selection frozen: {selected}. Computing validation-only permutation importance.",flush=True)
        permutation = permutation_importance(model,splits["validation"][features],splits["validation"][config["target"]],
                                             scoring="neg_mean_absolute_error",n_repeats=3,random_state=42,n_jobs=1)
        native = record["native_importance"]
        ranks = sorted([{"feature":c,"native_importance":native[c] if native else None,
                         "permutation_mean_mw":float(permutation.importances_mean[i]),
                         "permutation_std_mw":float(permutation.importances_std[i])} for i,c in enumerate(features)],
                        key=lambda x:(-x["permutation_mean_mw"],x["feature"]))
        importance = {"dataset":"validation only; all 17,470 rows","scoring":"negative MAE; positive importance means increased MAE",
            "n_repeats":3,"random_state":42,"native_available":native is not None,
            "features":[dict(rank=i+1,**r) for i,r in enumerate(ranks)]}
        dump(ARTIFACTS/"wind_advanced_feature_importance.json",importance)
        dump(receipt,{"experiment":selected,"status":"test prediction about to run exactly once","protected_hashes":protected})
        print("Running the single final test prediction/evaluation.",flush=True)
        predicted = model.predict(splits["test"][features])
    predictions = prediction_frame(splits["test"][config["timestamp"]],splits["test"][config["target"]],predicted,selected)
    test_metrics = calculate_capacity_metrics(predictions.actual_power_mw,predicted)
    errors = analyze_residuals(predictions)
    predictions.to_csv(ARTIFACTS/"wind_best_model_test_predictions.csv",index=False,float_format="%.15g")
    dump(ARTIFACTS/"wind_advanced_error_analysis.json",errors)
    best_baseline = baseline["best_baseline_model"]
    comparison = baseline_improvement(baseline["metrics"][best_baseline]["test"],test_metrics)
    meta = {"experiment":selected,"model_type":record["model"],"parameters":model.get_params(),"feature_names":features,
        "feature_count":len(features),"target":config["target"],"nominal_capacity_mw":99,"dataset":baseline["dataset"],
        "periods":baseline["splits"],"train_metrics":record["train"],"validation_metrics":record["validation"],"test_metrics":test_metrics,
        "prediction_task":"Weather-to-Wind-Power Estimation at T; not true future forecasting",
        "limitations":["single site","observed weather","unknown source timezone","no future weather forecast integration","test period previously reported in Milestone 3"],
        "selection_criteria":f"Minimum validation MAE; within {NEAR_TIE_MW} MW prefer lower tree-leaf budget, then fewer features, lower validation RMSE, higher validation R², lower MAE and stable id. No test input to selection.",
        "baseline":{"model":best_baseline,"metrics":baseline["metrics"][best_baseline]},"baseline_comparison":comparison,
        "feature_availability":review_feature_configuration(config),"protected_hashes":protected,
        "generalisation":{"train_validation_mae_gap":record["validation"]["mae_mw"]-record["train"]["mae_mw"],
                          "validation_test_mae_gap":test_metrics["mae_mw"]-record["validation"]["mae_mw"],
                          "interpretation":"Positive gaps suggest overfitting and/or temporal shift; no causal attribution from this holdout."},
        "test_evaluation_count":1,"runtime":{"python":platform.python_version(),"sklearn":sklearn.__version__,"numpy":np.__version__,"pandas":pd.__version__,"native_threads":1},
        "code_hashes":{p:sha256(ROOT/p) for p in ("ml/models/wind_advanced.py","ml/training/train_wind_advanced.py")}}
    report = ROOT/"docs/wind_advanced_model_report.md"
    report.write_text(render_report(meta,experiments,importance,errors),encoding="utf-8")
    for path,digest in protected.items():
        if sha256(ROOT/path)!=digest:
            raise ValueError(f"Protected input changed: {path}")
    meta["result_hashes"] = {p.relative_to(ROOT).as_posix():sha256(p) for p in [*(ARTIFACTS/name for name in FILES if name!=metadata_path.name),report,receipt]}
    dump(metadata_path,meta)
    print(json.dumps({"selected":selected,"validation":record["validation"],"test":test_metrics,"comparison":comparison},indent=2),flush=True)


if __name__=="__main__":
    try:
        main()
    except (OSError,ValueError,KeyError) as exc:
        raise SystemExit(f"Advanced estimation failed: {exc}") from exc
