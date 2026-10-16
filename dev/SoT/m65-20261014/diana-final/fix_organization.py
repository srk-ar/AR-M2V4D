"""Reconcile the organization paragraph with the restored Appendix E."""
from copy import deepcopy
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import hashlib
import json
from lxml import etree as E

Work = Path('/private/tmp/diana-final-20261016')
Source = Work/'delivery06/CAPR003324_Diana_R03.docx'
assert hashlib.sha256(Source.read_bytes()).hexdigest() == '7329245b1323d40a13a679e77032db28cfa7123a8a859a5dc2515de62951b0dc'
with ZipFile(Source) as FILE:
    Parts = {x:FILE.read(x) for x in FILE.namelist()}
Ns = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
W = '{'+Ns['w']+'}'
Xml = E.fromstring(Parts['word/document.xml'])
Body = Xml.find('w:body',Ns)
Before = [E.tostring(x) for x in Body]
for i in (370,382):
    Nodes = Body[i].xpath('.//w:t[contains(text(),"four appendices")]',namespaces=Ns)
    assert len(Nodes) == 1
    Nodes[0].text = Nodes[0].text.replace('four appendices','five appendices')
assert not Body[387].xpath('.//w:t',namespaces=Ns)
assert len(Body[387].xpath('.//w:br[@w:type="page"]',namespaces=Ns)) == 1
Props = deepcopy(Body[386].find('w:pPr',Ns))
for x in list(Props.xpath('.//w:ins',namespaces=Ns)):
    x.getparent().remove(x)
Body[387].replace(Body[387].find('w:pPr',Ns),Props)
Run = E.Element(W+'r')
E.SubElement(Run,W+'t').text = 'Appendix E presents the seismic coefficient formulations and results.'
Body[387].insert(1,Run)
assert [i for i,(a,b) in enumerate(zip(Before,Body)) if a != E.tostring(b)] == [370,382,387]
Parts['word/document.xml'] = E.tostring(Xml,xml_declaration=True,encoding='UTF-8',standalone=True)
Output = Work/'delivery07/CAPR003324_Diana_R03.docx'
Output.parent.mkdir(exist_ok=True)
assert not Output.exists()
with ZipFile(Output,'w',ZIP_DEFLATED) as FILE:
    for k,v in Parts.items(): FILE.writestr(k,v)
Record = {'output':str(Output),'sha256':hashlib.sha256(Output.read_bytes()).hexdigest(),'changedBodyBlocks':[370,382,387],'allOtherPartsAndBlocksUnchanged':True}
Path(__file__).with_name('candidate07.json').write_text(json.dumps(Record,indent=2)+'\n')
print(json.dumps(Record))
