# GridCast AI Advanced Wind Power Model Report

## 1. Prediction Task

**Weather-to-Wind-Power Estimation — Not True Future Forecasting.** Observed weather plus calendar at T estimates Power (MW) at T. No forecast-weather service, horizon, lagged target or multi-step prediction is implemented.

## 2. Baseline Performance

```json
{
  "model": "random_forest",
  "metrics": {
    "train": {
      "mae_mw": 3.1954999435431812,
      "rmse_mw": 5.010607761354556,
      "r2": 0.9534277067727449,
      "mae_capacity_percent": 3.227777720750688,
      "rmse_capacity_percent": 5.0612199609641975
    },
    "validation": {
      "mae_mw": 6.035483853567796,
      "rmse_mw": 10.233655838438642,
      "r2": 0.8209626366047573,
      "mae_capacity_percent": 6.096448336937168,
      "rmse_capacity_percent": 10.337026099432972
    },
    "test": {
      "mae_mw": 6.717430393716717,
      "rmse_mw": 12.06352262789784,
      "r2": 0.7802940942741506,
      "mae_capacity_percent": 6.785283225976482,
      "rmse_capacity_percent": 12.185376391816
    }
  }
}
```

The existing random forest wins Milestone 3 validation but has training MAE 3.1955 versus validation 6.0355 MW. Hub speed dominates native importance (76.45%), followed by 50 m speed (12.99%). This motivates shrinkage and smaller boosting trees rather than expanding the random forest blindly. Baseline artifacts were read and hashed; no baseline retraining occurred.

## 3. Advanced Model Candidates

HistGradientBoostingRegressor provides efficient binned nonlinear interactions with L2 regularization. GradientBoostingRegressor supplies conventional shallow-tree boosting without histogram binning. ExtraTrees is omitted because the existing forest already supplies a bagged-tree comparator. No additional ML framework is used.

## 4. Feature Experiments

```json
{
  "A": [
    "Wind speed at height of 10 meters (m/s)",
    "Wind speed at height of 30 meters (m/s)",
    "Wind speed at height of 50 meters (m/s)",
    "Wind speed - at the height of wheel hub(m/s)",
    "Wind direction at height of 10 meters (˚)",
    "Wind direction at height of 30 meters (˚)",
    "Wind direction at height of 50 meters (˚)",
    "Air temperature  (°C) ",
    "Atmosphere (hpa)",
    "Relative humidity (%)",
    "hour",
    "day_of_week",
    "month",
    "day_of_year",
    "quarter",
    "hour_sin",
    "hour_cos",
    "day_of_year_sin",
    "day_of_year_cos"
  ],
  "B": [
    "Wind speed at height of 10 meters (m/s)",
    "Wind speed at height of 30 meters (m/s)",
    "Wind speed at height of 50 meters (m/s)",
    "Wind speed - at the height of wheel hub(m/s)",
    "Wind direction at height of 10 meters (˚)",
    "Wind direction at height of 30 meters (˚)",
    "Wind direction at height of 50 meters (˚)",
    "Air temperature  (°C) ",
    "Atmosphere (hpa)",
    "Relative humidity (%)",
    "hour",
    "day_of_week",
    "month",
    "day_of_year",
    "quarter",
    "hour_sin",
    "hour_cos",
    "day_of_year_sin",
    "day_of_year_cos",
    "wind_direction_10m_sin",
    "wind_direction_10m_cos",
    "wind_direction_30m_sin",
    "wind_direction_30m_cos",
    "wind_direction_50m_sin",
    "wind_direction_50m_cos"
  ]
}
```

A has 10 original weather plus 9 calendar features (19 total). B adds the six engineered direction encodings (25 total). Both retain original measured directions and separate wind heights. All names come from the unchanged Milestone 2 manifest. No hidden feature search occurs.

```json
{
  "Wind speed at height of 10 meters (m/s)": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Measured weather at T supports estimating power at T; distinct height measurements remain separate.",
    "future_use": "CONDITIONAL FOR FUTURE FORECASTING",
    "future_condition": "Replace observed weather at the future target time with as-issued forecast weather, defining origin, horizon and availability."
  },
  "Wind speed at height of 30 meters (m/s)": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Measured weather at T supports estimating power at T; distinct height measurements remain separate.",
    "future_use": "CONDITIONAL FOR FUTURE FORECASTING",
    "future_condition": "Replace observed weather at the future target time with as-issued forecast weather, defining origin, horizon and availability."
  },
  "Wind speed at height of 50 meters (m/s)": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Measured weather at T supports estimating power at T; distinct height measurements remain separate.",
    "future_use": "CONDITIONAL FOR FUTURE FORECASTING",
    "future_condition": "Replace observed weather at the future target time with as-issued forecast weather, defining origin, horizon and availability."
  },
  "Wind speed - at the height of wheel hub(m/s)": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Measured weather at T supports estimating power at T; distinct height measurements remain separate.",
    "future_use": "CONDITIONAL FOR FUTURE FORECASTING",
    "future_condition": "Replace observed weather at the future target time with as-issued forecast weather, defining origin, horizon and availability."
  },
  "Wind direction at height of 10 meters (˚)": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Measured weather at T supports estimating power at T; distinct height measurements remain separate.",
    "future_use": "CONDITIONAL FOR FUTURE FORECASTING",
    "future_condition": "Replace observed weather at the future target time with as-issued forecast weather, defining origin, horizon and availability."
  },
  "Wind direction at height of 30 meters (˚)": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Measured weather at T supports estimating power at T; distinct height measurements remain separate.",
    "future_use": "CONDITIONAL FOR FUTURE FORECASTING",
    "future_condition": "Replace observed weather at the future target time with as-issued forecast weather, defining origin, horizon and availability."
  },
  "Wind direction at height of 50 meters (˚)": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Measured weather at T supports estimating power at T; distinct height measurements remain separate.",
    "future_use": "CONDITIONAL FOR FUTURE FORECASTING",
    "future_condition": "Replace observed weather at the future target time with as-issued forecast weather, defining origin, horizon and availability."
  },
  "Air temperature  (°C) ": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Measured weather at T supports estimating power at T; distinct height measurements remain separate.",
    "future_use": "CONDITIONAL FOR FUTURE FORECASTING",
    "future_condition": "Replace observed weather at the future target time with as-issued forecast weather, defining origin, horizon and availability."
  },
  "Atmosphere (hpa)": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Measured weather at T supports estimating power at T; distinct height measurements remain separate.",
    "future_use": "CONDITIONAL FOR FUTURE FORECASTING",
    "future_condition": "Replace observed weather at the future target time with as-issued forecast weather, defining origin, horizon and availability."
  },
  "Relative humidity (%)": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Measured weather at T supports estimating power at T; distinct height measurements remain separate.",
    "future_use": "CONDITIONAL FOR FUTURE FORECASTING",
    "future_condition": "Replace observed weather at the future target time with as-issued forecast weather, defining origin, horizon and availability."
  },
  "hour": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Deterministic calendar or cyclic season/time-of-day information; no epoch or raw timestamp predictor.",
    "future_use": "SAFE calendar availability",
    "future_condition": "Maintain known calendar/timezone convention"
  },
  "day_of_week": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Deterministic calendar or cyclic season/time-of-day information; no epoch or raw timestamp predictor.",
    "future_use": "SAFE calendar availability",
    "future_condition": "Maintain known calendar/timezone convention"
  },
  "month": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Deterministic calendar or cyclic season/time-of-day information; no epoch or raw timestamp predictor.",
    "future_use": "SAFE calendar availability",
    "future_condition": "Maintain known calendar/timezone convention"
  },
  "day_of_year": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Deterministic calendar or cyclic season/time-of-day information; no epoch or raw timestamp predictor.",
    "future_use": "SAFE calendar availability",
    "future_condition": "Maintain known calendar/timezone convention"
  },
  "quarter": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Deterministic calendar or cyclic season/time-of-day information; no epoch or raw timestamp predictor.",
    "future_use": "SAFE calendar availability",
    "future_condition": "Maintain known calendar/timezone convention"
  },
  "hour_sin": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Deterministic calendar or cyclic season/time-of-day information; no epoch or raw timestamp predictor.",
    "future_use": "SAFE calendar availability",
    "future_condition": "Maintain known calendar/timezone convention"
  },
  "hour_cos": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Deterministic calendar or cyclic season/time-of-day information; no epoch or raw timestamp predictor.",
    "future_use": "SAFE calendar availability",
    "future_condition": "Maintain known calendar/timezone convention"
  },
  "day_of_year_sin": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Deterministic calendar or cyclic season/time-of-day information; no epoch or raw timestamp predictor.",
    "future_use": "SAFE calendar availability",
    "future_condition": "Maintain known calendar/timezone convention"
  },
  "day_of_year_cos": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Deterministic calendar or cyclic season/time-of-day information; no epoch or raw timestamp predictor.",
    "future_use": "SAFE calendar availability",
    "future_condition": "Maintain known calendar/timezone convention"
  },
  "wind_direction_10m_sin": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Circular representation of verified direction at T; deterministic and target-independent.",
    "future_use": "CONDITIONAL FOR FUTURE FORECASTING",
    "future_condition": "Replace observed weather at the future target time with as-issued forecast weather, defining origin, horizon and availability."
  },
  "wind_direction_10m_cos": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Circular representation of verified direction at T; deterministic and target-independent.",
    "future_use": "CONDITIONAL FOR FUTURE FORECASTING",
    "future_condition": "Replace observed weather at the future target time with as-issued forecast weather, defining origin, horizon and availability."
  },
  "wind_direction_30m_sin": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Circular representation of verified direction at T; deterministic and target-independent.",
    "future_use": "CONDITIONAL FOR FUTURE FORECASTING",
    "future_condition": "Replace observed weather at the future target time with as-issued forecast weather, defining origin, horizon and availability."
  },
  "wind_direction_30m_cos": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Circular representation of verified direction at T; deterministic and target-independent.",
    "future_use": "CONDITIONAL FOR FUTURE FORECASTING",
    "future_condition": "Replace observed weather at the future target time with as-issued forecast weather, defining origin, horizon and availability."
  },
  "wind_direction_50m_sin": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Circular representation of verified direction at T; deterministic and target-independent.",
    "future_use": "CONDITIONAL FOR FUTURE FORECASTING",
    "future_condition": "Replace observed weather at the future target time with as-issued forecast weather, defining origin, horizon and availability."
  },
  "wind_direction_50m_cos": {
    "estimation": "SAFE FOR SAME-TIMESTAMP ESTIMATION",
    "inclusion_reason": "Circular representation of verified direction at T; deterministic and target-independent.",
    "future_use": "CONDITIONAL FOR FUTURE FORECASTING",
    "future_condition": "Replace observed weather at the future target time with as-issued forecast weather, defining origin, horizon and availability."
  },
  "Time(year-month-day h:m:s)": {
    "estimation": "EXCLUDE",
    "reason": "Index/split key only; avoids raw timestamp memorization"
  },
  "Power (MW)": {
    "estimation": "EXCLUDE",
    "reason": "Response only; never a predictor"
  },
  "Wind speed - at the height of wheel hub (˚)": {
    "estimation": "EXCLUDE",
    "reason": "EXCLUDED PENDING SEMANTIC VERIFICATION"
  }
}
```

All included predictors are SAFE FOR SAME-TIMESTAMP ESTIMATION. Observed weather and direction encodings are CONDITIONAL FOR FUTURE FORECASTING: replace them with as-issued weather forecasts and define forecast origin/horizon. Target and timestamp are EXCLUDE from predictors; timestamp remains a split key. The ambiguous hub degree column remains excluded.

## 5. Chronological Validation Strategy

```json
{
  "train": {
    "start": "2019-01-01 00:00:00",
    "end": "2019-12-31 23:45:00",
    "rows": 34945,
    "percent": 49.895767890799014
  },
  "validation": {
    "start": "2020-01-01 00:00:00",
    "end": "2020-06-30 23:45:00",
    "rows": 17470,
    "percent": 24.944314352618655
  },
  "test": {
    "start": "2020-07-01 00:00:00",
    "end": "2020-12-31 23:45:00",
    "rows": 17621,
    "percent": 25.159917756582328
  }
}
```

Training: 2019; validation: January–June 2020; test: July–December 2020. No shuffle, random CV or internal random validation is used; histogram early stopping is explicitly disabled. All fits use training only. No train+validation refit. Existing gaps after cleaning are preserved.

**Holdout limitation:** this period's baseline scores were already reported in Milestone 3. It is held out from advanced fitting/selection, but is not a never-before-observed benchmark. The experiment plan was fixed before advanced test predictions. Only the selected model was evaluated once on it; all subsequent error summaries reuse that prediction array and never alter selection.

## 6. Parameter Experiments

```json
[
  {
    "name": "hist_150",
    "model": "HistGradientBoostingRegressor",
    "parameters": {
      "max_iter": 150,
      "learning_rate": 0.08,
      "max_leaf_nodes": 15,
      "min_samples_leaf": 30,
      "l2_regularization": 1.0,
      "early_stopping": false,
      "random_state": 42
    }
  },
  {
    "name": "hist_250",
    "model": "HistGradientBoostingRegressor",
    "parameters": {
      "max_iter": 250,
      "learning_rate": 0.05,
      "max_leaf_nodes": 15,
      "min_samples_leaf": 50,
      "l2_regularization": 5.0,
      "early_stopping": false,
      "random_state": 42
    }
  },
  {
    "name": "gradient_120",
    "model": "GradientBoostingRegressor",
    "parameters": {
      "n_estimators": 120,
      "learning_rate": 0.05,
      "max_depth": 3,
      "min_samples_leaf": 20,
      "subsample": 1.0,
      "loss": "squared_error",
      "random_state": 42
    }
  },
  {
    "name": "gradient_180",
    "model": "GradientBoostingRegressor",
    "parameters": {
      "n_estimators": 180,
      "learning_rate": 0.05,
      "max_depth": 3,
      "min_samples_leaf": 40,
      "subsample": 1.0,
      "loss": "squared_error",
      "random_state": 42
    }
  }
]
```

All four configurations are crossed with A/B: eight total, including unsuccessful candidates. One native thread is used throughout; random_state=42. No stochastic subsampling or random validation fraction. No timing fields are used in selection or deterministic metadata.

## 7. Model Comparison

| Experiment | Features | Split | MAE MW | RMSE MW | R² | MAE % | RMSE % |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A_hist_150 | 19 | train | 3.969679 | 6.054819 | 0.931994 | 4.009777 | 6.115979 |
| A_hist_150 | 19 | validation | 6.196258 | 10.388202 | 0.815514 | 6.258846 | 10.493134 |
| A_hist_250 | 19 | train | 3.985878 | 6.122875 | 0.930456 | 4.02614 | 6.184722 |
| A_hist_250 | 19 | validation | 6.163928 | 10.309149 | 0.818311 | 6.22619 | 10.413282 |
| A_gradient_120 | 19 | train | 4.89495 | 7.409849 | 0.898149 | 4.944393 | 7.484696 |
| A_gradient_120 | 19 | validation | 6.22851 | 10.070497 | 0.826626 | 6.291424 | 10.172219 |
| A_gradient_180 | 19 | train | 4.712756 | 7.180705 | 0.904351 | 4.76036 | 7.253237 |
| A_gradient_180 | 19 | validation | 6.225995 | 10.143495 | 0.824103 | 6.288883 | 10.245954 |
| B_hist_150 | 25 | train | 3.968075 | 6.065324 | 0.931758 | 4.008156 | 6.12659 |
| B_hist_150 | 25 | validation | 6.121231 | 10.220096 | 0.821437 | 6.183061 | 10.32333 |
| B_hist_250 | 25 | train | 3.993979 | 6.140339 | 0.930059 | 4.034322 | 6.202363 |
| B_hist_250 | 25 | validation | 6.165265 | 10.304971 | 0.818459 | 6.22754 | 10.409062 |
| B_gradient_120 | 25 | train | 4.822929 | 7.329708 | 0.90034 | 4.871645 | 7.403746 |
| B_gradient_120 | 25 | validation | 6.169931 | 10.038767 | 0.827717 | 6.232254 | 10.140169 |
| B_gradient_180 | 25 | train | 4.646358 | 7.098704 | 0.906523 | 4.693291 | 7.170408 |
| B_gradient_180 | 25 | validation | 6.183715 | 10.134491 | 0.824416 | 6.246177 | 10.23686 |

Feature-pair comparison (positive A−B means engineered directions improved MAE):

| Configuration | A validation MAE | B validation MAE | A−B MAE MW | Tree-leaf budget |
| --- | --- | --- | --- | --- |
| hist_150 | 6.196257790461526 | 6.121230697476388 | 0.07502709298513732 | 2250 |
| hist_250 | 6.163928098384821 | 6.165264756674234 | -0.0013366582894134282 | 3750 |
| gradient_120 | 6.228509569858949 | 6.169931452189032 | 0.05857811766991716 | 960 |
| gradient_180 | 6.225994608819244 | 6.18371525837441 | 0.042279350444833774 | 1440 |

Direction-feature benefit is configuration-dependent. The final feature group is selected on the same predeclared validation criteria; engineered features are not retained simply because they exist.

## 8. Best Model Selection

**Selected advanced experiment: B_hist_150**.

Minimum validation MAE; within 0.01 MW prefer lower tree-leaf budget, then fewer features, lower validation RMSE, higher validation R², lower MAE and stable id. No test input to selection.

The comparison function rejects records containing test metrics. The selected model and experiment ledger are saved before final evaluation. Structural leaf budget proxies complexity; it is not a measurement of inference speed. The final advanced candidate is saved even if it fails to improve on the baseline; signed comparisons below disclose that outcome.

## 9. Held-Out Test Evaluation

```json
{
  "mae_mw": 6.719774166056929,
  "rmse_mw": 11.856344613350991,
  "r2": 0.7877757182402666,
  "mae_capacity_percent": 6.787650672784777,
  "rmse_capacity_percent": 11.976105670051506
}
```

MAE/RMSE are MW; percentages use 99 MW, not MAPE. R² is dimensionless. Predictions are not clipped.

## 10. Baseline vs Advanced Comparison

```json
{
  "mae_mw": {
    "baseline": 6.717430393716717,
    "advanced": 6.719774166056929,
    "absolute_improvement": -0.0023437723402119914,
    "percent_improvement": -0.03489090623706776
  },
  "rmse_mw": {
    "baseline": 12.06352262789784,
    "advanced": 11.856344613350991,
    "absolute_improvement": 0.20717801454684803,
    "percent_improvement": 1.7173923482991003
  },
  "r2": {
    "baseline": 0.7802940942741506,
    "advanced": 0.7877757182402666,
    "change": 0.007481623966115958
  }
}
```

Positive error improvement means reduction; negative means deterioration. These retrospective comparisons do not trigger model reselection or additional tuning.

## 11. Overfitting Analysis

| Experiment | Train MAE | Validation MAE | Gap MW |
| --- | --- | --- | --- |
| A_hist_150 | 3.9696790339429797 | 6.196257790461526 | 2.226578756518546 |
| A_hist_250 | 3.98587839569639 | 6.163928098384821 | 2.1780497026884307 |
| A_gradient_120 | 4.894949537115678 | 6.228509569858949 | 1.3335600327432715 |
| A_gradient_180 | 4.712756258461821 | 6.225994608819244 | 1.5132383503574234 |
| B_hist_150 | 3.9680748638529733 | 6.121230697476388 | 2.153155833623415 |
| B_hist_250 | 3.993978587840264 | 6.165264756674234 | 2.17128616883397 |
| B_gradient_120 | 4.822928615165739 | 6.169931452189032 | 1.3470028370232932 |
| B_gradient_180 | 4.646358171314554 | 6.18371525837441 | 1.5373570870598563 |

```json
{
  "train_validation_mae_gap": 2.153155833623415,
  "validation_test_mae_gap": 0.5985434685805409,
  "interpretation": "Positive gaps suggest overfitting and/or temporal shift; no causal attribution from this holdout."
}
```

Large positive train/validation gaps are consistent with overfitting and/or temporal shift, not proof of one cause. Similar poor errors may indicate underfitting. Compare actual magnitudes against the baseline; no model is declared generally reliable from a single site and two years.

## 12. Residual Analysis

```json
{
  "residual_definition": "actual minus predicted; positive means underestimation",
  "summary": {
    "mean": 0.33709627520638413,
    "median": -0.3201329399251467,
    "std_population": 11.851551530992854,
    "min": -60.33765025973952,
    "max": 46.1318036751497
  },
  "absolute_error_quantiles": {
    "0.0": 6.513605354857566e-05,
    "0.25": 0.8849292481966398,
    "0.5": 2.870020762559637,
    "0.75": 7.92492620197411,
    "0.9": 18.634023898944896,
    "0.95": 27.904452214724422,
    "0.99": 49.96153629526826,
    "1.0": 60.33765025973952
  }
}
```

Population standard deviation uses ddof=0. A 30-bin residual histogram is saved in the error-analysis JSON. The prediction CSV also supplies actual-vs-predicted data, avoiding a duplicate output file.

## 13. Error by Power Range

```json
[
  {
    "group": "0–10%",
    "rows": 7222,
    "mae_mw": 2.4895820198095526,
    "rmse_mw": 6.658359920239318,
    "mean_residual_mw": -1.9823295826765839
  },
  {
    "group": "10–25%",
    "rows": 3502,
    "mae_mw": 7.442717535280331,
    "rmse_mw": 14.49217330516966,
    "mean_residual_mw": -4.799528270382317
  },
  {
    "group": "25–50%",
    "rows": 3471,
    "mae_mw": 7.3397118966636,
    "rmse_mw": 10.699576553443817,
    "mean_residual_mw": -1.076519685721622
  },
  {
    "group": "50–75%",
    "rows": 2187,
    "mae_mw": 9.834016356508034,
    "rmse_mw": 11.807070407755825,
    "mean_residual_mw": 6.1376456947244264
  },
  {
    "group": "75–100%",
    "rows": 1239,
    "mae_mw": 22.099958562930134,
    "rmse_mw": 24.09139359236948,
    "mean_residual_mw": 22.09675093555955
  }
]
```

```json
{
  "lowest_mae": {
    "group": "0–10%",
    "rows": 7222,
    "mae_mw": 2.4895820198095526,
    "rmse_mw": 6.658359920239318,
    "mean_residual_mw": -1.9823295826765839
  },
  "highest_mae": {
    "group": "75–100%",
    "rows": 1239,
    "mae_mw": 22.099958562930134,
    "rmse_mw": 24.09139359236948,
    "mean_residual_mw": 22.09675093555955
  }
}
```

Groups use actual power divided by 99 MW: [0,10), [10,25), [25,50), [50,75), [75,100] percent. Best/worst here mean lowest/highest group MAE, not confidence-adjusted rankings. Counts matter.

## 14. Time-Based Error Analysis

```json
{
  "by_hour": [
    {
      "group": "0",
      "rows": 732,
      "mae_mw": 5.087596128650075,
      "rmse_mw": 8.917820209474032,
      "mean_residual_mw": 1.0968573693007584
    },
    {
      "group": "1",
      "rows": 732,
      "mae_mw": 5.809475429772033,
      "rmse_mw": 10.396709630810594,
      "mean_residual_mw": 0.5455017343408364
    },
    {
      "group": "2",
      "rows": 732,
      "mae_mw": 5.985926484980426,
      "rmse_mw": 10.505351187727861,
      "mean_residual_mw": 0.47952151615764177
    },
    {
      "group": "3",
      "rows": 732,
      "mae_mw": 5.695558463704113,
      "rmse_mw": 10.155105361637307,
      "mean_residual_mw": 0.9305358512275713
    },
    {
      "group": "4",
      "rows": 732,
      "mae_mw": 6.0546838552742726,
      "rmse_mw": 10.57157358154359,
      "mean_residual_mw": 1.2613954163286452
    },
    {
      "group": "5",
      "rows": 732,
      "mae_mw": 6.4558435041247675,
      "rmse_mw": 11.563668730327057,
      "mean_residual_mw": 1.4658085180086384
    },
    {
      "group": "6",
      "rows": 732,
      "mae_mw": 6.518114424469272,
      "rmse_mw": 11.314166793529228,
      "mean_residual_mw": 1.2103755799207507
    },
    {
      "group": "7",
      "rows": 732,
      "mae_mw": 6.01193211980353,
      "rmse_mw": 10.441274681046993,
      "mean_residual_mw": 1.5842093810990105
    },
    {
      "group": "8",
      "rows": 732,
      "mae_mw": 6.107361572433961,
      "rmse_mw": 10.688835826768043,
      "mean_residual_mw": 1.283635166267684
    },
    {
      "group": "9",
      "rows": 733,
      "mae_mw": 5.931474710662583,
      "rmse_mw": 10.379480092823636,
      "mean_residual_mw": 0.7884002790401028
    },
    {
      "group": "10",
      "rows": 736,
      "mae_mw": 5.725399902248467,
      "rmse_mw": 10.6991862582945,
      "mean_residual_mw": -0.24928991295080827
    },
    {
      "group": "11",
      "rows": 736,
      "mae_mw": 6.345736268304187,
      "rmse_mw": 11.93281852541827,
      "mean_residual_mw": -0.9504225561422234
    },
    {
      "group": "12",
      "rows": 736,
      "mae_mw": 7.2375411814607675,
      "rmse_mw": 13.151214879206421,
      "mean_residual_mw": -1.0166393227604278
    },
    {
      "group": "13",
      "rows": 733,
      "mae_mw": 8.471465364248061,
      "rmse_mw": 14.627433967141828,
      "mean_residual_mw": -1.7936285491680408
    },
    {
      "group": "14",
      "rows": 736,
      "mae_mw": 8.499712231525361,
      "rmse_mw": 14.805718179836857,
      "mean_residual_mw": -2.24860606277509
    },
    {
      "group": "15",
      "rows": 736,
      "mae_mw": 9.425097140509047,
      "rmse_mw": 15.433001806170159,
      "mean_residual_mw": -2.225768187094413
    },
    {
      "group": "16",
      "rows": 736,
      "mae_mw": 9.494781647264587,
      "rmse_mw": 15.45373958556307,
      "mean_residual_mw": -2.028333494973843
    },
    {
      "group": "17",
      "rows": 736,
      "mae_mw": 8.601884580966049,
      "rmse_mw": 14.056866328110836,
      "mean_residual_mw": -0.23966191290081704
    },
    {
      "group": "18",
      "rows": 736,
      "mae_mw": 7.5930370382410874,
      "rmse_mw": 12.555129964179214,
      "mean_residual_mw": 1.3171083119877804
    },
    {
      "group": "19",
      "rows": 736,
      "mae_mw": 7.526156951744263,
      "rmse_mw": 12.454338287658704,
      "mean_residual_mw": 2.432039545815644
    },
    {
      "group": "20",
      "rows": 736,
      "mae_mw": 6.647635546427937,
      "rmse_mw": 12.034247395816763,
      "mean_residual_mw": 2.060187162232839
    },
    {
      "group": "21",
      "rows": 736,
      "mae_mw": 5.562573108212589,
      "rmse_mw": 10.029095310120773,
      "mean_residual_mw": 1.2564898150852648
    },
    {
      "group": "22",
      "rows": 736,
      "mae_mw": 5.322174322798071,
      "rmse_mw": 9.573106935657727,
      "mean_residual_mw": 0.08181621601599841
    },
    {
      "group": "23",
      "rows": 735,
      "mae_mw": 5.128490003492748,
      "rmse_mw": 8.91101255100025,
      "mean_residual_mw": 1.0800295112669054
    }
  ],
  "by_month": [
    {
      "group": "2020-07",
      "rows": 2976,
      "mae_mw": 7.332677035027863,
      "rmse_mw": 10.719042119314883,
      "mean_residual_mw": 2.3309172447805384
    },
    {
      "group": "2020-08",
      "rows": 2976,
      "mae_mw": 8.35328003923797,
      "rmse_mw": 13.68612244321335,
      "mean_residual_mw": 1.9668852952300433
    },
    {
      "group": "2020-09",
      "rows": 2880,
      "mae_mw": 6.174265009827968,
      "rmse_mw": 10.39315353073765,
      "mean_residual_mw": 2.623082335471181
    },
    {
      "group": "2020-10",
      "rows": 2976,
      "mae_mw": 8.505399363241514,
      "rmse_mw": 15.516339777415224,
      "mean_residual_mw": -1.7957165979290617
    },
    {
      "group": "2020-11",
      "rows": 2879,
      "mae_mw": 5.682945390455583,
      "rmse_mw": 11.364295649728342,
      "mean_residual_mw": -2.087297000577139
    },
    {
      "group": "2020-12",
      "rows": 2934,
      "mae_mw": 4.1828837132382795,
      "rmse_mw": 7.794805454648079,
      "mean_residual_mw": -1.0400079617308562
    }
  ]
}
```

```json
{
  "hour_extrema": {
    "lowest_mae": {
      "group": "0",
      "rows": 732,
      "mae_mw": 5.087596128650075,
      "rmse_mw": 8.917820209474032,
      "mean_residual_mw": 1.0968573693007584
    },
    "highest_mae": {
      "group": "16",
      "rows": 736,
      "mae_mw": 9.494781647264587,
      "rmse_mw": 15.45373958556307,
      "mean_residual_mw": -2.028333494973843
    }
  },
  "month_extrema": {
    "lowest_mae": {
      "group": "2020-12",
      "rows": 2934,
      "mae_mw": 4.1828837132382795,
      "rmse_mw": 7.794805454648079,
      "mean_residual_mw": -1.0400079617308562
    },
    "highest_mae": {
      "group": "2020-10",
      "rows": 2976,
      "mae_mw": 8.505399363241514,
      "rmse_mw": 15.516339777415224,
      "mean_residual_mw": -1.7957165979290617
    }
  }
}
```

**OBSERVED PATTERN:** the tables identify higher/lower errors only in the evaluated period. **POSSIBLE EXPLANATION:** changes in weather/power mix, operating conditions or temporal shift could contribute; these causes are not established by available metadata. No strong daily pattern is assumed. No seasons inferred: site hemisphere/location metadata absent; test covers only July–December 2020.

## 15. Feature Importance

```json
{
  "dataset": "validation only; all 17,470 rows",
  "scoring": "negative MAE; positive importance means increased MAE",
  "n_repeats": 3,
  "random_state": 42,
  "native_available": false
}
```

| Permutation rank | Feature | Native importance | Validation MAE increase MW | Repeat std MW |
| --- | --- | --- | --- | --- |
| 1 | Wind speed - at the height of wheel hub(m/s) | None | 10.884668859109683 | 0.11890085616131549 |
| 2 | Wind speed at height of 50 meters (m/s) | None | 4.509178625391854 | 0.06286339671892956 |
| 3 | Wind speed at height of 30 meters (m/s) | None | 0.4912152746851242 | 0.006997068600070664 |
| 4 | Wind speed at height of 10 meters (m/s) | None | 0.3407938093275374 | 0.0027141466407758874 |
| 5 | wind_direction_50m_cos | None | 0.22431055034261357 | 0.012862112765139691 |
| 6 | wind_direction_30m_sin | None | 0.2231760127434453 | 0.00782392306386972 |
| 7 | Air temperature  (°C)  | None | 0.21403276106594019 | 0.004856991091689365 |
| 8 | day_of_year | None | 0.21377152518801198 | 0.0059700592796953725 |
| 9 | day_of_year_sin | None | 0.14892537574509923 | 0.011499050187109039 |
| 10 | day_of_year_cos | None | 0.11719123163927551 | 0.02173444511956919 |
| 11 | Relative humidity (%) | None | 0.0963269267901099 | 0.0024682060448258476 |
| 12 | hour_cos | None | 0.07061773468286603 | 0.008172059553500302 |
| 13 | wind_direction_50m_sin | None | 0.06146857619531124 | 0.0010185999973063614 |
| 14 | hour | None | 0.06014233117615516 | 0.003993802059545888 |
| 15 | wind_direction_10m_sin | None | 0.05430030700146974 | 0.0029993242265411927 |
| 16 | hour_sin | None | 0.03259225939728161 | 0.0041370489510076025 |
| 17 | wind_direction_30m_cos | None | 0.029377682404308974 | 0.0016422932805463585 |
| 18 | day_of_week | None | 0.0069664947471785865 | 0.0012095010146515402 |
| 19 | Wind direction at height of 30 meters (˚) | None | 0.0022709301837317377 | 0.00022300857860507397 |
| 20 | month | None | 0.0018814734234749626 | 0.0007023189669196312 |
| 21 | Wind direction at height of 10 meters (˚) | None | 0.0017562463169339775 | 0.0005018537880347869 |
| 22 | quarter | None | 0.0 | 0.0 |
| 23 | Wind direction at height of 50 meters (˚) | None | -0.008796503217302742 | 0.0014123660428916225 |
| 24 | wind_direction_10m_cos | None | -0.01024226403779623 | 0.003069924958051476 |
| 25 | Atmosphere (hpa) | None | -0.010456891072584185 | 0.0005435928216584747 |

Permutation importance uses the full validation split, three repeats, negative MAE scoring, seed 42 and one worker. It is computed after selection and does not feed selection. Native importance is null when unavailable (histogram boosting); all gradient-boosting candidates' native values are also retained in the experiment ledger. Importance is not causation. Correlated heights/encodings can share or mask importance; small negative values can reflect noise.

## 16. Final Model

```json
{
  "model_type": "HistGradientBoostingRegressor",
  "parameters": {
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
  "feature_names": [
    "Wind speed at height of 10 meters (m/s)",
    "Wind speed at height of 30 meters (m/s)",
    "Wind speed at height of 50 meters (m/s)",
    "Wind speed - at the height of wheel hub(m/s)",
    "Wind direction at height of 10 meters (˚)",
    "Wind direction at height of 30 meters (˚)",
    "Wind direction at height of 50 meters (˚)",
    "Air temperature  (°C) ",
    "Atmosphere (hpa)",
    "Relative humidity (%)",
    "hour",
    "day_of_week",
    "month",
    "day_of_year",
    "quarter",
    "hour_sin",
    "hour_cos",
    "day_of_year_sin",
    "day_of_year_cos",
    "wind_direction_10m_sin",
    "wind_direction_10m_cos",
    "wind_direction_30m_sin",
    "wind_direction_30m_cos",
    "wind_direction_50m_sin",
    "wind_direction_50m_cos"
  ],
  "feature_count": 25,
  "target": "Power (MW)",
  "nominal_capacity_mw": 99,
  "dataset": {
    "path": "ml/data/processed/wind_site_1_prepared.csv",
    "sha256": "46e108ca29e4eaeedcee791c6725fb557b99d3fdbfaa61b1f1b34cd3bcf2d803",
    "rows": 70036,
    "columns": 27,
    "features": 25,
    "missing_values": 0,
    "start": "2019-01-01 00:00:00",
    "end": "2020-12-31 23:45:00",
    "duplicate_rows": 0,
    "duplicate_timestamps": 0,
    "interval_counts": {
      "0 days 00:15:00": 70026,
      "0 days 00:30:00": 4,
      "0 days 03:00:00": 1,
      "0 days 01:15:00": 1,
      "0 days 19:45:00": 1,
      "0 days 10:15:00": 1,
      "0 days 01:00:00": 1
    },
    "cadence_note": "Nominal 15 minutes with documented gaps after complete-case selection; no resampling."
  }
}
```

Saved `ml/artifacts/wind_best_model.joblib` with `wind_best_model_metadata.json`. All generated local artifacts are Git-ignored. Raw/prepared data, preprocessing, baseline code and baseline artifacts remain unchanged. Rerunning verifies saved results and reuses them rather than reevaluating the test set.

```powershell
python -m ml.training.train_wind_advanced
```

## 17. Limitations

Single wind farm; site-specific model; observed weather; same-timestamp estimation; not true future forecasting; no weather forecast integration; limited temporal coverage; no demonstrated multi-site generalisation. Source timezone/location and operational metadata are incomplete. Complete-case row omission can bias results. Repeated validation comparison can overfit that period. Test residual analysis is descriptive only; any future adaptation needs a new untouched evaluation period. No confidence intervals or causal claims.

## 18. Recommended Next Steps

Recommendations only: collect additional sites/years, retain a new untouched holdout, investigate documented operating regimes, and define forecast inputs/horizon before future forecasting. No solar, demand, grid, API, UI or Milestone 5 work is implemented.
