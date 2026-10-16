"""Independently check numeric transfer, source integrity and redline endpoints."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import posixpath
import zipfile

from lxml import etree as E

Root = Path(__file__).resolve().parents[4]
Work = Path('/private/tmp/diana-editorial-20261016')
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
         'final':Work/'delivery02/CAPR003324_Diana_R04.docx',
         'redline':Work/'delivery02/CAPR003324_Diana_R04_Comparacion.docx'}
Docs = {k:read(v) for k,v in Paths.items()}
Results = {'endpoints':{}}
for accept,k in [(True,'final'),(False,'original')]:
    Xml = resolve(Docs['redline'][0],accept)
    A = visible(Xml); B = visible(Docs[k][0])
    if A != B:
        n = next((i for i,(a,b) in enumerate(zip(A,B)) if a != b),min(len(A),len(B)))
        raise AssertionError((k,n,A[n-100:n+200],B[n-100:n+200],len(A),len(B)))
    assert images(Xml,*Docs['redline'][1:]) == images(Docs[k][0],*Docs[k][1:])
    Results['endpoints'][k] = {'textAndMathExact':True,'imageOrderAndBytesExact':True,'characters':len(A)}
Ids = Docs['redline'][0].xpath('.//w:ins[@w:author=$a]/@w:id | .//w:del[@w:author=$a]/@w:id',namespaces=Ns,a=Author)
assert len(Ids) == len(set(Ids))
Results['revisions'] = len(Ids)
Results['hashes'] = {k:hashlib.sha256(v.read_bytes()).hexdigest() for k,v in Paths.items()}
Path(__file__).with_name('redline-verification.json').write_text(json.dumps(Results,indent=2)+'\n')
print(json.dumps(Results))


