# GridCast AI Wind Data Preprocessing Report

## 1. Input Dataset

**FACTS FOUND.** `ml/data/raw/wind/Wind farm site 1 (Nominal capacity-99MW).xlsx`. SHA-256 `c7b6c86e80fa1f36c7547bcbb17205dc063c554981f07620fa3a2e7ec463fddc`. Verified against the Milestone 1 hash and analysis. Source rows: 70,176; columns: 13; 2019-01-01 00:00 through 2020-12-31 23:45, regular 15 minutes. No schema discrepancy found.

## 2. Schema Verification

```json
{
  "rows": 70176,
  "columns": 13,
  "schema": [
    {
      "name": "Time(year-month-day h:m:s)",
      "dtype": "object",
      "missing": 0
    },
    {
      "name": "Wind speed at height of 10 meters (m/s)",
      "dtype": "float64",
      "missing": 0
    },
    {
      "name": "Wind direction at height of 10 meters (˚)",
      "dtype": "float64",
      "missing": 0
    },
    {
      "name": "Wind speed at height of 30 meters (m/s)",
      "dtype": "float64",
      "missing": 0
    },
    {
      "name": "Wind direction at height of 30 meters (˚)",
      "dtype": "float64",
      "missing": 0
    },
    {
      "name": "Wind speed at height of 50 meters (m/s)",
      "dtype": "float64",
      "missing": 0
    },
    {
      "name": "Wind direction at height of 50 meters (˚)",
      "dtype": "float64",
      "missing": 0
    },
    {
      "name": "Wind speed - at the height of wheel hub(m/s)",
      "dtype": "float64",
      "missing": 0
    },
    {
      "name": "Wind speed - at the height of wheel hub (˚)",
      "dtype": "float64",
      "missing": 1
    },
    {
      "name": "Air temperature  (°C) ",
      "dtype": "float64",
      "missing": 0
    },
    {
      "name": "Atmosphere (hpa)",
      "dtype": "float64",
      "missing": 0
    },
    {
      "name": "Relative humidity (%)",
      "dtype": "float64",
      "missing": 0
    },
    {
      "name": "Power (MW)",
      "dtype": "float64",
      "missing": 0
    }
  ],
  "earliest": "2019-01-01 00:00:00",
  "latest": "2020-12-31 23:45:00",
  "regular_15_minutes": true,
  "timezone": "unknown; source naive values preserved"
}
```

## 3. Sentinel Value Analysis

**FACTS FOUND.** All 11 weather columns contain -99 on the same 138 rows (0.19665% of observations). No supplied codebook defines it. Negative speed, direction, pressure and humidity violate header-supported ranges. The temperature and ambiguous-column codes coincide with the same multi-sensor outage, supporting context-based interpretation rather than a universal temperature cutoff.
**TRANSFORMATION DECISION.** LIKELY SENTINEL, not VERIFIED SENTINEL: replace these weather codes with null in memory. Never apply a blanket replacement to power.

```json
{
  "Wind speed at height of 10 meters (m/s)": {
    "count": 138,
    "percent_rows": 0.1966484268125855,
    "classification": "LIKELY SENTINEL",
    "documented": false,
    "physical_plausibility": "outside header-supported physical range",
    "reason": "No codebook. Invalid range or exact coincidence with multi-sensor -99 outage supports sentinel interpretation.",
    "action": "replace -99 with null in memory"
  },
  "Wind speed at height of 30 meters (m/s)": {
    "count": 138,
    "percent_rows": 0.1966484268125855,
    "classification": "LIKELY SENTINEL",
    "documented": false,
    "physical_plausibility": "outside header-supported physical range",
    "reason": "No codebook. Invalid range or exact coincidence with multi-sensor -99 outage supports sentinel interpretation.",
    "action": "replace -99 with null in memory"
  },
  "Wind speed at height of 50 meters (m/s)": {
    "count": 138,
    "percent_rows": 0.1966484268125855,
    "classification": "LIKELY SENTINEL",
    "documented": false,
    "physical_plausibility": "outside header-supported physical range",
    "reason": "No codebook. Invalid range or exact coincidence with multi-sensor -99 outage supports sentinel interpretation.",
    "action": "replace -99 with null in memory"
  },
  "Wind speed - at the height of wheel hub(m/s)": {
    "count": 138,
    "percent_rows": 0.1966484268125855,
    "classification": "LIKELY SENTINEL",
    "documented": false,
    "physical_plausibility": "outside header-supported physical range",
    "reason": "No codebook. Invalid range or exact coincidence with multi-sensor -99 outage supports sentinel interpretation.",
    "action": "replace -99 with null in memory"
  },
  "Wind direction at height of 10 meters (˚)": {
    "count": 138,
    "percent_rows": 0.1966484268125855,
    "classification": "LIKELY SENTINEL",
    "documented": false,
    "physical_plausibility": "outside header-supported physical range",
    "reason": "No codebook. Invalid range or exact coincidence with multi-sensor -99 outage supports sentinel interpretation.",
    "action": "replace -99 with null in memory"
  },
  "Wind direction at height of 30 meters (˚)": {
    "count": 138,
    "percent_rows": 0.1966484268125855,
    "classification": "LIKELY SENTINEL",
    "documented": false,
    "physical_plausibility": "outside header-supported physical range",
    "reason": "No codebook. Invalid range or exact coincidence with multi-sensor -99 outage supports sentinel interpretation.",
    "action": "replace -99 with null in memory"
  },
  "Wind direction at height of 50 meters (˚)": {
    "count": 138,
    "percent_rows": 0.1966484268125855,
    "classification": "LIKELY SENTINEL",
    "documented": false,
    "physical_plausibility": "outside header-supported physical range",
    "reason": "No codebook. Invalid range or exact coincidence with multi-sensor -99 outage supports sentinel interpretation.",
    "action": "replace -99 with null in memory"
  },
  "Wind speed - at the height of wheel hub (˚)": {
    "count": 138,
    "percent_rows": 0.1966484268125855,
    "classification": "LIKELY SENTINEL",
    "documented": false,
    "physical_plausibility": "not assessed as a standalone code; semantic or environmental context required",
    "reason": "No codebook. Invalid range or exact coincidence with multi-sensor -99 outage supports sentinel interpretation.",
    "action": "replace -99 with null in memory"
  },
  "Air temperature  (°C) ": {
    "count": 138,
    "percent_rows": 0.1966484268125855,
    "classification": "LIKELY SENTINEL",
    "documented": false,
    "physical_plausibility": "not assessed as a standalone code; semantic or environmental context required",
    "reason": "No codebook. Invalid range or exact coincidence with multi-sensor -99 outage supports sentinel interpretation.",
    "action": "replace -99 with null in memory"
  },
  "Atmosphere (hpa)": {
    "count": 138,
    "percent_rows": 0.1966484268125855,
    "classification": "LIKELY SENTINEL",
    "documented": false,
    "physical_plausibility": "outside header-supported physical range",
    "reason": "No codebook. Invalid range or exact coincidence with multi-sensor -99 outage supports sentinel interpretation.",
    "action": "replace -99 with null in memory"
  },
  "Relative humidity (%)": {
    "count": 138,
    "percent_rows": 0.1966484268125855,
    "classification": "LIKELY SENTINEL",
    "documented": false,
    "physical_plausibility": "outside header-supported physical range",
    "reason": "No codebook. Invalid range or exact coincidence with multi-sensor -99 outage supports sentinel interpretation.",
    "action": "replace -99 with null in memory"
  },
  "Power (MW)": {
    "count": 0,
    "percent_rows": 0.0,
    "classification": "UNCERTAIN",
    "documented": false,
    "physical_plausibility": "not assessed as a standalone code; semantic or environmental context required",
    "reason": "No automatic sentinel interpretation (including absent codes and target values).",
    "action": "retain; review if present"
  }
}
```

## 4. Invalid Value Analysis

**FACTS FOUND.** Two zero readings in `Atmosphere (hpa)` coincide with all-zero weather rows; neighboring pressures are near 889–890 hPa. Zero terrestrial ambient pressure is invalid.
**TRANSFORMATION DECISION.** Convert exactly these two pressure values to null. Other weather zeros are not blanket-changed. Both rows will be accounted for by complete-case selection.

```json
{
  "columns": {
    "Wind speed at height of 10 meters (m/s)": {
      "sentinels_to_null": 138
    },
    "Wind speed at height of 30 meters (m/s)": {
      "sentinels_to_null": 138
    },
    "Wind speed at height of 50 meters (m/s)": {
      "sentinels_to_null": 138
    },
    "Wind speed - at the height of wheel hub(m/s)": {
      "sentinels_to_null": 138
    },
    "Wind direction at height of 10 meters (˚)": {
      "sentinels_to_null": 138
    },
    "Wind direction at height of 30 meters (˚)": {
      "sentinels_to_null": 138
    },
    "Wind direction at height of 50 meters (˚)": {
      "sentinels_to_null": 138
    },
    "Wind speed - at the height of wheel hub (˚)": {
      "sentinels_to_null": 138
    },
    "Air temperature  (°C) ": {
      "sentinels_to_null": 138
    },
    "Atmosphere (hpa)": {
      "sentinels_to_null": 138
    },
    "Relative humidity (%)": {
      "sentinels_to_null": 138
    }
  },
  "zero_pressure_to_null": 2,
  "zero_pressure_reason": "Zero hPa is invalid for terrestrial ambient pressure; retain other zero weather values pending verification."
}
```

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-07-02 01:00:00",
    "Wind speed at height of 10 meters (m/s)": 1.358,
    "Wind direction at height of 10 meters (˚)": 220.2,
    "Wind speed at height of 30 meters (m/s)": 0.0,
    "Wind direction at height of 30 meters (˚)": 290.98,
    "Wind speed at height of 50 meters (m/s)": 0.0,
    "Wind direction at height of 50 meters (˚)": 314.0,
    "Wind speed - at the height of wheel hub(m/s)": 0.0,
    "Wind speed - at the height of wheel hub (˚)": 320.0,
    "Air temperature  (°C) ": 24.856,
    "Atmosphere (hpa)": 889.2,
    "Relative humidity (%)": 26.608,
    "Power (MW)": 0.145667
  },
  {
    "Time(year-month-day h:m:s)": "2019-07-02 01:15:00",
    "Wind speed at height of 10 meters (m/s)": 0.0,
    "Wind direction at height of 10 meters (˚)": 0.0,
    "Wind speed at height of 30 meters (m/s)": 0.0,
    "Wind direction at height of 30 meters (˚)": 0.0,
    "Wind speed at height of 50 meters (m/s)": 0.0,
    "Wind direction at height of 50 meters (˚)": 0.0,
    "Wind speed - at the height of wheel hub(m/s)": 0.0,
    "Wind speed - at the height of wheel hub (˚)": 0.0,
    "Air temperature  (°C) ": 0.0,
    "Atmosphere (hpa)": 0.0,
    "Relative humidity (%)": 0.0,
    "Power (MW)": 0.105164
  },
  {
    "Time(year-month-day h:m:s)": "2019-07-02 01:30:00",
    "Wind speed at height of 10 meters (m/s)": 1.631,
    "Wind direction at height of 10 meters (˚)": 201.067,
    "Wind speed at height of 30 meters (m/s)": 0.0,
    "Wind direction at height of 30 meters (˚)": 213.129,
    "Wind speed at height of 50 meters (m/s)": 0.0,
    "Wind direction at height of 50 meters (˚)": 233.733,
    "Wind speed - at the height of wheel hub(m/s)": 1.143,
    "Wind speed - at the height of wheel hub (˚)": 227.0,
    "Air temperature  (°C) ": 23.531,
    "Atmosphere (hpa)": 890.233,
    "Relative humidity (%)": 28.085,
    "Power (MW)": 0.65159
  },
  {
    "Time(year-month-day h:m:s)": "2020-05-12 19:45:00",
    "Wind speed at height of 10 meters (m/s)": 5.525,
    "Wind direction at height of 10 meters (˚)": 227.8,
    "Wind speed at height of 30 meters (m/s)": 4.4,
    "Wind direction at height of 30 meters (˚)": 227.744,
    "Wind speed at height of 50 meters (m/s)": 4.5,
    "Wind direction at height of 50 meters (˚)": 230.0,
    "Wind speed - at the height of wheel hub(m/s)": 4.419,
    "Wind speed - at the height of wheel hub (˚)": 221.0,
    "Air temperature  (°C) ": 13.266,
    "Atmosphere (hpa)": 890.0,
    "Relative humidity (%)": 8.72,
    "Power (MW)": 68.38707
  },
  {
    "Time(year-month-day h:m:s)": "2020-05-12T20:00:00.000",
    "Wind speed at height of 10 meters (m/s)": 0.0,
    "Wind direction at height of 10 meters (˚)": 0.0,
    "Wind speed at height of 30 meters (m/s)": 0.0,
    "Wind direction at height of 30 meters (˚)": 0.0,
    "Wind speed at height of 50 meters (m/s)": 0.0,
    "Wind direction at height of 50 meters (˚)": 0.0,
    "Wind speed - at the height of wheel hub(m/s)": 0.0,
    "Wind speed - at the height of wheel hub (˚)": 0.0,
    "Air temperature  (°C) ": 0.0,
    "Atmosphere (hpa)": 0.0,
    "Relative humidity (%)": 0.0,
    "Power (MW)": 60.698734
  },
  {
    "Time(year-month-day h:m:s)": "2020-05-12 20:15:00",
    "Wind speed at height of 10 meters (m/s)": 8.422,
    "Wind direction at height of 10 meters (˚)": 291.553,
    "Wind speed at height of 30 meters (m/s)": 9.219,
    "Wind direction at height of 30 meters (˚)": 292.55,
    "Wind speed at height of 50 meters (m/s)": 9.62,
    "Wind direction at height of 50 meters (˚)": 297.367,
    "Wind speed - at the height of wheel hub(m/s)": 10.065,
    "Wind speed - at the height of wheel hub (˚)": 294.367,
    "Air temperature  (°C) ": 24.56,
    "Atmosphere (hpa)": 889.3,
    "Relative humidity (%)": 9.761,
    "Power (MW)": 61.150658
  }
]
```

## 5. Ambiguous Column Analysis

**FACTS FOUND.** The hub degree column retains a contradictory speed label and one original null. Its non-sentinel range is 0–358.5; descriptive associations are stronger with direction than speed. Correlation cannot establish meaning, particularly for circular variables.
**TRANSFORMATION DECISION.** UNRESOLVED; **EXCLUDED PENDING SEMANTIC VERIFICATION**. No direction encoding is applied. Raw data remains intact. Workbook metadata inspected is recorded below and in the manifest.

```json
{
  "ambiguous_column": "Wind speed - at the height of wheel hub (˚)",
  "classification": "UNRESOLVED",
  "decision": "EXCLUDED PENDING SEMANTIC VERIFICATION",
  "raw_min": -99.0,
  "raw_max": 358.5,
  "original_nulls": 1,
  "quantiles_excluding_minus99": {
    "0.0": 0.0,
    "0.25": 142.0,
    "0.5": 248.717,
    "0.75": 279.267,
    "1.0": 358.5
  },
  "pearson_correlations_excluding_minus99": {
    "Wind speed at height of 10 meters (m/s)": 0.45858576232551773,
    "Wind speed at height of 30 meters (m/s)": 0.47773095096143753,
    "Wind speed at height of 50 meters (m/s)": 0.4697009585201645,
    "Wind speed - at the height of wheel hub(m/s)": 0.4602325593975121,
    "Wind direction at height of 10 meters (˚)": 0.843344883449738,
    "Wind direction at height of 30 meters (˚)": 0.9005800588199854,
    "Wind direction at height of 50 meters (˚)": 0.9469995500599601,
    "Wind speed - at the height of wheel hub (˚)": 1.0,
    "Air temperature  (°C) ": 0.2695750246283211,
    "Atmosphere (hpa)": 0.09448575714785915,
    "Relative humidity (%)": 0.012963388862000083
  },
  "interpretation": "Degree unit, range and stronger association with directions suggest direction, but contradictory header and absent semantic definition prevent verification. Pearson correlation of circular variables is descriptive only.",
  "synchronous_zero_weather_rows": 2,
  "zero_weather_decision": "Other zeros remain plausible individually and are not blanket-replaced. The two synchronous-zero rows are omitted due to invalid pressure regardless.",
  "workbook_metadata": {
    "docProps/core.xml": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\r\n<cp:coreProperties xmlns:cp=\"http://schemas.openxmlformats.org/package/2006/metadata/core-properties\" xmlns:dc=\"http://purl.org/dc/elements/1.1/\" xmlns:dcterms=\"http://purl.org/dc/terms/\" xmlns:dcmitype=\"http://purl.org/dc/dcmitype/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"><dc:creator>jwl</dc:creator><cp:lastModifiedBy>Chen Yongbao</cp:lastModifiedBy><dcterms:created xsi:type=\"dcterms:W3CDTF\">2020-04-12T03:42:00Z</dcterms:created><dcterms:modified xsi:type=\"dcterms:W3CDTF\">2022-05-19T08:39:32Z</dcterms:modified></cp:coreProperties>",
    "docProps/app.xml": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\r\n<Properties xmlns=\"http://schemas.openxmlformats.org/officeDocument/2006/extended-properties\" xmlns:vt=\"http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes\"><Application>Microsoft Excel</Application><DocSecurity>0</DocSecurity><ScaleCrop>false</ScaleCrop><HeadingPairs><vt:vector size=\"2\" baseType=\"variant\"><vt:variant><vt:lpstr>工作表</vt:lpstr></vt:variant><vt:variant><vt:i4>1</vt:i4></vt:variant></vt:vector></HeadingPairs><TitlesOfParts><vt:vector size=\"1\" baseType=\"lpstr\"><vt:lpstr>sheet1</vt:lpstr></vt:vector></TitlesOfParts><LinksUpToDate>false</LinksUpToDate><SharedDoc>false</SharedDoc><HyperlinksChanged>false</HyperlinksChanged><AppVersion>16.0300</AppVersion></Properties>",
    "docProps/custom.xml": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\r\n<Properties xmlns=\"http://schemas.openxmlformats.org/officeDocument/2006/custom-properties\" xmlns:vt=\"http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes\"><property fmtid=\"{D5CDD505-2E9C-101B-9397-08002B2CF9AE}\" pid=\"2\" name=\"KSOProductBuildVer\"><vt:lpwstr>2052-10.1.0.7224</vt:lpwstr></property></Properties>"
  }
}
```

## 6. Target Validation

**FACTS FOUND.** Target is labelled power in MW, not energy. Nominal 99 MW is a filename/user-provided rating.
**TRANSFORMATION DECISION.** Retain valid zero generation and statistical extremes. No target filling, clipping, scaling or future target features. Rows with missing weather can still have valid targets; their omission is recorded separately.

```json
{
  "before": {
    "column": "Power (MW)",
    "units": "MW",
    "measurement": "POWER",
    "nominal_capacity_MW": 99.0,
    "missing": 0,
    "nonfinite_nonnull": 0,
    "negative": 0,
    "above_nominal": 0,
    "valid_zero_generation": 206,
    "zero_decision": "VALID ZERO GENERATION for retention; not independent verification of operating state",
    "invalid_target_value": 0,
    "suspicious_iqr_values": 2,
    "suspicious_decision": "Retain; IQR extremes and nominal exceedances need review, not automatic clipping",
    "distribution": {
      "0.0": 0.0,
      "0.01": 0.105164,
      "0.25": 1.570352,
      "0.5": 14.939664,
      "0.75": 40.17366199999999,
      "0.99": 82.568915,
      "1.0": 98.09444
    },
    "mean": 23.40834716162933,
    "largest_absolute_adjacent_change_MW": 68.026812,
    "time_missing": 0,
    "duplicate_timestamps": 0,
    "regular_15_minutes": true
  },
  "after": {
    "column": "Power (MW)",
    "units": "MW",
    "measurement": "POWER",
    "nominal_capacity_MW": 99.0,
    "missing": 0,
    "nonfinite_nonnull": 0,
    "negative": 0,
    "above_nominal": 0,
    "valid_zero_generation": 206,
    "zero_decision": "VALID ZERO GENERATION for retention; not independent verification of operating state",
    "invalid_target_value": 0,
    "suspicious_iqr_values": 0,
    "suspicious_decision": "Retain; IQR extremes and nominal exceedances need review, not automatic clipping",
    "distribution": {
      "0.0": 0.0,
      "0.01": 0.105164,
      "0.25": 1.578879,
      "0.5": 14.9787445,
      "0.75": 40.206881749999994,
      "0.99": 82.58429299999987,
      "1.0": 98.09444
    },
    "mean": 23.432162066630017,
    "largest_absolute_adjacent_change_MW": 68.026812,
    "time_missing": 0,
    "duplicate_timestamps": 0,
    "regular_15_minutes": false
  }
}
```

## 7. Missing Value Strategy

**FACTS FOUND.** Per-column runs below are measured after invalid-value conversion and before omission. The seven synchronized sentinel runs contain 11, 1, 4, 78, 1, 40 and 3 observations in chronological order.
**TRANSFORMATION DECISION.** Drop the unresolved column for semantic reasons. For retained weather features, omit incomplete rows instead of fabricating long outages. The two short pressure gaps could support causal filling, but omitting two rows avoids an additional assumption. Do not interpolate, forward-fill or learn a median. Target values are never imputed. No omission depends on the excluded hub column's lone null.

```json
{
  "Wind speed at height of 10 meters (m/s)": {
    "missing": 138,
    "percent": 0.1966484268125855,
    "run_count": 7,
    "max_run": 78,
    "pattern": "clustered",
    "runs": [
      {
        "start": "2019-04-12 11:00:00",
        "end": "2019-04-12 13:30:00",
        "observations": 11,
        "minutes_at_15min_cadence": 165
      },
      {
        "start": "2019-06-21 23:45:00",
        "end": "2019-06-21 23:45:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2019-07-21 23:00:00",
        "end": "2019-07-21 23:45:00",
        "observations": 4,
        "minutes_at_15min_cadence": 60
      },
      {
        "start": "2019-09-20 08:15:00",
        "end": "2019-09-21 03:30:00",
        "observations": 78,
        "minutes_at_15min_cadence": 1170
      },
      {
        "start": "2020-03-29 23:45:00",
        "end": "2020-03-29 23:45:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2020-11-30 23:45:00",
        "end": "2020-12-01 09:30:00",
        "observations": 40,
        "minutes_at_15min_cadence": 600
      },
      {
        "start": "2020-12-17 13:15:00",
        "end": "2020-12-17 13:45:00",
        "observations": 3,
        "minutes_at_15min_cadence": 45
      }
    ]
  },
  "Wind speed at height of 30 meters (m/s)": {
    "missing": 138,
    "percent": 0.1966484268125855,
    "run_count": 7,
    "max_run": 78,
    "pattern": "clustered",
    "runs": [
      {
        "start": "2019-04-12 11:00:00",
        "end": "2019-04-12 13:30:00",
        "observations": 11,
        "minutes_at_15min_cadence": 165
      },
      {
        "start": "2019-06-21 23:45:00",
        "end": "2019-06-21 23:45:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2019-07-21 23:00:00",
        "end": "2019-07-21 23:45:00",
        "observations": 4,
        "minutes_at_15min_cadence": 60
      },
      {
        "start": "2019-09-20 08:15:00",
        "end": "2019-09-21 03:30:00",
        "observations": 78,
        "minutes_at_15min_cadence": 1170
      },
      {
        "start": "2020-03-29 23:45:00",
        "end": "2020-03-29 23:45:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2020-11-30 23:45:00",
        "end": "2020-12-01 09:30:00",
        "observations": 40,
        "minutes_at_15min_cadence": 600
      },
      {
        "start": "2020-12-17 13:15:00",
        "end": "2020-12-17 13:45:00",
        "observations": 3,
        "minutes_at_15min_cadence": 45
      }
    ]
  },
  "Wind speed at height of 50 meters (m/s)": {
    "missing": 138,
    "percent": 0.1966484268125855,
    "run_count": 7,
    "max_run": 78,
    "pattern": "clustered",
    "runs": [
      {
        "start": "2019-04-12 11:00:00",
        "end": "2019-04-12 13:30:00",
        "observations": 11,
        "minutes_at_15min_cadence": 165
      },
      {
        "start": "2019-06-21 23:45:00",
        "end": "2019-06-21 23:45:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2019-07-21 23:00:00",
        "end": "2019-07-21 23:45:00",
        "observations": 4,
        "minutes_at_15min_cadence": 60
      },
      {
        "start": "2019-09-20 08:15:00",
        "end": "2019-09-21 03:30:00",
        "observations": 78,
        "minutes_at_15min_cadence": 1170
      },
      {
        "start": "2020-03-29 23:45:00",
        "end": "2020-03-29 23:45:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2020-11-30 23:45:00",
        "end": "2020-12-01 09:30:00",
        "observations": 40,
        "minutes_at_15min_cadence": 600
      },
      {
        "start": "2020-12-17 13:15:00",
        "end": "2020-12-17 13:45:00",
        "observations": 3,
        "minutes_at_15min_cadence": 45
      }
    ]
  },
  "Wind speed - at the height of wheel hub(m/s)": {
    "missing": 138,
    "percent": 0.1966484268125855,
    "run_count": 7,
    "max_run": 78,
    "pattern": "clustered",
    "runs": [
      {
        "start": "2019-04-12 11:00:00",
        "end": "2019-04-12 13:30:00",
        "observations": 11,
        "minutes_at_15min_cadence": 165
      },
      {
        "start": "2019-06-21 23:45:00",
        "end": "2019-06-21 23:45:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2019-07-21 23:00:00",
        "end": "2019-07-21 23:45:00",
        "observations": 4,
        "minutes_at_15min_cadence": 60
      },
      {
        "start": "2019-09-20 08:15:00",
        "end": "2019-09-21 03:30:00",
        "observations": 78,
        "minutes_at_15min_cadence": 1170
      },
      {
        "start": "2020-03-29 23:45:00",
        "end": "2020-03-29 23:45:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2020-11-30 23:45:00",
        "end": "2020-12-01 09:30:00",
        "observations": 40,
        "minutes_at_15min_cadence": 600
      },
      {
        "start": "2020-12-17 13:15:00",
        "end": "2020-12-17 13:45:00",
        "observations": 3,
        "minutes_at_15min_cadence": 45
      }
    ]
  },
  "Wind direction at height of 10 meters (˚)": {
    "missing": 138,
    "percent": 0.1966484268125855,
    "run_count": 7,
    "max_run": 78,
    "pattern": "clustered",
    "runs": [
      {
        "start": "2019-04-12 11:00:00",
        "end": "2019-04-12 13:30:00",
        "observations": 11,
        "minutes_at_15min_cadence": 165
      },
      {
        "start": "2019-06-21 23:45:00",
        "end": "2019-06-21 23:45:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2019-07-21 23:00:00",
        "end": "2019-07-21 23:45:00",
        "observations": 4,
        "minutes_at_15min_cadence": 60
      },
      {
        "start": "2019-09-20 08:15:00",
        "end": "2019-09-21 03:30:00",
        "observations": 78,
        "minutes_at_15min_cadence": 1170
      },
      {
        "start": "2020-03-29 23:45:00",
        "end": "2020-03-29 23:45:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2020-11-30 23:45:00",
        "end": "2020-12-01 09:30:00",
        "observations": 40,
        "minutes_at_15min_cadence": 600
      },
      {
        "start": "2020-12-17 13:15:00",
        "end": "2020-12-17 13:45:00",
        "observations": 3,
        "minutes_at_15min_cadence": 45
      }
    ]
  },
  "Wind direction at height of 30 meters (˚)": {
    "missing": 138,
    "percent": 0.1966484268125855,
    "run_count": 7,
    "max_run": 78,
    "pattern": "clustered",
    "runs": [
      {
        "start": "2019-04-12 11:00:00",
        "end": "2019-04-12 13:30:00",
        "observations": 11,
        "minutes_at_15min_cadence": 165
      },
      {
        "start": "2019-06-21 23:45:00",
        "end": "2019-06-21 23:45:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2019-07-21 23:00:00",
        "end": "2019-07-21 23:45:00",
        "observations": 4,
        "minutes_at_15min_cadence": 60
      },
      {
        "start": "2019-09-20 08:15:00",
        "end": "2019-09-21 03:30:00",
        "observations": 78,
        "minutes_at_15min_cadence": 1170
      },
      {
        "start": "2020-03-29 23:45:00",
        "end": "2020-03-29 23:45:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2020-11-30 23:45:00",
        "end": "2020-12-01 09:30:00",
        "observations": 40,
        "minutes_at_15min_cadence": 600
      },
      {
        "start": "2020-12-17 13:15:00",
        "end": "2020-12-17 13:45:00",
        "observations": 3,
        "minutes_at_15min_cadence": 45
      }
    ]
  },
  "Wind direction at height of 50 meters (˚)": {
    "missing": 138,
    "percent": 0.1966484268125855,
    "run_count": 7,
    "max_run": 78,
    "pattern": "clustered",
    "runs": [
      {
        "start": "2019-04-12 11:00:00",
        "end": "2019-04-12 13:30:00",
        "observations": 11,
        "minutes_at_15min_cadence": 165
      },
      {
        "start": "2019-06-21 23:45:00",
        "end": "2019-06-21 23:45:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2019-07-21 23:00:00",
        "end": "2019-07-21 23:45:00",
        "observations": 4,
        "minutes_at_15min_cadence": 60
      },
      {
        "start": "2019-09-20 08:15:00",
        "end": "2019-09-21 03:30:00",
        "observations": 78,
        "minutes_at_15min_cadence": 1170
      },
      {
        "start": "2020-03-29 23:45:00",
        "end": "2020-03-29 23:45:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2020-11-30 23:45:00",
        "end": "2020-12-01 09:30:00",
        "observations": 40,
        "minutes_at_15min_cadence": 600
      },
      {
        "start": "2020-12-17 13:15:00",
        "end": "2020-12-17 13:45:00",
        "observations": 3,
        "minutes_at_15min_cadence": 45
      }
    ]
  },
  "Wind speed - at the height of wheel hub (˚)": {
    "missing": 139,
    "percent": 0.1980734154126767,
    "run_count": 8,
    "max_run": 78,
    "pattern": "clustered",
    "runs": [
      {
        "start": "2019-01-01 00:30:00",
        "end": "2019-01-01 00:30:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2019-04-12 11:00:00",
        "end": "2019-04-12 13:30:00",
        "observations": 11,
        "minutes_at_15min_cadence": 165
      },
      {
        "start": "2019-06-21 23:45:00",
        "end": "2019-06-21 23:45:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2019-07-21 23:00:00",
        "end": "2019-07-21 23:45:00",
        "observations": 4,
        "minutes_at_15min_cadence": 60
      },
      {
        "start": "2019-09-20 08:15:00",
        "end": "2019-09-21 03:30:00",
        "observations": 78,
        "minutes_at_15min_cadence": 1170
      },
      {
        "start": "2020-03-29 23:45:00",
        "end": "2020-03-29 23:45:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2020-11-30 23:45:00",
        "end": "2020-12-01 09:30:00",
        "observations": 40,
        "minutes_at_15min_cadence": 600
      },
      {
        "start": "2020-12-17 13:15:00",
        "end": "2020-12-17 13:45:00",
        "observations": 3,
        "minutes_at_15min_cadence": 45
      }
    ]
  },
  "Air temperature  (°C) ": {
    "missing": 138,
    "percent": 0.1966484268125855,
    "run_count": 7,
    "max_run": 78,
    "pattern": "clustered",
    "runs": [
      {
        "start": "2019-04-12 11:00:00",
        "end": "2019-04-12 13:30:00",
        "observations": 11,
        "minutes_at_15min_cadence": 165
      },
      {
        "start": "2019-06-21 23:45:00",
        "end": "2019-06-21 23:45:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2019-07-21 23:00:00",
        "end": "2019-07-21 23:45:00",
        "observations": 4,
        "minutes_at_15min_cadence": 60
      },
      {
        "start": "2019-09-20 08:15:00",
        "end": "2019-09-21 03:30:00",
        "observations": 78,
        "minutes_at_15min_cadence": 1170
      },
      {
        "start": "2020-03-29 23:45:00",
        "end": "2020-03-29 23:45:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2020-11-30 23:45:00",
        "end": "2020-12-01 09:30:00",
        "observations": 40,
        "minutes_at_15min_cadence": 600
      },
      {
        "start": "2020-12-17 13:15:00",
        "end": "2020-12-17 13:45:00",
        "observations": 3,
        "minutes_at_15min_cadence": 45
      }
    ]
  },
  "Atmosphere (hpa)": {
    "missing": 140,
    "percent": 0.1994984040127679,
    "run_count": 9,
    "max_run": 78,
    "pattern": "clustered",
    "runs": [
      {
        "start": "2019-04-12 11:00:00",
        "end": "2019-04-12 13:30:00",
        "observations": 11,
        "minutes_at_15min_cadence": 165
      },
      {
        "start": "2019-06-21 23:45:00",
        "end": "2019-06-21 23:45:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2019-07-02 01:15:00",
        "end": "2019-07-02 01:15:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2019-07-21 23:00:00",
        "end": "2019-07-21 23:45:00",
        "observations": 4,
        "minutes_at_15min_cadence": 60
      },
      {
        "start": "2019-09-20 08:15:00",
        "end": "2019-09-21 03:30:00",
        "observations": 78,
        "minutes_at_15min_cadence": 1170
      },
      {
        "start": "2020-03-29 23:45:00",
        "end": "2020-03-29 23:45:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2020-05-12 20:00:00",
        "end": "2020-05-12 20:00:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2020-11-30 23:45:00",
        "end": "2020-12-01 09:30:00",
        "observations": 40,
        "minutes_at_15min_cadence": 600
      },
      {
        "start": "2020-12-17 13:15:00",
        "end": "2020-12-17 13:45:00",
        "observations": 3,
        "minutes_at_15min_cadence": 45
      }
    ]
  },
  "Relative humidity (%)": {
    "missing": 138,
    "percent": 0.1966484268125855,
    "run_count": 7,
    "max_run": 78,
    "pattern": "clustered",
    "runs": [
      {
        "start": "2019-04-12 11:00:00",
        "end": "2019-04-12 13:30:00",
        "observations": 11,
        "minutes_at_15min_cadence": 165
      },
      {
        "start": "2019-06-21 23:45:00",
        "end": "2019-06-21 23:45:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2019-07-21 23:00:00",
        "end": "2019-07-21 23:45:00",
        "observations": 4,
        "minutes_at_15min_cadence": 60
      },
      {
        "start": "2019-09-20 08:15:00",
        "end": "2019-09-21 03:30:00",
        "observations": 78,
        "minutes_at_15min_cadence": 1170
      },
      {
        "start": "2020-03-29 23:45:00",
        "end": "2020-03-29 23:45:00",
        "observations": 1,
        "minutes_at_15min_cadence": 15
      },
      {
        "start": "2020-11-30 23:45:00",
        "end": "2020-12-01 09:30:00",
        "observations": 40,
        "minutes_at_15min_cadence": 600
      },
      {
        "start": "2020-12-17 13:15:00",
        "end": "2020-12-17 13:45:00",
        "observations": 3,
        "minutes_at_15min_cadence": 45
      }
    ]
  }
}
```

Omitted 140 rows (0.19950%). Every omitted timestamp and missing column is recorded in `wind_feature_manifest.json` → `audit.removed_rows`. Raw observations are preserved. The prepared table has gaps; do not interpret neighboring retained rows as necessarily 15 minutes apart.

## 8. Feature Selection

| Exact original column | Classification |
| --- | --- |
| "Time(year-month-day h:m:s)" | TIME SOURCE |
| "Wind speed at height of 10 meters (m/s)" | PRIMARY FEATURE |
| "Wind direction at height of 10 meters (˚)" | PRIMARY FEATURE |
| "Wind speed at height of 30 meters (m/s)" | PRIMARY FEATURE |
| "Wind direction at height of 30 meters (˚)" | PRIMARY FEATURE |
| "Wind speed at height of 50 meters (m/s)" | PRIMARY FEATURE |
| "Wind direction at height of 50 meters (˚)" | PRIMARY FEATURE |
| "Wind speed - at the height of wheel hub(m/s)" | PRIMARY FEATURE |
| "Wind speed - at the height of wheel hub (˚)" | EXCLUDE |
| "Air temperature  (°C) " | SECONDARY FEATURE |
| "Atmosphere (hpa)" | SECONDARY FEATURE |
| "Relative humidity (%)" | SECONDARY FEATURE |
| "Power (MW)" | TARGET |

## 9. Time Feature Engineering

**TRANSFORMATION DECISIONS.** Retain the timestamp under its original header, parsed without timezone conversion. hour=0–23, day_of_week=Monday 0–Sunday 6, month=1–12, day_of_year=1–365/366 and quarter=1–4. Hour sine/cosine use fractional hours including minutes and seconds with period 24. Annual sine/cosine use (day_of_year−1+fraction_of_day)/365 or /366 for the timestamp's year. These deterministic calendars require no fitted parameters or future observations. Source timezone remains unknown.

## 10. Wind Feature Engineering

**TRANSFORMATION DECISIONS.** For verified 10/30/50 m direction headers, compute sin(degrees × π/180) and cos(degrees × π/180). Retain original directions and all four speed measurements independently. No u/v components exist: no magnitude feature is created. No inferred hub direction, height aggregation, lag features or wind-shear assumptions are introduced.

## 11. Feature Leakage Review

**FACTS FOUND.** Weather issue times and forecast horizon are absent. Observed weather at a target timestamp is not verified available before a future forecast origin.
**TRANSFORMATION DECISIONS.** Calendar features are SAFE FOR FORECASTING; observed weather and its direction encodings are POTENTIAL LEAKAGE and must not be used as future weather observations. Target and ambiguous/unreviewed predictors are EXCLUDE. This output is a complete numerical observation table for subsequent alignment, not an approved operational future-forecast feature matrix. Only calendar predictors pass the current future-availability gate.

```json
{
  "Time(year-month-day h:m:s)": {
    "classification": "SAFE FOR FORECASTING",
    "reason": "Calendar is known in advance; maintain consistent source timezone convention."
  },
  "Wind speed at height of 10 meters (m/s)": {
    "classification": "POTENTIAL LEAKAGE",
    "reason": "Observation at target timestamp; availability before a future forecast origin is unverified. Must lag to known observations or replace with as-issued weather forecasts before forecasting."
  },
  "Wind speed at height of 30 meters (m/s)": {
    "classification": "POTENTIAL LEAKAGE",
    "reason": "Observation at target timestamp; availability before a future forecast origin is unverified. Must lag to known observations or replace with as-issued weather forecasts before forecasting."
  },
  "Wind speed at height of 50 meters (m/s)": {
    "classification": "POTENTIAL LEAKAGE",
    "reason": "Observation at target timestamp; availability before a future forecast origin is unverified. Must lag to known observations or replace with as-issued weather forecasts before forecasting."
  },
  "Wind speed - at the height of wheel hub(m/s)": {
    "classification": "POTENTIAL LEAKAGE",
    "reason": "Observation at target timestamp; availability before a future forecast origin is unverified. Must lag to known observations or replace with as-issued weather forecasts before forecasting."
  },
  "Wind direction at height of 10 meters (˚)": {
    "classification": "POTENTIAL LEAKAGE",
    "reason": "Observation at target timestamp; availability before a future forecast origin is unverified. Must lag to known observations or replace with as-issued weather forecasts before forecasting."
  },
  "Wind direction at height of 30 meters (˚)": {
    "classification": "POTENTIAL LEAKAGE",
    "reason": "Observation at target timestamp; availability before a future forecast origin is unverified. Must lag to known observations or replace with as-issued weather forecasts before forecasting."
  },
  "Wind direction at height of 50 meters (˚)": {
    "classification": "POTENTIAL LEAKAGE",
    "reason": "Observation at target timestamp; availability before a future forecast origin is unverified. Must lag to known observations or replace with as-issued weather forecasts before forecasting."
  },
  "Air temperature  (°C) ": {
    "classification": "POTENTIAL LEAKAGE",
    "reason": "Observation at target timestamp; availability before a future forecast origin is unverified. Must lag to known observations or replace with as-issued weather forecasts before forecasting."
  },
  "Atmosphere (hpa)": {
    "classification": "POTENTIAL LEAKAGE",
    "reason": "Observation at target timestamp; availability before a future forecast origin is unverified. Must lag to known observations or replace with as-issued weather forecasts before forecasting."
  },
  "Relative humidity (%)": {
    "classification": "POTENTIAL LEAKAGE",
    "reason": "Observation at target timestamp; availability before a future forecast origin is unverified. Must lag to known observations or replace with as-issued weather forecasts before forecasting."
  },
  "hour": {
    "classification": "SAFE FOR FORECASTING",
    "reason": "Calendar is known in advance; maintain consistent source timezone convention."
  },
  "day_of_week": {
    "classification": "SAFE FOR FORECASTING",
    "reason": "Calendar is known in advance; maintain consistent source timezone convention."
  },
  "month": {
    "classification": "SAFE FOR FORECASTING",
    "reason": "Calendar is known in advance; maintain consistent source timezone convention."
  },
  "day_of_year": {
    "classification": "SAFE FOR FORECASTING",
    "reason": "Calendar is known in advance; maintain consistent source timezone convention."
  },
  "quarter": {
    "classification": "SAFE FOR FORECASTING",
    "reason": "Calendar is known in advance; maintain consistent source timezone convention."
  },
  "hour_sin": {
    "classification": "SAFE FOR FORECASTING",
    "reason": "Calendar is known in advance; maintain consistent source timezone convention."
  },
  "hour_cos": {
    "classification": "SAFE FOR FORECASTING",
    "reason": "Calendar is known in advance; maintain consistent source timezone convention."
  },
  "day_of_year_sin": {
    "classification": "SAFE FOR FORECASTING",
    "reason": "Calendar is known in advance; maintain consistent source timezone convention."
  },
  "day_of_year_cos": {
    "classification": "SAFE FOR FORECASTING",
    "reason": "Calendar is known in advance; maintain consistent source timezone convention."
  },
  "wind_direction_10m_sin": {
    "classification": "POTENTIAL LEAKAGE",
    "reason": "Observation at target timestamp; availability before a future forecast origin is unverified. Must lag to known observations or replace with as-issued weather forecasts before forecasting."
  },
  "wind_direction_10m_cos": {
    "classification": "POTENTIAL LEAKAGE",
    "reason": "Observation at target timestamp; availability before a future forecast origin is unverified. Must lag to known observations or replace with as-issued weather forecasts before forecasting."
  },
  "wind_direction_30m_sin": {
    "classification": "POTENTIAL LEAKAGE",
    "reason": "Observation at target timestamp; availability before a future forecast origin is unverified. Must lag to known observations or replace with as-issued weather forecasts before forecasting."
  },
  "wind_direction_30m_cos": {
    "classification": "POTENTIAL LEAKAGE",
    "reason": "Observation at target timestamp; availability before a future forecast origin is unverified. Must lag to known observations or replace with as-issued weather forecasts before forecasting."
  },
  "wind_direction_50m_sin": {
    "classification": "POTENTIAL LEAKAGE",
    "reason": "Observation at target timestamp; availability before a future forecast origin is unverified. Must lag to known observations or replace with as-issued weather forecasts before forecasting."
  },
  "wind_direction_50m_cos": {
    "classification": "POTENTIAL LEAKAGE",
    "reason": "Observation at target timestamp; availability before a future forecast origin is unverified. Must lag to known observations or replace with as-issued weather forecasts before forecasting."
  },
  "Power (MW)": {
    "classification": "EXCLUDE",
    "reason": "Target, unresolved column or unreviewed feature; not an approved predictor."
  }
}
```

## 12. Final ML Feature Set

```json
{
  "primary_observations": [
    "Wind speed at height of 10 meters (m/s)",
    "Wind speed at height of 30 meters (m/s)",
    "Wind speed at height of 50 meters (m/s)",
    "Wind speed - at the height of wheel hub(m/s)",
    "Wind direction at height of 10 meters (˚)",
    "Wind direction at height of 30 meters (˚)",
    "Wind direction at height of 50 meters (˚)"
  ],
  "secondary_observations": [
    "Air temperature  (°C) ",
    "Atmosphere (hpa)",
    "Relative humidity (%)"
  ],
  "engineered": [
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
  "forecast_safe_predictors": [
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
  "target_not_a_predictor": "Power (MW)",
  "time_index": "Time(year-month-day h:m:s)"
}
```

## 13. Output Dataset

```json
{
  "path": "ml/data/processed/wind_site_1_prepared.csv",
  "rows": 70036,
  "columns": 27
}
```

**FACTS FOUND.** CSV has no index column, missing selected values or unexplained -99 codes. Inputs remain unchanged and output is Git-ignored. Reports and manifest can be tracked.
**TRANSFORMATION DECISIONS: chronological split plan.** Fixed calendar boundaries, no random shuffle and no separate split files. Percentages below refer to retained rows.

```json
{
  "train": "2019-01-01 <= t < 2020-01-01",
  "validation": "2020-01-01 <= t < 2020-07-01",
  "test": "2020-07-01 <= t < 2021-01-01"
}
```

```json
{
  "train": {
    "start": "2019-01-01 00:00:00",
    "end": "2019-12-31 23:45:00",
    "rows": 34945,
    "percent": 49.89576789079902
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

No shuffle, no fitted imputation/scaling, no cross-split fill. Any future fitted preprocessing must fit on train only; purge overlapping labels once a horizon is defined.

Reproduce from the repository root:

```powershell
python -m ml.data_processing.run_wind_preprocessing
```

## 14. Remaining Limitations

**FACTS FOUND / LIMITATIONS.** No source URL/license, verified sentinel codebook, site coordinates, weather availability times, hub height or angular reference is supplied. Semantic conclusions remain conservative. Full-data distributions are diagnostic summaries, never fitted imputation/scaling parameters. Sentinel and physical-range policies rely on domain validity and synchronized error evidence rather than optimized test performance. Complete-case selection can introduce missingness bias. Preserve the omission ledger and original time spacing during future lag construction. Define the forecast horizon and align available inputs before model training. No models, API changes or future milestone functionality are included.
