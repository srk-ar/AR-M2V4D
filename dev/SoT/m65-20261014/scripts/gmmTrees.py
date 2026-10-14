import xml.etree.ElementTree as ET, sys, os, collections
NS = {'n': 'http://openquake.org/xmlns/nrml/0.4'}
G = os.path.expanduser('~/kashimaDB/openquake/gmm')
S = sys.argv[1]
FILES = [
 ('legacy NRC run (repo)      ', f'{S}/legacy-oq/nrc/nrc/CanadaSHM6-GMM-LT.xml'),
 ('legacy GEM run Vs30_760    ', f'{S}/legacy-oq/gem/gem/gmm/Vs30_760.xml'),
 ('kashimaDB legacy/shm6      ', f'{G}/legacy/shm6/gmmLT_SHM6.xml'),
 ('kashimaDB legacy/nbcc      ', f'{G}/legacy/nbcc/gmmLT_NBCC.xml'),
 ('kashimaDB legacy/gem       ', f'{G}/legacy/gem/gmmLT_GEM.xml'),
 ('kashimaDB legacy/usgs      ', f'{G}/legacy/usgs/gmmLT_USGS.xml'),
 ('docs/legacy/SCC/gmmLT_SCC1 ', f'{G}/docs/legacy/SCC/gmmLT_SCC1.xml'),
 ('docs/legacy/SCC/gmmLT_SCC2 ', f'{G}/docs/legacy/SCC/gmmLT_SCC2.xml'),
 ('docs/legacy/SCC/gmmLT_SCC3 ', f'{G}/docs/legacy/SCC/gmmLT_SCC3.xml'),
 ('TRT/SCC/gmmLT_NBCC.xml     ', f'{G}/TRT/SCC/gmmLT_NBCC.xml'),
 ('TRT/ASC/gmmLT_NBCC.xml     ', f'{G}/TRT/ASC/gmmLT_NBCC.xml'),
 ('TRT/SIF/gmmLT_NBCC.xml     ', f'{G}/TRT/SIF/gmmLT_NBCC.xml'),
 ('TRT/SIS30/gmmLT_NBCC.xml   ', f'{G}/TRT/SIS30/gmmLT_NBCC.xml'),
 ('TRT/SIS55/gmmLT_NBCC.xml   ', f'{G}/TRT/SIS55/gmmLT_NBCC.xml'),
 ('TRT/ASC/gmmLT_ASC.xml      ', f'{G}/TRT/ASC/gmmLT_ASC.xml'),
 ('TRT/SCC/gmmLT_SCC.xml      ', f'{G}/TRT/SCC/gmmLT_SCC.xml'),
 ('current run gmmLT_GMM.xml  ', 'oq/.tmp.classical.M2V4D.CFD.180.nJu8R2/gmmLT_GMM.xml'),
]
for label, path in FILES:
    print('=' * 100); print(label, '->', path.replace(os.path.expanduser('~'), '~'))
    if not os.path.exists(path): print('   ABSENT'); continue
    root = ET.parse(path).getroot()
    for bs in root.iter('{%s}logicTreeBranchSet' % NS['n']):
        trt = bs.get('applyToTectonicRegionType')
        branches = bs.findall('n:logicTreeBranch', NS)
        models = collections.OrderedDict()
        for b in branches:
            um = b.find('n:uncertaintyModel', NS)
            name = um.text.strip().replace('\n', ' ')
            sub = um.get('submodel')
            key = f"{name}[{sub}]" if sub else name
            ws = b.findall('n:uncertaintyWeight', NS)
            w0 = [w for w in ws if w.get('imt') is None]
            w = float(w0[0].text) if w0 else float(ws[0].text)
            imtdep = any(w.get('imt') for w in ws)
            models[key] = (w, imtdep)
        tot = sum(v[0] for v in models.values())
        print(f"  TRT={trt:<10} branches={len(branches):3d}  sumW={tot:.4f}  imt-dependent={any(v[1] for v in models.values())}")
        for k, (w, dep) in models.items():
            print(f"      {w:7.4f}  {k[:95]}")
