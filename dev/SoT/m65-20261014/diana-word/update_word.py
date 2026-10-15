"""Copy the existing NGR results into Diana's two tables and three figures."""

from hashlib import sha256
from html import escape
import json
from pathlib import Path
import re
from zipfile import ZipFile

from lxml import etree, html


Root = Path(__file__).resolve().parents[4]
Folder = Path(__file__).resolve().parent
Original = Root / "docx/CAPR003324_Crawford_SeismicHazard_Final.docx"
Memo = Path("/private/tmp/diana-word.K8hYBK/memo-source.docx")
Hydrated = Path("/private/tmp/diana-coefficients-plan.GxJs0p/memo-current.md")
Output = Folder / Original.name
Namespaces = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
Changes = []


def readText(node):
    return "".join(node.xpath(".//w:t/text()", namespaces=Namespaces))


def parseFragment(fragment):
    return etree.fromstring(
        ('<root xmlns:w="' + Namespaces["w"] + '">' + fragment + "</root>").encode(),
        parser=etree.XMLParser(recover=True),
    )[0]


def replaceCell(fragment, value):
    # Accept only superseded revisions inside this updated numerical cell.
    fragment = re.sub(r"<w:del\b[^>]*>.*?</w:del>", "", fragment, flags=re.S)
    fragment = re.sub(r"</?w:ins\b[^>]*>", "", fragment)
    Texts = list(re.finditer(r"(<w:t\b[^>]*>)(.*?)(</w:t>)", fragment, flags=re.S))
    assert Texts
    for i, v in reversed(list(enumerate(Texts))):
        s = escape(value, quote=False) if i == 0 else ""
        fragment = fragment[:v.start(2)] + s + fragment[v.end(2):]
    return fragment


def replaceTable(fragment, rows, label, startColumn):
    Rows = list(re.finditer(r"<w:tr\b[^>]*>.*?</w:tr>", fragment, flags=re.S))
    assert len(Rows) == len(rows) + 1
    for i in range(len(rows) - 1, -1, -1):
        v = Rows[i + 1]
        s = v.group()
        Cells = list(re.finditer(r"<w:tc\b[^>]*>.*?</w:tc>", s, flags=re.S))
        assert len(Cells) == len(rows[i])
        for j in range(len(Cells) - 1, startColumn - 1, -1):
            x = Cells[j]
            Before = readText(parseFragment(x.group()))
            After = rows[i][j]
            if Before == After:
                continue
            Changes.append({"table": label, "row": i + 1, "column": j + 1,
                            "before": Before, "after": After})
            s = s[:x.start()] + replaceCell(x.group(), After) + s[x.end():]
        fragment = fragment[:v.start()] + s + fragment[v.end():]
    return fragment


assert not Output.exists(), "Refusing to replace an existing candidate"
assert sha256(Original.read_bytes()).hexdigest() == "bec7b8068951a03e36aaf98274702c9a70b408363f5e2dc980ccd17cd53efa3d"
assert sha256(Memo.read_bytes()).hexdigest() == "c861b12bbfe331c32175c280078d565c810c6906a471421d6bc57f43eba701f6"
Text = Hydrated.read_text()
Tables = html.fromstring(Text).xpath("//table")
Periods = [v for v in Tables if "Fundamental periods" in v.xpath("string(caption)")]
assert len(Periods) == 1
Periods = [[c.text_content().strip() for c in v.xpath("td")] for v in Periods[0].xpath("tbody/tr")]
assert len(Periods) == 5 and all(len(v) == 12 for v in Periods)

Coefficients = {}
for v in re.finditer(r"(?P<grid>\+[-+]+\+\n\| > \*\*ID\*\*(?:(?!\n: Table).)*?)\n(?P<caption>: Table\xa0\d+: Mean values of \$k_\{h\}\$.*?scenario (?P<scenario>S\d+),[^\n]*)", Text, flags=re.S):
    Rows = [s for s in v["grid"].splitlines() if s.startswith("| > TR") and "| > ensemble" in s]
    for s in Rows:
        Cells = [x.strip().removeprefix(">").strip() for x in s.strip("|").split("|")]
        Demand = int(re.fullmatch(r"TR ([\d,]+) yr", Cells[0])[1].replace(",", ""))
        Coefficients[(v["scenario"], Demand)] = Cells[2:]
assert len(Coefficients) == len(Periods) * 3

with ZipFile(Original) as Archive, ZipFile(Memo) as Source:
    Document = Archive.read("word/document.xml").decode()
    Tables = list(re.finditer(r"<w:tbl\b[^>]*>.*?</w:tbl>", Document, flags=re.S))
    Targets = {}
    for v in Tables:
        Header = parseFragment(v.group()).find("w:tr", Namespaces)
        Cells = Header.findall("w:tc", Namespaces)
        if len(Cells) == 12 and readText(Cells[0]) == "IDm":
            assert "periods" not in Targets
            Targets["periods"] = v
        if len(Cells) == 8 and readText(Cells[0]) == "Scenario":
            assert "coefficients" not in Targets
            Targets["coefficients"] = v
    assert set(Targets) == {"periods", "coefficients"}
    TargetRows = parseFragment(Targets["periods"].group()).findall("w:tr", Namespaces)[1:]
    assert [readText(v.findall("w:tc", Namespaces)[0]) for v in TargetRows] == [v[0] for v in Periods]
    Rows = []
    for v in parseFragment(Targets["coefficients"].group()).findall("w:tr", Namespaces)[1:]:
        Cells = [readText(c) for c in v.findall("w:tc", Namespaces)]
        Demand = int(Cells[1].split(":")[1].replace(",", ""))
        Demand = {2475: 2500}.get(Demand, Demand)
        Rows.append(Cells[:2] + Coefficients[(Cells[0], Demand)])
    assert len(Rows) == 10
    Replacements = [
        (Targets["periods"], replaceTable(Targets["periods"].group(), Periods, "10-1", 2)),
        (Targets["coefficients"], replaceTable(Targets["coefficients"].group(), Rows, "10-2", 2)),
    ]
    for v, s in sorted(Replacements, key=lambda x: x[0].start(), reverse=True):
        Document = Document[:v.start()] + s + Document[v.end():]
    etree.fromstring(Document.encode())
    Images = {"word/media/image41.png": "word/media/rId61.png",
              "word/media/image42.png": "word/media/rId66.png",
              "word/media/image43.png": "word/media/rId71.png"}
    with ZipFile(Output, "w") as Candidate:
        for v in Archive.infolist():
            DATA = Archive.read(v.filename)
            if v.filename == "word/document.xml":
                DATA = Document.encode()
            elif v.filename in Images:
                DATA = Source.read(Images[v.filename])
            Candidate.writestr(v, DATA)

with ZipFile(Original) as Archive, ZipFile(Output) as Candidate:
    assert Archive.namelist() == Candidate.namelist()
    ChangedParts = [v for v in Archive.namelist() if Archive.read(v) != Candidate.read(v)]
    assert set(ChangedParts) == {"word/document.xml", *Images}
    Before = etree.fromstring(Archive.read("word/document.xml"))
    After = etree.fromstring(Candidate.read("word/document.xml"))
    for x in (Before, After):
        for v in x.findall(".//w:tbl", Namespaces):
            Cells = v.find("w:tr", Namespaces).findall("w:tc", Namespaces)
            if readText(Cells[0]) in ("IDm", "Scenario"):
                v.getparent().remove(v)
    assert etree.tostring(Before) == etree.tostring(After), "Content outside the two tables changed"

(Folder / "changes.json").write_text(json.dumps({
    "original": str(Original), "source": str(Memo), "candidate": str(Output),
    "sourceSha256": sha256(Memo.read_bytes()).hexdigest(),
    "originalSha256": sha256(Original.read_bytes()).hexdigest(),
    "candidateSha256": sha256(Output.read_bytes()).hexdigest(),
    "changedParts": ChangedParts, "cells": sorted(Changes, key=lambda x: (x["table"], x["row"], x["column"])),
    "figures": Images, "allOtherPackagePartsIdentical": True,
    "documentOutsideTargetTablesIdentical": True,
}, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"output": str(Output), "changedCells": len(Changes), "changedParts": ChangedParts}))
