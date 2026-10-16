"""Make an editorial candidate from R03; retain scientific payloads verbatim."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
import zipfile
from lxml import etree as E

Root = Path(__file__).resolve().parents[4]
Work = Path('/private/tmp/diana-editorial-20261016')
Source = Root/'docx/diana-actualizado/CAPR003324_Diana_R03.docx'
Output = Work/'candidate06/CAPR003324_Diana_R04.docx'
Ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
      'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math',
      'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
W = '{'+Ns['w']+'}'
Changes = []
assert hashlib.sha256(Source.read_bytes()).hexdigest() == 'b99c80fad1f56c91b82c12304b68a8e33f43a69fe880225e341c14bb0221896b'
with zipfile.ZipFile(Source) as FILE:
    Parts = {x: FILE.read(x) for x in FILE.namelist()}
Xml = E.fromstring(Parts['word/document.xml'])
Body = Xml.find('w:body', Ns)
Baseline = deepcopy(Xml)


def visible(node):
    return ''.join((x.text or '') if x.tag in (W+'t', '{'+Ns['m']+'}t') else '-' if x.tag == W+'noBreakHyphen' else '\t'
                   for x in node.iter() if x.tag in (W+'t', '{'+Ns['m']+'}t', W+'noBreakHyphen', W+'tab')
                   and not any(y.tag in (W+'del', W+'moveFrom') for y in x.iterancestors()))


def unwrap(node):
    p = node.getparent(); i = p.index(node)
    for x in list(node):
        p.insert(i, x); i += 1
    p.remove(node)


def setText(node, text):
    """Replace ordinary text, preserving paragraph properties and bookmark IDs."""
    assert not node.xpath('.//m:oMath | .//w:drawing | .//w:tbl', namespaces=Ns)
    Runs = node.xpath('.//w:r[w:t]', namespaces=Ns)
    Props = deepcopy(Runs[0].find('w:rPr', Ns)) if Runs and Runs[0].find('w:rPr', Ns) is not None else None
    for x in list(node):
        if x.tag not in (W+'pPr', W+'bookmarkStart', W+'bookmarkEnd'):
            node.remove(x)
    r = E.Element(W+'r')
    if Props is not None: r.append(Props)
    t = E.SubElement(r, W+'t'); t.text = text; t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    node.append(r)


def replaceText(node, old, new):
    """Replace a known literal across text runs without touching math or pictures."""
    Nodes = node.xpath('.//w:t', namespaces=Ns)
    s = ''.join(x.text or '' for x in Nodes)
    assert old in s, (old, s[:120])
    for a in reversed([x.start() for x in re.finditer(re.escape(old),s)]):
        b = a+len(old); i = 0; Started = False
        for x in Nodes:
            t = x.text or ''; j = i+len(t)
            if j > a and i < b:
                x.text = t[:max(0,a-i)] + (new if not Started else '') + t[max(0,b-i):]
                x.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
                Started = True
            i = j
    Changes.append({'before': old, 'after': new})


# Materialize the R03 final view in this new delivery. R03 remains untouched.
for x in list(Xml.xpath('.//w:del | .//w:moveFrom | .//w:pPrChange | .//w:rPrChange | .//w:tblPrChange | .//w:tcPrChange | .//w:trPrChange', namespaces=Ns)):
    if x.getparent() is not None: x.getparent().remove(x)
for x in list(Xml.xpath('.//w:ins | .//w:moveTo', namespaces=Ns)):
    if x.getparent() is not None: unwrap(x)
for x in list(Xml.xpath('.//w:sdt', namespaces=Ns)):
    # Only inline SDTs; retain the body TOC and bibliography containers.
    if x.getparent() is not Body:
        p = x.getparent(); i = p.index(x)
        for y in list(x.find('w:sdtContent', Ns)): p.insert(i,y); i += 1
        p.remove(x)

# Complete field parsing handles nested TOCs and split instruction runs.
Stack = []; Fields = []
for x in Xml.iter():
    if x.tag == W+'fldChar':
        s = x.get(W+'fldCharType')
        if s == 'begin': Stack.append({'start': x, 'instruction': '', 'result': [], 'separate': False})
        elif s == 'separate': Stack[-1]['separate'] = True
        elif s == 'end':
            OUT = Stack.pop(); OUT['end'] = x; Fields.append(OUT)
    elif x.tag == W+'instrText' and Stack: Stack[-1]['instruction'] += x.text or ''
    elif x.tag in (W+'t', W+'noBreakHyphen'):
        for y in Stack:
            if y['separate']: y['result'].append(x)
assert not Stack

ChapterRefs = {'_Ref174451674': '2', '_Ref174451708': '3', '_Ref174031794': '4',
               '_Ref174451752': '5', '_Ref174451818': '7', '_Ref174451850': '7', '_Ref174967815': '9'}
for x in Fields:
    s = x['instruction'].strip(); t = ''.join(y.text or '-' for y in x['result'])
    if s.startswith('REF '):
        k = s.split()[1]
        v = ChapterRefs.get(k, t.replace('11Appendix', 'Appendix'))
        if k in ('_Ref175137289','_Ref178015982','_Ref172153802','_Ref172153775'): v = ''
        if k == '_Ref174438610': v = 'Table 7-2 '
        if v != t:
            assert x['result']
            x['result'][0].text = v
            for y in x['result'][1:]: y.getparent().remove(y)
            Changes.append({'field': s, 'before': t, 'after': v})
    if s.startswith('CITATION '):
        p = next(y for y in x['start'].iterancestors(W+'p'))
        b = next(y for y in x['start'].iterancestors() if y.getparent() is Body)
        if Body.index(b) == 26 and 'Nat213' in s:
            for y in x['result']:
                if y.text: y.text = y.text.replace('2021d','2021c')
        if 'Com10' in s:
            for y in x['result']:
                if y.text: y.text = y.text.replace('2010','2011')

# Verified caption caches are retained as text, avoiding corrupt STYLEREF/SEQ
# recomputation; references and bibliography likewise become stable final text.
for x in list(Xml.xpath('.//w:fldChar | .//w:instrText | .//w:delInstrText', namespaces=Ns)):
    x.getparent().remove(x)
for x in list(Xml.xpath('.//w:fldSimple', namespaces=Ns)): unwrap(x)

Replacements = {
    'Canadian Comission on Building and Fires Codes': 'Canadian Commission on Building and Fire Codes',
    'Natural Resources of Canada': 'Natural Resources Canada',
    'Natural Resources de Canada': 'Natural Resources Canada',
    'Gutenberg & Ritcher': 'Gutenberg & Richter',
    'Gutenberg, B., & Ritcher': 'Gutenberg, B., & Richter',
    'Mayfied': 'Mayfield', 'Travasauro': 'Travasarou',
    '(Goulet, et al., 2017)': '(Goulet et al., 2017)',
    '(Pagani, Monelli, & Weatgerill, 2014)': '(Pagani et al., 2014)',
    '(Atkinson & Adams, Ground motion prediction equations for application to the 2015 Canadian national seismic hazard maps, 2013)': '(Atkinson & Adams, 2013)',
    '(Mazzotti, 2005)': '(Mazzotti & Adams, 2005)',
    'Bray & Travasarou, Pseudostatic Coefficient for Use in Simplified Seismic Slope Stability Evaluation, 2009': 'Bray & Travasarou, 2009',
    'Bray & Travasarou, Simplified Procedure for Estimating Earthquake-Induced Deviatoric Slope Displacements, 2007': 'Bray & Travasarou, 2007',
    'Bray, Macedo, & Travasarou, Simplified procedure for estimating seismic slope displacements for subduction and crustal earthquakes, 2018': 'Bray, Macedo, & Travasarou, 2018',
    'Bray & Macedo, Procedure for Estimating Shear-Induced Seismic Slope Displacement for Shallow Crustal Earthquakes, 2019': 'Bray & Macedo, 2019',
    'Table B-1through': 'Table B-1 through',
    '(2013)(AA13)': '(2013) (AA13)',
}
for p in Xml.xpath('.//w:p', namespaces=Ns):
    for s,t in Replacements.items():
        if s in ''.join(p.xpath('.//w:t/text()', namespaces=Ns)): replaceText(p,s,t)
replaceText(Body[635], 'Harmon, et al.', 'Harmon')
replaceText(Body[25], '(SRK Consulting (Canada), Inc., 2023) (2024)', '(SRK Consulting (Canada), Inc., 2023, 2024)')
replaceText(Body[610], '(SRK Consulting (Canada), Inc., 2024) (2023)', '(SRK Consulting (Canada), Inc., 2023, 2024)')
replaceText(Body[653], '1500 m/s/', '1500 m/s')
replaceText(Body[656], '760 ms/', '760 m/s')
for i in [983,985,987]:
    for s,t in [('84h','84th'),('90h','90th'),('95h','95th'),('–95th','– 95th')]:
        if s in visible(Body[i]): replaceText(Body[i],s,t)

# The corrected section headings use the document's existing appendix labels.
Appendices = {825:'Appendix A - Crawford Updated Seismic Catalog',
              833:'Appendix B - Southeastern Model Seismic Sources of the CanadaSHM6',
              844:'Appendix C - Seismic Hazard Results',845:'C1 - Annual Exceedance Probability',
              899:'C2 - Uniform Hazard Spectra',952:'Appendix D - Design Earthquakes',
              954:'D1 - Design Peak Ground Acceleration',973:'D2 - Design Response Spectrum'}
for i,s in Appendices.items():
    setText(Body[i],s)
    p = Body[i].find('w:pPr',Ns)
    for x in list(p.findall('w:numPr',Ns)): p.remove(x)
    z = E.SubElement(p,W+'numPr'); E.SubElement(z,W+'numId').set(W+'val','0')
    z = p.find('w:outlineLvl',Ns)
    if z is None: z = E.SubElement(p,W+'outlineLvl')
    z.set(W+'val', '0' if s.startswith('Appendix') else '1')

for p in Xml.xpath('.//w:p[w:pPr/w:pStyle[starts-with(@w:val,"Heading")]]',namespaces=Ns):
    if not visible(p).strip():
        p.find('w:pPr/w:pStyle',Ns).set(W+'val','Normal')
        for x in list(p.xpath('./w:pPr/w:numPr',namespaces=Ns)): x.getparent().remove(x)
for i in [990,996,1017,1051]:
    p = Body[i].find('w:pPr',Ns)
    for x in list(p.findall('w:numPr',Ns)): p.remove(x)
    z = E.SubElement(p,W+'numPr'); E.SubElement(z,W+'numId').set(W+'val','0')

# Remove only mathematically empty shells, verified to contain no visible token.
for x in list(Xml.xpath('.//m:oMathPara | .//m:oMath', namespaces=Ns)):
    if not ''.join(x.xpath('.//m:t/text()', namespaces=Ns)) and x.getparent() is not None:
        x.getparent().remove(x)

References = Body[792].xpath('.//w:p[w:pPr/w:pStyle[@w:val="Bibliography"]]', namespaces=Ns)
Bibliography = {
 'American Society of Civil Engineers. (2022)': 'American Society of Civil Engineers. (2022). Minimum Design Loads and Associated Criteria for Buildings and Other Structures, ASCE/SEI 7-22. Reston, VA. https://doi.org/10.1061/9780784415788',
 'Atkinson, G. M., & Boore,': 'Atkinson, G. M., & Boore, D. M. (2006). Earthquake ground-motion prediction equations for eastern North America. Bulletin of the Seismological Society of America, 96(6), 2181-2205. https://doi.org/10.1785/0120050245',
 'Boore, D. M., & Campbell,': 'Boore, D. M., & Campbell, K. W. (2017). Adjusting central and eastern North America ground-motion intensity measures between sites with different reference-rock site conditions. Bulletin of the Seismological Society of America, 107(1), 132-148. https://doi.org/10.1785/0120160208',
 'Bray, J. D., Macedo,': 'Bray, J. D., Macedo, J., & Travasarou, T. (2018). Simplified Procedure for Estimating Seismic Slope Displacements for Subduction Zone Earthquakes. Journal of Geotechnical and Geoenvironmental Engineering, 144(3), 04017124. https://doi.org/10.1061/(ASCE)GT.1943-5606.0001833',
 'Goulet, C. A.,': 'Goulet, C. A., Bozorgnia, Y., Kuehn, N., Al Atik, L., Youngs, R. R., Graves, R. W., & Atkinson, G. M. (2017). NGA-East Ground-Motion Models for the U.S. Geological Survey National Seismic Hazard Maps. PEER Report No. 2017/03. Pacific Earthquake Engineering Research Center.',
 'Harmon, J. K.,': 'Harmon, J. A. (2017). Nonlinear site amplification functions for Central and Eastern North America. Ph.D. dissertation, University of Illinois at Urbana-Champaign. https://hdl.handle.net/2142/97722',
 'Kaklamanos, J.,': 'Kaklamanos, J., Baise, L. G., & Boore, D. M. (2011). Estimating Unknown Input Parameters when Implementing the NGA Ground-Motion Prediction Equations in Engineering Practice. Earthquake Spectra, 27(4), 1219-1235. https://doi.org/10.1193/1.3650372',
 'Mazzotti, S. (2005)': 'Mazzotti, S., & Adams, J. (2005). Rates and uncertainties on seismic moment and deformation in eastern Canada. Journal of Geophysical Research: Solid Earth, 110, B09301. https://doi.org/10.1029/2004JB003510',
 'Natural Resources Canada. (2020)': 'Kolaj, M., Halchuk, S., Adams, J., & Allen, T. I. (2020). Sixth generation seismic hazard model of Canada: input files to produce values proposed for the 2020 National Building Code of Canada. Geological Survey of Canada, Open File 8630.',
 'Pagani, M.,': 'Pagani, M., Monelli, D., Weatherill, G., Danciu, L., Crowley, H., Silva, V., Henshaw, P., Butler, R., Nastasi, M., Panzeri, L., Simionato, M., & Vigano, D. (2014). OpenQuake Engine: An Open Hazard (and Risk) Software for the Global Earthquake Model. Seismological Research Letters, 85(3), 692-702.',
 'Peltier, W. R. (2004)': 'Peltier, W. R. (2004). Global Glacial Isostasy and the Surface of the Ice-Age Earth: The ICE-5G (VM2) Model and GRACE. Annual Review of Earth and Planetary Sciences, 32, 111-149. https://doi.org/10.1146/annurev.earth.32.082503.144359',
 'Petersen, M. D.,': 'Petersen, M. D., Shumway, A. M., Powers, P. M., Mueller, C. S., Moschetti, M. P., Frankel, A. D., Rezaeian, S., McNamara, D. E., Hoover, S. M., Luco, N., Boyd, O. S., Rukstales, K. S., Jaiswal, K. S., Thompson, E. M., Clayton, B., Field, E. H., & Zeng, Y. (2018). Preliminary 2018 Update of the U.S. National Seismic Hazard Model: Overview of Model, Changes, and Implications. U.S. Geological Survey report for public comment, 1-47.',
}
for p in References:
    s = visible(p)
    for k,v in Bibliography.items():
        if s.startswith(k):
            assert v
            Changes.append({'before':s,'after':v}); setText(p,v); break
    if '7th World Conference' in visible(p): replaceText(p,'7th World Conference','17th World Conference')
    if 'Dakaoulas ,' in visible(p): replaceText(p,'Dakaoulas ,','Dakoulas,')
    if 'Pravia, Italy' in visible(p): replaceText(p,'Pravia, Italy','Pavia, Italy')
for p in Xml.xpath('.//w:p', namespaces=Ns):
    if '(Natural Resources Canada, 2020)' in visible(p): replaceText(p,'(Natural Resources Canada, 2020)','(Kolaj, Halchuk, Adams, & Allen, 2020)')
    if 'CAPR003324_Crawford_SeismicHazard_Final.docx' in visible(p): replaceText(p,'CAPR003324_Crawford_SeismicHazard_Final.docx','CAPR003324_Diana_R04.docx')

# Add the missing bibliography entry for the method already cited in chapter 3.
Gardner = deepcopy(References[0]); setText(Gardner, 'Gardner, J. K., & Knopoff, L. (1974). Is the sequence of earthquakes in Southern California, with aftershocks removed, Poissonian? Bulletin of the Seismological Society of America, 64(5), 1363-1367.')
for x in list(Gardner.xpath('.//w:bookmarkStart | .//w:bookmarkEnd',namespaces=Ns)): x.getparent().remove(x)
Container = References[0].getparent()
Container.insert(Container.index(References[0]),Gardner)
References.append(Gardner)
# Sort the existing bibliography paragraphs without changing unrelated objects.
for p in References: p.getparent().remove(p)
for p in sorted(References,key=lambda x: visible(x).casefold()):
    if visible(p).strip(): Container.append(p)

# Build linked navigation from real included headings and captions.
BookmarkId = max(int(x) for x in Xml.xpath('.//w:bookmarkStart/@w:id',namespaces=Ns))+1


def anchor(node, name):
    global BookmarkId
    a = E.Element(W+'bookmarkStart'); a.set(W+'id',str(BookmarkId)); a.set(W+'name',name)
    b = E.Element(W+'bookmarkEnd'); b.set(W+'id',str(BookmarkId)); BookmarkId += 1
    i = 1 if node.find('w:pPr',Ns) is not None else 0
    node.insert(i,a); node.append(b)


def entry(text, target, style):
    p = E.Element(W+'p'); Props = E.SubElement(p,W+'pPr')
    E.SubElement(Props,W+'pStyle').set(W+'val',style)
    Tabs = E.SubElement(Props,W+'tabs'); t = E.SubElement(Tabs,W+'tab')
    t.set(W+'val','right'); t.set(W+'leader','dot'); t.set(W+'pos','8640')
    Link = E.SubElement(p,W+'hyperlink'); Link.set(W+'anchor',target); Link.set(W+'history','1')
    r = E.SubElement(Link,W+'r'); E.SubElement(r,W+'t').text = text
    r = E.SubElement(p,W+'r'); E.SubElement(r,W+'tab')
    for k,s in [('begin',''),('instruction',' PAGEREF '+target+' \\h '),('separate',''),('text','0'),('end','')]:
        r = E.SubElement(p,W+'r')
        if k == 'instruction': E.SubElement(r,W+'instrText').text = s
        elif k == 'text': E.SubElement(r,W+'t').text = s
        else: E.SubElement(r,W+'fldChar').set(W+'fldCharType',k)
    return p


Headings = []; Captions = {'Table': [],'Figure': []}; Numbers = [0,0,0]
for i,b in enumerate(list(Body)):
    if i < 342: continue
    for p in ([b] if b.tag == W+'p' else b.xpath('.//w:p',namespaces=Ns)):
        s = visible(p).strip(); t = p.find('w:pPr/w:pStyle',Ns)
        t = t.get(W+'val') if t is not None else ''
        Label = None; Level = None
        if i in Appendices or i in [990,996,1017,1051]:
            Label = s; Level = 1 if s.startswith('Appendix') else 2
        elif t in ['Heading1','Heading2','Heading3']:
            Level = int(t[-1]); Numbers[Level-1] += 1
            for j in range(Level,3): Numbers[j] = 0
            Label = '.'.join(map(str,Numbers[:Level]))+' '+s
            if s == 'References': Label = s
        if Label:
            Target = 'R04Heading'+str(i); anchor(p,Target)
            Headings.append((Label,Target,'TOC'+str(Level)))
        if t == 'Caption' and re.match(r'^(Table|Figure) [A-E0-9][A-E0-9]*-\d+:',s):
            k = s.split()[0]; Target = 'R04'+k+str(i); anchor(p,Target)
            Captions[k].append((s,Target,'TableofFigures'))

Toc = Body[34].find('w:sdtContent',Ns)
Title = deepcopy(Toc[0])
for x in list(Toc): Toc.remove(x)
Toc.append(Title)
for s,t,k in Headings: Toc.append(entry(s,t,k))
for k,a,b in [('Table',37,91),('Figure',92,342)]:
    assert len(Captions[k]) <= b-a
    for i in range(a,b):
        p = Body[i]
        if p.tag != W+'p':
            assert i-a >= len(Captions[k])
            continue
        if i-a < len(Captions[k]):
            s,t,z = Captions[k][i-a]; Body.replace(p,entry(s,t,z))
        else:
            for x in list(p):
                if x.tag != W+'pPr': p.remove(x)
            Props = p.find('w:pPr',Ns)
            if Props is None: Props = E.SubElement(p,W+'pPr')
            for x in list(Props):
                if x.tag != W+'sectPr': Props.remove(x)
            Space = E.SubElement(Props,W+'spacing')
            for name,value in [('before','0'),('after','0'),('line','1'),('lineRule','exact')]: Space.set(W+name,value)
            RunProps = E.SubElement(Props,W+'rPr'); E.SubElement(RunProps,W+'sz').set(W+'val','2')

Settings = E.fromstring(Parts['word/settings.xml'])
for x in list(Settings.findall('w:trackRevisions',Ns)): Settings.remove(x)
Update = Settings.find('w:updateFields',Ns)
if Update is None: Update = E.SubElement(Settings,W+'updateFields')
Update.set(W+'val','true')
Parts['word/document.xml'] = E.tostring(Xml,xml_declaration=True,encoding='UTF-8',standalone=True)
Parts['word/settings.xml'] = E.tostring(Settings,xml_declaration=True,encoding='UTF-8',standalone=True)
Output.parent.mkdir(parents=True,exist_ok=True)
assert not Output.exists()
with zipfile.ZipFile(Output,'w',zipfile.ZIP_DEFLATED) as FILE:
    for k,v in Parts.items(): FILE.writestr(k,v)
Record = {'output':str(Output),'sha256':hashlib.sha256(Output.read_bytes()).hexdigest(),
          'changes':Changes,'headings':Headings,'captions':Captions}
Path(__file__).with_name('candidate06.json').write_text(json.dumps(Record,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'output':str(Output),'changes':len(Changes),'headings':len(Headings),'captions':{k:len(v) for k,v in Captions.items()}}))
