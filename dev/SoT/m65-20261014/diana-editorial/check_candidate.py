"""Compare R04 scientific content directly with the immutable R03 delivery."""
import hashlib
import json
from pathlib import Path
import re
import zipfile
from lxml import etree as E

Root = Path(__file__).resolve().parents[4]
Work = Path('/private/tmp/diana-editorial-20261016')
Ns = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
      'm':'http://schemas.openxmlformats.org/officeDocument/2006/math',
      'a':'http://schemas.openxmlformats.org/drawingml/2006/main',
      'r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
W = '{'+Ns['w']+'}'
Paths = [Root/'docx/diana-actualizado/CAPR003324_Diana_R03.docx',
         Work/'delivery02/CAPR003324_Diana_R04.docx']
Parts = []
for p in Paths:
    with zipfile.ZipFile(p) as FILE:
        assert FILE.testzip() is None
        Parts.append({x:FILE.read(x) for x in FILE.namelist()})
Docs = [E.fromstring(x['word/document.xml']) for x in Parts]
Bodies = [list(x.find('w:body',Ns)) for x in Docs]


def visible(node):
    return ''.join(node.xpath('.//w:t[not(ancestor::w:del)]/text() | .//m:t[not(ancestor::w:del)]/text()',namespaces=Ns))


def math(node):
    return [x.text for x in node.xpath('.//m:t[not(ancestor::w:del)]',namespaces=Ns) if x.text]


assert len(Bodies[0]) == len(Bodies[1])
assert all(Parts[0][k] == Parts[1][k] for k in Parts[0] if k.startswith('word/media/'))
assert Docs[0].xpath('.//a:blip[not(ancestor::w:del)]/@r:embed',namespaces=Ns) == Docs[1].xpath('.//a:blip/@r:embed',namespaces=Ns)
Tables = []; Diff = []; MathCount = 0
for i,(a,b) in enumerate(zip(*Bodies)):
    if i >= 342:
        assert math(a) == math(b), ('math',i)
        MathCount += len(math(a))
    if b.tag == W+'tbl':
        x = [visible(z) for z in a.xpath('.//w:tc',namespaces=Ns)]
        y = [visible(z) for z in b.xpath('.//w:tc',namespaces=Ns)]
        x = [z.replace('CAPR003324_Crawford_SeismicHazard_Final.docx','CAPR003324_Diana_R04.docx')
               .replace('(Atkinson & Adams, Ground motion prediction equations for application to the 2015 Canadian national seismic hazard maps, 2013)','(Atkinson & Adams, 2013)')
               .replace('(Goulet, et al., 2017)','(Goulet et al., 2017)') for z in x]
        assert x == y, ('table cells',i)
        Tables.append({'body':i,'cells':len(y)})
    if visible(a) != visible(b) and i >= 342:
        if b.tag == W+'sdt':
            continue
        Diff.append({'body':i,'before':visible(a),'after':visible(b)})
Names = set(Docs[1].xpath('.//w:bookmarkStart/@w:name',namespaces=Ns))
Links = Docs[1].xpath('.//w:hyperlink/@w:anchor',namespaces=Ns)
Missing = [x for x in Links if x not in Names]
assert not Missing, Missing
assert 'Error! Reference source not found.' not in visible(Docs[1])
assert '11Appendix' not in visible(Docs[1])
Record = {'sourceSha256':hashlib.sha256(Paths[0].read_bytes()).hexdigest(),
          'candidateSha256':hashlib.sha256(Paths[1].read_bytes()).hexdigest(),
          'tables':Tables,'mathTokens':MathCount,'imagePartsUnchanged':True,
          'imageOrderUnchanged':True,'links':len(Links),'missingLinks':Missing,'changes':Diff}
Path(__file__).with_name('verification-final.json').write_text(json.dumps(Record,indent=2,ensure_ascii=False)+'\n')
Path(__file__).with_name('text-diff-final.md').write_text('\n\n'.join('Body '+str(x['body'])+'\nBEFORE: '+x['before']+'\nAFTER: '+x['after'] for x in Diff)+'\n')
print(json.dumps({k:v for k,v in Record.items() if k not in ('changes','tables')}))
