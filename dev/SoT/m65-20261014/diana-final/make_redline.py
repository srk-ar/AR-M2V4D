"""Record cumulative content changes as native Word revisions on a separate copy."""
from copy import deepcopy
from difflib import SequenceMatcher
import hashlib
import json
from pathlib import Path
import posixpath
import zipfile

from lxml import etree as E

Root = Path(__file__).resolve().parents[4]
Work = Path('/private/tmp/diana-final-20261016')
Ns = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
      'm':'http://schemas.openxmlformats.org/officeDocument/2006/math',
      'a':'http://schemas.openxmlformats.org/drawingml/2006/main',
      'r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
      'wp':'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'}
Author = 'Codex revision acumulativa'
Date = '2026-10-16T12:00:00Z'


def q(name):
    x,y = name.split(':')
    return '{'+Ns[x]+'}'+y


def unpack(path):
    with zipfile.ZipFile(path) as FILE:
        return {x:FILE.read(x) for x in FILE.namelist()}


def unwrap(node):
    Parent = node.getparent()
    i = Parent.index(node)
    for x in list(node): Parent.insert(i,x); i += 1
    Parent.remove(node)


def displayed(node):
    """Materialize the existing final view only in blocks being compared."""
    OUT = deepcopy(node)
    for x in list(OUT.xpath('.//w:del | .//w:moveFrom | .//w:pPrChange | .//w:rPrChange | .//w:tblPrChange | .//w:tcPrChange | .//w:trPrChange',namespaces=Ns)):
        if x.getparent() is not None: x.getparent().remove(x)
    for x in list(OUT.xpath('.//w:ins | .//w:moveTo',namespaces=Ns)):
        if x.getparent() is not None: unwrap(x)
    for x in list(OUT.xpath('.//w:customXmlDelRangeStart | .//w:customXmlDelRangeEnd | .//w:customXmlInsRangeStart | .//w:customXmlInsRangeEnd',namespaces=Ns)):
        x.getparent().remove(x)
    return OUT


def content(node, parts, relations):
    """Declared comparison endpoint: text, math, tabs/breaks and picture bytes."""
    OUT = []
    for x in node.iter():
        if any(y.tag in (q('w:del'),q('w:moveFrom')) for y in x.iterancestors()): continue
        if x.tag in (q('w:t'),q('m:t')): OUT.append((E.QName(x).localname,x.text or ''))
        elif x.tag in (q('w:tab'),q('w:br'),q('w:noBreakHyphen')): OUT.append((E.QName(x).localname,tuple(sorted(x.attrib.items()))))
        elif x.tag == q('a:blip'):
            s = x.get(q('r:embed'))
            if s: OUT.append(('image',hashlib.sha256(parts[posixpath.normpath('word/'+relations[s])]).hexdigest()))
    # Word's run boundaries are not visible text boundaries.
    LIST = []
    for k,v in OUT:
        if k in ('t',) and LIST and LIST[-1][0] == k: LIST[-1] = (k,LIST[-1][1]+v)
        else: LIST.append((k,v))
    return LIST


def inline(node):
    OUT = displayed(node)
    # A revision contains runs/math, never a hyperlink or content-control wrapper.
    for x in list(OUT.xpath('.//w:sdt',namespaces=Ns)):
        Parent = x.getparent(); i = Parent.index(x)
        for y in list(x.find('w:sdtContent',Ns)): Parent.insert(i,y); i += 1
        Parent.remove(x)
    for x in list(OUT.xpath('.//w:hyperlink | .//w:fldSimple',namespaces=Ns)): unwrap(x)
    for x in list(OUT.xpath('.//w:fldChar | .//w:instrText | .//w:delInstrText | .//w:bookmarkStart | .//w:bookmarkEnd | .//w:commentRangeStart | .//w:commentRangeEnd | .//w:proofErr',namespaces=Ns)):
        x.getparent().remove(x)
    return [x for x in OUT if x.tag in (q('w:r'),q('m:oMath'),q('m:oMathPara'))]


def signature(node):
    OUT = deepcopy(node)
    for x in OUT.iter():
        for k in list(x.attrib):
            if E.QName(k).localname.startswith('rsid'): del x.attrib[k]
    E.cleanup_namespaces(OUT)
    return E.tostring(OUT)


Original = unpack(Root/'docx/CAPR003324_Crawford_SeismicHazard_Final.docx')
Final = unpack(Work/'delivery07/CAPR003324_Diana_R03.docx')
Xml = {k:E.fromstring(v['word/document.xml']) for k,v in [('original',Original),('final',Final)]}
Bodies = {k:list(v.find('w:body',Ns)) for k,v in Xml.items()}
assert len(Bodies['original']) == len(Bodies['final'])
Relations = {k:{x.get('Id'):x.get('Target') for x in E.fromstring(v['word/_rels/document.xml.rels']) if x.get('TargetMode') != 'External'} for k,v in [('original',Original),('final',Final)]}
Parts = dict(Final)
Rels = E.fromstring(Parts['word/_rels/document.xml.rels'])
Document = deepcopy(Xml['final'])
Body = Document.find('w:body',Ns)
RevisionId = max(int(x) for x in Document.xpath('.//@w:id',namespaces=Ns) if x.lstrip('-').isdigit()) + 1
PictureId = max(int(x) for x in Document.xpath('.//wp:docPr/@id',namespaces=Ns)) + 1
Imports = {}
Changes = []


def revision(kind):
    global RevisionId
    OUT = E.Element(q('w:'+kind))
    OUT.set(q('w:id'),str(RevisionId)); RevisionId += 1
    OUT.set(q('w:author'),Author); OUT.set(q('w:date'),Date)
    return OUT


def importPictures(node):
    global PictureId
    for x in node.xpath('.//a:blip[@r:embed]',namespaces=Ns):
        s = x.get(q('r:embed'))
        if s not in Imports:
            Name = posixpath.normpath('word/'+Relations['original'][s])
            Target = 'media/original-'+s+'-'+Path(Name).name
            Id = 'rIdOriginal'+s
            Parts['word/'+Target] = Original[Name]
            E.SubElement(Rels,'{http://schemas.openxmlformats.org/package/2006/relationships}Relationship',Id=Id,Type='http://schemas.openxmlformats.org/officeDocument/2006/relationships/image',Target=Target)
            Imports[s] = Id
        x.set(q('r:embed'),Imports[s])
    for x in node.xpath('.//wp:docPr',namespaces=Ns): x.set('id',str(PictureId)); PictureId += 1


def markRuns(node, kind):
    OUT = revision(kind)
    for x in node:
        x = deepcopy(x)
        if kind == 'del':
            importPictures(x)
            for y in x.iter(q('w:t')): y.tag = q('w:delText')
        OUT.append(x)
    return OUT


def paragraphDiff(before, after):
    OUT = deepcopy(after)
    for x in list(OUT):
        if x.tag != q('w:pPr'): OUT.remove(x)
    for x in after:
        if x.tag in (q('w:bookmarkStart'),q('w:bookmarkEnd')): OUT.append(deepcopy(x))
    A = inline(before); B = inline(after)
    if not content(before,Original,Relations['original']) and content(after,Final,Relations['final']):
        Props = OUT.find('w:pPr',Ns)
        if Props is None: Props = E.Element(q('w:pPr')); OUT.insert(0,Props)
        RunProps = Props.find('w:rPr',Ns)
        if RunProps is None: RunProps = E.SubElement(Props,q('w:rPr'))
        RunProps.append(revision('ins'))
    for kind,i,j,a,b in SequenceMatcher(a=[signature(x) for x in A],b=[signature(x) for x in B],autojunk=False).get_opcodes():
        if kind == 'equal':
            # Equal XML can refer to replaced media. Compare their payloads too.
            for x,y in zip(A[i:j],B[a:b]):
                if content(x,Original,Relations['original']) != content(y,Final,Relations['final']):
                    OUT.append(markRuns([x],'del')); OUT.append(markRuns([y],'ins'))
                else: OUT.append(deepcopy(y))
        else:
            if i != j: OUT.append(markRuns(A[i:j],'del'))
            if a != b: OUT.append(markRuns(B[a:b],'ins'))
    return OUT


def markTable(table, kind):
    OUT = displayed(table)
    for Row in OUT.findall('w:tr',Ns):
        Props = Row.find('w:trPr',Ns)
        if Props is None: Props = E.Element(q('w:trPr')); Row.insert(0,Props)
        Props.append(revision(kind))
        for Para in Row.xpath('.//w:tc/w:p',namespaces=Ns):
            Runs = inline(Para)
            for x in list(Para):
                if x.tag != q('w:pPr'): Para.remove(x)
            Para.append(markRuns(Runs,kind))
    return OUT


def tableDiff(before, after):
    OUT = deepcopy(after)
    A = before.findall('w:tr',Ns); B = OUT.findall('w:tr',Ns)
    if [len(x.findall('w:tc',Ns)) for x in A] != [len(x.findall('w:tc',Ns)) for x in B]: return None
    for a,b in zip(A,B):
        for x,y in zip(a.findall('w:tc',Ns),b.findall('w:tc',Ns)):
            P = x.findall('w:p',Ns); Q = y.findall('w:p',Ns)
            if len(P) != len(Q): return None
            for p,r in zip(P,Q):
                if content(p,Original,Relations['original']) != content(r,Final,Relations['final']):
                    y.replace(r,paragraphDiff(p,r))
    return OUT


for i,(A,B) in enumerate(zip(Bodies['original'],Bodies['final'])):
    if B.tag == q('w:sectPr'): continue
    a = content(A,Original,Relations['original']); b = content(B,Final,Relations['final'])
    if a == b:
        continue
    Changes.append(i)

# Rebuild once, preserving input indices for tables that become two tracked tables.
for x in list(Body): Body.remove(x)
for i,(A,B) in enumerate(zip(Bodies['original'],Bodies['final'])):
    if i not in Changes:
        Body.append(deepcopy(B)); continue
    if B.tag == q('w:p'):
        Body.append(paragraphDiff(A,B))
    elif B.tag == q('w:tbl'):
        Table = tableDiff(A,B) if content(A,Original,Relations['original']) else None
        if Table is not None:
            Body.append(Table)
        else:
            if content(A,Original,Relations['original']): Body.append(markTable(A,'del'))
            Body.append(markTable(B,'ins'))
    else:
        raise ValueError(f'Unhandled changed block {i}: {B.tag}')

Settings = E.fromstring(Parts['word/settings.xml'])
if Settings.find('w:trackRevisions',Ns) is None: E.SubElement(Settings,q('w:trackRevisions'))
View = Settings.find('w:revisionView',Ns)
if View is None: View = E.SubElement(Settings,q('w:revisionView'))
for s in ['markup','insDel']: View.set(q('w:'+s),'1')
View.set(q('w:formatting'),'0')
for name,node in [('word/document.xml',Document),('word/settings.xml',Settings),('word/_rels/document.xml.rels',Rels)]:
    Parts[name] = E.tostring(node,xml_declaration=True,encoding='UTF-8',standalone=True)
Output = Work/'delivery07/CAPR003324_Diana_R03_Comparacion.docx'
assert not Output.exists()
with zipfile.ZipFile(Output,'w',zipfile.ZIP_DEFLATED) as FILE:
    for k,v in Parts.items(): FILE.writestr(k,v)
Record = {'output':str(Output),'sha256':hashlib.sha256(Output.read_bytes()).hexdigest(),'author':Author,'changedInputBlocks':Changes,'revisionCount':len(Document.xpath('.//w:ins[@w:author=$a] | .//w:del[@w:author=$a]',namespaces=Ns,a=Author)),'originalImageParts':len(Imports)}
Path(__file__).with_name('redline04.json').write_text(json.dumps(Record,indent=2)+'\n')
print(json.dumps(Record))
