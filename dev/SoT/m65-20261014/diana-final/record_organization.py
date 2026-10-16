"""Bind the three reviewed outline corrections to their actual evidence."""
from pathlib import Path
import hashlib
import json

Root = Path(__file__).parent
Audit = json.loads((Root/'organization-audit.json').read_text())
Judgments = [
    ['The complete outline at parsed07/document.md:611–631 lists chapters 1–11; 635–643 lists A–E, entailing eleven chapters and five appendices.',
     'The sentence gives the scope of the existing organizational outline; removing it loses the report-level count Diana supplied.',
     'Document structure only; no scientific value, method or scenario selection.',
     'The counts are supported by the explicit outline; comprises is a neutral description.',
     'The eleven chapters and the original sentence structure remain; four becomes five to include the restored E.'],
    ['parsed07/document.md:635–643 supplies the five appendix entries immediately following this sentence.',
     'This existing sentence introduces the appendix list after the eleven chapter descriptions. Its repeated count is retained to preserve Diana structure.',
     'The appendix-list scope stays separate from the chapter list.',
     'A factual list introduction, with no evaluation or new vocabulary.',
     'Only the outdated count changes; report, includes and appendices remain.'],
    ['Appendix E at parsed07/document.md:2252 onward contains the formulations and coefficient results also read in prose.md; this sentence identifies that content.',
     'Without this entry the organization list ends at D despite the restored and referenced E. It supplies the missing navigation item.',
     'Seismic coefficients only, under the probabilistic delivery chosen by the owner.',
     'Uses the existing Appendix naming and the supplied technical terms formulations and results.',
     'Adds no scientific claim, numeric result or new appendix; names the content already restored from the owner sources.']]
for x,y in zip(Audit['units'],Judgments):
    x['checks'] = {k:{'verdict':'pass','evidence':v} for k,v in zip(x['checks'],y)}
for k in Audit['records']:
    p = Root/('organization-entities.txt' if k == 'entities' else 'organization-evidence.md')
    Audit['records'][k] = {'path':str(p.resolve()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
Audit['reviewer'] = 'Codex root, organization paragraphs and source outline read in context'
Audit['findings'] = [{'id':'repeated-count','fragment':'The report also includes five appendices.','rule':'contribution','diagnosis':'The appendix count repeats the opening outline count.','resolution':{'action':'retain','evidence':'Retained in Diana original structural position: after eleven chapter descriptions it introduces the separate appendix list, whose new E entry must be accounted for. No repeated scientific conclusion.','verified':True}}]
p = Root/'organization.md'
Audit['baseline'] = {'path':str(p.resolve()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
(Root/'organization-audit.json').write_text(json.dumps(Audit,ensure_ascii=False,indent=2)+'\n')
