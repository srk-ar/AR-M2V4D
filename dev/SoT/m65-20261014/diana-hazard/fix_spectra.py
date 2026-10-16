"""Apply the existing spectral-table grid consistently to every row."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
from zipfile import ZipFile
from lxml import etree

Folder = Path(__file__).resolve().parent
Source = Folder / "CAPR003324_Crawford_SeismicHazard_AVK_R02_candidate02.docx"
Output = Folder / "CAPR003324_Crawford_SeismicHazard_AVK_R02_candidate03.docx"
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
Tag = "{" + NS["w"] + "}"
with ZipFile(Source) as Archive:
    Document = etree.fromstring(Archive.read("word/document.xml"))
    Body = Document.find("w:body", NS)
    Baseline = [etree.tostring(x, method="c14n") for x in Body]
    Text = Document.xpath("//w:t/text()", namespaces=NS)
    for i in [689,692]:
        Table = Body[i]
        Grid = [int(x.get(Tag+"w")) for x in Table.find("w:tblGrid", NS)]
        Properties = Table.find("w:tblPr", NS)
        Layout = Properties.find("w:tblLayout", NS)
        if Layout is None:
            Layout = etree.SubElement(Properties, Tag+"tblLayout")
        Layout.set(Tag+"type", "fixed")
        Width = Properties.find("w:tblW", NS)
        Width.set(Tag+"type", "dxa")
        Width.set(Tag+"w", str(sum(Grid)))
        for Row in Table.findall("w:tr", NS):
            n = 0
            for Cell in Row.findall("w:tc", NS):
                Properties = Cell.find("w:tcPr", NS)
                Span = Properties.find("w:gridSpan", NS)
                k = 1 if Span is None else int(Span.get(Tag+"val"))
                Width = Properties.find("w:tcW", NS)
                Width.set(Tag+"type", "dxa")
                Width.set(Tag+"w", str(sum(Grid[n:n+k])))
                n += k
            assert n == len(Grid)
    assert Document.xpath("//w:t/text()", namespaces=NS) == Text
    assert all(etree.tostring(x, method="c14n") == Baseline[i] for i,x in enumerate(Body) if i not in [689,692])
    with ZipFile(Output, "x") as OUT:
        for Item in Archive.infolist():
            DATA = Archive.read(Item.filename)
            if Item.filename == "word/document.xml":
                DATA = etree.tostring(Document, xml_declaration=True, encoding="UTF-8", standalone=True)
            OUT.writestr(deepcopy(Item), DATA)
with ZipFile(Source) as Archive, ZipFile(Output) as OUT:
    assert OUT.testzip() is None
    assert all(OUT.read(s) == Archive.read(s) for s in Archive.namelist() if s != "word/document.xml")
(Folder / "spectral-layout-check.json").write_text(json.dumps(dict(
    baselineSha256=sha256(Source.read_bytes()).hexdigest(), candidateSha256=sha256(Output.read_bytes()).hexdigest(),
    preservedAllText=True, changedTables=[689,692], otherBodyObjectsAndZipPartsIdentical=True,
    visualQA="pending"), indent=2)+"\n")
print(Output)
