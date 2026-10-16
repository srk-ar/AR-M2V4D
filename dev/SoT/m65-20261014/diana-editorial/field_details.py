"""Read complete nested Word fields and their cached display, without edits."""
import json
from pathlib import Path
import zipfile
from lxml import etree as E

Ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
      'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math'}
W = '{' + Ns['w'] + '}'
Root = Path(__file__).resolve().parents[4]
with zipfile.ZipFile(Root/'docx/diana-actualizado/CAPR003324_Diana_R03.docx') as FILE:
    Xml = E.fromstring(FILE.read('word/document.xml'))
Body = list(Xml.find('w:body', Ns))
Positions = {x: i for i, x in enumerate(Body)}
Stack = []
Fields = []
for x in Xml.iter():
    if any(y.tag == W+'del' for y in x.iterancestors()):
        continue
    if x.tag == W+'fldChar':
        t = x.get(W+'fldCharType')
        if t == 'begin':
            p = next(y for y in x.iterancestors() if y.getparent() == Xml.find('w:body', Ns))
            Stack.append({'body': Positions[p], 'instruction': '', 'display': '', 'result': False})
        elif t == 'separate' and Stack:
            Stack[-1]['result'] = True
        elif t == 'end' and Stack:
            Fields.append(Stack.pop())
    elif x.tag == W+'instrText' and Stack:
        Stack[-1]['instruction'] += x.text or ''
    elif x.tag in (W+'t', W+'noBreakHyphen', W+'tab'):
        s = {W+'noBreakHyphen': '-', W+'tab': '\t'}.get(x.tag, x.text or '')
        for y in Stack:
            if y['result']:
                y['display'] += s
assert not Stack
Path(__file__).with_name('fields.json').write_text(json.dumps(Fields, ensure_ascii=False, indent=2)+'\n')
for x in Fields:
    if x['instruction'].strip().split()[0] in ['REF', 'CITATION']:
        print(x['body'], x['instruction'], '=>', x['display'])
