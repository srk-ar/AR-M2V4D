## Objective

Hijo B (reconciliación y mapeo): a partir de los dos inventarios independientes A1 y A2 y del texto base que la otra autora recibió, producir la lista única de ediciones de gramática y fluidez de Diana Reyes sobre el capítulo «Slope Design Parameters», decidir para cada una si se porta tal cual, se porta corregida o no se porta, y ubicar cada edición portable en archivo y línea de las fuentes actuales del proyecto con la oración propuesta. Propuesta para el propietario; nada se aplica.

## Rulings

- Contexto validado por el propietario (2026-10-15): el DOCX `docx/CAPR003324_Crawford_SeismicHazard_Final.docx` es el informe de Diana Reyes, que incorporó nuestro texto viejo (el memo del 2026-09-24, con la fórmula de T_s con H_s en el numerador, hoy corregida) y resultados viejos; ella editó la gramática y pide que al ajustar el capítulo no haya que rehacer su edición. Objetivo práctico: que nuestras fuentes incorporen sus mejoras de redacción, para regenerar el capítulo con fórmulas y resultados nuevos sin perderlas.
- Insumos, leer completos: `docx/CAPR003324_Crawford_SeismicHazard_Final.slope-design-parameters.md` (capítulo editado por ella, convertido con pdf2md, sin imágenes); `dev/SoT/m65-20261014/docx-review/base/gmdp.memo.en.md` (texto base que ella recibió: nuestro memo `docx/gmdp.memo.en.docx` del 2026-09-24 convertido con pdf2md; su manifiesto al lado); `dev/SoT/m65-20261014/docx-review/A1/EDITS.md`, `A1/SUMMARY.md`, `A2/EDITS.md`, `A2/SUMMARY.md` (inventarios independientes, con ids E/S/N/X propios de cada uno); fuentes actuales (inglés): `_chapters/deq.criteria.md`, `_chapters/deq.kmax.md`, `_chapters/ts.model.md`, `_chapters/dn.ensemble.md`, `_chapters/dn.model.md`, `_chapters/dn.uncertainty.md`, `_chapters/dn.appendix.md`, `_results/dn.inputs.qmd`, `_results/dn.results.qmd`, `_results/kmax.results.qmd`, `_results/ts.results.qmd`, `_local/gmdp.memo.en.qmd`, `_captions/tbl.Ts.md`; ensamblado del memo en `_local/gmdp.memo.en.qmd` y del Word del informe en `_docx/sdc.qmd` (líneas 89–169) y `_docx/gmdp.qmd` (44–80).
- Método: la base de comparación es el memo convertido, no las fuentes actuales; una diferencia entre el DOCX y el memo es edición de ella; una diferencia entre el memo y las fuentes actuales es reescritura nuestra posterior y no se porta. Reconciliar A1 y A2: unir sus registros por oración (citar los ids de ambos), resolver discrepancias leyendo los textos, y no inventar ediciones que ninguno de los dos ni la lectura directa respalden.
- Decisión por edición, con estas clases exactas: `portar` (gramática, fluidez, terminología, puntuación o reordenamiento correctos), `portar corregida` (la intención es buena pero su redacción introduce un error; proponer la oración correcta), `no portar: contenido` (agrega, quita o redefine una afirmación técnica; se lista para el propietario), `no portar: números` (cambia rótulos o valores, p. ej. 475/2475 frente a 500/2500 del memo), `no portar: artefacto` (conversión, numeración de Word, estilo de cita), `superada` (nuestra fuente actual ya cambió esa oración por una reescritura posterior; indicar si la mejora de ella todavía aplica a la nueva oración y, si aplica, proponerla como `portar` sobre la oración nueva).
- Ubicación: para cada edición `portar` o `portar corregida`, el archivo fuente actual y la línea, la oración actual textual y la oración propuesta final en inglés, lista para pegar. Si la oración vive en `_local/gmdp.memo.en.qmd` o en un `_results/*.qmd`, indicarlo igual. Respetar el marcado Quarto de la fuente (citas `[@Clave]`, referencias `@eq-…`, matemática en `$…$`): la propuesta reemplaza sólo palabras, nunca ecuaciones, números, citas ni referencias.
- Sólo lectura fuera del write root `dev/SoT/m65-20261014/docx-review/B/`. Sin Git. Sin cambios en fuentes, inventarios A1/A2, docx/ ni scaffold. No consultar a otros agentes.
- Entregables en el write root: `MAP.md` (tabla única por archivo fuente en el orden del Word: id B, ids A1/A2, archivo:línea, oración base del memo, oración de Diana, oración actual nuestra, decisión, oración propuesta, nota), `PATCH.md` (por archivo, bloques «actual → propuesta» sólo de las decisiones portar y portar corregida, en orden de línea), `DECISIONES-PROPIETARIO.md` (las `no portar: contenido` y `no portar: números`, con la oración de ella, la nuestra y qué habría que decidir) y `SUMMARY.md` (conteos por decisión y por archivo, discrepancias entre A1 y A2 y cómo se resolvieron). Terminar con un informe breve al coordinador con los cuatro archivos, sus tamaños y los conteos.
- Antes de cerrar, reescribir este STATE.md con el estado actual y validarlo con `python3 -B ~/.claude/lifecycle/continuity.py --root . --state dev/SoT/m65-20261014/docx-review/B/STATE.md`. No escribir DONE: dejar ACTIVE con el Next «Entregar el informe final al coordinador».

## Evidence and no-repeat

- 2026-10-15: locator DELEGATION validado contra `dev/SoT/m65-20261014/STATE.md` («## Delegations», mission y state idénticos; revalidado tras un cambio del archivo del coordinador). Skills `continuity` y `writing` traídas con el comando del catálogo (`unchanged`) y leídas (`writing`: SKILL.md y references/cases.md).
- Insumos leídos completos en esta sesión (sha256 16, bytes): DOCX editado `a1039d4829249121` 30789; memo base convertido `f02d6d0a5712f1f4` 106060; A1/EDITS `6f06854cc56a9ac0` 67763; A1/SUMMARY `6d16441a746e7177` 24231; A2/EDITS `d8e5228bb7287726` 83044; A2/SUMMARY `4b1f86453e837dbc` 8875; deq.criteria `4cba543a0280505e`; deq.kmax `385c18cb8f839fc9`; ts.model `58de3be2a981e858` 6406; dn.ensemble `b8fd331e9dda05ad`; dn.model `04961b5912ccf7c7`; dn.uncertainty `d62795bf18df6626`; dn.appendix `c742fc249db84b6b`; dn.inputs `8fc427c0994b5526`; dn.results `61ce786f89507979`; kmax.results `90bfd1474ac3c260`; ts.results `fbd266ec8ce58fa5`; _local/gmdp.memo.en.qmd `7e0a6a04822551a4`; _captions/tbl.Ts.md `5e3762fd1c18cf32`; _docx/sdc.qmd `90a33867602334e7`; _docx/gmdp.qmd `017c66d8c98c51fa`; además _local/tbl.Ts.md, _local/fig.kh.md, _local/tbl.kh.md, _captions/fig.kh.md, _captions/tbl.kh.md, _captions/tbl.kh.sites.md, _local/gmdp.memo.scenarios.csv y _chapters/notation.md:105,109.
- Comparación directa DOCX↔memo base por oración (script en el scratchpad de la sesión, sin escritura en el proyecto): confirma la cobertura de A1 y A2 y agrega una edición de números que ninguno registró (Tabla 10-1: $a_1$ redondeado de 3.6559, 3.3699, 3.1162, 3.1052, 2.9759 a 3.656, 3.370, 3.116, 3.105, 2.976).

## Effects

none yet

## Blocker

none

## Next

NEXT-ID {"action":"Leer completos los insumos, reconciliar A1 y A2 contra el memo base, decidir y ubicar cada edición, escribir MAP.md, PATCH.md, DECISIONES-PROPIETARIO.md y SUMMARY.md en dev/SoT/m65-20261014/docx-review/B/, reescribir y validar este estado, e informar al coordinador.","id":"m65-20261014.docx-review.B.v1"}

## Status

ACTIVE
