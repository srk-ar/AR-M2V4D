"""Record the completed clause review of the bounded Diana revision."""
from pathlib import Path
import hashlib
import json
import re

Root = Path(__file__).parent
Audit = json.loads((Root/'prose-audit.json').read_text())
Units = Audit['units']
Memo = '/private/tmp/diana-audit-root.25nVLM/memo/document.md'
Report = '/private/tmp/diana-audit-root.25nVLM/report/document.md'
Diana = '/private/tmp/diana-audit-root.25nVLM/r02/document.md'
Appendix = str((Root/'original-appendix.txt').resolve())
Locations = json.loads((Root/'prose-locations.json').read_text())
Judgments = {
0:(Report+':81; '+Memo+':400-446','The first sentence defines Dn as the performance measure; the second links ky to displacement and identifies the five formulations, demand-specific magnitude, 300 realizations and q=1-pe. Removing either loses the meaning or the computational basis of the slope results.','Executive overview of the actual five-model PSHA computation; no MCE result or cross-material range is imported.','Direct methodological description copied from the rendered executive block; each restricts the statement to geometry-material-demand combinations.','Replaces the obsolete singular empirical method. Dn, ky, all five codes, the realization count and the fractile relation match the full report.'),
1:(Diana+':1382; '+Memo+':400-446,896,930','Sentence one defines displacement; sentence two identifies the ensemble, magnitudes and realizations; sentence three defines kh, the four thresholds and where the results are tabulated. The corrected BM19 citation connects that model to its actual source.','Chapter 10 retains Diana wording and selected geometries; the correction is citation identity, not a new method or editorial rewrite.','Original prose and parenthetical Word citations retained as requested; no new evaluation of model adequacy is added.','Only the BM19 author/year is corrected here, to Bray and Macedo 2019. The surrounding quantities, units, thresholds and citations remain unchanged.'),
2:(Diana+':1467; '+Memo+':400-428','The clauses define lognormal parameters and conditioning, units, Arias-intensity derivation, magnitude allocation, shared magnitude within demand and the Appendix E formula location. Each prevents a different misreading of the ensuing criterion.','The owner selected PSHA: 5.5 through 2500 years and 6.5 for 5000/10000 remain, while the MCE mention is removed.','Every formulation is bounded to the declared active set, not all published models. The positive-branch wording is preserved from Diana.','Only the excluded MCE demand is removed; logarithmic conditioning, g/m/s/s units and magnitude allocation remain intact.'),
3:(Appendix+':990','The heading locates the restored coefficient appendix referenced from chapter 10.','Existing appendix scope.','Document title, no scientific claim.','Restores visibility without changing the chapter identity.'),
4:(Appendix+':992; '+Memo+':101-147','The caption identifies the shear-stiffness parameter table and its gravel, sand and fines families.','Same material families as the transferred table.','Short object label; E-1 is local numbering.','Retains the caption meaning while repairing its missing hyphen; numeric table content is separately checked.'),
5:(Memo+':832; '+Appendix+':996','The subsection heading distinguishes model equations from coefficient result tables.','Newmark formulations only.','Technical heading, no new entity.','Restores E1 with explicit numbering, avoiding the broken inherited heading field.'),
6:(Memo+':834; '+Appendix+':997','Sentence one distinguishes three rigid and two flexible active models; sentence two explains why both BM equations are displayed; sentence three identifies the extra Ts/spectral predictor in flexible models. All three are needed to read the formula list without treating both BM branches as active.','Five active formulations, with one BM branch selected by tectonic context.','Reproduces describes the equations physically supplied in the appendix, not the agent work process; retained from Diana and the memo.','Preserves counts, model families and spectral-period relationship.'),
7:(Memo+':836; '+Appendix+':998','The heading groups AM88, JB07 and SR08 under the rigid-block idealization.','Rigid family only.','Classification label.','Same grouping as the source.'),
8:(Memo+':838; '+Appendix+':999','The sentence identifies AM88 and the capped yield/PGA ratio that keeps the logarithm in its domain.','AM88 domain limit only.','Factual model description with existing parenthetical citation.','Retains r-star and 0.9999; removes a duplicate citation and dangling footnote, whose substantive AM88 limit remains below.'),
10:(Memo+':845; '+Appendix+':1001','The first sentence defines Arias intensity units, deterministic mapping from each PGA realization and propagated variability; the second identifies the JB07 predictors. Removing the first would imply an independent random IA draw.','JB07 and SR08 input construction, then JB07 equation.','Single is the sourced one-to-one PGA-to-IA relation, not an unsupported uniqueness claim.','Preserves IA m/s, PGA g and ky/PGA; duplicated citation removed without losing its source.'),
12:(Memo+':852; '+Appendix+':1003','The sentence defines SR08 ratio r and its PGA/IA predictors before the equation.','SR08 only.','Method statement, no ranking of models.','Retains r=ky/PGA and both intensity measures.'),
14:(Memo+':860; '+Appendix+':1005','The three sentences identify the AM88 exception, the all-grid capped plateau condition, and the physical-branch solve for Da above that plateau. The inequality and target condition are necessary limits.','Only AM88 full plateaus under the stated sampled-PGA condition.','All is qualified by may satisfy and the explicit grid inequality; the negative contrast rules out two technically incorrect inversions.','Preserves rmax, D0s, sampled PGA and Da>D0s; local reference E1-1 replaces the source equation number.'),
16:(Memo+':864; '+Appendix+':1007','The derivative and residual cancellation establish unique root recovery; the second sentence states acceptance and rejection conditions that bound the recovery.','No general recovery for another model or a target below the plateau.','Unique and only are justified by the displayed strictly negative derivative and the explicit eligibility condition.','Preserves both rejection branches, exact-flatness condition and sampled-PGA evidence.'),
17:(Memo+':866; '+Appendix+':1008','The heading groups the dynamic-response formulations apart from rigid models.','Flexible-block family.','Classification label.','Retains the source model split.'),
18:(Memo+':868; '+Appendix+':1009','The first sentence describes the period-scaled spectral predictor; the second assigns 1.5Ts and Mw to BT07.','BT07 plus its flexible-family context.','No claim of comparative performance; existing citation style retained.','Preserves the 1.5 factor, Ts and Mw and the 2007 source; duplicate citation removed.'),
20:(Memo+':880; '+Appendix+':1011','The sentence identifies BM17 as the subduction-interface branch and assigns Sa(1.5Ts).','Displayed for the branch rule; it is not activated for this crustal project.','Existing parenthetical bibliographic wording preserved.','Preserves BM17, 2018 source and the 1.5Ts spectral ordinate.'),
22:(Memo+':896; '+Appendix+':1013','The sentence identifies BM19 as the shallow-crustal branch and assigns Sa(1.3Ts).','The active crustal BM branch, without claiming both branches run together.','Existing citation and factual tectonic scope.','Preserves the 2019 identity and 1.3Ts predictor.'),
24:(Memo+':912; '+Appendix+':1015','The heading introduces the model-combination rule after individual equations.','Ensemble definition.','Technical label.','Same source classification.'),
25:(Memo+':914; '+Appendix+':1016','The first sentence identifies five active models and the mutually exclusive BM branches; the second retains published predictors/dispersion and equal weighting with the chapter cross-reference.','Model-set selection, not deterministic hazard scope.','Never both is the explicit mutually exclusive branch rule, necessary to avoid a six-model interpretation.','Preserves five-model weights and both family definitions; section 10.1.3 is the local counterpart of memo 1.3.'),
26:(Appendix+':1017; '+Memo+':448','The heading distinguishes kmax in acceleration units from kh percentage tables.','Absolute coefficient section.','Descriptive heading.','Unit distinction retained.'),
27:(Appendix+':1018; '+Memo+':450-632','Sentence one identifies the three g-valued curves and their return periods; sentence two identifies cm/s2 tables and four limits; sentence three identifies the model sets.','Only probabilistic rows and plots at 500/2500/10000.','The object references let the reader distinguish the plotted unit from the tabular unit.','Legacy 475/2475 labels in the restored appendix are replaced from the memo 500/2500 labels, without interpolation; all five scenarios and three sets remain.'),
52:(Appendix+':1051; '+Memo+':636','The heading distinguishes percentage-of-PGA results from acceleration-unit results.','Normalized coefficient section.','Descriptive heading.','PGA normalization remains explicit.'),
53:(Appendix+':1052; '+Memo+':636-828; '+Diana+':1531-1563','Sentence one identifies per-scenario kh tables and four limits; sentence two specifies all three sets; sentence three locates the ensemble subset in the main chapter.','Only the 2500/10000 ensemble subset is attributed to table 10-2.','References are navigation for interpreting related tables, with no new scientific comparison.','Corrects the broken Table 102 reference to 10-2, retains the subset distinction and omits MCE.'),
}
for i,a,b in [(9,840,843),(11,847,850),(13,854,858),(15,862,862),(19,870,878),(21,882,894),(23,898,910)]:
    Judgments[i]=(f'{Memo}:{a}-{b}',f'The displayed equation {Units[i]["text"].splitlines()[-1]} supplies the mean/dispersion or AM88 inversion used by its preceding paragraph; each coefficient, exponent, branch boundary and sign is retained.','Equation from the rendered memo; no scientific recomputation.','Native Word mathematical notation, no prose evaluation.','Seven OMML formulas match the memo token strings exactly after removal of literal alignment ampersands; local E1 numbering replaces memo numbering.')
for i,n in [(28,1),(31,2),(34,3)]:
    Judgments[i]=(f'{Memo}:{450+(n-1)*6}-{455+(n-1)*6}; {Appendix}:{1020+(n-1)*4}',f'Figure E2-{n} identifies kmax in g, the corresponding return period, relative displacement and the five named scenarios and three sets. Both caption sentences are required to decode the plot.','Same scenario and demand cut as the exact imported PNG.','Object caption with source vocabulary; no inference about governing scenarios.','Preserves mean statistic, g unit, Da/H percentage and scenario identities; updates return-period label from the model.')
for i,n in [(30,1),(33,2),(36,3)]:
    Judgments[i]=(f'{Memo}:{973+n*2}',f'Note to figure E2-{n}: the first sentence maps color/line style to scenario/model family; the second defines all four shaded damage thresholds.','Legend applies to the adjacent coefficient figure.','A decoding key rather than a claim of model accuracy.','Colors, solid/short/long dash meanings and 0.1/0.4/1.0/2.5 percent thresholds remain those of the source.')
for i,n,a in [(37,1,496),(40,2,530),(43,3,564),(46,4,598),(49,5,632),(54,1,692),(57,2,726),(60,3,760),(63,4,794),(66,5,828)]:
    s='E2' if i<52 else 'E3'
    v=['S135','S50','S32','S27','S35'][n-1]
    Judgments[i]=(f'{Memo}:{a}',f'Table {s}-{n} caption identifies the {v} scenario, mean statistic, coefficient unit and 500/2500/10000-year rows; none can be omitted without ambiguity.','The MCE rows/caption clause are excluded under the explicit PSHA decision.','Concise table identity, not a prose retelling of values.','Scenario identity and coefficient unit match the transferred table; only probabilistic source rows are retained.')
for i,n in [(39,1),(42,2),(45,3),(48,4),(51,5)]:
    Judgments[i]=(f'{Memo}:{981+n*2}; {Appendix}:{1030+n*4}',f'Note to E2-{n}: sentence one defines ID/IDn; sentence two defines Ts and Vs30 with units; sentence three identifies arithmetic-mean columns and relative limits; sentence four distinguishes exceedance fractiles from mean values.','The scenario table retains all three model families; mean is not mislabeled P84.','Technical column definitions, without a performance conclusion.','Preserves s, m/s, percent, mean statistic and the q/pe distinction of the source.')
for i,n in [(56,1),(59,2),(62,3),(65,4),(68,5)]:
    Judgments[i]=(f'{Memo}:{999+n*2},428,993; {Appendix}:{1052+n*4}',f'Note to E3-{n}: sentence one defines demand/model labels; sentence two defines Ts/Vs30 units; sentence three defines the mean coefficient and its 100*kmax/PGA normalization.','Percent of the corresponding site-condition PGA, not raw acceleration or another Vs30.','Technical column definitions; no invented numerical result.','The stray comma after 100 is removed to match memo equation 14 and figure notes; all mathematical quantities and units remain unchanged.')
for i,x in enumerate(Units):
    if x['text']=='Notes:':
        Judgments[i]=(Appendix,'The Notes label separates the adjacent object caption from its units, columns or legend definitions.','Adjacent object only.','Conventional label retained from Diana.','No scientific statement or value introduced.')
assert set(Judgments)==set(range(len(Units)))
Ledger = ['# Sentence provenance and review scope','',
    'Source paths below identify the owner-named DOCX conversions. original-appendix.txt is a literal OOXML transcript of Diana original body paragraphs 990–1072, including the deleted text; it supplies editorial wording, not newly calculated results. prose-locations.json binds the delivered transcript to candidate06. The owner requested preservation of Diana wording and selected PSHA explicitly.','',
    '| Unit/sentence | Type | Text | Primary passage |','| --- | --- | --- | --- |']
for i,x in enumerate(Units):
    a,b,c,d,e = Judgments[i]
    for k,s in enumerate(re.split(r'(?<=[.!?])\s+(?=[A-Z])',x['text']),1):
        Ledger.append(f'| {i+1}.{k} | methodological | '+s.replace('|','\\|').replace('\n',' ')+' | '+a+' |')
    x['checks']={k:{'verdict':'pass','evidence':v} for k,v in zip(['support','contribution','scope','register','preservation'],[f'Provenance unit {i+1}, all sentence rows: '+a,b,c,d,e])}
Ledger += ['','## Entity diagnostics resolved',
    'E1 is Diana local appendix numbering: original body992 says Table E1 and body1000–1014 use E1 equation labels. It is not an invented model acronym. The second entities run has zero unsupported entities.',
    'The eight register flags are retained with their exact limits: each geometry/material/demand (memo 400–446); every active formulation and its units (memo 420); reproduces the supplied model equations (memo 834); single IA per PGA realization (memo 845); all grid points under the AM88 capped condition (memo 860); unique root from the negative derivative and only a fully capped AM88 plateau (memo 864); never both mutually exclusive BM branches (memo 914). No generalization beyond these passages is introduced.',
    'Native Word author/year citations and Unicode mathematical typography are retained under the owner instruction to preserve Diana wording and Word design. Existing awkward phrasing in the unchanged chapter introduction is not presented as a new grammatical edit; only its BM19 citation changes here.']
(Root/'provenance.md').write_text('\n'.join(Ledger)+'\n')
Baseline = Path('/private/tmp/diana-audit-root.25nVLM/r02/document.md').read_text()+'\n'+(Root/'original-appendix.txt').read_text()
(Root/'prose-baseline.md').write_text(Baseline)
Findings = [
 ('summary','Seismic coefficients for the Crawford project embankments were estimated using an empirical','scope','The singular empirical-method summary does not describe the active ensemble.','revise',Units[0]['text'],'Full report executive paragraph copied; ensemble, demand allocation and sample count retained.'),
 ('bm19','and BM19 (Bray, Macedo, & Travasauro, 2018)','support','The BM19 label points to the wrong paper.','revise','and BM19 (Bray & Macedo, 2019)','Memo896/930 and Diana bibliography1627 identify Bray and Macedo2019; surrounding model list and magnitudes reread unchanged.'),
 ('normalization','100,kmax/PGA(VS30)','preservation','A literal comma in the old appendix note obscures the multiplicative normalization.','remove',None,'Memo equation14 and figure note993 define multiplication by100. Revised E3 notes retain this coefficient and site-condition denominator.'),
 ('caption','Table E1: Shear Stiffness Parameters for Gravels, Sands, and Fines','register','The restored table label lacked its caption hyphen.','revise','Table E-1: Shear Stiffness Parameters for Gravels, Sands, and Fines','Caption and adjacent table reread; E-1 identifies the existing appendix table, no new result.'),
 ('scope','for return periods of 5,000 and 10,000 years and the MCE','scope','MCE demand conflicts with the explicit PSHA-only delivery.','revise','for return periods of 5,000 and 10,000 years','Owner selected the probabilistic scope; Mw6.5 and both return periods remain, MCE is excluded only from this copy.')]
Audit['findings']=[]
for i,f,r,d,a,v,e in Findings:
    assert f in Baseline, (i,f)
    OUT={'id':i,'fragment':f,'rule':r,'diagnosis':d,'resolution':{'action':a,'evidence':e,'verified':True}}
    if v is not None: OUT['resolution']['replacement']=v
    Audit['findings'].append(OUT)
def record(path):
    return {'path':str(path.resolve()),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
Audit['reviewer']='Codex root, clause-by-clause review against named rendered sources'
Audit['baseline']=record(Root/'prose-baseline.md')
for k,p in [('contract','contract.md'),('provenance','provenance.md'),('entities','entities-resolved.txt'),('formal','formal.md')]:
    Audit['records'][k]=record(Root/p)
(Root/'prose-audit.json').write_text(json.dumps(Audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'units':len(Units),'findings':len(Audit['findings'])}))
