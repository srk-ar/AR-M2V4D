# Diana cumulative Word revision

## Product and surfaces
English cumulative copy of Diana's report, preserving its design and wording. The changed surfaces are the slope paragraph of the executive summary, the scope sentence in chapter 10, the existing Appendix E, and the image payloads in chapter 10. A separate comparison records cumulative changes from Diana's original.

The final review also corrects the BM19 citation in chapter 10 using the memo and Diana's existing 2019 bibliography entry. `prose.md` is the public pdf2md transcript of the three revised paragraphs and restored appendix prose, headings, equations and captions in document order; `prose-locations.json` binds each block to its converted line range. Numeric table grids and image payloads are covered by `verification06.json`, not duplicated as prose. Unchanged Hazard prose retains its previous audited transfer. Existing Word citation style, Unicode typography and English wording are preserved under the owner's explicit preservation instruction; this is not a new scaffold or translation.

## Reader and purpose
Diana and Alejandro need to review the updated probabilistic hazard and slope design parameters and see the changes in Word.

## Sources
| Source | Class | Access | Locations read |
| --- | --- | --- | --- |
| Diana original and R02 DOCX | project truth, owner's named editorial baseline | targeted text and OOXML | R02 document.md:160-185,1449-1488; body 989-1073 read in full, with tables and formulas |
| docx/gmdp.memo.en.docx | project truth, owner's rendered numerical source | targeted text and OOXML | memo document.md:400-495,832-943; body 43,81-83,88,95,102,109,116,130,137,144,151,158; formula nodes 170-186 |
| docx/docx.en.docx | project truth, owner's full rendered report | targeted read | report document.md:60-100; master and executive caller read |
| docx/hazard.diana.en.docx | project truth, transfer at Diana's approved Vs30 | previously verified transfer retained | audit-root/checkDelivery.py and primary numerical comparisons; no new hazard calculations |

## Unit of analysis
Each geometry-material-demand scenario remains separate. Hazard tables keep their Vs30 and statistical dimensions. The appendix retains rigid, flexible and ensemble sets, and reports only probabilistic demands.

## Language direction
The owner requested preserving Diana's improved English wording. Existing English sources supply the revised method statement; no translation is introduced.

## Length and structure
Retain Diana's chapter, appendix, equation and caption structure. Correct only inconsistencies and missing content needed for the requested cumulative delivery. Numeric cells and formula coefficients are transferred from the rendered source, not retyped or recalculated.

## Acceptor and delivery order
Alejandro receives one cumulative report and its comparison with the original. The final clarification supersedes delivery of the obsolete intermediate AVK comparison.

## Exclusions
Owner: "Conservar el alcance probabilístico de Diana". Exclude DSHA/MCE results and figures. Preserve original, AVK and R02 intact. No Git, deployment, scientific recalculation or blanket hydration. Preserve Diana's Vs30 and complete direct hazard curves as explicitly requested.

## Baseline and oracle
R02 SHA256 86dd4a5e7631e1abc5db539176fdf0da118904690a86be77a03187bd501a180e. Candidates are separate files under /private/tmp/diana-final-20261016. Verify exact source-cell and media transfer, appendix formula content, preserved unrelated XML, cumulative changes visible as Word revisions, comparison acceptance/rejection endpoints, and rendered affected pages. The baseline fails appendix visibility and revision attribution checks, as observed in audit-root/verification.json.
