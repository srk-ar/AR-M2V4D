import csv, glob, math, os, re, sys
S = sys.argv[1]
def readCurve(path):
    with open(path) as f:
        rows = list(csv.reader(f))
    hdr = rows[1]; val = rows[2]
    iml = [float(h.split('-', 1)[1]) for h in hdr if h.startswith('poe-')]
    poe = [float(v) for v in val[3:3 + len(iml)]]
    return iml, poe
def imlAt(iml, poe, target):
    # log-log interpolation of IML at a target PoE on a monotonically decreasing curve
    for i in range(len(poe) - 1):
        a, b = poe[i], poe[i + 1]
        if a >= target >= b and a > 0 and b > 0 and a != b:
            la, lb = math.log(a), math.log(b); lt = math.log(target)
            f = (la - lt) / (la - lb)
            return math.exp(math.log(iml[i]) + f * (math.log(iml[i + 1]) - math.log(iml[i])))
    return float('nan')
IMTS = ['PGA', 'SA(0.1)', 'SA(0.2)', 'SA(0.3)', 'SA(0.5)', 'SA(1.0)', 'SA(2.0)']
RUNS = [('nrc_760', 'NRC 2024, SHM6 oficial, Vs30 760'), ('gem_760', 'GEM 2024, tablas SHM6-trial, Vs30 760'),
        ('cur_760', 'Actual M2V4D CAN+GMM generales, Vs30 760'), ('nrc_450', 'NRC 2024, Vs30 450 (clase C NRCan)'), ('gem_450', 'GEM 2024, Vs30 450')]
POES = [('TR 2475 (2 % en 50)', 0.02), ('TR 2500', 1 - math.exp(-50 / 2500)), ('TR 475 (10 % en 50)', 0.10)]
def find(run, imt):
    cands = glob.glob(f'{S}/hc/{run}/hazard_curve-mean-{imt}_*.csv')
    return cands[0] if cands else None
for label, p in POES:
    print(f'\n=== Sa media [g] a PoE {p:.5f} en 50 años: {label} ===')
    print('run'.ljust(10) + ''.join(i.rjust(10) for i in IMTS))
    for run, desc in RUNS:
        vals = []
        for imt in IMTS:
            f = find(run, imt)
            if f is None: vals.append('   n/a'); continue
            iml, poe = readCurve(f)
            vals.append(f'{imlAt(iml, poe, p):10.4f}')
        print(run.ljust(10) + ''.join(vals) + '   ' + desc)
    base = {}
    for imt in IMTS:
        f = find('nrc_760', imt); iml, poe = readCurve(f); base[imt] = imlAt(iml, poe, p)
    print('cur/nrc'.ljust(10) + ''.join(f'{(imlAt(*readCurve(find("cur_760", imt)), p) / base[imt]):10.3f}' for imt in IMTS) + '   cociente actual / NRC a 760')
    print('gem/nrc'.ljust(10) + ''.join(f'{(imlAt(*readCurve(find("gem_760", imt)), p) / base[imt]):10.3f}' for imt in IMTS) + '   cociente GEM / NRC a 760')
