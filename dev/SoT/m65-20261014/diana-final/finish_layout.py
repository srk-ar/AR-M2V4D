"""Remove observed layout residues in a separate cumulative Word candidate."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import hashlib
import json
from lxml import etree as E

Work = Path('/private/tmp/diana-final-20261016')
Source = Work/'R03-candidate04.docx'
assert hashlib.sha256(Source.read_bytes()).hexdigest() == '2fe1d686e0f506781b847c14568bb7838f88bcbf24a3597fd175b851c9cdfec1'
with ZipFile(Source) as FILE:
    Parts = {x:FILE.read(x) for x in FILE.namelist()}
Ns = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','m':'http://schemas.openxmlformats.org/officeDocument/2006/math'}
Xml = E.fromstring(Parts['word/document.xml'])
Body = Xml.find('w:body',Ns)
Changes = []
for i in range(695,780):
    for x in Body[i].xpath('.//m:oMath',namespaces=Ns):
        if not ''.join(x.xpath('.//m:t/text()',namespaces=Ns)).strip():
            x.getparent().remove(x)
            Changes.append({'bodyIndex':i,'change':'remove empty equation placeholder'})
for i,a,b in [(992,'Table E','Table E-'),(1052,'Table 102','Table 10-2')]:
    x = Body[i].xpath('.//w:t[text()=$a]',namespaces=Ns,a=a)
    if i == 992:
        x = Body[i].xpath('.//w:t[text()="E"]',namespaces=Ns)
        a,b = 'E','E-'
    assert len(x) == 1
    x[0].text = b
    Changes.append({'bodyIndex':i,'change':a+' -> '+b})
for i in [1000,1002,1004,1006,1010,1012,1014]:
    x = Body[i].xpath('./w:r/w:t[starts-with(text(),"  (E1-")]',namespaces=Ns)
    assert len(x) == 1
    x[0].set('{http://www.w3.org/XML/1998/namespace}space','preserve')
for i in [1056,1060,1064,1068,1072]:
    x = Body[i].xpath('.//m:oMath[starts-with(string(.),"100")]//m:t[text()=","]',namespaces=Ns)
    assert len(x) == 1
    x[0].getparent().remove(x[0])
    Changes.append({'bodyIndex':i,'change':'remove comma between 100 and kmax; memo equation 14 defines multiplication'})
Parts['word/document.xml'] = E.tostring(Xml,xml_declaration=True,encoding='UTF-8',standalone=True)
Output = Work/'delivery/CAPR003324_Diana_R03.docx'
Output.parent.mkdir(exist_ok=True)
assert not Output.exists()
with ZipFile(Output,'w',ZIP_DEFLATED) as FILE:
    for k,v in Parts.items(): FILE.writestr(k,v)
Record = {'output':str(Output),'sha256':hashlib.sha256(Output.read_bytes()).hexdigest(),'changes':Changes}
Path(__file__).with_name('candidate05.json').write_text(json.dumps(Record,indent=2)+'\n')
print(json.dumps(Record))
