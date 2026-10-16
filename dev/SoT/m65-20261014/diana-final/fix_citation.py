"""Correct the BM19 reference using the rendered memo and existing bibliography."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import hashlib
import json
from lxml import etree as E

Work = Path('/private/tmp/diana-final-20261016')
Source = Work/'delivery/CAPR003324_Diana_R03.docx'
assert hashlib.sha256(Source.read_bytes()).hexdigest() == '0883fc9824318119bfc207a38d5f0ec5e9c077ef31d81b4e468d1f3e45bd5073'
with ZipFile(Source) as FILE:
    Parts = {x:FILE.read(x) for x in FILE.namelist()}
Ns = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
Xml = E.fromstring(Parts['word/document.xml'])
Body = Xml.find('w:body',Ns)
Nodes = Body[697].xpath('.//w:t[text()="(Bray, Macedo, & Travasauro, 2018)"]',namespaces=Ns)
assert len(Nodes) == 1
Nodes[0].text = '(Bray & Macedo, 2019)'
Parts['word/document.xml'] = E.tostring(Xml,xml_declaration=True,encoding='UTF-8',standalone=True)
Output = Work/'delivery06/CAPR003324_Diana_R03.docx'
Output.parent.mkdir(exist_ok=True)
assert not Output.exists()
with ZipFile(Output,'w',ZIP_DEFLATED) as FILE:
    for k,v in Parts.items(): FILE.writestr(k,v)
with ZipFile(Source) as FILE:
    assert all(v == FILE.read(k) for k,v in Parts.items() if k != 'word/document.xml')
    Before = FILE.read('word/document.xml')
    Xml = E.fromstring(Before)
    Nodes = Xml.find('w:body',Ns)[697].xpath('.//w:t[text()="(Bray, Macedo, & Travasauro, 2018)"]',namespaces=Ns)
    Nodes[0].text = '(Bray & Macedo, 2019)'
    assert Parts['word/document.xml'] == E.tostring(Xml,xml_declaration=True,encoding='UTF-8',standalone=True)
Record = {'output':str(Output),'sha256':hashlib.sha256(Output.read_bytes()).hexdigest(),'change':'body697: BM19 citation -> Bray & Macedo, 2019; all other XML and parts unchanged'}
Path(__file__).with_name('candidate06.json').write_text(json.dumps(Record,indent=2)+'\n')
print(json.dumps(Record))
