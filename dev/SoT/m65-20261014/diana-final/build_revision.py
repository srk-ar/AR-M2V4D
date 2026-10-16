"""Create a separate cumulative Diana DOCX from the audited rendered sources."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
import zipfile

from lxml import etree as E

Root = Path(__file__).resolve().parents[4]
Work = Path('/private/tmp/diana-final-20261016')
Ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
      'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math',
      'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
      'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
      'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'}


def q(name):
    x, y = name.split(':')
    return '{' + Ns[x] + '}' + y


def textOf(node):
    return ''.join(node.xpath('.//w:t[not(ancestor::w:del)]/text() | .//m:t[not(ancestor::w:del)]/text()', namespaces=Ns))


def unwrap(node):
    Parent = node.getparent()
    i = Parent.index(node)
    for x in list(node):
        Parent.insert(i, x)
        i += 1
    Parent.remove(node)


def clean(node, restore=False):
    OUT = deepcopy(node)
    if restore:
        for x in list(OUT.xpath('.//w:pPrChange | .//w:rPrChange', namespaces=Ns)):
            Parent = x.getparent()
            Props = deepcopy(x[0])
            Parent.clear()
            for y in Props:
                Parent.append(y)
    for x in list(OUT.iter()):
        if x.getparent() is None:
            continue
        s = E.QName(x).localname
        if s in ('pPrChange', 'rPrChange', 'tblPrChange', 'trPrChange', 'tcPrChange', 'sectPrChange'):
            x.getparent().remove(x)
        elif x.tag in (q('w:del'), q('w:moveFrom')):
            if restore:
                unwrap(x)
            else:
                x.getparent().remove(x)
        elif x.tag in (q('w:ins'), q('w:moveTo')):
            unwrap(x)
    for x in OUT.iter(q('w:delText')):
        x.tag = q('w:t')
    return OUT


def replaceText(node, before, after):
    """Replace literal text spanning Word runs without disturbing adjacent math."""
    Runs = node.xpath('.//w:t', namespaces=Ns)
    s = ''.join(x.text or '' for x in Runs)
    assert before in s, (before, s[:200])
    while before in s:
        i = s.index(before)
        j = i + len(before)
        n = 0
        for x in Runs:
            t = x.text or ''
            if n < j and n + len(t) > i:
                x.text = t[:max(0, i-n)] + (after if n <= i < n+len(t) else '') + t[max(0, j-n):]
                x.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
            n += len(t)
        s = ''.join(x.text or '' for x in Runs)


def plainParagraph(template, value):
    OUT = clean(template)
    for x in list(OUT):
        if x.tag != q('w:pPr'):
            OUT.remove(x)
    x = E.SubElement(E.SubElement(OUT, q('w:r')), q('w:t'))
    x.text = value
    x.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    return OUT


def putContent(target, source):
    for x in list(target):
        if x.tag != q('w:pPr'):
            target.remove(x)
    for x in source:
        if x.tag != q('w:pPr'):
            target.append(deepcopy(x))


def tableRows(node):
    return [[textOf(y).strip() for y in x.findall('w:tc', Ns)] for x in node.findall('w:tr', Ns)]


def setCell(cell, source):
    for x in list(cell):
        if x.tag != q('w:tcPr'):
            cell.remove(x)
    for x in source:
        if x.tag != q('w:tcPr'):
            cell.append(deepcopy(x))


def importTable(template, source):
    OUT = clean(template, restore=True)
    Rows = source.findall('w:tr', Ns)
    Rows = [Rows[0]] + [x for x in Rows[1:] if textOf(x.findall('w:tc', Ns)[0]).startswith('TR ')]
    assert len(Rows) == len(OUT.findall('w:tr', Ns))
    for x, y in zip(OUT.findall('w:tr', Ns), Rows):
        assert len(x.findall('w:tc', Ns)) == len(y.findall('w:tc', Ns))
        for a, b in zip(x.findall('w:tc', Ns), y.findall('w:tc', Ns)):
            setCell(a, b)
    return OUT


def xmlBytes(node):
    return E.tostring(node, xml_declaration=True, encoding='UTF-8', standalone=True)


Paths = {'r02': Root/'docx/diana-actualizado/CAPR003324_Crawford_SeismicHazard_Final_AVK_R02.docx',
         'memo': Root/'docx/gmdp.memo.en.docx', 'report': Root/'docx/docx.en.docx'}
Expected = {'r02': '86dd4a5e7631e1abc5db539176fdf0da118904690a86be77a03187bd501a180e',
            'memo': '9812e23c42a59a5be3738723e8e1e06684f2aa84287870c3f06472a03c92a329',
            'report': '7b1096f0f6223b024f3b2c2a3dd9af50835743fdfa1154848fe447a94418c760'}
Parts = {}
Documents = {}
for k, v in Paths.items():
    assert hashlib.sha256(v.read_bytes()).hexdigest() == Expected[k]
    with zipfile.ZipFile(v) as FILE:
        Parts[k] = {x: FILE.read(x) for x in FILE.namelist()}
    Documents[k] = E.fromstring(Parts[k]['word/document.xml'])
Body = Documents['r02'].find('w:body', Ns)
Before = list(Body)
Memo = list(Documents['memo'].find('w:body', Ns))
Report = list(Documents['report'].find('w:body', Ns))
Changes = []


def replaceBlock(index, node, source):
    Body.replace(Body[index], node)
    Changes.append({'bodyIndex': index, 'source': source, 'text': textOf(node)})


# The summary borrows the existing NGR paragraph, including its native math.
Summary = next(x for x in Report if 'Newmark Permanent Displacements.' in textOf(x) and '300 realizations' in textOf(x))
Summary = clean(Summary)
replaceText(Summary, 'Newmark Permanent Displacements. ', '')
Summary.find('w:pPr', Ns).clear()
for x in clean(Before[28]).find('w:pPr', Ns):
    Summary.find('w:pPr', Ns).append(deepcopy(x))
replaceBlock(28, Summary, 'docx.en.docx: executive Newmark paragraph; method and simulated realizations retained exactly')

# Keep the already approved probabilistic scope; remove the unused MCE branch.
Scope = clean(Before[740])
replaceText(Scope, ' years and the MCE.', ' years.')
replaceBlock(740, Scope, 'owner PSHA-only decision; existing chapter 10 magnitude allocation retained')

# Restore the existing appendix wording and structure, not its obsolete numbers.
for i in range(990, 1073):
    replaceBlock(i, clean(Before[i], restore=True), 'Diana Appendix E wording restored from deleted content')
for i in [991,995]:
    Props = Body[i].find('w:pPr',Ns)
    x = Props.find('w:pStyle',Ns)
    if x is None: x = E.SubElement(Props,q('w:pStyle'))
    x.set(q('w:val'),'BodyText')

# Copy the source stiffness table (its formulation identifiers replace obsolete columns).
Stiffness = clean(Memo[43])
replaceBlock(993, Stiffness, 'gmdp.memo.en.docx: body 43, full table')

# Native Word equations from the rendered memo. Remove literal TeX alignment tokens only.
for i, j in zip([1000,1002,1004,1006,1010,1012,1014], [170,172,174,176,182,184,186]):
    Formula = clean(Body[i])
    for x in list(Formula):
        if x.tag != q('w:pPr'):
            Formula.remove(x)
    for x in Memo[j]:
        if x.tag in (q('m:oMath'), q('m:oMathPara')):
            Formula.append(deepcopy(x))
    for x in Formula.xpath('.//m:t[text()="&"]', namespaces=Ns):
        x.getparent().remove(x)
    x = E.SubElement(E.SubElement(Formula, q('w:r')), q('w:t'))
    x.text = '  (E1-' + str([1000,1002,1004,1006,1010,1012,1014].index(i)+1) + ')'
    replaceBlock(i, Formula, f'gmdp.memo.en.docx: body {j}; equation label adapted, alignment tokens removed')

TableMap = dict(zip([1032,1036,1040,1044,1048,1054,1058,1062,1066,1070], [88,95,102,109,116,130,137,144,151,158]))
for i, j in TableMap.items():
    replaceBlock(i, importTable(Before[i], Memo[j]), f'gmdp.memo.en.docx: body {j}, header and all TR rows; MCE rows excluded')

# Deduplicate the existing citation displays without changing their citation identity.
for i in [999,1001,1003,1009,1011,1013]:
    Nodes = Body[i].xpath('.//w:t', namespaces=Ns)
    s = ''.join(x.text or '' for x in Nodes)
    m = re.search(r'(\([^)]*\))(\([^)]*\))', s)
    if m:
        replaceText(Body[i], m.group(0), m.group(1))

# Unlink only the restored appendix's stale field codes; retain its displayed labels.
for Node in list(Body)[990:1073]:
    for x in list(Node.xpath('.//w:fldChar | .//w:instrText | .//w:delInstrText',namespaces=Ns)):
        x.getparent().remove(x)
    for x in list(Node.xpath('.//w:fldSimple',namespaces=Ns)):
        unwrap(x)
    if Node.tag == q('w:p'):
        s = ''.join(Node.xpath('.//w:t/text()',namespaces=Ns))
        for m in re.finditer(r'((?:Table|Figure) (?:E\d\d|102))\1',s):
            replaceText(Node,m.group(0),m.group(1))
        for s in ['E11','E12','E13','E14','E15','E16','E17','E21','E22','E23','E24','E25','E31','E32','E33','E34','E35']:
            if s in ''.join(Node.xpath('.//w:t/text()',namespaces=Ns)):
                replaceText(Node,s,s[:2]+'-'+s[2:])

# The deleted footnote duplicates the AM88 limit explained in E1-4 and its prose.
# Remove its dangling marker; retain that complete explanation in the appendix.
for x in Body[999].xpath('.//w:footnoteReference',namespaces=Ns): x.getparent().remove(x)
for Node in list(Body)[990:1073]:
    for x in Node.xpath('.//w:noBreakHyphen',namespaces=Ns): x.getparent().remove(x)

# The numerical TR labels in restored captions come from the source tables.
Labels = [x[0] for x in tableRows(Memo[88])[1:] if x[1] == 'ensemble' and x[0].startswith('TR ')]
LabelMap = {'475': re.search(r'TR (.*?) yr', Labels[0]).group(1),
            '2,475': re.search(r'TR (.*?) yr', Labels[1]).group(1)}
for i in range(990,1073):
    if Body[i].tag == q('w:p'):
        for x in Body[i].xpath('.//w:t | .//m:t', namespaces=Ns):
            if x.text:
                x.text = re.sub(r'(?<![\d,])(2,475|475)(?!\d)', lambda m: LabelMap[m.group(1)], x.text)

# Appendix headings do not inherit chapter numbering or vertical centering.
for i, value in {990:'Appendix E Seismic Coefficients',996:'E1 Newmark Permanent-Displacement Formulations',1017:'E2 Seismic Coefficient in Acceleration Units',1051:'E3 Seismic Coefficient as a Percentage of PGA'}.items():
    Node = plainParagraph(Body[i], value)
    Props = Node.find('w:pPr', Ns)
    for x in list(Props):
        Props.remove(x)
    E.SubElement(Props, q('w:pStyle')).set(q('w:val'), 'Heading1' if i == 990 else 'Heading2')
    E.SubElement(E.SubElement(Props, q('w:numPr')), q('w:numId')).set(q('w:val'), '0')
    E.SubElement(Props, q('w:pageBreakBefore'))
    if i == 990:
        x = E.SubElement(Node, q('w:bookmarkStart')); x.set(q('w:id'),'24000'); x.set(q('w:name'),'appendix-e')
        E.SubElement(Node, q('w:bookmarkEnd')).set(q('w:id'),'24000')
    replaceBlock(i, Node, 'Diana existing appendix headings; explicit numbering for restored section')
for i in [995,1073]:
    for x in Body[i].xpath('.//w:vAlign', namespaces=Ns):
        x.set(q('w:val'), 'top')
    if Body[i].tag == q('w:sectPr'):
        x = Body[i].find('w:vAlign', Ns)
        if x is not None: x.set(q('w:val'),'top')

# Correct the appendix reference display, preserving the source prose around it.
for i in range(695,780):
    if 'Appendix E' in textOf(Body[i]):
        Node = clean(Body[i])
        for x in Node.xpath('.//w:hyperlink', namespaces=Ns):
            if 'Appendix E' in textOf(x):
                x.set(q('w:anchor'),'appendix-e')
                for y in list(x): x.remove(y)
                E.SubElement(E.SubElement(x,q('w:r')),q('w:t')).text = 'Appendix E'
        # Word fields not inside hyperlinks retain their reference identity.
        replaceBlock(i, Node, 'restore live reference to Appendix E')

# Chapter 10's saved equation and reference displays are correct; its legacy
# STYLEREF/SEQ fields recalculate to chapter titles or missing appendix numbers.
# Retain those reviewed displays instead of these broken field instructions.
for i in range(695,780):
    Node = clean(Body[i])
    for x in list(Node.xpath('.//w:fldChar | .//w:instrText | .//w:delInstrText',namespaces=Ns)):
        x.getparent().remove(x)
    for x in list(Node.xpath('.//w:fldSimple',namespaces=Ns)): unwrap(x)
    if Node.tag == q('w:p'):
        s = ''.join(Node.xpath('.//w:t/text()',namespaces=Ns))
        if '11Appendix E' in s: replaceText(Node,'11Appendix E','Appendix E')
        s = ''.join(Node.xpath('.//w:t/text()',namespaces=Ns))
        for m in list(re.finditer(r'(\([^()]+\))\1',s)):
            if m.group(0) in ''.join(Node.xpath('.//w:t/text()',namespaces=Ns)):
                replaceText(Node,m.group(0),m.group(1))
    replaceBlock(i, Node, 'chapter 10 saved equation and cross-reference labels retained; duplicate identical citation displays removed')

# Pictures use the exact bytes of the current rendered memo.
MemoRels = {x.get('Id'): x.get('Target') for x in E.fromstring(Parts['memo']['word/_rels/document.xml.rels'])}
Rels = {x.get('Id'): x.get('Target') for x in E.fromstring(Parts['r02']['word/_rels/document.xml.rels'])}
Media = []
for i, j in zip([768,772,776,1019,1023,1027], [123,124,125,81,82,83]):
    a = Body[i].xpath('.//a:blip', namespaces=Ns)[0].get(q('r:embed'))
    b = Memo[j].xpath('.//a:blip', namespaces=Ns)[0].get(q('r:embed'))
    Target = 'word/' + Rels[a]
    Source = 'word/' + MemoRels[b]
    Parts['r02'][Target] = Parts['memo'][Source]
    Media.append({'bodyIndex':i, 'target':Target, 'source':Source, 'sha256':hashlib.sha256(Parts['memo'][Source]).hexdigest()})

# Make imported tables fit Diana's printable width and repeat their headers.
for i in [993, *TableMap]:
    Table = Body[i]
    Grid = Table.find('w:tblGrid',Ns)
    if i == 993:
        assert Grid is None
        Grid = E.Element(q('w:tblGrid'))
        Table.insert(1, Grid)
        for n in [1200,850,2300,2250,920,920,920]:
            E.SubElement(Grid,q('w:gridCol')).set(q('w:w'),str(n))
    Widths = [int(x.get(q('w:w'))) for x in Grid]
    Width = 9360 if i == 993 else 8640
    Widths = [round(x*Width/sum(Widths)) for x in Widths]
    Widths[-1] += Width-sum(Widths)
    for x,n in zip(Grid,Widths): x.set(q('w:w'),str(n))
    for Row in Table.findall('w:tr',Ns):
        Props = Row.find('w:trPr',Ns)
        if Props is None: Props = E.SubElement(Row,q('w:trPr'))
        for x in list(Props):
            if x.tag == q('w:trHeight'): Props.remove(x)
        E.SubElement(Props,q('w:cantSplit'))
        for Cell,n in zip(Row.findall('w:tc',Ns),Widths):
            PropsCell = Cell.find('w:tcPr',Ns)
            x = PropsCell.find('w:tcW',Ns)
            if x is None: x = E.SubElement(PropsCell,q('w:tcW'))
            x.set(q('w:w'),str(n)); x.set(q('w:type'),'dxa')
    for x in Table.xpath('.//w:rPr/w:sz | .//w:rPr/w:szCs',namespaces=Ns): x.set(q('w:val'),'17')
    Props = Table.find('w:tblPr',Ns)
    for x in Props.findall('w:tblW',Ns): x.set(q('w:w'),str(Width)); x.set(q('w:type'),'dxa')
    Props = Table.findall('w:tr',Ns)[0].find('w:trPr',Ns)
    E.SubElement(Props,q('w:tblHeader'))

# Freeze content for review. Unrelated XML parts and scientific data stay intact.
Parts['r02']['word/document.xml'] = xmlBytes(Documents['r02'])
Settings = E.fromstring(Parts['r02']['word/settings.xml'])
for x in Settings.findall('w:revisionView',Ns):
    x.set(q('w:markup'),'0'); x.set(q('w:insDel'),'0'); x.set(q('w:formatting'),'0')
Parts['r02']['word/settings.xml'] = xmlBytes(Settings)
Output = Work/'R03-candidate04.docx'
assert not Output.exists()
with zipfile.ZipFile(Output,'w',zipfile.ZIP_DEFLATED) as FILE:
    for k,v in Parts['r02'].items(): FILE.writestr(k,v)
Record = {'output':str(Output),'sha256':hashlib.sha256(Output.read_bytes()).hexdigest(),'changes':Changes,'media':Media,'sourceHashes':Expected}
Path(__file__).with_name('candidate04.json').write_text(json.dumps(Record,indent=2)+'\n')
print(json.dumps({k:Record[k] for k in ['output','sha256']}))
