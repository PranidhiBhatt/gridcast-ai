"""Small synthetic solar fixtures; no downloaded files required."""

import json

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from ml.data_processing.solar_data_inspector import discover_solar_files, inspect_solar_dataset
from ml.data_processing.run_solar_analysis import run_analysis


def test_discovery(tmp_path):
    (tmp_path / 'solar.csv').touch()
    (tmp_path / 'wind.csv').touch()
    (tmp_path / 'pv_data.xlsx').touch()
    assert {p.name for p in discover_solar_files(tmp_path)} == {'solar.csv', 'pv_data.xlsx'}


def test_schema_statistics_flags_and_integrity():
    frame = pd.DataFrame({'timestamp': ['2024-01-01 00:00', '2024-01-01 00:30', '2024-01-01 00:45', 'bad'],
                          'Irradiance (W/m2)': [0., -99., 100., None],
                          'Power (MW)': [0., -1., 4., 1.]})
    before = frame.copy(deep=True)
    result = inspect_solar_dataset('solar.csv', data=frame, size_bytes=1)
    assert result['schema'][1]['dtype'] == 'float64'
    assert result['missing']['Irradiance (W/m2)'] == {'count': 1, 'percent': 25.}
    assert result['numeric']['Power (MW)']['mean'] == 1
    assert result['numeric']['Power (MW)']['median'] == .5
    assert result['suspicious']['Irradiance (W/m2)']['sentinel_counts']['-99'] == 1
    assert result['targets']['Power (MW)']['unit_in_header'] == 'MW'
    assert result['targets']['Power (MW)']['measurement'] == 'POWER'
    assert result['time']['timestamp']['parse_failures'] == 1
    assert result['time']['timestamp']['missing_intervals_on_modal_grid'] == 1
    assert 'UNRESOLVED' in result['solar_checks']['day_night']
    assert_frame_equal(before, frame)


def test_energy_and_unknown_units():
    frame = pd.DataFrame({'Energy (kWh)': [1, 2], 'Generation': ['bad', 'unknown']})
    result = inspect_solar_dataset('solar.csv', data=frame, size_bytes=1)
    assert result['targets']['Energy (kWh)']['measurement'] == 'ENERGY'
    assert result['targets']['Generation']['unit_in_header'] is None
    assert result['targets']['Generation']['statistics'] is None


def test_duplicate_times_and_zero_irradiance_are_not_night():
    frame = pd.DataFrame({'timestamp': ['2024-01-01', '2024-01-01'],
                          'Irradiance (W/m2)': [0, 0], 'Power (MW)': [2, 0]})
    result = inspect_solar_dataset('solar.csv', data=frame, size_bytes=1)
    assert result['time']['timestamp']['duplicate_timestamps'] == 1
    condition = result['solar_checks']['irradiance_conditions'][0]
    assert condition['positive_target'] == 1
    assert condition['zero_target'] == 1
    assert 'not an astronomical' in condition['note']


def test_errors(tmp_path):
    bad = tmp_path / 'solar.json'
    bad.write_text('bad json')
    with pytest.raises(ValueError, match='Cannot read'):
        inspect_solar_dataset(bad)
    unsupported = tmp_path / 'solar.bin'
    unsupported.touch()
    with pytest.raises(ValueError, match='Unsupported'):
        inspect_solar_dataset(unsupported)


def test_runner_reproducibility_and_hash_guard(tmp_path):
    path = tmp_path / 'solar.csv'
    path.write_text('timestamp,Power (MW),Irradiance (W/m2)\n2024-01-01,0,0\n2024-01-02,2,20\n')
    original = path.read_bytes()
    run_analysis(tmp_path)
    report = tmp_path / 'docs/solar_dataset_analysis.md'
    first = report.read_bytes()
    run_analysis(tmp_path)
    assert report.read_bytes() == first
    assert path.read_bytes() == original
    assert json.loads((tmp_path / 'docs/solar_dataset_sources.json').read_text())['selected_dataset'] == 'solar.csv'
    assert 'timezone' in json.loads((tmp_path / 'docs/solar_dataset_sources.json').read_text())['unresolved']
    path.write_text('changed')
    with pytest.raises(ValueError, match='Source changed'):
        run_analysis(tmp_path)


def test_excel_all_sheets_and_unnamed_headers(tmp_path):
    path = tmp_path / 'observations.xlsx'
    with pd.ExcelWriter(path) as writer:
        for sheet in ['first', 'second']:
            pd.DataFrame({'Irradiance': [0, 20], 'Power (MW)': [0, 1]}).to_excel(writer, sheet_name=sheet, index=False)
    run_analysis(tmp_path)
    meta = json.loads((tmp_path / 'docs/solar_dataset_sources.json').read_text())
    assert len(meta['datasets']) == 2
    assert meta['selected_dataset'] is None
