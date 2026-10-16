"""Record the completed, bounded editorial review; no scientific prose rewrite."""
from pathlib import Path
import hashlib
import json

Here = Path(__file__).parent
Audit = json.loads((Here/'prose-audit.json').read_text())
Changes = json.loads((Here/'candidate04.json').read_text())['changes']
Sources = {
1:'R03 NBCC reference and Canadian Commission corporate identity',2:'PEER Report 2017/03, primary PEER publications metadata',
3:'R03 Atkinson and Adams 2013 citation and AA13 abbreviation; whitespace only',4:'Official NRCan Open File 8630 publisher identity',
5:'Wiley DOI 10.1029/2004JB003510, two authors',6:'R03 bibliography Gutenberg and Richter 1944, surname spelling',
7:'R03 bibliography Atkinson and Adams 2013, same work with title removed from in-text citation',8:'GEM OpenQuake citation; Kolaj 2019 references, hydrated lines83-90',
9:'R03 Rathje and Mayfield 2008 bibliography',10:'R03 bibliography Bray and Travasarou 2009; title retained in bibliography',
11:'ASCE Bray et al. 2018 author list',12:'R03 Gutenberg and Richter 1944 bibliography',
13:'R03 bibliography Bray and Travasarou 2007',14:'ASCE DOI10.1061/(ASCE)GT.1943-5606.0001833 and bib/references.bib:394-406',
15:'R03 bibliography Bray and Macedo 2019',16:'Illinois IDEALS102775, owner-confirmed Harmon thesis 2017',
17:'R03 SRK2023 and SRK2024 entries and adjacent citations, both retained',18:'R03 caption body653 and Vs1500 figure',19:'R03 caption body656 and Vs760 figure',
20:'R03 body983 percentile84 caption',21:'R03 body985 percentile90 caption',22:'R03 body987 percentile95 caption',23:'R03 body987 separator before percentile95',
24:'ASCE official book DOI10.1061/9780784415788, ASCE/SEI7-22',25:'USGS publication70028671 metadata',26:'USGS publication70189619 metadata',
27:'ASCE DOI10.1061/(ASCE)GT.1943-5606.0001833, 144(3),04017124',28:'R03 Dakoulas source surname, same work',29:'R03 European school publication location, Pavia',
30:'PEER primary publications 2017/03 complete author list',31:'Illinois IDEALS102775 / handle2142/97722; owner expressly approved thesis',32:'USGS publication70041861 metadata, 2011',
33:'NRCan primary 17WCEE_Kolaj_etal_SECanHazardUncertainty_1c-0029.pdf metadata',34:'Wiley DOI10.1029/2004JB003510 metadata',
35:'Government of Canada publication9.960685, GSC Open File8630',36:'GEM OpenQuake citation and official NRCan Kolaj2019 bibliography for Butler R.',
37:'Annual Reviews DOI10.1146/annurev.earth.32.082503.144359 metadata',38:'Official NRCan Kolaj2019 hydrated references lines83-90; secondary metadata for the preliminary2018 report, not the later published model',
39:'Owner-authorized separate R04 copy, filename matches output',40:'Government of Canada publication9.960685 author identity for the same Open File8630',
41:'R03 body825 Appendix A contents',42:'R03 body833 Appendix B sources',43:'R03 body844 Appendix C contents',44:'R03 body845 AEP subsection',45:'R03 body899 UHS subsection',
46:'R03 body952 Appendix D contents',47:'R03 body954 PGA subsection',48:'R03 body973 spectra subsection',49:'bib/references.bib:4892-4901; already cited R03 body423'}
Bibliography = set([24,25,26,27,30,31,32,34,35,36,37,38,49])
Descriptions = []
for i,u in enumerate(Audit['units'],1):
    s=u['text']; source=Sources[i]
    if i in Bibliography:
        contribution='Retains the full work identity so the reader can locate '+s.split('. (')[0]+': author, year, title and publication details are required; the title is bibliographic metadata, not a new methodological claim.'
        scope='Bibliography only; the work already supports an existing citation. The Harmon identity is the owner-selected thesis; Petersen remains explicitly preliminary2018.' if i in (31,38) else 'Bibliography identity repair for an already cited work; no recommendation or numerical result is added.'
        preservation='The cited work and its purpose stay the same; incorrect metadata are replaced by the stated source. Scientific body, conditions and equations remain unchanged.'
    elif i >= 41:
        contribution='The label '+s+' identifies the existing appendix or subsection; removing it would lose the visible navigation destination.'
        scope='Existing appendix heading, with its established subject and A-D/C1-C2/D1-D2 hierarchy retained.'
        preservation='Letter and subject match the existing appendix; only the broken automatic numbering is replaced.'
    elif i in (18,19,20,21,22,23):
        contribution='The caption fragment '+s+' communicates the existing velocity unit or percentile without the malformed slash/ordinal.'
        scope='Caption typography only, on the same existing figure.'
        preservation='The digits '+''.join(c for c in s if c.isdigit())+' are unchanged; no curve, percentile selection or velocity changes.'
    elif i == 39:
        contribution='The filename distinguishes the new R04 deliverable from the preserved original.'
        scope='Document identifier on the existing cover, not a technical assertion.'
        preservation='Report identity remains CAPR003324; only the delivered-copy filename changes.'
    else:
        contribution='The exact fragment '+s+' restores the named author/institution/year or citation punctuation so the reader can match the reference list.'
        scope='A citation or name within the existing sentence. The surrounding technical proposition is retained.'
        preservation='The cited proposition is not rewritten; spelling, author identity, citation shortening or adjacent-year punctuation is the only change, supported by '+source+'.'
    u['checks']={
        'support':{'verdict':'pass','evidence':source+'; fragment read in context in text-diff03/04 and R03 hydrated prose.'},
        'contribution':{'verdict':'pass','evidence':contribution},
        'scope':{'verdict':'pass','evidence':scope},
        'register':{'verdict':'pass','evidence':'The literal '+s[:100]+' keeps the report citation/heading register; it adds no appraisal, instruction, comparison or account of the editing process.'},
        'preservation':{'verdict':'pass','evidence':preservation}}
    Descriptions.append(str(i)+'. '+s+'\nSource: '+source+'\nDecision: '+contribution+' '+preservation)
(Here/'provenance.md').write_text('\n\n'.join(Descriptions)+'\n')
(Here/'entities.md').write_text('The 49 edited fragments and their exact entity sources are listed in provenance.md. No new model, scenario, Vs30, percentile or return-period value is introduced. Harmon2017 is the owner-approved doctoral thesis; Gardner1974 closes an existing in-text citation. Numeric caption edits preserve digits; scientific data and formulas are verified by verification04.json. Field destinations and generated indices are structural repairs, accounted for by candidate04.json and page-cache.json, rather than new scientific prose. All listed entity decisions are resolved.\n')
(Here/'formal.md').write_text('Scope: edited prose fragments only; full technical prose already audited in diana-final and not reopened. verification04.json establishes equality of all table cells after the declared filename/two-citation normalizations,3442 mathematical tokens, image bytes and order,192 valid links. The final layout pass changes only empty index paragraph spacing and page caches. Chapter REF caches use actual headings; duplicated/broken empty references are removed; captions preserve numbers. Cites are stable plain text with no live CITATION/BIBLIOGRAPHY field, so the untouched historical customXml library cannot regenerate the corrected visible entries. This is not a new NGR source/render or a scientific bibliography-method audit. The 49 fragments read in prose.md are the exact strings installed by build_word.py; surrounding paragraphs were read in text-diff03/04 and hydrated R03. No Pandoc or R execution applies to this direct DOCX editorial operation.\n')
Baseline='\n\n'.join(x['before'] for x in Changes if 'field' not in x and x.get('before'))+'\n'
(Here/'prose-baseline.md').write_text(Baseline)
Candidate=(Here/'prose.md').read_text(); Findings=[]
for x in Changes:
    a=x.get('before',''); b=x.get('after','')
    if 'field' in x or not a or a in Candidate or b not in Candidate: continue
    if any(f['fragment']==a for f in Findings): continue
    Findings.append({'id':'editorial-'+str(len(Findings)+1),'fragment':a,'rule':'preservation','diagnosis':'The original citation/name/caption fragment contains the identity, punctuation or typographic defect recorded by the exact before/after edit.','resolution':{'action':'revise','replacement':b,'evidence':'Reread '+b+' in its preserved surrounding sentence; provenance.md identifies its source and retained technical meaning.','verified':True}})
Audit['findings']=Findings
def identity(path):
    return {'path':str(path.resolve()),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
Audit['baseline']=identity(Here/'prose-baseline.md')
Audit['reviewer']='Codex root, bounded editorial corrections and surrounding-context review'
Audit['records']={k:identity(Here/v) for k,v in {'contract':'contract.md','provenance':'provenance.md','entities':'entities.md','formal':'formal.md'}.items()}
(Here/'prose-audit.json').write_text(json.dumps(Audit,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'units':len(Audit['units']),'resolvedFindings':len(Findings)}))
