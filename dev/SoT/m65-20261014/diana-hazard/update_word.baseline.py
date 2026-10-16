"""Transfer the audited NGR objects into a new copy of Diana's accepted Word."""

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import re
from zipfile import ZipFile
from lxml import etree

Root = Path(__file__).resolve().parents[4]
Folder = Path(__file__).resolve().parent
Layout = json.loads((Root / "_local/hazard.diana.json").read_text())
Original = Root / Layout["source"]
Transfer = Root / "docx/hazard.diana.en.docx"
Output = Folder / "CAPR003324_Crawford_SeismicHazard_AVK_R02_candidate01.docx"
NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
    "mc": "http://schemas.openxmlformats.org/markup-compatibility/2006",
}
Changes = []

def readText(node):
    return "".join(node.xpath(".//w:t/text()", namespaces=NS))

def replaceText(node, before, after):
    Texts = node.xpath(".//w:t", namespaces=NS)
    Text = "".join(x.text or "" for x in Texts)
    assert Text.count(before) == 1, (before, Text)
    a = Text.index(before)
    b = a + len(before)
    n = 0
    for x in Texts:
        s = x.text or ""
        if n < b and n + len(s) > a:
            x.text = s[:max(a-n, 0)] + (after if n <= a else "") + s[max(b-n, 0):]
            x.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        n += len(s)
    assert readText(node) == Text[:a] + after + Text[b:]
    Changes.append(dict(kind="text", before=before, after=after))

def replaceCell(node, value):
    Before = readText(node)
    for x in node.xpath(".//w:del", namespaces=NS):
        x.getparent().remove(x)
    for x in node.xpath(".//w:ins", namespaces=NS):
        Parent = x.getparent()
        n = Parent.index(x)
        for i, v in enumerate(list(x)):
            Parent.insert(n+i, deepcopy(v))
        Parent.remove(x)
    Texts = node.xpath(".//w:t", namespaces=NS)
    assert Texts and not node.xpath(".//m:oMath", namespaces=NS)
    Texts[0].text = value
    for x in Texts[1:]:
        x.text = ""
    assert readText(node) == value
    return Before

assert not Output.exists(), "Candidate already exists; inspect its result before another attempt"
assert sha256(Original.read_bytes()).hexdigest() == "69eee3e499fde36cba7886ec8504114d164cc8d4942725a9bc8b9560226cfdc8"
with ZipFile(Transfer) as Source, ZipFile(Original) as Archive:
    Document = etree.fromstring(Archive.read("word/document.xml"))
    Relations = etree.fromstring(Archive.read("word/_rels/document.xml.rels"))
    Body = Document.find("w:body", NS)
    Baseline = [etree.tostring(x, method="c14n") for x in Body]
    SourceRoot = etree.fromstring(Source.read("word/document.xml"))
    SourceBody = SourceRoot.find("w:body", NS)
    SourceRelations = {x.get("Id"): x.get("Target") for x in etree.fromstring(Source.read("word/_rels/document.xml.rels"))}
    SourceTables = SourceBody.findall("w:tbl", NS)
    SourceImages = SourceBody.xpath(".//a:blip", namespaces=NS)
    assert len(SourceTables) == len(Layout["tables"]) == 9
    assert len(SourceImages) == len(Layout["figures"]) == 77
    for k in ["Table", "Figure"]:
        Captions = [re.search(r"\b"+k+r" ([A-Z0-9]+-\d+)$", readText(x)) for x in SourceBody if x.tag == "{"+NS["w"]+"}p"]
        Captions = [x.group(1) for x in Captions if x]
        Expected = [x["label"] for x in Layout["tables" if k == "Table" else "figures"]]
        assert Captions == Expected, (k, Captions, Expected)
    Values = {}
    Keys = ["Engine", "PGA 10000 mean", "PGA 10000 P84", "PGA 2500 mean", "PGA 2500 P84",
            "Site amplification", "AEP method", "NRC comparison", "Controlling scenarios", "NRC periods"]
    for i, x in enumerate(SourceBody):
        if readText(x) in Keys:
            Values[readText(x)] = readText(SourceBody[i+1])
    assert set(Values) == set(Keys) and all(Values.values())
    Changed = set()
    for Item, Table in zip(Layout["tables"], SourceTables):
        Rows = Table.findall("w:tr", NS)[1:]
        TargetRows = Body[Item["index"]].findall("w:tr", NS)[2:]
        assert len(Rows) == len(TargetRows)
        for i, (SourceRow, TargetRow) in enumerate(zip(Rows, TargetRows)):
            Cells = SourceRow.findall("w:tc", NS)
            Targets = TargetRow.findall("w:tc", NS)
            assert len(Cells) == len(Targets) == 6
            for j, (Cell, Target) in enumerate(zip(Cells, Targets)):
                s = readText(Cell)
                Before = replaceCell(Target, s)
                Changes.append(dict(kind="cell", table=Item["label"], row=i, column=j, before=Before, after=s))
        Changed.add(Item["index"])

    Parts = {}
    for Item, SourceImage in zip(Layout["figures"], SourceImages):
        Node = Body[Item["index"]]
        Images = Node.xpath(".//a:blip", namespaces=NS)
        assert len(Images) == 1
        Target = "media/diana-hazard-" + Item["label"].lower() + ".png"
        RelationID = "rIdDianaHazard" + Item["label"].replace("-", "")
        assert RelationID not in {x.get("Id") for x in Relations}
        x = etree.SubElement(Relations, "{http://schemas.openxmlformats.org/package/2006/relationships}Relationship")
        x.set("Id", RelationID)
        x.set("Type", "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image")
        x.set("Target", Target)
        Images[0].set("{"+NS["r"]+"}embed", RelationID)
        for x in Node.xpath(".//a:srcRect", namespaces=NS):
            x.getparent().remove(x)
        for x in Node.xpath("./w:r[mc:AlternateContent]", namespaces=NS):
            assert readText(x) == "5% Damping5% Damping"
            x.getparent().remove(x)
        SourceTarget = SourceRelations[SourceImage.get("{"+NS["r"]+"}embed")]
        Parts["word/"+Target] = Source.read("word/"+SourceTarget)
        assert Parts["word/"+Target].startswith(b"\x89PNG\r\n\x1a\n")
        Changes.append(dict(kind="figure", figure=Item["label"], target=Target,
                            sha256=sha256(Parts["word/"+Target]).hexdigest()))
        Changed.add(Item["index"])

    for i in [24,543,786]:
        replaceText(Body[i], "3.19.1" if i != 543 else "3.19", Values["Engine"])
        Changed.add(i)
    replaceText(Body[543], "The results are presented in terms of AEP and UHS for various site conditions", Values["AEP method"] + " The results are presented in terms of AEP and UHS for various site conditions")
    for i in [27,672,788]:
        for s, k in [("0.395","PGA 10000 mean"),("0.491","PGA 10000 P84"),("0.157","PGA 2500 mean"),("0.198","PGA 2500 P84")]:
            replaceText(Body[i], s, Values[k])
        Changed.add(i)
    replaceText(Body[25], "Amplification factors were adopted from the from GMMs of the CanadaSHM6.", Values["Site amplification"])
    replaceText(Body[25], "The amplification factors were then applied to adjust the UHS for these site-specific conditions", "The resulting UHS for these site-specific conditions")
    replaceText(Body[633], "Site amplification factors from GMMs of the CanadaSHM6 were adopted for this study.", "Site amplification factors from GMMs of the CanadaSHM6 were adopted in the direct calculation. " + Values["Site amplification"])
    replaceText(Body[787], "Amplification factors were applied to the Uniform Hazard Spectra (UHS) to account for the site's geotechnical conditions.", Values["Site amplification"])
    replaceText(Body[26], "The results demonstrate that the PSHA analysis aligns with the seismic hazard estimations used in the 2020 NBCC tool.", Values["NRC comparison"])
    replaceText(Body[651], "The comparisons in both figures reveal a good agreement between the PSHA analysis results and the NRC 2020 values, supporting the reliability of the PSHA in estimating seismic hazards for the design of the project facilities.", Values["NRC comparison"])
    replaceText(Body[649], readText(Body[649]), Values["NRC periods"])
    ThirdSentence = "There are no known fault sources in the study area that can contribute to the hazard or influence the deaggregation results."
    assert readText(Body[593]).endswith(ThirdSentence)
    assert not Body[593].xpath(".//w:fldChar", namespaces=NS)
    replaceText(Body[593], readText(Body[593]), Values["Controlling scenarios"] + " " + ThirdSentence)
    for x in Body[593].xpath(".//m:oMath", namespaces=NS):
        x.getparent().remove(x)
    replaceText(Body[856], "90th Percentile", "95th Percentile")
    Changed.update([25,26,593,633,649,651,787,856])

    assert len(Body) == len(Baseline)
    assert all(etree.tostring(x, method="c14n") == Baseline[i] for i,x in enumerate(Body) if i not in Changed)
    assert all(etree.tostring(Body[i], method="c14n") == Baseline[i] for i in range(694,777))
    Parts["word/document.xml"] = etree.tostring(Document, xml_declaration=True, encoding="UTF-8", standalone=True)
    Parts["word/_rels/document.xml.rels"] = etree.tostring(Relations, xml_declaration=True, encoding="UTF-8", standalone=True)
    assert b'Extension="png"' in Archive.read("[Content_Types].xml")
    with ZipFile(Output, "x") as OUT:
        for x in Archive.infolist():
            OUT.writestr(x, Parts.pop(x.filename, Archive.read(x.filename)))
        for s, v in Parts.items():
            OUT.writestr(s, v)
    with ZipFile(Output) as OUT:
        assert OUT.testzip() is None
        for x in Archive.infolist():
            if x.filename not in ["word/document.xml", "word/_rels/document.xml.rels"]:
                assert OUT.read(x.filename) == Archive.read(x.filename), x.filename
    (Folder / "word-changes.json").write_text(json.dumps(Changes, indent=2, ensure_ascii=False)+"\n")
    (Folder / "word-verification.json").write_text(json.dumps(dict(
        original=str(Original), originalSha256=sha256(Original.read_bytes()).hexdigest(),
        transferSha256=sha256(Transfer.read_bytes()).hexdigest(), candidate=str(Output),
        candidateSha256=sha256(Output.read_bytes()).hexdigest(), changedBodyIndices=sorted(Changed),
        tables=len(Layout["tables"]), figures=len(Layout["figures"]),
        allOtherZipPartsUnchanged=True, allOtherBodyObjectsUnchanged=True,
        chapter10Unchanged=True, visualQA="pending"), indent=2)+"\n")
print(Output)
