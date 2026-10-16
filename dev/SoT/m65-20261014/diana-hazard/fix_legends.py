"""Replace only UHS images from the NGR render with readable legends."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import re
from zipfile import ZipFile
from lxml import etree

Folder = Path(__file__).resolve().parent
Root = Folder.parents[3]
Source = Folder / "CAPR003324_Crawford_SeismicHazard_AVK_R02_candidate03.docx"
Transfer = Root / "docx/hazard.diana.en.docx"
Output = Folder / "CAPR003324_Crawford_SeismicHazard_AVK_R02_candidate04.docx"
Layout = json.loads((Root / "_local/hazard.diana.json").read_text())
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
      "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
      "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
Parts = {}
with ZipFile(Transfer) as Archive:
    Body = etree.fromstring(Archive.read("word/document.xml")).find("w:body", NS)
    Relations = {x.get("Id"): x.get("Target") for x in etree.fromstring(Archive.read("word/_rels/document.xml.rels"))}
    for Table in Body.findall("w:tbl", NS):
        Text = "".join(Table.xpath(".//w:t/text()", namespaces=NS))
        Label = re.search(r"\bFigure ([A-Z0-9]+-\d+)$", Text)
        if Label is None:
            continue
        Item = next(x for x in Layout["figures"] if x["label"] == Label.group(1))
        if Item["kind"] != "uhs":
            continue
        Image = Table.xpath(".//a:blip", namespaces=NS)
        assert len(Image) == 1
        Target = Relations[Image[0].get("{"+NS["r"]+"}embed")]
        Parts["word/media/diana-hazard-" + Item["label"].lower() + ".png"] = Archive.read("word/" + Target)
assert len(Parts) == sum(x["kind"] == "uhs" for x in Layout["figures"]) == 31
with ZipFile(Source) as Archive, ZipFile(Output, "x") as OUT:
    assert set(Parts).issubset(Archive.namelist())
    for Item in Archive.infolist():
        OUT.writestr(deepcopy(Item), Parts.get(Item.filename, Archive.read(Item.filename)))
with ZipFile(Source) as Archive, ZipFile(Output) as OUT:
    assert OUT.testzip() is None
    assert Archive.namelist() == OUT.namelist()
    assert all(Archive.read(s) == OUT.read(s) for s in Archive.namelist() if s not in Parts)
    assert all(OUT.read(s) == v for s,v in Parts.items())
(Folder / "legend-check.json").write_text(json.dumps(dict(
    baselineSha256=sha256(Source.read_bytes()).hexdigest(),
    transferSha256=sha256(Transfer.read_bytes()).hexdigest(),
    candidateSha256=sha256(Output.read_bytes()).hexdigest(),
    changedImages={s:sha256(v).hexdigest() for s,v in Parts.items()},
    otherPartsIdentical=True, visualQA="pending"), indent=2)+"\n")
print(Output)
