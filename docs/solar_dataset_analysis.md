# Solar Dataset Discovery and Analysis

## 1. Purpose

Milestone 5A inspects actual solar observations before solar preprocessing or training. Full-table statistics; no raw writes, copies, merges, conversions or models. Generic diagnostics and archive transport are reused unchanged; no wind feature constants are used.

## 2. Files Discovered

Repository root and ml/data were inspected. ml/data/raw/solar contains only .gitkeep; ml/data/solar is absent in this checkout. Archives are read in memory. Other archive members retain their existing wind inventory.

| File | Bytes | Sheet | Status |
| --- | --- | --- | --- |
| data_original.rar | 77966660 |  | archive screened by member names; all solar members inspected |
| data_original.rar!data_original/solar_stations/Solar station site 1 (Nominal capacity-50MW).xlsx | 3738807 | sheet1 | solar candidate |
| data_original.rar!data_original/solar_stations/Solar station site 2 (Nominal capacity-130MW).xlsx | 4365111 | sheet1 | solar candidate |
| data_original.rar!data_original/solar_stations/Solar station site 3 (Nominal capacity-30MW).xlsx | 3444470 | Sheet1 | solar candidate |
| data_original.rar!data_original/solar_stations/Solar station site 4 (Nominal capacity-130MW).xlsx | 6487609 | Sheet1 | solar candidate |
| data_original.rar!data_original/solar_stations/Solar station site 5 (Nominal capacity-110MW).xlsx | 3465493 | Sheet1 | solar candidate |
| data_original.rar!data_original/solar_stations/Solar station site 6 (Nominal capacity-35MW).xlsx | 4284319 | Sheet1 | solar candidate |
| data_original.rar!data_original/solar_stations/Solar station site 7 (Nominal capacity-30MW).xlsx | 4302012 | Sheet1 | solar candidate |
| data_original.rar!data_original/solar_stations/Solar station site 8 (Nominal capacity-30MW).xlsx | 4716036 | Sheet1 | solar candidate |
| data_processed.rar | 74468298 |  | archive screened by member names; all solar members inspected |
| data_processed.rar!data_processed/solar_stations/Solar station site 1 (Nominal capacity-50MW).xlsx | 3377039 | sheet1 | solar candidate |
| data_processed.rar!data_processed/solar_stations/Solar station site 2 (Nominal capacity-130MW).xlsx | 3983338 | sheet1 | solar candidate |
| data_processed.rar!data_processed/solar_stations/Solar station site 3 (Nominal capacity-30MW).xlsx | 1069047 | Sheet1 | solar candidate |
| data_processed.rar!data_processed/solar_stations/Solar station site 4 (Nominal capacity-130MW).xlsx | 6479911 | Sheet1 | solar candidate |
| data_processed.rar!data_processed/solar_stations/Solar station site 5 (Nominal capacity-110MW).xlsx | 3470280 | Sheet1 | solar candidate |
| data_processed.rar!data_processed/solar_stations/Solar station site 6 (Nominal capacity-35MW).xlsx | 4285324 | Sheet1 | solar candidate |
| data_processed.rar!data_processed/solar_stations/Solar station site 7 (Nominal capacity-30MW).xlsx | 4460611 | Sheet1 | solar candidate |
| data_processed.rar!data_processed/solar_stations/Solar station site 8 (Nominal capacity-30MW).xlsx | 4717372 | Sheet1 | solar candidate |
| ml/data/processed/wind_site_1_prepared.csv | 20540578 |  | screened: no solar evidence |
| ml/data/raw/wind/Wind farm site 1 (Nominal capacity-99MW).xlsx | 8299552 | sheet1 | screened: no solar name/irradiance header evidence |
| requirements.txt | 191 |  | screened: no solar evidence |
| Solar station site 1 (Nominal capacity-50MW).xlsx | 3738807 | sheet1 | solar candidate |
| SS_correlation.png | 191180 |  | image; not used as measurement evidence |
| Wind farm site 1 (Nominal capacity-99MW).xlsx | 8299552 | sheet1 | screened: no solar name/irradiance header evidence |

## 3. Dataset Schemas

### data_original.rar!data_original/solar_stations/Solar station site 1 (Nominal capacity-50MW).xlsx [sheet1]
Rows: 70176; columns: 8; format: .xlsx.

| Exact header (JSON quoted) | dtype | Missing | Missing % | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | object | 0 | 0.0 | None | None | None | None |
| "Total solar irradiance (W/m2)" | int64 | 0 | 0.0 | -99.0 | 1359.0 | 266.0510003419973 | 5.0 |
| "Direct normal irradiance (W/m2)" | int64 | 0 | 0.0 | -99.0 | 980.0 | 93.16146545827634 | 1.0 |
| "Global horizontal irradiance (W/m2)" | int64 | 0 | 0.0 | -99.0 | 989.0 | 67.55383606931144 | 4.0 |
| "Air temperature  (°C) " | float64 | 0 | 0.0 | -99.0 | 41.2 | 13.042668433652532 | 15.0 |
| "Atmosphere (hpa)" | float64 | 0 | 0.0 | -99.0 | 936.3 | 912.5075837893296 | 913.3 |
| "Relative humidity (%)" | float64 | 0 | 0.0 | -99.0 | 6553.5 | 650.6998247264022 | 21.0 |
| "Power (MW)" | float64 | 0 | 0.0 | 0.0 | 48.32173 | 9.669416544730392 | 0.0 |

Example values (first row only):

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:00:00",
    "Total solar irradiance (W/m2)": 0,
    "Direct normal irradiance (W/m2)": 0,
    "Global horizontal irradiance (W/m2)": 0,
    "Air temperature  (°C) ": -11.7,
    "Atmosphere (hpa)": 930.5,
    "Relative humidity (%)": 39.1,
    "Power (MW)": 0.0
  }
]
```

### data_original.rar!data_original/solar_stations/Solar station site 2 (Nominal capacity-130MW).xlsx [sheet1]
Rows: 70176; columns: 8; format: .xlsx.

| Exact header (JSON quoted) | dtype | Missing | Missing % | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | object | 0 | 0.0 | None | None | None | None |
| "Total solar irradiance (W/m2)" | float64 | 0 | 0.0 | -99.0 | 1041.93 | 166.8754998860009 | 0.0 |
| "Direct normal irradiance (W/m2)" | float64 | 0 | 0.0 | -99.0 | 751.75 | 120.12222241222071 | 0.0 |
| "Global horicontal irradiance (W/m2)" | float64 | 0 | 0.0 | -99.0 | 561.8 | 76.5440275877793 | 0.0 |
| "Air temperature  (°C) " | float64 | 0 | 0.0 | -99.0 | 40.47 | 12.541515047879617 | 15.31 |
| "Atmosphere (hpa)" | float64 | 0 | 0.0 | -99.0 | 881.67 | 851.3060990937073 | 860.71 |
| "Relative humidity (%)" | float64 | 0 | 0.0 | -99.0 | 6553.44 | 140.404341370269 | 22.28 |
| "Power (MW)" | float64 | 0 | 0.0 | 0.0 | 109.3603 | 19.57157019428779 | 0.3269 |

Example values (first row only):

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:00:00",
    "Total solar irradiance (W/m2)": 0.0,
    "Direct normal irradiance (W/m2)": 0.0,
    "Global horicontal irradiance (W/m2)": 0.0,
    "Air temperature  (°C) ": -9.62,
    "Atmosphere (hpa)": 872.81,
    "Relative humidity (%)": 47.94,
    "Power (MW)": 0.269033
  }
]
```

### data_original.rar!data_original/solar_stations/Solar station site 3 (Nominal capacity-30MW).xlsx [Sheet1]
Rows: 52608; columns: 8; format: .xlsx.

| Exact header (JSON quoted) | dtype | Missing | Missing % | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | datetime64[ns] | 0 | 0.0 | None | None | None | None |
| "Total solar irradiance (W/m2)" | float64 | 0 | 0.0 | 0.0 | 1117.0 | 81.14352361147728 | 1.62596 |
| "Direct normal irradiance (W/m2)" | int64 | 0 | 0.0 | 0.0 | 893.0 | 111.1159329379562 | 0.0 |
| "Global horizontal irradiance (W/m2)" | int64 | 0 | 0.0 | 0.0 | 656.0 | 66.3297597323601 | 0.0 |
| "Air temperature  (°C) " | float64 | 0 | 0.0 | -3276.7 | 3276.7 | -302.5224300486618 | 13.8 |
| "Atmosphere (hpa)" | float64 | 0 | 0.0 | 0.0 | 1044.4 | 1017.7516803527981 | 1018.5 |
| "Relative humidity (%)" | float64 | 0 | 0.0 | 0.0 | 3276.7 | 62.309087971411195 | 64.3 |
| "Power (MW)" | float64 | 0 | 0.0 | -0.063 | 29.9113395 | 5.210598531240495 | 0.0 |

Example values (first row only):

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:00:00.000",
    "Total solar irradiance (W/m2)": 0.0,
    "Direct normal irradiance (W/m2)": 0,
    "Global horizontal irradiance (W/m2)": 0,
    "Air temperature  (°C) ": -3270.9,
    "Atmosphere (hpa)": 1028.9,
    "Relative humidity (%)": 57.6,
    "Power (MW)": -0.0357
  }
]
```

### data_original.rar!data_original/solar_stations/Solar station site 4 (Nominal capacity-130MW).xlsx [Sheet1]
Rows: 70176; columns: 8; format: .xlsx.

| Exact header (JSON quoted) | dtype | Missing | Missing % | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | object | 0 | 0.0 | None | None | None | None |
| "Total solar irradiance (W/m2)" | float64 | 0 | 0.0 | 0.0 | 1237.4 | 150.11718939523482 | 0.0 |
| "Direct normal irradiance (W/m2)" | float64 | 0 | 0.0 | 0.0 | 1010.27256487175 | 138.92233082406568 | 0.0 |
| "Global horizontal irradiance (W/m2)" | float64 | 0 | 0.0 | 0.0 | 150.960268314169 | 20.75722673529134 | 0.0 |
| "Air temperature  (°C) " | float64 | 0 | 0.0 | -5.31873614994194 | 49.7996190860246 | 18.64315462271015 | 19.20875537463445 |
| "Atmosphere (hpa)" | float64 | 0 | 0.0 | 0.0 | 1100.31056206144 | 1005.7863824747349 | 1010.91545968965 |
| "Relative humidity (%)" | float64 | 0 | 0.0 | 0.0 | 100.0 | 65.88896263888411 | 66.46743336906894 |
| "Power (MW)" | float64 | 6 | 0.008549931600547196 | -0.44 | 114.688 | 16.468546472851646 | 0.078 |

Example values (first row only):

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:00:00.000",
    "Total solar irradiance (W/m2)": 0.0,
    "Direct normal irradiance (W/m2)": 0.0,
    "Global horizontal irradiance (W/m2)": 0.0,
    "Air temperature  (°C) ": -1.3329461794,
    "Atmosphere (hpa)": 1005.9406407839,
    "Relative humidity (%)": 87.6949447228,
    "Power (MW)": -0.273
  }
]
```

### data_original.rar!data_original/solar_stations/Solar station site 5 (Nominal capacity-110MW).xlsx [Sheet1]
Rows: 70176; columns: 8; format: .xlsx.

| Exact header (JSON quoted) | dtype | Missing | Missing % | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | datetime64[ns] | 0 | 0.0 | None | None | None | None |
| "Total solar irradiance (W/m2)" | object | 0 | 0.0 | None | None | None | None |
| "Direct normal irradiance (W/m2)" | object | 0 | 0.0 | None | None | None | None |
| "Global horizontal irradiance (W/m2)" | object | 0 | 0.0 | None | None | None | None |
| "Air temperature  (°C) " | object | 0 | 0.0 | None | None | None | None |
| "Atmosphere (hpa)" | object | 0 | 0.0 | None | None | None | None |
| "Relative humidity (%)" | object | 0 | 0.0 | None | None | None | None |
| "Power (MW)" | object | 0 | 0.0 | None | None | None | None |

Example values (first row only):

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:00:00.000",
    "Total solar irradiance (W/m2)": 0,
    "Direct normal irradiance (W/m2)": 0,
    "Global horizontal irradiance (W/m2)": 0,
    "Air temperature  (°C) ": 0.6,
    "Atmosphere (hpa)": 1037.9,
    "Relative humidity (%)": 83.1,
    "Power (MW)": 0
  }
]
```

### data_original.rar!data_original/solar_stations/Solar station site 6 (Nominal capacity-35MW).xlsx [Sheet1]
Rows: 70176; columns: 8; format: .xlsx.

| Exact header (JSON quoted) | dtype | Missing | Missing % | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | datetime64[ns] | 0 | 0.0 | None | None | None | None |
| "Total solar irradiance (W/m2)" | object | 0 | 0.0 | None | None | None | None |
| "Direct normal irradiance (W/m2)" | object | 0 | 0.0 | None | None | None | None |
| "Global horizontal irradiance (W/m2)" | object | 0 | 0.0 | None | None | None | None |
| "Air temperature  (°C) " | object | 0 | 0.0 | None | None | None | None |
| "Atmosphere (hpa)" | object | 0 | 0.0 | None | None | None | None |
| "Relative humidity (%)" | object | 0 | 0.0 | None | None | None | None |
| "Power (MW)" | float64 | 0 | 0.0 | 0.0 | 31.239334 | 6.36851536829973 | 0.0 |

Example values (first row only):

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:00:00.000",
    "Total solar irradiance (W/m2)": 0,
    "Direct normal irradiance (W/m2)": 0,
    "Global horizontal irradiance (W/m2)": 0,
    "Air temperature  (°C) ": 11.9,
    "Atmosphere (hpa)": 837.2,
    "Relative humidity (%)": 53.06,
    "Power (MW)": 0.0
  }
]
```

### data_original.rar!data_original/solar_stations/Solar station site 7 (Nominal capacity-30MW).xlsx [Sheet1]
Rows: 70176; columns: 8; format: .xlsx.

| Exact header (JSON quoted) | dtype | Missing | Missing % | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | datetime64[ns] | 0 | 0.0 | None | None | None | None |
| "Total solar irradiance (W/m2)" | object | 0 | 0.0 | None | None | None | None |
| "Direct normal irradiance (W/m2)" | object | 0 | 0.0 | None | None | None | None |
| "Global horizontal irradiance (W/m2)" | object | 0 | 0.0 | None | None | None | None |
| "Air temperature  (°C) " | object | 0 | 0.0 | None | None | None | None |
| "Atmosphere (hpa)" | object | 0 | 0.0 | None | None | None | None |
| "Relative humidity (%)" | object | 0 | 0.0 | None | None | None | None |
| "Power (MW)" | float64 | 0 | 0.0 | 0.0 | 29.775333 | 5.411922601045942 | 0.0 |

Example values (first row only):

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:00:00.000",
    "Total solar irradiance (W/m2)": 0,
    "Direct normal irradiance (W/m2)": 0,
    "Global horizontal irradiance (W/m2)": 0,
    "Air temperature  (°C) ": 4.6,
    "Atmosphere (hpa)": 862.5,
    "Relative humidity (%)": 40.97,
    "Power (MW)": 0.0
  }
]
```

### data_original.rar!data_original/solar_stations/Solar station site 8 (Nominal capacity-30MW).xlsx [Sheet1]
Rows: 69408; columns: 8; format: .xlsx.

| Exact header (JSON quoted) | dtype | Missing | Missing % | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | datetime64[ns] | 0 | 0.0 | None | None | None | None |
| "Total solar irradiance (W/m2)" | float64 | 0 | 0.0 | 0.0 | 1214.54 | 163.24392663669894 | 0.0 |
| "Direct normal irradiance (W/m2)" | float64 | 0 | 0.0 | 0.0 | 1056.650339 | 142.02223113829447 | 0.0 |
| "Global horizontal irradiance (W/m2)" | float64 | 0 | 0.0 | 0.0 | 157.8902806 | 21.221707551800485 | 0.0 |
| "Air temperature  (°C) " | float64 | 0 | 0.0 | -8.04 | 47.63 | 18.0096503538057 | 18.19 |
| "Atmosphere (hpa)" | float64 | 0 | 0.0 | 881.4 | 1037.78 | 956.4192689867365 | 956.07 |
| "Relative humidity (%)" | float64 | 0 | 0.0 | 11.83 | 100.0 | 71.70595580663093 | 73.53 |
| "Power (MW)" | float64 | 0 | 0.0 | 0.0 | 29.41 | 4.230664476717382 | 0.0 |

Example values (first row only):

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:00:00.000",
    "Total solar irradiance (W/m2)": 0.0,
    "Direct normal irradiance (W/m2)": 0.0,
    "Global horizontal irradiance (W/m2)": 0.0,
    "Air temperature  (°C) ": 2.960593318,
    "Atmosphere (hpa)": 948.9191176,
    "Relative humidity (%)": 69.25049758,
    "Power (MW)": 0.0
  }
]
```

### data_processed.rar!data_processed/solar_stations/Solar station site 1 (Nominal capacity-50MW).xlsx [sheet1]
Rows: 70176; columns: 7; format: .xlsx.

| Exact header (JSON quoted) | dtype | Missing | Missing % | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | object | 0 | 0.0 | None | None | None | None |
| "Total solar irradiance (W/m2)" | int64 | 0 | 0.0 | 0.0 | 1359.0 | 266.2073358413133 | 5.0 |
| "Direct normal irradiance (W/m2)" | int64 | 0 | 0.0 | 0.0 | 980.0 | 93.25699669402644 | 1.0 |
| "Global horizontal irradiance (W/m2)" | int64 | 0 | 0.0 | 0.0 | 989.0 | 67.69262995896032 | 4.0 |
| "Air temperature  (°C) " | float64 | 0 | 0.0 | -18.2 | 41.2 | 13.148167464660283 | 15.1 |
| "Atmosphere (hpa)" | float64 | 0 | 0.0 | 894.0 | 936.3 | 913.3671483128135 | 913.3 |
| "Power (MW)" | float64 | 0 | 0.0 | 0.0 | 48.32173 | 9.669360930389306 | 0.0 |

Example values (first row only):

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:00:00",
    "Total solar irradiance (W/m2)": 0,
    "Direct normal irradiance (W/m2)": 0,
    "Global horizontal irradiance (W/m2)": 0,
    "Air temperature  (°C) ": -11.7,
    "Atmosphere (hpa)": 930.5,
    "Power (MW)": 0.0
  }
]
```

### data_processed.rar!data_processed/solar_stations/Solar station site 2 (Nominal capacity-130MW).xlsx [sheet1]
Rows: 70176; columns: 7; format: .xlsx.

| Exact header (JSON quoted) | dtype | Missing | Missing % | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | object | 0 | 0.0 | None | None | None | None |
| "Total solar irradiance (W/m2)" | float64 | 0 | 0.0 | 0.0 | 1041.93 | 169.30336653556773 | 0.0 |
| "Direct normal irradiance (W/m2)" | float64 | 0 | 0.0 | 0.0 | 751.75 | 122.1523955483356 | 0.0 |
| "Global horizontal irradiance (W/m2)" | float64 | 0 | 0.0 | 0.0 | 561.8 | 78.29928152074784 | 0.0 |
| "Air temperature  (°C) " | float64 | 0 | 0.0 | -13.92 | 40.47 | 13.695107586639308 | 15.46 |
| "Atmosphere (hpa)" | float64 | 0 | 0.0 | 844.51 | 881.67 | 861.0362623974008 | 860.87 |
| "Power (MW)" | float64 | 0 | 0.0 | 0.0 | 109.3603 | 19.567488451669234 | 0.3269 |

Example values (first row only):

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:00:00",
    "Total solar irradiance (W/m2)": 0.0,
    "Direct normal irradiance (W/m2)": 0.0,
    "Global horizontal irradiance (W/m2)": 0.0,
    "Air temperature  (°C) ": -9.62,
    "Atmosphere (hpa)": 872.81,
    "Power (MW)": 0.269033
  }
]
```

### data_processed.rar!data_processed/solar_stations/Solar station site 3 (Nominal capacity-30MW).xlsx [Sheet1]
Rows: 20352; columns: 7; format: .xlsx.

| Exact header (JSON quoted) | dtype | Missing | Missing % | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | datetime64[ns] | 0 | 0.0 | None | None | None | None |
| "Total solar irradiance (W/m2)" | int64 | 0 | 0.0 | 0.0 | 1117.0 | 198.8134335691824 | 0.0 |
| "Direct normal irradiance (W/m2)" | int64 | 0 | 0.0 | 0.0 | 760.0 | 100.72955974842768 | 0.0 |
| "Global horizontal irradiance (W/m2)" | int64 | 0 | 0.0 | 0.0 | 656.0 | 69.305080581761 | 0.0 |
| "Atmosphere (hpa)" | float64 | 0 | 0.0 | 994.8 | 1038.6 | 1016.0137676886794 | 1014.7 |
| "Relative humidity (%)" | float64 | 0 | 0.0 | 14.1 | 80.5 | 58.249243317610066 | 61.0 |
| "Power (MW)" | float64 | 0 | 0.0 | -0.063 | 29.9113395 | 5.449246788104363 | 0.115101 |

Example values (first row only):

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:00:00.000",
    "Total solar irradiance (W/m2)": 0,
    "Direct normal irradiance (W/m2)": 0,
    "Global horizontal irradiance (W/m2)": 0,
    "Atmosphere (hpa)": 1028.9,
    "Relative humidity (%)": 57.6,
    "Power (MW)": -0.0357
  }
]
```

### data_processed.rar!data_processed/solar_stations/Solar station site 4 (Nominal capacity-130MW).xlsx [Sheet1]
Rows: 70176; columns: 8; format: .xlsx.

| Exact header (JSON quoted) | dtype | Missing | Missing % | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | object | 0 | 0.0 | None | None | None | None |
| "Total solar irradiance (W/m2)" | float64 | 0 | 0.0 | 0.0 | 1237.4 | 150.15481737346101 | 0.0 |
| "Direct normal irradiance (W/m2)" | float64 | 0 | 0.0 | 0.0 | 1010.27256487175 | 139.5115814412417 | 0.0 |
| "Global horizontal irradiance (W/m2)" | float64 | 0 | 0.0 | 0.0 | 150.960268314169 | 20.84527567808776 | 0.0 |
| "Air temperature  (°C) " | float64 | 0 | 0.0 | -5.31873614994194 | 49.7996190860246 | 18.716369112034823 | 19.261013922330697 |
| "Atmosphere (hpa)" | float64 | 0 | 0.0 | 928.598377167773 | 1100.31056206144 | 1011.3737482909615 | 1011.20001912569 |
| "Relative humidity (%)" | float64 | 0 | 0.0 | 18.5036549489169 | 100.0 | 66.24012304536782 | 66.56264061585635 |
| "Power (MW)" | float64 | 6 | 0.008549931600547196 | -0.44 | 114.688 | 16.455695126122272 | 0.078 |

Example values (first row only):

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:00:00.000",
    "Total solar irradiance (W/m2)": 0.0,
    "Direct normal irradiance (W/m2)": 0.0,
    "Global horizontal irradiance (W/m2)": 0.0,
    "Air temperature  (°C) ": -1.3329461794,
    "Atmosphere (hpa)": 1005.9406407839,
    "Relative humidity (%)": 87.6949447228,
    "Power (MW)": -0.273
  }
]
```

### data_processed.rar!data_processed/solar_stations/Solar station site 5 (Nominal capacity-110MW).xlsx [Sheet1]
Rows: 70176; columns: 8; format: .xlsx.

| Exact header (JSON quoted) | dtype | Missing | Missing % | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | datetime64[ns] | 0 | 0.0 | None | None | None | None |
| "Total solar irradiance (W/m2)" | int64 | 0 | 0.0 | 0.0 | 1467.0 | 164.59610123119015 | 0.0 |
| "Direct normal irradiance (W/m2)" | int64 | 0 | 0.0 | 0.0 | 1962.0 | 148.10131668946647 | 1.0 |
| "Global horizontal irradiance (W/m2)" | int64 | 0 | 0.0 | 0.0 | 1208.0 | 115.27204457364341 | 0.0 |
| "Air temperature  (°C) " | float64 | 0 | 0.0 | -6.6 | 39.5 | 17.78077975376197 | 18.7 |
| "Atmosphere (hpa)" | float64 | 0 | 0.0 | 990.7 | 1039.4 | 1011.9912648198814 | 1012.2 |
| "Relative humidity (%)" | float64 | 0 | 0.0 | 10.6 | 93.2 | 71.58947218422253 | 77.2 |
| "Power (MW)" | float64 | 0 | 0.0 | -0.54 | 99.55 | 14.513072132922938 | 0.0 |

Example values (first row only):

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:00:00.000",
    "Total solar irradiance (W/m2)": 0,
    "Direct normal irradiance (W/m2)": 0,
    "Global horizontal irradiance (W/m2)": 0,
    "Air temperature  (°C) ": 0.6,
    "Atmosphere (hpa)": 1037.9,
    "Relative humidity (%)": 83.1,
    "Power (MW)": 0.0
  }
]
```

### data_processed.rar!data_processed/solar_stations/Solar station site 6 (Nominal capacity-35MW).xlsx [Sheet1]
Rows: 70176; columns: 8; format: .xlsx.

| Exact header (JSON quoted) | dtype | Missing | Missing % | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | datetime64[ns] | 0 | 0.0 | None | None | None | None |
| "Total solar irradiance (W/m2)" | float64 | 0 | 0.0 | 0.0 | 1365.4 | 243.08193456656062 | 0.06666667 |
| "Direct normal irradiance (W/m2)" | float64 | 0 | 0.0 | 0.0 | 1179.8 | 215.1498262226405 | 0.0 |
| "Global horizontal irradiance (W/m2)" | float64 | 0 | 0.0 | 0.0 | 296.2 | 53.92730949951344 | 0.0 |
| "Air temperature  (°C) " | float64 | 0 | 0.0 | 2.9466667 | 36.693333 | 20.62948917147458 | 20.68 |
| "Atmosphere (hpa)" | float64 | 0 | 0.0 | 389.82 | 846.0733 | 830.6714380534656 | 830.42 |
| "Relative humidity (%)" | float64 | 0 | 0.0 | 1.4133333 | 97.9 | 53.94283213849607 | 52.486668 |
| "Power (MW)" | float64 | 0 | 0.0 | 0.0 | 31.239334 | 6.364345823162932 | 0.0 |

Example values (first row only):

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:00:00.000",
    "Total solar irradiance (W/m2)": 0.0,
    "Direct normal irradiance (W/m2)": 0.0,
    "Global horizontal irradiance (W/m2)": 0.0,
    "Air temperature  (°C) ": 11.9,
    "Atmosphere (hpa)": 837.2,
    "Relative humidity (%)": 53.06,
    "Power (MW)": 0.0
  }
]
```

### data_processed.rar!data_processed/solar_stations/Solar station site 7 (Nominal capacity-30MW).xlsx [Sheet1]
Rows: 70176; columns: 8; format: .xlsx.

| Exact header (JSON quoted) | dtype | Missing | Missing % | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | datetime64[ns] | 0 | 0.0 | None | None | None | None |
| "Total solar irradiance (W/m2)" | float64 | 0 | 0.0 | 0.0 | 1393.733333 | 206.0824669133607 | 2.6 |
| "Direct normal irradiance (W/m2)" | float64 | 0 | 0.0 | 0.0 | 1095.4 | 182.99632227089032 | 0.0 |
| "Global horizontal irradiance (W/m2)" | float64 | 0 | 0.0 | 0.0 | 1125.133333 | 108.6800597563982 | 2.0 |
| "Air temperature  (°C) " | float64 | 0 | 0.0 | -4.263333 | 30.12 | 13.739213486605108 | 14.36 |
| "Atmosphere (hpa)" | float64 | 0 | 0.0 | 398.206667 | 867.1 | 842.9337953072275 | 854.412667 |
| "Relative humidity (%)" | float64 | 0 | 0.0 | 1.953333 | 100.94 | 55.18065928303123 | 54.869 |
| "Power (MW)" | float64 | 0 | 0.0 | 0.0 | 29.775333 | 5.409623686730507 | 0.0 |

Example values (first row only):

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:00:00.000",
    "Total solar irradiance (W/m2)": 0.0,
    "Direct normal irradiance (W/m2)": 0.0,
    "Global horizontal irradiance (W/m2)": 0.0,
    "Air temperature  (°C) ": 4.6,
    "Atmosphere (hpa)": 862.5,
    "Relative humidity (%)": 40.97,
    "Power (MW)": 0.0
  }
]
```

### data_processed.rar!data_processed/solar_stations/Solar station site 8 (Nominal capacity-30MW).xlsx [Sheet1]
Rows: 69408; columns: 8; format: .xlsx.

| Exact header (JSON quoted) | dtype | Missing | Missing % | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | datetime64[ns] | 0 | 0.0 | None | None | None | None |
| "Total solar irradiance (W/m2)" | float64 | 0 | 0.0 | 0.0 | 1214.54 | 163.24392663669894 | 0.0 |
| "Direct normal irradiance (W/m2)" | float64 | 0 | 0.0 | 0.0 | 1056.650339 | 142.02223113829447 | 0.0 |
| "Global horizontal irradiance (W/m2)" | float64 | 0 | 0.0 | 0.0 | 157.8902806 | 21.221707551800485 | 0.0 |
| "Air temperature  (°C) " | float64 | 0 | 0.0 | -8.04 | 47.63 | 18.0096503538057 | 18.19 |
| "Atmosphere (hpa)" | float64 | 0 | 0.0 | 881.4 | 1037.78 | 956.4192689867365 | 956.07 |
| "Relative humidity (%)" | float64 | 0 | 0.0 | 11.83 | 100.0 | 71.70595580663093 | 73.53 |
| "Power (MW)" | float64 | 0 | 0.0 | 0.0 | 29.41 | 4.230664476717382 | 0.0 |

Example values (first row only):

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01T00:00:00.000",
    "Total solar irradiance (W/m2)": 0.0,
    "Direct normal irradiance (W/m2)": 0.0,
    "Global horizontal irradiance (W/m2)": 0.0,
    "Air temperature  (°C) ": 2.960593318,
    "Atmosphere (hpa)": 948.9191176,
    "Relative humidity (%)": 69.25049758,
    "Power (MW)": 0.0
  }
]
```

### Solar station site 1 (Nominal capacity-50MW).xlsx [sheet1]
Rows: 70176; columns: 8; format: .xlsx.

| Exact header (JSON quoted) | dtype | Missing | Missing % | Min | Max | Mean | Median |
| --- | --- | --- | --- | --- | --- | --- | --- |
| "Time(year-month-day h:m:s)" | object | 0 | 0.0 | None | None | None | None |
| "Total solar irradiance (W/m2)" | int64 | 0 | 0.0 | -99.0 | 1359.0 | 266.0510003419973 | 5.0 |
| "Direct normal irradiance (W/m2)" | int64 | 0 | 0.0 | -99.0 | 980.0 | 93.16146545827634 | 1.0 |
| "Global horizontal irradiance (W/m2)" | int64 | 0 | 0.0 | -99.0 | 989.0 | 67.55383606931144 | 4.0 |
| "Air temperature  (°C) " | float64 | 0 | 0.0 | -99.0 | 41.2 | 13.042668433652532 | 15.0 |
| "Atmosphere (hpa)" | float64 | 0 | 0.0 | -99.0 | 936.3 | 912.5075837893296 | 913.3 |
| "Relative humidity (%)" | float64 | 0 | 0.0 | -99.0 | 6553.5 | 650.6998247264022 | 21.0 |
| "Power (MW)" | float64 | 0 | 0.0 | 0.0 | 48.32173 | 9.669416544730392 | 0.0 |

Example values (first row only):

```json
[
  {
    "Time(year-month-day h:m:s)": "2019-01-01 00:00:00",
    "Total solar irradiance (W/m2)": 0,
    "Direct normal irradiance (W/m2)": 0,
    "Global horizontal irradiance (W/m2)": 0,
    "Air temperature  (°C) ": -11.7,
    "Atmosphere (hpa)": 930.5,
    "Relative humidity (%)": 39.1,
    "Power (MW)": 0.0
  }
]
```

## 4. Timestamp Analysis

### data_original.rar!data_original/solar_stations/Solar station site 1 (Nominal capacity-50MW).xlsx [sheet1]

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
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values.",
    "missing_intervals_on_modal_grid": 0
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 2 (Nominal capacity-130MW).xlsx [sheet1]

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
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values.",
    "missing_intervals_on_modal_grid": 0
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 3 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "Time(year-month-day h:m:s)": {
    "column": "Time(year-month-day h:m:s)",
    "status": "parsed diagnostic copy",
    "non_null": 52608,
    "parsed": 52608,
    "parse_failures": 0,
    "ambiguous_day_month_values": 0,
    "missing": 0,
    "earliest": "2019-01-01 00:00:00+00:00",
    "latest": "2020-07-01 23:45:00+00:00",
    "unique_timestamps": 52608,
    "duplicate_timestamps": 0,
    "ascending_valid_values": true,
    "descending_valid_values": false,
    "timezone": "not documented in values (naive)",
    "estimated_frequency": "0 days 00:15:00",
    "regular_unique_spacing": true,
    "interval_counts": {
      "0 days 00:15:00": 52607
    },
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values.",
    "missing_intervals_on_modal_grid": 0
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 4 (Nominal capacity-130MW).xlsx [Sheet1]

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
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values.",
    "missing_intervals_on_modal_grid": 0
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 5 (Nominal capacity-110MW).xlsx [Sheet1]

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
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values.",
    "missing_intervals_on_modal_grid": 0
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 6 (Nominal capacity-35MW).xlsx [Sheet1]

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
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values.",
    "missing_intervals_on_modal_grid": 0
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 7 (Nominal capacity-30MW).xlsx [Sheet1]

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
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values.",
    "missing_intervals_on_modal_grid": 0
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 8 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "Time(year-month-day h:m:s)": {
    "column": "Time(year-month-day h:m:s)",
    "status": "parsed diagnostic copy",
    "non_null": 69408,
    "parsed": 69408,
    "parse_failures": 0,
    "ambiguous_day_month_values": 0,
    "missing": 0,
    "earliest": "2019-01-01 00:00:00+00:00",
    "latest": "2020-12-31 23:45:00+00:00",
    "unique_timestamps": 69408,
    "duplicate_timestamps": 0,
    "ascending_valid_values": true,
    "descending_valid_values": false,
    "timezone": "not documented in values (naive)",
    "estimated_frequency": "0 days 00:15:00",
    "regular_unique_spacing": false,
    "interval_counts": {
      "0 days 00:15:00": 69401,
      "1 days 00:15:00": 5,
      "3 days 00:15:00": 1
    },
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values.",
    "missing_intervals_on_modal_grid": 768
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 1 (Nominal capacity-50MW).xlsx [sheet1]

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
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values.",
    "missing_intervals_on_modal_grid": 0
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 2 (Nominal capacity-130MW).xlsx [sheet1]

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
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values.",
    "missing_intervals_on_modal_grid": 0
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 3 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "Time(year-month-day h:m:s)": {
    "column": "Time(year-month-day h:m:s)",
    "status": "parsed diagnostic copy",
    "non_null": 20352,
    "parsed": 20352,
    "parse_failures": 0,
    "ambiguous_day_month_values": 0,
    "missing": 0,
    "earliest": "2019-01-01 00:00:00+00:00",
    "latest": "2019-07-31 23:45:00+00:00",
    "unique_timestamps": 20352,
    "duplicate_timestamps": 0,
    "ascending_valid_values": true,
    "descending_valid_values": false,
    "timezone": "not documented in values (naive)",
    "estimated_frequency": "0 days 00:15:00",
    "regular_unique_spacing": true,
    "interval_counts": {
      "0 days 00:15:00": 20351
    },
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values.",
    "missing_intervals_on_modal_grid": 0
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 4 (Nominal capacity-130MW).xlsx [Sheet1]

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
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values.",
    "missing_intervals_on_modal_grid": 0
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 5 (Nominal capacity-110MW).xlsx [Sheet1]

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
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values.",
    "missing_intervals_on_modal_grid": 0
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 6 (Nominal capacity-35MW).xlsx [Sheet1]

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
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values.",
    "missing_intervals_on_modal_grid": 0
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 7 (Nominal capacity-30MW).xlsx [Sheet1]

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
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values.",
    "missing_intervals_on_modal_grid": 0
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 8 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "Time(year-month-day h:m:s)": {
    "column": "Time(year-month-day h:m:s)",
    "status": "parsed diagnostic copy",
    "non_null": 69408,
    "parsed": 69408,
    "parse_failures": 0,
    "ambiguous_day_month_values": 0,
    "missing": 0,
    "earliest": "2019-01-01 00:00:00+00:00",
    "latest": "2020-12-31 23:45:00+00:00",
    "unique_timestamps": 69408,
    "duplicate_timestamps": 0,
    "ascending_valid_values": true,
    "descending_valid_values": false,
    "timezone": "not documented in values (naive)",
    "estimated_frequency": "0 days 00:15:00",
    "regular_unique_spacing": false,
    "interval_counts": {
      "0 days 00:15:00": 69401,
      "1 days 00:15:00": 5,
      "3 days 00:15:00": 1
    },
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values.",
    "missing_intervals_on_modal_grid": 768
  }
}
```

### Solar station site 1 (Nominal capacity-50MW).xlsx [sheet1]

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
    "note": "UTC suffix in diagnostic bounds is not evidence of source timezone; frequency uses sorted unique valid values.",
    "missing_intervals_on_modal_grid": 0
  }
}
```

## 5. Candidate Generation Targets

### data_original.rar!data_original/solar_stations/Solar station site 1 (Nominal capacity-50MW).xlsx [sheet1]

```json
{
  "Power (MW)": {
    "dtype": "float64",
    "unit_in_header": "MW",
    "measurement": "POWER",
    "evidence": "VERIFIED header label only; metering, AC/DC and averaging convention UNRESOLVED",
    "statistics": {
      "min": 0.0,
      "max": 48.32173,
      "mean": 9.669416544730392,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 35264,
      "iqr_outliers": 44
    },
    "missing": {
      "count": 0,
      "percent": 0.0
    },
    "ml_suitability": "candidate after quality review",
    "above_filename_capacity_label": 0
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 2 (Nominal capacity-130MW).xlsx [sheet1]

```json
{
  "Power (MW)": {
    "dtype": "float64",
    "unit_in_header": "MW",
    "measurement": "POWER",
    "evidence": "VERIFIED header label only; metering, AC/DC and averaging convention UNRESOLVED",
    "statistics": {
      "min": 0.0,
      "max": 109.3603,
      "mean": 19.57157019428779,
      "median": 0.3269,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 118,
      "iqr_outliers": 1064
    },
    "missing": {
      "count": 0,
      "percent": 0.0
    },
    "ml_suitability": "candidate after quality review",
    "above_filename_capacity_label": 0
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 3 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "Power (MW)": {
    "dtype": "float64",
    "unit_in_header": "MW",
    "measurement": "POWER",
    "evidence": "VERIFIED header label only; metering, AC/DC and averaging convention UNRESOLVED",
    "statistics": {
      "min": -0.063,
      "max": 29.9113395,
      "mean": 5.210598531240495,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 25652,
      "zero": 700,
      "iqr_outliers": 4494
    },
    "missing": {
      "count": 0,
      "percent": 0.0
    },
    "ml_suitability": "candidate after quality review",
    "above_filename_capacity_label": 0
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 4 (Nominal capacity-130MW).xlsx [Sheet1]

```json
{
  "Power (MW)": {
    "dtype": "float64",
    "unit_in_header": "MW",
    "measurement": "POWER",
    "evidence": "VERIFIED header label only; metering, AC/DC and averaging convention UNRESOLVED",
    "statistics": {
      "min": -0.44,
      "max": 114.688,
      "mean": 16.468546472851646,
      "median": 0.078,
      "missing": 6,
      "non_finite_non_null": 0,
      "negative": 33878,
      "zero": 939,
      "iqr_outliers": 9376
    },
    "missing": {
      "count": 6,
      "percent": 0.008549931600547196
    },
    "ml_suitability": "candidate after quality review",
    "above_filename_capacity_label": 0
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 5 (Nominal capacity-110MW).xlsx [Sheet1]

```json
{
  "Power (MW)": {
    "dtype": "object",
    "unit_in_header": "MW",
    "measurement": "POWER",
    "evidence": "VERIFIED header label only; metering, AC/DC and averaging convention UNRESOLVED",
    "statistics": null,
    "missing": {
      "count": 0,
      "percent": 0.0
    },
    "ml_suitability": "UNRESOLVED nonnumeric target"
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 6 (Nominal capacity-35MW).xlsx [Sheet1]

```json
{
  "Power (MW)": {
    "dtype": "float64",
    "unit_in_header": "MW",
    "measurement": "POWER",
    "evidence": "VERIFIED header label only; metering, AC/DC and averaging convention UNRESOLVED",
    "statistics": {
      "min": 0.0,
      "max": 31.239334,
      "mean": 6.36851536829973,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 35833,
      "iqr_outliers": 51
    },
    "missing": {
      "count": 0,
      "percent": 0.0
    },
    "ml_suitability": "candidate after quality review",
    "above_filename_capacity_label": 0
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 7 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "Power (MW)": {
    "dtype": "float64",
    "unit_in_header": "MW",
    "measurement": "POWER",
    "evidence": "VERIFIED header label only; metering, AC/DC and averaging convention UNRESOLVED",
    "statistics": {
      "min": 0.0,
      "max": 29.775333,
      "mean": 5.411922601045942,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 37855,
      "iqr_outliers": 2485
    },
    "missing": {
      "count": 0,
      "percent": 0.0
    },
    "ml_suitability": "candidate after quality review",
    "above_filename_capacity_label": 0
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 8 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "Power (MW)": {
    "dtype": "float64",
    "unit_in_header": "MW",
    "measurement": "POWER",
    "evidence": "VERIFIED header label only; metering, AC/DC and averaging convention UNRESOLVED",
    "statistics": {
      "min": 0.0,
      "max": 29.41,
      "mean": 4.230664476717382,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 35328,
      "iqr_outliers": 6579
    },
    "missing": {
      "count": 0,
      "percent": 0.0
    },
    "ml_suitability": "candidate after quality review",
    "above_filename_capacity_label": 0
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 1 (Nominal capacity-50MW).xlsx [sheet1]

```json
{
  "Power (MW)": {
    "dtype": "float64",
    "unit_in_header": "MW",
    "measurement": "POWER",
    "evidence": "VERIFIED header label only; metering, AC/DC and averaging convention UNRESOLVED",
    "statistics": {
      "min": 0.0,
      "max": 48.32173,
      "mean": 9.669360930389306,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 35266,
      "iqr_outliers": 44
    },
    "missing": {
      "count": 0,
      "percent": 0.0
    },
    "ml_suitability": "candidate after quality review",
    "above_filename_capacity_label": 0
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 2 (Nominal capacity-130MW).xlsx [sheet1]

```json
{
  "Power (MW)": {
    "dtype": "float64",
    "unit_in_header": "MW",
    "measurement": "POWER",
    "evidence": "VERIFIED header label only; metering, AC/DC and averaging convention UNRESOLVED",
    "statistics": {
      "min": 0.0,
      "max": 109.3603,
      "mean": 19.567488451669234,
      "median": 0.3269,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 118,
      "iqr_outliers": 1052
    },
    "missing": {
      "count": 0,
      "percent": 0.0
    },
    "ml_suitability": "candidate after quality review",
    "above_filename_capacity_label": 0
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 3 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "Power (MW)": {
    "dtype": "float64",
    "unit_in_header": "MW",
    "measurement": "POWER",
    "evidence": "VERIFIED header label only; metering, AC/DC and averaging convention UNRESOLVED",
    "statistics": {
      "min": -0.063,
      "max": 29.9113395,
      "mean": 5.449246788104363,
      "median": 0.115101,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 9517,
      "zero": 346,
      "iqr_outliers": 1435
    },
    "missing": {
      "count": 0,
      "percent": 0.0
    },
    "ml_suitability": "candidate after quality review",
    "above_filename_capacity_label": 0
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 4 (Nominal capacity-130MW).xlsx [Sheet1]

```json
{
  "Power (MW)": {
    "dtype": "float64",
    "unit_in_header": "MW",
    "measurement": "POWER",
    "evidence": "VERIFIED header label only; metering, AC/DC and averaging convention UNRESOLVED",
    "statistics": {
      "min": -0.44,
      "max": 114.688,
      "mean": 16.455695126122272,
      "median": 0.078,
      "missing": 6,
      "non_finite_non_null": 0,
      "negative": 33881,
      "zero": 936,
      "iqr_outliers": 9382
    },
    "missing": {
      "count": 6,
      "percent": 0.008549931600547196
    },
    "ml_suitability": "candidate after quality review",
    "above_filename_capacity_label": 0
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 5 (Nominal capacity-110MW).xlsx [Sheet1]

```json
{
  "Power (MW)": {
    "dtype": "float64",
    "unit_in_header": "MW",
    "measurement": "POWER",
    "evidence": "VERIFIED header label only; metering, AC/DC and averaging convention UNRESOLVED",
    "statistics": {
      "min": -0.54,
      "max": 99.55,
      "mean": 14.513072132922938,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 18055,
      "zero": 18621,
      "iqr_outliers": 9270
    },
    "missing": {
      "count": 0,
      "percent": 0.0
    },
    "ml_suitability": "candidate after quality review",
    "above_filename_capacity_label": 0
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 6 (Nominal capacity-35MW).xlsx [Sheet1]

```json
{
  "Power (MW)": {
    "dtype": "float64",
    "unit_in_header": "MW",
    "measurement": "POWER",
    "evidence": "VERIFIED header label only; metering, AC/DC and averaging convention UNRESOLVED",
    "statistics": {
      "min": 0.0,
      "max": 31.239334,
      "mean": 6.364345823162932,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 35839,
      "iqr_outliers": 52
    },
    "missing": {
      "count": 0,
      "percent": 0.0
    },
    "ml_suitability": "candidate after quality review",
    "above_filename_capacity_label": 0
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 7 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "Power (MW)": {
    "dtype": "float64",
    "unit_in_header": "MW",
    "measurement": "POWER",
    "evidence": "VERIFIED header label only; metering, AC/DC and averaging convention UNRESOLVED",
    "statistics": {
      "min": 0.0,
      "max": 29.775333,
      "mean": 5.409623686730507,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 37853,
      "iqr_outliers": 2519
    },
    "missing": {
      "count": 0,
      "percent": 0.0
    },
    "ml_suitability": "candidate after quality review",
    "above_filename_capacity_label": 0
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 8 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "Power (MW)": {
    "dtype": "float64",
    "unit_in_header": "MW",
    "measurement": "POWER",
    "evidence": "VERIFIED header label only; metering, AC/DC and averaging convention UNRESOLVED",
    "statistics": {
      "min": 0.0,
      "max": 29.41,
      "mean": 4.230664476717382,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 35328,
      "iqr_outliers": 6579
    },
    "missing": {
      "count": 0,
      "percent": 0.0
    },
    "ml_suitability": "candidate after quality review",
    "above_filename_capacity_label": 0
  }
}
```

### Solar station site 1 (Nominal capacity-50MW).xlsx [sheet1]

```json
{
  "Power (MW)": {
    "dtype": "float64",
    "unit_in_header": "MW",
    "measurement": "POWER",
    "evidence": "VERIFIED header label only; metering, AC/DC and averaging convention UNRESOLVED",
    "statistics": {
      "min": 0.0,
      "max": 48.32173,
      "mean": 9.669416544730392,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 35264,
      "iqr_outliers": 44
    },
    "missing": {
      "count": 0,
      "percent": 0.0
    },
    "ml_suitability": "candidate after quality review",
    "above_filename_capacity_label": 0
  }
}
```

## 6. Candidate Features

VERIFIED: exact header strings and explicit units. LIKELY: sensor categories inferred from those strings. UNRESOLVED: sensor plane, calibration, location and availability at forecast origin. Calendar candidates come only from parsed time columns; no features are created.

### data_original.rar!data_original/solar_stations/Solar station site 1 (Nominal capacity-50MW).xlsx [sheet1]

```json
{
  "irradiance": [
    "Total solar irradiance (W/m2)",
    "Direct normal irradiance (W/m2)",
    "Global horizontal irradiance (W/m2)"
  ],
  "temperature": [
    "Air temperature  (°C) "
  ],
  "humidity": [
    "Relative humidity (%)"
  ],
  "pressure": [
    "Atmosphere (hpa)"
  ],
  "wind": [],
  "cloud": [],
  "solar_angle": [],
  "site_metadata": []
}
```

### data_original.rar!data_original/solar_stations/Solar station site 2 (Nominal capacity-130MW).xlsx [sheet1]

```json
{
  "irradiance": [
    "Total solar irradiance (W/m2)",
    "Direct normal irradiance (W/m2)",
    "Global horicontal irradiance (W/m2)"
  ],
  "temperature": [
    "Air temperature  (°C) "
  ],
  "humidity": [
    "Relative humidity (%)"
  ],
  "pressure": [
    "Atmosphere (hpa)"
  ],
  "wind": [],
  "cloud": [],
  "solar_angle": [],
  "site_metadata": []
}
```

### data_original.rar!data_original/solar_stations/Solar station site 3 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "irradiance": [
    "Total solar irradiance (W/m2)",
    "Direct normal irradiance (W/m2)",
    "Global horizontal irradiance (W/m2)"
  ],
  "temperature": [
    "Air temperature  (°C) "
  ],
  "humidity": [
    "Relative humidity (%)"
  ],
  "pressure": [
    "Atmosphere (hpa)"
  ],
  "wind": [],
  "cloud": [],
  "solar_angle": [],
  "site_metadata": []
}
```

### data_original.rar!data_original/solar_stations/Solar station site 4 (Nominal capacity-130MW).xlsx [Sheet1]

```json
{
  "irradiance": [
    "Total solar irradiance (W/m2)",
    "Direct normal irradiance (W/m2)",
    "Global horizontal irradiance (W/m2)"
  ],
  "temperature": [
    "Air temperature  (°C) "
  ],
  "humidity": [
    "Relative humidity (%)"
  ],
  "pressure": [
    "Atmosphere (hpa)"
  ],
  "wind": [],
  "cloud": [],
  "solar_angle": [],
  "site_metadata": []
}
```

### data_original.rar!data_original/solar_stations/Solar station site 5 (Nominal capacity-110MW).xlsx [Sheet1]

```json
{
  "irradiance": [
    "Total solar irradiance (W/m2)",
    "Direct normal irradiance (W/m2)",
    "Global horizontal irradiance (W/m2)"
  ],
  "temperature": [
    "Air temperature  (°C) "
  ],
  "humidity": [
    "Relative humidity (%)"
  ],
  "pressure": [
    "Atmosphere (hpa)"
  ],
  "wind": [],
  "cloud": [],
  "solar_angle": [],
  "site_metadata": []
}
```

### data_original.rar!data_original/solar_stations/Solar station site 6 (Nominal capacity-35MW).xlsx [Sheet1]

```json
{
  "irradiance": [
    "Total solar irradiance (W/m2)",
    "Direct normal irradiance (W/m2)",
    "Global horizontal irradiance (W/m2)"
  ],
  "temperature": [
    "Air temperature  (°C) "
  ],
  "humidity": [
    "Relative humidity (%)"
  ],
  "pressure": [
    "Atmosphere (hpa)"
  ],
  "wind": [],
  "cloud": [],
  "solar_angle": [],
  "site_metadata": []
}
```

### data_original.rar!data_original/solar_stations/Solar station site 7 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "irradiance": [
    "Total solar irradiance (W/m2)",
    "Direct normal irradiance (W/m2)",
    "Global horizontal irradiance (W/m2)"
  ],
  "temperature": [
    "Air temperature  (°C) "
  ],
  "humidity": [
    "Relative humidity (%)"
  ],
  "pressure": [
    "Atmosphere (hpa)"
  ],
  "wind": [],
  "cloud": [],
  "solar_angle": [],
  "site_metadata": []
}
```

### data_original.rar!data_original/solar_stations/Solar station site 8 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "irradiance": [
    "Total solar irradiance (W/m2)",
    "Direct normal irradiance (W/m2)",
    "Global horizontal irradiance (W/m2)"
  ],
  "temperature": [
    "Air temperature  (°C) "
  ],
  "humidity": [
    "Relative humidity (%)"
  ],
  "pressure": [
    "Atmosphere (hpa)"
  ],
  "wind": [],
  "cloud": [],
  "solar_angle": [],
  "site_metadata": []
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 1 (Nominal capacity-50MW).xlsx [sheet1]

```json
{
  "irradiance": [
    "Total solar irradiance (W/m2)",
    "Direct normal irradiance (W/m2)",
    "Global horizontal irradiance (W/m2)"
  ],
  "temperature": [
    "Air temperature  (°C) "
  ],
  "humidity": [],
  "pressure": [
    "Atmosphere (hpa)"
  ],
  "wind": [],
  "cloud": [],
  "solar_angle": [],
  "site_metadata": []
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 2 (Nominal capacity-130MW).xlsx [sheet1]

```json
{
  "irradiance": [
    "Total solar irradiance (W/m2)",
    "Direct normal irradiance (W/m2)",
    "Global horizontal irradiance (W/m2)"
  ],
  "temperature": [
    "Air temperature  (°C) "
  ],
  "humidity": [],
  "pressure": [
    "Atmosphere (hpa)"
  ],
  "wind": [],
  "cloud": [],
  "solar_angle": [],
  "site_metadata": []
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 3 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "irradiance": [
    "Total solar irradiance (W/m2)",
    "Direct normal irradiance (W/m2)",
    "Global horizontal irradiance (W/m2)"
  ],
  "temperature": [],
  "humidity": [
    "Relative humidity (%)"
  ],
  "pressure": [
    "Atmosphere (hpa)"
  ],
  "wind": [],
  "cloud": [],
  "solar_angle": [],
  "site_metadata": []
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 4 (Nominal capacity-130MW).xlsx [Sheet1]

```json
{
  "irradiance": [
    "Total solar irradiance (W/m2)",
    "Direct normal irradiance (W/m2)",
    "Global horizontal irradiance (W/m2)"
  ],
  "temperature": [
    "Air temperature  (°C) "
  ],
  "humidity": [
    "Relative humidity (%)"
  ],
  "pressure": [
    "Atmosphere (hpa)"
  ],
  "wind": [],
  "cloud": [],
  "solar_angle": [],
  "site_metadata": []
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 5 (Nominal capacity-110MW).xlsx [Sheet1]

```json
{
  "irradiance": [
    "Total solar irradiance (W/m2)",
    "Direct normal irradiance (W/m2)",
    "Global horizontal irradiance (W/m2)"
  ],
  "temperature": [
    "Air temperature  (°C) "
  ],
  "humidity": [
    "Relative humidity (%)"
  ],
  "pressure": [
    "Atmosphere (hpa)"
  ],
  "wind": [],
  "cloud": [],
  "solar_angle": [],
  "site_metadata": []
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 6 (Nominal capacity-35MW).xlsx [Sheet1]

```json
{
  "irradiance": [
    "Total solar irradiance (W/m2)",
    "Direct normal irradiance (W/m2)",
    "Global horizontal irradiance (W/m2)"
  ],
  "temperature": [
    "Air temperature  (°C) "
  ],
  "humidity": [
    "Relative humidity (%)"
  ],
  "pressure": [
    "Atmosphere (hpa)"
  ],
  "wind": [],
  "cloud": [],
  "solar_angle": [],
  "site_metadata": []
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 7 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "irradiance": [
    "Total solar irradiance (W/m2)",
    "Direct normal irradiance (W/m2)",
    "Global horizontal irradiance (W/m2)"
  ],
  "temperature": [
    "Air temperature  (°C) "
  ],
  "humidity": [
    "Relative humidity (%)"
  ],
  "pressure": [
    "Atmosphere (hpa)"
  ],
  "wind": [],
  "cloud": [],
  "solar_angle": [],
  "site_metadata": []
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 8 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "irradiance": [
    "Total solar irradiance (W/m2)",
    "Direct normal irradiance (W/m2)",
    "Global horizontal irradiance (W/m2)"
  ],
  "temperature": [
    "Air temperature  (°C) "
  ],
  "humidity": [
    "Relative humidity (%)"
  ],
  "pressure": [
    "Atmosphere (hpa)"
  ],
  "wind": [],
  "cloud": [],
  "solar_angle": [],
  "site_metadata": []
}
```

### Solar station site 1 (Nominal capacity-50MW).xlsx [sheet1]

```json
{
  "irradiance": [
    "Total solar irradiance (W/m2)",
    "Direct normal irradiance (W/m2)",
    "Global horizontal irradiance (W/m2)"
  ],
  "temperature": [
    "Air temperature  (°C) "
  ],
  "humidity": [
    "Relative humidity (%)"
  ],
  "pressure": [
    "Atmosphere (hpa)"
  ],
  "wind": [],
  "cloud": [],
  "solar_angle": [],
  "site_metadata": []
}
```

## 7. Data Quality Findings

VERIFIED ISSUE denotes observed missing/non-finite cells or duplicate records, not a decision to delete. Negative irradiance and out-of-range percentages are LIKELY ISSUE candidates. Sentinel counts, IQR outliers (1.5 IQR), constant and zero-heavy columns REQUIRE SEMANTIC VERIFICATION; negative temperature and zero generation are not automatically invalid.

### data_original.rar!data_original/solar_stations/Solar station site 1 (Nominal capacity-50MW).xlsx [sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "numeric_text_candidates": [],
  "flags": {
    "Total solar irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 60,
        "-999": 0
      },
      "zero_percent": 48.740310077519375,
      "status": "LIKELY ISSUE; sensor offsets/sentinels require verification",
      "negative_physical_candidate": 60
    },
    "Direct normal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 60,
        "-999": 0
      },
      "zero_percent": 38.05574555403557,
      "status": "LIKELY ISSUE; sensor offsets/sentinels require verification",
      "negative_physical_candidate": 60
    },
    "Global horizontal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 60,
        "-999": 0
      },
      "zero_percent": 48.79873461012312,
      "status": "LIKELY ISSUE; sensor offsets/sentinels require verification",
      "negative_physical_candidate": 60
    },
    "Air temperature  (°C) ": {
      "sentinel_counts": {
        "-99": 60,
        "-999": 0
      },
      "zero_percent": 0.32489740082079344,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Atmosphere (hpa)": {
      "sentinel_counts": {
        "-99": 60,
        "-999": 0
      },
      "zero_percent": 0.0,
      "status": "LIKELY ISSUE; sensor offsets/sentinels require verification",
      "negative_physical_candidate": 60
    },
    "Relative humidity (%)": {
      "sentinel_counts": {
        "-99": 60,
        "-999": 0
      },
      "zero_percent": 0.5272457820337437,
      "status": "LIKELY ISSUE; sensor offsets/sentinels require verification",
      "negative_physical_candidate": 60,
      "outside_header_percent_range": 6807
    },
    "Power (MW)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 50.25079799361605,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    }
  },
  "numeric_checks": {
    "Total solar irradiance (W/m2)": {
      "min": -99.0,
      "max": 1359.0,
      "mean": 266.0510003419973,
      "median": 5.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 60,
      "zero": 34204,
      "iqr_outliers": 1
    },
    "Direct normal irradiance (W/m2)": {
      "min": -99.0,
      "max": 980.0,
      "mean": 93.16146545827634,
      "median": 1.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 60,
      "zero": 26706,
      "iqr_outliers": 14776
    },
    "Global horizontal irradiance (W/m2)": {
      "min": -99.0,
      "max": 989.0,
      "mean": 67.55383606931144,
      "median": 4.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 60,
      "zero": 34245,
      "iqr_outliers": 4835
    },
    "Air temperature  (°C) ": {
      "min": -99.0,
      "max": 41.2,
      "mean": 13.042668433652532,
      "median": 15.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 17490,
      "zero": 228,
      "iqr_outliers": 60
    },
    "Atmosphere (hpa)": {
      "min": -99.0,
      "max": 936.3,
      "mean": 912.5075837893296,
      "median": 913.3,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 60,
      "zero": 0,
      "iqr_outliers": 60
    },
    "Relative humidity (%)": {
      "min": -99.0,
      "max": 6553.5,
      "mean": 650.6998247264022,
      "median": 21.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 60,
      "zero": 370,
      "iqr_outliers": 6807
    },
    "Power (MW)": {
      "min": 0.0,
      "max": 48.32173,
      "mean": 9.669416544730392,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 35264,
      "iqr_outliers": 44
    }
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 2 (Nominal capacity-130MW).xlsx [sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "numeric_text_candidates": [],
  "flags": {
    "Total solar irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 709,
        "-999": 0
      },
      "zero_percent": 50.85214318285453,
      "status": "LIKELY ISSUE; sensor offsets/sentinels require verification",
      "negative_physical_candidate": 709
    },
    "Direct normal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 709,
        "-999": 0
      },
      "zero_percent": 50.85641814865481,
      "status": "LIKELY ISSUE; sensor offsets/sentinels require verification",
      "negative_physical_candidate": 709
    },
    "Global horicontal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 709,
        "-999": 0
      },
      "zero_percent": 50.96186730506156,
      "status": "LIKELY ISSUE; sensor offsets/sentinels require verification",
      "negative_physical_candidate": 709
    },
    "Air temperature  (°C) ": {
      "sentinel_counts": {
        "-99": 709,
        "-999": 0
      },
      "zero_percent": 0.012824897400820793,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Atmosphere (hpa)": {
      "sentinel_counts": {
        "-99": 710,
        "-999": 0
      },
      "zero_percent": 0.0,
      "status": "LIKELY ISSUE; sensor offsets/sentinels require verification",
      "negative_physical_candidate": 710
    },
    "Relative humidity (%)": {
      "sentinel_counts": {
        "-99": 445,
        "-999": 0
      },
      "zero_percent": 0.004274965800273598,
      "status": "LIKELY ISSUE; sensor offsets/sentinels require verification",
      "negative_physical_candidate": 710,
      "outside_header_percent_range": 2116
    },
    "Power (MW)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.16814865481076152,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    }
  },
  "numeric_checks": {
    "Total solar irradiance (W/m2)": {
      "min": -99.0,
      "max": 1041.93,
      "mean": 166.8754998860009,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 709,
      "zero": 35686,
      "iqr_outliers": 2451
    },
    "Direct normal irradiance (W/m2)": {
      "min": -99.0,
      "max": 751.75,
      "mean": 120.12222241222071,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 709,
      "zero": 35689,
      "iqr_outliers": 2451
    },
    "Global horicontal irradiance (W/m2)": {
      "min": -99.0,
      "max": 561.8,
      "mean": 76.5440275877793,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 709,
      "zero": 35763,
      "iqr_outliers": 4815
    },
    "Air temperature  (°C) ": {
      "min": -99.0,
      "max": 40.47,
      "mean": 12.541515047879617,
      "median": 15.31,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 14164,
      "zero": 9,
      "iqr_outliers": 709
    },
    "Atmosphere (hpa)": {
      "min": -99.0,
      "max": 881.67,
      "mean": 851.3060990937073,
      "median": 860.71,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 710,
      "zero": 0,
      "iqr_outliers": 711
    },
    "Relative humidity (%)": {
      "min": -99.0,
      "max": 6553.44,
      "mean": 140.404341370269,
      "median": 22.28,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 710,
      "zero": 3,
      "iqr_outliers": 1852
    },
    "Power (MW)": {
      "min": 0.0,
      "max": 109.3603,
      "mean": 19.57157019428779,
      "median": 0.3269,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 118,
      "iqr_outliers": 1064
    }
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 3 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "numeric_text_candidates": [],
  "flags": {
    "Total solar irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 37.76041666666667,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Direct normal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 69.21190693430657,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Global horizontal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 55.67784367396593,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Air temperature  (°C) ": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.534139294403893,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Atmosphere (hpa)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.0076034063260340635,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Relative humidity (%)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.0076034063260340635,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0,
      "outside_header_percent_range": 1
    },
    "Power (MW)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 1.330596107055961,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    }
  },
  "numeric_checks": {
    "Total solar irradiance (W/m2)": {
      "min": 0.0,
      "max": 1117.0,
      "mean": 81.14352361147728,
      "median": 1.62596,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 19865,
      "iqr_outliers": 8911
    },
    "Direct normal irradiance (W/m2)": {
      "min": 0.0,
      "max": 893.0,
      "mean": 111.1159329379562,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 36411,
      "iqr_outliers": 7200
    },
    "Global horizontal irradiance (W/m2)": {
      "min": 0.0,
      "max": 656.0,
      "mean": 66.3297597323601,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 29291,
      "iqr_outliers": 2935
    },
    "Air temperature  (°C) ": {
      "min": -3276.7,
      "max": 3276.7,
      "mean": -302.5224300486618,
      "median": 13.8,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 5083,
      "zero": 281,
      "iqr_outliers": 5084
    },
    "Atmosphere (hpa)": {
      "min": 0.0,
      "max": 1044.4,
      "mean": 1017.7516803527981,
      "median": 1018.5,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 4,
      "iqr_outliers": 4
    },
    "Relative humidity (%)": {
      "min": 0.0,
      "max": 3276.7,
      "mean": 62.309087971411195,
      "median": 64.3,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 4,
      "iqr_outliers": 541
    },
    "Power (MW)": {
      "min": -0.063,
      "max": 29.9113395,
      "mean": 5.210598531240495,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 25652,
      "zero": 700,
      "iqr_outliers": 4494
    }
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 4 (Nominal capacity-130MW).xlsx [Sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "numeric_text_candidates": [],
  "flags": {
    "Total solar irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 51.51048791609667,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Direct normal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 52.295656634746926,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Global horizontal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 52.2999316005472,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Air temperature  (°C) ": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.5528955768353853,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Atmosphere (hpa)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.5471956224350205,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Relative humidity (%)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.5471956224350205,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0,
      "outside_header_percent_range": 0
    },
    "Power (MW)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 1.338064295485636,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    }
  },
  "numeric_checks": {
    "Total solar irradiance (W/m2)": {
      "min": 0.0,
      "max": 1237.4,
      "mean": 150.11718939523482,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 36148,
      "iqr_outliers": 9308
    },
    "Direct normal irradiance (W/m2)": {
      "min": 0.0,
      "max": 1010.27256487175,
      "mean": 138.92233082406568,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 36699,
      "iqr_outliers": 4340
    },
    "Global horizontal irradiance (W/m2)": {
      "min": 0.0,
      "max": 150.960268314169,
      "mean": 20.75722673529134,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 36702,
      "iqr_outliers": 4340
    },
    "Air temperature  (°C) ": {
      "min": -5.31873614994194,
      "max": 49.7996190860246,
      "mean": 18.64315462271015,
      "median": 19.20875537463445,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 554,
      "zero": 388,
      "iqr_outliers": 0
    },
    "Atmosphere (hpa)": {
      "min": 0.0,
      "max": 1100.31056206144,
      "mean": 1005.7863824747349,
      "median": 1010.91545968965,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 384,
      "iqr_outliers": 384
    },
    "Relative humidity (%)": {
      "min": 0.0,
      "max": 100.0,
      "mean": 65.88896263888411,
      "median": 66.46743336906894,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 384,
      "iqr_outliers": 384
    },
    "Power (MW)": {
      "min": -0.44,
      "max": 114.688,
      "mean": 16.468546472851646,
      "median": 0.078,
      "missing": 6,
      "non_finite_non_null": 0,
      "negative": 33878,
      "zero": 939,
      "iqr_outliers": 9376
    }
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 5 (Nominal capacity-110MW).xlsx [Sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "numeric_text_candidates": [
    {
      "name": "Total solar irradiance (W/m2)",
      "dtype": "object",
      "missing": 0,
      "unique_non_null": 1145,
      "constant": false,
      "sparse_over_50_percent_missing": false,
      "numeric_text_values": 70130,
      "non_numeric_text_values": 46
    },
    {
      "name": "Direct normal irradiance (W/m2)",
      "dtype": "object",
      "missing": 0,
      "unique_non_null": 890,
      "constant": false,
      "sparse_over_50_percent_missing": false,
      "numeric_text_values": 70130,
      "non_numeric_text_values": 46
    },
    {
      "name": "Global horizontal irradiance (W/m2)",
      "dtype": "object",
      "missing": 0,
      "unique_non_null": 971,
      "constant": false,
      "sparse_over_50_percent_missing": false,
      "numeric_text_values": 70130,
      "non_numeric_text_values": 46
    },
    {
      "name": "Air temperature  (°C) ",
      "dtype": "object",
      "missing": 0,
      "unique_non_null": 453,
      "constant": false,
      "sparse_over_50_percent_missing": false,
      "numeric_text_values": 70130,
      "non_numeric_text_values": 46
    },
    {
      "name": "Atmosphere (hpa)",
      "dtype": "object",
      "missing": 0,
      "unique_non_null": 488,
      "constant": false,
      "sparse_over_50_percent_missing": false,
      "numeric_text_values": 70130,
      "non_numeric_text_values": 46
    },
    {
      "name": "Relative humidity (%)",
      "dtype": "object",
      "missing": 0,
      "unique_non_null": 796,
      "constant": false,
      "sparse_over_50_percent_missing": false,
      "numeric_text_values": 70130,
      "non_numeric_text_values": 46
    },
    {
      "name": "Power (MW)",
      "dtype": "object",
      "missing": 0,
      "unique_non_null": 8343,
      "constant": false,
      "sparse_over_50_percent_missing": false,
      "numeric_text_values": 70130,
      "non_numeric_text_values": 46
    }
  ],
  "flags": {},
  "numeric_checks": {}
}
```

### data_original.rar!data_original/solar_stations/Solar station site 6 (Nominal capacity-35MW).xlsx [Sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "numeric_text_candidates": [
    {
      "name": "Total solar irradiance (W/m2)",
      "dtype": "object",
      "missing": 0,
      "unique_non_null": 16031,
      "constant": false,
      "sparse_over_50_percent_missing": false,
      "numeric_text_values": 69602,
      "non_numeric_text_values": 574
    },
    {
      "name": "Direct normal irradiance (W/m2)",
      "dtype": "object",
      "missing": 0,
      "unique_non_null": 12163,
      "constant": false,
      "sparse_over_50_percent_missing": false,
      "numeric_text_values": 69602,
      "non_numeric_text_values": 574
    },
    {
      "name": "Global horizontal irradiance (W/m2)",
      "dtype": "object",
      "missing": 0,
      "unique_non_null": 5245,
      "constant": false,
      "sparse_over_50_percent_missing": false,
      "numeric_text_values": 69602,
      "non_numeric_text_values": 574
    },
    {
      "name": "Air temperature  (°C) ",
      "dtype": "object",
      "missing": 0,
      "unique_non_null": 6170,
      "constant": false,
      "sparse_over_50_percent_missing": false,
      "numeric_text_values": 69602,
      "non_numeric_text_values": 574
    },
    {
      "name": "Atmosphere (hpa)",
      "dtype": "object",
      "missing": 0,
      "unique_non_null": 4349,
      "constant": false,
      "sparse_over_50_percent_missing": false,
      "numeric_text_values": 69602,
      "non_numeric_text_values": 574
    },
    {
      "name": "Relative humidity (%)",
      "dtype": "object",
      "missing": 0,
      "unique_non_null": 15715,
      "constant": false,
      "sparse_over_50_percent_missing": false,
      "numeric_text_values": 69602,
      "non_numeric_text_values": 574
    }
  ],
  "flags": {
    "Power (MW)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 51.06161650706794,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    }
  },
  "numeric_checks": {
    "Power (MW)": {
      "min": 0.0,
      "max": 31.239334,
      "mean": 6.36851536829973,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 35833,
      "iqr_outliers": 51
    }
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 7 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "numeric_text_candidates": [
    {
      "name": "Total solar irradiance (W/m2)",
      "dtype": "object",
      "missing": 0,
      "unique_non_null": 15171,
      "constant": false,
      "sparse_over_50_percent_missing": false,
      "numeric_text_values": 69595,
      "non_numeric_text_values": 581
    },
    {
      "name": "Direct normal irradiance (W/m2)",
      "dtype": "object",
      "missing": 0,
      "unique_non_null": 19440,
      "constant": false,
      "sparse_over_50_percent_missing": false,
      "numeric_text_values": 69595,
      "non_numeric_text_values": 581
    },
    {
      "name": "Global horizontal irradiance (W/m2)",
      "dtype": "object",
      "missing": 0,
      "unique_non_null": 11823,
      "constant": false,
      "sparse_over_50_percent_missing": false,
      "numeric_text_values": 69595,
      "non_numeric_text_values": 581
    },
    {
      "name": "Air temperature  (°C) ",
      "dtype": "object",
      "missing": 0,
      "unique_non_null": 27360,
      "constant": false,
      "sparse_over_50_percent_missing": false,
      "numeric_text_values": 69595,
      "non_numeric_text_values": 581
    },
    {
      "name": "Atmosphere (hpa)",
      "dtype": "object",
      "missing": 0,
      "unique_non_null": 7797,
      "constant": false,
      "sparse_over_50_percent_missing": false,
      "numeric_text_values": 69616,
      "non_numeric_text_values": 560
    },
    {
      "name": "Relative humidity (%)",
      "dtype": "object",
      "missing": 0,
      "unique_non_null": 49245,
      "constant": false,
      "sparse_over_50_percent_missing": false,
      "numeric_text_values": 69595,
      "non_numeric_text_values": 581
    }
  ],
  "flags": {
    "Power (MW)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 53.942943456452355,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    }
  },
  "numeric_checks": {
    "Power (MW)": {
      "min": 0.0,
      "max": 29.775333,
      "mean": 5.411922601045942,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 37855,
      "iqr_outliers": 2485
    }
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 8 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "numeric_text_candidates": [],
  "flags": {
    "Total solar irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 52.10638543107423,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Direct normal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 52.10638543107423,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Global horizontal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 52.10638543107423,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Air temperature  (°C) ": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.007203780544029507,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Atmosphere (hpa)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.0,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Relative humidity (%)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.0,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0,
      "outside_header_percent_range": 0
    },
    "Power (MW)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 50.89903181189488,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    }
  },
  "numeric_checks": {
    "Total solar irradiance (W/m2)": {
      "min": 0.0,
      "max": 1214.54,
      "mean": 163.24392663669894,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 36166,
      "iqr_outliers": 4266
    },
    "Direct normal irradiance (W/m2)": {
      "min": 0.0,
      "max": 1056.650339,
      "mean": 142.02223113829447,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 36166,
      "iqr_outliers": 4266
    },
    "Global horizontal irradiance (W/m2)": {
      "min": 0.0,
      "max": 157.8902806,
      "mean": 21.221707551800485,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 36166,
      "iqr_outliers": 4267
    },
    "Air temperature  (°C) ": {
      "min": -8.04,
      "max": 47.63,
      "mean": 18.0096503538057,
      "median": 18.19,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 721,
      "zero": 5,
      "iqr_outliers": 31
    },
    "Atmosphere (hpa)": {
      "min": 881.4,
      "max": 1037.78,
      "mean": 956.4192689867365,
      "median": 956.07,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 0,
      "iqr_outliers": 0
    },
    "Relative humidity (%)": {
      "min": 11.83,
      "max": 100.0,
      "mean": 71.70595580663093,
      "median": 73.53,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 0,
      "iqr_outliers": 46
    },
    "Power (MW)": {
      "min": 0.0,
      "max": 29.41,
      "mean": 4.230664476717382,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 35328,
      "iqr_outliers": 6579
    }
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 1 (Nominal capacity-50MW).xlsx [sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "numeric_text_candidates": [],
  "flags": {
    "Total solar irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 48.7859097127223,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Direct normal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 38.11417008663931,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Global horizontal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 48.84433424532604,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Air temperature  (°C) ": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.32489740082079344,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Atmosphere (hpa)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.0,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Power (MW)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 50.25364797081623,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    }
  },
  "numeric_checks": {
    "Total solar irradiance (W/m2)": {
      "min": 0.0,
      "max": 1359.0,
      "mean": 266.2073358413133,
      "median": 5.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 34236,
      "iqr_outliers": 1
    },
    "Direct normal irradiance (W/m2)": {
      "min": 0.0,
      "max": 980.0,
      "mean": 93.25699669402644,
      "median": 1.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 26747,
      "iqr_outliers": 14717
    },
    "Global horizontal irradiance (W/m2)": {
      "min": 0.0,
      "max": 989.0,
      "mean": 67.69262995896032,
      "median": 4.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 34277,
      "iqr_outliers": 4837
    },
    "Air temperature  (°C) ": {
      "min": -18.2,
      "max": 41.2,
      "mean": 13.148167464660283,
      "median": 15.1,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 17431,
      "zero": 228,
      "iqr_outliers": 0
    },
    "Atmosphere (hpa)": {
      "min": 894.0,
      "max": 936.3,
      "mean": 913.3671483128135,
      "median": 913.3,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 0,
      "iqr_outliers": 0
    },
    "Power (MW)": {
      "min": 0.0,
      "max": 48.32173,
      "mean": 9.669360930389306,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 35266,
      "iqr_outliers": 44
    }
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 2 (Nominal capacity-130MW).xlsx [sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "numeric_text_candidates": [],
  "flags": {
    "Total solar irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 51.41786365709075,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Direct normal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 51.42213862289101,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Global horizontal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 51.53186274509803,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Air temperature  (°C) ": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.012824897400820793,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Atmosphere (hpa)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.0,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Power (MW)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.16814865481076152,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    }
  },
  "numeric_checks": {
    "Total solar irradiance (W/m2)": {
      "min": 0.0,
      "max": 1041.93,
      "mean": 169.30336653556773,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 36083,
      "iqr_outliers": 2257
    },
    "Direct normal irradiance (W/m2)": {
      "min": 0.0,
      "max": 751.75,
      "mean": 122.1523955483356,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 36086,
      "iqr_outliers": 2257
    },
    "Global horizontal irradiance (W/m2)": {
      "min": 0.0,
      "max": 561.8,
      "mean": 78.29928152074784,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 36163,
      "iqr_outliers": 4658
    },
    "Air temperature  (°C) ": {
      "min": -13.92,
      "max": 40.47,
      "mean": 13.695107586639308,
      "median": 15.46,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 13467,
      "zero": 9,
      "iqr_outliers": 0
    },
    "Atmosphere (hpa)": {
      "min": 844.51,
      "max": 881.67,
      "mean": 861.0362623974008,
      "median": 860.87,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 0,
      "iqr_outliers": 1
    },
    "Power (MW)": {
      "min": 0.0,
      "max": 109.3603,
      "mean": 19.567488451669234,
      "median": 0.3269,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 118,
      "iqr_outliers": 1052
    }
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 3 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "numeric_text_candidates": [],
  "flags": {
    "Total solar irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 53.370676100628934,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Direct normal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 69.37893081761007,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Global horizontal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 54.662932389937104,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Atmosphere (hpa)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.0,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Relative humidity (%)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.0,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0,
      "outside_header_percent_range": 0
    },
    "Power (MW)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 1.7000786163522013,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    }
  },
  "numeric_checks": {
    "Total solar irradiance (W/m2)": {
      "min": 0.0,
      "max": 1117.0,
      "mean": 198.8134335691824,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 10862,
      "iqr_outliers": 972
    },
    "Direct normal irradiance (W/m2)": {
      "min": 0.0,
      "max": 760.0,
      "mean": 100.72955974842768,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 14120,
      "iqr_outliers": 3596
    },
    "Global horizontal irradiance (W/m2)": {
      "min": 0.0,
      "max": 656.0,
      "mean": 69.305080581761,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 11125,
      "iqr_outliers": 1221
    },
    "Atmosphere (hpa)": {
      "min": 994.8,
      "max": 1038.6,
      "mean": 1016.0137676886794,
      "median": 1014.7,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 0,
      "iqr_outliers": 0
    },
    "Relative humidity (%)": {
      "min": 14.1,
      "max": 80.5,
      "mean": 58.249243317610066,
      "median": 61.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 0,
      "iqr_outliers": 235
    },
    "Power (MW)": {
      "min": -0.063,
      "max": 29.9113395,
      "mean": 5.449246788104363,
      "median": 0.115101,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 9517,
      "zero": 346,
      "iqr_outliers": 1435
    }
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 4 (Nominal capacity-130MW).xlsx [Sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "numeric_text_candidates": [],
  "flags": {
    "Total solar irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 51.51476288189695,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Direct normal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 52.0562585499316,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Global horizontal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 52.060533515731876,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Air temperature  (°C) ": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.005699954400364797,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Atmosphere (hpa)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.0,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Relative humidity (%)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.0,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0,
      "outside_header_percent_range": 0
    },
    "Power (MW)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 1.3337893296853625,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    }
  },
  "numeric_checks": {
    "Total solar irradiance (W/m2)": {
      "min": 0.0,
      "max": 1237.4,
      "mean": 150.15481737346101,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 36151,
      "iqr_outliers": 9295
    },
    "Direct normal irradiance (W/m2)": {
      "min": 0.0,
      "max": 1010.27256487175,
      "mean": 139.5115814412417,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 36531,
      "iqr_outliers": 4202
    },
    "Global horizontal irradiance (W/m2)": {
      "min": 0.0,
      "max": 150.960268314169,
      "mean": 20.84527567808776,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 36534,
      "iqr_outliers": 4202
    },
    "Air temperature  (°C) ": {
      "min": -5.31873614994194,
      "max": 49.7996190860246,
      "mean": 18.716369112034823,
      "median": 19.261013922330697,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 554,
      "zero": 4,
      "iqr_outliers": 0
    },
    "Atmosphere (hpa)": {
      "min": 928.598377167773,
      "max": 1100.31056206144,
      "mean": 1011.3737482909615,
      "median": 1011.20001912569,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 0,
      "iqr_outliers": 0
    },
    "Relative humidity (%)": {
      "min": 18.5036549489169,
      "max": 100.0,
      "mean": 66.24012304536782,
      "median": 66.56264061585635,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 0,
      "iqr_outliers": 0
    },
    "Power (MW)": {
      "min": -0.44,
      "max": 114.688,
      "mean": 16.455695126122272,
      "median": 0.078,
      "missing": 6,
      "non_finite_non_null": 0,
      "negative": 33881,
      "zero": 936,
      "iqr_outliers": 9382
    }
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 5 (Nominal capacity-110MW).xlsx [Sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "numeric_text_candidates": [],
  "flags": {
    "Total solar irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 50.76379388964888,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Direct normal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 49.74635202918377,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Global horizontal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 50.54577063383493,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Air temperature  (°C) ": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.15674874601003191,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Atmosphere (hpa)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.0,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Relative humidity (%)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.0,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0,
      "outside_header_percent_range": 0
    },
    "Power (MW)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 26.53471272229822,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    }
  },
  "numeric_checks": {
    "Total solar irradiance (W/m2)": {
      "min": 0.0,
      "max": 1467.0,
      "mean": 164.59610123119015,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 35624,
      "iqr_outliers": 9388
    },
    "Direct normal irradiance (W/m2)": {
      "min": 0.0,
      "max": 1962.0,
      "mean": 148.10131668946647,
      "median": 1.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 34910,
      "iqr_outliers": 7488
    },
    "Global horizontal irradiance (W/m2)": {
      "min": 0.0,
      "max": 1208.0,
      "mean": 115.27204457364341,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 35471,
      "iqr_outliers": 8627
    },
    "Air temperature  (°C) ": {
      "min": -6.6,
      "max": 39.5,
      "mean": 17.78077975376197,
      "median": 18.7,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 789,
      "zero": 110,
      "iqr_outliers": 0
    },
    "Atmosphere (hpa)": {
      "min": 990.7,
      "max": 1039.4,
      "mean": 1011.9912648198814,
      "median": 1012.2,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 0,
      "iqr_outliers": 0
    },
    "Relative humidity (%)": {
      "min": 10.6,
      "max": 93.2,
      "mean": 71.58947218422253,
      "median": 77.2,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 0,
      "iqr_outliers": 2982
    },
    "Power (MW)": {
      "min": -0.54,
      "max": 99.55,
      "mean": 14.513072132922938,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 18055,
      "zero": 18621,
      "iqr_outliers": 9270
    }
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 6 (Nominal capacity-35MW).xlsx [Sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "numeric_text_candidates": [],
  "flags": {
    "Total solar irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 49.924475604195166,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Direct normal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 51.28961468308254,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Global horizontal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 50.49874601003192,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Air temperature  (°C) ": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.0,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Atmosphere (hpa)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.0,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Relative humidity (%)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.0,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0,
      "outside_header_percent_range": 0
    },
    "Power (MW)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 51.070166438668494,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    }
  },
  "numeric_checks": {
    "Total solar irradiance (W/m2)": {
      "min": 0.0,
      "max": 1365.4,
      "mean": 243.08193456656062,
      "median": 0.06666667,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 35035,
      "iqr_outliers": 1101
    },
    "Direct normal irradiance (W/m2)": {
      "min": 0.0,
      "max": 1179.8,
      "mean": 215.1498262226405,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 35993,
      "iqr_outliers": 13
    },
    "Global horizontal irradiance (W/m2)": {
      "min": 0.0,
      "max": 296.2,
      "mean": 53.92730949951344,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 35438,
      "iqr_outliers": 302
    },
    "Air temperature  (°C) ": {
      "min": 2.9466667,
      "max": 36.693333,
      "mean": 20.62948917147458,
      "median": 20.68,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 0,
      "iqr_outliers": 61
    },
    "Atmosphere (hpa)": {
      "min": 389.82,
      "max": 846.0733,
      "mean": 830.6714380534656,
      "median": 830.42,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 0,
      "iqr_outliers": 438
    },
    "Relative humidity (%)": {
      "min": 1.4133333,
      "max": 97.9,
      "mean": 53.94283213849607,
      "median": 52.486668,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 0,
      "iqr_outliers": 0
    },
    "Power (MW)": {
      "min": 0.0,
      "max": 31.239334,
      "mean": 6.364345823162932,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 35839,
      "iqr_outliers": 52
    }
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 7 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "numeric_text_candidates": [],
  "flags": {
    "Total solar irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 40.01652986776106,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Direct normal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 53.94436844505244,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Global horizontal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 48.50518695850433,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Air temperature  (°C) ": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.004274965800273598,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Atmosphere (hpa)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.0,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Relative humidity (%)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.0,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0,
      "outside_header_percent_range": 113
    },
    "Power (MW)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 53.94009347925217,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    }
  },
  "numeric_checks": {
    "Total solar irradiance (W/m2)": {
      "min": 0.0,
      "max": 1393.733333,
      "mean": 206.0824669133607,
      "median": 2.6,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 28082,
      "iqr_outliers": 2729
    },
    "Direct normal irradiance (W/m2)": {
      "min": 0.0,
      "max": 1095.4,
      "mean": 182.99632227089032,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 37856,
      "iqr_outliers": 9679
    },
    "Global horizontal irradiance (W/m2)": {
      "min": 0.0,
      "max": 1125.133333,
      "mean": 108.6800597563982,
      "median": 2.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 34039,
      "iqr_outliers": 7829
    },
    "Air temperature  (°C) ": {
      "min": -4.263333,
      "max": 30.12,
      "mean": 13.739213486605108,
      "median": 14.36,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 584,
      "zero": 3,
      "iqr_outliers": 5
    },
    "Atmosphere (hpa)": {
      "min": 398.206667,
      "max": 867.1,
      "mean": 842.9337953072275,
      "median": 854.412667,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 0,
      "iqr_outliers": 1942
    },
    "Relative humidity (%)": {
      "min": 1.953333,
      "max": 100.94,
      "mean": 55.18065928303123,
      "median": 54.869,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 0,
      "iqr_outliers": 0
    },
    "Power (MW)": {
      "min": 0.0,
      "max": 29.775333,
      "mean": 5.409623686730507,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 37853,
      "iqr_outliers": 2519
    }
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 8 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "numeric_text_candidates": [],
  "flags": {
    "Total solar irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 52.10638543107423,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Direct normal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 52.10638543107423,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Global horizontal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 52.10638543107423,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Air temperature  (°C) ": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.007203780544029507,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Atmosphere (hpa)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.0,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Relative humidity (%)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 0.0,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0,
      "outside_header_percent_range": 0
    },
    "Power (MW)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 50.89903181189488,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    }
  },
  "numeric_checks": {
    "Total solar irradiance (W/m2)": {
      "min": 0.0,
      "max": 1214.54,
      "mean": 163.24392663669894,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 36166,
      "iqr_outliers": 4266
    },
    "Direct normal irradiance (W/m2)": {
      "min": 0.0,
      "max": 1056.650339,
      "mean": 142.02223113829447,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 36166,
      "iqr_outliers": 4266
    },
    "Global horizontal irradiance (W/m2)": {
      "min": 0.0,
      "max": 157.8902806,
      "mean": 21.221707551800485,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 36166,
      "iqr_outliers": 4267
    },
    "Air temperature  (°C) ": {
      "min": -8.04,
      "max": 47.63,
      "mean": 18.0096503538057,
      "median": 18.19,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 721,
      "zero": 5,
      "iqr_outliers": 31
    },
    "Atmosphere (hpa)": {
      "min": 881.4,
      "max": 1037.78,
      "mean": 956.4192689867365,
      "median": 956.07,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 0,
      "iqr_outliers": 0
    },
    "Relative humidity (%)": {
      "min": 11.83,
      "max": 100.0,
      "mean": 71.70595580663093,
      "median": 73.53,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 0,
      "iqr_outliers": 46
    },
    "Power (MW)": {
      "min": 0.0,
      "max": 29.41,
      "mean": 4.230664476717382,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 35328,
      "iqr_outliers": 6579
    }
  }
}
```

### Solar station site 1 (Nominal capacity-50MW).xlsx [sheet1]

```json
{
  "duplicates": {
    "duplicate_rows": 0,
    "rows_in_duplicate_groups": 0
  },
  "constant_columns": [],
  "sparse_columns": [],
  "numeric_text_candidates": [],
  "flags": {
    "Total solar irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 60,
        "-999": 0
      },
      "zero_percent": 48.740310077519375,
      "status": "LIKELY ISSUE; sensor offsets/sentinels require verification",
      "negative_physical_candidate": 60
    },
    "Direct normal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 60,
        "-999": 0
      },
      "zero_percent": 38.05574555403557,
      "status": "LIKELY ISSUE; sensor offsets/sentinels require verification",
      "negative_physical_candidate": 60
    },
    "Global horizontal irradiance (W/m2)": {
      "sentinel_counts": {
        "-99": 60,
        "-999": 0
      },
      "zero_percent": 48.79873461012312,
      "status": "LIKELY ISSUE; sensor offsets/sentinels require verification",
      "negative_physical_candidate": 60
    },
    "Air temperature  (°C) ": {
      "sentinel_counts": {
        "-99": 60,
        "-999": 0
      },
      "zero_percent": 0.32489740082079344,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    },
    "Atmosphere (hpa)": {
      "sentinel_counts": {
        "-99": 60,
        "-999": 0
      },
      "zero_percent": 0.0,
      "status": "LIKELY ISSUE; sensor offsets/sentinels require verification",
      "negative_physical_candidate": 60
    },
    "Relative humidity (%)": {
      "sentinel_counts": {
        "-99": 60,
        "-999": 0
      },
      "zero_percent": 0.5272457820337437,
      "status": "LIKELY ISSUE; sensor offsets/sentinels require verification",
      "negative_physical_candidate": 60,
      "outside_header_percent_range": 6807
    },
    "Power (MW)": {
      "sentinel_counts": {
        "-99": 0,
        "-999": 0
      },
      "zero_percent": 50.25079799361605,
      "status": "REQUIRES SEMANTIC VERIFICATION",
      "negative_physical_candidate": 0
    }
  },
  "numeric_checks": {
    "Total solar irradiance (W/m2)": {
      "min": -99.0,
      "max": 1359.0,
      "mean": 266.0510003419973,
      "median": 5.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 60,
      "zero": 34204,
      "iqr_outliers": 1
    },
    "Direct normal irradiance (W/m2)": {
      "min": -99.0,
      "max": 980.0,
      "mean": 93.16146545827634,
      "median": 1.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 60,
      "zero": 26706,
      "iqr_outliers": 14776
    },
    "Global horizontal irradiance (W/m2)": {
      "min": -99.0,
      "max": 989.0,
      "mean": 67.55383606931144,
      "median": 4.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 60,
      "zero": 34245,
      "iqr_outliers": 4835
    },
    "Air temperature  (°C) ": {
      "min": -99.0,
      "max": 41.2,
      "mean": 13.042668433652532,
      "median": 15.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 17490,
      "zero": 228,
      "iqr_outliers": 60
    },
    "Atmosphere (hpa)": {
      "min": -99.0,
      "max": 936.3,
      "mean": 912.5075837893296,
      "median": 913.3,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 60,
      "zero": 0,
      "iqr_outliers": 60
    },
    "Relative humidity (%)": {
      "min": -99.0,
      "max": 6553.5,
      "mean": 650.6998247264022,
      "median": 21.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 60,
      "zero": 370,
      "iqr_outliers": 6807
    },
    "Power (MW)": {
      "min": 0.0,
      "max": 48.32173,
      "mean": 9.669416544730392,
      "median": 0.0,
      "missing": 0,
      "non_finite_non_null": 0,
      "negative": 0,
      "zero": 35264,
      "iqr_outliers": 44
    }
  }
}
```

## 8. Solar-Specific Findings

No astronomical day/night assignment is justified without coordinates and source timezone. Zero irradiance is an observational condition, potentially affected by sensor problems. Hourly summaries preserve source clock hours for naive values; explicit offsets use UTC for diagnostics. No energy-to-power conversion is performed.

### data_original.rar!data_original/solar_stations/Solar station site 1 (Nominal capacity-50MW).xlsx [sheet1]

```json
{
  "day_night": "UNRESOLVED: no verified coordinates/timezone; clock hours and zero irradiance do not prove night",
  "irradiance_conditions": [
    {
      "irradiance": "Total solar irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 34204,
      "zero_target": 34163,
      "positive_target": 41,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Direct normal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 26706,
      "zero_target": 22726,
      "positive_target": 3980,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Global horizontal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 34245,
      "zero_target": 34189,
      "positive_target": 56,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    }
  ],
  "hourly_target_summary": {
    "Power (MW) / Time(year-month-day h:m:s)": [
      {
        "hour": 0,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 1,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 2,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 3,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 4,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 5,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 6,
        "non_null": 2924,
        "zero": 2548,
        "mean": 0.0425262424760602
      },
      {
        "hour": 7,
        "non_null": 2924,
        "zero": 1613,
        "mean": 0.6179867277701778
      },
      {
        "hour": 8,
        "non_null": 2924,
        "zero": 854,
        "mean": 3.555915092681259
      },
      {
        "hour": 9,
        "non_null": 2924,
        "zero": 105,
        "mean": 10.817056751709986
      },
      {
        "hour": 10,
        "non_null": 2924,
        "zero": 12,
        "mean": 20.270795838235294
      },
      {
        "hour": 11,
        "non_null": 2924,
        "zero": 12,
        "mean": 27.301747183310535
      },
      {
        "hour": 12,
        "non_null": 2924,
        "zero": 10,
        "mean": 30.9065564750342
      },
      {
        "hour": 13,
        "non_null": 2924,
        "zero": 8,
        "mean": 31.863327343365253
      },
      {
        "hour": 14,
        "non_null": 2924,
        "zero": 8,
        "mean": 31.088385107045145
      },
      {
        "hour": 15,
        "non_null": 2924,
        "zero": 8,
        "mean": 28.429521315321473
      },
      {
        "hour": 16,
        "non_null": 2924,
        "zero": 8,
        "mean": 23.307554080711355
      },
      {
        "hour": 17,
        "non_null": 2924,
        "zero": 10,
        "mean": 15.127454021545827
      },
      {
        "hour": 18,
        "non_null": 2924,
        "zero": 483,
        "mean": 6.78710541621067
      },
      {
        "hour": 19,
        "non_null": 2924,
        "zero": 1262,
        "mean": 1.7090952520519838
      },
      {
        "hour": 20,
        "non_null": 2924,
        "zero": 2058,
        "mean": 0.2399727787277702
      },
      {
        "hour": 21,
        "non_null": 2924,
        "zero": 2873,
        "mean": 0.0009974473324213407
      },
      {
        "hour": 22,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 23,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      }
    ]
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 2 (Nominal capacity-130MW).xlsx [sheet1]

```json
{
  "day_night": "UNRESOLVED: no verified coordinates/timezone; clock hours and zero irradiance do not prove night",
  "irradiance_conditions": [
    {
      "irradiance": "Total solar irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 35686,
      "zero_target": 76,
      "positive_target": 35610,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Direct normal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 35689,
      "zero_target": 76,
      "positive_target": 35613,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Global horicontal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 35763,
      "zero_target": 76,
      "positive_target": 35687,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    }
  ],
  "hourly_target_summary": {
    "Power (MW) / Time(year-month-day h:m:s)": [
      {
        "hour": 0,
        "non_null": 2924,
        "zero": 8,
        "mean": 0.23836420485636114
      },
      {
        "hour": 1,
        "non_null": 2924,
        "zero": 8,
        "mean": 0.23962355073187414
      },
      {
        "hour": 2,
        "non_null": 2924,
        "zero": 8,
        "mean": 0.24101788816689468
      },
      {
        "hour": 3,
        "non_null": 2924,
        "zero": 8,
        "mean": 0.24233026778385774
      },
      {
        "hour": 4,
        "non_null": 2924,
        "zero": 8,
        "mean": 0.2430324620383037
      },
      {
        "hour": 5,
        "non_null": 2924,
        "zero": 6,
        "mean": 0.24356681224350205
      },
      {
        "hour": 6,
        "non_null": 2924,
        "zero": 4,
        "mean": 0.24387570861833105
      },
      {
        "hour": 7,
        "non_null": 2924,
        "zero": 4,
        "mean": 0.27971352051983583
      },
      {
        "hour": 8,
        "non_null": 2924,
        "zero": 4,
        "mean": 1.5938495448016416
      },
      {
        "hour": 9,
        "non_null": 2924,
        "zero": 4,
        "mean": 7.719639953488372
      },
      {
        "hour": 10,
        "non_null": 2924,
        "zero": 4,
        "mean": 22.85044024350205
      },
      {
        "hour": 11,
        "non_null": 2924,
        "zero": 4,
        "mean": 42.332260605677156
      },
      {
        "hour": 12,
        "non_null": 2924,
        "zero": 4,
        "mean": 57.394826999658
      },
      {
        "hour": 13,
        "non_null": 2924,
        "zero": 4,
        "mean": 64.44359595075238
      },
      {
        "hour": 14,
        "non_null": 2924,
        "zero": 4,
        "mean": 64.03692393057456
      },
      {
        "hour": 15,
        "non_null": 2924,
        "zero": 4,
        "mean": 61.8681991121751
      },
      {
        "hour": 16,
        "non_null": 2924,
        "zero": 4,
        "mean": 56.497574784883724
      },
      {
        "hour": 17,
        "non_null": 2924,
        "zero": 4,
        "mean": 45.00986885978112
      },
      {
        "hour": 18,
        "non_null": 2924,
        "zero": 3,
        "mean": 27.659053982558138
      },
      {
        "hour": 19,
        "non_null": 2924,
        "zero": 0,
        "mean": 11.809862201094392
      },
      {
        "hour": 20,
        "non_null": 2924,
        "zero": 0,
        "mean": 3.3384942708618337
      },
      {
        "hour": 21,
        "non_null": 2924,
        "zero": 0,
        "mean": 0.670541502735978
      },
      {
        "hour": 22,
        "non_null": 2924,
        "zero": 9,
        "mean": 0.2704050030779754
      },
      {
        "hour": 23,
        "non_null": 2924,
        "zero": 12,
        "mean": 0.2506233023255814
      }
    ]
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 3 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "day_night": "UNRESOLVED: no verified coordinates/timezone; clock hours and zero irradiance do not prove night",
  "irradiance_conditions": [
    {
      "irradiance": "Total solar irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 19865,
      "zero_target": 282,
      "positive_target": 2088,
      "negative_target": 17495,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Direct normal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 36411,
      "zero_target": 524,
      "positive_target": 10567,
      "negative_target": 25320,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Global horizontal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 29291,
      "zero_target": 396,
      "positive_target": 3265,
      "negative_target": 25630,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    }
  ],
  "hourly_target_summary": {
    "Power (MW) / Time(year-month-day h:m:s)": [
      {
        "hour": 0,
        "non_null": 2192,
        "zero": 24,
        "mean": -0.03563485401459854
      },
      {
        "hour": 1,
        "non_null": 2192,
        "zero": 24,
        "mean": -0.035725866788321174
      },
      {
        "hour": 2,
        "non_null": 2192,
        "zero": 24,
        "mean": -0.03575939781021898
      },
      {
        "hour": 3,
        "non_null": 2192,
        "zero": 24,
        "mean": -0.035721076642335765
      },
      {
        "hour": 4,
        "non_null": 2192,
        "zero": 40,
        "mean": -0.035040214872262776
      },
      {
        "hour": 5,
        "non_null": 2192,
        "zero": 33,
        "mean": 0.12439673334854016
      },
      {
        "hour": 6,
        "non_null": 2192,
        "zero": 30,
        "mean": 0.9903490401459855
      },
      {
        "hour": 7,
        "non_null": 2192,
        "zero": 36,
        "mean": 3.693956011633212
      },
      {
        "hour": 8,
        "non_null": 2192,
        "zero": 32,
        "mean": 8.247116867016423
      },
      {
        "hour": 9,
        "non_null": 2192,
        "zero": 32,
        "mean": 12.97383263640511
      },
      {
        "hour": 10,
        "non_null": 2192,
        "zero": 28,
        "mean": 15.897048774635035
      },
      {
        "hour": 11,
        "non_null": 2192,
        "zero": 32,
        "mean": 17.420816250228103
      },
      {
        "hour": 12,
        "non_null": 2192,
        "zero": 32,
        "mean": 17.468411123631384
      },
      {
        "hour": 13,
        "non_null": 2192,
        "zero": 32,
        "mean": 16.137365529881386
      },
      {
        "hour": 14,
        "non_null": 2192,
        "zero": 32,
        "mean": 14.097824892107665
      },
      {
        "hour": 15,
        "non_null": 2192,
        "zero": 32,
        "mean": 10.415513921304745
      },
      {
        "hour": 16,
        "non_null": 2192,
        "zero": 28,
        "mean": 5.667531510948905
      },
      {
        "hour": 17,
        "non_null": 2192,
        "zero": 37,
        "mean": 1.9080837830748172
      },
      {
        "hour": 18,
        "non_null": 2192,
        "zero": 29,
        "mean": 0.3473745752737227
      },
      {
        "hour": 19,
        "non_null": 2192,
        "zero": 23,
        "mean": -0.014760389370437957
      },
      {
        "hour": 20,
        "non_null": 2192,
        "zero": 24,
        "mean": -0.035713412408759124
      },
      {
        "hour": 21,
        "non_null": 2192,
        "zero": 24,
        "mean": -0.035613777372262775
      },
      {
        "hour": 22,
        "non_null": 2192,
        "zero": 24,
        "mean": -0.03572969890510949
      },
      {
        "hour": 23,
        "non_null": 2192,
        "zero": 24,
        "mean": -0.03555821167883212
      }
    ]
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 4 (Nominal capacity-130MW).xlsx [Sheet1]

```json
{
  "day_night": "UNRESOLVED: no verified coordinates/timezone; clock hours and zero irradiance do not prove night",
  "irradiance_conditions": [
    {
      "irradiance": "Total solar irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 36146,
      "zero_target": 628,
      "positive_target": 2997,
      "negative_target": 32521,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Direct normal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 36697,
      "zero_target": 672,
      "positive_target": 2731,
      "negative_target": 33294,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Global horizontal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 36700,
      "zero_target": 672,
      "positive_target": 2731,
      "negative_target": 33297,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    }
  ],
  "hourly_target_summary": {
    "Power (MW) / Time(year-month-day h:m:s)": [
      {
        "hour": 0,
        "non_null": 2924,
        "zero": 52,
        "mean": -0.2295123119015048
      },
      {
        "hour": 1,
        "non_null": 2924,
        "zero": 52,
        "mean": -0.2309069767441861
      },
      {
        "hour": 2,
        "non_null": 2924,
        "zero": 52,
        "mean": -0.2330013679890561
      },
      {
        "hour": 3,
        "non_null": 2924,
        "zero": 52,
        "mean": -0.23414056087551305
      },
      {
        "hour": 4,
        "non_null": 2924,
        "zero": 52,
        "mean": -0.23470554035567714
      },
      {
        "hour": 5,
        "non_null": 2923,
        "zero": 46,
        "mean": -0.19288812863496413
      },
      {
        "hour": 6,
        "non_null": 2924,
        "zero": 39,
        "mean": 1.3420054719562242
      },
      {
        "hour": 7,
        "non_null": 2924,
        "zero": 36,
        "mean": 8.155716142270862
      },
      {
        "hour": 8,
        "non_null": 2924,
        "zero": 23,
        "mean": 21.729904924760604
      },
      {
        "hour": 9,
        "non_null": 2922,
        "zero": 20,
        "mean": 37.25008213552361
      },
      {
        "hour": 10,
        "non_null": 2924,
        "zero": 20,
        "mean": 49.131464432284545
      },
      {
        "hour": 11,
        "non_null": 2924,
        "zero": 20,
        "mean": 56.3053156634747
      },
      {
        "hour": 12,
        "non_null": 2924,
        "zero": 24,
        "mean": 57.56200205198358
      },
      {
        "hour": 13,
        "non_null": 2924,
        "zero": 24,
        "mean": 53.88746545827634
      },
      {
        "hour": 14,
        "non_null": 2924,
        "zero": 24,
        "mean": 46.48584473324213
      },
      {
        "hour": 15,
        "non_null": 2923,
        "zero": 25,
        "mean": 34.895291481354775
      },
      {
        "hour": 16,
        "non_null": 2923,
        "zero": 25,
        "mean": 20.933325008552856
      },
      {
        "hour": 17,
        "non_null": 2924,
        "zero": 37,
        "mean": 8.357090287277702
      },
      {
        "hour": 18,
        "non_null": 2924,
        "zero": 33,
        "mean": 1.6406196990424078
      },
      {
        "hour": 19,
        "non_null": 2924,
        "zero": 55,
        "mean": -0.14915389876880988
      },
      {
        "hour": 20,
        "non_null": 2924,
        "zero": 66,
        "mean": -0.22512653898768809
      },
      {
        "hour": 21,
        "non_null": 2923,
        "zero": 56,
        "mean": -0.23000513171399245
      },
      {
        "hour": 22,
        "non_null": 2924,
        "zero": 52,
        "mean": -0.23098803009575927
      },
      {
        "hour": 23,
        "non_null": 2924,
        "zero": 54,
        "mean": -0.2299493844049248
      }
    ]
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 5 (Nominal capacity-110MW).xlsx [Sheet1]

```json
{
  "day_night": "UNRESOLVED: no verified coordinates/timezone; clock hours and zero irradiance do not prove night",
  "irradiance_conditions": [],
  "hourly_target_summary": {}
}
```

### data_original.rar!data_original/solar_stations/Solar station site 6 (Nominal capacity-35MW).xlsx [Sheet1]

```json
{
  "day_night": "UNRESOLVED: no verified coordinates/timezone; clock hours and zero irradiance do not prove night",
  "irradiance_conditions": [],
  "hourly_target_summary": {
    "Power (MW) / Time(year-month-day h:m:s)": [
      {
        "hour": 0,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 1,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 2,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 3,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 4,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 5,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 6,
        "non_null": 2924,
        "zero": 2831,
        "mean": 0.0033226174057797548
      },
      {
        "hour": 7,
        "non_null": 2924,
        "zero": 1573,
        "mean": 0.38954827004278386
      },
      {
        "hour": 8,
        "non_null": 2924,
        "zero": 214,
        "mean": 2.7570908591275995
      },
      {
        "hour": 9,
        "non_null": 2924,
        "zero": 24,
        "mean": 8.21775896544015
      },
      {
        "hour": 10,
        "non_null": 2924,
        "zero": 20,
        "mean": 13.854853874404924
      },
      {
        "hour": 11,
        "non_null": 2924,
        "zero": 16,
        "mean": 18.336147974644323
      },
      {
        "hour": 12,
        "non_null": 2924,
        "zero": 16,
        "mean": 20.859574545434338
      },
      {
        "hour": 13,
        "non_null": 2924,
        "zero": 16,
        "mean": 21.723862858187417
      },
      {
        "hour": 14,
        "non_null": 2924,
        "zero": 16,
        "mean": 20.908714205000003
      },
      {
        "hour": 15,
        "non_null": 2924,
        "zero": 13,
        "mean": 18.40551556215458
      },
      {
        "hour": 16,
        "non_null": 2924,
        "zero": 12,
        "mean": 14.531751305725034
      },
      {
        "hour": 17,
        "non_null": 2924,
        "zero": 12,
        "mean": 9.051351852480849
      },
      {
        "hour": 18,
        "non_null": 2924,
        "zero": 304,
        "mean": 3.3066505349547195
      },
      {
        "hour": 19,
        "non_null": 2924,
        "zero": 1602,
        "mean": 0.4723634670725376
      },
      {
        "hour": 20,
        "non_null": 2924,
        "zero": 2848,
        "mean": 0.025861947118502048
      },
      {
        "hour": 21,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 22,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 23,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      }
    ]
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 7 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "day_night": "UNRESOLVED: no verified coordinates/timezone; clock hours and zero irradiance do not prove night",
  "irradiance_conditions": [],
  "hourly_target_summary": {
    "Power (MW) / Time(year-month-day h:m:s)": [
      {
        "hour": 0,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 1,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 2,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 3,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 4,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 5,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 6,
        "non_null": 2924,
        "zero": 2894,
        "mean": 0.0008882800957592337
      },
      {
        "hour": 7,
        "non_null": 2924,
        "zero": 1889,
        "mean": 0.2800843392612859
      },
      {
        "hour": 8,
        "non_null": 2924,
        "zero": 485,
        "mean": 2.440780861491108
      },
      {
        "hour": 9,
        "non_null": 2924,
        "zero": 130,
        "mean": 7.682821896716827
      },
      {
        "hour": 10,
        "non_null": 2924,
        "zero": 124,
        "mean": 12.850436548905607
      },
      {
        "hour": 11,
        "non_null": 2924,
        "zero": 116,
        "mean": 16.172614077975375
      },
      {
        "hour": 12,
        "non_null": 2924,
        "zero": 120,
        "mean": 17.781224493160053
      },
      {
        "hour": 13,
        "non_null": 2924,
        "zero": 120,
        "mean": 18.008848077291383
      },
      {
        "hour": 14,
        "non_null": 2924,
        "zero": 116,
        "mean": 16.98641506908345
      },
      {
        "hour": 15,
        "non_null": 2924,
        "zero": 117,
        "mean": 14.905652931600548
      },
      {
        "hour": 16,
        "non_null": 2924,
        "zero": 119,
        "mean": 11.872100570793434
      },
      {
        "hour": 17,
        "non_null": 2924,
        "zero": 134,
        "mean": 7.664031005129959
      },
      {
        "hour": 18,
        "non_null": 2924,
        "zero": 469,
        "mean": 2.8215881299589602
      },
      {
        "hour": 19,
        "non_null": 2924,
        "zero": 1817,
        "mean": 0.3923743368673051
      },
      {
        "hour": 20,
        "non_null": 2924,
        "zero": 2889,
        "mean": 0.02628180677154583
      },
      {
        "hour": 21,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 22,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 23,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      }
    ]
  }
}
```

### data_original.rar!data_original/solar_stations/Solar station site 8 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "day_night": "UNRESOLVED: no verified coordinates/timezone; clock hours and zero irradiance do not prove night",
  "irradiance_conditions": [
    {
      "irradiance": "Total solar irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 36166,
      "zero_target": 35165,
      "positive_target": 1001,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Direct normal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 36166,
      "zero_target": 35165,
      "positive_target": 1001,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Global horizontal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 36166,
      "zero_target": 35165,
      "positive_target": 1001,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    }
  ],
  "hourly_target_summary": {
    "Power (MW) / Time(year-month-day h:m:s)": [
      {
        "hour": 0,
        "non_null": 2892,
        "zero": 2892,
        "mean": 0.0
      },
      {
        "hour": 1,
        "non_null": 2892,
        "zero": 2892,
        "mean": 0.0
      },
      {
        "hour": 2,
        "non_null": 2892,
        "zero": 2892,
        "mean": 0.0
      },
      {
        "hour": 3,
        "non_null": 2892,
        "zero": 2892,
        "mean": 0.0
      },
      {
        "hour": 4,
        "non_null": 2892,
        "zero": 2892,
        "mean": 0.0
      },
      {
        "hour": 5,
        "non_null": 2892,
        "zero": 2543,
        "mean": 0.019391424619640385
      },
      {
        "hour": 6,
        "non_null": 2892,
        "zero": 1266,
        "mean": 0.48283195020746883
      },
      {
        "hour": 7,
        "non_null": 2892,
        "zero": 139,
        "mean": 2.4162551867219917
      },
      {
        "hour": 8,
        "non_null": 2892,
        "zero": 2,
        "mean": 6.218457814661134
      },
      {
        "hour": 9,
        "non_null": 2892,
        "zero": 0,
        "mean": 9.988737897648686
      },
      {
        "hour": 10,
        "non_null": 2892,
        "zero": 0,
        "mean": 12.406974412171508
      },
      {
        "hour": 11,
        "non_null": 2892,
        "zero": 0,
        "mean": 13.958568464730291
      },
      {
        "hour": 12,
        "non_null": 2892,
        "zero": 0,
        "mean": 14.689125172890732
      },
      {
        "hour": 13,
        "non_null": 2892,
        "zero": 0,
        "mean": 14.420864453665283
      },
      {
        "hour": 14,
        "non_null": 2892,
        "zero": 0,
        "mean": 12.018125864453665
      },
      {
        "hour": 15,
        "non_null": 2892,
        "zero": 0,
        "mean": 8.290141770401107
      },
      {
        "hour": 16,
        "non_null": 2892,
        "zero": 5,
        "mean": 4.749498616874135
      },
      {
        "hour": 17,
        "non_null": 2892,
        "zero": 586,
        "mean": 1.6548962655601658
      },
      {
        "hour": 18,
        "non_null": 2892,
        "zero": 1867,
        "mean": 0.22207814661134162
      },
      {
        "hour": 19,
        "non_null": 2892,
        "zero": 2892,
        "mean": 0.0
      },
      {
        "hour": 20,
        "non_null": 2892,
        "zero": 2892,
        "mean": 0.0
      },
      {
        "hour": 21,
        "non_null": 2892,
        "zero": 2892,
        "mean": 0.0
      },
      {
        "hour": 22,
        "non_null": 2892,
        "zero": 2892,
        "mean": 0.0
      },
      {
        "hour": 23,
        "non_null": 2892,
        "zero": 2892,
        "mean": 0.0
      }
    ]
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 1 (Nominal capacity-50MW).xlsx [sheet1]

```json
{
  "day_night": "UNRESOLVED: no verified coordinates/timezone; clock hours and zero irradiance do not prove night",
  "irradiance_conditions": [
    {
      "irradiance": "Total solar irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 34236,
      "zero_target": 34195,
      "positive_target": 41,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Direct normal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 26747,
      "zero_target": 22756,
      "positive_target": 3991,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Global horizontal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 34277,
      "zero_target": 34221,
      "positive_target": 56,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    }
  ],
  "hourly_target_summary": {
    "Power (MW) / Time(year-month-day h:m:s)": [
      {
        "hour": 0,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 1,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 2,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 3,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 4,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 5,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 6,
        "non_null": 2924,
        "zero": 2548,
        "mean": 0.04255601915184679
      },
      {
        "hour": 7,
        "non_null": 2924,
        "zero": 1613,
        "mean": 0.6193584103967168
      },
      {
        "hour": 8,
        "non_null": 2924,
        "zero": 854,
        "mean": 3.554154172708619
      },
      {
        "hour": 9,
        "non_null": 2924,
        "zero": 105,
        "mean": 10.813127180574556
      },
      {
        "hour": 10,
        "non_null": 2924,
        "zero": 12,
        "mean": 20.270795838235294
      },
      {
        "hour": 11,
        "non_null": 2924,
        "zero": 12,
        "mean": 27.301747183310535
      },
      {
        "hour": 12,
        "non_null": 2924,
        "zero": 10,
        "mean": 30.906512040013677
      },
      {
        "hour": 13,
        "non_null": 2924,
        "zero": 8,
        "mean": 31.86349688235294
      },
      {
        "hour": 14,
        "non_null": 2924,
        "zero": 8,
        "mean": 31.088419671682626
      },
      {
        "hour": 15,
        "non_null": 2924,
        "zero": 8,
        "mean": 28.429678360123116
      },
      {
        "hour": 16,
        "non_null": 2924,
        "zero": 8,
        "mean": 23.30759641997264
      },
      {
        "hour": 17,
        "non_null": 2924,
        "zero": 10,
        "mean": 15.127454021545827
      },
      {
        "hour": 18,
        "non_null": 2924,
        "zero": 482,
        "mean": 6.787130495896033
      },
      {
        "hour": 19,
        "non_null": 2924,
        "zero": 1263,
        "mean": 1.7120532093023253
      },
      {
        "hour": 20,
        "non_null": 2924,
        "zero": 2060,
        "mean": 0.23958497674418605
      },
      {
        "hour": 21,
        "non_null": 2924,
        "zero": 2873,
        "mean": 0.0009974473324213407
      },
      {
        "hour": 22,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 23,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      }
    ]
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 2 (Nominal capacity-130MW).xlsx [sheet1]

```json
{
  "day_night": "UNRESOLVED: no verified coordinates/timezone; clock hours and zero irradiance do not prove night",
  "irradiance_conditions": [
    {
      "irradiance": "Total solar irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 36083,
      "zero_target": 76,
      "positive_target": 36007,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Direct normal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 36086,
      "zero_target": 76,
      "positive_target": 36010,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Global horizontal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 36163,
      "zero_target": 76,
      "positive_target": 36087,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    }
  ],
  "hourly_target_summary": {
    "Power (MW) / Time(year-month-day h:m:s)": [
      {
        "hour": 0,
        "non_null": 2924,
        "zero": 8,
        "mean": 0.2383608549931601
      },
      {
        "hour": 1,
        "non_null": 2924,
        "zero": 8,
        "mean": 0.23963368513679892
      },
      {
        "hour": 2,
        "non_null": 2924,
        "zero": 8,
        "mean": 0.24103113474692203
      },
      {
        "hour": 3,
        "non_null": 2924,
        "zero": 8,
        "mean": 0.24233864603283176
      },
      {
        "hour": 4,
        "non_null": 2924,
        "zero": 8,
        "mean": 0.24302528043775648
      },
      {
        "hour": 5,
        "non_null": 2924,
        "zero": 6,
        "mean": 0.2435483785909713
      },
      {
        "hour": 6,
        "non_null": 2924,
        "zero": 4,
        "mean": 0.24386565526675785
      },
      {
        "hour": 7,
        "non_null": 2924,
        "zero": 4,
        "mean": 0.27945265663474694
      },
      {
        "hour": 8,
        "non_null": 2924,
        "zero": 4,
        "mean": 1.595132081395349
      },
      {
        "hour": 9,
        "non_null": 2924,
        "zero": 4,
        "mean": 7.724183329685363
      },
      {
        "hour": 10,
        "non_null": 2924,
        "zero": 4,
        "mean": 22.85042668160055
      },
      {
        "hour": 11,
        "non_null": 2924,
        "zero": 4,
        "mean": 42.3147847004104
      },
      {
        "hour": 12,
        "non_null": 2924,
        "zero": 4,
        "mean": 57.410338152872775
      },
      {
        "hour": 13,
        "non_null": 2924,
        "zero": 4,
        "mean": 64.4756792376881
      },
      {
        "hour": 14,
        "non_null": 2924,
        "zero": 4,
        "mean": 64.03834460123119
      },
      {
        "hour": 15,
        "non_null": 2924,
        "zero": 4,
        "mean": 61.77970449726402
      },
      {
        "hour": 16,
        "non_null": 2924,
        "zero": 4,
        "mean": 56.4171675752394
      },
      {
        "hour": 17,
        "non_null": 2924,
        "zero": 4,
        "mean": 45.011940214432286
      },
      {
        "hour": 18,
        "non_null": 2924,
        "zero": 3,
        "mean": 27.697099370383036
      },
      {
        "hour": 19,
        "non_null": 2924,
        "zero": 0,
        "mean": 11.791446187756497
      },
      {
        "hour": 20,
        "non_null": 2924,
        "zero": 0,
        "mean": 3.3483897096443234
      },
      {
        "hour": 21,
        "non_null": 2924,
        "zero": 0,
        "mean": 0.6727669480164159
      },
      {
        "hour": 22,
        "non_null": 2924,
        "zero": 9,
        "mean": 0.2704394781121751
      },
      {
        "hour": 23,
        "non_null": 2924,
        "zero": 12,
        "mean": 0.2506237824897401
      }
    ]
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 3 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "day_night": "UNRESOLVED: no verified coordinates/timezone; clock hours and zero irradiance do not prove night",
  "irradiance_conditions": [
    {
      "irradiance": "Total solar irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 10862,
      "zero_target": 178,
      "positive_target": 1188,
      "negative_target": 9496,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Direct normal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 14120,
      "zero_target": 245,
      "positive_target": 4679,
      "negative_target": 9196,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Global horizontal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 11125,
      "zero_target": 197,
      "positive_target": 1433,
      "negative_target": 9495,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    }
  ],
  "hourly_target_summary": {
    "Power (MW) / Time(year-month-day h:m:s)": [
      {
        "hour": 0,
        "non_null": 848,
        "zero": 12,
        "mean": -0.03522700471698113
      },
      {
        "hour": 1,
        "non_null": 848,
        "zero": 12,
        "mean": -0.03531615566037736
      },
      {
        "hour": 2,
        "non_null": 848,
        "zero": 12,
        "mean": -0.03531120283018868
      },
      {
        "hour": 3,
        "non_null": 848,
        "zero": 12,
        "mean": -0.035274056603773585
      },
      {
        "hour": 4,
        "non_null": 848,
        "zero": 20,
        "mean": -0.03436597995283019
      },
      {
        "hour": 5,
        "non_null": 848,
        "zero": 18,
        "mean": 0.19512787676886795
      },
      {
        "hour": 6,
        "non_null": 848,
        "zero": 13,
        "mean": 1.2292992877358493
      },
      {
        "hour": 7,
        "non_null": 848,
        "zero": 17,
        "mean": 4.066604454599057
      },
      {
        "hour": 8,
        "non_null": 848,
        "zero": 16,
        "mean": 8.661602443985851
      },
      {
        "hour": 9,
        "non_null": 848,
        "zero": 16,
        "mean": 13.259374220518868
      },
      {
        "hour": 10,
        "non_null": 848,
        "zero": 14,
        "mean": 16.174105912735847
      },
      {
        "hour": 11,
        "non_null": 848,
        "zero": 16,
        "mean": 17.729386462853775
      },
      {
        "hour": 12,
        "non_null": 848,
        "zero": 16,
        "mean": 17.75016224410377
      },
      {
        "hour": 13,
        "non_null": 848,
        "zero": 16,
        "mean": 16.51363837441038
      },
      {
        "hour": 14,
        "non_null": 848,
        "zero": 16,
        "mean": 14.690677787146226
      },
      {
        "hour": 15,
        "non_null": 848,
        "zero": 16,
        "mean": 11.320586692806604
      },
      {
        "hour": 16,
        "non_null": 848,
        "zero": 14,
        "mean": 6.615111405660376
      },
      {
        "hour": 17,
        "non_null": 848,
        "zero": 16,
        "mean": 2.39738532134434
      },
      {
        "hour": 18,
        "non_null": 848,
        "zero": 14,
        "mean": 0.49711034080188676
      },
      {
        "hour": 19,
        "non_null": 848,
        "zero": 12,
        "mean": -0.0018772093160377382
      },
      {
        "hour": 20,
        "non_null": 848,
        "zero": 12,
        "mean": -0.03521462264150944
      },
      {
        "hour": 21,
        "non_null": 848,
        "zero": 12,
        "mean": -0.035175000000000005
      },
      {
        "hour": 22,
        "non_null": 848,
        "zero": 12,
        "mean": -0.035298820754716985
      },
      {
        "hour": 23,
        "non_null": 848,
        "zero": 12,
        "mean": -0.03518985849056604
      }
    ]
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 4 (Nominal capacity-130MW).xlsx [Sheet1]

```json
{
  "day_night": "UNRESOLVED: no verified coordinates/timezone; clock hours and zero irradiance do not prove night",
  "irradiance_conditions": [
    {
      "irradiance": "Total solar irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 36149,
      "zero_target": 627,
      "positive_target": 3000,
      "negative_target": 32522,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Direct normal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 36529,
      "zero_target": 669,
      "positive_target": 2567,
      "negative_target": 33293,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Global horizontal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 36532,
      "zero_target": 669,
      "positive_target": 2567,
      "negative_target": 33296,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    }
  ],
  "hourly_target_summary": {
    "Power (MW) / Time(year-month-day h:m:s)": [
      {
        "hour": 0,
        "non_null": 2924,
        "zero": 52,
        "mean": -0.22959302325581402
      },
      {
        "hour": 1,
        "non_null": 2924,
        "zero": 52,
        "mean": -0.23098768809849526
      },
      {
        "hour": 2,
        "non_null": 2924,
        "zero": 52,
        "mean": -0.23307216142270865
      },
      {
        "hour": 3,
        "non_null": 2924,
        "zero": 52,
        "mean": -0.23421135430916554
      },
      {
        "hour": 4,
        "non_null": 2924,
        "zero": 52,
        "mean": -0.23476641586867308
      },
      {
        "hour": 5,
        "non_null": 2923,
        "zero": 46,
        "mean": -0.1929627095449881
      },
      {
        "hour": 6,
        "non_null": 2924,
        "zero": 39,
        "mean": 1.341829343365253
      },
      {
        "hour": 7,
        "non_null": 2924,
        "zero": 35,
        "mean": 8.153047879616963
      },
      {
        "hour": 8,
        "non_null": 2924,
        "zero": 23,
        "mean": 21.72323358413133
      },
      {
        "hour": 9,
        "non_null": 2922,
        "zero": 20,
        "mean": 37.238722108145105
      },
      {
        "hour": 10,
        "non_null": 2924,
        "zero": 20,
        "mean": 49.099710670314636
      },
      {
        "hour": 11,
        "non_null": 2924,
        "zero": 20,
        "mean": 56.24090424076608
      },
      {
        "hour": 12,
        "non_null": 2924,
        "zero": 24,
        "mean": 57.42929958960328
      },
      {
        "hour": 13,
        "non_null": 2924,
        "zero": 24,
        "mean": 53.83022571819426
      },
      {
        "hour": 14,
        "non_null": 2924,
        "zero": 24,
        "mean": 46.45365458276334
      },
      {
        "hour": 15,
        "non_null": 2923,
        "zero": 25,
        "mean": 34.88843585357509
      },
      {
        "hour": 16,
        "non_null": 2923,
        "zero": 25,
        "mean": 20.962209373930893
      },
      {
        "hour": 17,
        "non_null": 2924,
        "zero": 35,
        "mean": 8.365229822161423
      },
      {
        "hour": 18,
        "non_null": 2924,
        "zero": 33,
        "mean": 1.6413197674418605
      },
      {
        "hour": 19,
        "non_null": 2924,
        "zero": 55,
        "mean": -0.14910909712722298
      },
      {
        "hour": 20,
        "non_null": 2924,
        "zero": 66,
        "mean": -0.22505061559507525
      },
      {
        "hour": 21,
        "non_null": 2923,
        "zero": 56,
        "mean": -0.22998084160109475
      },
      {
        "hour": 22,
        "non_null": 2924,
        "zero": 52,
        "mean": -0.23091450068399455
      },
      {
        "hour": 23,
        "non_null": 2924,
        "zero": 54,
        "mean": -0.2298307113543092
      }
    ]
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 5 (Nominal capacity-110MW).xlsx [Sheet1]

```json
{
  "day_night": "UNRESOLVED: no verified coordinates/timezone; clock hours and zero irradiance do not prove night",
  "irradiance_conditions": [
    {
      "irradiance": "Total solar irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 35624,
      "zero_target": 17818,
      "positive_target": 70,
      "negative_target": 17736,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Direct normal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 34910,
      "zero_target": 16929,
      "positive_target": 798,
      "negative_target": 17183,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Global horizontal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 35471,
      "zero_target": 17758,
      "positive_target": 63,
      "negative_target": 17650,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    }
  ],
  "hourly_target_summary": {
    "Power (MW) / Time(year-month-day h:m:s)": [
      {
        "hour": 0,
        "non_null": 2924,
        "zero": 1464,
        "mean": -0.14350547195622435
      },
      {
        "hour": 1,
        "non_null": 2924,
        "zero": 1464,
        "mean": -0.143515731874145
      },
      {
        "hour": 2,
        "non_null": 2924,
        "zero": 1464,
        "mean": -0.14452120383036937
      },
      {
        "hour": 3,
        "non_null": 2924,
        "zero": 1464,
        "mean": -0.14435362517099865
      },
      {
        "hour": 4,
        "non_null": 2924,
        "zero": 1464,
        "mean": -0.14466142270861834
      },
      {
        "hour": 5,
        "non_null": 2924,
        "zero": 1443,
        "mean": -0.0930984952120383
      },
      {
        "hour": 6,
        "non_null": 2924,
        "zero": 877,
        "mean": 1.4817407660738715
      },
      {
        "hour": 7,
        "non_null": 2924,
        "zero": 302,
        "mean": 7.942489740082079
      },
      {
        "hour": 8,
        "non_null": 2924,
        "zero": 50,
        "mean": 19.92074555403557
      },
      {
        "hour": 9,
        "non_null": 2924,
        "zero": 31,
        "mean": 32.83355677154583
      },
      {
        "hour": 10,
        "non_null": 2924,
        "zero": 24,
        "mean": 42.92070109439125
      },
      {
        "hour": 11,
        "non_null": 2924,
        "zero": 24,
        "mean": 48.72671340629276
      },
      {
        "hour": 12,
        "non_null": 2924,
        "zero": 24,
        "mean": 50.53304035567715
      },
      {
        "hour": 13,
        "non_null": 2924,
        "zero": 21,
        "mean": 48.0643023255814
      },
      {
        "hour": 14,
        "non_null": 2924,
        "zero": 20,
        "mean": 40.918047195622435
      },
      {
        "hour": 15,
        "non_null": 2924,
        "zero": 21,
        "mean": 30.313830369357046
      },
      {
        "hour": 16,
        "non_null": 2924,
        "zero": 38,
        "mean": 17.72768809849521
      },
      {
        "hour": 17,
        "non_null": 2924,
        "zero": 353,
        "mean": 7.036077291381668
      },
      {
        "hour": 18,
        "non_null": 2924,
        "zero": 844,
        "mean": 1.3501949384404925
      },
      {
        "hour": 19,
        "non_null": 2924,
        "zero": 1373,
        "mean": -0.08576949384404925
      },
      {
        "hour": 20,
        "non_null": 2924,
        "zero": 1464,
        "mean": -0.13556429548563612
      },
      {
        "hour": 21,
        "non_null": 2924,
        "zero": 1464,
        "mean": -0.13782831737346102
      },
      {
        "hour": 22,
        "non_null": 2924,
        "zero": 1464,
        "mean": -0.13995212038303695
      },
      {
        "hour": 23,
        "non_null": 2924,
        "zero": 1464,
        "mean": -0.1426265389876881
      }
    ]
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 6 (Nominal capacity-35MW).xlsx [Sheet1]

```json
{
  "day_night": "UNRESOLVED: no verified coordinates/timezone; clock hours and zero irradiance do not prove night",
  "irradiance_conditions": [
    {
      "irradiance": "Total solar irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 35035,
      "zero_target": 35024,
      "positive_target": 11,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Direct normal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 35993,
      "zero_target": 35232,
      "positive_target": 761,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Global horizontal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 35438,
      "zero_target": 35373,
      "positive_target": 65,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    }
  ],
  "hourly_target_summary": {
    "Power (MW) / Time(year-month-day h:m:s)": [
      {
        "hour": 0,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 1,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 2,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 3,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 4,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 5,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 6,
        "non_null": 2924,
        "zero": 2831,
        "mean": 0.0033226174057797548
      },
      {
        "hour": 7,
        "non_null": 2924,
        "zero": 1571,
        "mean": 0.39392651914675103
      },
      {
        "hour": 8,
        "non_null": 2924,
        "zero": 211,
        "mean": 2.756648542609131
      },
      {
        "hour": 9,
        "non_null": 2924,
        "zero": 24,
        "mean": 8.236659785029756
      },
      {
        "hour": 10,
        "non_null": 2924,
        "zero": 20,
        "mean": 13.876027836265388
      },
      {
        "hour": 11,
        "non_null": 2924,
        "zero": 16,
        "mean": 18.33747834359097
      },
      {
        "hour": 12,
        "non_null": 2924,
        "zero": 16,
        "mean": 20.856954619579344
      },
      {
        "hour": 13,
        "non_null": 2924,
        "zero": 16,
        "mean": 21.72369482364569
      },
      {
        "hour": 14,
        "non_null": 2924,
        "zero": 16,
        "mean": 20.905082878392612
      },
      {
        "hour": 15,
        "non_null": 2924,
        "zero": 13,
        "mean": 18.387816634452804
      },
      {
        "hour": 16,
        "non_null": 2924,
        "zero": 12,
        "mean": 14.521148934316004
      },
      {
        "hour": 17,
        "non_null": 2924,
        "zero": 12,
        "mean": 9.033862340579343
      },
      {
        "hour": 18,
        "non_null": 2924,
        "zero": 306,
        "mean": 3.274272742116142
      },
      {
        "hour": 19,
        "non_null": 2924,
        "zero": 1608,
        "mean": 0.4349594543160396
      },
      {
        "hour": 20,
        "non_null": 2924,
        "zero": 2851,
        "mean": 0.002443684464603283
      },
      {
        "hour": 21,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 22,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 23,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      }
    ]
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 7 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "day_night": "UNRESOLVED: no verified coordinates/timezone; clock hours and zero irradiance do not prove night",
  "irradiance_conditions": [
    {
      "irradiance": "Total solar irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 28082,
      "zero_target": 28075,
      "positive_target": 7,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Direct normal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 37856,
      "zero_target": 34814,
      "positive_target": 3042,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Global horizontal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 34039,
      "zero_target": 34019,
      "positive_target": 20,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    }
  ],
  "hourly_target_summary": {
    "Power (MW) / Time(year-month-day h:m:s)": [
      {
        "hour": 0,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 1,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 2,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 3,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 4,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 5,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 6,
        "non_null": 2924,
        "zero": 2894,
        "mean": 0.0008882800957592337
      },
      {
        "hour": 7,
        "non_null": 2924,
        "zero": 1888,
        "mean": 0.28553134575923395
      },
      {
        "hour": 8,
        "non_null": 2924,
        "zero": 482,
        "mean": 2.4427658139534882
      },
      {
        "hour": 9,
        "non_null": 2924,
        "zero": 126,
        "mean": 7.7041912544459645
      },
      {
        "hour": 10,
        "non_null": 2924,
        "zero": 120,
        "mean": 12.89023146511628
      },
      {
        "hour": 11,
        "non_null": 2924,
        "zero": 116,
        "mean": 16.155770940834472
      },
      {
        "hour": 12,
        "non_null": 2924,
        "zero": 120,
        "mean": 17.79395340355677
      },
      {
        "hour": 13,
        "non_null": 2924,
        "zero": 120,
        "mean": 18.009027511969904
      },
      {
        "hour": 14,
        "non_null": 2924,
        "zero": 116,
        "mean": 16.989221954514367
      },
      {
        "hour": 15,
        "non_null": 2924,
        "zero": 117,
        "mean": 14.906673907318742
      },
      {
        "hour": 16,
        "non_null": 2924,
        "zero": 119,
        "mean": 11.859391952804378
      },
      {
        "hour": 17,
        "non_null": 2924,
        "zero": 134,
        "mean": 7.651738711696306
      },
      {
        "hour": 18,
        "non_null": 2924,
        "zero": 471,
        "mean": 2.7855705748974007
      },
      {
        "hour": 19,
        "non_null": 2924,
        "zero": 1822,
        "mean": 0.35214542647058833
      },
      {
        "hour": 20,
        "non_null": 2924,
        "zero": 2892,
        "mean": 0.0038659380984952126
      },
      {
        "hour": 21,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 22,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 23,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      }
    ]
  }
}
```

### data_processed.rar!data_processed/solar_stations/Solar station site 8 (Nominal capacity-30MW).xlsx [Sheet1]

```json
{
  "day_night": "UNRESOLVED: no verified coordinates/timezone; clock hours and zero irradiance do not prove night",
  "irradiance_conditions": [
    {
      "irradiance": "Total solar irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 36166,
      "zero_target": 35165,
      "positive_target": 1001,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Direct normal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 36166,
      "zero_target": 35165,
      "positive_target": 1001,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Global horizontal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 36166,
      "zero_target": 35165,
      "positive_target": 1001,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    }
  ],
  "hourly_target_summary": {
    "Power (MW) / Time(year-month-day h:m:s)": [
      {
        "hour": 0,
        "non_null": 2892,
        "zero": 2892,
        "mean": 0.0
      },
      {
        "hour": 1,
        "non_null": 2892,
        "zero": 2892,
        "mean": 0.0
      },
      {
        "hour": 2,
        "non_null": 2892,
        "zero": 2892,
        "mean": 0.0
      },
      {
        "hour": 3,
        "non_null": 2892,
        "zero": 2892,
        "mean": 0.0
      },
      {
        "hour": 4,
        "non_null": 2892,
        "zero": 2892,
        "mean": 0.0
      },
      {
        "hour": 5,
        "non_null": 2892,
        "zero": 2543,
        "mean": 0.019391424619640385
      },
      {
        "hour": 6,
        "non_null": 2892,
        "zero": 1266,
        "mean": 0.48283195020746883
      },
      {
        "hour": 7,
        "non_null": 2892,
        "zero": 139,
        "mean": 2.4162551867219917
      },
      {
        "hour": 8,
        "non_null": 2892,
        "zero": 2,
        "mean": 6.218457814661134
      },
      {
        "hour": 9,
        "non_null": 2892,
        "zero": 0,
        "mean": 9.988737897648686
      },
      {
        "hour": 10,
        "non_null": 2892,
        "zero": 0,
        "mean": 12.406974412171508
      },
      {
        "hour": 11,
        "non_null": 2892,
        "zero": 0,
        "mean": 13.958568464730291
      },
      {
        "hour": 12,
        "non_null": 2892,
        "zero": 0,
        "mean": 14.689125172890732
      },
      {
        "hour": 13,
        "non_null": 2892,
        "zero": 0,
        "mean": 14.420864453665283
      },
      {
        "hour": 14,
        "non_null": 2892,
        "zero": 0,
        "mean": 12.018125864453665
      },
      {
        "hour": 15,
        "non_null": 2892,
        "zero": 0,
        "mean": 8.290141770401107
      },
      {
        "hour": 16,
        "non_null": 2892,
        "zero": 5,
        "mean": 4.749498616874135
      },
      {
        "hour": 17,
        "non_null": 2892,
        "zero": 586,
        "mean": 1.6548962655601658
      },
      {
        "hour": 18,
        "non_null": 2892,
        "zero": 1867,
        "mean": 0.22207814661134162
      },
      {
        "hour": 19,
        "non_null": 2892,
        "zero": 2892,
        "mean": 0.0
      },
      {
        "hour": 20,
        "non_null": 2892,
        "zero": 2892,
        "mean": 0.0
      },
      {
        "hour": 21,
        "non_null": 2892,
        "zero": 2892,
        "mean": 0.0
      },
      {
        "hour": 22,
        "non_null": 2892,
        "zero": 2892,
        "mean": 0.0
      },
      {
        "hour": 23,
        "non_null": 2892,
        "zero": 2892,
        "mean": 0.0
      }
    ]
  }
}
```

### Solar station site 1 (Nominal capacity-50MW).xlsx [sheet1]

```json
{
  "day_night": "UNRESOLVED: no verified coordinates/timezone; clock hours and zero irradiance do not prove night",
  "irradiance_conditions": [
    {
      "irradiance": "Total solar irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 34204,
      "zero_target": 34163,
      "positive_target": 41,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Direct normal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 26706,
      "zero_target": 22726,
      "positive_target": 3980,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    },
    {
      "irradiance": "Global horizontal irradiance (W/m2)",
      "target": "Power (MW)",
      "zero_irradiance_target_observations": 34245,
      "zero_target": 34189,
      "positive_target": 56,
      "negative_target": 0,
      "note": "Observed zero-irradiance association, not an astronomical night classification"
    }
  ],
  "hourly_target_summary": {
    "Power (MW) / Time(year-month-day h:m:s)": [
      {
        "hour": 0,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 1,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 2,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 3,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 4,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 5,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 6,
        "non_null": 2924,
        "zero": 2548,
        "mean": 0.0425262424760602
      },
      {
        "hour": 7,
        "non_null": 2924,
        "zero": 1613,
        "mean": 0.6179867277701778
      },
      {
        "hour": 8,
        "non_null": 2924,
        "zero": 854,
        "mean": 3.555915092681259
      },
      {
        "hour": 9,
        "non_null": 2924,
        "zero": 105,
        "mean": 10.817056751709986
      },
      {
        "hour": 10,
        "non_null": 2924,
        "zero": 12,
        "mean": 20.270795838235294
      },
      {
        "hour": 11,
        "non_null": 2924,
        "zero": 12,
        "mean": 27.301747183310535
      },
      {
        "hour": 12,
        "non_null": 2924,
        "zero": 10,
        "mean": 30.9065564750342
      },
      {
        "hour": 13,
        "non_null": 2924,
        "zero": 8,
        "mean": 31.863327343365253
      },
      {
        "hour": 14,
        "non_null": 2924,
        "zero": 8,
        "mean": 31.088385107045145
      },
      {
        "hour": 15,
        "non_null": 2924,
        "zero": 8,
        "mean": 28.429521315321473
      },
      {
        "hour": 16,
        "non_null": 2924,
        "zero": 8,
        "mean": 23.307554080711355
      },
      {
        "hour": 17,
        "non_null": 2924,
        "zero": 10,
        "mean": 15.127454021545827
      },
      {
        "hour": 18,
        "non_null": 2924,
        "zero": 483,
        "mean": 6.78710541621067
      },
      {
        "hour": 19,
        "non_null": 2924,
        "zero": 1262,
        "mean": 1.7090952520519838
      },
      {
        "hour": 20,
        "non_null": 2924,
        "zero": 2058,
        "mean": 0.2399727787277702
      },
      {
        "hour": 21,
        "non_null": 2924,
        "zero": 2873,
        "mean": 0.0009974473324213407
      },
      {
        "hour": 22,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      },
      {
        "hour": 23,
        "non_null": 2924,
        "zero": 2924,
        "mean": 0.0
      }
    ]
  }
}
```

## 9. Dataset Comparison

| File | Rows | Targets | Irradiance fields | Missing cells | Filename capacity MW |
| --- | --- | --- | --- | --- | --- |
| data_original.rar!data_original/solar_stations/Solar station site 1 (Nominal capacity-50MW).xlsx | 70176 | Power (MW) | 3 | 0 | 50.0 |
| data_original.rar!data_original/solar_stations/Solar station site 2 (Nominal capacity-130MW).xlsx | 70176 | Power (MW) | 3 | 0 | 130.0 |
| data_original.rar!data_original/solar_stations/Solar station site 3 (Nominal capacity-30MW).xlsx | 52608 | Power (MW) | 3 | 0 | 30.0 |
| data_original.rar!data_original/solar_stations/Solar station site 4 (Nominal capacity-130MW).xlsx | 70176 | Power (MW) | 3 | 6 | 130.0 |
| data_original.rar!data_original/solar_stations/Solar station site 5 (Nominal capacity-110MW).xlsx | 70176 | Power (MW) | 3 | 0 | 110.0 |
| data_original.rar!data_original/solar_stations/Solar station site 6 (Nominal capacity-35MW).xlsx | 70176 | Power (MW) | 3 | 0 | 35.0 |
| data_original.rar!data_original/solar_stations/Solar station site 7 (Nominal capacity-30MW).xlsx | 70176 | Power (MW) | 3 | 0 | 30.0 |
| data_original.rar!data_original/solar_stations/Solar station site 8 (Nominal capacity-30MW).xlsx | 69408 | Power (MW) | 3 | 0 | 30.0 |
| data_processed.rar!data_processed/solar_stations/Solar station site 1 (Nominal capacity-50MW).xlsx | 70176 | Power (MW) | 3 | 0 | 50.0 |
| data_processed.rar!data_processed/solar_stations/Solar station site 2 (Nominal capacity-130MW).xlsx | 70176 | Power (MW) | 3 | 0 | 130.0 |
| data_processed.rar!data_processed/solar_stations/Solar station site 3 (Nominal capacity-30MW).xlsx | 20352 | Power (MW) | 3 | 0 | 30.0 |
| data_processed.rar!data_processed/solar_stations/Solar station site 4 (Nominal capacity-130MW).xlsx | 70176 | Power (MW) | 3 | 6 | 130.0 |
| data_processed.rar!data_processed/solar_stations/Solar station site 5 (Nominal capacity-110MW).xlsx | 70176 | Power (MW) | 3 | 0 | 110.0 |
| data_processed.rar!data_processed/solar_stations/Solar station site 6 (Nominal capacity-35MW).xlsx | 70176 | Power (MW) | 3 | 0 | 35.0 |
| data_processed.rar!data_processed/solar_stations/Solar station site 7 (Nominal capacity-30MW).xlsx | 70176 | Power (MW) | 3 | 0 | 30.0 |
| data_processed.rar!data_processed/solar_stations/Solar station site 8 (Nominal capacity-30MW).xlsx | 69408 | Power (MW) | 3 | 0 | 30.0 |
| Solar station site 1 (Nominal capacity-50MW).xlsx | 70176 | Power (MW) | 3 | 0 | 50.0 |

Coverage, cadence and duplicates are compared in section 4; header units in sections 3 and 5. Filename site/capacity labels are not independently verified metadata. Original/processed variants need documented processing and conflict policies. Cross-site combination requires verified identifiers, timezone, sensor definitions and units; matching timestamps alone are insufficient. No merging performed.

## 10. Selected Primary Candidate

PRIMARY CANDIDATE: `Solar station site 1 (Nominal capacity-50MW).xlsx` [sheet1]. It is an accessible standalone table with labelled numeric target units, irradiance and parseable duplicate-free timestamps. Selection prefers the lowest missing-cell rate among eligible standalone files, then path for determinism. This is a conditional inspection choice, not proof it is cleaner than all archived sites. Archive variants remain alternatives pending provenance verification.

## 11. Unresolved Questions

Source URL/license and processing history; site coordinates/timezone; filename nominal versus installed capacity; AC/DC power and metering/interval-average convention; irradiance plane and meaning of total versus global; sensor offsets and sentinels; curtailment/outages and negative output; true nighttime classification; observed versus forecast-weather availability. Publisher-labelled processed tables must not be assumed leakage-free.

## 12. Recommended Next Step

SOLAR PREPROCESSING (Milestone 5B): verify the selected schema and semantics; define auditable per-column sentinel, missing and target policies; preserve legitimate zero output; establish timestamp conventions and chronological splits; fit any learned transformation on training only. Define estimation versus forecasting and input availability before feature engineering. No preprocessing is implemented in 5A.

Reproduce: `python -m ml.data_processing.run_solar_analysis`. Requires existing dependencies and libarchive-compatible tar. Source SHA-256 values are checked before/after analysis and against the previous solar manifest on reruns.
