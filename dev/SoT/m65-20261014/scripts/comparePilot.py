"""Compare the pilot classical run (deduplicated CAN) with the committed
generation at the same Vs30: mean Sa at TR 475, 2475 and 10000 years, plus
the ratio pilot / committed. Usage: comparePilot.py PILOT_DIR COMMITTED_DIR
(each holding hazard_curve-mean-<IMT>_<id>.csv)."""
import csv, glob, math, sys
P, C = sys.argv[1], sys.argv[2]
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
IMTS = ['PGA', 'SA(0.1)', 'SA(0.2)', 'SA(0.3)', 'SA(0.5)', 'SA(1.0)', 'SA(2.0)']
def find(d, imt):
    c = glob.glob(f'{d}/hazard_curve-mean-{imt}_*.csv'); return c[0] if c else None
for label, tr in (('TR 475', 475), ('TR 2475', 2475), ('TR 2500', 2500), ('TR 10000', 10000)):
    p = 1 - math.exp(-50 / tr)
    print(f'\n=== Sa media [g] a {label} (PoE {p:.5f} en 50 años), Vs30 760 ===')
    print('run'.ljust(12) + ''.join(i.rjust(10) for i in IMTS))
    vals = {}
    for name, d in (('commit', C), ('pilot', P)):
        vals[name] = [imlAt(*readCurve(find(d, imt)), p) for imt in IMTS]
        print(name.ljust(12) + ''.join(f'{v:10.4f}' for v in vals[name]))
    print('pilot/commit'.ljust(12) + ''.join(f'{(a/b):10.3f}' for a, b in zip(vals['pilot'], vals['commit'])))
