#!/usr/bin/env python3
"""Deduplicate the CanadaSHM6 national source model in ssm/CAN (approved plan
of 2026-10-14): remove, from the Eastern Arctic and Western Canada files and
their _collapsed variants, the copies of zones owned by another region. The
three Southeastern Canada files and the logic tree branches stay untouched.
Text-level removal: every other byte of the files is preserved. Also filters
the support CSVs. Usage: dedupCAN.py <CAN dir> [--check]"""
import re, sys, csv, io, pathlib, xml.etree.ElementTree as ET

CAN = pathlib.Path(sys.argv[1]).expanduser()
CHECK = '--check' in sys.argv
MODEL = CAN / 'model' / 'ssm_CAN'
OWNER = {  # removed id -> (file prefix, owner id, owner file, owner region)
    'SCCECH_ARC':  ('EasternArctic_H', 'SCCECH',  'SouthEasternCanada_H2', 'SE'),
    'SCCEAHE_ARC': ('EasternArctic_H', 'SCCEAHE', 'SouthEasternCanada_H2', 'SE'),
    'JMS_ARC':     ('EasternArctic_H', 'JMS',     'SouthEasternCanada_H2/HY/R2', 'SE'),
    'SCCWC_ARC':   ('EasternArctic_H', 'SCCWC',   'WesternCanada', 'WEST'),
    'SCCECR_ARC':  ('EasternArctic_R', 'SCCECR',  'SouthEasternCanada_R2', 'SE'),
    'ECM_ARC':     ('EasternArctic_R', 'ECM',     'SouthEasternCanada_R2', 'SE'),
    'SCCECHW':     ('WesternCanada',   'SCCECH',  'SouthEasternCanada_H2', 'SE'),
}
EXTRA = {('EasternArctic_R', 'JMS_ARC'): ('JMS', 'SouthEasternCanada_H2/HY/R2', 'SE'),
         ('EasternArctic_R', 'SCCWC_ARC'): ('SCCWC', 'WesternCanada', 'WEST')}
TARGETS = {}
for sid, (pre, oid, ofile, oreg) in OWNER.items():
    TARGETS.setdefault(pre, {})[sid] = (oid, ofile, oreg)
for (pre, sid), v in EXTRA.items():
    TARGETS.setdefault(pre, {})[sid] = v
REMOVED = set(OWNER) | {sid for (_, sid) in EXTRA}

def removeSources(path, ids):
    txt = path.read_text(encoding='utf-8')
    for sid, (oid, ofile, oreg) in ids.items():
        pat = re.compile(r'[ \t]*<areaSource id="%s"[^>]*>.*?</areaSource>[ \t]*\r?\n' % re.escape(sid), re.S)
        hits = pat.findall(txt)
        if len(hits) != 1: raise SystemExit(f'{path.name}: expected one block for {sid}, found {len(hits)}')
        if hits[0].count('<areaSource') != 1: raise SystemExit(f'{path.name}: nested block for {sid}')
        note = f'            <!-- {sid} removed 2026-10-14 (CAN v2020.1.4 deduplication): same zone as {oid} in {ofile}, owned by region {oreg} -->\n'
        txt = pat.sub(lambda m: note, txt, count=1)
    if not CHECK: path.write_text(txt, encoding='utf-8')
    return txt

def countSources(path):
    root = ET.parse(path).getroot()
    return sum(1 for e in root.iter() if e.tag.split('}')[-1].endswith('Source'))

report = []
for pre, ids in TARGETS.items():
    for suffix in ('', '_collapsed'):
        p = MODEL / f'CanadaSHM6_NBCC2020_{pre}{suffix}.xml'
        before = countSources(p)
        removeSources(p, ids)
        after = countSources(p) if not CHECK else before - len(ids)
        txt = p.read_text(encoding='utf-8')
        left = [s for s in ids if f'<areaSource id="{s}"' in txt]
        report.append((p.name, before, after, len(ids), left))
for name, b, a, n, left in report:
    print(f'{name:<52} sources {b:3d} -> {a:3d} (removed {n}) leftover={left}')

if not CHECK:
    for name in ('CAN_sources_index.csv', 'CAN_sources_depth.csv', 'CAN_sources_mmax.csv', 'CAN_sources_recurrence.csv', 'CAN_sources_evidence.csv'):
        p = CAN / 'support' / name
        raw = p.read_text(encoding='utf-8')
        rows = list(csv.reader(io.StringIO(raw)))
        hdr = rows[0]; i = hdr.index('provider_id')
        # Rows of the removed sources, plus the stale rows the index kept under the
        # pre-rename ids of the Arctic models (JMS, SCCEAHE, SCCECH, SCCWC, ECM, SCCECR),
        # which no longer exist in those files.
        STALE = {'JMS', 'SCCEAHE', 'SCCECH', 'SCCWC', 'ECM', 'SCCECR'}
        m = hdr.index('model_id') if 'model_id' in hdr else None
        keep = [r for r in rows[1:] if r and r[i] not in REMOVED and not (m is not None and 'EasternArctic' in r[m] and r[i] in STALE)]
        out = io.StringIO(); w = csv.writer(out, lineterminator='\n'); w.writerow(hdr); w.writerows(keep)
        p.write_text(out.getvalue(), encoding='utf-8')
        print(f'{name:<32} rows {len(rows)-1:4d} -> {len(keep):4d}')
