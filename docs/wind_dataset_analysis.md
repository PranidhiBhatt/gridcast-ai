# GridCast AI Wind Dataset Analysis

## 1. Dataset Source and Discovery

**FACTS FROM ACTUAL DATA.** Discovery root: `C:\Users\prani\Documents\ChatGPT\Hackout2026\gridcast-ai`. Parent `C:\Users\prani\Documents\ChatGPT\Hackout2026` contained this project only. Two extracted Excel workbooks, two RAR archives and two correlation PNGs were found at the repository root. Archive listings contain six wind and eight solar workbooks each. No external source URL, license, site coordinates, data dictionary or processing methodology was found among these local files. Archive names identify versions only; they do not prove how processing was performed.

Every archived wind workbook and every sheet was inspected in memory. Solar headers were inspected only in the extracted site 1 file; archived solar files were inventoried by name and size. PNG contents were not used as measurement evidence. Sizes below are bytes (uncompressed for archive members).

Source and selected-copy SHA-256 hashes are recorded in `docs/dataset_sources.json` and checked before and after every run. The source manifest is a discovery baseline, not a publisher authenticity guarantee.

## 2. Available Dataset Files

| Relative path (! denotes archive member) | File name | Extension | Bytes | Wind | Solar | Generation | Weather |
| --- | --- | --- | --- | --- | --- | --- | --- |
| data_original.rar | data_original.rar | .rar | 77966660 | unknown | unknown | see members/selected copy | see members/selected copy |
| data_original.rar!data_original/solar_stations/Solar station site 1 (Nominal capacity-50MW).xlsx | Solar station site 1 (Nominal capacity-50MW).xlsx | .xlsx | 3738807 | no indication | yes (filename only) | unverified | unverified |
| data_original.rar!data_original/solar_stations/Solar station site 2 (Nominal capacity-130MW).xlsx | Solar station site 2 (Nominal capacity-130MW).xlsx | .xlsx | 4365111 | no indication | yes (filename only) | unverified | unverified |
| data_original.rar!data_original/solar_stations/Solar station site 3 (Nominal capacity-30MW).xlsx | Solar station site 3 (Nominal capacity-30MW).xlsx | .xlsx | 3444470 | no indication | yes (filename only) | unverified | unverified |
| data_original.rar!data_original/solar_stations/Solar station site 4 (Nominal capacity-130MW).xlsx | Solar station site 4 (Nominal capacity-130MW).xlsx | .xlsx | 6487609 | no indication | yes (filename only) | unverified | unverified |
| data_original.rar!data_original/solar_stations/Solar station site 5 (Nominal capacity-110MW).xlsx | Solar station site 5 (Nominal capacity-110MW).xlsx | .xlsx | 3465493 | no indication | yes (filename only) | unverified | unverified |
| data_original.rar!data_original/solar_stations/Solar station site 6 (Nominal capacity-35MW).xlsx | Solar station site 6 (Nominal capacity-35MW).xlsx | .xlsx | 4284319 | no indication | yes (filename only) | unverified | unverified |
| data_original.rar!data_original/solar_stations/Solar station site 7 (Nominal capacity-30MW).xlsx | Solar station site 7 (Nominal capacity-30MW).xlsx | .xlsx | 4302012 | no indication | yes (filename only) | unverified | unverified |
| data_original.rar!data_original/solar_stations/Solar station site 8 (Nominal capacity-30MW).xlsx | Solar station site 8 (Nominal capacity-30MW).xlsx | .xlsx | 4716036 | no indication | yes (filename only) | unverified | unverified |
| data_original.rar!data_original/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx | Wind farm site 1 (Nominal capacity-99MW).xlsx | .xlsx | 8299552 | yes (headers) | no indication | yes (Power header) | yes (wind/weather headers) |
| data_original.rar!data_original/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx | Wind farm site 2 (Nominal capacity-200MW).xlsx | .xlsx | 8004735 | yes (headers) | no indication | yes (Power header) | yes (wind/weather headers) |
| data_original.rar!data_original/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx | Wind farm site 3 (Nominal capacity-99MW).xlsx | .xlsx | 7547380 | yes (headers) | no indication | yes (Power header) | yes (wind/weather headers) |
| data_original.rar!data_original/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx | Wind farm site 4 (Nominal capacity-66MW).xlsx | .xlsx | 7736279 | yes (headers) | no indication | yes (Power header) | yes (wind/weather headers) |
| data_original.rar!data_original/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx | Wind farm site 5 (Nominal capacity-36MW).xlsx | .xlsx | 6346125 | yes (headers) | no indication | yes (Power header) | yes (wind/weather headers) |
| data_original.rar!data_original/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx | Wind farm site 6 (Nominal capacity-96MW).xlsx | .xlsx | 6750700 | yes (headers) | no indication | yes (Power header) | yes (wind/weather headers) |
| data_processed.rar | data_processed.rar | .rar | 74468298 | unknown | unknown | see members/selected copy | see members/selected copy |
| data_processed.rar!data_processed/solar_stations/Solar station site 1 (Nominal capacity-50MW).xlsx | Solar station site 1 (Nominal capacity-50MW).xlsx | .xlsx | 3377039 | no indication | yes (filename only) | unverified | unverified |
| data_processed.rar!data_processed/solar_stations/Solar station site 2 (Nominal capacity-130MW).xlsx | Solar station site 2 (Nominal capacity-130MW).xlsx | .xlsx | 3983338 | no indication | yes (filename only) | unverified | unverified |
| data_processed.rar!data_processed/solar_stations/Solar station site 3 (Nominal capacity-30MW).xlsx | Solar station site 3 (Nominal capacity-30MW).xlsx | .xlsx | 1069047 | no indication | yes (filename only) | unverified | unverified |
| data_processed.rar!data_processed/solar_stations/Solar station site 4 (Nominal capacity-130MW).xlsx | Solar station site 4 (Nominal capacity-130MW).xlsx | .xlsx | 6479911 | no indication | yes (filename only) | unverified | unverified |
| data_processed.rar!data_processed/solar_stations/Solar station site 5 (Nominal capacity-110MW).xlsx | Solar station site 5 (Nominal capacity-110MW).xlsx | .xlsx | 3470280 | no indication | yes (filename only) | unverified | unverified |
| data_processed.rar!data_processed/solar_stations/Solar station site 6 (Nominal capacity-35MW).xlsx | Solar station site 6 (Nominal capacity-35MW).xlsx | .xlsx | 4285324 | no indication | yes (filename only) | unverified | unverified |
| data_processed.rar!data_processed/solar_stations/Solar station site 7 (Nominal capacity-30MW).xlsx | Solar station site 7 (Nominal capacity-30MW).xlsx | .xlsx | 4460611 | no indication | yes (filename only) | unverified | unverified |
| data_processed.rar!data_processed/solar_stations/Solar station site 8 (Nominal capacity-30MW).xlsx | Solar station site 8 (Nominal capacity-30MW).xlsx | .xlsx | 4717372 | no indication | yes (filename only) | unverified | unverified |
| data_processed.rar!data_processed/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx | Wind farm site 1 (Nominal capacity-99MW).xlsx | .xlsx | 8301819 | yes (headers) | no indication | yes (Power header) | yes (wind/weather headers) |
| data_processed.rar!data_processed/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx | Wind farm site 2 (Nominal capacity-200MW).xlsx | .xlsx | 8122793 | yes (headers) | no indication | yes (Power header) | yes (wind/weather headers) |
| data_processed.rar!data_processed/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx | Wind farm site 3 (Nominal capacity-99MW).xlsx | .xlsx | 7576032 | yes (headers) | no indication | yes (Power header) | yes (wind/weather headers) |
| data_processed.rar!data_processed/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx | Wind farm site 4 (Nominal capacity-66MW).xlsx | .xlsx | 7740877 | yes (headers) | no indication | yes (Power header) | yes (wind/weather headers) |
| data_processed.rar!data_processed/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx | Wind farm site 5 (Nominal capacity-36MW).xlsx | .xlsx | 5451779 | yes (headers) | no indication | yes (Power header) | yes (wind/weather headers) |
| data_processed.rar!data_processed/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx | Wind farm site 6 (Nominal capacity-96MW).xlsx | .xlsx | 6753502 | yes (headers) | no indication | yes (Power header) | yes (wind/weather headers) |
| Solar station site 1 (Nominal capacity-50MW).xlsx | Solar station site 1 (Nominal capacity-50MW).xlsx | .xlsx | 3738807 | unknown | yes (filename) | yes (Power header) | yes (weather headers) |
| SS_correlation.png | SS_correlation.png | .png | 191180 | unknown | yes (filename) | not tabular | not tabular |
| WF_correlation.png | WF_correlation.png | .png | 346621 | yes (filename) | unknown | not tabular | not tabular |
| Wind farm site 1 (Nominal capacity-99MW).xlsx | Wind farm site 1 (Nominal capacity-99MW).xlsx | .xlsx | 8299552 | yes (filename) | unknown | see members/selected copy | see members/selected copy |

## 3. Selected Wind Data Files

**FACTS.** Only the extracted wind site 1 workbook was copied, without changing bytes, to `ml/data/raw/wind/Wind farm site 1 (Nominal capacity-99MW).xlsx`. Its original remains at the root. All 12 archived wind workbooks are comparison candidates, inspected without permanent extraction. No solar copy was necessary. Raw directories, root downloads and archives are ignored by Git.

| Inspected file | Sheet | Format | Bytes | Rows | Columns |
| --- | --- | --- | --- | --- | --- |
| data_original.rar!data_original/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx | sheet1 | .xlsx | 8299552 | 70176 | 13 |
| data_original.rar!data_original/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx | sheet1 | .xlsx | 8004735 | 70176 | 13 |
| data_original.rar!data_original/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx | sheet1 | .xlsx | 7547380 | 70176 | 13 |
| data_original.rar!data_original/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx | sheet1 | .xlsx | 7736279 | 70176 | 13 |
| data_original.rar!data_original/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx | sheet 1 | .xlsx | 6346125 | 70176 | 13 |
| data_original.rar!data_original/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx | 2019 | .xlsx | 6750700 | 70176 | 13 |
| data_processed.rar!data_processed/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx | sheet1 | .xlsx | 8301819 | 70176 | 13 |
| data_processed.rar!data_processed/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx | sheet1 | .xlsx | 8122793 | 70176 | 12 |
| data_processed.rar!data_processed/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx | sheet1 | .xlsx | 7576032 | 70176 | 13 |
| data_processed.rar!data_processed/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx | sheet1 | .xlsx | 7740877 | 70176 | 13 |
| data_processed.rar!data_processed/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx | sheet 1 | .xlsx | 5451779 | 69999 | 11 |
| data_processed.rar!data_processed/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx | 2019 | .xlsx | 6753502 | 70176 | 13 |
| ml/data/raw/wind/Wind farm site 1 (Nominal capacity-99MW).xlsx | sheet1 | .xlsx | 8299552 | 70176 | 13 |

## 4. Dataset Schema

**FACTS.** Exact headers (including whitespace) are JSON-quoted below. Types are Pandas-inferred. Statistics exclude null and infinite values; missing and non-finite counts are reported separately. Samples are the first five rows in source order.

### data_original.rar!data_original/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx [sheet1]

| Exact column | dtype | Missing | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | object | 0 | — | — | — | — |
| "Wind speed at height of 10 meters (m/s)" | float64 | 0 | -99.0 | 25.465 | 5.495283501481988 | 5.372 |
| "Wind direction at height of 10 meters (˚)" | float64 | 0 | -99.0 | 358.987 | 221.82965451151392 | 235.753 |
| "Wind speed at height of 30 meters (m/s)" | float64 | 0 | -99.0 | 29.187 | 5.820112189352486 | 5.76 |
| "Wind direction at height of 30 meters (˚)" | float64 | 0 | -99.0 | 359.087 | 219.6239449099407 | 245.19650000000001 |
| "Wind speed at height of 50 meters (m/s)" | float64 | 0 | -99.0 | 29.678 | 5.949485735864114 | 5.78 |
| "Wind direction at height of 50 meters (˚)" | float64 | 0 | -99.0 | 358.933 | 220.83160671739626 | 251.6 |
| "Wind speed - at the height of wheel hub(m/s)" | float64 | 0 | -99.0 | 30.247 | 6.1566923022115825 | 5.849 |
| "Wind speed - at the height of wheel hub (˚)" | float64 | 1 | -99.0 | 358.5 | 215.95179120769507 | 248.567 |
| "Air temperature  (°C) " | float64 | 0 | -99.0 | 36.13 | 8.31075534370725 | 9.733 |
| "Atmosphere (hpa)" | float64 | 0 | -99.0 | 918.192 | 886.4167509262426 | 889.742 |
| "Relative humidity (%)" | float64 | 0 | -99.0 | 93.12 | 37.260329072617424 | 34.309 |
| "Power (MW)" | float64 | 0 | 0.0 | 98.09444 | 23.40834716162933 | 14.939664 |

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:00:00",
    "Wind speed at height of 10 meters (m/s)": 2.209,
    "Wind direction at height of 10 meters (˚)": 81.317,
    "Wind speed at height of 30 meters (m/s)": 1.991,
    "Wind direction at height of 30 meters (˚)": 74.814,
    "Wind speed at height of 50 meters (m/s)": 2.094,
    "Wind direction at height of 50 meters (˚)": 77.667,
    "Wind speed - at the height of wheel hub(m/s)": 2.494,
    "Wind speed - at the height of wheel hub (˚)": 74.5,
    "Air temperature  (°C) ": -13.484,
    "Atmosphere (hpa)": 889.867,
    "Relative humidity (%)": 76.32,
    "Power (MW)": 0.254383
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:15:00",
    "Wind speed at height of 10 meters (m/s)": 1.828,
    "Wind direction at height of 10 meters (˚)": 77.46,
    "Wind speed at height of 30 meters (m/s)": 1.698,
    "Wind direction at height of 30 meters (˚)": 75.048,
    "Wind speed at height of 50 meters (m/s)": 1.757,
    "Wind direction at height of 50 meters (˚)": 88.733,
    "Wind speed - at the height of wheel hub(m/s)": 1.882,
    "Wind speed - at the height of wheel hub (˚)": 74.367,
    "Air temperature  (°C) ": -13.691,
    "Atmosphere (hpa)": 889.575,
    "Relative humidity (%)": 76.757,
    "Power (MW)": 0.329703
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:30:00",
    "Wind speed at height of 10 meters (m/s)": 2.193,
    "Wind direction at height of 10 meters (˚)": 86.7,
    "Wind speed at height of 30 meters (m/s)": 2.313,
    "Wind direction at height of 30 meters (˚)": 84.688,
    "Wind speed at height of 50 meters (m/s)": 2.344,
    "Wind direction at height of 50 meters (˚)": 89.1,
    "Wind speed - at the height of wheel hub(m/s)": 2.35,
    "Wind speed - at the height of wheel hub (˚)": null,
    "Air temperature  (°C) ": -13.766,
    "Atmosphere (hpa)": 889.942,
    "Relative humidity (%)": 76.981,
    "Power (MW)": 0.296306
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:45:00",
    "Wind speed at height of 10 meters (m/s)": 2.654,
    "Wind direction at height of 10 meters (˚)": 78.16,
    "Wind speed at height of 30 meters (m/s)": 2.494,
    "Wind direction at height of 30 meters (˚)": 74.939,
    "Wind speed at height of 50 meters (m/s)": 2.574,
    "Wind direction at height of 50 meters (˚)": 87.267,
    "Wind speed - at the height of wheel hub(m/s)": 2.808,
    "Wind speed - at the height of wheel hub (˚)": 82.733,
    "Air temperature  (°C) ": -13.691,
    "Atmosphere (hpa)": 889.675,
    "Relative humidity (%)": 76.821,
    "Power (MW)": 0.18759
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01 01:00:00",
    "Wind speed at height of 10 meters (m/s)": 2.249,
    "Wind direction at height of 10 meters (˚)": 94.297,
    "Wind speed at height of 30 meters (m/s)": 2.192,
    "Wind direction at height of 30 meters (˚)": 91.14,
    "Wind speed at height of 50 meters (m/s)": 2.558,
    "Wind direction at height of 50 meters (˚)": 96.9,
    "Wind speed - at the height of wheel hub(m/s)": 2.924,
    "Wind speed - at the height of wheel hub (˚)": 92.967,
    "Air temperature  (°C) ": -13.447,
    "Atmosphere (hpa)": 890.025,
    "Relative humidity (%)": 74.571,
    "Power (MW)": 0.081005
  }
]
```

### data_original.rar!data_original/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx [sheet1]

| Exact column | dtype | Missing | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | object | 0 | — | — | — | — |
| "Wind speed at height of 10 meters (m/s)" | float64 | 0 | -99.0 | 23.3 | 6.22722181372549 | 6.47 |
| "Wind direction at height of 10 meters (˚)" | float64 | 0 | -99.0 | 359.916 | 217.61222702918377 | 248.65800000000002 |
| "Wind speed at height of 30 meters (m/s)" | float64 | 0 | -99.0 | 27.125 | 7.058590800273597 | 7.288 |
| "Wind direction at height of 30 meters (˚)" | float64 | 0 | -99.0 | 360.0 | 216.52108374658002 | 265.58500000000004 |
| "Wind speed at height of 50 meters (m/s)" | float64 | 0 | -99.0 | 28.196 | 7.297933111035111 | 7.525 |
| "Wind direction at height of 50 meters (˚)" | float64 | 0 | -99.0 | 359.889 | 208.740900250798 | 256.7435 |
| "Wind speed - at the height of wheel hub (m/s)" | float64 | 0 | -99.0 | 28.808 | 7.45560201493388 | 7.631 |
| "Wind speed - at the height of wheel hub  (˚)" | float64 | 0 | -99.0 | 359.802 | 206.79784047252622 | 243.1295 |
| "Air temperature  (°C) " | float64 | 0 | -99.0 | 37.59 | 8.61460265617875 | 10.274 |
| "Atmosphere (hpa)" | float64 | 0 | -99.0 | 900.45 | 877.4135514420884 | 884.022 |
| "Relative humidity (%)" | float64 | 0 | -99.0 | 97.58 | 33.26691670941632 | 32.908 |
| "Power (MW)" | float64 | 0 | 0.0 | 201.24808 | 72.68070406413874 | 75.36283499999999 |

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:00:00",
    "Wind speed at height of 10 meters (m/s)": 2.951,
    "Wind direction at height of 10 meters (˚)": 124.685,
    "Wind speed at height of 30 meters (m/s)": 4.634,
    "Wind direction at height of 30 meters (˚)": 114.568,
    "Wind speed at height of 50 meters (m/s)": 3.869,
    "Wind direction at height of 50 meters (˚)": 102.139,
    "Wind speed - at the height of wheel hub (m/s)": 2.645,
    "Wind speed - at the height of wheel hub  (˚)": 103.023,
    "Air temperature  (°C) ": -12.735,
    "Atmosphere (hpa)": 887.187,
    "Relative humidity (%)": 33.003,
    "Power (MW)": 33.451336
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:15:00",
    "Wind speed at height of 10 meters (m/s)": 2.951,
    "Wind direction at height of 10 meters (˚)": 129.697,
    "Wind speed at height of 30 meters (m/s)": 2.951,
    "Wind direction at height of 30 meters (˚)": 118.488,
    "Wind speed at height of 50 meters (m/s)": 2.951,
    "Wind direction at height of 50 meters (˚)": 97.463,
    "Wind speed - at the height of wheel hub (m/s)": 2.186,
    "Wind speed - at the height of wheel hub  (˚)": 108.914,
    "Air temperature  (°C) ": -12.992,
    "Atmosphere (hpa)": 887.227,
    "Relative humidity (%)": 33.005,
    "Power (MW)": 36.811337
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:30:00",
    "Wind speed at height of 10 meters (m/s)": 2.951,
    "Wind direction at height of 10 meters (˚)": 124.756,
    "Wind speed at height of 30 meters (m/s)": 3.563,
    "Wind direction at height of 30 meters (˚)": 118.21,
    "Wind speed at height of 50 meters (m/s)": 2.798,
    "Wind direction at height of 50 meters (˚)": 91.528,
    "Wind speed - at the height of wheel hub (m/s)": 2.492,
    "Wind speed - at the height of wheel hub  (˚)": 97.322,
    "Air temperature  (°C) ": -12.745,
    "Atmosphere (hpa)": 887.094,
    "Relative humidity (%)": 33.0,
    "Power (MW)": 31.172535
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:45:00",
    "Wind speed at height of 10 meters (m/s)": 2.186,
    "Wind direction at height of 10 meters (˚)": 129.019,
    "Wind speed at height of 30 meters (m/s)": 2.339,
    "Wind direction at height of 30 meters (˚)": 112.761,
    "Wind speed at height of 50 meters (m/s)": 2.339,
    "Wind direction at height of 50 meters (˚)": 94.015,
    "Wind speed - at the height of wheel hub (m/s)": 1.281,
    "Wind speed - at the height of wheel hub  (˚)": 99.393,
    "Air temperature  (°C) ": -12.904,
    "Atmosphere (hpa)": 887.214,
    "Relative humidity (%)": 33.004,
    "Power (MW)": 27.836002
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01 01:00:00",
    "Wind speed at height of 10 meters (m/s)": 2.033,
    "Wind direction at height of 10 meters (˚)": 121.358,
    "Wind speed at height of 30 meters (m/s)": 1.88,
    "Wind direction at height of 30 meters (˚)": 105.626,
    "Wind speed at height of 50 meters (m/s)": 2.186,
    "Wind direction at height of 50 meters (˚)": 99.392,
    "Wind speed - at the height of wheel hub (m/s)": 2.186,
    "Wind speed - at the height of wheel hub  (˚)": 95.703,
    "Air temperature  (°C) ": -12.979,
    "Atmosphere (hpa)": 887.227,
    "Relative humidity (%)": 33.005,
    "Power (MW)": 31.192802
  }
]
```

### data_original.rar!data_original/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx [sheet1]

| Exact column | dtype | Missing | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | datetime64[ns] | 0 | — | — | — | — |
| "Wind speed at height of 10 meters (m/s)" | float64 | 0 | 0.0 | 27.926 | 3.5788002451122893 | 3.148 |
| "Wind direction at height of 10 meters (˚)" | float64 | 0 | 0.0 | 360.0 | 147.78127913533115 | 148.2 |
| "Wind speed at height of 30 meters (m/s)" | float64 | 0 | 0.0 | 22.0917 | 5.362684756896945 | 4.934 |
| "Wind direction at height of 30 meters (˚)" | float64 | 0 | 0.0 | 360.0 | 144.52969042682741 | 162.1 |
| "Wind speed at height of 50 meters (m/s)" | float64 | 0 | 0.0 | 21.836 | 4.925015288474691 | 4.5689150000000005 |
| "Wind direction at height of 50 meters (˚)" | float64 | 0 | 0.0 | 360.0 | 142.48838721056916 | 149.4 |
| "Wind speed - at the height of wheel hub  (m/s)" | float64 | 0 | 0.0 | 36.9203 | 4.026917558324783 | 3.837 |
| "Wind speed - at the height of wheel hub  (˚)" | float64 | 0 | 0.0 | 360.0 | 179.06615824078744 | 165.1 |
| "Air temperature  (°C) " | float64 | 0 | -115.6 | 36.32 | 17.432819539443685 | 20.48 |
| "Atmosphere (hpa)" | float64 | 0 | -92.496 | 990.731 | 967.3443259091426 | 971.731 |
| "Relative humidity (%)" | float64 | 0 | 0.0 | 356.915 | 58.47565179178066 | 56.85975 |
| "Power (MW)" | float64 | 0 | -0.668767 | 94.2666 | 18.143144855601122 | 8.346655 |

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:00:00.000",
    "Wind speed at height of 10 meters (m/s)": 2.32218,
    "Wind direction at height of 10 meters (˚)": 317.431,
    "Wind speed at height of 30 meters (m/s)": 2.59042,
    "Wind direction at height of 30 meters (˚)": 312.468,
    "Wind speed at height of 50 meters (m/s)": 1.62735,
    "Wind direction at height of 50 meters (˚)": 351.117,
    "Wind speed - at the height of wheel hub  (m/s)": 2.34887,
    "Wind speed - at the height of wheel hub  (˚)": 313.33,
    "Air temperature  (°C) ": 26.46,
    "Atmosphere (hpa)": 984.37,
    "Relative humidity (%)": 31.7949,
    "Power (MW)": -0.36579
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:15:00.000",
    "Wind speed at height of 10 meters (m/s)": 2.32218,
    "Wind direction at height of 10 meters (˚)": 317.431,
    "Wind speed at height of 30 meters (m/s)": 2.59042,
    "Wind direction at height of 30 meters (˚)": 312.468,
    "Wind speed at height of 50 meters (m/s)": 1.62735,
    "Wind direction at height of 50 meters (˚)": 351.117,
    "Wind speed - at the height of wheel hub  (m/s)": 2.34887,
    "Wind speed - at the height of wheel hub  (˚)": 313.33,
    "Air temperature  (°C) ": 26.46,
    "Atmosphere (hpa)": 984.37,
    "Relative humidity (%)": 31.7949,
    "Power (MW)": -0.376874
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:30:00.000",
    "Wind speed at height of 10 meters (m/s)": 2.32218,
    "Wind direction at height of 10 meters (˚)": 317.431,
    "Wind speed at height of 30 meters (m/s)": 2.59042,
    "Wind direction at height of 30 meters (˚)": 312.468,
    "Wind speed at height of 50 meters (m/s)": 1.62735,
    "Wind direction at height of 50 meters (˚)": 351.117,
    "Wind speed - at the height of wheel hub  (m/s)": 2.34887,
    "Wind speed - at the height of wheel hub  (˚)": 313.33,
    "Air temperature  (°C) ": 26.46,
    "Atmosphere (hpa)": 984.37,
    "Relative humidity (%)": 31.7949,
    "Power (MW)": -0.387959
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:45:00.000",
    "Wind speed at height of 10 meters (m/s)": 2.32218,
    "Wind direction at height of 10 meters (˚)": 317.431,
    "Wind speed at height of 30 meters (m/s)": 2.59042,
    "Wind direction at height of 30 meters (˚)": 312.468,
    "Wind speed at height of 50 meters (m/s)": 1.62735,
    "Wind direction at height of 50 meters (˚)": 351.117,
    "Wind speed - at the height of wheel hub  (m/s)": 2.34887,
    "Wind speed - at the height of wheel hub  (˚)": 313.33,
    "Air temperature  (°C) ": 26.46,
    "Atmosphere (hpa)": 984.37,
    "Relative humidity (%)": 31.7949,
    "Power (MW)": -0.395348
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T01:00:00.000",
    "Wind speed at height of 10 meters (m/s)": 2.32218,
    "Wind direction at height of 10 meters (˚)": 317.431,
    "Wind speed at height of 30 meters (m/s)": 2.59042,
    "Wind direction at height of 30 meters (˚)": 312.468,
    "Wind speed at height of 50 meters (m/s)": 1.62735,
    "Wind direction at height of 50 meters (˚)": 351.117,
    "Wind speed - at the height of wheel hub  (m/s)": 2.34887,
    "Wind speed - at the height of wheel hub  (˚)": 313.33,
    "Air temperature  (°C) ": 26.46,
    "Atmosphere (hpa)": 984.37,
    "Relative humidity (%)": 31.7949,
    "Power (MW)": -0.384264
  }
]
```

### data_original.rar!data_original/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx [sheet1]

| Exact column | dtype | Missing | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | datetime64[ns] | 0 | — | — | — | — |
| "Wind speed at height of 10 meters (m/s)" | float64 | 580 | 0.0 | 17.744 | 3.769946250646589 | 3.256667 |
| "Wind direction at height of 10 meters (˚)" | float64 | 580 | 0.0 | 356.6 | 193.48130763826944 | 176.4523335 |
| "Wind speed at height of 30 meters (m/s)" | float64 | 580 | 0.0 | 20.406667 | 4.201022013032358 | 3.663333 |
| "Wind direction at height of 30 meters (˚)" | float64 | 580 | 0.0 | 357.0 | 205.46400144644807 | 189.90633350000002 |
| "Wind speed at height of 50 meters (m/s)" | float64 | 580 | 0.0 | 30.819333 | 5.357921661216162 | 4.47 |
| "Wind direction at height of 50 meters (˚)" | float64 | 580 | 0.0 | 356.9 | 149.69480950406634 | 163.441 |
| "Wind speed - at the height of wheel hub  (m/s)" | float64 | 580 | 0.0 | 31.086 | 5.519318265374447 | 4.6313335 |
| "Wind speed - at the height of wheel hub (˚)" | float64 | 580 | 0.0 | 356.8 | 147.2832961058538 | 151.18433349999998 |
| "Air temperature  (°C) " | float64 | 580 | -3.82 | 35.253333 | 13.78685938551066 | 14.21 |
| "Atmosphere (hpa)" | float64 | 584 | 0.0 | 902.0 | 886.79714402256 | 887.0 |
| "Relative humidity (%)" | float64 | 584 | 0.0 | 100.0 | 80.7227967830354 | 85.62 |
| "Power (MW)" | float64 | 0 | 0.0 | 64.614 | 17.353544986833107 | 7.3196665 |

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:00:00.000",
    "Wind speed at height of 10 meters (m/s)": 4.41,
    "Wind direction at height of 10 meters (˚)": 19.81,
    "Wind speed at height of 30 meters (m/s)": 5.07,
    "Wind direction at height of 30 meters (˚)": 21.76,
    "Wind speed at height of 50 meters (m/s)": 7.52,
    "Wind direction at height of 50 meters (˚)": 179.1,
    "Wind speed - at the height of wheel hub  (m/s)": 0.0,
    "Wind speed - at the height of wheel hub (˚)": 209.2,
    "Air temperature  (°C) ": -2.25,
    "Atmosphere (hpa)": 898.0,
    "Relative humidity (%)": 100.0,
    "Power (MW)": 15.806
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:15:00.000",
    "Wind speed at height of 10 meters (m/s)": 4.4,
    "Wind direction at height of 10 meters (˚)": 19.79,
    "Wind speed at height of 30 meters (m/s)": 5.063333,
    "Wind direction at height of 30 meters (˚)": 21.75,
    "Wind speed at height of 50 meters (m/s)": 7.293333,
    "Wind direction at height of 50 meters (˚)": 179.1,
    "Wind speed - at the height of wheel hub  (m/s)": 0.0,
    "Wind speed - at the height of wheel hub (˚)": 209.2,
    "Air temperature  (°C) ": -2.24,
    "Atmosphere (hpa)": 898.0,
    "Relative humidity (%)": 100.0,
    "Power (MW)": 16.699333
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:30:00.000",
    "Wind speed at height of 10 meters (m/s)": 4.833333,
    "Wind direction at height of 10 meters (˚)": 19.79,
    "Wind speed at height of 30 meters (m/s)": 5.563333,
    "Wind direction at height of 30 meters (˚)": 21.75,
    "Wind speed at height of 50 meters (m/s)": 7.566667,
    "Wind direction at height of 50 meters (˚)": 179.1,
    "Wind speed - at the height of wheel hub  (m/s)": 0.0,
    "Wind speed - at the height of wheel hub (˚)": 209.2,
    "Air temperature  (°C) ": -2.24,
    "Atmosphere (hpa)": 898.0,
    "Relative humidity (%)": 100.0,
    "Power (MW)": 15.840667
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:45:00.000",
    "Wind speed at height of 10 meters (m/s)": 4.78,
    "Wind direction at height of 10 meters (˚)": 19.79,
    "Wind speed at height of 30 meters (m/s)": 5.5,
    "Wind direction at height of 30 meters (˚)": 21.75,
    "Wind speed at height of 50 meters (m/s)": 7.6,
    "Wind direction at height of 50 meters (˚)": 179.1,
    "Wind speed - at the height of wheel hub  (m/s)": 0.0,
    "Wind speed - at the height of wheel hub (˚)": 209.2,
    "Air temperature  (°C) ": -2.29,
    "Atmosphere (hpa)": 898.0,
    "Relative humidity (%)": 100.0,
    "Power (MW)": 14.887333
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T01:00:00.000",
    "Wind speed at height of 10 meters (m/s)": 4.34,
    "Wind direction at height of 10 meters (˚)": 19.79,
    "Wind speed at height of 30 meters (m/s)": 5.0,
    "Wind direction at height of 30 meters (˚)": 21.75,
    "Wind speed at height of 50 meters (m/s)": 7.12,
    "Wind direction at height of 50 meters (˚)": 179.1,
    "Wind speed - at the height of wheel hub  (m/s)": 0.0,
    "Wind speed - at the height of wheel hub (˚)": 209.2,
    "Air temperature  (°C) ": -2.343333,
    "Atmosphere (hpa)": 898.0,
    "Relative humidity (%)": 100.0,
    "Power (MW)": 14.865333
  }
]
```

### data_original.rar!data_original/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx [sheet 1]

| Exact column | dtype | Missing | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | datetime64[ns] | 0 | — | — | — | — |
| "Wind speed at height of 10 meters (m/s)" | float64 | 580 | -272.64 | 52.18 | 0.19181310252457037 | 0.0 |
| "Wind direction at height of 10 meters (˚)" | float64 | 580 | -0.9 | 357.0 | 159.84864024797406 | 150.54333350000002 |
| "Wind speed at height of 30 meters (m/s)" | float64 | 580 | -0.9 | 40.646667 | 0.30705286767199264 | 0.0 |
| "Wind direction at height of 30 meters (˚)" | float64 | 580 | -0.9 | 356.933333 | 118.3498991927266 | 85.713333 |
| "Wind speed at height of 50 meters (m/s)" | float64 | 580 | -0.9 | 24.046667 | 4.205987664783896 | 3.96 |
| "Wind direction at height of 50 meters (˚)" | float64 | 580 | -0.9 | 356.9 | 106.76005253849358 | 70.6633335 |
| "Wind speed - at the height of wheel hub (m/s)" | float64 | 580 | 0.0 | 26.166667 | 4.687790925191103 | 3.96 |
| "Wind speed - at the height of wheel hub  (˚)" | float64 | 580 | 0.0 | 358.6 | 184.94912690085638 | 191.066667 |
| "Air temperature  (°C) " | float64 | 580 | -9.92 | 35.753333 | 13.562583342341082 | 14.16 |
| "Atmosphere (hpa)" | float64 | 584 | 0.0 | 2110.486667 | 718.1043936727353 | 817.2 |
| "Relative humidity (%)" | float64 | 584 | 0.0 | 101.0 | 69.88984621896195 | 78.9 |
| "Power (MW)" | float64 | 0 | 0.0 | 35.350667 | 6.680827338591541 | 1.7189999999999999 |

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:00:00.000",
    "Wind speed at height of 10 meters (m/s)": 0.0,
    "Wind direction at height of 10 meters (˚)": 0.0,
    "Wind speed at height of 30 meters (m/s)": 0.0,
    "Wind direction at height of 30 meters (˚)": 0.0,
    "Wind speed at height of 50 meters (m/s)": 0.0,
    "Wind direction at height of 50 meters (˚)": 0.0,
    "Wind speed - at the height of wheel hub (m/s)": 3.57,
    "Wind speed - at the height of wheel hub  (˚)": 41.7,
    "Air temperature  (°C) ": 0.0,
    "Atmosphere (hpa)": 0.0,
    "Relative humidity (%)": 0.0,
    "Power (MW)": 0.114
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:15:00.000",
    "Wind speed at height of 10 meters (m/s)": 0.0,
    "Wind direction at height of 10 meters (˚)": 0.0,
    "Wind speed at height of 30 meters (m/s)": 0.0,
    "Wind direction at height of 30 meters (˚)": 0.0,
    "Wind speed at height of 50 meters (m/s)": 0.0,
    "Wind direction at height of 50 meters (˚)": 0.0,
    "Wind speed - at the height of wheel hub (m/s)": 3.706667,
    "Wind speed - at the height of wheel hub  (˚)": 9.866667,
    "Air temperature  (°C) ": 0.0,
    "Atmosphere (hpa)": 0.0,
    "Relative humidity (%)": 0.0,
    "Power (MW)": 1.080667
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:30:00.000",
    "Wind speed at height of 10 meters (m/s)": 0.0,
    "Wind direction at height of 10 meters (˚)": 0.0,
    "Wind speed at height of 30 meters (m/s)": 0.0,
    "Wind direction at height of 30 meters (˚)": 0.0,
    "Wind speed at height of 50 meters (m/s)": 0.0,
    "Wind direction at height of 50 meters (˚)": 0.0,
    "Wind speed - at the height of wheel hub (m/s)": 3.72,
    "Wind speed - at the height of wheel hub  (˚)": 11.133333,
    "Air temperature  (°C) ": 0.0,
    "Atmosphere (hpa)": 0.0,
    "Relative humidity (%)": 0.0,
    "Power (MW)": 1.667333
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:45:00.000",
    "Wind speed at height of 10 meters (m/s)": 0.0,
    "Wind direction at height of 10 meters (˚)": 0.0,
    "Wind speed at height of 30 meters (m/s)": 0.0,
    "Wind direction at height of 30 meters (˚)": 0.0,
    "Wind speed at height of 50 meters (m/s)": 0.0,
    "Wind direction at height of 50 meters (˚)": 0.0,
    "Wind speed - at the height of wheel hub (m/s)": 3.746667,
    "Wind speed - at the height of wheel hub  (˚)": 31.666667,
    "Air temperature  (°C) ": 0.0,
    "Atmosphere (hpa)": 0.0,
    "Relative humidity (%)": 0.0,
    "Power (MW)": 2.062667
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T01:00:00.000",
    "Wind speed at height of 10 meters (m/s)": 0.0,
    "Wind direction at height of 10 meters (˚)": 0.0,
    "Wind speed at height of 30 meters (m/s)": 0.0,
    "Wind direction at height of 30 meters (˚)": 0.0,
    "Wind speed at height of 50 meters (m/s)": 0.0,
    "Wind direction at height of 50 meters (˚)": 0.0,
    "Wind speed - at the height of wheel hub (m/s)": 3.613333,
    "Wind speed - at the height of wheel hub  (˚)": 215.8,
    "Air temperature  (°C) ": 0.0,
    "Atmosphere (hpa)": 0.0,
    "Relative humidity (%)": 0.0,
    "Power (MW)": 1.798667
  }
]
```

### data_original.rar!data_original/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx [2019]

| Exact column | dtype | Missing | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | object | 0 | — | — | — | — |
| "Wind speed at height of 10 meters (m/s)" | float64 | 0 | -99.0 | 15.28 | 4.84703716370269 | 4.91 |
| "Wind direction at height of 10 meters (˚)" | float64 | 0 | -99.0 | 359.95 | 99.58784940720474 | 46.0 |
| "Wind speed at height of 30 meters (m/s)" | float64 | 0 | -99.0 | 19.71 | 6.418972155722754 | 6.48 |
| "Wind direction at height of 30 meters (˚)" | float64 | 0 | -99.0 | 359.99 | 70.85869186046513 | 35.165 |
| "Wind speed at height of 50 meters (m/s)" | float64 | 0 | -99.0 | 21.81 | 7.237500427496579 | 7.34 |
| "Wind direction at height of 50 meters (˚)" | float64 | 0 | -99.0 | 360.0 | 87.26178707820337 | 38.98 |
| "Wind speed - at the height of wheel hub  (m/s)" | float64 | 0 | -99.0 | 23.82 | 7.945254502963976 | 8.08 |
| "Wind speed - at the height of wheel hub  (˚)" | float64 | 0 | -99.0 | 360.0 | 93.60504830711356 | 44.98 |
| "Air temperature  (°C) " | float64 | 0 | 0.0 | 37.13 | 21.15334159826721 | 21.41 |
| "Atmosphere (hpa)" | float64 | 0 | 0.0 | 1090.24 | 1087.9934342225263 | 1088.25 |
| "Relative humidity (%)" | float64 | 0 | 0.0 | 99.38 | 78.63453203374372 | 79.82 |
| "Power (MW)" | float64 | 0 | -99.0 | 114.36 | 28.720571463178295 | 20.0395 |

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:00:00.000",
    "Wind speed at height of 10 meters (m/s)": 9.95,
    "Wind direction at height of 10 meters (˚)": 33.54,
    "Wind speed at height of 30 meters (m/s)": 12.35,
    "Wind direction at height of 30 meters (˚)": 31.01,
    "Wind speed at height of 50 meters (m/s)": 14.18,
    "Wind direction at height of 50 meters (˚)": 26.39,
    "Wind speed - at the height of wheel hub  (m/s)": 15.37,
    "Wind speed - at the height of wheel hub  (˚)": 31.64,
    "Air temperature  (°C) ": 10.57,
    "Atmosphere (hpa)": 1089.58,
    "Relative humidity (%)": 80.05,
    "Power (MW)": 93.186
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:15:00.000",
    "Wind speed at height of 10 meters (m/s)": 9.95,
    "Wind direction at height of 10 meters (˚)": 33.54,
    "Wind speed at height of 30 meters (m/s)": 12.35,
    "Wind direction at height of 30 meters (˚)": 31.01,
    "Wind speed at height of 50 meters (m/s)": 14.18,
    "Wind direction at height of 50 meters (˚)": 26.39,
    "Wind speed - at the height of wheel hub  (m/s)": 15.37,
    "Wind speed - at the height of wheel hub  (˚)": 31.64,
    "Air temperature  (°C) ": 10.57,
    "Atmosphere (hpa)": 1089.58,
    "Relative humidity (%)": 80.05,
    "Power (MW)": 93.628
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:30:00.000",
    "Wind speed at height of 10 meters (m/s)": 9.95,
    "Wind direction at height of 10 meters (˚)": 33.54,
    "Wind speed at height of 30 meters (m/s)": 12.35,
    "Wind direction at height of 30 meters (˚)": 31.01,
    "Wind speed at height of 50 meters (m/s)": 14.18,
    "Wind direction at height of 50 meters (˚)": 26.39,
    "Wind speed - at the height of wheel hub  (m/s)": 15.37,
    "Wind speed - at the height of wheel hub  (˚)": 31.64,
    "Air temperature  (°C) ": 10.57,
    "Atmosphere (hpa)": 1089.58,
    "Relative humidity (%)": 80.05,
    "Power (MW)": 93.53
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:45:00.000",
    "Wind speed at height of 10 meters (m/s)": 9.95,
    "Wind direction at height of 10 meters (˚)": 33.54,
    "Wind speed at height of 30 meters (m/s)": 12.35,
    "Wind direction at height of 30 meters (˚)": 31.01,
    "Wind speed at height of 50 meters (m/s)": 14.18,
    "Wind direction at height of 50 meters (˚)": 26.39,
    "Wind speed - at the height of wheel hub  (m/s)": 15.37,
    "Wind speed - at the height of wheel hub  (˚)": 31.64,
    "Air temperature  (°C) ": 10.57,
    "Atmosphere (hpa)": 1089.58,
    "Relative humidity (%)": 80.05,
    "Power (MW)": 87.713
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T01:00:00.000",
    "Wind speed at height of 10 meters (m/s)": 9.92,
    "Wind direction at height of 10 meters (˚)": 35.69,
    "Wind speed at height of 30 meters (m/s)": 12.4,
    "Wind direction at height of 30 meters (˚)": 30.45,
    "Wind speed at height of 50 meters (m/s)": 14.2,
    "Wind direction at height of 50 meters (˚)": 28.83,
    "Wind speed - at the height of wheel hub  (m/s)": 15.46,
    "Wind speed - at the height of wheel hub  (˚)": 33.56,
    "Air temperature  (°C) ": 10.58,
    "Atmosphere (hpa)": 1089.58,
    "Relative humidity (%)": 78.75,
    "Power (MW)": 92.794
  }
]
```

### data_processed.rar!data_processed/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx [sheet1]

| Exact column | dtype | Missing | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | object | 0 | — | — | — | — |
| "Wind speed at height of 10 meters (m/s)" | float64 | 0 | 0.0 | 25.465 | 5.711011200410397 | 5.389 |
| "Wind direction at height of 10 meters (˚)" | float64 | 0 | 0.0 | 358.987 | 222.8297476487688 | 235.987 |
| "Wind speed at height of 30 meters (m/s)" | float64 | 0 | 0.0 | 29.187 | 6.0392548307113545 | 5.783 |
| "Wind direction at height of 30 meters (˚)" | float64 | 0 | 0.0 | 359.087 | 220.63395717909256 | 245.442 |
| "Wind speed at height of 50 meters (m/s)" | float64 | 0 | 0.0 | 29.678 | 6.168762668148655 | 5.811 |
| "Wind direction at height of 50 meters (˚)" | float64 | 0 | 0.0 | 358.933 | 221.86820313212493 | 251.833 |
| "Wind speed - at the height of wheel hub (m/s)" | float64 | 0 | 0.0 | 30.247 | 6.375875669744642 | 5.8795 |
| "Wind speed - at the height of wheel hub (˚)" | float64 | 0 | 0.0 | 358.5 | 216.98622360921112 | 248.825 |
| "Air temperature  (°C) " | float64 | 0 | -24.131 | 36.13 | 8.54332404240766 | 9.823 |
| "Atmosphere (hpa)" | float64 | 0 | 858.4 | 918.192 | 889.5274691062473 | 889.742 |
| "Relative humidity (%)" | float64 | 0 | 1.502 | 93.12 | 37.58114265560876 | 34.4015 |
| "Power (MW)" | float64 | 0 | 0.0 | 98.09444 | 23.426896034420597 | 14.9577835 |

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:00:00",
    "Wind speed at height of 10 meters (m/s)": 2.209,
    "Wind direction at height of 10 meters (˚)": 81.317,
    "Wind speed at height of 30 meters (m/s)": 1.991,
    "Wind direction at height of 30 meters (˚)": 74.814,
    "Wind speed at height of 50 meters (m/s)": 2.094,
    "Wind direction at height of 50 meters (˚)": 77.667,
    "Wind speed - at the height of wheel hub (m/s)": 2.494,
    "Wind speed - at the height of wheel hub (˚)": 74.5,
    "Air temperature  (°C) ": -13.484,
    "Atmosphere (hpa)": 889.867,
    "Relative humidity (%)": 76.32,
    "Power (MW)": 0.254383
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:15:00",
    "Wind speed at height of 10 meters (m/s)": 1.828,
    "Wind direction at height of 10 meters (˚)": 77.46,
    "Wind speed at height of 30 meters (m/s)": 1.698,
    "Wind direction at height of 30 meters (˚)": 75.048,
    "Wind speed at height of 50 meters (m/s)": 1.757,
    "Wind direction at height of 50 meters (˚)": 88.733,
    "Wind speed - at the height of wheel hub (m/s)": 1.882,
    "Wind speed - at the height of wheel hub (˚)": 74.367,
    "Air temperature  (°C) ": -13.691,
    "Atmosphere (hpa)": 889.575,
    "Relative humidity (%)": 76.757,
    "Power (MW)": 0.329703
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:30:00",
    "Wind speed at height of 10 meters (m/s)": 2.193,
    "Wind direction at height of 10 meters (˚)": 86.7,
    "Wind speed at height of 30 meters (m/s)": 2.313,
    "Wind direction at height of 30 meters (˚)": 84.688,
    "Wind speed at height of 50 meters (m/s)": 2.344,
    "Wind direction at height of 50 meters (˚)": 89.1,
    "Wind speed - at the height of wheel hub (m/s)": 2.35,
    "Wind speed - at the height of wheel hub (˚)": 89.0,
    "Air temperature  (°C) ": -13.766,
    "Atmosphere (hpa)": 889.942,
    "Relative humidity (%)": 76.981,
    "Power (MW)": 0.296306
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:45:00",
    "Wind speed at height of 10 meters (m/s)": 2.654,
    "Wind direction at height of 10 meters (˚)": 78.16,
    "Wind speed at height of 30 meters (m/s)": 2.494,
    "Wind direction at height of 30 meters (˚)": 74.939,
    "Wind speed at height of 50 meters (m/s)": 2.574,
    "Wind direction at height of 50 meters (˚)": 87.267,
    "Wind speed - at the height of wheel hub (m/s)": 2.808,
    "Wind speed - at the height of wheel hub (˚)": 82.733,
    "Air temperature  (°C) ": -13.691,
    "Atmosphere (hpa)": 889.675,
    "Relative humidity (%)": 76.821,
    "Power (MW)": 0.18759
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01 01:00:00",
    "Wind speed at height of 10 meters (m/s)": 2.249,
    "Wind direction at height of 10 meters (˚)": 94.297,
    "Wind speed at height of 30 meters (m/s)": 2.192,
    "Wind direction at height of 30 meters (˚)": 91.14,
    "Wind speed at height of 50 meters (m/s)": 2.558,
    "Wind direction at height of 50 meters (˚)": 96.9,
    "Wind speed - at the height of wheel hub (m/s)": 2.924,
    "Wind speed - at the height of wheel hub (˚)": 92.967,
    "Air temperature  (°C) ": -13.447,
    "Atmosphere (hpa)": 890.025,
    "Relative humidity (%)": 74.571,
    "Power (MW)": 0.081005
  }
]
```

### data_processed.rar!data_processed/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx [sheet1]

| Exact column | dtype | Missing | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | object | 0 | — | — | — | — |
| "Wind speed at height of 10 meters (m/s)" | float64 | 0 | 0.0 | 23.3 | 6.325568328203374 | 6.47 |
| "Wind direction at height of 10 meters (˚)" | float64 | 0 | 0.008 | 359.916 | 218.59844428294574 | 250.56400000000002 |
| "Wind speed at height of 30 meters (m/s)" | float64 | 0 | 0.0 | 27.125 | 7.160942644208847 | 7.337 |
| "Wind direction at height of 30 meters (˚)" | float64 | 0 | 0.0 | 360.0 | 217.54665824498406 | 266.41200000000003 |
| "Wind speed at height of 50 meters (m/s)" | float64 | 0 | 0.0 | 28.196 | 7.40004628362973 | 7.541 |
| "Wind direction at height of 50 meters (˚)" | float64 | 0 | 0.009 | 359.889 | 209.72360825638395 | 257.695 |
| "Wind speed - at the height of wheel hub  (m/s)" | float64 | 0 | 0.0 | 28.808 | 7.5581647999316015 | 7.683 |
| "Wind speed - at the height of wheel hub (˚)" | float64 | 0 | 0.063 | 359.802 | 207.7480264335385 | 244.942 |
| "Air temperature  (°C) " | float64 | 0 | -24.547 | 37.59 | 8.665842652758778 | 10.2935 |
| "Atmosphere (hpa)" | float64 | 0 | 441.272 | 900.45 | 883.2223220189238 | 884.053 |
| "Power (MW)" | float64 | 0 | 0.0 | 201.24808 | 72.70527905794005 | 75.401173 |

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:00:00",
    "Wind speed at height of 10 meters (m/s)": 2.951,
    "Wind direction at height of 10 meters (˚)": 124.685,
    "Wind speed at height of 30 meters (m/s)": 4.634,
    "Wind direction at height of 30 meters (˚)": 114.568,
    "Wind speed at height of 50 meters (m/s)": 3.869,
    "Wind direction at height of 50 meters (˚)": 102.139,
    "Wind speed - at the height of wheel hub  (m/s)": 2.645,
    "Wind speed - at the height of wheel hub (˚)": 103.023,
    "Air temperature  (°C) ": -12.735,
    "Atmosphere (hpa)": 887.187,
    "Power (MW)": 33.451336
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:15:00",
    "Wind speed at height of 10 meters (m/s)": 2.951,
    "Wind direction at height of 10 meters (˚)": 129.697,
    "Wind speed at height of 30 meters (m/s)": 2.951,
    "Wind direction at height of 30 meters (˚)": 118.488,
    "Wind speed at height of 50 meters (m/s)": 2.951,
    "Wind direction at height of 50 meters (˚)": 97.463,
    "Wind speed - at the height of wheel hub  (m/s)": 2.186,
    "Wind speed - at the height of wheel hub (˚)": 108.914,
    "Air temperature  (°C) ": -12.992,
    "Atmosphere (hpa)": 887.227,
    "Power (MW)": 36.811337
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:30:00",
    "Wind speed at height of 10 meters (m/s)": 2.951,
    "Wind direction at height of 10 meters (˚)": 124.756,
    "Wind speed at height of 30 meters (m/s)": 3.563,
    "Wind direction at height of 30 meters (˚)": 118.21,
    "Wind speed at height of 50 meters (m/s)": 2.798,
    "Wind direction at height of 50 meters (˚)": 91.528,
    "Wind speed - at the height of wheel hub  (m/s)": 2.492,
    "Wind speed - at the height of wheel hub (˚)": 97.322,
    "Air temperature  (°C) ": -12.745,
    "Atmosphere (hpa)": 887.094,
    "Power (MW)": 31.172535
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:45:00",
    "Wind speed at height of 10 meters (m/s)": 2.186,
    "Wind direction at height of 10 meters (˚)": 129.019,
    "Wind speed at height of 30 meters (m/s)": 2.339,
    "Wind direction at height of 30 meters (˚)": 112.761,
    "Wind speed at height of 50 meters (m/s)": 2.339,
    "Wind direction at height of 50 meters (˚)": 94.015,
    "Wind speed - at the height of wheel hub  (m/s)": 1.281,
    "Wind speed - at the height of wheel hub (˚)": 99.393,
    "Air temperature  (°C) ": -12.904,
    "Atmosphere (hpa)": 887.214,
    "Power (MW)": 27.836002
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01 01:00:00",
    "Wind speed at height of 10 meters (m/s)": 2.033,
    "Wind direction at height of 10 meters (˚)": 121.358,
    "Wind speed at height of 30 meters (m/s)": 1.88,
    "Wind direction at height of 30 meters (˚)": 105.626,
    "Wind speed at height of 50 meters (m/s)": 2.186,
    "Wind direction at height of 50 meters (˚)": 99.392,
    "Wind speed - at the height of wheel hub  (m/s)": 2.186,
    "Wind speed - at the height of wheel hub (˚)": 95.703,
    "Air temperature  (°C) ": -12.979,
    "Atmosphere (hpa)": 887.227,
    "Power (MW)": 31.192802
  }
]
```

### data_processed.rar!data_processed/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx [sheet1]

| Exact column | dtype | Missing | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | datetime64[ns] | 0 | — | — | — | — |
| "Wind speed at height of 10 meters (m/s)" | float64 | 0 | 0.0 | 27.926 | 3.589178511613657 | 3.15867 |
| "Wind direction at height of 10 meters (˚)" | float64 | 0 | 0.0 | 360.0 | 148.32922873416837 | 148.338 |
| "Wind speed at height of 30 meters (m/s)" | float64 | 0 | 0.0 | 22.0917 | 5.381621369841541 | 4.957 |
| "Wind direction at height of 30 meters (˚)" | float64 | 0 | 0.00287437 | 360.0 | 145.12780228772002 | 162.332 |
| "Wind speed at height of 50 meters (m/s)" | float64 | 0 | 0.0 | 21.836 | 4.932601727342681 | 4.573 |
| "Wind direction at height of 50 meters (˚)" | float64 | 0 | 0.0 | 360.0 | 143.01903383895348 | 149.5605 |
| "Wind speed - at the height of wheel hub (m/s)" | float64 | 0 | 0.0 | 36.9203 | 4.03872203125 | 3.855 |
| "Wind speed - at the height of wheel hub (˚)" | float64 | 0 | 0.0 | 360.0 | 179.94851276210525 | 165.647 |
| "Air temperature  (°C) " | float64 | 0 | -14.27 | 36.32 | 17.51121290754674 | 20.5 |
| "Atmosphere (hpa)" | float64 | 0 | 950.958 | 990.731 | 971.7870240538074 | 971.877 |
| "Relative humidity (%)" | float64 | 0 | 3.43656 | 100.0 | 58.809448883663926 | 57.142849999999996 |
| "Power (MW)" | float64 | 0 | -0.668767 | 94.2666 | 18.167233450459758 | 8.39469 |

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:00:00.000",
    "Wind speed at height of 10 meters (m/s)": 2.32218,
    "Wind direction at height of 10 meters (˚)": 317.431,
    "Wind speed at height of 30 meters (m/s)": 2.59042,
    "Wind direction at height of 30 meters (˚)": 312.468,
    "Wind speed at height of 50 meters (m/s)": 1.62735,
    "Wind direction at height of 50 meters (˚)": 351.117,
    "Wind speed - at the height of wheel hub (m/s)": 2.34887,
    "Wind speed - at the height of wheel hub (˚)": 313.33,
    "Air temperature  (°C) ": 26.46,
    "Atmosphere (hpa)": 984.37,
    "Relative humidity (%)": 31.7949,
    "Power (MW)": -0.36579
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:15:00.000",
    "Wind speed at height of 10 meters (m/s)": 2.32218,
    "Wind direction at height of 10 meters (˚)": 317.431,
    "Wind speed at height of 30 meters (m/s)": 2.59042,
    "Wind direction at height of 30 meters (˚)": 312.468,
    "Wind speed at height of 50 meters (m/s)": 1.62735,
    "Wind direction at height of 50 meters (˚)": 351.117,
    "Wind speed - at the height of wheel hub (m/s)": 2.34887,
    "Wind speed - at the height of wheel hub (˚)": 313.33,
    "Air temperature  (°C) ": 26.46,
    "Atmosphere (hpa)": 984.37,
    "Relative humidity (%)": 31.7949,
    "Power (MW)": -0.376874
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:30:00.000",
    "Wind speed at height of 10 meters (m/s)": 2.32218,
    "Wind direction at height of 10 meters (˚)": 317.431,
    "Wind speed at height of 30 meters (m/s)": 2.59042,
    "Wind direction at height of 30 meters (˚)": 312.468,
    "Wind speed at height of 50 meters (m/s)": 1.62735,
    "Wind direction at height of 50 meters (˚)": 351.117,
    "Wind speed - at the height of wheel hub (m/s)": 2.34887,
    "Wind speed - at the height of wheel hub (˚)": 313.33,
    "Air temperature  (°C) ": 26.46,
    "Atmosphere (hpa)": 984.37,
    "Relative humidity (%)": 31.7949,
    "Power (MW)": -0.387959
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:45:00.000",
    "Wind speed at height of 10 meters (m/s)": 2.32218,
    "Wind direction at height of 10 meters (˚)": 317.431,
    "Wind speed at height of 30 meters (m/s)": 2.59042,
    "Wind direction at height of 30 meters (˚)": 312.468,
    "Wind speed at height of 50 meters (m/s)": 1.62735,
    "Wind direction at height of 50 meters (˚)": 351.117,
    "Wind speed - at the height of wheel hub (m/s)": 2.34887,
    "Wind speed - at the height of wheel hub (˚)": 313.33,
    "Air temperature  (°C) ": 26.46,
    "Atmosphere (hpa)": 984.37,
    "Relative humidity (%)": 31.7949,
    "Power (MW)": -0.395348
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T01:00:00.000",
    "Wind speed at height of 10 meters (m/s)": 2.32218,
    "Wind direction at height of 10 meters (˚)": 317.431,
    "Wind speed at height of 30 meters (m/s)": 2.59042,
    "Wind direction at height of 30 meters (˚)": 312.468,
    "Wind speed at height of 50 meters (m/s)": 1.62735,
    "Wind direction at height of 50 meters (˚)": 351.117,
    "Wind speed - at the height of wheel hub (m/s)": 2.34887,
    "Wind speed - at the height of wheel hub (˚)": 313.33,
    "Air temperature  (°C) ": 26.46,
    "Atmosphere (hpa)": 984.37,
    "Relative humidity (%)": 31.7949,
    "Power (MW)": -0.384264
  }
]
```

### data_processed.rar!data_processed/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx [sheet1]

| Exact column | dtype | Missing | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | datetime64[ns] | 0 | — | — | — | — |
| "Wind speed at height of 10 meters (m/s)" | float64 | 0 | 0.0 | 17.744 | 3.7674629150136796 | 3.253333 |
| "Wind direction at height of 10 meters (˚)" | float64 | 0 | 0.0 | 356.6 | 193.49220590981244 | 176.4523335 |
| "Wind speed at height of 30 meters (m/s)" | float64 | 0 | 0.0 | 20.406667 | 4.1982068461297315 | 3.66 |
| "Wind direction at height of 30 meters (˚)" | float64 | 0 | 0.0 | 357.0 | 205.46494762832023 | 189.8733335 |
| "Wind speed at height of 50 meters (m/s)" | float64 | 0 | 0.0 | 30.819333 | 5.3549054021460325 | 4.462667 |
| "Wind direction at height of 50 meters (˚)" | float64 | 0 | 0.0 | 356.9 | 149.66902855047312 | 163.5206665 |
| "Wind speed - at the height of wheel hub (m/s)" | float64 | 0 | 0.0 | 31.086 | 5.516342413047196 | 4.623333 |
| "Wind speed - at the height of wheel hub  (˚)" | float64 | 0 | 0.0 | 356.8 | 147.29036018125856 | 151.221 |
| "Air temperature  (°C) " | float64 | 0 | -3.82 | 35.253333 | 13.766049991948817 | 14.151 |
| "Atmosphere (hpa)" | float64 | 0 | 472.533333 | 902.0 | 886.8190209059792 | 887.0 |
| "Relative humidity (%)" | float64 | 0 | 8.219333 | 100.0 | 80.76512392409084 | 85.666667 |
| "Power (MW)" | float64 | 0 | 0.0 | 64.614 | 17.37090403846044 | 7.3563335 |

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:00:00.000",
    "Wind speed at height of 10 meters (m/s)": 4.41,
    "Wind direction at height of 10 meters (˚)": 19.81,
    "Wind speed at height of 30 meters (m/s)": 5.07,
    "Wind direction at height of 30 meters (˚)": 21.76,
    "Wind speed at height of 50 meters (m/s)": 7.52,
    "Wind direction at height of 50 meters (˚)": 179.1,
    "Wind speed - at the height of wheel hub (m/s)": 0.0,
    "Wind speed - at the height of wheel hub  (˚)": 209.2,
    "Air temperature  (°C) ": -2.25,
    "Atmosphere (hpa)": 898.0,
    "Relative humidity (%)": 100.0,
    "Power (MW)": 15.806
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:15:00.000",
    "Wind speed at height of 10 meters (m/s)": 4.4,
    "Wind direction at height of 10 meters (˚)": 19.79,
    "Wind speed at height of 30 meters (m/s)": 5.063333,
    "Wind direction at height of 30 meters (˚)": 21.75,
    "Wind speed at height of 50 meters (m/s)": 7.293333,
    "Wind direction at height of 50 meters (˚)": 179.1,
    "Wind speed - at the height of wheel hub (m/s)": 0.0,
    "Wind speed - at the height of wheel hub  (˚)": 209.2,
    "Air temperature  (°C) ": -2.24,
    "Atmosphere (hpa)": 898.0,
    "Relative humidity (%)": 100.0,
    "Power (MW)": 16.699333
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:30:00.000",
    "Wind speed at height of 10 meters (m/s)": 4.833333,
    "Wind direction at height of 10 meters (˚)": 19.79,
    "Wind speed at height of 30 meters (m/s)": 5.563333,
    "Wind direction at height of 30 meters (˚)": 21.75,
    "Wind speed at height of 50 meters (m/s)": 7.566667,
    "Wind direction at height of 50 meters (˚)": 179.1,
    "Wind speed - at the height of wheel hub (m/s)": 0.0,
    "Wind speed - at the height of wheel hub  (˚)": 209.2,
    "Air temperature  (°C) ": -2.24,
    "Atmosphere (hpa)": 898.0,
    "Relative humidity (%)": 100.0,
    "Power (MW)": 15.840667
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:45:00.000",
    "Wind speed at height of 10 meters (m/s)": 4.78,
    "Wind direction at height of 10 meters (˚)": 19.79,
    "Wind speed at height of 30 meters (m/s)": 5.5,
    "Wind direction at height of 30 meters (˚)": 21.75,
    "Wind speed at height of 50 meters (m/s)": 7.6,
    "Wind direction at height of 50 meters (˚)": 179.1,
    "Wind speed - at the height of wheel hub (m/s)": 0.0,
    "Wind speed - at the height of wheel hub  (˚)": 209.2,
    "Air temperature  (°C) ": -2.29,
    "Atmosphere (hpa)": 898.0,
    "Relative humidity (%)": 100.0,
    "Power (MW)": 14.887333
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T01:00:00.000",
    "Wind speed at height of 10 meters (m/s)": 4.34,
    "Wind direction at height of 10 meters (˚)": 19.79,
    "Wind speed at height of 30 meters (m/s)": 5.0,
    "Wind direction at height of 30 meters (˚)": 21.75,
    "Wind speed at height of 50 meters (m/s)": 7.12,
    "Wind direction at height of 50 meters (˚)": 179.1,
    "Wind speed - at the height of wheel hub (m/s)": 0.0,
    "Wind speed - at the height of wheel hub  (˚)": 209.2,
    "Air temperature  (°C) ": -2.343333,
    "Atmosphere (hpa)": 898.0,
    "Relative humidity (%)": 100.0,
    "Power (MW)": 14.865333
  }
]
```

### data_processed.rar!data_processed/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx [sheet 1]

| Exact column | dtype | Missing | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | datetime64[ns] | 0 | — | — | — | — |
| "Wind speed at height of 10 meters (m/s)" | float64 | 580 | -0.9 | 31.873333 | 0.1957435958930552 | 0.0 |
| "Wind direction at height of 10 meters (˚)" | float64 | 580 | -0.9 | 357.0 | 160.2498530185828 | 151.36 |
| "Wind speed at height of 30 meters (m/s)" | float64 | 580 | -0.9 | 40.646667 | 0.30783577087684927 | 0.0 |
| "Wind direction at height of 30 meters (˚)" | float64 | 580 | -0.9 | 356.933333 | 118.65005196777537 | 86.046667 |
| "Wind speed at height of 50 meters (m/s)" | float64 | 580 | -0.9 | 24.046667 | 4.216657075430358 | 3.966667 |
| "Wind direction at height of 50 meters (˚)" | float64 | 580 | -0.9 | 356.9 | 107.03132758756249 | 70.933333 |
| "Wind speed - at the height of wheel hub (m/s)" | float64 | 0 | 0.0 | 26.166667 | 4.686263680575437 | 3.953333 |
| "Wind speed - at the height of wheel hub  (˚)" | float64 | 0 | 0.0 | 358.6 | 184.88929402237176 | 191.0 |
| "Air temperature  (°C) " | float64 | 580 | -9.92 | 35.753333 | 13.597133209835492 | 14.2 |
| "Power (MW)" | float64 | 0 | 0.0 | 35.350667 | 6.68418598809983 | 1.717 |

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01T11:00:00.000",
    "Wind speed at height of 10 meters (m/s)": 0.0,
    "Wind direction at height of 10 meters (˚)": 81.28,
    "Wind speed at height of 30 meters (m/s)": 0.0,
    "Wind direction at height of 30 meters (˚)": 26.56,
    "Wind speed at height of 50 meters (m/s)": 0.0,
    "Wind direction at height of 50 meters (˚)": 26.906667,
    "Wind speed - at the height of wheel hub (m/s)": 4.606667,
    "Wind speed - at the height of wheel hub  (˚)": 28.666667,
    "Air temperature  (°C) ": -0.04,
    "Power (MW)": 2.669333
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T11:15:00.000",
    "Wind speed at height of 10 meters (m/s)": 0.0,
    "Wind direction at height of 10 meters (˚)": 304.793333,
    "Wind speed at height of 30 meters (m/s)": 0.0,
    "Wind direction at height of 30 meters (˚)": 99.6,
    "Wind speed at height of 50 meters (m/s)": 0.0,
    "Wind direction at height of 50 meters (˚)": 100.9,
    "Wind speed - at the height of wheel hub (m/s)": 4.133333,
    "Wind speed - at the height of wheel hub  (˚)": 30.0,
    "Air temperature  (°C) ": -0.12,
    "Power (MW)": 1.947333
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T11:30:00.000",
    "Wind speed at height of 10 meters (m/s)": 0.08,
    "Wind direction at height of 10 meters (˚)": 302.153333,
    "Wind speed at height of 30 meters (m/s)": 0.0,
    "Wind direction at height of 30 meters (˚)": 99.533333,
    "Wind speed at height of 50 meters (m/s)": 0.0,
    "Wind direction at height of 50 meters (˚)": 100.9,
    "Wind speed - at the height of wheel hub (m/s)": 3.946667,
    "Wind speed - at the height of wheel hub  (˚)": 12.266667,
    "Air temperature  (°C) ": -0.046667,
    "Power (MW)": 1.163333
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T11:45:00.000",
    "Wind speed at height of 10 meters (m/s)": 0.613333,
    "Wind direction at height of 10 meters (˚)": 282.586667,
    "Wind speed at height of 30 meters (m/s)": 0.0,
    "Wind direction at height of 30 meters (˚)": 99.5,
    "Wind speed at height of 50 meters (m/s)": 0.0,
    "Wind direction at height of 50 meters (˚)": 100.9,
    "Wind speed - at the height of wheel hub (m/s)": 4.073333,
    "Wind speed - at the height of wheel hub  (˚)": 56.466667,
    "Air temperature  (°C) ": 0.233333,
    "Power (MW)": 0.756667
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T12:00:00.000",
    "Wind speed at height of 10 meters (m/s)": 0.32,
    "Wind direction at height of 10 meters (˚)": 274.606667,
    "Wind speed at height of 30 meters (m/s)": 0.0,
    "Wind direction at height of 30 meters (˚)": 99.54,
    "Wind speed at height of 50 meters (m/s)": 0.0,
    "Wind direction at height of 50 meters (˚)": 100.9,
    "Wind speed - at the height of wheel hub (m/s)": 4.0,
    "Wind speed - at the height of wheel hub  (˚)": 53.6,
    "Air temperature  (°C) ": 0.5,
    "Power (MW)": 0.928
  }
]
```

### data_processed.rar!data_processed/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx [2019]

| Exact column | dtype | Missing | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | object | 0 | — | — | — | — |
| "Wind speed at height of 10 meters (m/s)" | float64 | 0 | 0.0 | 15.28 | 5.040179263565891 | 4.91 |
| "Wind direction at height of 10 meters (˚)" | float64 | 0 | 0.0 | 359.95 | 100.12131939694484 | 46.12 |
| "Wind speed at height of 30 meters (m/s)" | float64 | 0 | 0.0 | 19.71 | 6.615397144322845 | 6.49 |
| "Wind direction at height of 30 meters (˚)" | float64 | 0 | 0.0 | 359.99 | 71.30592567259463 | 35.27 |
| "Wind speed at height of 50 meters (m/s)" | float64 | 0 | 0.0 | 21.81 | 7.436062471500228 | 7.35 |
| "Wind direction at height of 50 meters (˚)" | float64 | 0 | 0.0 | 360.0 | 87.77847554719563 | 39.07 |
| "Wind speed - at the height of wheel hub (m/s)" | float64 | 0 | 0.0 | 23.82 | 8.14519080597355 | 8.09 |
| "Wind speed - at the height of wheel hub (˚)" | float64 | 0 | 0.0 | 360.0 | 94.14524367305062 | 44.98 |
| "Air temperature  (°C) " | float64 | 0 | 0.0 | 37.13 | 21.157727998176014 | 21.415 |
| "Atmosphere (hpa)" | float64 | 0 | 0.0 | 1090.24 | 1088.1639395234838 | 1088.25 |
| "Relative humidity (%)" | float64 | 0 | 0.0 | 99.38 | 78.64908358983128 | 79.82 |
| "Power (MW)" | float64 | 0 | -1.316 | 114.36 | 28.761022172822617 | 20.046 |

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:00:00.000",
    "Wind speed at height of 10 meters (m/s)": 9.95,
    "Wind direction at height of 10 meters (˚)": 33.54,
    "Wind speed at height of 30 meters (m/s)": 12.35,
    "Wind direction at height of 30 meters (˚)": 31.01,
    "Wind speed at height of 50 meters (m/s)": 14.18,
    "Wind direction at height of 50 meters (˚)": 26.39,
    "Wind speed - at the height of wheel hub (m/s)": 15.37,
    "Wind speed - at the height of wheel hub (˚)": 31.64,
    "Air temperature  (°C) ": 10.57,
    "Atmosphere (hpa)": 1089.58,
    "Relative humidity (%)": 80.05,
    "Power (MW)": 93.186
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:15:00.000",
    "Wind speed at height of 10 meters (m/s)": 9.95,
    "Wind direction at height of 10 meters (˚)": 33.54,
    "Wind speed at height of 30 meters (m/s)": 12.35,
    "Wind direction at height of 30 meters (˚)": 31.01,
    "Wind speed at height of 50 meters (m/s)": 14.18,
    "Wind direction at height of 50 meters (˚)": 26.39,
    "Wind speed - at the height of wheel hub (m/s)": 15.37,
    "Wind speed - at the height of wheel hub (˚)": 31.64,
    "Air temperature  (°C) ": 10.57,
    "Atmosphere (hpa)": 1089.58,
    "Relative humidity (%)": 80.05,
    "Power (MW)": 93.628
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:30:00.000",
    "Wind speed at height of 10 meters (m/s)": 9.95,
    "Wind direction at height of 10 meters (˚)": 33.54,
    "Wind speed at height of 30 meters (m/s)": 12.35,
    "Wind direction at height of 30 meters (˚)": 31.01,
    "Wind speed at height of 50 meters (m/s)": 14.18,
    "Wind direction at height of 50 meters (˚)": 26.39,
    "Wind speed - at the height of wheel hub (m/s)": 15.37,
    "Wind speed - at the height of wheel hub (˚)": 31.64,
    "Air temperature  (°C) ": 10.57,
    "Atmosphere (hpa)": 1089.58,
    "Relative humidity (%)": 80.05,
    "Power (MW)": 93.53
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:45:00.000",
    "Wind speed at height of 10 meters (m/s)": 9.95,
    "Wind direction at height of 10 meters (˚)": 33.54,
    "Wind speed at height of 30 meters (m/s)": 12.35,
    "Wind direction at height of 30 meters (˚)": 31.01,
    "Wind speed at height of 50 meters (m/s)": 14.18,
    "Wind direction at height of 50 meters (˚)": 26.39,
    "Wind speed - at the height of wheel hub (m/s)": 15.37,
    "Wind speed - at the height of wheel hub (˚)": 31.64,
    "Air temperature  (°C) ": 10.57,
    "Atmosphere (hpa)": 1089.58,
    "Relative humidity (%)": 80.05,
    "Power (MW)": 87.713
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01T01:00:00.000",
    "Wind speed at height of 10 meters (m/s)": 9.92,
    "Wind direction at height of 10 meters (˚)": 35.69,
    "Wind speed at height of 30 meters (m/s)": 12.4,
    "Wind direction at height of 30 meters (˚)": 30.45,
    "Wind speed at height of 50 meters (m/s)": 14.2,
    "Wind direction at height of 50 meters (˚)": 28.83,
    "Wind speed - at the height of wheel hub (m/s)": 15.46,
    "Wind speed - at the height of wheel hub (˚)": 33.56,
    "Air temperature  (°C) ": 10.58,
    "Atmosphere (hpa)": 1089.58,
    "Relative humidity (%)": 78.75,
    "Power (MW)": 92.794
  }
]
```

### ml/data/raw/wind/Wind farm site 1 (Nominal capacity-99MW).xlsx [sheet1]

| Exact column | dtype | Missing | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | object | 0 | — | — | — | — |
| "Wind speed at height of 10 meters (m/s)" | float64 | 0 | -99.0 | 25.465 | 5.495283501481988 | 5.372 |
| "Wind direction at height of 10 meters (˚)" | float64 | 0 | -99.0 | 358.987 | 221.82965451151392 | 235.753 |
| "Wind speed at height of 30 meters (m/s)" | float64 | 0 | -99.0 | 29.187 | 5.820112189352486 | 5.76 |
| "Wind direction at height of 30 meters (˚)" | float64 | 0 | -99.0 | 359.087 | 219.6239449099407 | 245.19650000000001 |
| "Wind speed at height of 50 meters (m/s)" | float64 | 0 | -99.0 | 29.678 | 5.949485735864114 | 5.78 |
| "Wind direction at height of 50 meters (˚)" | float64 | 0 | -99.0 | 358.933 | 220.83160671739626 | 251.6 |
| "Wind speed - at the height of wheel hub(m/s)" | float64 | 0 | -99.0 | 30.247 | 6.1566923022115825 | 5.849 |
| "Wind speed - at the height of wheel hub (˚)" | float64 | 1 | -99.0 | 358.5 | 215.95179120769507 | 248.567 |
| "Air temperature  (°C) " | float64 | 0 | -99.0 | 36.13 | 8.31075534370725 | 9.733 |
| "Atmosphere (hpa)" | float64 | 0 | -99.0 | 918.192 | 886.4167509262426 | 889.742 |
| "Relative humidity (%)" | float64 | 0 | -99.0 | 93.12 | 37.260329072617424 | 34.309 |
| "Power (MW)" | float64 | 0 | 0.0 | 98.09444 | 23.40834716162933 | 14.939664 |

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:00:00",
    "Wind speed at height of 10 meters (m/s)": 2.209,
    "Wind direction at height of 10 meters (˚)": 81.317,
    "Wind speed at height of 30 meters (m/s)": 1.991,
    "Wind direction at height of 30 meters (˚)": 74.814,
    "Wind speed at height of 50 meters (m/s)": 2.094,
    "Wind direction at height of 50 meters (˚)": 77.667,
    "Wind speed - at the height of wheel hub(m/s)": 2.494,
    "Wind speed - at the height of wheel hub (˚)": 74.5,
    "Air temperature  (°C) ": -13.484,
    "Atmosphere (hpa)": 889.867,
    "Relative humidity (%)": 76.32,
    "Power (MW)": 0.254383
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:15:00",
    "Wind speed at height of 10 meters (m/s)": 1.828,
    "Wind direction at height of 10 meters (˚)": 77.46,
    "Wind speed at height of 30 meters (m/s)": 1.698,
    "Wind direction at height of 30 meters (˚)": 75.048,
    "Wind speed at height of 50 meters (m/s)": 1.757,
    "Wind direction at height of 50 meters (˚)": 88.733,
    "Wind speed - at the height of wheel hub(m/s)": 1.882,
    "Wind speed - at the height of wheel hub (˚)": 74.367,
    "Air temperature  (°C) ": -13.691,
    "Atmosphere (hpa)": 889.575,
    "Relative humidity (%)": 76.757,
    "Power (MW)": 0.329703
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:30:00",
    "Wind speed at height of 10 meters (m/s)": 2.193,
    "Wind direction at height of 10 meters (˚)": 86.7,
    "Wind speed at height of 30 meters (m/s)": 2.313,
    "Wind direction at height of 30 meters (˚)": 84.688,
    "Wind speed at height of 50 meters (m/s)": 2.344,
    "Wind direction at height of 50 meters (˚)": 89.1,
    "Wind speed - at the height of wheel hub(m/s)": 2.35,
    "Wind speed - at the height of wheel hub (˚)": null,
    "Air temperature  (°C) ": -13.766,
    "Atmosphere (hpa)": 889.942,
    "Relative humidity (%)": 76.981,
    "Power (MW)": 0.296306
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:45:00",
    "Wind speed at height of 10 meters (m/s)": 2.654,
    "Wind direction at height of 10 meters (˚)": 78.16,
    "Wind speed at height of 30 meters (m/s)": 2.494,
    "Wind direction at height of 30 meters (˚)": 74.939,
    "Wind speed at height of 50 meters (m/s)": 2.574,
    "Wind direction at height of 50 meters (˚)": 87.267,
    "Wind speed - at the height of wheel hub(m/s)": 2.808,
    "Wind speed - at the height of wheel hub (˚)": 82.733,
    "Air temperature  (°C) ": -13.691,
    "Atmosphere (hpa)": 889.675,
    "Relative humidity (%)": 76.821,
    "Power (MW)": 0.18759
  },
  {
    "Time(year-month-day h:m:s)": "2019-01-01 01:00:00",
    "Wind speed at height of 10 meters (m/s)": 2.249,
    "Wind direction at height of 10 meters (˚)": 94.297,
    "Wind speed at height of 30 meters (m/s)": 2.192,
    "Wind direction at height of 30 meters (˚)": 91.14,
    "Wind speed at height of 50 meters (m/s)": 2.558,
    "Wind direction at height of 50 meters (˚)": 96.9,
    "Wind speed - at the height of wheel hub(m/s)": 2.924,
    "Wind speed - at the height of wheel hub (˚)": 92.967,
    "Air temperature  (°C) ": -13.447,
    "Atmosphere (hpa)": 890.025,
    "Relative humidity (%)": 74.571,
    "Power (MW)": 0.081005
  }
]
```

## 5. Timestamp and Time-Series Analysis

**FACTS.** Parsing is diagnostic only. Frequency is calculated from sorted unique valid timestamps; it does not imply the original rows are ordered or gap-free. UTC in the diagnostic output is a comparison representation, not a verified source timezone.

### data_original.rar!data_original/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx [sheet1]

```json
{
  "Time(year-month-day h:m:s)": {
    "column": "Time(year-month-day h:m:s)",
    "status": "parsed diagnostic copy",
    "non_null": 70176,
    "parsed": 70176,
    "parse_failures": 0,
    "ambiguous_day_month_values": 0,
    "missing": 0,
    "earliest": "2019-01-01 00:00:00+00:00",
    "latest": "2020-12-31 23:45:00+00:00",
    "unique_timestamps": 70176,
    "duplicate_timestamps": 0,
    "ascending_valid_values": true,
    "descending_valid_values": false,
    "timezone": "not documented in values (naive)",
    "estimated_frequency": "0 days 00:15:00",
    "regular_unique_spacing": true,
    "interval_counts": {
      "0 days 00:15:00": 70175
    },
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values."
  }
}
```

### data_original.rar!data_original/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx [sheet1]

```json
{
  "Time(year-month-day h:m:s)": {
    "column": "Time(year-month-day h:m:s)",
    "status": "parsed diagnostic copy",
    "non_null": 70176,
    "parsed": 70176,
    "parse_failures": 0,
    "ambiguous_day_month_values": 0,
    "missing": 0,
    "earliest": "2019-01-01 00:00:00+00:00",
    "latest": "2020-12-31 23:45:00+00:00",
    "unique_timestamps": 70176,
    "duplicate_timestamps": 0,
    "ascending_valid_values": true,
    "descending_valid_values": false,
    "timezone": "not documented in values (naive)",
    "estimated_frequency": "0 days 00:15:00",
    "regular_unique_spacing": true,
    "interval_counts": {
      "0 days 00:15:00": 70175
    },
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values."
  }
}
```

### data_original.rar!data_original/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx [sheet1]

```json
{
  "Time(year-month-day h:m:s)": {
    "column": "Time(year-month-day h:m:s)",
    "status": "parsed diagnostic copy",
    "non_null": 70176,
    "parsed": 70176,
    "parse_failures": 0,
    "ambiguous_day_month_values": 0,
    "missing": 0,
    "earliest": "2019-01-01 00:00:00+00:00",
    "latest": "2020-12-31 23:45:00+00:00",
    "unique_timestamps": 70176,
    "duplicate_timestamps": 0,
    "ascending_valid_values": true,
    "descending_valid_values": false,
    "timezone": "not documented in values (naive)",
    "estimated_frequency": "0 days 00:15:00",
    "regular_unique_spacing": true,
    "interval_counts": {
      "0 days 00:15:00": 70175
    },
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values."
  }
}
```

### data_original.rar!data_original/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx [sheet1]

```json
{
  "Time(year-month-day h:m:s)": {
    "column": "Time(year-month-day h:m:s)",
    "status": "parsed diagnostic copy",
    "non_null": 70176,
    "parsed": 70176,
    "parse_failures": 0,
    "ambiguous_day_month_values": 0,
    "missing": 0,
    "earliest": "2019-01-01 00:00:00+00:00",
    "latest": "2020-12-31 23:45:00+00:00",
    "unique_timestamps": 70176,
    "duplicate_timestamps": 0,
    "ascending_valid_values": true,
    "descending_valid_values": false,
    "timezone": "not documented in values (naive)",
    "estimated_frequency": "0 days 00:15:00",
    "regular_unique_spacing": true,
    "interval_counts": {
      "0 days 00:15:00": 70175
    },
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values."
  }
}
```

### data_original.rar!data_original/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx [sheet 1]

```json
{
  "Time(year-month-day h:m:s)": {
    "column": "Time(year-month-day h:m:s)",
    "status": "parsed diagnostic copy",
    "non_null": 70176,
    "parsed": 70176,
    "parse_failures": 0,
    "ambiguous_day_month_values": 0,
    "missing": 0,
    "earliest": "2019-01-01 00:00:00+00:00",
    "latest": "2020-12-31 23:45:00+00:00",
    "unique_timestamps": 70176,
    "duplicate_timestamps": 0,
    "ascending_valid_values": true,
    "descending_valid_values": false,
    "timezone": "not documented in values (naive)",
    "estimated_frequency": "0 days 00:15:00",
    "regular_unique_spacing": true,
    "interval_counts": {
      "0 days 00:15:00": 70175
    },
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values."
  }
}
```

### data_original.rar!data_original/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx [2019]

```json
{
  "Time(year-month-day h:m:s)": {
    "column": "Time(year-month-day h:m:s)",
    "status": "parsed diagnostic copy",
    "non_null": 70176,
    "parsed": 70153,
    "parse_failures": 23,
    "ambiguous_day_month_values": 0,
    "missing": 0,
    "earliest": "2019-01-01 00:00:00+00:00",
    "latest": "2020-12-31 23:45:00+00:00",
    "unique_timestamps": 70150,
    "duplicate_timestamps": 3,
    "ascending_valid_values": false,
    "descending_valid_values": false,
    "timezone": "not documented in values (naive)",
    "estimated_frequency": "0 days 00:15:00",
    "regular_unique_spacing": false,
    "interval_counts": {
      "0 days 00:15:00": 70075,
      "0 days 00:30:00": 26,
      "0 days 00:16:00": 24,
      "0 days 00:14:00": 24
    },
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values."
  }
}
```

### data_processed.rar!data_processed/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx [sheet1]

```json
{
  "Time(year-month-day h:m:s)": {
    "column": "Time(year-month-day h:m:s)",
    "status": "parsed diagnostic copy",
    "non_null": 70176,
    "parsed": 70176,
    "parse_failures": 0,
    "ambiguous_day_month_values": 0,
    "missing": 0,
    "earliest": "2019-01-01 00:00:00+00:00",
    "latest": "2020-12-31 23:45:00+00:00",
    "unique_timestamps": 70176,
    "duplicate_timestamps": 0,
    "ascending_valid_values": true,
    "descending_valid_values": false,
    "timezone": "not documented in values (naive)",
    "estimated_frequency": "0 days 00:15:00",
    "regular_unique_spacing": true,
    "interval_counts": {
      "0 days 00:15:00": 70175
    },
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values."
  }
}
```

### data_processed.rar!data_processed/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx [sheet1]

```json
{
  "Time(year-month-day h:m:s)": {
    "column": "Time(year-month-day h:m:s)",
    "status": "parsed diagnostic copy",
    "non_null": 70176,
    "parsed": 70176,
    "parse_failures": 0,
    "ambiguous_day_month_values": 0,
    "missing": 0,
    "earliest": "2019-01-01 00:00:00+00:00",
    "latest": "2020-12-31 23:45:00+00:00",
    "unique_timestamps": 70176,
    "duplicate_timestamps": 0,
    "ascending_valid_values": true,
    "descending_valid_values": false,
    "timezone": "not documented in values (naive)",
    "estimated_frequency": "0 days 00:15:00",
    "regular_unique_spacing": true,
    "interval_counts": {
      "0 days 00:15:00": 70175
    },
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values."
  }
}
```

### data_processed.rar!data_processed/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx [sheet1]

```json
{
  "Time(year-month-day h:m:s)": {
    "column": "Time(year-month-day h:m:s)",
    "status": "parsed diagnostic copy",
    "non_null": 70176,
    "parsed": 70176,
    "parse_failures": 0,
    "ambiguous_day_month_values": 0,
    "missing": 0,
    "earliest": "2019-01-01 00:00:00+00:00",
    "latest": "2020-12-31 23:45:00+00:00",
    "unique_timestamps": 70176,
    "duplicate_timestamps": 0,
    "ascending_valid_values": true,
    "descending_valid_values": false,
    "timezone": "not documented in values (naive)",
    "estimated_frequency": "0 days 00:15:00",
    "regular_unique_spacing": true,
    "interval_counts": {
      "0 days 00:15:00": 70175
    },
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values."
  }
}
```

### data_processed.rar!data_processed/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx [sheet1]

```json
{
  "Time(year-month-day h:m:s)": {
    "column": "Time(year-month-day h:m:s)",
    "status": "parsed diagnostic copy",
    "non_null": 70176,
    "parsed": 70176,
    "parse_failures": 0,
    "ambiguous_day_month_values": 0,
    "missing": 0,
    "earliest": "2019-01-01 00:00:00+00:00",
    "latest": "2020-12-31 23:45:00+00:00",
    "unique_timestamps": 70176,
    "duplicate_timestamps": 0,
    "ascending_valid_values": true,
    "descending_valid_values": false,
    "timezone": "not documented in values (naive)",
    "estimated_frequency": "0 days 00:15:00",
    "regular_unique_spacing": true,
    "interval_counts": {
      "0 days 00:15:00": 70175
    },
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values."
  }
}
```

### data_processed.rar!data_processed/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx [sheet 1]

```json
{
  "Time(year-month-day h:m:s)": {
    "column": "Time(year-month-day h:m:s)",
    "status": "parsed diagnostic copy",
    "non_null": 69999,
    "parsed": 69999,
    "parse_failures": 0,
    "ambiguous_day_month_values": 0,
    "missing": 0,
    "earliest": "2019-01-01 11:00:00+00:00",
    "latest": "2020-12-31 23:45:00+00:00",
    "unique_timestamps": 69999,
    "duplicate_timestamps": 0,
    "ascending_valid_values": true,
    "descending_valid_values": false,
    "timezone": "not documented in values (naive)",
    "estimated_frequency": "0 days 00:15:00",
    "regular_unique_spacing": false,
    "interval_counts": {
      "0 days 00:15:00": 69996,
      "0 days 18:30:00": 1,
      "0 days 15:15:00": 1
    },
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values."
  }
}
```

### data_processed.rar!data_processed/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx [2019]

```json
{
  "Time(year-month-day h:m:s)": {
    "column": "Time(year-month-day h:m:s)",
    "status": "parsed diagnostic copy",
    "non_null": 70176,
    "parsed": 70153,
    "parse_failures": 23,
    "ambiguous_day_month_values": 0,
    "missing": 0,
    "earliest": "2019-01-01 00:00:00+00:00",
    "latest": "2020-12-31 23:45:00+00:00",
    "unique_timestamps": 70150,
    "duplicate_timestamps": 3,
    "ascending_valid_values": false,
    "descending_valid_values": false,
    "timezone": "not documented in values (naive)",
    "estimated_frequency": "0 days 00:15:00",
    "regular_unique_spacing": false,
    "interval_counts": {
      "0 days 00:15:00": 70075,
      "0 days 00:30:00": 26,
      "0 days 00:16:00": 24,
      "0 days 00:14:00": 24
    },
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values."
  }
}
```

### ml/data/raw/wind/Wind farm site 1 (Nominal capacity-99MW).xlsx [sheet1]

```json
{
  "Time(year-month-day h:m:s)": {
    "column": "Time(year-month-day h:m:s)",
    "status": "parsed diagnostic copy",
    "non_null": 70176,
    "parsed": 70176,
    "parse_failures": 0,
    "ambiguous_day_month_values": 0,
    "missing": 0,
    "earliest": "2019-01-01 00:00:00+00:00",
    "latest": "2020-12-31 23:45:00+00:00",
    "unique_timestamps": 70176,
    "duplicate_timestamps": 0,
    "ascending_valid_values": true,
    "descending_valid_values": false,
    "timezone": "not documented in values (naive)",
    "estimated_frequency": "0 days 00:15:00",
    "regular_unique_spacing": true,
    "interval_counts": {
      "0 days 00:15:00": 70175
    },
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values."
  }
}
```

## 6. Verified Wind Generation Target

**ACTUAL VERIFIED TARGET: `Power (MW)`** in the wind-farm workbooks. The wind-farm file context and explicit power header support wind output measured as **POWER**, in **MW**. It is not an energy measurement, capacity factor or normalized output. This verifies the column meaning from local headers, not the measurement provenance, sensor calibration, or gross/net/export convention.

| File | Target | dtype | Min MW | Max MW | Missing | Non-null target time coverage |
| --- | --- | --- | --- | --- | --- | --- |
| data_original.rar!data_original/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx | Power (MW) | float64 | 0.0 | 98.09444 | 0 | 2019-01-01 00:00:00+00:00 to 2020-12-31 23:45:00+00:00; 0 parse failures |
| data_original.rar!data_original/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx | Power (MW) | float64 | 0.0 | 201.24808 | 0 | 2019-01-01 00:00:00+00:00 to 2020-12-31 23:45:00+00:00; 0 parse failures |
| data_original.rar!data_original/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx | Power (MW) | float64 | -0.668767 | 94.2666 | 0 | 2019-01-01 00:00:00+00:00 to 2020-12-31 23:45:00+00:00; 0 parse failures |
| data_original.rar!data_original/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx | Power (MW) | float64 | 0.0 | 64.614 | 0 | 2019-01-01 00:00:00+00:00 to 2020-12-31 23:45:00+00:00; 0 parse failures |
| data_original.rar!data_original/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx | Power (MW) | float64 | 0.0 | 35.350667 | 0 | 2019-01-01 00:00:00+00:00 to 2020-12-31 23:45:00+00:00; 0 parse failures |
| data_original.rar!data_original/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx | Power (MW) | float64 | -99.0 | 114.36 | 0 | 2019-01-01 00:00:00+00:00 to 2020-12-31 23:45:00+00:00; 23 parse failures |
| data_processed.rar!data_processed/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx | Power (MW) | float64 | 0.0 | 98.09444 | 0 | 2019-01-01 00:00:00+00:00 to 2020-12-31 23:45:00+00:00; 0 parse failures |
| data_processed.rar!data_processed/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx | Power (MW) | float64 | 0.0 | 201.24808 | 0 | 2019-01-01 00:00:00+00:00 to 2020-12-31 23:45:00+00:00; 0 parse failures |
| data_processed.rar!data_processed/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx | Power (MW) | float64 | -0.668767 | 94.2666 | 0 | 2019-01-01 00:00:00+00:00 to 2020-12-31 23:45:00+00:00; 0 parse failures |
| data_processed.rar!data_processed/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx | Power (MW) | float64 | 0.0 | 64.614 | 0 | 2019-01-01 00:00:00+00:00 to 2020-12-31 23:45:00+00:00; 0 parse failures |
| data_processed.rar!data_processed/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx | Power (MW) | float64 | 0.0 | 35.350667 | 0 | 2019-01-01 11:00:00+00:00 to 2020-12-31 23:45:00+00:00; 0 parse failures |
| data_processed.rar!data_processed/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx | Power (MW) | float64 | -1.316 | 114.36 | 0 | 2019-01-01 00:00:00+00:00 to 2020-12-31 23:45:00+00:00; 23 parse failures |
| ml/data/raw/wind/Wind farm site 1 (Nominal capacity-99MW).xlsx | Power (MW) | float64 | 0.0 | 98.09444 | 0 | 2019-01-01 00:00:00+00:00 to 2020-12-31 23:45:00+00:00; 0 parse failures |

## 7. Primary Feature Candidates

**RECOMMENDATIONS** for the selected site 1 original, based on headers rather than model experiments.

| Exact column | Inferred description | dtype | Missing | Range | Recommendation |
| --- | --- | --- | --- | --- | --- |
| "Wind speed at height of 10 meters (m/s)" | Wind speed at the height stated in the header; metres per second. | float64 | 0 | -99.0 to 25.465 | PRIMARY FEATURE |
| "Wind direction at height of 10 meters (˚)" | Direction at the height stated in the header; degree symbol; reference convention unknown. | float64 | 0 | -99.0 to 358.987 | PRIMARY FEATURE |
| "Wind speed at height of 30 meters (m/s)" | Wind speed at the height stated in the header; metres per second. | float64 | 0 | -99.0 to 29.187 | PRIMARY FEATURE |
| "Wind direction at height of 30 meters (˚)" | Direction at the height stated in the header; degree symbol; reference convention unknown. | float64 | 0 | -99.0 to 359.087 | PRIMARY FEATURE |
| "Wind speed at height of 50 meters (m/s)" | Wind speed at the height stated in the header; metres per second. | float64 | 0 | -99.0 to 29.678 | PRIMARY FEATURE |
| "Wind direction at height of 50 meters (˚)" | Direction at the height stated in the header; degree symbol; reference convention unknown. | float64 | 0 | -99.0 to 358.933 | PRIMARY FEATURE |
| "Wind speed - at the height of wheel hub(m/s)" | Wind speed at the height stated in the header; metres per second. | float64 | 0 | -99.0 to 30.247 | PRIMARY FEATURE |

## 8. Secondary Feature Candidates

| Exact column | Inferred description | dtype | Missing | Range | Recommendation |
| --- | --- | --- | --- | --- | --- |
| "Air temperature  (°C) " | Air temperature; degrees Celsius in header. | float64 | 0 | -99.0 to 36.13 | SECONDARY FEATURE |
| "Atmosphere (hpa)" | Inferred air pressure from hpa unit; metadata confirmation recommended. | float64 | 0 | -99.0 to 918.192 | SECONDARY FEATURE |
| "Relative humidity (%)" | Relative humidity; percent in header. | float64 | 0 | -99.0 to 93.12 | SECONDARY FEATURE |

### Optional and excluded columns

| Exact column | Inferred description | dtype | Missing | Range | Recommendation |
| --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | Time index for future calendar features; source timezone unknown. | object | 0 | None to None | OPTIONAL FEATURE |

| Exact column | Inferred description | dtype | Missing | Range | Recommendation |
| --- | --- | --- | --- | --- | --- |
| "Wind speed - at the height of wheel hub (˚)" | Ambiguous: speed label with degree unit; verify before treating as hub direction. | float64 | 1 | -99.0 to 358.5 | EXCLUDE |
| "Power (MW)" | Prediction target; exclude from simultaneous predictors to prevent leakage. | float64 | 0 | 0.0 to 98.09444 | EXCLUDE |

## 9. Potential Derived Features

**RECOMMENDATIONS ONLY; nothing derived yet.** The timestamp supports hour, day_of_week, month and day_of_year once timezone is established. Verified direction columns support sine/cosine encodings once angular convention is confirmed. Multi-height speed measurements support investigation of speed differences or wind shear after height and sensor metadata checks. No u/v wind components were identified, so a component-based wind_speed_magnitude is not recommended. Hub height in metres is unspecified; do not assume it.

## 10. Data Quality Analysis

**FACTS.** Nulls and distributions are in section 4; timestamp issues are in section 5. Sparse means >50% null. IQR flags use 1.5 × IQR and are statistical candidates, not proof of invalid readings. Negative power may reflect consumption or measurement conventions; no automatic correction is justified. Negative temperature alone is not invalid. No external schema exists to conclusively validate all types. Repeated -99 values are counted as possible undocumented sentinels, not automatically converted to null. IQR flags on angles require circular interpretation; they are not physical validity tests.

### data_original.rar!data_original/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx [sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "physical_range_checks": {
    "Wind speed at height of 10 meters (m/s): values equal to -99 (possible undocumented sentinel)": 138,
    "Wind speed at height of 10 meters (m/s): negative speed": 138,
    "Wind direction at height of 10 meters (˚): values equal to -99 (possible undocumented sentinel)": 138,
    "Wind direction at height of 10 meters (˚): outside [0, 360]": 138,
    "Wind speed at height of 30 meters (m/s): values equal to -99 (possible undocumented sentinel)": 138,
    "Wind speed at height of 30 meters (m/s): negative speed": 138,
    "Wind direction at height of 30 meters (˚): values equal to -99 (possible undocumented sentinel)": 138,
    "Wind direction at height of 30 meters (˚): outside [0, 360]": 138,
    "Wind speed at height of 50 meters (m/s): values equal to -99 (possible undocumented sentinel)": 138,
    "Wind speed at height of 50 meters (m/s): negative speed": 138,
    "Wind direction at height of 50 meters (˚): values equal to -99 (possible undocumented sentinel)": 138,
    "Wind direction at height of 50 meters (˚): outside [0, 360]": 138,
    "Wind speed - at the height of wheel hub(m/s): values equal to -99 (possible undocumented sentinel)": 138,
    "Wind speed - at the height of wheel hub(m/s): negative speed": 138,
    "Wind speed - at the height of wheel hub (˚): values equal to -99 (possible undocumented sentinel)": 138,
    "Wind speed - at the height of wheel hub (˚): outside [0, 360]": 138,
    "Air temperature  (°C) : values equal to -99 (possible undocumented sentinel)": 138,
    "Atmosphere (hpa): values equal to -99 (possible undocumented sentinel)": 138,
    "Atmosphere (hpa): non-positive pressure": 140,
    "Relative humidity (%): values equal to -99 (possible undocumented sentinel)": 138,
    "Relative humidity (%): outside [0, 100]": 138,
    "Power (MW): values equal to -99 (possible undocumented sentinel)": 0,
    "Power (MW): negative output (investigate, not automatically invalid)": 0
  },
  "numeric_text_candidates": [],
  "non_finite_values": {
    "Wind speed at height of 10 meters (m/s)": 0,
    "Wind direction at height of 10 meters (˚)": 0,
    "Wind speed at height of 30 meters (m/s)": 0,
    "Wind direction at height of 30 meters (˚)": 0,
    "Wind speed at height of 50 meters (m/s)": 0,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub(m/s)": 0,
    "Wind speed - at the height of wheel hub (˚)": 0,
    "Air temperature  (°C) ": 0,
    "Atmosphere (hpa)": 0,
    "Relative humidity (%)": 0,
    "Power (MW)": 0
  },
  "iqr_outlier_counts": {
    "Wind speed at height of 10 meters (m/s)": 2279,
    "Wind direction at height of 10 meters (˚)": 10154,
    "Wind speed at height of 30 meters (m/s)": 1324,
    "Wind direction at height of 30 meters (˚)": 3031,
    "Wind speed at height of 50 meters (m/s)": 1131,
    "Wind direction at height of 50 meters (˚)": 138,
    "Wind speed - at the height of wheel hub(m/s)": 1153,
    "Wind speed - at the height of wheel hub (˚)": 138,
    "Air temperature  (°C) ": 138,
    "Atmosphere (hpa)": 2479,
    "Relative humidity (%)": 138,
    "Power (MW)": 2
  }
}
```

### data_original.rar!data_original/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx [sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "physical_range_checks": {
    "Wind speed at height of 10 meters (m/s): values equal to -99 (possible undocumented sentinel)": 51,
    "Wind speed at height of 10 meters (m/s): negative speed": 51,
    "Wind direction at height of 10 meters (˚): values equal to -99 (possible undocumented sentinel)": 51,
    "Wind direction at height of 10 meters (˚): outside [0, 360]": 51,
    "Wind speed at height of 30 meters (m/s): values equal to -99 (possible undocumented sentinel)": 51,
    "Wind speed at height of 30 meters (m/s): negative speed": 51,
    "Wind direction at height of 30 meters (˚): values equal to -99 (possible undocumented sentinel)": 51,
    "Wind direction at height of 30 meters (˚): outside [0, 360]": 51,
    "Wind speed at height of 50 meters (m/s): values equal to -99 (possible undocumented sentinel)": 51,
    "Wind speed at height of 50 meters (m/s): negative speed": 51,
    "Wind direction at height of 50 meters (˚): values equal to -99 (possible undocumented sentinel)": 51,
    "Wind direction at height of 50 meters (˚): outside [0, 360]": 51,
    "Wind speed - at the height of wheel hub (m/s): values equal to -99 (possible undocumented sentinel)": 51,
    "Wind speed - at the height of wheel hub (m/s): negative speed": 51,
    "Wind speed - at the height of wheel hub  (˚): values equal to -99 (possible undocumented sentinel)": 51,
    "Wind speed - at the height of wheel hub  (˚): outside [0, 360]": 51,
    "Air temperature  (°C) : values equal to -99 (possible undocumented sentinel)": 51,
    "Atmosphere (hpa): values equal to -99 (possible undocumented sentinel)": 51,
    "Atmosphere (hpa): non-positive pressure": 202,
    "Relative humidity (%): values equal to -99 (possible undocumented sentinel)": 51,
    "Relative humidity (%): outside [0, 100]": 51,
    "Power (MW): values equal to -99 (possible undocumented sentinel)": 0,
    "Power (MW): negative output (investigate, not automatically invalid)": 0
  },
  "numeric_text_candidates": [],
  "non_finite_values": {
    "Wind speed at height of 10 meters (m/s)": 0,
    "Wind direction at height of 10 meters (˚)": 0,
    "Wind speed at height of 30 meters (m/s)": 0,
    "Wind direction at height of 30 meters (˚)": 0,
    "Wind speed at height of 50 meters (m/s)": 0,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub (m/s)": 0,
    "Wind speed - at the height of wheel hub  (˚)": 0,
    "Air temperature  (°C) ": 0,
    "Atmosphere (hpa)": 0,
    "Relative humidity (%)": 0,
    "Power (MW)": 0
  },
  "iqr_outlier_counts": {
    "Wind speed at height of 10 meters (m/s)": 175,
    "Wind direction at height of 10 meters (˚)": 0,
    "Wind speed at height of 30 meters (m/s)": 263,
    "Wind direction at height of 30 meters (˚)": 0,
    "Wind speed at height of 50 meters (m/s)": 331,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub (m/s)": 318,
    "Wind speed - at the height of wheel hub  (˚)": 0,
    "Air temperature  (°C) ": 51,
    "Atmosphere (hpa)": 3883,
    "Relative humidity (%)": 11921,
    "Power (MW)": 0
  }
}
```

### data_original.rar!data_original/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx [sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "physical_range_checks": {
    "Wind speed at height of 10 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 10 meters (m/s): negative speed": 0,
    "Wind direction at height of 10 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 10 meters (˚): outside [0, 360]": 0,
    "Wind speed at height of 30 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 30 meters (m/s): negative speed": 0,
    "Wind direction at height of 30 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 30 meters (˚): outside [0, 360]": 0,
    "Wind speed at height of 50 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 50 meters (m/s): negative speed": 0,
    "Wind direction at height of 50 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 50 meters (˚): outside [0, 360]": 0,
    "Wind speed - at the height of wheel hub  (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed - at the height of wheel hub  (m/s): negative speed": 0,
    "Wind speed - at the height of wheel hub  (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed - at the height of wheel hub  (˚): outside [0, 360]": 0,
    "Air temperature  (°C) : values equal to -99 (possible undocumented sentinel)": 0,
    "Atmosphere (hpa): values equal to -99 (possible undocumented sentinel)": 0,
    "Atmosphere (hpa): non-positive pressure": 313,
    "Relative humidity (%): values equal to -99 (possible undocumented sentinel)": 0,
    "Relative humidity (%): outside [0, 100]": 4,
    "Power (MW): values equal to -99 (possible undocumented sentinel)": 0,
    "Power (MW): negative output (investigate, not automatically invalid)": 12944
  },
  "numeric_text_candidates": [],
  "non_finite_values": {
    "Wind speed at height of 10 meters (m/s)": 0,
    "Wind direction at height of 10 meters (˚)": 0,
    "Wind speed at height of 30 meters (m/s)": 0,
    "Wind direction at height of 30 meters (˚)": 0,
    "Wind speed at height of 50 meters (m/s)": 0,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub  (m/s)": 0,
    "Wind speed - at the height of wheel hub  (˚)": 0,
    "Air temperature  (°C) ": 0,
    "Atmosphere (hpa)": 0,
    "Relative humidity (%)": 0,
    "Power (MW)": 0
  },
  "iqr_outlier_counts": {
    "Wind speed at height of 10 meters (m/s)": 279,
    "Wind direction at height of 10 meters (˚)": 4478,
    "Wind speed at height of 30 meters (m/s)": 1175,
    "Wind direction at height of 30 meters (˚)": 0,
    "Wind speed at height of 50 meters (m/s)": 936,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub  (m/s)": 660,
    "Wind speed - at the height of wheel hub  (˚)": 0,
    "Air temperature  (°C) ": 7,
    "Atmosphere (hpa)": 320,
    "Relative humidity (%)": 4,
    "Power (MW)": 3762
  }
}
```

### data_original.rar!data_original/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx [sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "physical_range_checks": {
    "Wind speed at height of 10 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 10 meters (m/s): negative speed": 0,
    "Wind direction at height of 10 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 10 meters (˚): outside [0, 360]": 0,
    "Wind speed at height of 30 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 30 meters (m/s): negative speed": 0,
    "Wind direction at height of 30 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 30 meters (˚): outside [0, 360]": 0,
    "Wind speed at height of 50 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 50 meters (m/s): negative speed": 0,
    "Wind direction at height of 50 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 50 meters (˚): outside [0, 360]": 0,
    "Wind speed - at the height of wheel hub  (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed - at the height of wheel hub  (m/s): negative speed": 0,
    "Wind speed - at the height of wheel hub (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed - at the height of wheel hub (˚): outside [0, 360]": 0,
    "Air temperature  (°C) : values equal to -99 (possible undocumented sentinel)": 0,
    "Atmosphere (hpa): values equal to -99 (possible undocumented sentinel)": 0,
    "Atmosphere (hpa): non-positive pressure": 1,
    "Relative humidity (%): values equal to -99 (possible undocumented sentinel)": 0,
    "Relative humidity (%): outside [0, 100]": 0,
    "Power (MW): values equal to -99 (possible undocumented sentinel)": 0,
    "Power (MW): negative output (investigate, not automatically invalid)": 0
  },
  "numeric_text_candidates": [],
  "non_finite_values": {
    "Wind speed at height of 10 meters (m/s)": 0,
    "Wind direction at height of 10 meters (˚)": 0,
    "Wind speed at height of 30 meters (m/s)": 0,
    "Wind direction at height of 30 meters (˚)": 0,
    "Wind speed at height of 50 meters (m/s)": 0,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub  (m/s)": 0,
    "Wind speed - at the height of wheel hub (˚)": 0,
    "Air temperature  (°C) ": 0,
    "Atmosphere (hpa)": 0,
    "Relative humidity (%)": 0,
    "Power (MW)": 0
  },
  "iqr_outlier_counts": {
    "Wind speed at height of 10 meters (m/s)": 1344,
    "Wind direction at height of 10 meters (˚)": 0,
    "Wind speed at height of 30 meters (m/s)": 1251,
    "Wind direction at height of 30 meters (˚)": 0,
    "Wind speed at height of 50 meters (m/s)": 1944,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub  (m/s)": 1701,
    "Wind speed - at the height of wheel hub (˚)": 0,
    "Air temperature  (°C) ": 0,
    "Atmosphere (hpa)": 7,
    "Relative humidity (%)": 289,
    "Power (MW)": 0
  }
}
```

### data_original.rar!data_original/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx [sheet 1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "physical_range_checks": {
    "Wind speed at height of 10 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 10 meters (m/s): negative speed": 2059,
    "Wind direction at height of 10 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 10 meters (˚): outside [0, 360]": 2057,
    "Wind speed at height of 30 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 30 meters (m/s): negative speed": 2057,
    "Wind direction at height of 30 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 30 meters (˚): outside [0, 360]": 2057,
    "Wind speed at height of 50 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 50 meters (m/s): negative speed": 2057,
    "Wind direction at height of 50 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 50 meters (˚): outside [0, 360]": 2057,
    "Wind speed - at the height of wheel hub (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed - at the height of wheel hub (m/s): negative speed": 0,
    "Wind speed - at the height of wheel hub  (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed - at the height of wheel hub  (˚): outside [0, 360]": 0,
    "Air temperature  (°C) : values equal to -99 (possible undocumented sentinel)": 0,
    "Atmosphere (hpa): values equal to -99 (possible undocumented sentinel)": 0,
    "Atmosphere (hpa): non-positive pressure": 8878,
    "Relative humidity (%): values equal to -99 (possible undocumented sentinel)": 0,
    "Relative humidity (%): outside [0, 100]": 14522,
    "Power (MW): values equal to -99 (possible undocumented sentinel)": 0,
    "Power (MW): negative output (investigate, not automatically invalid)": 0
  },
  "numeric_text_candidates": [],
  "non_finite_values": {
    "Wind speed at height of 10 meters (m/s)": 0,
    "Wind direction at height of 10 meters (˚)": 0,
    "Wind speed at height of 30 meters (m/s)": 0,
    "Wind direction at height of 30 meters (˚)": 0,
    "Wind speed at height of 50 meters (m/s)": 0,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub (m/s)": 0,
    "Wind speed - at the height of wheel hub  (˚)": 0,
    "Air temperature  (°C) ": 0,
    "Atmosphere (hpa)": 0,
    "Relative humidity (%)": 0,
    "Power (MW)": 0
  },
  "iqr_outlier_counts": {
    "Wind speed at height of 10 meters (m/s)": 14556,
    "Wind direction at height of 10 meters (˚)": 0,
    "Wind speed at height of 30 meters (m/s)": 16134,
    "Wind direction at height of 30 meters (˚)": 0,
    "Wind speed at height of 50 meters (m/s)": 355,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub (m/s)": 2985,
    "Wind speed - at the height of wheel hub  (˚)": 0,
    "Air temperature  (°C) ": 0,
    "Atmosphere (hpa)": 18278,
    "Relative humidity (%)": 0,
    "Power (MW)": 9212
  }
}
```

### data_original.rar!data_original/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx [2019]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "physical_range_checks": {
    "Wind speed at height of 10 meters (m/s): values equal to -99 (possible undocumented sentinel)": 131,
    "Wind speed at height of 10 meters (m/s): negative speed": 131,
    "Wind direction at height of 10 meters (˚): values equal to -99 (possible undocumented sentinel)": 131,
    "Wind direction at height of 10 meters (˚): outside [0, 360]": 131,
    "Wind speed at height of 30 meters (m/s): values equal to -99 (possible undocumented sentinel)": 131,
    "Wind speed at height of 30 meters (m/s): negative speed": 131,
    "Wind direction at height of 30 meters (˚): values equal to -99 (possible undocumented sentinel)": 131,
    "Wind direction at height of 30 meters (˚): outside [0, 360]": 131,
    "Wind speed at height of 50 meters (m/s): values equal to -99 (possible undocumented sentinel)": 131,
    "Wind speed at height of 50 meters (m/s): negative speed": 131,
    "Wind direction at height of 50 meters (˚): values equal to -99 (possible undocumented sentinel)": 131,
    "Wind direction at height of 50 meters (˚): outside [0, 360]": 131,
    "Wind speed - at the height of wheel hub  (m/s): values equal to -99 (possible undocumented sentinel)": 131,
    "Wind speed - at the height of wheel hub  (m/s): negative speed": 131,
    "Wind speed - at the height of wheel hub  (˚): values equal to -99 (possible undocumented sentinel)": 131,
    "Wind speed - at the height of wheel hub  (˚): outside [0, 360]": 131,
    "Air temperature  (°C) : values equal to -99 (possible undocumented sentinel)": 0,
    "Atmosphere (hpa): values equal to -99 (possible undocumented sentinel)": 0,
    "Atmosphere (hpa): non-positive pressure": 21,
    "Relative humidity (%): values equal to -99 (possible undocumented sentinel)": 0,
    "Relative humidity (%): outside [0, 100]": 0,
    "Power (MW): values equal to -99 (possible undocumented sentinel)": 25,
    "Power (MW): negative output (investigate, not automatically invalid)": 7591
  },
  "numeric_text_candidates": [],
  "non_finite_values": {
    "Wind speed at height of 10 meters (m/s)": 0,
    "Wind direction at height of 10 meters (˚)": 0,
    "Wind speed at height of 30 meters (m/s)": 0,
    "Wind direction at height of 30 meters (˚)": 0,
    "Wind speed at height of 50 meters (m/s)": 0,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub  (m/s)": 0,
    "Wind speed - at the height of wheel hub  (˚)": 0,
    "Air temperature  (°C) ": 0,
    "Atmosphere (hpa)": 0,
    "Relative humidity (%)": 0,
    "Power (MW)": 0
  },
  "iqr_outlier_counts": {
    "Wind speed at height of 10 meters (m/s)": 159,
    "Wind direction at height of 10 meters (˚)": 0,
    "Wind speed at height of 30 meters (m/s)": 181,
    "Wind direction at height of 30 meters (˚)": 1396,
    "Wind speed at height of 50 meters (m/s)": 187,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub  (m/s)": 187,
    "Wind speed - at the height of wheel hub  (˚)": 0,
    "Air temperature  (°C) ": 0,
    "Atmosphere (hpa)": 678,
    "Relative humidity (%)": 596,
    "Power (MW)": 25
  }
}
```

### data_processed.rar!data_processed/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx [sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "physical_range_checks": {
    "Wind speed at height of 10 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 10 meters (m/s): negative speed": 0,
    "Wind direction at height of 10 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 10 meters (˚): outside [0, 360]": 0,
    "Wind speed at height of 30 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 30 meters (m/s): negative speed": 0,
    "Wind direction at height of 30 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 30 meters (˚): outside [0, 360]": 0,
    "Wind speed at height of 50 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 50 meters (m/s): negative speed": 0,
    "Wind direction at height of 50 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 50 meters (˚): outside [0, 360]": 0,
    "Wind speed - at the height of wheel hub (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed - at the height of wheel hub (m/s): negative speed": 0,
    "Wind speed - at the height of wheel hub (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed - at the height of wheel hub (˚): outside [0, 360]": 0,
    "Air temperature  (°C) : values equal to -99 (possible undocumented sentinel)": 0,
    "Atmosphere (hpa): values equal to -99 (possible undocumented sentinel)": 0,
    "Atmosphere (hpa): non-positive pressure": 0,
    "Relative humidity (%): values equal to -99 (possible undocumented sentinel)": 0,
    "Relative humidity (%): outside [0, 100]": 0,
    "Power (MW): values equal to -99 (possible undocumented sentinel)": 0,
    "Power (MW): negative output (investigate, not automatically invalid)": 0
  },
  "numeric_text_candidates": [],
  "non_finite_values": {
    "Wind speed at height of 10 meters (m/s)": 0,
    "Wind direction at height of 10 meters (˚)": 0,
    "Wind speed at height of 30 meters (m/s)": 0,
    "Wind direction at height of 30 meters (˚)": 0,
    "Wind speed at height of 50 meters (m/s)": 0,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub (m/s)": 0,
    "Wind speed - at the height of wheel hub (˚)": 0,
    "Air temperature  (°C) ": 0,
    "Atmosphere (hpa)": 0,
    "Relative humidity (%)": 0,
    "Power (MW)": 0
  },
  "iqr_outlier_counts": {
    "Wind speed at height of 10 meters (m/s)": 2155,
    "Wind direction at height of 10 meters (˚)": 9980,
    "Wind speed at height of 30 meters (m/s)": 1205,
    "Wind direction at height of 30 meters (˚)": 3884,
    "Wind speed at height of 50 meters (m/s)": 1008,
    "Wind direction at height of 50 meters (˚)": 168,
    "Wind speed - at the height of wheel hub (m/s)": 1028,
    "Wind speed - at the height of wheel hub (˚)": 0,
    "Air temperature  (°C) ": 0,
    "Atmosphere (hpa)": 2263,
    "Relative humidity (%)": 0,
    "Power (MW)": 0
  }
}
```

### data_processed.rar!data_processed/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx [sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "physical_range_checks": {
    "Wind speed at height of 10 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 10 meters (m/s): negative speed": 0,
    "Wind direction at height of 10 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 10 meters (˚): outside [0, 360]": 0,
    "Wind speed at height of 30 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 30 meters (m/s): negative speed": 0,
    "Wind direction at height of 30 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 30 meters (˚): outside [0, 360]": 0,
    "Wind speed at height of 50 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 50 meters (m/s): negative speed": 0,
    "Wind direction at height of 50 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 50 meters (˚): outside [0, 360]": 0,
    "Wind speed - at the height of wheel hub  (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed - at the height of wheel hub  (m/s): negative speed": 0,
    "Wind speed - at the height of wheel hub (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed - at the height of wheel hub (˚): outside [0, 360]": 0,
    "Air temperature  (°C) : values equal to -99 (possible undocumented sentinel)": 0,
    "Atmosphere (hpa): values equal to -99 (possible undocumented sentinel)": 0,
    "Atmosphere (hpa): non-positive pressure": 0,
    "Power (MW): values equal to -99 (possible undocumented sentinel)": 0,
    "Power (MW): negative output (investigate, not automatically invalid)": 0
  },
  "numeric_text_candidates": [],
  "non_finite_values": {
    "Wind speed at height of 10 meters (m/s)": 0,
    "Wind direction at height of 10 meters (˚)": 0,
    "Wind speed at height of 30 meters (m/s)": 0,
    "Wind direction at height of 30 meters (˚)": 0,
    "Wind speed at height of 50 meters (m/s)": 0,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub  (m/s)": 0,
    "Wind speed - at the height of wheel hub (˚)": 0,
    "Air temperature  (°C) ": 0,
    "Atmosphere (hpa)": 0,
    "Power (MW)": 0
  },
  "iqr_outlier_counts": {
    "Wind speed at height of 10 meters (m/s)": 127,
    "Wind direction at height of 10 meters (˚)": 0,
    "Wind speed at height of 30 meters (m/s)": 222,
    "Wind direction at height of 30 meters (˚)": 0,
    "Wind speed at height of 50 meters (m/s)": 280,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub  (m/s)": 268,
    "Wind speed - at the height of wheel hub (˚)": 0,
    "Air temperature  (°C) ": 0,
    "Atmosphere (hpa)": 3550,
    "Power (MW)": 0
  }
}
```

### data_processed.rar!data_processed/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx [sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "physical_range_checks": {
    "Wind speed at height of 10 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 10 meters (m/s): negative speed": 0,
    "Wind direction at height of 10 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 10 meters (˚): outside [0, 360]": 0,
    "Wind speed at height of 30 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 30 meters (m/s): negative speed": 0,
    "Wind direction at height of 30 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 30 meters (˚): outside [0, 360]": 0,
    "Wind speed at height of 50 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 50 meters (m/s): negative speed": 0,
    "Wind direction at height of 50 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 50 meters (˚): outside [0, 360]": 0,
    "Wind speed - at the height of wheel hub (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed - at the height of wheel hub (m/s): negative speed": 0,
    "Wind speed - at the height of wheel hub (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed - at the height of wheel hub (˚): outside [0, 360]": 0,
    "Air temperature  (°C) : values equal to -99 (possible undocumented sentinel)": 0,
    "Atmosphere (hpa): values equal to -99 (possible undocumented sentinel)": 0,
    "Atmosphere (hpa): non-positive pressure": 0,
    "Relative humidity (%): values equal to -99 (possible undocumented sentinel)": 0,
    "Relative humidity (%): outside [0, 100]": 0,
    "Power (MW): values equal to -99 (possible undocumented sentinel)": 0,
    "Power (MW): negative output (investigate, not automatically invalid)": 12979
  },
  "numeric_text_candidates": [],
  "non_finite_values": {
    "Wind speed at height of 10 meters (m/s)": 0,
    "Wind direction at height of 10 meters (˚)": 0,
    "Wind speed at height of 30 meters (m/s)": 0,
    "Wind direction at height of 30 meters (˚)": 0,
    "Wind speed at height of 50 meters (m/s)": 0,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub (m/s)": 0,
    "Wind speed - at the height of wheel hub (˚)": 0,
    "Air temperature  (°C) ": 0,
    "Atmosphere (hpa)": 0,
    "Relative humidity (%)": 0,
    "Power (MW)": 0
  },
  "iqr_outlier_counts": {
    "Wind speed at height of 10 meters (m/s)": 279,
    "Wind direction at height of 10 meters (˚)": 5014,
    "Wind speed at height of 30 meters (m/s)": 1175,
    "Wind direction at height of 30 meters (˚)": 0,
    "Wind speed at height of 50 meters (m/s)": 937,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub (m/s)": 694,
    "Wind speed - at the height of wheel hub (˚)": 0,
    "Air temperature  (°C) ": 18,
    "Atmosphere (hpa)": 0,
    "Relative humidity (%)": 0,
    "Power (MW)": 3763
  }
}
```

### data_processed.rar!data_processed/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx [sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "physical_range_checks": {
    "Wind speed at height of 10 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 10 meters (m/s): negative speed": 0,
    "Wind direction at height of 10 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 10 meters (˚): outside [0, 360]": 0,
    "Wind speed at height of 30 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 30 meters (m/s): negative speed": 0,
    "Wind direction at height of 30 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 30 meters (˚): outside [0, 360]": 0,
    "Wind speed at height of 50 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 50 meters (m/s): negative speed": 0,
    "Wind direction at height of 50 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 50 meters (˚): outside [0, 360]": 0,
    "Wind speed - at the height of wheel hub (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed - at the height of wheel hub (m/s): negative speed": 0,
    "Wind speed - at the height of wheel hub  (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed - at the height of wheel hub  (˚): outside [0, 360]": 0,
    "Air temperature  (°C) : values equal to -99 (possible undocumented sentinel)": 0,
    "Atmosphere (hpa): values equal to -99 (possible undocumented sentinel)": 0,
    "Atmosphere (hpa): non-positive pressure": 0,
    "Relative humidity (%): values equal to -99 (possible undocumented sentinel)": 0,
    "Relative humidity (%): outside [0, 100]": 0,
    "Power (MW): values equal to -99 (possible undocumented sentinel)": 0,
    "Power (MW): negative output (investigate, not automatically invalid)": 0
  },
  "numeric_text_candidates": [],
  "non_finite_values": {
    "Wind speed at height of 10 meters (m/s)": 0,
    "Wind direction at height of 10 meters (˚)": 0,
    "Wind speed at height of 30 meters (m/s)": 0,
    "Wind direction at height of 30 meters (˚)": 0,
    "Wind speed at height of 50 meters (m/s)": 0,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub (m/s)": 0,
    "Wind speed - at the height of wheel hub  (˚)": 0,
    "Air temperature  (°C) ": 0,
    "Atmosphere (hpa)": 0,
    "Relative humidity (%)": 0,
    "Power (MW)": 0
  },
  "iqr_outlier_counts": {
    "Wind speed at height of 10 meters (m/s)": 1352,
    "Wind direction at height of 10 meters (˚)": 0,
    "Wind speed at height of 30 meters (m/s)": 1250,
    "Wind direction at height of 30 meters (˚)": 0,
    "Wind speed at height of 50 meters (m/s)": 1957,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub (m/s)": 1698,
    "Wind speed - at the height of wheel hub  (˚)": 0,
    "Air temperature  (°C) ": 0,
    "Atmosphere (hpa)": 7,
    "Relative humidity (%)": 297,
    "Power (MW)": 0
  }
}
```

### data_processed.rar!data_processed/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx [sheet 1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "physical_range_checks": {
    "Wind speed at height of 10 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 10 meters (m/s): negative speed": 2058,
    "Wind direction at height of 10 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 10 meters (˚): outside [0, 360]": 2057,
    "Wind speed at height of 30 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 30 meters (m/s): negative speed": 2057,
    "Wind direction at height of 30 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 30 meters (˚): outside [0, 360]": 2057,
    "Wind speed at height of 50 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 50 meters (m/s): negative speed": 2057,
    "Wind direction at height of 50 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 50 meters (˚): outside [0, 360]": 2057,
    "Wind speed - at the height of wheel hub (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed - at the height of wheel hub (m/s): negative speed": 0,
    "Wind speed - at the height of wheel hub  (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed - at the height of wheel hub  (˚): outside [0, 360]": 0,
    "Air temperature  (°C) : values equal to -99 (possible undocumented sentinel)": 0,
    "Power (MW): values equal to -99 (possible undocumented sentinel)": 0,
    "Power (MW): negative output (investigate, not automatically invalid)": 0
  },
  "numeric_text_candidates": [],
  "non_finite_values": {
    "Wind speed at height of 10 meters (m/s)": 0,
    "Wind direction at height of 10 meters (˚)": 0,
    "Wind speed at height of 30 meters (m/s)": 0,
    "Wind direction at height of 30 meters (˚)": 0,
    "Wind speed at height of 50 meters (m/s)": 0,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub (m/s)": 0,
    "Wind speed - at the height of wheel hub  (˚)": 0,
    "Air temperature  (°C) ": 0,
    "Power (MW)": 0
  },
  "iqr_outlier_counts": {
    "Wind speed at height of 10 meters (m/s)": 14555,
    "Wind direction at height of 10 meters (˚)": 0,
    "Wind speed at height of 30 meters (m/s)": 16134,
    "Wind direction at height of 30 meters (˚)": 0,
    "Wind speed at height of 50 meters (m/s)": 358,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub (m/s)": 3007,
    "Wind speed - at the height of wheel hub  (˚)": 0,
    "Air temperature  (°C) ": 0,
    "Power (MW)": 9222
  }
}
```

### data_processed.rar!data_processed/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx [2019]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "physical_range_checks": {
    "Wind speed at height of 10 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 10 meters (m/s): negative speed": 0,
    "Wind direction at height of 10 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 10 meters (˚): outside [0, 360]": 0,
    "Wind speed at height of 30 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 30 meters (m/s): negative speed": 0,
    "Wind direction at height of 30 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 30 meters (˚): outside [0, 360]": 0,
    "Wind speed at height of 50 meters (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed at height of 50 meters (m/s): negative speed": 0,
    "Wind direction at height of 50 meters (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind direction at height of 50 meters (˚): outside [0, 360]": 0,
    "Wind speed - at the height of wheel hub (m/s): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed - at the height of wheel hub (m/s): negative speed": 0,
    "Wind speed - at the height of wheel hub (˚): values equal to -99 (possible undocumented sentinel)": 0,
    "Wind speed - at the height of wheel hub (˚): outside [0, 360]": 0,
    "Air temperature  (°C) : values equal to -99 (possible undocumented sentinel)": 0,
    "Atmosphere (hpa): values equal to -99 (possible undocumented sentinel)": 0,
    "Atmosphere (hpa): non-positive pressure": 10,
    "Relative humidity (%): values equal to -99 (possible undocumented sentinel)": 0,
    "Relative humidity (%): outside [0, 100]": 0,
    "Power (MW): values equal to -99 (possible undocumented sentinel)": 0,
    "Power (MW): negative output (investigate, not automatically invalid)": 7566
  },
  "numeric_text_candidates": [],
  "non_finite_values": {
    "Wind speed at height of 10 meters (m/s)": 0,
    "Wind direction at height of 10 meters (˚)": 0,
    "Wind speed at height of 30 meters (m/s)": 0,
    "Wind direction at height of 30 meters (˚)": 0,
    "Wind speed at height of 50 meters (m/s)": 0,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub (m/s)": 0,
    "Wind speed - at the height of wheel hub (˚)": 0,
    "Air temperature  (°C) ": 0,
    "Atmosphere (hpa)": 0,
    "Relative humidity (%)": 0,
    "Power (MW)": 0
  },
  "iqr_outlier_counts": {
    "Wind speed at height of 10 meters (m/s)": 30,
    "Wind direction at height of 10 meters (˚)": 0,
    "Wind speed at height of 30 meters (m/s)": 51,
    "Wind direction at height of 30 meters (˚)": 1360,
    "Wind speed at height of 50 meters (m/s)": 56,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub (m/s)": 58,
    "Wind speed - at the height of wheel hub (˚)": 0,
    "Air temperature  (°C) ": 0,
    "Atmosphere (hpa)": 668,
    "Relative humidity (%)": 590,
    "Power (MW)": 0
  }
}
```

### ml/data/raw/wind/Wind farm site 1 (Nominal capacity-99MW).xlsx [sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "physical_range_checks": {
    "Wind speed at height of 10 meters (m/s): values equal to -99 (possible undocumented sentinel)": 138,
    "Wind speed at height of 10 meters (m/s): negative speed": 138,
    "Wind direction at height of 10 meters (˚): values equal to -99 (possible undocumented sentinel)": 138,
    "Wind direction at height of 10 meters (˚): outside [0, 360]": 138,
    "Wind speed at height of 30 meters (m/s): values equal to -99 (possible undocumented sentinel)": 138,
    "Wind speed at height of 30 meters (m/s): negative speed": 138,
    "Wind direction at height of 30 meters (˚): values equal to -99 (possible undocumented sentinel)": 138,
    "Wind direction at height of 30 meters (˚): outside [0, 360]": 138,
    "Wind speed at height of 50 meters (m/s): values equal to -99 (possible undocumented sentinel)": 138,
    "Wind speed at height of 50 meters (m/s): negative speed": 138,
    "Wind direction at height of 50 meters (˚): values equal to -99 (possible undocumented sentinel)": 138,
    "Wind direction at height of 50 meters (˚): outside [0, 360]": 138,
    "Wind speed - at the height of wheel hub(m/s): values equal to -99 (possible undocumented sentinel)": 138,
    "Wind speed - at the height of wheel hub(m/s): negative speed": 138,
    "Wind speed - at the height of wheel hub (˚): values equal to -99 (possible undocumented sentinel)": 138,
    "Wind speed - at the height of wheel hub (˚): outside [0, 360]": 138,
    "Air temperature  (°C) : values equal to -99 (possible undocumented sentinel)": 138,
    "Atmosphere (hpa): values equal to -99 (possible undocumented sentinel)": 138,
    "Atmosphere (hpa): non-positive pressure": 140,
    "Relative humidity (%): values equal to -99 (possible undocumented sentinel)": 138,
    "Relative humidity (%): outside [0, 100]": 138,
    "Power (MW): values equal to -99 (possible undocumented sentinel)": 0,
    "Power (MW): negative output (investigate, not automatically invalid)": 0
  },
  "numeric_text_candidates": [],
  "non_finite_values": {
    "Wind speed at height of 10 meters (m/s)": 0,
    "Wind direction at height of 10 meters (˚)": 0,
    "Wind speed at height of 30 meters (m/s)": 0,
    "Wind direction at height of 30 meters (˚)": 0,
    "Wind speed at height of 50 meters (m/s)": 0,
    "Wind direction at height of 50 meters (˚)": 0,
    "Wind speed - at the height of wheel hub(m/s)": 0,
    "Wind speed - at the height of wheel hub (˚)": 0,
    "Air temperature  (°C) ": 0,
    "Atmosphere (hpa)": 0,
    "Relative humidity (%)": 0,
    "Power (MW)": 0
  },
  "iqr_outlier_counts": {
    "Wind speed at height of 10 meters (m/s)": 2279,
    "Wind direction at height of 10 meters (˚)": 10154,
    "Wind speed at height of 30 meters (m/s)": 1324,
    "Wind direction at height of 30 meters (˚)": 3031,
    "Wind speed at height of 50 meters (m/s)": 1131,
    "Wind direction at height of 50 meters (˚)": 138,
    "Wind speed - at the height of wheel hub(m/s)": 1153,
    "Wind speed - at the height of wheel hub (˚)": 138,
    "Air temperature  (°C) ": 138,
    "Atmosphere (hpa)": 2479,
    "Relative humidity (%)": 138,
    "Power (MW)": 2
  }
}
```

**RECOMMENDED ACTIONS.** Validate null handling per column, review flagged ranges against source metadata, confirm the contradictory hub-speed/degree header, verify whether -99 encodes missing observations, investigate zero pressure, and decide target-quality policies before any cleaning.

## 11. Dataset Compatibility and Merge Analysis

**FACTS.** Wind files have a timestamp column and site identifiers in filenames, not explicit row-level plant/site keys. Same timestamps across different sites are not evidence of co-location. Identical headers imply compatible labelled units only; timezone and measurement conventions remain unverified. The table evaluates every pair of wind candidates, including the selected copy. No joins were performed.

| A | B | Classification | Shared timestamps | Units/schema | Reason |
| --- | --- | --- | --- | --- | --- |
| data_original.rar!data_original/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | data_original.rar!data_original/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | data_original.rar!data_original/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | data_original.rar!data_original/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | data_original.rar!data_original/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | data_original.rar!data_original/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | MERGE REQUIRES PREPROCESSING | 70126 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Same filename site; original/processed conflict policy needed. |
| data_original.rar!data_original/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | MERGE REQUIRES PREPROCESSING | 69999 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | MERGE REQUIRES PREPROCESSING | 70126 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | ml/data/raw/wind/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | MERGE READY | 70176 | same labelled units | Identical tables; redundant copy. Select one; do not append duplicates. |
| data_original.rar!data_original/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | data_original.rar!data_original/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | data_original.rar!data_original/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | data_original.rar!data_original/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | MERGE REQUIRES PREPROCESSING | 70176 | same labelled units | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | data_original.rar!data_original/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | MERGE REQUIRES PREPROCESSING | 70126 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Same filename site; original/processed conflict policy needed. |
| data_original.rar!data_original/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | same labelled units | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | MERGE REQUIRES PREPROCESSING | 69999 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | MERGE REQUIRES PREPROCESSING | 70126 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | ml/data/raw/wind/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | data_original.rar!data_original/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | data_original.rar!data_original/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | data_original.rar!data_original/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | MERGE REQUIRES PREPROCESSING | 70126 | same labelled units | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Same filename site; original/processed conflict policy needed. |
| data_original.rar!data_original/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | MERGE REQUIRES PREPROCESSING | 69999 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | MERGE REQUIRES PREPROCESSING | 70126 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | ml/data/raw/wind/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | data_original.rar!data_original/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | data_original.rar!data_original/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | MERGE REQUIRES PREPROCESSING | 70126 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Same filename site; original/processed conflict policy needed. |
| data_original.rar!data_original/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | MERGE REQUIRES PREPROCESSING | 69999 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | MERGE REQUIRES PREPROCESSING | 70126 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | ml/data/raw/wind/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | data_original.rar!data_original/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | MERGE REQUIRES PREPROCESSING | 70126 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | data_processed.rar!data_processed/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | data_processed.rar!data_processed/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | data_processed.rar!data_processed/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | data_processed.rar!data_processed/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | same labelled units | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | data_processed.rar!data_processed/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | MERGE REQUIRES PREPROCESSING | 69999 | schema differs | Same filename site; original/processed conflict policy needed. |
| data_original.rar!data_original/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | data_processed.rar!data_processed/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | MERGE REQUIRES PREPROCESSING | 70126 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | ml/data/raw/wind/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | data_processed.rar!data_processed/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70126 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | data_processed.rar!data_processed/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70126 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | data_processed.rar!data_processed/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70126 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | data_processed.rar!data_processed/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70126 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | data_processed.rar!data_processed/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | MERGE REQUIRES PREPROCESSING | 69949 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_original.rar!data_original/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | data_processed.rar!data_processed/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | MERGE REQUIRES PREPROCESSING | 70150 | schema differs | Same filename site; original/processed conflict policy needed. |
| data_original.rar!data_original/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | ml/data/raw/wind/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70126 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_processed.rar!data_processed/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_processed.rar!data_processed/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | same labelled units | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_processed.rar!data_processed/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_processed.rar!data_processed/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | MERGE REQUIRES PREPROCESSING | 69999 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_processed.rar!data_processed/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | MERGE REQUIRES PREPROCESSING | 70126 | same labelled units | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_processed.rar!data_processed/wind_farms/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | ml/data/raw/wind/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Same filename site; original/processed conflict policy needed. |
| data_processed.rar!data_processed/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_processed.rar!data_processed/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_processed.rar!data_processed/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | MERGE REQUIRES PREPROCESSING | 69999 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_processed.rar!data_processed/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | MERGE REQUIRES PREPROCESSING | 70126 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_processed.rar!data_processed/wind_farms/Wind farm site 2 (Nominal capacity-200MW).xlsx::sheet1 | ml/data/raw/wind/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_processed.rar!data_processed/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_processed.rar!data_processed/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | MERGE REQUIRES PREPROCESSING | 69999 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_processed.rar!data_processed/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | MERGE REQUIRES PREPROCESSING | 70126 | same labelled units | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_processed.rar!data_processed/wind_farms/Wind farm site 3 (Nominal capacity-99MW).xlsx::sheet1 | ml/data/raw/wind/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_processed.rar!data_processed/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | MERGE REQUIRES PREPROCESSING | 69999 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_processed.rar!data_processed/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | data_processed.rar!data_processed/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | MERGE REQUIRES PREPROCESSING | 70126 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_processed.rar!data_processed/wind_farms/Wind farm site 4 (Nominal capacity-66MW).xlsx::sheet1 | ml/data/raw/wind/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70176 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_processed.rar!data_processed/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | data_processed.rar!data_processed/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | MERGE REQUIRES PREPROCESSING | 69949 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_processed.rar!data_processed/wind_farms/Wind farm site 5 (Nominal capacity-36MW).xlsx::sheet 1 | ml/data/raw/wind/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 69999 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |
| data_processed.rar!data_processed/wind_farms/Wind farm site 6 (Nominal capacity-96MW).xlsx::2019 | ml/data/raw/wind/Wind farm site 1 (Nominal capacity-99MW).xlsx::sheet1 | MERGE REQUIRES PREPROCESSING | 70126 | schema differs | Different filename sites; add verified site keys; avoid timestamp-only join. |

Time coverage and interval distributions for each pair's inputs are in section 5. Even where 15-minute spacing matches, gaps, calendar coverage and undocumented timezone must be resolved before joining. Wind/solar site 1 identifiers belong to different naming domains; no shared physical site is established and no wind/solar join is recommended.

## 12. Recommended Dataset for Wind Model

**RECOMMENDATION.** Start Milestone 2 with the selected original wind site 1 workbook. It contains co-recorded weather and labelled MW power, so no cross-file join is needed for an initial single-site dataset. Keep the publisher-labelled processed variant for comparison until its transformations are documented. Other sites are potential later evaluation datasets, not automatically interchangeable rows.

## 13. Recommended Preprocessing for Milestone 2

**RECOMMENDATIONS; NOT IMPLEMENTED.**

1. Obtain source URL, license, timezone, site/sensor metadata, hub height, direction reference and processing history.
2. Resolve the hub degree-column label before assigning it a feature meaning.
3. Establish timestamp format/timezone, inspect gaps and duplicates by site, and retain original values for audit.
4. Verify possible -99 sentinels and zero pressure, then define missing-value and suspicious-output policies; do not blindly clip negative MW or replace target nulls.
5. Validate units and ranges, preserve column mappings, and evaluate circular direction/calendar features.
6. Establish forecast horizon and feature availability; contemporaneous weather is not proof of future forecast availability.
7. Plan chronological train/validation/test boundaries before fitting any imputation or scaling; prevent time leakage.

## 14. Limitations and Missing Information

**FACTS / LIMITATIONS.** Header-based semantics do not establish measured versus simulated weather, forecast issue times, turbine availability, curtailment, capacity changes, or power metering convention. Filename nominal capacities are labels, not independently verified ratings. Solar archives are inventory-only. No model, cleaned dataset, derived features, database or API change is produced. The reproducible runner requires the original six downloads in their documented locations, the selected raw copy, Pandas, openpyxl and libarchive-compatible tar. Missing or changed sources fail explicitly.

Reproduce from the repository root:

```powershell
python -m ml.data_processing.run_wind_analysis
```
