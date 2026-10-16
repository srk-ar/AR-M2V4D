from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import posixpath
from zipfile import ZipFile

from lxml import etree


Root = Path(__file__).resolve().parents[4]
Output = Path(__file__).resolve().parent
Files = {
    "original": "docx/CAPR003324_Crawford_SeismicHazard_Final.docx",
    "avk": "docx/diana-actualizado/CAPR003324_Crawford_SeismicHazard_Final_AVK.docx",
    "r02": "docx/diana-actualizado/CAPR003324_Crawford_SeismicHazard_Final_AVK_R02.docx",
    "report": "docx/docx.en.docx",
    "memo": "docx/gmdp.memo.en.docx",
    "hazard": "docx/hazard.diana.en.docx",
}
Namespaces = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}


def nodeHash(node):
    return sha256(etree.tostring(node, method="c14n", exclusive=True)).hexdigest()


def nodeText(node):
    return "".join(node.xpath(".//w:t/text() | .//m:t/text()", namespaces=Namespaces))


def inspectDocument(path):
    with ZipFile(path) as FILE:
        Parts = {x: sha256(FILE.read(x)).hexdigest() for x in FILE.namelist()}
        Document = etree.fromstring(FILE.read("word/document.xml"))
        Body = Document.find("w:body", Namespaces)
        Relations = {
            x.get("Id"): posixpath.normpath("word/" + x.get("Target"))
            for x in etree.fromstring(FILE.read("word/_rels/document.xml.rels"))
            if x.get("TargetMode") != "External"
        }
        Settings = etree.fromstring(FILE.read("word/settings.xml"))
        OUT = {
            "path": str(path), "bytes": path.stat().st_size,
            "sha256": sha256(path.read_bytes()).hexdigest(), "parts": Parts,
            "bodyCount": len(Body), "nodes": [], "tables": [], "images": [],
            "revisions": {}, "trackRevisions": bool(Settings.xpath("./w:trackRevisions", namespaces=Namespaces)),
        }
        for i, x in enumerate(Body, start=1):
            OUT["nodes"].append({"bodyIndex": i, "tag": etree.QName(x).localname, "sha256": nodeHash(x), "text": nodeText(x)})
            if x.tag == "{" + Namespaces["w"] + "}tbl":
                OUT["tables"].append({"bodyIndex": i, "rows": [[nodeText(v) for v in y.findall("w:tc", Namespaces)] for y in x.findall("w:tr", Namespaces)]})
            for y in x.xpath(".//a:blip", namespaces=Namespaces):
                s = y.get("{" + Namespaces["r"] + "}embed")
                OUT["images"].append({"bodyIndex": i, "relationship": s, "part": Relations.get(s), "sha256": Parts.get(Relations.get(s))})
        for s in ["ins", "del", "rPrChange", "pPrChange", "tblPrChange", "trPrChange", "tcPrChange", "moveFrom", "moveTo"]:
            OUT["revisions"][s] = [{"id": x.get("{" + Namespaces["w"] + "}id"), "author": x.get("{" + Namespaces["w"] + "}author"), "sha256": nodeHash(x)} for x in Document.xpath(".//w:" + s, namespaces=Namespaces)]
        OUT["math"] = [nodeHash(x) for x in Document.xpath(".//m:oMath", namespaces=Namespaces)]
        return OUT


Documents = {s: inspectDocument(Root / x) for s, x in Files.items()}
Comparisons = {}
for s, t in [("original", "avk"), ("avk", "r02")]:
    A = Documents[s]
    B = Documents[t]
    OUT = {
        "changedParts": [x for x in A["parts"] if x in B["parts"] and A["parts"][x] != B["parts"][x]],
        "addedParts": sorted(set(B["parts"]) - set(A["parts"])),
        "removedParts": sorted(set(A["parts"]) - set(B["parts"])),
        "bodyCounts": [A["bodyCount"], B["bodyCount"]], "changedNodes": [], "revisions": {},
    }
    if A["bodyCount"] == B["bodyCount"]:
        OUT["changedNodes"] = [{"bodyIndex": x["bodyIndex"], "tag": x["tag"], "before": x["text"], "after": y["text"]} for x, y in zip(A["nodes"], B["nodes"]) if x["sha256"] != y["sha256"]]
    for k in A["revisions"]:
        DATA = Counter(x["sha256"] for x in A["revisions"][k])
        AUX = Counter(x["sha256"] for x in B["revisions"][k])
        OUT["revisions"][k] = {"counts": [sum(DATA.values()), sum(AUX.values())], "added": sum((AUX - DATA).values()), "removed": sum((DATA - AUX).values())}
    Comparisons[s + "-" + t] = OUT

for s, x in Documents.items():
    (Output / (s + ".structure.json")).write_text(json.dumps(x, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(Output / "comparison.json").write_text(json.dumps(Comparisons, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"documents": {s: {k: x[k] for k in ["sha256", "bytes", "bodyCount", "trackRevisions"]} for s, x in Documents.items()}, "comparisons": {s: {"changedParts": x["changedParts"], "addedParts": x["addedParts"], "changedNodes": len(x["changedNodes"]), "revisions": x["revisions"]} for s, x in Comparisons.items()}}, indent=2))
