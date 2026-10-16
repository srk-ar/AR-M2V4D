"""Read-only comparison of the six owner-selected DOCX deliveries."""
import collections
import hashlib
import json
import posixpath
import zipfile
from decimal import Decimal
from pathlib import Path

from lxml import etree

Root = Path(__file__).resolve().parents[4]
Ns = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
}
Paths = {
    'original': 'docx/CAPR003324_Crawford_SeismicHazard_Final.docx',
    'avk': 'docx/diana-actualizado/CAPR003324_Crawford_SeismicHazard_Final_AVK.docx',
    'r02': 'docx/diana-actualizado/CAPR003324_Crawford_SeismicHazard_Final_AVK_R02.docx',
    'report': 'docx/docx.en.docx',
    'memo': 'docx/gmdp.memo.en.docx',
    'hazard': 'docx/hazard.diana.en.docx',
}


def visibleText(node):
    return ''.join(node.xpath('.//w:t[not(ancestor::w:del)]/text() | .//m:t[not(ancestor::w:del)]/text()', namespaces=Ns))


def canonical(node):
    return etree.tostring(node, method='c14n')


def readDocument(path):
    with path.open('rb') as FILE:
        Digest = hashlib.file_digest(FILE, 'sha256').hexdigest()
    with zipfile.ZipFile(path) as FILE:
        Xml = etree.fromstring(FILE.read('word/document.xml'))
        Body = list(Xml.find('w:body', Ns))
        Relations = {x.get('Id'): posixpath.normpath('word/' + x.get('Target')) for x in etree.fromstring(FILE.read('word/_rels/document.xml.rels')) if x.get('TargetMode') != 'External'}
        Images = [(i, Relations[y.get('{'+Ns['r']+'}embed')], hashlib.sha256(FILE.read(Relations[y.get('{'+Ns['r']+'}embed')])).hexdigest()) for i, x in enumerate(Body) for y in x.xpath('.//a:blip', namespaces=Ns)]
        Revisions = {(etree.QName(x).localname, x.get('{'+Ns['w']+'}id'), x.get('{'+Ns['w']+'}author')): canonical(x) for x in Xml.xpath('.//w:ins | .//w:del', namespaces=Ns)}
        Tables = {i: [[visibleText(z).strip() for z in y.findall('w:tc', Ns)] for y in x.findall('w:tr', Ns)] for i, x in enumerate(Body) if x.tag == '{'+Ns['w']+'}tbl'}
        Parts = {x.filename: (x.CRC, x.file_size) for x in FILE.infolist()}
    return {'identity': {'path': str(path), 'sha256': Digest, 'bytes': path.stat().st_size}, 'body': Body, 'tables': Tables, 'images': Images, 'revisions': Revisions, 'parts': Parts}


Documents = {k: readDocument(Root / v) for k, v in Paths.items()}
OUT = {'identities': {k: v['identity'] for k, v in Documents.items()}, 'bodyIndexBase': 0, 'numericReturnPeriod': 2500, 'stages': {}}
for x, y in [('original', 'avk'), ('avk', 'r02')]:
    A, B = Documents[x], Documents[y]
    assert len(A['body']) == len(B['body'])
    assert [i[0] for i in A['images']] == [i[0] for i in B['images']]
    Changed = [i for i, (a, b) in enumerate(zip(A['body'], B['body'])) if canonical(a) != canonical(b)]
    OUT['stages'][x+'-'+y] = {
        'changedBodyIndices': Changed,
        'changedParagraphs': [{'bodyIndex': i, 'before': visibleText(A['body'][i]), 'after': visibleText(B['body'][i])} for i in Changed if B['body'][i].tag == '{'+Ns['w']+'}p' and visibleText(B['body'][i])],
        'changedImages': [{'bodyIndex': b[0], 'before': a[1], 'after': b[1], 'sha256': b[2]} for a, b in zip(A['images'], B['images']) if a[2] != b[2]],
        'newInsDel': len(B['revisions'].keys() - A['revisions'].keys()),
        'removedInsDel': dict(collections.Counter(k[0] for k in A['revisions'].keys() - B['revisions'].keys())),
        'changedRemainingInsDel': sum(A['revisions'][k] != B['revisions'][k] for k in A['revisions'].keys() & B['revisions'].keys()),
        'changedZipParts': [k for k in sorted(A['parts'].keys() | B['parts'].keys()) if A['parts'].get(k) != B['parts'].get(k)],
    }
OUT['chapter10'] = {
    'start': 695, 'endExclusive': 780,
    'bodyExact': all(canonical(a) == canonical(b) for a, b in zip(Documents['avk']['body'][695:780], Documents['r02']['body'][695:780])),
    'imagesExact': [x for x in Documents['avk']['images'] if 695 <= x[0] < 780] == [x for x in Documents['r02']['images'] if 695 <= x[0] < 780],
}
Tables = {k: v['tables'] for k, v in Documents.items()}
OUT['table10_1'] = {'matchesMemoIncludingHeaders': Tables['avk'][754] == Tables['memo'][52], 'cellsIncludingHeaders': 72}
OUT['table10_2'] = []
for i, a in enumerate(Tables['avk'][765][1:], start=1):
    Demand = {'1:2,475': 'TR 2,500 yr', '1:10,000': 'TR 10,000 yr'}[a[1]]
    Source = next(x for x in Tables['memo'][{'S135':130, 'S50':137, 'S32':144, 'S27':151, 'S35':158}[a[0]]][1:] if x[:2] == [Demand, 'ensemble'])
    OUT['table10_2'].append({'scenario': a[0], 'modelDemand': Demand, 'dianaLabel': a[1], 'columns': ['Ts','Vs30','0.1%','0.4%','1%','2.5%'], 'original': Tables['original'][765][i][2:], 'avk': a[2:], 'r02': Tables['r02'][765][i][2:], 'source': Source[2:], 'exact': a[2:] == Source[2:] == Tables['r02'][765][i][2:]})
OUT['hazardTables'] = []
for i, j, label in [(667,47,'9-1'),(670,52,'9-2'),(689,57,'9-3'),(692,62,'9-4'),(957,67,'D1-1'),(960,72,'D1-2'),(963,77,'D1-3'),(966,82,'D1-4'),(970,87,'D1-5')]:
    A, B = Tables['r02'][i][2:], Tables['hazard'][j][1:]
    OUT['hazardTables'].append({'label':label, 'r02BodyIndex':i, 'sourceBodyIndex':j, 'cells':sum(map(len,A)), 'accelerations':sum(len(a)-1 for a in A), 'exact':A == B, 'headersPreserved':Tables['original'][i][:2] == Tables['r02'][i][:2]})
OUT['hazardImages'] = [{'target': x['after'], 'matchingSources': [y[1] for y in Documents['hazard']['images'] if y[2] == x['sha256']]} for x in OUT['stages']['avk-r02']['changedImages']]
OUT['fullReportCommonPga1500'] = []
for tr, label in [('500','475'),('1000','975'),('2500','2,475'),('5000','5,000'),('10000','10,000'),('MDE (84%)','10,000')]:
    A = next(a[-1] for a in Tables['report'][313][1:] if a[0].replace(',','') == tr)
    B = next(a[1] for a in Tables['r02'][670 if tr == 'MDE (84%)' else 667][2:] if a[0] == label)
    OUT['fullReportCommonPga1500'].append({'modelDemand':tr, 'statistic':'P84' if tr == 'MDE (84%)' else 'mean', 'Vs30':1500, 'units':'g', 'report':A, 'r02':B, 'equalAtReportPrecision':Decimal(A) == Decimal(B).quantize(Decimal('0.001'))})
OUT['fullReportCommonGeometry'] = {'IDm':'U2', 'Hs':50, 'reportRow':Tables['report'][459][2], 'dianaRow':Tables['r02'][754][2], 'exact':Tables['report'][459][2] == Tables['r02'][754][2]}
OUT['appendixE'] = {'start':989, 'endExclusive':1074, 'exactOriginalR02':all(canonical(a) == canonical(b) for a,b in zip(Documents['original']['body'][989:1074], Documents['r02']['body'][989:1074])), 'visibleTextCharacters':sum(len(visibleText(a)) for a in Documents['r02']['body'][989:1074]), 'deletedTextCharacters':sum(len(t) for a in Documents['r02']['body'][989:1074] for t in a.xpath('.//w:delText/text()', namespaces=Ns))}
assert all(OUT['chapter10'][k] for k in ['bodyExact','imagesExact'])
assert OUT['table10_1']['matchesMemoIncludingHeaders']
assert all(x['exact'] for x in OUT['table10_2'] + OUT['hazardTables'])
assert len(OUT['hazardImages']) == 77 and all(len(x['matchingSources']) == 1 for x in OUT['hazardImages'])
assert all(x['equalAtReportPrecision'] for x in OUT['fullReportCommonPga1500'])
assert OUT['fullReportCommonGeometry']['exact']
Path(__file__).with_name('verification.json').write_text(json.dumps(OUT, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'chapter10':OUT['chapter10'], 'coefficientRows':len(OUT['table10_2']), 'hazardTables':len(OUT['hazardTables']), 'hazardCells':sum(x['cells'] for x in OUT['hazardTables']), 'hazardAccelerations':sum(x['accelerations'] for x in OUT['hazardTables']), 'hazardImages':len(OUT['hazardImages']), 'fullReportCommonPga1500':OUT['fullReportCommonPga1500'], 'appendixE':OUT['appendixE']}, indent=2))
