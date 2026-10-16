"""Inspect field targets and visible captions before the editorial Word patch."""
import json
from pathlib import Path
import re
import zipfile

from lxml import etree as E

Root = Path(__file__).resolve().parents[4]
Source = Root / 'docx/diana-actualizado/CAPR003324_Diana_R03.docx'
Ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
      'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math'}
W = '{' + Ns['w'] + '}'
with zipfile.ZipFile(Source) as FILE:
    Xml = E.fromstring(FILE.read('word/document.xml'))
    Styles = E.fromstring(FILE.read('word/styles.xml'))
    Names = FILE.namelist()
    Bibliography = {x: FILE.read(x).decode('utf-8') for x in Names
                    if x.startswith('customXml/item') and x.endswith('.xml')
                    and b'bibliography' in FILE.read(x)}


def visible(node):
    return ''.join(node.xpath('.//w:t[not(ancestor::w:del)]/text() | .//m:t[not(ancestor::w:del)]/text()', namespaces=Ns))


Body = list(Xml.find('w:body', Ns))
Paragraphs = Xml.xpath('.//w:p', namespaces=Ns)
Positions = {x: i for i, x in enumerate(Paragraphs)}
Bookmarks = {}
for x in Xml.xpath('.//w:bookmarkStart', namespaces=Ns):
    LIST = list(x.iterancestors(W + 'p'))
    if LIST:
        Bookmarks[x.get(W + 'name')] = {'paragraph': Positions[LIST[0]], 'text': visible(LIST[0])}
Fields = []
Blocks = []
for i, x in enumerate(Body):
    LIST = [x] if x.tag == W + 'p' else x.xpath('.//w:p', namespaces=Ns)
    for y in LIST:
        s = visible(y)
        t = ''.join(y.xpath('./w:pPr/w:pStyle/@w:val', namespaces=Ns))
        if s and (re.match(r'^(Table|Figure|Appendix|[A-E][1-3] )', s) or 'Heading' in t or 'Caption' in t or 'caption' in t or 'Bibliography' in t):
            Blocks.append({'body': i, 'paragraph': Positions[y], 'style': t, 'text': s})
        for z in y.xpath('.//w:instrText[not(ancestor::w:del)] | .//w:fldSimple[not(ancestor::w:del)]', namespaces=Ns):
            s = (z.text or '') if z.tag == W + 'instrText' else z.get(W + 'instr')
            OUT = {'body': i, 'paragraph': Positions[y], 'instruction': s, 'text': visible(y)}
            if re.match(r'\s*(REF|PAGEREF)\s', s or ''):
                OUT['target'] = Bookmarks.get(s.split()[1])
            Fields.append(OUT)
Output = {'fields': Fields, 'blocks': Blocks, 'bookmarks': Bookmarks,
          'styleNumbering': [{'id': x.get(W + 'styleId'), 'xml': E.tostring(x, encoding='unicode')}
                             for x in Styles if x.xpath('.//w:numPr', namespaces=Ns)]}
Path(__file__).with_name('inventory.json').write_text(json.dumps(Output, indent=2, ensure_ascii=False) + '\n')
Path(__file__).with_name('bibliography.xml').write_text('\n'.join(Bibliography.values()))
print(json.dumps({'fields': len(Fields), 'blocks': len(Blocks), 'bookmarks': len(Bookmarks),
                  'brokenTargets': [x for x in Fields if 'target' in x and x['target'] is None]}, ensure_ascii=False, indent=2))
