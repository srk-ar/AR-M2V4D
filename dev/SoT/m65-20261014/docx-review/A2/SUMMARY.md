# A2 · Resumen de la extracción

Resumen de `EDITS.md` (mismo directorio): ediciones del otro autor en la sección «Slope Design Parameters» del DOCX CAPR003324 frente a los textos fuente del proyecto. Insumos, método y citas textuales están en `EDITS.md`.

## Cifras

- Oraciones del DOCX inventariadas: 110 (prosa, leyendas y notas; sin encabezados, celdas de tabla ni ecuaciones).
- Con edición del otro autor: 38 oraciones en 36 registros (E01-E36), con 87 cambios.
- Sin edición del otro autor, con diferencias no portables: 38.
- Sin diferencias de redacción: 21.
- Sin contraparte: 13 oraciones (S01-S13).
- Diferencias clasificadas como «no es edición a portar»: 36 entradas (N01-N36).
- Contenido nuestro sin contraparte en la sección: 6 entradas (X01-X06).

## Conteo por clase

Cada cambio lleva una etiqueta; un registro puede tener varias.

| Clase | Cambios | Registros con la clase |
|---|---:|---:|
| gramática | 14 | 11 |
| fluidez | 18 | 16 |
| terminología | 25 | 18 |
| puntuación | 5 | 5 |
| reordenamiento | 3 | 3 |
| contenido | 22 | 15 |
| total | 87 | 36 |

«contenido» es una extensión de las cinco clases del estado: marca cambios que añaden, quitan o redefinen una afirmación técnica.

## Conteo por archivo fuente (orden de ensamblado del Word)

| Archivo | Registros | Cambios | Ids |
|---|---:|---:|---|
| `_results/ts.results.qmd` | 0 | 0 | - |
| `_results/dn.results.qmd` | 2 | 4 | E01, E02 |
| `_results/kmax.results.qmd` | 1 | 1 | E03 |
| `_chapters/deq.criteria.md` | 0 | 0 | - |
| `_chapters/deq.kmax.md` | 7 | 30 | E04, E05, E06, E07, E08, E09, E10 |
| `_chapters/ts.model.md` | 6 | 12 | E11, E12, E13, E14, E15, E16 |
| `_captions/tbl.Ts.md` | 0 | 0 | - |
| `_chapters/dn.ensemble.md` | 9 | 23 | E17, E18, E19, E20, E21, E22, E23, E24, E25 |
| `_chapters/dn.model.md` | 2 | 3 | E26, E27 |
| `_chapters/dn.uncertainty.md` | 7 | 10 | E28, E29, E30, E31, E32, E33, E34 |
| `_results/dn.inputs.qmd` | 0 | 0 | - |
| `_local/gmdp.memo.en.qmd` | 1 | 2 | E35 |
| `_local/tbl.Ts.md` | 1 | 2 | E36 |
| `_local/fig.kh.md` | 0 | 0 | - |
| total | 36 | 87 | |

Los tres últimos archivos están fuera de la lista nombrada en el estado: son el master y las leyendas del memo, usados como testigo (punto 2 del método de `EDITS.md`).

## Patrones de edición observados

- Terminología recurrente: «yield acceleration» por «yield coefficient» para $k_y$ (E17, E19); «support» por «range» (E25, E31, E34); «extended/extension» por «extrapolated/extrapolation» (E31, E34); «site-adjusted PGA» (E18, E27); «shallow crustal» (E28); «logarithmically spaced» (E25); «assessment» y «analysis» por «estimate» y «verification» (E05); «relative displacement thresholds» por «damage thresholds» (E08).
- Condensación de `_chapters/deq.kmax.md` (E04-E10): reestructura las oraciones, suprime ámbito y procedencia (E04, E06, E08) y omite el párrafo de NCHRP y Eurocode (X02); los deícticos que quedaban sin antecedente se reescriben (E04, E07).
- Supresión de la demanda MCE en el texto (E22, E23, E33) y en las figuras y tablas (X03).
- Adiciones o redefiniciones técnicas: E11, E12, E14, E15, E18, E19, E20, E23, E26 y E36, más las oraciones nuevas S01 y S03.
- Retoques de fluidez locales: E09, E13, E16, E21, E24, E27, E29, E32.
- Ortografía estadounidense: «analysed» por «analyzed» (E03, E35).
- Errores introducidos por la edición: E01, E04, E05, E06, E11, E17, E30, E35 (agramaticalidad con «induced by», mayúscula indebida, construcción no paralela, coordinación y punto faltantes, cláusula sin verbo, relación alterada con «such that», «an separate»).

Registros sin cambios de contenido ni errores introducidos: E02, E03, E07, E09, E10, E13, E16, E21, E24, E25, E27, E28, E29, E31, E32, E34 (16).

## No es edición a portar

36 entradas; detalle en la sección 3 de `EDITS.md`.

| Id | Motivo | Líneas DOCX |
|---|---|---|
| N01 | reescritura nuestra (memo) | 5 |
| N02 | reescritura nuestra (memo) | 7 |
| N03 | reescritura nuestra (memo) | 15 |
| N04 | ecuación; reescritura nuestra posterior | 21, 23 |
| N05 | contenido ya integrado en la fuente actual | 23 |
| N06 | reescritura nuestra posterior | 43 |
| N07 | reescritura nuestra (memo) | 43 |
| N08 | reescritura nuestra (memo) | 78 |
| N09 | reescritura nuestra (memo) | 84 |
| N10 | reescritura nuestra (memo) | 86 |
| N11 | reescritura nuestra (memo) | 92 |
| N12 | reescritura nuestra (memo) | 104 |
| N13 | reescritura nuestra (memo) | 106, 108 |
| N14 | reescritura nuestra (memo) | 112 |
| N15 | reescritura nuestra (memo) | 112 |
| N16 | reescritura nuestra (leyenda del memo) | 132, 143 |
| N17 | reescritura nuestra (leyenda del memo) | 179-199 |
| N18 | adaptación al documento receptor | 5, 76 |
| N19 | estructura del documento receptor | 3, 9, 11, 17, 74, 114, 143 |
| N20 | estilo de leyenda del documento receptor | 132, 179, 187, 195 |
| N21 | estructura del documento receptor | 66 |
| N22 | estilo de cita | 7, 13, 15, 19, 27, 43, 47, 55, 78, 80, 82, 84, 88, 108 |
| N23 | citas añadidas | 7 |
| N24 | cita: año distinto | 43, 55 |
| N25 | cita narrada | 15 |
| N26 | referencia cruzada (numeración de Word) | 7, 15, 82, 92, 106, 108, 112 |
| N27 | numeración de ecuaciones | 21-110 |
| N28 | ecuación: forma de presentación | 51-55 |
| N29 | artefactos de conversión en la matemática | 23, 49, 51, 53, 55, 60, 70, 84, 86, 90, 92, 94, 106, 179 |
| N30 | números renderizados | 5, 7, 92, 112, 183, 191, 199 |
| N31 | número: período de retorno | 112, 145, 150-168, 171, 179, 187 |
| N32 | formato perdido en la conversión | 7, 82, 84, 102, 143, 179-199 |
| N33 | conversión de guiones | 5, 19, 27, 55, 68, 76, 78, 82, 92, 96, 112 |
| N34 | conversión de la lista de notas | 134-143 |
| N35 | texto alternativo de imágenes | 177, 185, 193 |
| N36 | artefactos de anclas | 94, 110, 132, 171, 179, 187, 195 |

## Sin contraparte

13 oraciones del DOCX sin contraparte en `_chapters/*.md` ni `_results/*.qmd`:

- S01 (línea 51): tratamiento del nivel freático en el peso unitario.
- S02 (línea 66): remisión a la tabla de correlaciones del apéndice.
- S03 (línea 78): interpretación del factor de seguridad bajo el coeficiente aplicado.
- S04-S06 (línea 116): párrafo que presenta la Tabla 10-1 y la nomenclatura S<altura>.
- S07-S09 (línea 145): párrafo que presenta las Figuras 10-1 a 10-3 y la Tabla 10-2.
- S10-S13 (líneas 171 y 175): leyenda y notas de la Tabla 10-2, que es una tabla del otro autor.

## Contenido nuestro sin contraparte

- X01 `_local/gmdp.memo.en.qmd:64 (de _chapters/deq.criteria.md:1 y :9)`: El párrafo del marco OBE/SEE y la definición de MDE y MCE con que el memo abre «Seismic Design Criteria for Slopes» no aparece en la sección del DOCX. Supresión o traslado del otro autor; el DOCX puede tratarlo en otro capítulo que este extracto no contiene.
- X02 `_chapters/deq.kmax.md:3 (memo línea 68)`: El párrafo de NCHRP Report 611 y Eurocode 8 (tres oraciones) no aparece en el DOCX. Supresión del otro autor; deja sin antecedente «That objective» (E07).
- X03 `_local/gmdp.memo.en.qmd:229-266`: Las figuras y tablas del memo para $k_{max}$, para la demanda MCE y por escenario no aparecen; el DOCX pone sus Figuras 10-1 a 10-3 ($k_h$, tres períodos) y su Tabla 10-2.
- X04 `_chapters/dn.appendix.md (memo líneas 268-327)`: Las formulaciones están en el Apéndice E del DOCX, fuera del extracto; no se compararon.
- X05 `_results/dn.inputs.qmd:12`: Bloque del Word propio (_docx/gmdp.qmd:52) que el memo no incluye; bajo la inferencia del punto 2 del método, el otro autor no lo recibió.
- X06 `_chapters/deq.criteria.md:3-11 (salvo :9 primera oración)`: Capítulo del Word propio (_docx/sdc.qmd:91) que el memo no incluye.

## Puntos para el coordinador

1. La atribución de diferencias a nuestras propias reescrituras (N01-N17) se apoya en `_local/gmdp.memo.en.qmd` como testigo de la versión que recibió el otro autor. El memo no figura entre los insumos del estado; esa inferencia requiere validación.
2. N31: el DOCX rotula 475 y 2,475 años donde el memo y el texto alternativo de sus propias imágenes dicen 500 y 2,500. Es un cambio de números del otro autor, contrario a la premisa del estado.
3. N05: la oración «The height from the virtual apex ...» no aparece en el memo ni en ninguna fuente leída; su origen no se puede determinar con los archivos leídos. La fuente actual ya integra esa altura (`_chapters/ts.model.md:7`).
4. `_chapters/ts.model.md` cambió en disco durante la extracción (6044 a 6406 bytes; SHA-256 actual `58de3be2a981e858`). El inventario usa la versión actual.
5. El texto del DOCX declara $M_w$ = 7.0 (líneas 7 y 92); esta extracción no coteja ese valor con los datos.
6. Ocho registros llevan errores introducidos por la edición; no se pueden portar tal como están escritos.
