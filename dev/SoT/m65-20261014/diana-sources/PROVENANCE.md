# Procedencia del cambio editorial acotado

La unidad candidata es el texto de los párrafos que cambian, expandido por knitr en candidate.md; no es un nuevo master. La revisión preserva el resto del memo ya aprobado. Los números que aparecen en este registro y en candidate.md son resultados del knit; los archivos de producto conservan las expresiones R.

| Oración | Tipo | Pasaje leído | Tratamiento |
| --- | --- | --- | --- |
| The reference magnitudes assigned… | factual | data/newmark/PROCEDENCIA.md:7–12, magnitude-map.csv:1–10 y Mw.gmdp en ambos contratos | Mapa idéntico copiado a data/newmark; unión por source con path.products de los contratos. No se deduce Mw del nombre del archivo. |
| Within each demand… | methodological | PROCEDENCIA.md:7–12 y contratos M55/M65 completos | El reparto es por demanda, no por material; se limita expresamente a esa demanda. |
| The Newmark permanent displacement… (memo y resumen) | methodological | _local/gmdp.memo.en.qmd:53; _results/dn.results.qmd:7 | Sin cambios; conserva la definición editada por Diana. |
| The Dn(ky) curves relate… (memo y resumen) | methodological | mismas líneas; ambos contratos: NS, subduction y Dn_weights; PROCEDENCIA.md:7–12 | Sólo se sustituye la magnitud única por la magnitud asignada a cada demanda. Modelos, realizaciones y fractiles intactos. |
| The horizontal pseudostatic coefficient… | methodological | _local/gmdp.memo.en.qmd:53 | Sin cambios; umbrales interpolados desde DAMAGE.CUTS de setup.R:90–97, referencias conservadas. |
| where mu and sigma… (memo y capítulo) | methodological | _local/gmdp.memo.en.qmd:200 y _chapters/dn.model.md:7 | Sin cambios; define los parámetros de la ecuación previa. |
| Some source formulations… (ambas copias) | methodological | mismas líneas | Sin cambios; conserva el alcance de la rama positiva aprobado previamente. No se introduce la variante de texto aún no integrada del scaffold externo. |
| In every formulation… (ambas copias) | methodological | mismas líneas; PROCEDENCIA.md:7–12 | Conserva unidades, Arias y geometrías; sólo corrige el alcance de la magnitud. |
| The published form… (ambas copias) | composition | referencias existentes de las mismas líneas y anchors del memo | Conserva Section/Appendix según el caller. |
| The performance-based seismic coefficient is defined by (ambas copias) | composition | continuidad inmediata con eq-kmax-criterion en las fuentes | Se conserva como introducción de la fórmula siguiente; el extracto de auditoría no reordena el producto. |
| The Newmark displacements were computed… | methodological | _results/dn.inputs.qmd:3–12, contratos M55/M65 completos | Sin cambios: familia, rama cortical y pesos iguales. |
| Every formulation received… | factual | _results/dn.inputs.qmd:8–12, contratos M55/M65 completos, PROCEDENCIA.md:7–12 | Misma selección completa de datos; cambia únicamente la afirmación de magnitud constante. Los conteos de TR, alturas y materiales se derivan de esos contratos por R. |
| Ecuación kh | methodological | scripts/tbl/kh.R:31, units.Kh=ratio observado en kmaxTable; _chapters/dn.model.md:14–20 | El factor 100 expresa el porcentaje ya declarado. No cambia ningún coeficiente ni producto numérico. |

## Entidades y registro

El gate reportó cero nombres y cero siglas sin fuente. Los dos números 0.40 y 2.50 son las representaciones con dos decimales que .fmt aplica a 0.4 y 2.5 de DaH.gmdp, leídos en ambos contratos; no son datos nuevos. Se conservan las marcas each/Every: cada demanda tiene una sola corrida de origen y sus magnitudes se aplican a las combinaciones de esa corrida. El every de las unidades ya estaba aprobado; no se amplía su alcance. English ASCII comprobado por checkCandidate.R.

## Diferencia y límites

Se excluyen de esta revisión las tablas y figuras del DOCX de Diana, que se modifican en una misión paralela. Aquí no se cambia su original ni se afirma haber corregido sus fórmulas. No se modifica la fuente española, no se corrige ciencia adicional, ni se valida de nuevo la literatura de los párrafos heredados. La autoridad de estos últimos es el texto de proyecto ya aprobado; las proposiciones nuevas se apoyan sólo en la procedencia auditada.
