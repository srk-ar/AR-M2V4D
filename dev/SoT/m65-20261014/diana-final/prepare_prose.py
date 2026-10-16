"""Bind the revised prose transcript to the public DOCX conversion for audit."""
from pathlib import Path
import json
import re

Root = Path(__file__).parent
Source = Path('/private/tmp/diana-final-20261016/parsed06/document.md')
Lines = Source.read_text().splitlines()
Blocks = []
Locations = []
for i,j in [(183,183),(1382,1382),(1467,1467),(2252,len(Lines))]:
    DATA = []
    k = i
    for n in range(i,j+2):
        s = Lines[n-1] if n <= j else ''
        if s.startswith(('+','|')): continue
        if not s.strip():
            if DATA:
                Blocks.append('\n'.join(DATA))
                Locations.append({'source':str(Source),'start':k,'end':n-1})
                DATA = []
        else:
            if not DATA: k = n
            if s.startswith('!['): s = s[2:s.index('](')]
            DATA.append(s)
assert Blocks[0].startswith('The Newmark')
assert '(Bray & Macedo, 2019)' in Blocks[1]
assert 'and the MCE' not in Blocks[2]
Root.joinpath('prose.md').write_text('\n\n'.join(Blocks)+'\n')
Root.joinpath('prose-locations.json').write_text(json.dumps(Locations,indent=2)+'\n')
print(json.dumps({'blocks':len(Blocks),'lines':len(Lines),'locations':len(Locations)}))
