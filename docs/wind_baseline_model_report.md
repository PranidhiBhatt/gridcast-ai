# GridCast AI Wind Power Baseline Model Report

## 1. Prediction Task Definition

**Weather-to-Wind-Power Estimation — Not True Future Forecasting.** Input observed weather and calendar variables at timestamp T; estimate wind power in MW at the same T. There is no prediction horizon, lag construction or external weather forecast input in this experiment.

## 2. Dataset

```json
{
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
```

Input is the unchanged Milestone 2 CSV. Shape, exact headers, missingness, ordering and split counts match its report/manifest. Nominal cadence is 15 minutes, with 140 documented omissions causing gaps. No new cleaning, random shuffle, resampling or imputation is performed.

## 3. Target

`Power (MW)`; MW power, nominal capacity 99 MW. Target is never a predictor. Zero power is retained. Estimator outputs are not clipped; all metrics reflect raw predictions, including any physically implausible linear outputs.

## 4. Feature Set

25 predictors loaded from `docs/wind_feature_manifest.json`.

```json
{
  "weather": [
    "Wind speed at height of 10 meters (m/s)",
    "Wind speed at height of 30 meters (m/s)",
    "Wind speed at height of 50 meters (m/s)",
    "Wind speed - at the height of wheel hub(m/s)",
    "Wind direction at height of 10 meters (˚)",
    "Wind direction at height of 30 meters (˚)",
    "Wind direction at height of 50 meters (˚)",
    "Air temperature  (°C) ",
    "Atmosphere (hpa)",
    "Relative humidity (%)"
  ],
  "time": [
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
  "engineered_wind": [
    "wind_direction_10m_sin",
    "wind_direction_10m_cos",
    "wind_direction_30m_sin",
    "wind_direction_30m_cos",
    "wind_direction_50m_sin",
    "wind_direction_50m_cos"
  ]
}
```

| Exact feature | Why included | Same-time classification | Future use |
| --- | --- | --- | --- |
| "Wind speed at height of 10 meters (m/s)" | Measured weather at T supports estimating power at T; distinct height measurements remain separate. | SAFE FOR SAME-TIMESTAMP ESTIMATION | CONDITIONAL FOR FUTURE FORECASTING |
| "Wind speed at height of 30 meters (m/s)" | Measured weather at T supports estimating power at T; distinct height measurements remain separate. | SAFE FOR SAME-TIMESTAMP ESTIMATION | CONDITIONAL FOR FUTURE FORECASTING |
| "Wind speed at height of 50 meters (m/s)" | Measured weather at T supports estimating power at T; distinct height measurements remain separate. | SAFE FOR SAME-TIMESTAMP ESTIMATION | CONDITIONAL FOR FUTURE FORECASTING |
| "Wind speed - at the height of wheel hub(m/s)" | Measured weather at T supports estimating power at T; distinct height measurements remain separate. | SAFE FOR SAME-TIMESTAMP ESTIMATION | CONDITIONAL FOR FUTURE FORECASTING |
| "Wind direction at height of 10 meters (˚)" | Measured weather at T supports estimating power at T; distinct height measurements remain separate. | SAFE FOR SAME-TIMESTAMP ESTIMATION | CONDITIONAL FOR FUTURE FORECASTING |
| "Wind direction at height of 30 meters (˚)" | Measured weather at T supports estimating power at T; distinct height measurements remain separate. | SAFE FOR SAME-TIMESTAMP ESTIMATION | CONDITIONAL FOR FUTURE FORECASTING |
| "Wind direction at height of 50 meters (˚)" | Measured weather at T supports estimating power at T; distinct height measurements remain separate. | SAFE FOR SAME-TIMESTAMP ESTIMATION | CONDITIONAL FOR FUTURE FORECASTING |
| "Air temperature  (°C) " | Measured weather at T supports estimating power at T; distinct height measurements remain separate. | SAFE FOR SAME-TIMESTAMP ESTIMATION | CONDITIONAL FOR FUTURE FORECASTING |
| "Atmosphere (hpa)" | Measured weather at T supports estimating power at T; distinct height measurements remain separate. | SAFE FOR SAME-TIMESTAMP ESTIMATION | CONDITIONAL FOR FUTURE FORECASTING |
| "Relative humidity (%)" | Measured weather at T supports estimating power at T; distinct height measurements remain separate. | SAFE FOR SAME-TIMESTAMP ESTIMATION | CONDITIONAL FOR FUTURE FORECASTING |
| "hour" | Deterministic calendar or cyclic season/time-of-day information; no epoch or raw timestamp predictor. | SAFE FOR SAME-TIMESTAMP ESTIMATION | SAFE calendar availability |
| "day_of_week" | Deterministic calendar or cyclic season/time-of-day information; no epoch or raw timestamp predictor. | SAFE FOR SAME-TIMESTAMP ESTIMATION | SAFE calendar availability |
| "month" | Deterministic calendar or cyclic season/time-of-day information; no epoch or raw timestamp predictor. | SAFE FOR SAME-TIMESTAMP ESTIMATION | SAFE calendar availability |
| "day_of_year" | Deterministic calendar or cyclic season/time-of-day information; no epoch or raw timestamp predictor. | SAFE FOR SAME-TIMESTAMP ESTIMATION | SAFE calendar availability |
| "quarter" | Deterministic calendar or cyclic season/time-of-day information; no epoch or raw timestamp predictor. | SAFE FOR SAME-TIMESTAMP ESTIMATION | SAFE calendar availability |
| "hour_sin" | Deterministic calendar or cyclic season/time-of-day information; no epoch or raw timestamp predictor. | SAFE FOR SAME-TIMESTAMP ESTIMATION | SAFE calendar availability |
| "hour_cos" | Deterministic calendar or cyclic season/time-of-day information; no epoch or raw timestamp predictor. | SAFE FOR SAME-TIMESTAMP ESTIMATION | SAFE calendar availability |
| "day_of_year_sin" | Deterministic calendar or cyclic season/time-of-day information; no epoch or raw timestamp predictor. | SAFE FOR SAME-TIMESTAMP ESTIMATION | SAFE calendar availability |
| "day_of_year_cos" | Deterministic calendar or cyclic season/time-of-day information; no epoch or raw timestamp predictor. | SAFE FOR SAME-TIMESTAMP ESTIMATION | SAFE calendar availability |
| "wind_direction_10m_sin" | Circular representation of verified direction at T; deterministic and target-independent. | SAFE FOR SAME-TIMESTAMP ESTIMATION | CONDITIONAL FOR FUTURE FORECASTING |
| "wind_direction_10m_cos" | Circular representation of verified direction at T; deterministic and target-independent. | SAFE FOR SAME-TIMESTAMP ESTIMATION | CONDITIONAL FOR FUTURE FORECASTING |
| "wind_direction_30m_sin" | Circular representation of verified direction at T; deterministic and target-independent. | SAFE FOR SAME-TIMESTAMP ESTIMATION | CONDITIONAL FOR FUTURE FORECASTING |
| "wind_direction_30m_cos" | Circular representation of verified direction at T; deterministic and target-independent. | SAFE FOR SAME-TIMESTAMP ESTIMATION | CONDITIONAL FOR FUTURE FORECASTING |
| "wind_direction_50m_sin" | Circular representation of verified direction at T; deterministic and target-independent. | SAFE FOR SAME-TIMESTAMP ESTIMATION | CONDITIONAL FOR FUTURE FORECASTING |
| "wind_direction_50m_cos" | Circular representation of verified direction at T; deterministic and target-independent. | SAFE FOR SAME-TIMESTAMP ESTIMATION | CONDITIONAL FOR FUTURE FORECASTING |

Excluded predictors:

```json
{
  "Wind speed - at the height of wheel hub (˚)": "EXCLUDED PENDING SEMANTIC VERIFICATION",
  "Time(year-month-day h:m:s)": "Split/index key only",
  "Power (MW)": "Response only"
}
```

## 5. Feature Availability and Leakage Considerations

Observed weather and its deterministic direction encodings are **SAFE FOR SAME-TIMESTAMP ESTIMATION** when all inputs at T are available. They are **CONDITIONAL FOR FUTURE FORECASTING**: replace them with as-issued forecast weather and define origin/horizon before claiming future prediction. Calendar variables are known in advance but require a consistent timezone convention. The source timezone is unknown.
Raw timestamp and target are excluded. Exact-schema validation rejects extra columns; feature provenance is checked against Milestone 2 roles and reviewed deterministic engineering. Obvious target/future feature names and exact copies of the target are rejected. These checks cannot prove absence of an undisclosed upstream target-derived transformation; the unchanged preprocessing code supplies the reviewed lineage. Linear scaling fits only training rows, inside the saved pipeline. No feature selection or tuning uses test.

```json
{
  "train/validation": {
    "timestamp_overlap": 0,
    "identical_predictor_target_signatures": 0
  },
  "train/test": {
    "timestamp_overlap": 0,
    "identical_predictor_target_signatures": 0
  },
  "validation/test": {
    "timestamp_overlap": 0,
    "identical_predictor_target_signatures": 0
  }
}
```

Exact feature/target signatures excluding timestamps were also checked across partitions; rounded or near-duplicate measurements are not the same as proven duplicated records.

## 6. Chronological Split

| Split | Start | End | Rows | Dataset % |
| --- | --- | --- | --- | --- |
| train | 2019-01-01 00:00:00 | 2019-12-31 23:45:00 | 34945 | 49.89577 |
| validation | 2020-01-01 00:00:00 | 2020-06-30 23:45:00 | 17470 | 24.94431 |
| test | 2020-07-01 00:00:00 | 2020-12-31 23:45:00 | 17621 | 25.15992 |

The existing 2019 / January–June 2020 / July–December 2020 plan is unchanged. All models fit training only; there is no train+validation refit. Test metrics are computed after selection is frozen.

## 7. Models Evaluated

### Mean Baseline

DummyRegressor predicts the training-set mean. This is a constant benchmark, not a useful production model.

### Linear Regression

StandardScaler followed by ordinary least squares with an intercept. Both stages fit training only. Named features are preserved through the scaler. The saved pipeline contains its scaler, so no separate scaler artifact is needed.

### Random Forest

Fixed lightweight configuration selected before results; no hyperparameter search. One worker and a fixed seed aid reproducibility. Correlated original/cyclic predictors are retained for this baseline rather than tuned feature selection.

```json
{
  "mean_baseline": {
    "strategy": "mean"
  },
  "linear_regression": {
    "scaler": "StandardScaler, fit train only, with_mean=True, with_std=True",
    "fit_intercept": true,
    "positive": false
  },
  "random_forest": {
    "n_estimators": 80,
    "max_depth": 12,
    "min_samples_leaf": 5,
    "min_samples_split": 2,
    "max_features": 1.0,
    "bootstrap": true,
    "criterion": "squared_error",
    "random_state": 42,
    "n_jobs": 1
  }
}
```

## 8. Evaluation Metrics

MAE is mean absolute prediction error in MW. RMSE is the square root of mean squared error in MW and weights large errors more heavily. R² compares squared error with the evaluation split's own mean benchmark; 1 is perfect, 0 matches that benchmark, and negative values are possible. Capacity-normalized errors are 100 × error / 99; they are not MAPE.

## 9. Model Results

| Model | Split | MAE MW | RMSE MW | R² | MAE % capacity | RMSE % capacity |
| --- | --- | --- | --- | --- | --- | --- |
| mean_baseline | train | 19.889517 | 23.218096 | 0.0 | 20.090422 | 23.452622 |
| mean_baseline | validation | 20.370847 | 24.186111 | -3.3e-05 | 20.576613 | 24.430415 |
| mean_baseline | test | 21.240027 | 25.793312 | -0.004402 | 21.454572 | 26.05385 |
| linear_regression | train | 8.280135 | 11.516513 | 0.75397 | 8.363772 | 11.632841 |
| linear_regression | validation | 8.713065 | 12.260865 | 0.743005 | 8.801076 | 12.384713 |
| linear_regression | test | 9.45707 | 13.350744 | 0.730906 | 9.552596 | 13.4856 |
| random_forest | train | 3.1955 | 5.010608 | 0.953428 | 3.227778 | 5.06122 |
| random_forest | validation | 6.035484 | 10.233656 | 0.820963 | 6.096448 | 10.337026 |
| random_forest | test | 6.71743 | 12.063523 | 0.780294 | 6.785283 | 12.185376 |

Full-precision metrics are saved locally in `ml/artifacts/wind_baseline_metrics.json`.

## 10. Best Baseline Model

**BEST BASELINE MODEL: random_forest**. Selection criterion: lowest validation MAE; ties use validation RMSE, then model name. The selection function receives validation metrics only. No test data is used for fitting or selection.

## 11. Test Evaluation

```json
{
  "mae_mw": 6.717430393716717,
  "rmse_mw": 12.06352262789784,
  "r2": 0.7802940942741506,
  "mae_capacity_percent": 6.785283225976482,
  "rmse_capacity_percent": 12.185376391816
}
```

All three predeclared candidates have held-out scores in section 9. The selected model was fixed first; these results trigger no tuning, changes to features, refitting or reselection. Prediction CSVs store only the selected model's validation/test outputs to avoid redundant copies of the actual values.

Prediction-range diagnostics (no clipping):

```json
{
  "mean_baseline": {
    "train": {
      "below_zero": 0,
      "above_99_mw": 0,
      "min_mw": 23.036969354385466,
      "max_mw": 23.036969354385466
    },
    "validation": {
      "below_zero": 0,
      "above_99_mw": 0,
      "min_mw": 23.036969354385466,
      "max_mw": 23.036969354385466
    },
    "test": {
      "below_zero": 0,
      "above_99_mw": 0,
      "min_mw": 23.036969354385466,
      "max_mw": 23.036969354385466
    }
  },
  "linear_regression": {
    "train": {
      "below_zero": 3382,
      "above_99_mw": 47,
      "min_mw": -16.57748875457641,
      "max_mw": 129.43976529225847
    },
    "validation": {
      "below_zero": 1937,
      "above_99_mw": 37,
      "min_mw": -15.094720422112662,
      "max_mw": 144.43620662040368
    },
    "test": {
      "below_zero": 1417,
      "above_99_mw": 35,
      "min_mw": -17.286304749895425,
      "max_mw": 116.20781437731412
    }
  },
  "random_forest": {
    "train": {
      "below_zero": 0,
      "above_99_mw": 0,
      "min_mw": 0.1897121726575515,
      "max_mw": 79.70522875351134
    },
    "validation": {
      "below_zero": 0,
      "above_99_mw": 0,
      "min_mw": 0.2914979025620451,
      "max_mw": 70.84098474257516
    },
    "test": {
      "below_zero": 0,
      "above_99_mw": 0,
      "min_mw": 0.2821516747745989,
      "max_mw": 79.40488188194078
    }
  }
}
```

## 12. Overfitting Review

```json
{
  "mean_baseline": {
    "train_mae_mw": 19.889517328507115,
    "validation_mae_mw": 20.3708472917823,
    "test_mae_mw": 21.240026723639364,
    "validation_minus_train_mae_mw": 0.4813299632751864,
    "test_minus_validation_mae_mw": 0.8691794318570629,
    "interpretation": "UNDERFITTING benchmark by construction: constant output ignores all weather; not a production model."
  },
  "linear_regression": {
    "train_mae_mw": 8.280134526038156,
    "validation_mae_mw": 8.71306498282152,
    "test_mae_mw": 9.45707020902695,
    "validation_minus_train_mae_mw": 0.43293045678336384,
    "test_minus_validation_mae_mw": 0.7440052262054309,
    "interpretation": "Train/validation gap does not show strong overfitting under the descriptive 25% MAE-gap rule; absolute errors and held-out behavior still matter."
  },
  "random_forest": {
    "train_mae_mw": 3.1954999435431812,
    "validation_mae_mw": 6.035483853567796,
    "test_mae_mw": 6.717430393716717,
    "validation_minus_train_mae_mw": 2.839983910024615,
    "test_minus_validation_mae_mw": 0.6819465401489211,
    "interpretation": "Possible OVERFITTING and/or temporal distribution shift: validation MAE exceeds training by >25%. This descriptive threshold is not a tuning or model-selection rule."
  }
}
```

A train-to-validation gap can reflect overfitting, temporal distribution shift or both. A single chronological holdout cannot establish causality or multi-site generalisation. Compare absolute errors against the mean benchmark as well as gaps; similar poor scores can indicate underfitting.

## 13. Feature Importance

| Rank | Feature | Importance |
| --- | --- | --- |
| 1 | "Wind speed - at the height of wheel hub(m/s)" | 0.76447849 |
| 2 | "Wind speed at height of 50 meters (m/s)" | 0.12985231 |
| 3 | "day_of_year_cos" | 0.028621 |
| 4 | "day_of_year_sin" | 0.01359503 |
| 5 | "Air temperature  (°C) " | 0.00808745 |
| 6 | "wind_direction_50m_cos" | 0.00634535 |
| 7 | "wind_direction_30m_sin" | 0.00620306 |
| 8 | "Relative humidity (%)" | 0.00567176 |
| 9 | "day_of_year" | 0.00533026 |
| 10 | "Wind speed at height of 30 meters (m/s)" | 0.00465639 |
| 11 | "Wind speed at height of 10 meters (m/s)" | 0.00446242 |
| 12 | "Atmosphere (hpa)" | 0.0032883 |
| 13 | "hour_cos" | 0.00273207 |
| 14 | "wind_direction_30m_cos" | 0.00219292 |
| 15 | "hour_sin" | 0.00199294 |
| 16 | "wind_direction_50m_sin" | 0.00174133 |
| 17 | "wind_direction_10m_cos" | 0.00171846 |
| 18 | "Wind direction at height of 50 meters (˚)" | 0.00167737 |
| 19 | "hour" | 0.00161796 |
| 20 | "day_of_week" | 0.00138801 |
| 21 | "month" | 0.00112256 |
| 22 | "Wind direction at height of 10 meters (˚)" | 0.0010692 |
| 23 | "wind_direction_10m_sin" | 0.00105844 |
| 24 | "Wind direction at height of 30 meters (˚)" | 0.00099991 |
| 25 | "quarter" | 9.701e-05 |

Random forest impurity-based importance reflects model usage, not causation. Correlated heights, raw directions and their encodings can share importance. No test-based permutation or feature tuning is performed. Full values are in `wind_baseline_feature_importance.json`.

## 14. Limitations

Single wind farm; site-specific model; observed weather inputs; not yet true future forecasting; no external weather forecast data; no multi-site generalisation demonstrated. Missingness-based row omission can bias evaluation. Calendar cycles and correlated features may complicate linear interpretation. Unbounded linear output can be physically invalid. Source metadata and timezone remain incomplete. Baselines are fixed and untuned; no confidence intervals or deployment claims are made. Model serialization is intended for trusted local artifacts in this environment.

Reproduce from the repository root:

```powershell
python -m ml.training.train_wind_baseline
```

Experiment versions and input/code hashes are saved in the metrics artifact. No wall-clock timestamp or elapsed-time field contaminates deterministic result comparison. Different library/BLAS/platform versions can produce numerical differences.

## 15. Next Steps

Recommendations only: compare additional models in a later milestone; define forecast origin and horizon; integrate as-issued weather forecasts; evaluate additional sites. Preserve a new untouched holdout if future experiments adapt to these test results. None of these next steps is implemented here.
