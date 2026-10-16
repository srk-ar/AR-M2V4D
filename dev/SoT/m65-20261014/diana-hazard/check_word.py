"""Check final transferred numbers, figure payloads and untouched Word content."""
from hashlib import sha256
import json
from pathlib import Path
from zipfile import ZipFile
from lxml import etree

Folder = Path(__file__).resolve().parent
Root = Folder.parents[3]
Layout = json.loads((Root / "_local/hazard.diana.json").read_text())
Products = json.loads((Folder / "product-verification.json").read_text())
Verification = json.loads((Folder / "word-verification.json").read_text())
Changes = json.loads((Folder / "word-changes.json").read_text())
Legends = json.loads((Folder / "legend-check.json").read_text())
Original = Root / Layout["source"]
Candidate = Folder / "CAPR003324_Crawford_SeismicHazard_AVK_R02_candidate04.docx"
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
      "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
      "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
assert sha256(Original.read_bytes()).hexdigest() == Verification["originalSha256"]
assert sha256(Candidate.read_bytes()).hexdigest() == Legends["candidateSha256"]
Cells = 0
with ZipFile(Original) as Source, ZipFile(Candidate) as Archive:
    assert Archive.testzip() is None
    Body = etree.fromstring(Archive.read("word/document.xml")).find("w:body", NS)
    Baseline = etree.fromstring(Source.read("word/document.xml")).find("w:body", NS)
    assert len(Body) == len(Baseline)
    assert all(etree.tostring(x, method="c14n") == etree.tostring(Baseline[i], method="c14n")
               for i,x in enumerate(Body) if i not in Verification["changedBodyIndices"])
    assert all(etree.tostring(Body[i], method="c14n") == etree.tostring(Baseline[i], method="c14n") for i in range(694,777))
    assert all(Archive.read(s) == Source.read(s) for s in Source.namelist()
               if s not in ["word/document.xml", "word/_rels/document.xml.rels"])
    Relations = {x.get("Id"): x.get("Target") for x in etree.fromstring(Archive.read("word/_rels/document.xml.rels"))}
    for Item in Layout["tables"]:
        Rows = Body[Item["index"]].findall("w:tr", NS)[2:]
        Expected = Products["tables"][Item["label"]]
        assert len(Rows) == len(Expected)
        for Row, Values in zip(Rows, Expected):
            Actual = ["".join(x.xpath(".//w:t/text()", namespaces=NS)) for x in Row.findall("w:tc", NS)]
            assert Actual == [Values[s] for s in ["Row"] + [str(v) for v in Layout["vs30"]]], Item["label"]
            Cells += len(Actual)
    for Item in Layout["figures"]:
        Images = Body[Item["index"]].xpath(".//a:blip", namespaces=NS)
        assert len(Images) == 1
        Target = "word/" + Relations[Images[0].get("{"+NS["r"]+"}embed")]
        Expected = next(x["sha256"] for x in Changes if x["kind"] == "figure" and x["figure"] == Item["label"])
        if Target in Legends["changedImages"]:
            Expected = Legends["changedImages"][Target]
        assert sha256(Archive.read(Target)).hexdigest() == Expected, Item["label"]
Result = dict(candidateSha256=Legends["candidateSha256"], tables=9, auditedCells=Cells,
              figurePayloads=77, originalUnchanged=True, chapter10Unchanged=True,
              otherOriginalZipPartsUnchanged=True, otherBodyObjectsUnchanged=True)
(Folder / "final-check.json").write_text(json.dumps(Result, indent=2)+"\n")
print(json.dumps(Result))
