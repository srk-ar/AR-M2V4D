from pathlib import Path
from zipfile import ZipFile
import json
from lxml import etree

Source = Path("docx/diana-actualizado/CAPR003324_Crawford_SeismicHazard_Final_AVK.docx")
with ZipFile(Source) as FILE:
    Root = etree.fromstring(FILE.read("word/document.xml"))
    Relations = etree.fromstring(FILE.read("word/_rels/document.xml.rels"))
NS = {k: v for k, v in Root.nsmap.items() if k}
NS["a"] = "http://schemas.openxmlformats.org/drawingml/2006/main"
NS["wp"] = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
Body = Root.find("w:body", NS)
Targets = {x.get("Id"): x.get("Target") for x in Relations}
Figures = []

def addFigure(index, label, kind, vs30, tr, stat):
    Node = Body[index]
    Images = Node.xpath(".//a:blip", namespaces=NS)
    Extents = Node.xpath(".//w:drawing[.//a:blip]//wp:extent", namespaces=NS)
    assert len(Images) == 1 and len(Extents) == 1, index
    Figures.append(dict(index=index, label=label, kind=kind, vs30=vs30,
                        tr=tr, stat=stat,
                        target=Targets[Images[0].get("{" + NS["r"] + "}embed")],
                        width=int(Extents[0].get("cx"))/914400,
                        height=int(Extents[0].get("cy"))/914400))

for i, v, p, s in [(547,1500,"mean",1),(549,1500,"0.84",2),(554,760,"mean",3),(556,760,"0.84",4)]:
    addFigure(i, f"6-{s}", "aep", v, None, p)
for i, v, p, s in [(560,1500,"mean",5),(562,1500,"0.84",6),(564,760,"mean",7),(567,760,"0.84",8)]:
    addFigure(i, f"6-{s}", "uhs", v, None, p)
for i, t, s in zip([581,583,585,587,590],[500,1000,2500,5000,10000],range(9,14)):
    addFigure(i, f"6-{s}", "rmw", 760, t, None)
for i, p, s in [(638,"mean",7),(640,"0.84",8)]:
    addFigure(i, f"7-{s}", "uhs", 220, None, p)
for i, v, s in [(652,1500,1),(655,760,2),(657,220,3)]:
    addFigure(i, f"8-{s}", "nrc", v, None, "mean")
for i, t, p, s in [(678,10000,"mean",1),(680,10000,"0.84",2),(682,2500,"mean",3),(684,2500,"0.84",4)]:
    addFigure(i, f"9-{s}", "design", None, t, p)
for a, b, k in [("C1",847,"aep"),("C2",901,"uhs")]:
    for j, v in enumerate([1500,910,760,580,220]):
        for n, p in enumerate(["mean","0.5","0.84","0.9","0.95"]):
            addFigure(b+10*j+2*n, f"{a}-{5*j+n+1}", k, v, None, p)
for n, p in enumerate(["mean","0.5","0.84","0.9","0.95"]):
    addFigure(978+2*n, f"D2-{n+1}", "design", None, 10000, p)

Tables = [dict(index=i,label=s,kind=k,stat=p,tr=t) for i,s,k,p,t in [
    (667,"9-1","pga","mean",None),(670,"9-2","pga","0.84",None),
    (689,"9-3","spectra","mean",10000),(692,"9-4","spectra","mean",2500),
    (957,"D1-1","pga","mean",None),(960,"D1-2","pga","0.5",None),
    (963,"D1-3","pga","0.84",None),(966,"D1-4","pga","0.9",None),
    (970,"D1-5","pga","0.95",None)]]
for x in Tables:
    assert Body[x["index"]].tag == "{"+NS["w"]+"}tbl"
assert len(Figures) == 77
assert len({x["index"] for x in Figures}) == 77
OUT = dict(source=str(Source), figures=Figures, tables=Tables,
           vs30=[1500,910,760,580,220], tr=[500,1000,2500,5000,10000],
           trLabel=["475","975","2,475","5,000","10,000"],
           aepPeriods=[0,0.05,0.1,0.2,0.3,0.4,0.5,1,1.5,2.5])
Path("_local/hazard.diana.json").write_text(json.dumps(OUT,indent=2)+"\n")
print("Mapped",len(Tables),"tables and",len(Figures),"figure occurrences")
