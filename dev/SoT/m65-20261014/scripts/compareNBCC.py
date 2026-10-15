"""Compare the NBCC pilot (deduplicated CAN + official CanadaSHM6 trees) with
the 2024 replication (nrc), the deduplicated pilot with the general trees
(calc 34) and the committed generation, at Vs30 760, on every spectral period
the runs share. Usage: compareNBCC.py NBCC_DIR NRC_DIR DEDUP_DIR COMMIT_DIR"""
import csv, glob, math, sys, re
N, R, D, C = sys.argv[1:5]
def readCurve(path):
    rows = list(csv.reader(open(path))); hdr, val = rows[1], rows[2]
    iml = [float(h.split('-', 1)[1]) for h in hdr if h.startswith('poe-')]
    return iml, [float(v) for v in val[3:3 + len(iml)]]
def imlAt(iml, poe, t):
    for i in range(len(poe) - 1):
        a, b = poe[i], poe[i + 1]
        if a >= t >= b and a > 0 and b > 0 and a != b:
            f = (math.log(a) - math.log(t)) / (math.log(a) - math.log(b))
            return math.exp(math.log(iml[i]) + f * (math.log(iml[i + 1]) - math.log(iml[i])))
    return float('nan')
def imts(d):
    out = {}
    for f in glob.glob(f'{d}/hazard_curve-mean-*_*.csv'):
        m = re.search(r'hazard_curve-mean-(.+)_\d+\.csv$', f); k = m.group(1)
        key = 'PGA' if k == 'PGA' else ('PGV' if k == 'PGV' else f"SA({float(k[3:-1]):g})")
        out[key] = f
    return out
runs = {'nbcc': imts(N), 'nrc2024': imts(R), 'dedup+gen': imts(D), 'commit': imts(C)}
common = [k for k in runs['nbcc'] if k in runs['nrc2024'] and k != 'PGV']
common.sort(key=lambda k: -1 if k == 'PGA' else float(k[3:-1]))
for label, tr in (('TR 475', 475), ('TR 975', 975), ('TR 2475', 2475), ('TR 5000', 5000), ('TR 10000', 10000)):
    p = 1 - math.exp(-50 / tr)
    print(f'\n=== {label}: Sa media [g] a Vs30 760 y cociente frente a la corrida 2024 (nrc) ===')
    print('IMT'.ljust(10) + 'nrc2024'.rjust(9) + 'nbcc'.rjust(9) + 'nbcc/nrc'.rjust(10) + 'dedup+gen'.rjust(11) + '/nrc'.rjust(7) + 'commit'.rjust(9) + '/nrc'.rjust(7))
    for k in common:
        v = {}
        for name in runs:
            f = runs[name].get(k); v[name] = imlAt(*readCurve(f), p) if f else float('nan')
        r = v['nrc2024']
        print(f"{k:<10}{r:9.4f}{v['nbcc']:9.4f}{v['nbcc']/r:10.3f}{v['dedup+gen']:11.4f}{v['dedup+gen']/r:7.3f}{v['commit']:9.4f}{v['commit']/r:7.3f}")
