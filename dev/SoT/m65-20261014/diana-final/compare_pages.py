"""Index exact page-body equality to reuse an already completed visual review."""
from pathlib import Path
import hashlib
import json
from PIL import Image

Root = Path('/private/tmp/diana-final-20261016')
Output = Path(__file__).parent/'page-coverage06.json'

def pageKey(path):
    with Image.open(path) as im:
        body = im.crop((0, 0, im.width, int(im.height * 0.92)))
        return hashlib.sha256(body.tobytes()).hexdigest()

def pages(path):
    return sorted(path.glob('page-*.png'), key=lambda p:int(p.stem.split('-')[1]))

Results = {}
for target, baseline in [('qa06','/private/tmp/diana-hazard-r02-qa04'),('qa-redline03',str(Root/'qa06'))]:
    index = {}
    for p in pages(Path(baseline)):
        index.setdefault(pageKey(p),[]).append(int(p.stem.split('-')[1]))
    matches = {}
    changed = []
    for p in pages(Root/target):
        n = int(p.stem.split('-')[1])
        key = pageKey(p)
        if key in index:
            matches[n] = index[key]
        else:
            changed.append(n)
    Results[target] = {'baseline':baseline,'crop':'top 92%, footer excluded','matches':matches,'changed':changed}
Output.write_text(json.dumps(Results,indent=2)+'\n')
print(json.dumps({k:{'matched':len(v['matches']),'changed':v['changed']} for k,v in Results.items()}))
