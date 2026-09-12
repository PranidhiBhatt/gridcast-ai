"""Reproduce Milestone 5A: python -m ml.data_processing.run_solar_analysis."""

from __future__ import annotations

import hashlib
import io
import json
import re
import subprocess
from pathlib import Path
from typing import Any

import pandas as pd

from ml.data_processing.data_inspector import SUPPORTED_EXTENSIONS, read_dataset
from ml.data_processing.run_wind_analysis import archive_members, sha256, table
from ml.data_processing.solar_data_inspector import feature_groups, inspect_solar_dataset

ROOT = Path(__file__).resolve().parents[2]


def block(value: Any) -> str:
    """Render finite structured diagnostics without raw table dumps."""
    return '```json\n' + json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n```\n'


def run_analysis(root: Path) -> None:
    """Screen data locations and archives, verify hashes, then write two small reports."""
    root = root.resolve()
    paths = sorted({p for folder in [root, root / 'ml/data'] if folder.exists()
                    for p in (folder.iterdir() if folder == root else folder.rglob('*'))
                    if p.is_file() and p.name != '.gitkeep'
                    and (p.suffix.lower() in SUPPORTED_EXTENSIONS | {'.rar', '.png'}
                         or re.search(r'solar|photovoltaic', p.name, re.I))})
    protected = {p.relative_to(root).as_posix(): sha256(p) for p in paths}
    metadata_path = root / 'docs/solar_dataset_sources.json'
    if metadata_path.exists():
        previous = json.loads(metadata_path.read_text(encoding='utf-8'))
        for p, digest in previous['source_hashes'].items():
            if protected.get(p) != digest:
                raise ValueError(f'Source changed since solar discovery: {p}')
    inventory: list[dict[str, Any]] = []
    reports: list[dict[str, Any]] = []

    def inspect_content(content: Any, label: str, size: int, digest: str) -> None:
        suffix = Path(label).suffix.lower()
        named = bool(re.search(r'solar|photovoltaic|\bpv\b', label, re.I))
        if suffix not in SUPPORTED_EXTENSIONS:
            inventory.append({'file': label, 'bytes': size, 'status': 'unsupported/non-tabular; no measurement evidence'})
            if named:
                raise ValueError(f'Unsupported solar candidate: {label}')
            return
        try:
            if suffix in {'.xlsx', '.xls'}:
                with pd.ExcelFile(content) as book:
                    for sheet in book.sheet_names:
                        headers = list(map(str, book.parse(sheet, nrows=0).columns))
                        candidate = named or bool(feature_groups(headers)['irradiance'])
                        inventory.append({'file': label, 'bytes': size, 'sheet': sheet,
                                          'status': 'solar candidate' if candidate else 'screened: no solar name/irradiance header evidence'})
                        if candidate:
                            frame = book.parse(sheet)
                            result = inspect_solar_dataset(label, data=frame, sheet_name=sheet, size_bytes=size)
                            result['sha256'] = digest
                            reports.append(result)
                            print(f'{label} [{sheet}]: {len(frame)} rows; {len(headers)} columns', flush=True)
            else:
                frame = read_dataset(content)
                candidate = named or bool(feature_groups(list(map(str, frame.columns)))['irradiance'])
                inventory.append({'file': label, 'bytes': size, 'status': 'solar candidate' if candidate else 'screened: no solar evidence'})
                if candidate:
                    result = inspect_solar_dataset(label, data=frame, size_bytes=size)
                    result['sha256'] = digest
                    reports.append(result)
        except Exception as exc:
            raise ValueError(f'Cannot inspect {label}: {exc}') from exc

    for p in paths:
        label = p.relative_to(root).as_posix()
        if p.suffix.lower() == '.rar':
            inventory.append({'file': label, 'bytes': p.stat().st_size, 'status': 'archive screened by member names; all solar members inspected'})
            for member, size in archive_members(p):
                if not re.search(r'solar|photovoltaic|\bpv\b', member, re.I):
                    continue
                content = subprocess.run(['tar', '-xOf', str(p), member], check=True, capture_output=True).stdout
                if len(content) != size:
                    raise ValueError(f'Archive size mismatch: {member}')
                inspect_content(io.BytesIO(content), f'{label}!{member}', size, hashlib.sha256(content).hexdigest())
        elif p.suffix.lower() in SUPPORTED_EXTENSIONS or re.search(r'solar|photovoltaic|\bpv\b|SS_', label, re.I):
            # Correlation PNG is inventoried only; it cannot verify measurement semantics.
            if p.suffix.lower() == '.png':
                inventory.append({'file': label, 'bytes': p.stat().st_size, 'status': 'image; not used as measurement evidence'})
            else:
                inspect_content(p, label, p.stat().st_size, protected[label])
    if not reports:
        raise ValueError('No solar tables found; no primary candidate can be selected')
    eligible = [r for r in reports if '!' not in r['file'] and r['rows'] > 0
                and any(t['statistics'] and t['unit_in_header'] for t in r['targets'].values())
                and any(t.get('parse_failures') == 0 and t.get('duplicate_timestamps') == 0 for t in r['time'].values())
                and r['feature_groups']['irradiance']]
    selected = min(eligible, key=lambda r: (sum(v['count'] for v in r['missing'].values()) / r['rows'], r['file'])) if eligible else None
    sections = ['# Solar Dataset Discovery and Analysis\n', '## 1. Purpose\n',
                'Milestone 5A inspects actual solar observations before solar preprocessing or training. Full-table statistics; no raw writes, copies, merges, conversions or models. Generic diagnostics and archive transport are reused unchanged; no wind feature constants are used.\n',
                '## 2. Files Discovered\n', 'Repository root and ml/data were inspected. ml/data/raw/solar contains only .gitkeep; ml/data/solar is absent in this checkout. Archives are read in memory. Other archive members retain their existing wind inventory.\n',
                table(['File', 'Bytes', 'Sheet', 'Status'], [[r['file'], r['bytes'], r.get('sheet', ''), r['status']] for r in inventory]),
                '## 3. Dataset Schemas\n']
    for r in reports:
        sections += [f"### {r['file']} [{r['sheet']}]\nRows: {r['rows']}; columns: {r['columns_count']}; format: {r['format']}.\n",
                     table(['Exact header (JSON quoted)', 'dtype', 'Missing', 'Missing %', 'Min', 'Max', 'Mean', 'Median'],
                           [[json.dumps(c['name'], ensure_ascii=False), c['dtype'], r['missing'][c['name']]['count'],
                             r['missing'][c['name']]['percent'], *[r['numeric'].get(c['name'], {}).get(k) for k in ['min','max','mean','median']]] for c in r['schema']]),
                     'Example values (first row only):\n', block(r['sample'][:1])]
    for title, key in [('4. Timestamp Analysis', 'time'), ('5. Candidate Generation Targets', 'targets'),
                       ('6. Candidate Features', 'feature_groups')]:
        sections += [f'## {title}\n']
        if key == 'feature_groups':
            sections += ['VERIFIED: exact header strings and explicit units. LIKELY: sensor categories inferred from those strings. UNRESOLVED: sensor plane, calibration, location and availability at forecast origin. Calendar candidates come only from parsed time columns; no features are created.\n']
        for r in reports:
            sections += [f"### {r['file']} [{r['sheet']}]\n", block(r[key])]
    sections += ['## 7. Data Quality Findings\n',
                 'VERIFIED ISSUE denotes observed missing/non-finite cells or duplicate records, not a decision to delete. Negative irradiance and out-of-range percentages are LIKELY ISSUE candidates. Sentinel counts, IQR outliers (1.5 IQR), constant and zero-heavy columns REQUIRE SEMANTIC VERIFICATION; negative temperature and zero generation are not automatically invalid.\n']
    for r in reports:
        sections += [f"### {r['file']} [{r['sheet']}]\n", block({'duplicates': r['duplicates'],
            'constant_columns': [c['name'] for c in r['schema'] if c['constant']],
            'sparse_columns': [c['name'] for c in r['schema'] if c['sparse_over_50_percent_missing']],
            'numeric_text_candidates': [c for c in r['schema'] if c['numeric_text_values']],
            'flags': r['suspicious'], 'numeric_checks': r['numeric']})]
    sections += ['## 8. Solar-Specific Findings\n',
                 'No astronomical day/night assignment is justified without coordinates and source timezone. Zero irradiance is an observational condition, potentially affected by sensor problems. Hourly summaries preserve source clock hours for naive values; explicit offsets use UTC for diagnostics. No energy-to-power conversion is performed.\n']
    for r in reports:
        sections += [f"### {r['file']} [{r['sheet']}]\n", block(r['solar_checks'])]
    sections += ['## 9. Dataset Comparison\n',
                 table(['File', 'Rows', 'Targets', 'Irradiance fields', 'Missing cells', 'Filename capacity MW'],
                       [[r['file'], r['rows'], ', '.join(r['targets']), len(r['feature_groups']['irradiance']), sum(v['count'] for v in r['missing'].values()), r['filename_capacity_label_mw']] for r in reports]),
                 'Coverage, cadence and duplicates are compared in section 4; header units in sections 3 and 5. Filename site/capacity labels are not independently verified metadata. Original/processed variants need documented processing and conflict policies. Cross-site combination requires verified identifiers, timezone, sensor definitions and units; matching timestamps alone are insufficient. No merging performed.\n',
                 '## 10. Selected Primary Candidate\n',
                 (f"PRIMARY CANDIDATE: `{selected['file']}` [{selected['sheet']}]. It is an accessible standalone table with labelled numeric target units, irradiance and parseable duplicate-free timestamps. Selection prefers the lowest missing-cell rate among eligible standalone files, then path for determinism. This is a conditional inspection choice, not proof it is cleaner than all archived sites. Archive variants remain alternatives pending provenance verification.\n" if selected else 'NO SUFFICIENT PRIMARY CANDIDATE: reviewed standalone eligibility criteria were not satisfied.\n'),
                 '## 11. Unresolved Questions\n',
                 'Source URL/license and processing history; site coordinates/timezone; filename nominal versus installed capacity; AC/DC power and metering/interval-average convention; irradiance plane and meaning of total versus global; sensor offsets and sentinels; curtailment/outages and negative output; true nighttime classification; observed versus forecast-weather availability. Publisher-labelled processed tables must not be assumed leakage-free.\n',
                 '## 12. Recommended Next Step\n',
                 'SOLAR PREPROCESSING (Milestone 5B): verify the selected schema and semantics; define auditable per-column sentinel, missing and target policies; preserve legitimate zero output; establish timestamp conventions and chronological splits; fit any learned transformation on training only. Define estimation versus forecasting and input availability before feature engineering. No preprocessing is implemented in 5A.\n',
                 'Reproduce: `python -m ml.data_processing.run_solar_analysis`. Requires existing dependencies and libarchive-compatible tar. Source SHA-256 values are checked before/after analysis and against the previous solar manifest on reruns.\n']
    for label, digest in protected.items():
        if sha256(root / label) != digest:
            raise RuntimeError(f'Source changed during inspection: {label}')
    meta = {'status': 'Milestone 5A; discovery and analysis only', 'source_hashes': protected,
            'selected_dataset': selected['file'] if selected else None,
            'datasets': [{k: r[k] for k in ['file','format','sheet','size_bytes','sha256','rows','columns_count','time','feature_groups','filename_capacity_label_mw']}
                         | {'target_columns': list(r['targets'])} for r in reports],
            'unresolved': sections[-4]}
    (root / 'docs').mkdir(exist_ok=True)
    (root / 'docs/solar_dataset_analysis.md').write_text('\n'.join(sections), encoding='utf-8')
    metadata_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    print(f'Inspected {len(reports)} solar tables; source hashes unchanged; selected: {meta["selected_dataset"]}', flush=True)


if __name__ == '__main__':
    run_analysis(ROOT)
