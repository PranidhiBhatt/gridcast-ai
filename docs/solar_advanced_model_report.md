# Solar Advanced Model Evaluation

## 1. Objective

Weather-to-Solar-Power Estimation: observed weather/irradiance and calendar at T estimate power at T; not true future forecasting.

## 2. Dataset and Fixed Feature Set

```json
{
  "path": "ml/data/processed/solar_site_1_prepared.csv",
  "rows": 70116,
  "columns": 16,
  "predictors": 14,
  "float_serialization": "17 significant digits; pd.read_csv(float_precision='round_trip') preserves binary measurement values exactly",
  "sha256": "b9d9bdc9ce32b3cf50c807c7ac8dbcedb2c91009551bf21988d1e58857fbc243"
}
```

```json
[
  "Total solar irradiance (W/m2)",
  "Direct normal irradiance (W/m2)",
  "Global horizontal irradiance (W/m2)",
  "Air temperature  (°C) ",
  "Atmosphere (hpa)",
  "hour",
  "day_of_week",
  "month",
  "day_of_year",
  "quarter",
  "hour_sin",
  "hour_cos",
  "annual_sin",
  "annual_cos"
]
```

Unchanged 5B data and policies, including humidity exclusion, sentinel handling and retained zeros. No preprocessing or feature changes.

## 3. Chronological Evaluation Protocol

TRAIN: 2019 (34,987); VALIDATION: January–June 2020 (17,472); TEST: July–December 2020 (17,657). Manifest boundaries, counts, order and hashes are checked. TRAIN alone fits both candidates; no refit, shuffle, CV, parameter search or internal early stopping. Selection is saved before a single selected-model test prediction. Reruns verify hashes and reuse results.

## 4. Baseline Random Forest Reference

| Model | Rows | MAE MW | RMSE MW | R² |
| --- | --- | --- | --- | --- |
| random_forest | 17472 | 2.10255 | 5.281641 | 0.850101 |

Existing 5C artifact and metrics are reused, without baseline retraining. Metadata must match the same dataset, feature order, target and splits.

## 5. Two Advanced Candidates

HistGradientBoosting uses shallow leaf-limited boosting with shrinkage and L2 regularization. ExtraTrees uses randomized tree thresholds with bounded depth/leaf size. Exactly one configuration per family was declared before training.

## 6. Actual Model Parameters

```json
{
  "hist_gradient_boosting": {
    "categorical_features": "from_dtype",
    "early_stopping": false,
    "interaction_cst": null,
    "l2_regularization": 1.0,
    "learning_rate": 0.08,
    "loss": "squared_error",
    "max_bins": 255,
    "max_depth": null,
    "max_features": 1.0,
    "max_iter": 150,
    "max_leaf_nodes": 15,
    "min_samples_leaf": 30,
    "monotonic_cst": null,
    "n_iter_no_change": 10,
    "quantile": null,
    "random_state": 42,
    "scoring": "loss",
    "tol": 1e-07,
    "validation_fraction": 0.1,
    "verbose": 0,
    "warm_start": false
  },
  "extra_trees": {
    "bootstrap": false,
    "ccp_alpha": 0.0,
    "criterion": "squared_error",
    "max_depth": 12,
    "max_features": 1.0,
    "max_leaf_nodes": null,
    "max_samples": null,
    "min_impurity_decrease": 0.0,
    "min_samples_leaf": 5,
    "min_samples_split": 2,
    "min_weight_fraction_leaf": 0.0,
    "monotonic_cst": null,
    "n_estimators": 100,
    "n_jobs": 1,
    "oob_score": false,
    "random_state": 42,
    "verbose": 0,
    "warm_start": false
  }
}
```

One native thread; seed 42. Histogram early_stopping=False prevents a random internal validation split.

## 7. Validation Comparison

| Model | Rows | MAE MW | RMSE MW | R² |
| --- | --- | --- | --- | --- |
| random_forest | 17472 | 2.10255 | 5.281641 | 0.850101 |
| hist_gradient_boosting | 17472 | 2.139205 | 5.243352 | 0.852266 |
| extra_trees | 17472 | 2.050627 | 5.08144 | 0.861249 |

## 8. Model Selection Decision

```json
{
  "best_advanced": "extra_trees",
  "selected_model": "extra_trees",
  "advanced_mae_gain_mw": 0.051923311292554786,
  "advanced_relative_mae_gain": 0.024695394218061998,
  "minimum_relative_mae_gain": 0.01,
  "rule": "Advanced: validation MAE, RMSE, descending R2; exact ties retain declared order. Replace RF only with >=1% validation MAE reduction. No test input.",
  "threshold_note": "Predeclared experiment threshold, not statistical significance or an operational accuracy requirement."
}
```

## 9. Held-Out Test Results

| Model | Rows | MAE MW | RMSE MW | R² |
| --- | --- | --- | --- | --- |
| extra_trees | 17657 | 1.748794 | 4.100357 | 0.909256 |

Only the frozen overall winner receives a test prediction in 5D. All diagnostics reuse it; losing candidates are not scored on test. The period was already reported in 5C, so it is held out from fitting/selection but is not a previously unseen benchmark.

## 10. Comparison with Baseline

| Model | Rows | MAE MW | RMSE MW | R² |
| --- | --- | --- | --- | --- |
| 5C random_forest (historical test) | 17657 | 1.782275 | 4.468826 | 0.892214 |
| extra_trees (5D test) | 17657 | 1.748794 | 4.100357 | 0.909256 |

Signed error reductions (baseline minus selected; negative means deterioration):

```json
{
  "validation": {
    "mae_reduction_mw": 0.051923311292554786,
    "rmse_reduction_mw": 0.20020162377549955,
    "r2_increase": 0.011148532483420515
  },
  "test": {
    "mae_reduction_mw": 0.03348111523230024,
    "rmse_reduction_mw": 0.3684694793700025,
    "r2_increase": 0.01704181756524803
  }
}
```

These retrospective test differences do not change selection.

## 11. Focused Diagnostics

Positive TRAIN tertiles reused from 5C: [10.402465999999995, 27.570731999999992]; zero separate; positive ranges open-left/closed-right. Recorded hours do not imply verified local solar time.

### Validation

zero positive:

| Group | Rows | MAE MW | RMSE MW |
| --- | --- | --- | --- |
| positive | 8961 | 3.997657 | 7.095443 |
| zero | 8511 | 0.000653 | 0.00913 |

power ranges:

| Group | Rows | MAE MW | RMSE MW |
| --- | --- | --- | --- |
| high positive | 2717 | 3.976783 | 5.008258 |
| low positive | 3234 | 3.509833 | 8.320474 |
| medium positive | 3010 | 4.540625 | 7.270383 |
| zero | 8511 | 0.000653 | 0.00913 |

recorded hour:

| Group | Rows | MAE MW | RMSE MW |
| --- | --- | --- | --- |
| 0 | 728 | 0.0 | 0.0 |
| 1 | 728 | 0.0 | 0.0 |
| 2 | 728 | 0.0 | 0.0 |
| 3 | 728 | 0.0 | 0.0 |
| 4 | 728 | 6e-06 | 0.000126 |
| 5 | 728 | 0.0 | 1e-06 |
| 6 | 728 | 0.054117 | 0.127356 |
| 7 | 728 | 0.235029 | 0.406799 |
| 8 | 728 | 0.769578 | 1.095891 |
| 9 | 728 | 1.541976 | 2.717815 |
| 10 | 728 | 2.723838 | 5.240456 |
| 11 | 728 | 4.972391 | 8.444713 |
| 12 | 728 | 6.80509 | 10.178399 |
| 13 | 728 | 7.933315 | 11.016827 |
| 14 | 728 | 8.146955 | 11.173925 |
| 15 | 728 | 6.931422 | 9.756561 |
| 16 | 728 | 4.821546 | 6.860931 |
| 17 | 728 | 2.619902 | 4.049817 |
| 18 | 728 | 1.240647 | 1.818498 |
| 19 | 728 | 0.350073 | 0.581933 |
| 20 | 728 | 0.067979 | 0.153303 |
| 21 | 728 | 0.001181 | 0.009551 |
| 22 | 728 | 1e-06 | 1e-06 |
| 23 | 728 | 1e-06 | 1e-06 |

month:

| Group | Rows | MAE MW | RMSE MW |
| --- | --- | --- | --- |
| 2020-01 | 2976 | 1.154409 | 2.628969 |
| 2020-02 | 2784 | 2.626373 | 6.457418 |
| 2020-03 | 2976 | 1.376272 | 2.897886 |
| 2020-04 | 2880 | 1.43611 | 3.466018 |
| 2020-05 | 2976 | 4.04301 | 8.652363 |
| 2020-06 | 2880 | 1.672719 | 3.338806 |

```json
{
  "definition": "actual minus predicted; positive means underprediction",
  "mean_mw": -0.5398993048574674,
  "median_mw": -4.904700283689161e-07,
  "std_population_mw": 5.052676224939551,
  "largest_absolute_error_mw": 34.463832630376785
}
```

```json
{
  "min_mw": 3.44280830898235e-07,
  "max_mw": 43.55768629679329,
  "negative_predictions": 0
}
```

### Test

zero positive:

| Group | Rows | MAE MW | RMSE MW |
| --- | --- | --- | --- |
| positive | 8563 | 3.573823 | 5.828421 |
| zero | 9094 | 0.030329 | 0.810675 |

power ranges:

| Group | Rows | MAE MW | RMSE MW |
| --- | --- | --- | --- |
| high positive | 2858 | 3.924634 | 4.904275 |
| low positive | 2734 | 2.502789 | 6.063615 |
| medium positive | 2971 | 4.221951 | 6.398281 |
| zero | 9094 | 0.030329 | 0.810675 |

recorded hour:

| Group | Rows | MAE MW | RMSE MW |
| --- | --- | --- | --- |
| 0 | 736 | 4e-06 | 5.6e-05 |
| 1 | 736 | 1e-06 | 1e-06 |
| 2 | 736 | 4e-06 | 9.5e-05 |
| 3 | 736 | 1.2e-05 | 0.00016 |
| 4 | 736 | 2.5e-05 | 0.000347 |
| 5 | 736 | 4e-05 | 0.000574 |
| 6 | 736 | 0.027361 | 0.094771 |
| 7 | 736 | 0.14923 | 0.292283 |
| 8 | 736 | 0.880439 | 1.327177 |
| 9 | 736 | 1.809711 | 2.630695 |
| 10 | 736 | 2.675864 | 4.16884 |
| 11 | 736 | 4.05892 | 5.99507 |
| 12 | 735 | 5.563101 | 7.925388 |
| 13 | 736 | 7.225124 | 9.615224 |
| 14 | 736 | 6.943984 | 9.339373 |
| 15 | 736 | 5.311755 | 7.514511 |
| 16 | 736 | 3.42516 | 5.276101 |
| 17 | 736 | 2.380983 | 3.412654 |
| 18 | 736 | 1.117928 | 1.577904 |
| 19 | 732 | 0.341793 | 0.627617 |
| 20 | 734 | 0.052246 | 0.134916 |
| 21 | 736 | 0.000294 | 0.002966 |
| 22 | 736 | 1e-06 | 1e-06 |
| 23 | 736 | 1e-06 | 1e-06 |

month:

| Group | Rows | MAE MW | RMSE MW |
| --- | --- | --- | --- |
| 2020-07 | 2976 | 1.630852 | 3.445874 |
| 2020-08 | 2970 | 1.706512 | 3.426207 |
| 2020-09 | 2880 | 1.476916 | 2.762211 |
| 2020-10 | 2976 | 2.16809 | 5.503217 |
| 2020-11 | 2880 | 2.149401 | 5.430784 |
| 2020-12 | 2975 | 1.364932 | 3.155357 |

```json
{
  "definition": "actual minus predicted; positive means underprediction",
  "mean_mw": -0.1425795663845635,
  "median_mw": -6.103273725909692e-07,
  "std_population_mw": 4.097877268317921,
  "largest_absolute_error_mw": 32.89756524282722
}
```

```json
{
  "min_mw": 3.504251037721691e-07,
  "max_mw": 40.95919782480561,
  "negative_predictions": 0
}
```

Feature importance:

```json
[
  {
    "feature": "Total solar irradiance (W/m2)",
    "importance": 0.742954807798963
  },
  {
    "feature": "hour_cos",
    "importance": 0.1545737201720827
  },
  {
    "feature": "Global horizontal irradiance (W/m2)",
    "importance": 0.03804929901634071
  },
  {
    "feature": "hour",
    "importance": 0.02336778401174111
  },
  {
    "feature": "hour_sin",
    "importance": 0.0164764436762953
  },
  {
    "feature": "Atmosphere (hpa)",
    "importance": 0.004896630975866429
  },
  {
    "feature": "annual_cos",
    "importance": 0.0030921792591346
  },
  {
    "feature": "annual_sin",
    "importance": 0.003041231300782009
  },
  {
    "feature": "Air temperature  (°C) ",
    "importance": 0.0030137585017024873
  },
  {
    "feature": "day_of_week",
    "importance": 0.0028955120379176393
  },
  {
    "feature": "day_of_year",
    "importance": 0.002875788228296684
  },
  {
    "feature": "Direct normal irradiance (W/m2)",
    "importance": 0.00224567490876858
  },
  {
    "feature": "month",
    "importance": 0.001726754114339345
  },
  {
    "feature": "quarter",
    "importance": 0.0007904159977693423
  }
]
```

Native impurity importance is model-specific and affected by correlated features; it is not causal evidence. Histogram boosting has no native importance; no permutation computation is added.

## 12. Important Limitations

- Single site, two years, observed contemporaneous inputs; no future forecast input or horizon
- Unresolved observation timezone, total irradiance plane, AC/DC and interval-averaging semantics
- Filename nominal capacity is not verified; no capacity normalization or clipping
- Humidity remains excluded; complete-case omission can bias coverage; gaps remain
- Native forest importance is model-specific and affected by correlated predictors, not causal evidence
- Diagnostic test analysis must not drive additional tuning against this same test period

Single chronological comparison; no confidence intervals or statistical significance claim. Previously observed test results limit independent confirmation. Future adaptations need a fresh untouched period. Predictions are not clipped; small negative boosting estimates may occur.

The model performs weather-to-solar-power estimation using observed contemporaneous weather and irradiance measurements. It is NOT true future solar forecasting.

## 13. Final Model Recommendation

**extra_trees**, under the predeclared validation rule. No operational readiness claim.

Reproduce/verify: `python -m ml.training.train_solar_advanced`. Models and JSON artifacts remain Git-ignored. No prediction CSV, new dependency, API integration or future milestone component was added.
