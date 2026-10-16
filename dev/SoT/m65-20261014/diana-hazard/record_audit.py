"""Record the sentence-level judgments made for the computed replacement text."""
from hashlib import sha256
import json
from pathlib import Path

Folder = Path(__file__).resolve().parent
Candidate = Folder / "prose-candidate.md"
assert Candidate.read_text().isascii()
Audit = json.loads((Folder / "prose-audit.json").read_text())
Audit["reviewer"] = "/root"
for k, s in {"contract": "WRITING-CONTRACT.md", "provenance": "PROVENANCE.md", "entities": "prose-entities.txt", "formal": "PROSE-FORMAL.md"}.items():
    Audit["records"][k] = {"path": s, "sha256": sha256((Folder / s).read_bytes()).hexdigest()}
Judgments = [
    ["P1: submit.log line1 explicitly identifies Engine3.26.2; original body24/543/786 contain the older versions.",
     "The value identifies the implementation that produced the replacement results; removing it leaves the old engine claim.",
     "Execution provenance for the requested Hazard update, not a new scientific parameter.",
     "Numeric version only; Engine is an internal transfer heading and adds no promotion or interpretation.",
     "Only the version changes in the three existing sentences; PSHA scope, conditions and citations remain."],
    ["P2: independent RDS query returned SaF0.3123115g at CFD/M2V4D/Vs220/T0/TR10000/mean; formatC gives0.312.",
     "This is the mean PGA required by the existing TMF design-event sentences.",
     "Same site,Vs30,event and mean statistic as the existing paragraphs27/672/788.",
     "The label distinguishes mean from P84; the value is factual and contains no adequacy claim.",
     "Three-decimal precision and g units in the surrounding original sentences are retained; replaces0.395 only."],
    ["P3: independent RDS query returned SaF0.4423981g at the same TR10000 selection,p0.84; formatC gives0.442.",
     "This is the84th-percentile PGA paired with the mean for the same TMF event.",
     "P84 is a transfer key for the original84th percentile, with no confusion with P50 or the mean.",
     "Numeric result and descriptive mapping label; no statement of confidence adequacy.",
     "Retains the original84th-percentile wording and g context, replacing0.491."],
    ["P4: RDS query gives SaF0.1587537g at TR2500,mean,Vs220,T0; formatting gives0.159.",
     "The impoundments and stockpiles require their distinct mean PGA; the TMF number cannot substitute for it.",
     "Owner accepted the2475/2500 correspondence; original2475 labels stay in Diana.",
     "Factual numeric value; no assertion that the two return-period labels are mathematically identical.",
     "Replaces0.157 while preserving facilities, event label, units and precision."],
    ["P5: RDS query gives SaF0.2287538g at TR2500,p0.84,Vs220,T0; formatting gives0.229.",
     "Supplies the upper percentile paired with the stockpile/impoundment mean.",
     "Same target population asP4, with the explicit84th percentile; no Vs800 or cm/s2 product is used.",
     "Numeric result without evaluative language; P84 label is resolved in the ledger.",
     "Replaces0.198 and keeps the existing84th percentile annotation; no new design criterion."],
    ["P6: site.results.qmd line17 states direct logic-tree plus ST20 at reference760m/s conditioned by the PGA of the same realization; UHS.Vref verifies760.",
     "Both branches and the conditioning explain why the replacement design UHS differ from the old direct-only description.",
     "Describes the already validated model, within the existing site-response paragraphs; adds no stratigraphic calculation.",
     "Declarative method statement. Each refers to evaluated conditions from the source, not a universal site claim.",
     "Preserves the source method and its realization-level condition; replaces only the incompatible old amplification description."],
    ["P7/P8: the owner selected full direct curves; exported CSVs feed AEP. P6 supports the mixed design UHS in the second sentence.",
     "The first sentence identifies the curve product; the second prevents readers equating it with the tabulated design-mixture ordinates.",
     "This is the exact distinction requested in the AEP answer; it does not interpolate or extrapolate design points into curves.",
     "Two declarative method sentences, no instructions or unjustified comparison. Repetition ofP6 occurs at a separate existing method location.",
     "Retains all conditions ofP6 and the owner's direct-curve choice; it changes no probability, grid or statistical definition."],
    ["P9: R computed project/NRC ratios on the81 common Vs/TR/period rows; rounded extrema0.70/1.30 follow from the auditedUHS and officialNBC2020 response.",
     "The ratio range replaces the obsolete good-agreement/reliability assertion with the measured comparison the figure presents.",
     "Bounded to the periods and site conditions compared in8-1..3; does not generalize to all Canada, P84 or noncommon periods.",
     "Owner-authorized comparison; no adequacy, causal explanation or claim of reliability remains in the replaced sentence.",
     "Preserves PSHA/NRC2020 identity and mean comparison context while updating the quantitative relation; citations around the sentence stay."],
    ["P10/P11: independently queried joint maxima giveMw4.875–5.125,R18.75–31.25km; summed marginal maxima giveMw5.125–6.875 for the five originalTRs.",
     "The first sentence describes the dominant joint bins visible in deaggregation; the second preserves information on magnitude peaks that differ after summing distances.",
     "PGA deaggregation only. Bin centers are identified explicitly and are not the design magnitudes used in Newmark.",
     "Largest is the actual argmax under the authorized update of the controlling-sources paragraph; no unsupported background/fault classification is added.",
     "Corrects the obsolete magnitude/distance ranges while preserving multiple magnitudes and the original final fault-source sentence outside this fragment."],
    ["P12: the official response fields enumeratePGA and nine spectral periods0.05,0.1,0.2,0.3,0.5,1,2,5,10seconds.",
     "The listing updates what the official tool provides; omitting it would retain the incomplete old period list.",
     "This paragraph describes service availability; comparison plots use only the common model grid through5s, as recorded inP9.",
     "Structural periods is the original paragraph649 opening; numbers are formatted response field identities, not invented measurements.",
     "Keeps PGA separate from positive spectral periods and retains seconds; adds only periods actually returned byNBC2020."]
]
Rules = ["support", "contribution", "scope", "register", "preservation"]
assert len(Audit["units"]) == 2 * len(Judgments)
for i, Row in enumerate(Judgments):
    for n in [2*i, 2*i+1]:
        for k, s in zip(Rules, Row):
            Audit["units"][n]["checks"][k] = {"verdict": "pass", "evidence": s}
Audit["baseline"] = {"path": "prose-candidate.md", "sha256": sha256(Candidate.read_bytes()).hexdigest()}
Audit["findings"] = [
    {"id": "F1", "fragment": "at each condition", "rule": "register", "diagnosis": "Entity checker flags each as a potential unsupported quantifier.",
     "resolution": {"action": "retain", "evidence": "P6 limits each to evaluated site conditions and preserves the same wording and method of site.results.qmd:17; removing it loses the condition-specific direct evaluation.", "verified": True}},
    {"id": "F2", "fragment": "largest joint contributions", "rule": "support", "diagnosis": "A maximum claim requires observed support and authorized scope.",
     "resolution": {"action": "retain", "evidence": "P10 independently reads the RMw joint argmax for the five original return periods. The owner authorized updating this existing controlling-hazard paragraph; bin centers explicitly prevent treating these as Newmark design magnitudes.", "verified": True}},
    {"id": "F3", "fragment": "for the periods and site conditions compared", "rule": "scope", "diagnosis": "The NRC ratio could be misread as applying outside the plotted intersection.",
     "resolution": {"action": "retain", "evidence": "P9 enumerates the exact81 comparison rows at threeVs,threeTR,ninecommonperiods; retaining this clause bounds the ratio to figures8-1..3 and avoids a general adequacy claim.", "verified": True}}
]
(Folder / "prose-audit.json").write_text(json.dumps(Audit, indent=2)+"\n")
