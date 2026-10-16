"""Copy only calculated PAGEREF display values from the isolated QA roundtrip."""
from pathlib import Path
import json
import zipfile
from lxml import etree as E

Work = Path('/private/tmp/diana-editorial-20261016')
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


def fields(node):
    Stack = []; OUT = {}
    for x in node.iter():
        if x.tag == W+'fldChar':
            k = x.get(W+'fldCharType')
            if k == 'begin': Stack.append({'code':'','text':[],'result':False})
            elif k == 'separate': Stack[-1]['result'] = True
            elif k == 'end':
                f = Stack.pop(); s = f['code'].split()
                if s and s[0] == 'PAGEREF' and s[1].startswith('R04'): OUT[s[1]] = f['text']
        elif x.tag == W+'instrText' and Stack: Stack[-1]['code'] += x.text or ''
        elif x.tag == W+'t' and Stack and Stack[-1]['result']: Stack[-1]['text'].append(x)
    return OUT


with zipfile.ZipFile(Work/'candidate06/CAPR003324_Diana_R04.docx') as FILE:
    Parts = {x:FILE.read(x) for x in FILE.namelist()}
with zipfile.ZipFile(Work/'fields06/CAPR003324_Diana_R04.docx') as FILE:
    Cached = fields(E.fromstring(FILE.read('word/document.xml')))
Xml = E.fromstring(Parts['word/document.xml']); Original = fields(Xml)
assert set(Original) == set(Cached) and len(Original) == 192
Values = {}
for k,Nodes in Original.items():
    s = ''.join(x.text or '' for x in Cached[k])
    assert s and s != '0' and 'Error' not in s, (k,s)
    Nodes[0].text = s
    for x in Nodes[1:]: x.text = ''
    Values[k] = s
Parts['word/document.xml'] = E.tostring(Xml,xml_declaration=True,encoding='UTF-8',standalone=True)
Output = Work/'delivery02/CAPR003324_Diana_R04.docx'; Output.parent.mkdir(exist_ok=True)
assert not Output.exists()
with zipfile.ZipFile(Output,'w',zipfile.ZIP_DEFLATED) as FILE:
    for k,v in Parts.items(): FILE.writestr(k,v)
Path(__file__).with_name('page-cache.json').write_text(json.dumps(Values,indent=2)+'\n')
print(json.dumps({'output':str(Output),'pageReferences':len(Values)}))
