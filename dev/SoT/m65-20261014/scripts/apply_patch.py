"""Apply the owner-approved sentence replacements of docx-review/B/PATCH.md
to the project sources. Each block names a file and gives the exact current
sentence (Actual) and the approved sentence (Propuesta); a block is applied
only when the current sentence occurs exactly once in the file. Usage:
python3 apply_patch.py PATCH.md [--apply]   (without --apply: report only)."""
import re, sys, pathlib
PATCH = pathlib.Path(sys.argv[1]); APPLY = '--apply' in sys.argv
Text = PATCH.read_text(encoding='utf-8')
Blocks = re.findall(r'^### (B\d+) · `([^:`]+):(\d+)`[^\n]*\n\nActual:\n\n```text\n(.*?)\n```\n\nPropuesta:\n\n```text\n(.*?)\n```', Text, flags=re.S | re.M)
print('blocks parsed:', len(Blocks))
Pending = {}
for bid, path, line, old, new in Blocks:
    Pending.setdefault(path, []).append((bid, int(line), old, new))
Applied = 0; Failed = []
for path, items in Pending.items():
    P = pathlib.Path(path); s = P.read_text(encoding='utf-8'); n0 = s
    for bid, line, old, new in items:
        c = s.count(old)
        if c != 1:
            Failed.append((bid, path, line, c)); continue
        if old == new:
            Failed.append((bid, path, line, 'identical')); continue
        s = s.replace(old, new, 1); Applied += 1
        print(f'{bid:5s} {path}:{line}  ok')
    if APPLY and s != n0:
        P.write_text(s, encoding='utf-8')
print('applied' if APPLY else 'applicable', Applied, '| not applied', len(Failed))
for f in Failed: print('  NOT APPLIED', f)
