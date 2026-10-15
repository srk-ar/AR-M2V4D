"""Apply the owner's bounded technical corrections to the preserved Word copy."""

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import re
from zipfile import ZipFile

from lxml import etree


Folder = Path(__file__).resolve().parent
Root = Path(__file__).resolve().parents[4]
Baseline = Folder / "tablas-figuras.baseline.docx"
Output = Folder / "CAPR003324_Crawford_SeismicHazard_Final.docx"
Memo = Path("/private/tmp/diana-word.K8hYBK/memo-updated.docx")
Namespaces = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
              "m": "http://schemas.openxmlformats.org/officeDocument/2006/math"}
ContractA = json.loads((Root / "newmark-M55.json").read_text())
ContractB = json.loads((Root / "newmark-M65.json").read_text())
MagnitudeA = str(ContractA["Mw.gmdp"])
MagnitudeB = str(ContractB["Mw.gmdp"])
assert (Folder / "corrections.md").read_bytes() == (Folder / "corrections.delivered.md").read_bytes()
Verdict = json.loads((Folder / "corrections.verdict.json").read_text())
assert Verdict["status"] == "ready"
assert Output.read_bytes() == Baseline.read_bytes() or sha256(Output.read_bytes()).hexdigest() == "031ef6aa25e52133338cdc348c0b65b79e9f9823dd49c9dc8d72fe49e4529588", "Only an owned checked candidate may be replaced"


def textOf(node):
    return "".join(node.xpath(".//w:t/text()|.//m:t/text()", namespaces=Namespaces))


def oneNode(nodes, predicate):
    LIST = [v for v in nodes if predicate(v)]
    assert len(LIST) == 1, f"Expected one target, found {len(LIST)}"
    return LIST[0]


def textRun(template, text):
    OUT = deepcopy(template)
    for v in list(OUT):
        if v.tag != "{" + Namespaces["w"] + "}rPr":
            OUT.remove(v)
    v = etree.SubElement(OUT, "{" + Namespaces["w"] + "}t")
    v.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    v.text = text
    return OUT


with ZipFile(Baseline) as Archive, ZipFile(Memo) as Source:
    Document = Archive.read("word/document.xml").decode()
    Tree = etree.fromstring(Document.encode())
    MemoTree = etree.fromstring(Source.read("word/document.xml"))
    FormulaTs = oneNode(MemoTree.findall(".//m:oMath", Namespaces),
                        lambda v: textOf(v).startswith("Ts=4") and v.find("m:f", Namespaces) is not None)
    FormulaH = oneNode(MemoTree.findall(".//m:oMath", Namespaces),
                       lambda v: textOf(v).startswith("H=Hs/") and len(textOf(v)) < 30)
    FormulaKh = oneNode(MemoTree.findall(".//m:oMath", Namespaces),
                        lambda v: textOf(v).startswith("kh=100") and v.find("m:f", Namespaces) is not None)
    assert "4πHs" not in textOf(FormulaTs)
    MemoIntro = oneNode(MemoTree.findall(".//w:p", Namespaces),
                        lambda v: "estimated fundamental period varies between" in textOf(v))
    PeriodRange = re.search(r"estimated fundamental period varies between ([\d.]+) and ([\d.]+) s", textOf(MemoIntro)).groups()
    Paragraphs = []
    Starts = []
    for v in re.finditer(r"</?w:p(?:\s[^>]*)?/?>", Document):
        if v.group().endswith("/>"):
            continue
        if v.group().startswith("</"):
            Paragraphs.append((Starts.pop(), v.end()))
        else:
            Starts.append(v.start())
    assert not Starts
    Paragraphs.sort()
    Changed = []
    for i, v in enumerate(Paragraphs):
        Wrapper = "<root " + " ".join('xmlns' + (":" + k if k else "") + '="' + s + '"' for k, s in Tree.nsmap.items()) + ">"
        p = etree.fromstring((Wrapper + Document[v[0]:v[1]] + "</root>").encode())[0]
        s = textOf(p)
        Kind = None
        if "estimated fundamental period varies between" in s:
            t = oneNode(p.findall(".//w:t", Namespaces), lambda x: "estimated fundamental period varies between" in (x.text or ""))
            t.text, n = re.subn(r"estimated fundamental period varies between [\d.]+ and [\d.]+ s", "estimated fundamental period varies between " + PeriodRange[0] + " and " + PeriodRange[1] + " s", t.text)
            assert n == 1
            Kind = "period-range"
        elif "with the reference magnitude" in s:
            t = oneNode(p.findall(".//w:t", Namespaces), lambda x: "with the reference magnitude" in (x.text or ""))
            t.text = t.text.replace("with the reference magnitude", "with reference magnitudes")
            t = oneNode(p.findall(".//w:t", Namespaces), lambda x: " = 7.0 and 300 realizations per demand" == x.text)
            r = t.getparent()
            Math = deepcopy(r.getprevious())
            assert textOf(Math) == "Mw"
            t.text = " = " + MagnitudeA + " and "
            j = p.index(r)
            p.insert(j + 1, Math)
            p.insert(j + 2, textRun(r, " = " + MagnitudeB + " assigned according to the seismic demand and 300 realizations per demand"))
            Kind = "magnitude-summary"
        elif "is applied as a constant input to every demand" in s:
            t = oneNode(p.findall(".//w:t", Namespaces), lambda x: "reference magnitude of the project" in (x.text or ""))
            t.text = t.text.replace("reference magnitude of the project, ", "reference magnitude is ")
            t = oneNode(p.findall(".//w:t", Namespaces), lambda x: "is applied as a constant input to every demand" in (x.text or ""))
            r = t.getparent()
            Math = deepcopy(r.getprevious())
            assert textOf(Math) == "Mw="
            Tail = t.text.split(" The published form", 1)[1]
            t.text = " " + MagnitudeA + " for return periods up to 2,500 years and "
            j = p.index(r)
            p.insert(j + 1, Math)
            p.insert(j + 2, textRun(r, " " + MagnitudeB + " for return periods of 5,000 and 10,000 years and the MCE. Within each demand, that magnitude is common to the geometry, material and site combinations evaluated. The published form" + Tail))
            Kind = "magnitude-demands"
        elif "The height from the virtual apex" in s:
            Math = oneNode(p.findall("m:oMath", Namespaces), lambda x: x.find("m:f", Namespaces) is not None)
            Replacement = deepcopy(FormulaH)
            r = etree.SubElement(Replacement, "{" + Namespaces["m"] + "}r")
            etree.SubElement(r, "{" + Namespaces["m"] + "}t").text = "."
            t = oneNode(p.findall(".//w:t", Namespaces), lambda x: (x.text or "").startswith("The modal root depends"))
            t.text = " " + t.text
            p.replace(Math, Replacement)
            Kind = "apex-definition"
        elif s.startswith("Ts=4πHs"):
            Math = oneNode(p.findall("m:oMath", Namespaces), lambda x: textOf(x).startswith("Ts="))
            p.replace(Math, deepcopy(FormulaTs))
            Kind = "period-equation"
        elif s.startswith("kh=kmaxPGA(VS30)"):
            Math = oneNode(p.findall("m:oMath", Namespaces), lambda x: textOf(x).startswith("kh="))
            p.replace(Math, deepcopy(FormulaKh))
            Kind = "percentage-equation"
        if Kind is None:
            continue
        s = etree.tostring(p, encoding="unicode")
        for k, x in Tree.nsmap.items():
            s = s.replace(' xmlns' + (":" + k if k else "") + '="' + x + '"', "")
        Changed.append({"kind": Kind, "paragraph": i, "start": v[0], "end": v[1], "xml": s})
    assert len(Changed) == 6 and len({v["kind"] for v in Changed}) == 6
    for v in reversed(Changed):
        Document = Document[:v["start"]] + v["xml"] + Document[v["end"]:]
    etree.fromstring(Document.encode())
    Candidate = Folder / "complete.candidate.docx"
    assert not Candidate.exists()
    with ZipFile(Candidate, "w") as Target:
        for v in Archive.infolist():
            Target.writestr(v, Document.encode() if v.filename == "word/document.xml" else Archive.read(v.filename))

with ZipFile(Baseline) as Archive, ZipFile(Candidate) as Target:
    assert Archive.namelist() == Target.namelist()
    assert [v for v in Archive.namelist() if Archive.read(v) != Target.read(v)] == ["word/document.xml"]
    Before = etree.fromstring(Archive.read("word/document.xml"))
    After = etree.fromstring(Target.read("word/document.xml"))
    Before = Before.findall(".//w:p", Namespaces)
    After = After.findall(".//w:p", Namespaces)
    assert len(Before) == len(After)
    ChangedParagraphs = [i for i, (x, y) in enumerate(zip(Before, After)) if etree.tostring(x) != etree.tostring(y)]
    assert len(ChangedParagraphs) == 6
    assert all("Slope Design Parameters" not in textOf(v) for v in (Before[i] for i in ChangedParagraphs))
    Check = {"baselineSha256": sha256(Baseline.read_bytes()).hexdigest(),
             "memoSha256": sha256(Memo.read_bytes()).hexdigest(),
             "candidateSha256": sha256(Candidate.read_bytes()).hexdigest(),
             "changedParagraphs": ChangedParagraphs,
             "corrections": [{k: v[k] for k in ("kind", "paragraph")} for v in Changed],
             "allOtherPackagePartsIdentical": True,
             "allOtherParagraphsIdentical": True,
             "periodRangeFromMemo": PeriodRange}
    (Folder / "technical-check.json").write_text(json.dumps(Check, indent=2) + "\n")
Candidate.replace(Output)
print(json.dumps(Check))
