"""Independently check numeric transfer, source integrity and redline endpoints."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import posixpath
import zipfile

from lxml import etree as E

Root = Path(__file__).resolve().parents[4]
Work = Path('/private/tmp/diana-final-20261016')
Ns = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','m':'http://schemas.openxmlformats.org/officeDocument/2006/math','a':'http://schemas.openxmlformats.org/drawingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
W = '{'+Ns['w']+'}'
Author = 'Codex revision acumulativa'


def read(path):
    with zipfile.ZipFile(path) as FILE:
        assert FILE.testzip() is None
        Parts = {x:FILE.read(x) for x in FILE.namelist()}
    Xml = E.fromstring(Parts['word/document.xml'])
    Relations = {x.get('Id'):posixpath.normpath('word/'+x.get('Target')) for x in E.fromstring(Parts['word/_rels/document.xml.rels']) if x.get('TargetMode') != 'External'}
    return Xml, Parts, Relations


def visible(node):
    return ''.join(node.xpath('.//w:t[not(ancestor::w:del)]/text() | .//m:t[not(ancestor::w:del)]/text()',namespaces=Ns))


def rows(node):
    return [[visible(z).strip() for z in y.findall('w:tc',Ns)] for y in node.findall('w:tr',Ns)]


def images(node, parts, relations):
    return [hashlib.sha256(parts[relations[x]]).hexdigest() for x in node.xpath('.//a:blip[not(ancestor::w:del)]/@r:embed',namespaces=Ns)]


def resolve(node, accept):
    OUT = deepcopy(node)
    # A table row's insertion/deletion applies to the whole row.
    for Row in list(OUT.xpath('.//w:tr',namespaces=Ns)):
        for x in Row.xpath('./w:trPr/w:ins | ./w:trPr/w:del',namespaces=Ns):
            if x.get(W+'author') == Author and ((x.tag == W+'ins') != accept):
                Row.getparent().remove(Row); break
    for x in list(OUT.xpath('.//w:ins | .//w:del',namespaces=Ns)):
        if x.get(W+'author') != Author or x.getparent() is None: continue
        Parent = x.getparent()
        if (x.tag == W+'ins') == accept:
            i = Parent.index(x)
            for y in list(x):
                if not accept:
                    for z in y.iter(W+'delText'): z.tag = W+'t'
                Parent.insert(i,y); i += 1
        Parent.remove(x)
    return OUT


Paths = {'original':Root/'docx/CAPR003324_Crawford_SeismicHazard_Final.docx',
         'avk':Root/'docx/diana-actualizado/CAPR003324_Crawford_SeismicHazard_Final_AVK.docx',
         'r02':Root/'docx/diana-actualizado/CAPR003324_Crawford_SeismicHazard_Final_AVK_R02.docx',
         'r03':Work/'delivery07/CAPR003324_Diana_R03.docx',
         'redline':Work/'delivery07/CAPR003324_Diana_R03_Comparacion.docx',
         'memo':Root/'docx/gmdp.memo.en.docx',
         'hazard':Root/'docx/hazard.diana.en.docx'}
Expected = {'original':'bec7b8068951a03e36aaf98274702c9a70b408363f5e2dc980ccd17cd53efa3d','avk':'69eee3e499fde36cba7886ec8504114d164cc8d4942725a9bc8b9560226cfdc8','r02':'86dd4a5e7631e1abc5db539176fdf0da118904690a86be77a03187bd501a180e'}
Hashes = {k:hashlib.sha256(v.read_bytes()).hexdigest() for k,v in Paths.items()}
for k,v in Expected.items(): assert Hashes[k] == v
Docs = {k:read(v) for k,v in Paths.items()}
B = {k:list(v[0].find('w:body',Ns)) for k,v in Docs.items()}
Results = {'hashes':Hashes,'originalsIntact':True,'hazardTables':[],'appendixTables':[]}
for i,j in [(667,47),(670,52),(689,57),(692,62),(957,67),(960,72),(963,77),(966,82),(970,87)]:
    A = rows(B['r03'][i])[2:]; C = rows(B['hazard'][j])[1:]
    assert A == C
    Results['hazardTables'].append({'bodyIndex':i,'source':j,'cells':sum(map(len,A))})
assert rows(B['r03'][754]) == rows(B['memo'][52])
assert rows(B['r03'][765]) == rows(B['r02'][765])
assert rows(B['r03'][993]) == rows(B['memo'][43])
for i,j in zip([1032,1036,1040,1044,1048,1054,1058,1062,1066,1070],[88,95,102,109,116,130,137,144,151,158]):
    A = rows(B['r03'][i]); C = rows(B['memo'][j]); C = C[:1] + [x for x in C[1:] if x[0].startswith('TR ')]
    assert A == C, i
    Results['appendixTables'].append({'bodyIndex':i,'source':j,'cells':sum(map(len,A)),'rows':len(A)-1})
Results['slopeImages'] = []
for i,j in zip([768,772,776,1019,1023,1027],[123,124,125,81,82,83]):
    A = images(B['r03'][i],*Docs['r03'][1:]); C = images(B['memo'][j],*Docs['memo'][1:]); assert A == C
    Results['slopeImages'].append({'bodyIndex':i,'source':j,'sha256':A[0]})
assert all(images(B['r03'][i],*Docs['r03'][1:]) == images(B['r02'][i],*Docs['r02'][1:]) for i in range(695))
assert all(images(B['r03'][i],*Docs['r03'][1:]) == images(B['r02'][i],*Docs['r02'][1:]) for i in range(780,989))
for i,j in zip([1000,1002,1004,1006,1010,1012,1014],[170,172,174,176,182,184,186]):
    A = ''.join(B['r03'][i].xpath('.//m:t/text()',namespaces=Ns)); C = ''.join(B['memo'][j].xpath('.//m:t/text()',namespaces=Ns)).replace('&','')
    assert A == C, i
assert 'MCE' not in ''.join(visible(x) for x in B['r03'][695:780]+B['r03'][990:1073])
Results['equationsExactIgnoringAlignmentTokens'] = 7
Results['scopePshaOnly'] = True
Results['endpoints'] = {}
for mode,accept,k in [('accepted',True,'r03'),('rejected',False,'original')]:
    Xml = resolve(Docs['redline'][0],accept)
    A = visible(Xml); C = visible(Docs[k][0])
    if A != C:
        n = next((i for i,(a,b) in enumerate(zip(A,C)) if a != b),min(len(A),len(C)))
        raise AssertionError((mode,n,A[n-100:n+200],C[n-100:n+200],len(A),len(C)))
    assert images(Xml,*Docs['redline'][1:]) == images(Docs[k][0],*Docs[k][1:]), mode
    Results['endpoints'][mode] = {'textExact':True,'imageOrderAndBytesExact':True,'characters':len(A),'images':len(images(Xml,*Docs['redline'][1:]))}
Revisions = Docs['redline'][0].xpath('.//w:ins[@w:author=$a] | .//w:del[@w:author=$a]',namespaces=Ns,a=Author)
Ids = [x.get(W+'id') for x in Revisions]
assert len(set(Ids)) == len(Ids)
assert not Docs['redline'][0].xpath('.//w:ins[@w:author=$a]//w:ins | .//w:del[@w:author=$a]//w:del',namespaces=Ns,a=Author)
Results['newRevisions'] = len(Ids)
Results['newRevisionIdsUnique'] = True
Path(__file__).with_name('verification07.json').write_text(json.dumps(Results,indent=2)+'\n')
print(json.dumps({'originalsIntact':True,'hazardCells':sum(x['cells'] for x in Results['hazardTables']),'appendixCells':sum(x['cells'] for x in Results['appendixTables']),'endpoints':Results['endpoints'],'revisions':len(Ids)},indent=2))
