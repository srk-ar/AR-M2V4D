# B · Resumen de la reconciliación

Reconciliación de los inventarios A1 y A2 contra el memo base del 2026-09-24: lista única de las ediciones de gramática y fluidez de Diana Reyes en «Slope Design Parameters», decisión por edición y ubicación en las fuentes actuales. Nada se aplicó; no se usó Git ni se consultó a otros agentes.

## Entregables

- `MAP.md`: tabla por archivo fuente, en el orden del Word, con las oraciones completas y una fila por edición.
- `PATCH.md`: 54 bloques «actual → propuesta» de las decisiones portar y portar corregida: 26 en fuentes del Word (`_chapters/`, `_results/`) y 28 en el memo (`_local/gmdp.memo.en.qmd` y `_local/tbl.Ts.md`).
- `DECISIONES-PROPIETARIO.md`: 16 puntos con las 41 ediciones de contenido y de números.
- `SUMMARY.md`: este resumen.

## Conteo por decisión

109 ediciones: 102 en 54 oraciones o elementos (párrafos, leyendas, celdas) y 7 transversales que agrupan diferencias repetidas (estilo de cita, numeración de Word, conversión, estructura y leyendas).

| Decisión | Ediciones | de ellas transversales |
|---|---:|---:|
| portar | 40 | 0 |
| portar corregida | 10 | 0 |
| no portar: contenido | 35 | 0 |
| no portar: números | 6 | 0 |
| no portar: artefacto | 16 | 7 |
| superada | 2 | 0 |
| **Total** | **109** | **7** |

Portables (portar y portar corregida): 50. De ellas, 9 se apoyan en oraciones que reescribimos después del memo y conservan su fragmento: B03a, B12a, B12b, B35a, B35b, B35c, B40a, B44a, B44b.

## Conteo por archivo fuente (orden del Word, después `_local/`)

| Archivo | portar | portar corregida | no portar: contenido | no portar: números | no portar: artefacto | superada | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| `_results/ts.results.qmd` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `_results/dn.results.qmd` | 2 | 1 | 2 | 0 | 0 | 0 | 5 |
| `_results/kmax.results.qmd` | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| `_chapters/deq.criteria.md` | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| `_chapters/deq.kmax.md` | 14 | 4 | 7 | 0 | 1 | 0 | 26 |
| `_chapters/ts.model.md` | 3 | 0 | 10 | 0 | 3 | 1 | 17 |
| `_captions/tbl.Ts.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `_chapters/dn.ensemble.md` | 10 | 2 | 11 | 0 | 1 | 1 | 25 |
| `_chapters/dn.model.md` | 1 | 1 | 1 | 0 | 0 | 0 | 3 |
| `_chapters/dn.uncertainty.md` | 7 | 1 | 1 | 1 | 0 | 0 | 10 |
| `_results/dn.inputs.qmd` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `_chapters/dn.appendix.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `_local/gmdp.memo.en.qmd` | 1 | 1 | 1 | 0 | 1 | 0 | 4 |
| `_local/tbl.Ts.md` | 1 | 0 | 1 | 1 | 0 | 0 | 3 |
| `_local/fig.kh.md` | 0 | 0 | 0 | 3 | 2 | 0 | 5 |
| `_local/tbl.kh.md` | 0 | 0 | 0 | 1 | 1 | 0 | 2 |
| Transversales | 0 | 0 | 0 | 0 | 7 | 0 | 7 |
| **Total** | **40** | **10** | **35** | **6** | **16** | **2** | **109** |

Sin ediciones: `_results/ts.results.qmd` (DOCX 5 repite la oración del memo), `_captions/tbl.Ts.md` (su leyenda sigue a la del memo, B46), `_results/dn.inputs.qmd` (el memo no lo incluye) y `_chapters/dn.appendix.md` (su Apéndice E queda fuera del capítulo convertido).

## Método aplicado

- Base de comparación: el memo convertido `dev/SoT/m65-20261014/docx-review/base/gmdp.memo.en.md`. Una diferencia entre el DOCX y el memo es edición de ella; una diferencia entre el memo y la fuente actual es reescritura nuestra y no se lista como edición.
- Cada registro de A1 y A2 se unió por oración y fragmento; cada fila B cita los ids de ambos. Además se comparó el DOCX con el memo oración por oración con un script (scratchpad de la sesión, fuera del proyecto) para no omitir diferencias; esa lectura agregó B47a.
- Un error que ella introduce dentro de una edición forma parte de esa edición: si la intención vale, la decisión es «portar corregida» con la oración corregida. Una edición que sólo tiene sentido junto con otra no portable hereda su decisión (B09a de B08a, B28b de B28a).
- «superada»: nuestra reescritura posterior cambió el fragmento que ella editó (B14a, B34a); en ninguno de los dos casos la mejora aplica a la oración nueva. Cuando el fragmento editado sobrevive en una oración que reescribimos, la edición se porta sobre la oración nueva (lista de arriba).
- «no portar: artefacto» cubre conversión, numeración de Word y estilo de cita, y además la adaptación a su documento (deícticos «This section»/«In this section», estructura, leyendas y remisiones a su Apéndice E).
- Todas las oraciones citadas en MAP.md, PATCH.md y DECISIONES-PROPIETARIO.md se extrajeron por programa de los archivos y se verificaron contra ellos; cada reemplazo de PATCH.md aparece una sola vez en su oración y cada fragmento propuesto está en la oración propuesta.

## Discrepancias entre A1 y A2 y su resolución

| # | Tema | A1 / A2 | Resolución |
|---:|---|---|---|
| 1 | «effective unit weight» (B17a) | A1 E14a la trata como terminología portable; A2 E14, como contenido. | Contenido. Leídos los textos: «effective unit weight» suele designar el peso sumergido y en su DOCX va acompañada de la oración nueva sobre el nivel freático (B18a); juntas afirman el método. Ambas van a D07. |
| 2 | Supresiones del MCE (B31a, B32a, B33b, B33d, B43a) | A1 las deja fuera del inventario como alcance (N22); A2 las registra como ediciones de contenido (E22, E23, E33). | Ediciones de ella (difieren del memo), «no portar: contenido», agrupadas en D11. |
| 3 | Notas de su Tabla 10-2 (B53a) | A1 las lee como ediciones de las notas del memo (SA08, SA09; SA08b portable); A2, como notas nuevas de su tabla (S11-S13). | Se adopta A2: describen las columnas de su Tabla 10-2, que reemplaza a las tablas del memo, y sus leyendas de figura conservan «Relative to Slope Height» sin artículo. «no portar: artefacto». |
| 4 | Oración del ápice (B14a) | A1 N08: origen indeterminable sin Git; A2 N05: contenido ya integrado en la fuente actual. | Por el método no está en el memo base, así que es adición de ella; nuestra fuente ya define $H$ desde el ápice (ts.model.md:7): «superada». |
| 5 | «estimated deterministically» (B34a) | A1 E23a la marca «ya cubierta»; A2 E24 la registra como edición de fluidez. | «superada»: dn.ensemble.md:9 ya dice «and the relation is applied deterministically» desde nuestra reescritura posterior. |
| 6 | Leyenda de la tabla de períodos (B46a) | A1 SA02b: no portar por ecuación y unidad; A2 E36: contenido. | «no portar: contenido» (quita el símbolo y la unidad de la leyenda), en D15; «slope scenarios» se porta (B46b). |
| 7 | Granularidad | A1: 66 cambios en 32 oraciones más SA/SB/N/O; A2: 87 cambios en 36 registros más S/N/X. | B: 102 ediciones en 54 elementos más 7 transversales. Los cambios compuestos se partieron por fragmento (p. ej. A2 E04 en B05a-e) y los cambios con error interno se unieron a su edición (A1 E29a+E29b en B40a). |
| 8 | Decisiones de B distintas de ambos | A1 y A2 coinciden en la clase, pero la lectura del texto lleva a otra decisión. | B02a («an ensemble set»: ambos gramática; B: contenido, cambia el referente). B09a (ambos fluidez/terminología; B: contenido, depende de suprimir B08a). B10a y B11a (ambos fluidez; B: portar corregida, para conservar el objeto de «evaluates» y el vínculo «Their denominator»). B26a y B37b (ambos terminología; B: portar corregida con «site-condition PGA», término de notation.md:109). B28b (ambos puntuación; B: depende de B28a). |
| 9 | Edición que ninguno registró | Ambos excluyeron las celdas de tabla. | B47a: su Tabla 10-1 redondea $a_1$ a tres decimales (memo: 3.6559, 3.3699, 3.1162, 3.1052, 2.9759). «no portar: números», D16. |
| 10 | Testigo del memo | Ambos compararon contra `_local/gmdp.memo.en.qmd` como testigo y pidieron validarlo. | B usó el memo convertido, base validada por el coordinador. Las atribuciones a reescrituras nuestras de A1 (N10-N20) y A2 (N01-N17) coinciden con el memo convertido (p. ej. «Those layer moduli», memo:79; «preceding sections», memo:402; «; that interval», memo:410; «$D_{a}/H_{s}$ … %», memo:436; sin «figures shade», memo:51). |

## Diferencias que no son ediciones de ella

Oraciones del DOCX idénticas al memo cuyo texto cambiamos después (no se listan en MAP.md): la composición de ts.results.qmd:6 y kmax.results.qmd:6; «The layer moduli» y la cláusula del ápice de ts.model.md:37; la ecuación de $T_s$ con $H$ y su definición en ts.model.md:4 y :7; «preceding chapters» (dn.ensemble.md:3); «used by … [@Verri2023a]» (dn.ensemble.md:9); «scenario. That interval» (dn.ensemble.md:11); «according to [-@eq-newmark-arias]» (dn.model.md:7); «are reported in Chapter [-@sec-slope_periods] and» (dn.uncertainty.md:3); el párrafo único de dn.uncertainty.md:5; «$D_a$ … cm» y «which the coefficient figures shade» (dn.uncertainty.md:11); «and the coefficient figures shade the intervals they delimit» (deq.kmax.md:5); «$b$ the geometric parameter» y la frase final de _captions/tbl.Ts.md:1; «Chapter»/«Appendix» por «Section». Los números renderizados del DOCX ($M_w$ = 7.0, 300 realizaciones, umbrales, alturas, rango de $T_s$) coinciden con el memo y tampoco son ediciones.

## Puntos abiertos para el coordinador

1. Armonización fuera de su capítulo. Si se portan B25b y B27a, $k_y$ sigue llamándose «yield acceleration» en dn.results.qmd:7 (ella tampoco lo cambió allí, DOCX 7), dn.model.md:1 y dn.appendix.md:5. Si se portan B35b, B41a-b y B44a-b, «support» y «extension» siguen en dn.appendix.md:5 (nota), :29 y :38. Si se porta B38a, «crustal control» sigue en dn.inputs.qmd:12 y dn.appendix.md:62. Su capítulo no incluye esas oraciones; B no propone cambios en ellas.
2. Término de la PGA. B26a y B37b proponen «site-condition PGA» (notation.md:109) en lugar de su «site-adjusted PGA». Si el propietario prefiere su término literal, se cambia en esos dos bloques de PATCH.md y en sus copias del memo.
3. Copias del memo. PATCH.md trae 28 bloques del memo con el mismo cambio sobre su propio texto; mantener el memo sincronizado es decisión del propietario. Observado al leerlo: `_local/gmdp.memo.en.qmd:79` conserva $T_s=\frac{4\pi H_s}{a_1(2-m_o)V_S^o}$ y `:82` «where $H_s$ is the slope height», mientras ts.model.md:4 y :7 usan $H=H_s/(1-\lambda_o)$; si el capítulo para ella se regenera desde el memo, esa ecuación sigue siendo la vieja.
4. Compuertas de la skill `writing`. Las propuestas son candidatas, no texto entregado. `check_entities.py` sobre las 54 oraciones propuestas, contra las fuentes actuales, el memo y el DOCX: 0 siglas, nombres o números sin fuente; 9 marcas de registro (each, single, all, lowest, exceeds, All, first, every, exceed), todas ya presentes en nuestras oraciones actuales. Todas las propuestas son ASCII. Falta el libro de procedencia y el veredicto de `audit.py deliver` antes de integrar; B no declara ninguna propuesta lista.
5. El encabezado del capítulo convertido dice «0 image embeds removed», pero el archivo conserva tres enlaces de imagen (DOCX 177, 185 y 193); no afecta a B.

## Insumos leídos

| sha256 (16) | Bytes | Archivo | Lectura |
|---|---:|---|---|
| `a1039d4829249121` | 30789 | `docx/CAPR003324_Crawford_SeismicHazard_Final.slope-design-parameters.md` | completa |
| `f02d6d0a5712f1f4` | 106060 | `dev/SoT/m65-20261014/docx-review/base/gmdp.memo.en.md` | prosa, leyendas y notas completas; de las tablas de $k_{max}$ y $k_h$, las filas citadas |
| `6f06854cc56a9ac0` | 67763 | `dev/SoT/m65-20261014/docx-review/A1/EDITS.md` | completa |
| `6d16441a746e7177` | 24231 | `dev/SoT/m65-20261014/docx-review/A1/SUMMARY.md` | completa |
| `d8e5228bb7287726` | 83044 | `dev/SoT/m65-20261014/docx-review/A2/EDITS.md` | completa |
| `4b1f86453e837dbc` | 8875 | `dev/SoT/m65-20261014/docx-review/A2/SUMMARY.md` | completa |
| `4cba543a0280505e` | 6172 | `_chapters/deq.criteria.md` | completa |
| `385c18cb8f839fc9` | 2854 | `_chapters/deq.kmax.md` | completa |
| `58de3be2a981e858` | 6406 | `_chapters/ts.model.md` | completa |
| `b8fd331e9dda05ad` | 5218 | `_chapters/dn.ensemble.md` | completa |
| `04961b5912ccf7c7` | 2041 | `_chapters/dn.model.md` | completa |
| `d62795bf18df6626` | 3760 | `_chapters/dn.uncertainty.md` | completa |
| `c742fc249db84b6b` | 5610 | `_chapters/dn.appendix.md` | completa |
| `8fc427c0994b5526` | 1464 | `_results/dn.inputs.qmd` | completa |
| `61ce786f89507979` | 846 | `_results/dn.results.qmd` | completa |
| `90bfd1474ac3c260` | 712 | `_results/kmax.results.qmd` | completa |
| `fbd266ec8ce58fa5` | 910 | `_results/ts.results.qmd` | completa |
| `7e0a6a04822551a4` | 31511 | `_local/gmdp.memo.en.qmd` | completa |
| `5e3762fd1c18cf32` | 822 | `_captions/tbl.Ts.md` | completa |
| `90a33867602334e7` | 4496 | `_docx/sdc.qmd` | líneas 85-170 (bloque de la sección de criterios) |
| `017c66d8c98c51fa` | 2169 | `_docx/gmdp.qmd` | completa |
| `85f8685246e5cbfa` | 655 | `_local/tbl.Ts.md` | completa |
| `ce37888646c0d95a` | 568 | `_local/fig.kh.md` | completa |
| `f25f5106fa74dc01` | 520 | `_local/tbl.kh.md` | completa |
| `130e188fb2b8436f` | 661 | `_captions/fig.kh.md` | completa |
| `4ef10a8ad7de0665` | 714 | `_captions/tbl.kh.md` | completa |
| `00e27276a79f5e02` | 485 | `_captions/tbl.kh.sites.md` | completa |
| `48aa7a05810f2795` | 44 | `_local/gmdp.memo.scenarios.csv` | completa |
| `d4cf2d1a50bea96f` | 1917 | `dev/SoT/m65-20261014/docx-review/base/gmdp.memo.en.assets.json` | completa |

Lecturas puntuales: `_chapters/notation.md` (líneas 105 y 109, y búsqueda de IP y POP sin resultado) y la skill `writing` (`SKILL.md`, `references/cases.md`).
