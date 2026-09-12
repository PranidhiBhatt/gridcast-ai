# Solar Baseline Model Evaluation

## 1. Objective

Weather-to-Solar-Power Estimation: observed weather/irradiance and calendar at T estimate power at T; not true future forecasting.

## 2. Dataset

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

Unchanged Milestone 5B data, policy `solar-site-1-v1`. 60 rows were omitted during preprocessing; no new row removal, cleaning, shuffle or imputation. Raw/prepared bytes and preprocessing source hashes are checked before and after training.

## 3. Target

`Power (MW)`. Header-labelled power in MW; AC/DC and averaging convention unresolved. Zeros and high values retained. Predictions remain unclipped, including negative linear outputs. Nominal capacity is not used as a verified normalization denominator.

## 4. Features

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

```json
{
  "Total solar irradiance (W/m2)": {
    "source_column": "Total solar irradiance (W/m2)",
    "category": "irradiance",
    "unit_from_header": "W/m2",
    "semantic_confidence": "VERIFIED header units; UNRESOLVED geometry/calibration",
    "included": true,
    "missing_policy": "-99/non-finite to missing; omit only incomplete required rows",
    "availability_at_T": "co-recorded observation at T; delivery latency unverified",
    "estimation_suitability": "conditional contemporaneous empirical predictor; preserve label and uncertainties",
    "future_availability": "NOT VERIFIED; future forecasting requires as-issued/available inputs and an explicit origin/horizon"
  },
  "Direct normal irradiance (W/m2)": {
    "source_column": "Direct normal irradiance (W/m2)",
    "category": "irradiance",
    "unit_from_header": "W/m2",
    "semantic_confidence": "VERIFIED header units; UNRESOLVED geometry/calibration",
    "included": true,
    "missing_policy": "-99/non-finite to missing; omit only incomplete required rows",
    "availability_at_T": "co-recorded observation at T; delivery latency unverified",
    "estimation_suitability": "conditional contemporaneous empirical predictor; preserve label and uncertainties",
    "future_availability": "NOT VERIFIED; future forecasting requires as-issued/available inputs and an explicit origin/horizon"
  },
  "Global horizontal irradiance (W/m2)": {
    "source_column": "Global horizontal irradiance (W/m2)",
    "category": "irradiance",
    "unit_from_header": "W/m2",
    "semantic_confidence": "VERIFIED header units; UNRESOLVED geometry/calibration",
    "included": true,
    "missing_policy": "-99/non-finite to missing; omit only incomplete required rows",
    "availability_at_T": "co-recorded observation at T; delivery latency unverified",
    "estimation_suitability": "conditional contemporaneous empirical predictor; preserve label and uncertainties",
    "future_availability": "NOT VERIFIED; future forecasting requires as-issued/available inputs and an explicit origin/horizon"
  },
  "Air temperature  (°C) ": {
    "source_column": "Air temperature  (°C) ",
    "category": "temperature",
    "unit_from_header": "°C",
    "semantic_confidence": "VERIFIED header; LIKELY sentinel",
    "included": true,
    "missing_policy": "-99/non-finite to missing; omit only incomplete required rows",
    "availability_at_T": "co-recorded observation at T; delivery latency unverified",
    "estimation_suitability": "conditional contemporaneous empirical predictor; preserve label and uncertainties",
    "future_availability": "NOT VERIFIED; future forecasting requires as-issued/available inputs and an explicit origin/horizon"
  },
  "Atmosphere (hpa)": {
    "source_column": "Atmosphere (hpa)",
    "category": "pressure",
    "unit_from_header": "hpa",
    "semantic_confidence": "LIKELY",
    "included": true,
    "missing_policy": "-99/non-finite to missing; omit only incomplete required rows",
    "availability_at_T": "co-recorded observation at T; delivery latency unverified",
    "estimation_suitability": "conditional contemporaneous empirical predictor; preserve label and uncertainties",
    "future_availability": "NOT VERIFIED; future forecasting requires as-issued/available inputs and an explicit origin/horizon"
  },
  "Relative humidity (%)": {
    "source_column": "Relative humidity (%)",
    "category": "humidity",
    "unit_from_header": "%",
    "semantic_confidence": "UNRESOLVED",
    "included": false,
    "missing_policy": "excluded column; never determines omission",
    "availability_at_T": "co-recorded observation at T; delivery latency unverified",
    "estimation_suitability": "excluded pending semantic verification",
    "future_availability": "NOT VERIFIED; future forecasting requires as-issued/available inputs and an explicit origin/horizon"
  },
  "hour": {
    "source_column": "Time(year-month-day h:m:s)",
    "category": "calendar",
    "unit_from_header": null,
    "semantic_confidence": "VERIFIED recorded-calendar arithmetic; timezone UNRESOLVED",
    "included": true,
    "missing_policy": "invalid timestamp fails before feature generation",
    "availability_at_T": "known from supplied timestamp T",
    "estimation_suitability": "approved",
    "future_availability": "calendar known if target timestamp and source clock convention are defined"
  },
  "day_of_week": {
    "source_column": "Time(year-month-day h:m:s)",
    "category": "calendar",
    "unit_from_header": null,
    "semantic_confidence": "VERIFIED recorded-calendar arithmetic; timezone UNRESOLVED",
    "included": true,
    "missing_policy": "invalid timestamp fails before feature generation",
    "availability_at_T": "known from supplied timestamp T",
    "estimation_suitability": "approved",
    "future_availability": "calendar known if target timestamp and source clock convention are defined"
  },
  "month": {
    "source_column": "Time(year-month-day h:m:s)",
    "category": "calendar",
    "unit_from_header": null,
    "semantic_confidence": "VERIFIED recorded-calendar arithmetic; timezone UNRESOLVED",
    "included": true,
    "missing_policy": "invalid timestamp fails before feature generation",
    "availability_at_T": "known from supplied timestamp T",
    "estimation_suitability": "approved",
    "future_availability": "calendar known if target timestamp and source clock convention are defined"
  },
  "day_of_year": {
    "source_column": "Time(year-month-day h:m:s)",
    "category": "calendar",
    "unit_from_header": null,
    "semantic_confidence": "VERIFIED recorded-calendar arithmetic; timezone UNRESOLVED",
    "included": true,
    "missing_policy": "invalid timestamp fails before feature generation",
    "availability_at_T": "known from supplied timestamp T",
    "estimation_suitability": "approved",
    "future_availability": "calendar known if target timestamp and source clock convention are defined"
  },
  "quarter": {
    "source_column": "Time(year-month-day h:m:s)",
    "category": "calendar",
    "unit_from_header": null,
    "semantic_confidence": "VERIFIED recorded-calendar arithmetic; timezone UNRESOLVED",
    "included": true,
    "missing_policy": "invalid timestamp fails before feature generation",
    "availability_at_T": "known from supplied timestamp T",
    "estimation_suitability": "approved",
    "future_availability": "calendar known if target timestamp and source clock convention are defined"
  },
  "hour_sin": {
    "source_column": "Time(year-month-day h:m:s)",
    "category": "calendar",
    "unit_from_header": null,
    "semantic_confidence": "VERIFIED recorded-calendar arithmetic; timezone UNRESOLVED",
    "included": true,
    "missing_policy": "invalid timestamp fails before feature generation",
    "availability_at_T": "known from supplied timestamp T",
    "estimation_suitability": "approved",
    "future_availability": "calendar known if target timestamp and source clock convention are defined"
  },
  "hour_cos": {
    "source_column": "Time(year-month-day h:m:s)",
    "category": "calendar",
    "unit_from_header": null,
    "semantic_confidence": "VERIFIED recorded-calendar arithmetic; timezone UNRESOLVED",
    "included": true,
    "missing_policy": "invalid timestamp fails before feature generation",
    "availability_at_T": "known from supplied timestamp T",
    "estimation_suitability": "approved",
    "future_availability": "calendar known if target timestamp and source clock convention are defined"
  },
  "annual_sin": {
    "source_column": "Time(year-month-day h:m:s)",
    "category": "calendar",
    "unit_from_header": null,
    "semantic_confidence": "VERIFIED recorded-calendar arithmetic; timezone UNRESOLVED",
    "included": true,
    "missing_policy": "invalid timestamp fails before feature generation",
    "availability_at_T": "known from supplied timestamp T",
    "estimation_suitability": "approved",
    "future_availability": "calendar known if target timestamp and source clock convention are defined"
  },
  "annual_cos": {
    "source_column": "Time(year-month-day h:m:s)",
    "category": "calendar",
    "unit_from_header": null,
    "semantic_confidence": "VERIFIED recorded-calendar arithmetic; timezone UNRESOLVED",
    "included": true,
    "missing_policy": "invalid timestamp fails before feature generation",
    "availability_at_T": "known from supplied timestamp T",
    "estimation_suitability": "approved",
    "future_availability": "calendar known if target timestamp and source clock convention are defined"
  }
}
```

Feature order is loaded from the manifest and used identically for fitting and prediction. Target/raw timestamp/humidity are excluded. No target-derived or future-observation features. Hash and lineage checks support reproducibility but cannot certify undocumented upstream sensor provenance.

## 5. Chronological Split

```json
{
  "train": {
    "boundary_start_inclusive": "2019-01-01",
    "boundary_end_exclusive": "2020-01-01",
    "rows": 34987,
    "percent": 49.898739232129614,
    "start": "2019-01-01 00:00:00",
    "end": "2019-12-31 23:45:00"
  },
  "validation": {
    "boundary_start_inclusive": "2020-01-01",
    "boundary_end_exclusive": "2020-07-01",
    "rows": 17472,
    "percent": 24.918706144104057,
    "start": "2020-01-01 00:00:00",
    "end": "2020-06-30 23:45:00"
  },
  "test": {
    "boundary_start_inclusive": "2020-07-01",
    "boundary_end_exclusive": "2021-01-01",
    "rows": 17657,
    "percent": 25.18255462376633,
    "start": "2020-07-01 00:00:00",
    "end": "2020-12-31 23:45:00"
  }
}
```

Manifest half-open boundaries, counts and actual date ranges are verified. Each unique timestamp is assigned once; no overlap or train+validation refit. Equal solar measurement values at different times are not automatically duplicate observations.

## 6. Models Evaluated

DummyRegressor predicts the training-only mean. LinearRegression uses a training-fitted StandardScaler pipeline as an interpretable additive baseline; it cannot represent all nonlinear behavior. RandomForestRegressor uses 100 trees, depth 12 and minimum leaf size 5 to bound baseline cost and leaf variance. Settings were fixed before fitting, not searched.

## 7. Model Parameters

```json
{
  "dummy": {
    "constant": null,
    "quantile": null,
    "strategy": "mean"
  },
  "linear_regression": {
    "scaler": {
      "copy": true,
      "with_mean": true,
      "with_std": true
    },
    "regression": {
      "copy_X": true,
      "fit_intercept": true,
      "n_jobs": null,
      "positive": false,
      "tol": 1e-06
    }
  },
  "random_forest": {
    "bootstrap": true,
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

Forest random_state=42; one worker and one native thread. No GridSearchCV, RandomizedSearchCV, random CV or advanced solar model. Saved linear artifact includes its scaler.

## 8. Evaluation Metrics

MAE is sklearn mean absolute error (MW); RMSE is sqrt(mean squared error) (MW); R² uses sklearn r2_score against the evaluated split's mean. Stored scores retain full precision. Subsets report counts/MAE/RMSE; zero-only R² is intentionally omitted as uninformative. Empty subsets have no metrics; overall errors remain primary.

Training results:

| Model | Rows | MAE MW | RMSE MW | R² |
| --- | --- | --- | --- | --- |
| dummy | 34987 | 11.7706971 | 13.7900283 | 0.0 |
| linear_regression | 34987 | 1.8266364 | 3.7133359 | 0.92749 |
| random_forest | 34987 | 0.7785742 | 1.9539546 | 0.979923 |

## 9. Validation Results

| Model | Rows | MAE MW | RMSE MW | R² |
| --- | --- | --- | --- | --- |
| dummy | 17472 | 11.4670736 | 13.6421061 | -5.54e-05 |
| linear_regression | 17472 | 2.5211429 | 5.5316953 | 0.8355713 |
| random_forest | 17472 | 2.1025504 | 5.2816412 | 0.8501009 |

Train-to-validation MAE gaps (descriptive; could reflect overfitting and/or temporal shift):

```json
{
  "dummy": -0.30362341628329403,
  "linear_regression": 0.6945064849165594,
  "random_forest": 1.3239762371861943
}
```

## 10. Model Selection

**Selected using validation data only: random_forest.**

Validation MAE ascending, validation RMSE ascending, validation R2 descending. Exact ties retain declared model order; no test input.

Overall validation MAE is primary; zero/positive subset diagnostics and test scores do not select the model. No additional close-score heuristics.

## 11. Held-Out Test Evaluation

| Model | Rows | MAE MW | RMSE MW | R² |
| --- | --- | --- | --- | --- |
| dummy | 17657 | 11.7081607 | 13.6125018 | -0.0001171 |
| linear_regression | 17657 | 2.2104981 | 4.4117379 | 0.8949504 |
| random_forest | 17657 | 1.782275 | 4.4688264 | 0.8922141 |

Selection was frozen and logged before any test prediction. All three fixed baselines are scored on test afterward for transparent comparison; none is reselected or tuned. Selected predictions are reused for all diagnostics.

## 12. Zero vs Positive Generation Analysis

```json
{
  "dummy": {
    "validation": {
      "zero": {
        "rows": 8511,
        "mae_mw": 9.736911083945467,
        "rmse_mw": 9.736911083945465
      },
      "positive": {
        "rows": 8961,
        "mae_mw": 13.110351583162917,
        "rmse_mw": 16.51731906349871
      }
    },
    "test": {
      "zero": {
        "rows": 9094,
        "mae_mw": 9.736911083945467,
        "rmse_mw": 9.736911083945465
      },
      "positive": {
        "rows": 8563,
        "mae_mw": 13.801649453932871,
        "rmse_mw": 16.77511604883232
      }
    }
  },
  "linear_regression": {
    "validation": {
      "zero": {
        "rows": 8511,
        "mae_mw": 0.4877093093942636,
        "rmse_mw": 0.607198415455641
      },
      "positive": {
        "rows": 8961,
        "mae_mw": 4.452462230427356,
        "rmse_mw": 7.701460165859866
      }
    },
    "test": {
      "zero": {
        "rows": 9094,
        "mae_mw": 0.5323992865613185,
        "rmse_mw": 0.965553322358809
      },
      "positive": {
        "rows": 8563,
        "mae_mw": 3.992657401153707,
        "rmse_mw": 6.256492932330766
      }
    }
  },
  "random_forest": {
    "validation": {
      "zero": {
        "rows": 8511,
        "mae_mw": 0.0006147573941286963,
        "rmse_mw": 0.009110368486683763
      },
      "positive": {
        "rows": 8961,
        "mae_mw": 4.098931882794927,
        "rmse_mw": 7.37499368731875
      }
    },
    "test": {
      "zero": {
        "rows": 9094,
        "mae_mw": 0.03010065259514174,
        "rmse_mw": 0.8088267486483024
      },
      "positive": {
        "rows": 8563,
        "mae_mw": 3.6431034526955806,
        "rmse_mw": 6.36273804455457
      }
    }
  }
}
```

No zero target rows were discarded to improve performance. Selected-model residual mean is actual minus predicted.

## 13. Power-Range Error Analysis

```json
{
  "source": "positive TRAINING targets only",
  "quantiles": [
    0.3333333333333333,
    0.6666666666666666
  ],
  "cutpoints_mw": [
    10.402465999999995,
    27.570731999999992
  ]
}
```

Zero is its own bin. Positive-training-target tertiles define low/medium/high; positive bins are open-left and closed-right with an unbounded upper bin. Held-out target distribution and filename capacity did not set boundaries.

```json
{
  "validation": [
    {
      "group": "high positive",
      "rows": 2717,
      "mae_mw": 4.118393490459331,
      "rmse_mw": 5.458968335153466,
      "mean_residual_mw": 3.366650657579061
    },
    {
      "group": "low positive",
      "rows": 3234,
      "mae_mw": 3.5987394378598623,
      "rmse_mw": 8.614970046232196,
      "mean_residual_mw": -3.14534259894661
    },
    {
      "group": "medium positive",
      "rows": 3010,
      "mae_mw": 4.618780779438056,
      "rmse_mw": 7.435346459913939,
      "mean_residual_mw": -2.953850237903912
    },
    {
      "group": "zero",
      "rows": 8511,
      "mae_mw": 0.0006147573941286963,
      "rmse_mw": 0.009110368486683763,
      "mean_residual_mw": -0.0006147573941286963
    }
  ],
  "test": [
    {
      "group": "high positive",
      "rows": 2858,
      "mae_mw": 4.062180409961175,
      "rmse_mw": 6.48751051090371,
      "mean_residual_mw": 3.3247450705369923
    },
    {
      "group": "low positive",
      "rows": 2734,
      "mae_mw": 2.4225551983529012,
      "rmse_mw": 5.898004989295941,
      "mean_residual_mw": -1.7787655666008162
    },
    {
      "group": "medium positive",
      "rows": 2971,
      "mae_mw": 4.363149559564587,
      "rmse_mw": 6.647217444141826,
      "mean_residual_mw": -2.4221918806398626
    },
    {
      "group": "zero",
      "rows": 9094,
      "mae_mw": 0.03010065259514174,
      "rmse_mw": 0.8088267486483024,
      "mean_residual_mw": -0.03010065259514174
    }
  ]
}
```

## 14. Time-Based Error Analysis

Recorded timestamp hour is not verified local solar time. Monthly groups use year-month; no astronomical interpretation or seasonal attribution.

```json
{
  "validation": {
    "recorded_hour": [
      {
        "group": "0",
        "rows": 728,
        "mae_mw": 2.9725277957526915e-08,
        "rmse_mw": 2.9725277957526915e-08,
        "mean_residual_mw": -2.9725277957526915e-08
      },
      {
        "group": "1",
        "rows": 728,
        "mae_mw": 2.9725277957526915e-08,
        "rmse_mw": 2.9725277957526915e-08,
        "mean_residual_mw": -2.9725277957526915e-08
      },
      {
        "group": "2",
        "rows": 728,
        "mae_mw": 2.9725277957526915e-08,
        "rmse_mw": 2.9725277957526915e-08,
        "mean_residual_mw": -2.9725277957526915e-08
      },
      {
        "group": "3",
        "rows": 728,
        "mae_mw": 2.9725277957526915e-08,
        "rmse_mw": 2.9725277957526915e-08,
        "mean_residual_mw": -2.9725277957526915e-08
      },
      {
        "group": "4",
        "rows": 728,
        "mae_mw": 4.440713402211634e-06,
        "rmse_mw": 9.204017354648073e-05,
        "mean_residual_mw": -4.440713402211634e-06
      },
      {
        "group": "5",
        "rows": 728,
        "mae_mw": 2.9725277957526915e-08,
        "rmse_mw": 2.9725277957526915e-08,
        "mean_residual_mw": -2.9725277957526915e-08
      },
      {
        "group": "6",
        "rows": 728,
        "mae_mw": 0.051581560564378744,
        "rmse_mw": 0.12230015935365499,
        "mean_residual_mw": -0.051245464752465844
      },
      {
        "group": "7",
        "rows": 728,
        "mae_mw": 0.2259139503713558,
        "rmse_mw": 0.4036129511720964,
        "mean_residual_mw": -0.19949243719596432
      },
      {
        "group": "8",
        "rows": 728,
        "mae_mw": 0.8356014823464043,
        "rmse_mw": 1.2019676298054516,
        "mean_residual_mw": -0.7510143121762325
      },
      {
        "group": "9",
        "rows": 728,
        "mae_mw": 1.5904319059586955,
        "rmse_mw": 2.7952715368467658,
        "mean_residual_mw": -1.3554413664772962
      },
      {
        "group": "10",
        "rows": 728,
        "mae_mw": 2.8264772826925384,
        "rmse_mw": 5.380663486581173,
        "mean_residual_mw": -1.6959436494642313
      },
      {
        "group": "11",
        "rows": 728,
        "mae_mw": 5.207304272434045,
        "rmse_mw": 8.640367434477586,
        "mean_residual_mw": -2.4215009489242765
      },
      {
        "group": "12",
        "rows": 728,
        "mae_mw": 7.0746824124222885,
        "rmse_mw": 10.564170783338152,
        "mean_residual_mw": -2.149358296111316
      },
      {
        "group": "13",
        "rows": 728,
        "mae_mw": 8.08757008923407,
        "rmse_mw": 11.408931757002179,
        "mean_residual_mw": -1.54686871596615
      },
      {
        "group": "14",
        "rows": 728,
        "mae_mw": 8.263563752504277,
        "rmse_mw": 11.683830099003346,
        "mean_residual_mw": -1.9269136191343403
      },
      {
        "group": "15",
        "rows": 728,
        "mae_mw": 7.124283439081707,
        "rmse_mw": 10.336814206023677,
        "mean_residual_mw": -2.0793383450477814
      },
      {
        "group": "16",
        "rows": 728,
        "mae_mw": 4.893156003956803,
        "rmse_mw": 7.1393348579695255,
        "mean_residual_mw": -0.7608598065193233
      },
      {
        "group": "17",
        "rows": 728,
        "mae_mw": 2.629451555917308,
        "rmse_mw": 4.093614650734733,
        "mean_residual_mw": 0.23509853257332292
      },
      {
        "group": "18",
        "rows": 728,
        "mae_mw": 1.2305492168816028,
        "rmse_mw": 1.7950953949119042,
        "mean_residual_mw": 0.764568497202357
      },
      {
        "group": "19",
        "rows": 728,
        "mae_mw": 0.34991481451209094,
        "rmse_mw": 0.5946709255502809,
        "mean_residual_mw": 0.2525599782309195
      },
      {
        "group": "20",
        "rows": 728,
        "mae_mw": 0.06947848933466522,
        "rmse_mw": 0.15188242567794538,
        "mean_residual_mw": 0.05653734418485635
      },
      {
        "group": "21",
        "rows": 728,
        "mae_mw": 0.0012450157265108204,
        "rmse_mw": 0.01002024256550062,
        "mean_residual_mw": 0.0012371146550361474
      },
      {
        "group": "22",
        "rows": 728,
        "mae_mw": 2.9725277957526915e-08,
        "rmse_mw": 2.9725277957526915e-08,
        "mean_residual_mw": -2.9725277957526915e-08
      },
      {
        "group": "23",
        "rows": 728,
        "mae_mw": 2.9725277957526915e-08,
        "rmse_mw": 2.9725277957526915e-08,
        "mean_residual_mw": -2.9725277957526915e-08
      }
    ],
    "month": [
      {
        "group": "2020-01",
        "rows": 2976,
        "mae_mw": 1.1602782546396244,
        "rmse_mw": 2.7794234563541327,
        "mean_residual_mw": 0.5836645925682002
      },
      {
        "group": "2020-02",
        "rows": 2784,
        "mae_mw": 2.803241345384503,
        "rmse_mw": 6.947317169239206,
        "mean_residual_mw": -1.0027429060083843
      },
      {
        "group": "2020-03",
        "rows": 2976,
        "mae_mw": 1.3113928834663828,
        "rmse_mw": 2.880183929614628,
        "mean_residual_mw": 0.04896973518000244
      },
      {
        "group": "2020-04",
        "rows": 2880,
        "mae_mw": 1.6444264450016313,
        "rmse_mw": 3.9805293698636754,
        "mean_residual_mw": -0.043140327337247854
      },
      {
        "group": "2020-05",
        "rows": 2976,
        "mae_mw": 4.037776298374447,
        "rmse_mw": 8.723421061032372,
        "mean_residual_mw": -3.187469152951283
      },
      {
        "group": "2020-06",
        "rows": 2880,
        "mae_mw": 1.6748170707589556,
        "rmse_mw": 3.3976132882282437,
        "mean_residual_mw": 0.20760391952769086
      }
    ]
  },
  "test": {
    "recorded_hour": [
      {
        "group": "0",
        "rows": 736,
        "mae_mw": 2.787715051413471e-06,
        "rmse_mw": 4.721649676684461e-05,
        "mean_residual_mw": -2.787715051413471e-06
      },
      {
        "group": "1",
        "rows": 736,
        "mae_mw": 2.9725277957526918e-08,
        "rmse_mw": 2.9725277957526918e-08,
        "mean_residual_mw": -2.9725277957526918e-08
      },
      {
        "group": "2",
        "rows": 736,
        "mae_mw": 6.976298552336238e-07,
        "rmse_mw": 1.812091699692622e-05,
        "mean_residual_mw": -6.976298552336238e-07
      },
      {
        "group": "3",
        "rows": 736,
        "mae_mw": 2.595636418576118e-06,
        "rmse_mw": 3.285072659076766e-05,
        "mean_residual_mw": -2.595636418576118e-06
      },
      {
        "group": "4",
        "rows": 736,
        "mae_mw": 1.062507870327065e-05,
        "rmse_mw": 0.0001617812325347742,
        "mean_residual_mw": -1.062507870327065e-05
      },
      {
        "group": "5",
        "rows": 736,
        "mae_mw": 2.683118390477995e-05,
        "rmse_mw": 0.00041499117954365503,
        "mean_residual_mw": -2.683118390477995e-05
      },
      {
        "group": "6",
        "rows": 736,
        "mae_mw": 0.026545661328702497,
        "rmse_mw": 0.09437867774669638,
        "mean_residual_mw": -0.026545661328702497
      },
      {
        "group": "7",
        "rows": 736,
        "mae_mw": 0.1453108411396716,
        "rmse_mw": 0.2920400953110562,
        "mean_residual_mw": -0.08766663514799788
      },
      {
        "group": "8",
        "rows": 736,
        "mae_mw": 0.9245395881090003,
        "rmse_mw": 1.3895595861404817,
        "mean_residual_mw": 0.014294002379066731
      },
      {
        "group": "9",
        "rows": 736,
        "mae_mw": 1.8299310544526712,
        "rmse_mw": 2.6832170625193377,
        "mean_residual_mw": 0.4999680422409367
      },
      {
        "group": "10",
        "rows": 736,
        "mae_mw": 2.783662219120512,
        "rmse_mw": 4.295576795214562,
        "mean_residual_mw": 0.5790434585811617
      },
      {
        "group": "11",
        "rows": 736,
        "mae_mw": 4.2184585527174505,
        "rmse_mw": 6.539174508482279,
        "mean_residual_mw": 0.5146172093163309
      },
      {
        "group": "12",
        "rows": 735,
        "mae_mw": 5.540363952239877,
        "rmse_mw": 8.43266188201335,
        "mean_residual_mw": 0.08355961884856675
      },
      {
        "group": "13",
        "rows": 736,
        "mae_mw": 7.636555795497616,
        "rmse_mw": 10.968144934558884,
        "mean_residual_mw": 0.21975678040281071
      },
      {
        "group": "14",
        "rows": 736,
        "mae_mw": 6.997985850969358,
        "rmse_mw": 10.31907326316263,
        "mean_residual_mw": -1.4084857748143063
      },
      {
        "group": "15",
        "rows": 736,
        "mae_mw": 5.171378562381948,
        "rmse_mw": 8.051556442037484,
        "mean_residual_mw": -1.6855700082424057
      },
      {
        "group": "16",
        "rows": 736,
        "mae_mw": 3.5332180744284445,
        "rmse_mw": 5.5716763960616955,
        "mean_residual_mw": -1.0456254477617306
      },
      {
        "group": "17",
        "rows": 736,
        "mae_mw": 2.3968467939406626,
        "rmse_mw": 3.4446067631455044,
        "mean_residual_mw": -1.2093040356306162
      },
      {
        "group": "18",
        "rows": 736,
        "mae_mw": 1.1433581758299567,
        "rmse_mw": 1.6259974034771196,
        "mean_residual_mw": -0.28588738834979077
      },
      {
        "group": "19",
        "rows": 732,
        "mae_mw": 0.3662255137585973,
        "rmse_mw": 0.6855752121278322,
        "mean_residual_mw": -0.041897027347386054
      },
      {
        "group": "20",
        "rows": 734,
        "mae_mw": 0.05257601334022699,
        "rmse_mw": 0.13415273962631513,
        "mean_residual_mw": 0.032862006192535355
      },
      {
        "group": "21",
        "rows": 736,
        "mae_mw": 0.00031034683427526186,
        "rmse_mw": 0.003221782183620531,
        "mean_residual_mw": 0.0003085033159208442
      },
      {
        "group": "22",
        "rows": 736,
        "mae_mw": 2.9725277957526918e-08,
        "rmse_mw": 2.9725277957526918e-08,
        "mean_residual_mw": -2.9725277957526918e-08
      },
      {
        "group": "23",
        "rows": 736,
        "mae_mw": 2.9725277957526918e-08,
        "rmse_mw": 2.9725277957526918e-08,
        "mean_residual_mw": -2.9725277957526918e-08
      }
    ],
    "month": [
      {
        "group": "2020-07",
        "rows": 2976,
        "mae_mw": 1.576969717831674,
        "rmse_mw": 3.477129671744532,
        "mean_residual_mw": -0.39334447741561135
      },
      {
        "group": "2020-08",
        "rows": 2970,
        "mae_mw": 1.568398267729766,
        "rmse_mw": 3.393053405299643,
        "mean_residual_mw": -0.3303053834032613
      },
      {
        "group": "2020-09",
        "rows": 2880,
        "mae_mw": 1.4357566541382318,
        "rmse_mw": 3.292404481210716,
        "mean_residual_mw": 0.5239387151101156
      },
      {
        "group": "2020-10",
        "rows": 2976,
        "mae_mw": 2.328741838744306,
        "rmse_mw": 5.991093816567869,
        "mean_residual_mw": -0.5016301237636234
      },
      {
        "group": "2020-11",
        "rows": 2880,
        "mae_mw": 2.2549540352526254,
        "rmse_mw": 5.765158565705139,
        "mean_residual_mw": -0.8509660361008586
      },
      {
        "group": "2020-12",
        "rows": 2975,
        "mae_mw": 1.532384190641777,
        "rmse_mw": 4.045267700355926,
        "mean_residual_mw": 0.5899828661167295
      }
    ]
  }
}
```

```json
{
  "validation": {
    "recorded_hour": {
      "lowest_mae": {
        "group": "0",
        "rows": 728,
        "mae_mw": 2.9725277957526915e-08,
        "rmse_mw": 2.9725277957526915e-08,
        "mean_residual_mw": -2.9725277957526915e-08
      },
      "highest_mae": {
        "group": "14",
        "rows": 728,
        "mae_mw": 8.263563752504277,
        "rmse_mw": 11.683830099003346,
        "mean_residual_mw": -1.9269136191343403
      }
    },
    "month": {
      "lowest_mae": {
        "group": "2020-01",
        "rows": 2976,
        "mae_mw": 1.1602782546396244,
        "rmse_mw": 2.7794234563541327,
        "mean_residual_mw": 0.5836645925682002
      },
      "highest_mae": {
        "group": "2020-05",
        "rows": 2976,
        "mae_mw": 4.037776298374447,
        "rmse_mw": 8.723421061032372,
        "mean_residual_mw": -3.187469152951283
      }
    }
  },
  "test": {
    "recorded_hour": {
      "lowest_mae": {
        "group": "1",
        "rows": 736,
        "mae_mw": 2.9725277957526918e-08,
        "rmse_mw": 2.9725277957526918e-08,
        "mean_residual_mw": -2.9725277957526918e-08
      },
      "highest_mae": {
        "group": "13",
        "rows": 736,
        "mae_mw": 7.636555795497616,
        "rmse_mw": 10.968144934558884,
        "mean_residual_mw": 0.21975678040281071
      }
    },
    "month": {
      "lowest_mae": {
        "group": "2020-09",
        "rows": 2880,
        "mae_mw": 1.4357566541382318,
        "rmse_mw": 3.292404481210716,
        "mean_residual_mw": 0.5239387151101156
      },
      "highest_mae": {
        "group": "2020-10",
        "rows": 2976,
        "mae_mw": 2.328741838744306,
        "rmse_mw": 5.991093816567869,
        "mean_residual_mw": -0.5016301237636234
      }
    }
  }
}
```

## 15. Feature Importance

| Feature | Random forest importance |
| --- | --- |
| Total solar irradiance (W/m2) | 0.953884713898493 |
| annual_sin | 0.008818560242849062 |
| Atmosphere (hpa) | 0.006301614704243548 |
| Global horizontal irradiance (W/m2) | 0.006258931017690361 |
| annual_cos | 0.005914178454403909 |
| Direct normal irradiance (W/m2) | 0.005205200850292757 |
| day_of_year | 0.005187248489339641 |
| Air temperature  (°C)  | 0.003316631550453809 |
| hour_sin | 0.001626432205330182 |
| hour_cos | 0.0015194030994975171 |
| day_of_week | 0.0014843328869075228 |
| hour | 0.0002637192877401284 |
| month | 0.00016147838829525836 |
| quarter | 5.755492446327643e-05 |

```json
{
  "scale": "MW per training-standardized input; not causal importance",
  "coefficients": [
    {
      "feature": "Total solar irradiance (W/m2)",
      "coefficient": 12.456327414179261
    },
    {
      "feature": "Direct normal irradiance (W/m2)",
      "coefficient": -0.29229843854219956
    },
    {
      "feature": "Global horizontal irradiance (W/m2)",
      "coefficient": 0.044516444267966554
    },
    {
      "feature": "Air temperature  (°C) ",
      "coefficient": 1.084303475842863
    },
    {
      "feature": "Atmosphere (hpa)",
      "coefficient": 0.381269385025875
    },
    {
      "feature": "hour",
      "coefficient": -0.3058823762936832
    },
    {
      "feature": "day_of_week",
      "coefficient": 0.09174501917742202
    },
    {
      "feature": "month",
      "coefficient": 0.73737573330696
    },
    {
      "feature": "day_of_year",
      "coefficient": -1.0647037233397243
    },
    {
      "feature": "quarter",
      "coefficient": 0.3680855100979277
    },
    {
      "feature": "hour_sin",
      "coefficient": -0.45487657220814925
    },
    {
      "feature": "hour_cos",
      "coefficient": -0.8742013484625972
    },
    {
      "feature": "annual_sin",
      "coefficient": 0.3749390477744309
    },
    {
      "feature": "annual_cos",
      "coefficient": 0.7991882334861873
    }
  ],
  "intercept_mw": 9.736911083945472
}
```

Forest impurity importance indicates model-specific relative usage, not causation or physical proof. Correlated irradiance/calendar predictors may share or mask importance. Linear coefficients use training-standardized inputs (MW per training standard deviation), not raw-unit or causal importance; collinearity remains relevant.

## 16. Residual Analysis

```json
{
  "validation": {
    "residual": {
      "definition": "actual minus predicted; positive means underprediction",
      "mean_mw": -0.5678325059880515,
      "median_mw": -2.9725277957526918e-08,
      "std_population_mw": 5.251028484240427,
      "min_mw": -37.51565145035141,
      "max_mw": 25.28284863361268,
      "overpredictions": 12745,
      "underpredictions": 4727,
      "exact_predictions": 0,
      "largest_absolute_errors": [
        {
          "timestamp": "2020-02-14T12:45:00.000",
          "split": "validation",
          "actual_power_mw": 4.498667,
          "predicted_power_mw": 42.0143184504,
          "residual_mw": -37.5156514504,
          "model_name": "random_forest",
          "power_group": "low positive",
          "absolute_error_mw": 37.5156514504
        },
        {
          "timestamp": "2020-02-14T13:15:00.000",
          "split": "validation",
          "actual_power_mw": 4.3526,
          "predicted_power_mw": 41.8646574558,
          "residual_mw": -37.5120574558,
          "model_name": "random_forest",
          "power_group": "low positive",
          "absolute_error_mw": 37.5120574558
        },
        {
          "timestamp": "2020-02-14T13:00:00.000",
          "split": "validation",
          "actual_power_mw": 4.5278,
          "predicted_power_mw": 41.9914635267,
          "residual_mw": -37.4636635267,
          "model_name": "random_forest",
          "power_group": "low positive",
          "absolute_error_mw": 37.4636635267
        },
        {
          "timestamp": "2020-02-14T12:30:00.000",
          "split": "validation",
          "actual_power_mw": 4.6146,
          "predicted_power_mw": 41.9600553767,
          "residual_mw": -37.3454553767,
          "model_name": "random_forest",
          "power_group": "low positive",
          "absolute_error_mw": 37.3454553767
        },
        {
          "timestamp": "2020-02-14T14:30:00.000",
          "split": "validation",
          "actual_power_mw": 3.9866,
          "predicted_power_mw": 41.2255494236,
          "residual_mw": -37.2389494236,
          "model_name": "random_forest",
          "power_group": "low positive",
          "absolute_error_mw": 37.2389494236
        },
        {
          "timestamp": "2020-02-14T12:15:00.000",
          "split": "validation",
          "actual_power_mw": 4.579667,
          "predicted_power_mw": 41.7465494039,
          "residual_mw": -37.1668824039,
          "model_name": "random_forest",
          "power_group": "low positive",
          "absolute_error_mw": 37.1668824039
        },
        {
          "timestamp": "2020-02-14T13:30:00.000",
          "split": "validation",
          "actual_power_mw": 4.4174,
          "predicted_power_mw": 41.3577969884,
          "residual_mw": -36.9403969884,
          "model_name": "random_forest",
          "power_group": "low positive",
          "absolute_error_mw": 36.9403969884
        },
        {
          "timestamp": "2020-05-11T14:15:00.000",
          "split": "validation",
          "actual_power_mw": 3.1892,
          "predicted_power_mw": 40.0891811539,
          "residual_mw": -36.8999811539,
          "model_name": "random_forest",
          "power_group": "low positive",
          "absolute_error_mw": 36.8999811539
        },
        {
          "timestamp": "2020-05-11T13:15:00.000",
          "split": "validation",
          "actual_power_mw": 3.8276,
          "predicted_power_mw": 40.0773249174,
          "residual_mw": -36.2497249174,
          "model_name": "random_forest",
          "power_group": "low positive",
          "absolute_error_mw": 36.2497249174
        },
        {
          "timestamp": "2020-05-11T13:30:00.000",
          "split": "validation",
          "actual_power_mw": 3.954467,
          "predicted_power_mw": 40.0564362518,
          "residual_mw": -36.1019692518,
          "model_name": "random_forest",
          "power_group": "low positive",
          "absolute_error_mw": 36.1019692518
        }
      ]
    },
    "prediction_range": {
      "min_mw": 2.9725277957526918e-08,
      "max_mw": 44.47294395458838,
      "negative_predictions": 0
    }
  },
  "test": {
    "residual": {
      "definition": "actual minus predicted; positive means underprediction",
      "mean_mw": -0.16033816954030466,
      "median_mw": -2.9725277957526918e-08,
      "std_population_mw": 4.465949086331704,
      "min_mw": -35.384074468257204,
      "max_mw": 31.09279880535877,
      "overpredictions": 13038,
      "underpredictions": 4619,
      "exact_predictions": 0,
      "largest_absolute_errors": [
        {
          "timestamp": "2020-10-25T14:00:00.000",
          "split": "test",
          "actual_power_mw": 5.2072,
          "predicted_power_mw": 40.5912744683,
          "residual_mw": -35.3840744683,
          "model_name": "random_forest",
          "power_group": "low positive",
          "absolute_error_mw": 35.3840744683
        },
        {
          "timestamp": "2020-10-25T14:15:00.000",
          "split": "test",
          "actual_power_mw": 5.1356,
          "predicted_power_mw": 39.7405351184,
          "residual_mw": -34.6049351184,
          "model_name": "random_forest",
          "power_group": "low positive",
          "absolute_error_mw": 34.6049351184
        },
        {
          "timestamp": "2020-10-25T13:30:00.000",
          "split": "test",
          "actual_power_mw": 5.750133,
          "predicted_power_mw": 39.9683117423,
          "residual_mw": -34.2181787423,
          "model_name": "random_forest",
          "power_group": "low positive",
          "absolute_error_mw": 34.2181787423
        },
        {
          "timestamp": "2020-10-25T14:30:00.000",
          "split": "test",
          "actual_power_mw": 5.0868,
          "predicted_power_mw": 38.420444985,
          "residual_mw": -33.333644985,
          "model_name": "random_forest",
          "power_group": "low positive",
          "absolute_error_mw": 33.333644985
        },
        {
          "timestamp": "2020-10-25T13:45:00.000",
          "split": "test",
          "actual_power_mw": 5.730133,
          "predicted_power_mw": 38.3315835274,
          "residual_mw": -32.6014505274,
          "model_name": "random_forest",
          "power_group": "low positive",
          "absolute_error_mw": 32.6014505274
        },
        {
          "timestamp": "2020-11-04T14:15:00.000",
          "split": "test",
          "actual_power_mw": 6.397266,
          "predicted_power_mw": 38.8301613196,
          "residual_mw": -32.4328953196,
          "model_name": "random_forest",
          "power_group": "low positive",
          "absolute_error_mw": 32.4328953196
        },
        {
          "timestamp": "2020-10-27T13:45:00.000",
          "split": "test",
          "actual_power_mw": 7.506067,
          "predicted_power_mw": 39.6315664614,
          "residual_mw": -32.1254994614,
          "model_name": "random_forest",
          "power_group": "low positive",
          "absolute_error_mw": 32.1254994614
        },
        {
          "timestamp": "2020-10-25T14:45:00.000",
          "split": "test",
          "actual_power_mw": 5.115067,
          "predicted_power_mw": 37.0753974764,
          "residual_mw": -31.9603304764,
          "model_name": "random_forest",
          "power_group": "low positive",
          "absolute_error_mw": 31.9603304764
        },
        {
          "timestamp": "2020-10-25T13:15:00.000",
          "split": "test",
          "actual_power_mw": 5.710933,
          "predicted_power_mw": 37.5604842315,
          "residual_mw": -31.8495512315,
          "model_name": "random_forest",
          "power_group": "low positive",
          "absolute_error_mw": 31.8495512315
        },
        {
          "timestamp": "2020-11-04T14:30:00.000",
          "split": "test",
          "actual_power_mw": 5.824733,
          "predicted_power_mw": 37.6021022264,
          "residual_mw": -31.7773692264,
          "model_name": "random_forest",
          "power_group": "low positive",
          "absolute_error_mw": 31.7773692264
        }
      ]
    },
    "prediction_range": {
      "min_mw": 2.9725277957526918e-08,
      "max_mw": 42.40073271937054,
      "negative_predictions": 0
    }
  }
}
```

Residual standard deviation uses population ddof=0. Positive mean suggests average underprediction; negative mean suggests overprediction. Largest errors and group means are descriptive and not proof of operational causes.

## 17. Limitations

```json
[
  "Single site, two years, observed contemporaneous inputs; no future forecast input or horizon",
  "Unresolved observation timezone, total irradiance plane, AC/DC and interval-averaging semantics",
  "Filename nominal capacity is not verified; no capacity normalization or clipping",
  "Humidity remains excluded; complete-case omission can bias coverage; gaps remain",
  "Native forest importance is model-specific and affected by correlated predictors, not causal evidence",
  "Diagnostic test analysis must not drive additional tuning against this same test period"
]
```

No deployment accuracy threshold or confidence interval is established; one site and two years cannot demonstrate wider generalisation.

## 18. Future Forecasting Limitation

This model performs weather-to-solar-power estimation using observed contemporaneous inputs. It is not yet a true future solar forecasting model. Future forecasting requires weather and irradiance forecasts or forecastable substitutes, forecast origin/horizon and verified prediction-time availability.

## 19. Recommended Next Step

Milestone 5D — Advanced Solar Model Evaluation is justified as a bounded experiment: the selected baseline improves validation MAE over the constant benchmark, while train/validation gaps and the reported residuals leave questions about nonlinear generalisation. Improvement from advanced models is not guaranteed. Predeclare candidates and validation criteria; do not use the test diagnostics to tune. A fresh untouched period is preferable for confirming any adaptation.

Reproduce from the repository root: `python -m ml.training.train_solar_baseline`. Models, metrics, predictions, diagnostics and best-model metadata are Git-ignored under ml/artifacts. No Milestone 5D/6, model API, aggregation or control is implemented.
