# Resumen de la extracción A1: ediciones del otro autor en «Slope Design Parameters»

Inventario completo en `EDITS.md`. El otro autor editó **32 oraciones nuestras** con **66 cambios de redacción**. Además, **20 oraciones únicas** del DOCX no tienen contraparte en las fuentes actuales, y **25 diferencias** no son ediciones a portar.

## Conteos

### Cambios de redacción por clase (entradas E01–E32)

| Clase | Cambios | Oraciones con esa clase principal |
|---|---:|---:|
| gramática | 7 | 2 |
| fluidez | 25 | 13 |
| terminología | 28 | 15 |
| puntuación | 4 | 0 |
| reordenamiento | 2 | 2 |
| **Total** | **66** | **32** |

Marcas sobre esos cambios: 16 de contenido técnico, 10 con error introducido en el DOCX y 1 ya cubierta por la fuente actual.

### Por archivo fuente (orden de ensamblado del Word)

| Archivo | Oraciones editadas | Cambios | Gramática | Fluidez | Terminología | Puntuación | Reordenamiento |
|---|---:|---:|---:|---:|---:|---:|---:|
| `_results/ts.results.qmd` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `_results/dn.results.qmd` | 2 | 4 | 2 | 0 | 1 | 1 | 0 |
| `_results/kmax.results.qmd` | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| `_chapters/deq.criteria.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `_chapters/deq.kmax.md` | 7 | 22 | 2 | 9 | 7 | 2 | 2 |
| `_chapters/ts.model.md` | 6 | 9 | 1 | 4 | 4 | 0 | 0 |
| `_captions/tbl.Ts.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `_chapters/dn.ensemble.md` | 8 | 18 | 0 | 8 | 9 | 1 | 0 |
| `_chapters/dn.model.md` | 2 | 3 | 0 | 2 | 1 | 0 | 0 |
| `_chapters/dn.uncertainty.md` | 6 | 9 | 1 | 2 | 6 | 0 | 0 |
| `_results/dn.inputs.qmd` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `_captions/tbl.kh.sites.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `_chapters/dn.appendix.md` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

`_chapters/deq.criteria.md`, `_results/dn.inputs.qmd` y `_chapters/dn.appendix.md` no tienen contraparte en la sección extraída. `_results/ts.results.qmd`, `_captions/tbl.Ts.md` y `_captions/tbl.kh.sites.md` tienen contraparte, pero sin ediciones de redacción.

### Sin contraparte

- 9 oraciones únicas con contraparte sólo en el memo (`_local/`), que suman 19 apariciones porque los pies de figura se repiten tres veces: SA01–SA09. Dentro de ellas hay 6 cambios de redacción respecto del memo (gramática 3, fluidez 1, terminología 2), 1 de ellos con error introducido.
- 11 oraciones sin contraparte en ningún texto del proyecto (SB01–SB11), todas añadidas por el otro autor.

## Patrones de edición observados

1. **$k_y$ como «yield coefficient».** El otro autor llama «coefficient» a $k_y$ y reserva «acceleration» para $a_y$ (E17, E19; en E20 conserva «yield acceleration $a_{y}$»).
2. **Términos numéricos más llanos.** «support» pasa a «range» (E24, E30, E32), «extended»/«extension» a «extrapolated»/«extrapolation» (E30, E32) y «distributed» a «spaced» (E24).
3. **«site-adjusted PGA»** donde decimos «the PGA» (E18, E26).
4. **Definiciones geotécnicas explícitas** (contenido): convención H:V de $s$, «crest» y sección simétrica (E12), «effective unit weight» (E14), POP como incremento y definición de IP (E15), $a_y$ definida por factor de seguridad unitario y $k_y$ «minimum» (E20), condición de la rama lognormal (E25), separación de los papeles de $T_s$ y $V_{S30}$ (E11), y dos oraciones nuevas sobre el nivel freático (SB01) y el factor de seguridad (SB03).
5. **Condensación del párrafo de criterios** (deq.kmax.md, E04–E10): oraciones más cortas, voz pasiva o activa directa, y supresión de atribuciones y justificaciones («ICOLD and FEMA frame for dams and embankments», «ninety case histories …», «so the coefficient results …»). Además omite el párrafo de NCHRP/Eurocode (O2).
6. **Sustituciones breves de fluidez**: «whose index is» → «indexed by» (E13), «the mean estimates» → «the estimates calculated from the mean parameter values» (E16), «the wedge in potential sliding is» → «the potentially sliding wedge is represented as» (E21), «keeps its demand state» → «preserves the pairing between displacement and seismic demand» (E28), «per model» → «for each model» (E31), «with» → «using» (E26).
7. **Ortografía estadounidense**: «analysed» → «analyzed» (E03, SA01).
8. **Errores introducidos, que no deben copiarse literal**: «Slope Performance» (E04), «rather than assigned as» (E05), conjunción y punto faltantes en la oración de USACE (E06), «Alberti et. al.» (E08), verbo faltante en «while $V_{S30}$ the site conditions» (E11), «${IP}^{(k)}$is» (E15), «such that $D_{n}$ exceeds $D_{a}$» (E17), «an separate» (E29), «induced by an earthquake accumulates» (E01) y «induced by the design earthquakes accumulate» (SA01).
9. **Adaptaciones de alcance y documento**: suprime el MCE, quita el sitio de los pies, escribe «section» donde decíamos «memo» o «report», pone los pies en mayúsculas de título y usa su propia numeración (N21–N24).

## No es edición a portar

25 entradas. Algunas agrupan varias apariciones de la misma causa; las líneas se indican en cada una.

- **N01 · Numeración y remisiones de Word.** El DOCX cambia nuestras remisiones de Quarto (`[-@sec-…]`, `[-@eq-…]`, `{#eq-…}`) por la numeración de su documento: «[**11Appendix E**](#section-2)» (DOCX 7, 92, 106 y 145), «Section [**10.1.3**]» (15), las etiquetas «Eq. 10‑1» a «Eq. 10‑16» (21–110), «[Table E‑1](#section-4)» (66), «Section [**10.1.2**]» (82), «[**Eq. 10‑14**]» (106), «[**Eq. 10‑16**]» (108) y «Section [**10.1.1**]» (112). En la línea 108 la remisión absorbe además la palabra «expression» de dn.uncertainty.md:5. Causa: numeración de Word.
- **N02 · Estilo de cita.** El DOCX cita como (Autor, Año) donde nosotros usamos `[@Clave]` o `[-@Clave]` (DOCX 7, 13, 15, 19, 27, 43, 47, 55, 78, 80, 82, 84, 88 y 108). Para desambiguar, Word agrega títulos (Bray & Travasarou 2009; Hardin 1968 y 1972). En DOCX 43 y 55 figura «Ishihara (1997)» donde ts.model.md:37 y :55 citan «[-@Ishihara1996]». Causa: estilo de cita del documento del otro autor.
- **N03 · Citas añadidas a cada modelo (DOCX 7).** El DOCX agrega «AM88 (Ambraseys & Menu, 1988), JB07 (Jibson, 2007), SR08 (Saygili & Rathje, 2008), BT07 (Bray & Travasarou, 2007), and BM19 (Bray, Macedo, & Travasauro, 2018)». dn.results.qmd:7 no cita nada en esa oración. «Travasauro» está mal escrito, y BM19 lleva el año 2018, mientras dn.appendix.md:54 cita BM19 como «[@BrayMacedo2019]» y dn.appendix.md:48 cita BM17 como «[@BrayEtAl2018]». Son citas: quedan fuera del alcance y se informan.
- **N04 · «Alberti et. al.» (DOCX 15).** El DOCX escribe «Alberti et. al. (Aliberti, Biondi, Cascone, & Rampello, 2019)» donde deq.kmax.md:5 cita «[@Aliberti2019]». El apellido está mal escrito y «et al.» mal puntuado. Es una cita y no se porta.
- **N05 · Números renderizados de expresiones `r`.** Los valores que el DOCX muestra son el resultado de nuestras expresiones en línea: «5 geometry–material scenarios with heights between 27 and 135 m» y «0.19 and 0.83 s» (DOCX 5); «$M_{w}$ = 7.0» (7) y «$M_{w} =$ 7.0» (92); «300 realizations» (7, 112); «0.1, 0.4, 1.0, 2.5%» (7, 15, 112, notas de figura); «0.05 to 2.50 %» (112); la lista de escenarios S135 … S35 de los pies (179–195). No son ediciones.
- **N06 · Períodos de retorno 475 y 2,475 años.** El DOCX dice «$T_{R}$ = 475, 2,475, 10,000 years» (112), «1:475, 1:2,475, and 1:10,000 years» (145) y «$T_{R} = 2,475$» (187). El memo fija «TR.target <- c(500, 2500, TR.MDE)» (_local/gmdp.memo.en.qmd:24), y el texto alternativo de las imágenes del propio DOCX conserva «TR=500 yr» (177) y «TR=2,500 yr» (185). Son números y quedan fuera del alcance. Lo informo para que el coordinador verifique qué demanda representan las figuras.
- **N07 · Marcado de ecuaciones tras la conversión.** La conversión LaTeX → Word → Markdown altera el marcado de todas las ecuaciones (Eq. 10‑1 a 10‑16) y de los símbolos en línea, sin cambiar su contenido. Ejemplos: «$k_{y} = a_{y}/g$» (DOCX 78) frente a «$k_y=a_y/g$» (dn.ensemble.md:3); «\mathcal{l}» (51) frente a «\ell» (ts.model.md:55); «$\ln{(S}_{a})$» (84) frente a «$\ln S_a$» (dn.ensemble.md:9); «$(lnD_{n},lnk_{y})$» (106) frente a «$(\ln D_n,\ln k_y)$» (dn.uncertainty.md:5); funciones sin barra («exp\left(», 90; «inf\left\{», 94; «max(30 - H_{s},0)», 70); `\mathrm` perdido; `cases` → `matrix` con «\right.\$» suelto (60); negritas «$\mathbf{k}_{\mathbf{h}}$» (179); residuos «${}_{}$» (187, 195).
- **N08 · Período fundamental y altura desde el ápice.** El DOCX tiene «$T_{s} = \frac{4\pi H_{s}}{a_{1}(2 - m_{o})V_{S}^{o}},$» (21) y la oración «The height from the virtual apex to the base of the equivalent wedge is $\frac{H_{s}}{(1 - \lambda_{o})}.\$» (23). La fuente actual define el período con «T_s=\frac{4\pi H}{a_1(2-m_o)V_S^o},» (ts.model.md:4), con «where $H=H_s/(1-\lambda_o)$ is the height of the truncated wedge from the apex of the extended slopes to the base,» (ts.model.md:7) y con la cláusula «; the characteristic equation corresponds to the power law with depth measured from the apex of the extended slopes and normalized by $H$ [-@DakoulasGazetas1985Inhomogeneous], so evaluating $a_1$ with the exponent fitted from the crest is an approximation.» (ts.model.md:37). El memo del 2026-09-24 usa «4\pi H_s» (_local/gmdp.memo.en.qmd:79) y no trae la oración del ápice. Es ecuación y reescritura nuestra posterior (el estado la fecha el 2026-10-13). Sin Git no puedo determinar de dónde salió la oración del ápice del DOCX.
- **N09 · Ecuación del OCR pasada a ecuación numerada.** ts.model.md:55 escribe en línea «$\mathrm{OCR}^{(k)}=\max[(p_m^{(k)}+\mathrm{POP})/p_m^{(k)},1]$». El DOCX la convierte en la Eq. 10‑9 (53) y parte la oración en 51 y 55. Es maquetación de ecuación. Las palabras que agregó el otro autor van en E15.
- **N10 · deq.kmax.md:5, frase agregada por nosotros.** «and the coefficient figures shade the intervals they delimit» está en la fuente actual y falta en memo:70 y en DOCX 15. Es una reescritura nuestra posterior al memo, no una supresión del otro autor.
- **N11 · «Chapter»/«Appendix» (fuente actual) frente a «Section» (memo y DOCX).** deq.kmax.md:5 «developed in Chapter» (memo:70 «developed in Section»); dn.ensemble.md:3 «preceding chapters» (memo:184 y DOCX 78 «preceding sections»); dn.ensemble.md:7 «established in Chapter» (memo:188 «established in Section»); dn.model.md:7 «reproduced in Appendix» (memo:200 «reproduced in Section»); dn.uncertainty.md:5 «treated in Appendix» (memo:219 «treated in Section»); dn.uncertainty.md:11 «% of Chapter» (memo:227 «% of Section»). El memo adaptó estas remisiones a su propio formato. No son ediciones del otro autor.
- **N12 · ts.model.md:37, «The» frente a «Those».** La fuente actual dice «The layer moduli come from»; memo:112 y DOCX 43 dicen «Those layer moduli come from». Es una reescritura nuestra.
- **N13 · dn.ensemble.md:9, reescritura de la intensidad de Arias.** La fuente actual dice «The Arias intensity used by `JB07` and `SR08`» y «from the PGA [@Verri2023a], and the relation is applied deterministically»; memo:190 y DOCX 84 dicen «that `JB07` and `SR08` require» / «that JB07 and SR08 require». Es reescritura nuestra. El adverbio que agregó el otro autor va en E23.
- **N14 · dn.ensemble.md:11, punto frente a punto y coma.** La fuente actual dice «scenario. That interval»; memo:192 y DOCX 86 dicen «scenario; that interval». Es reescritura nuestra.
- **N15 · dn.model.md:7, remisión a la ecuación de Arias.** «according to [-@eq-newmark-arias]» está en la fuente actual y falta en memo:200 y en DOCX 92. Es reescritura nuestra.
- **N16 · dn.uncertainty.md:3, frase agregada por nosotros.** «are reported in Chapter [-@sec-slope_periods] and» está en la fuente actual y falta en memo:217 y en DOCX 104. Es reescritura nuestra.
- **N17 · dn.uncertainty.md:5, división en párrafos.** La fuente actual tiene un solo párrafo. El memo (219 y 221) y el DOCX (106 y 108) lo parten en dos antes de «The root distributions». El memo lo partió así; no es una edición del otro autor.
- **N18 · dn.uncertainty.md:11, malla de desplazamientos y figuras.** La fuente actual dice «a grid of allowable displacements $D_a$ ranging from» y termina en «cm.». Memo:227 y DOCX 112 dicen «$D_a/H_s$» y «%». Además, «and which the coefficient figures shade» falta en el memo y en el DOCX. Es reescritura nuestra (y la diferencia afecta números).
- **N19 · _captions/tbl.Ts.md:1, nota de la tabla de períodos.** La fuente actual dice «$b$ the geometric parameter» y cierra con «and $T_s \approx T_1$ is the fundamental period, in seconds.». El memo (_local/tbl.Ts.md:1) y el DOCX 143 dicen «$b$ the berm width» y no traen esa última frase. Es reescritura nuestra. Por lo demás, la nota del DOCX coincide con la nuestra, salvo los artefactos de N25.
- **N20 · Resumen ejecutivo compuesto en el memo.** _results/ts.results.qmd:6 y _results/kmax.results.qmd:6 están compuestos de otra manera en el memo (por ejemplo «the analyses considered `r nrow(Scenarios)` geometry--material scenarios», memo:45, y «is in turn derived», memo:53), y el DOCX sigue al memo. En DOCX 5 la segunda oración es la del memo sin ninguna edición; en DOCX 7 la única edición es la de E03.
- **N21 · Adaptación al documento del otro autor.** «In this report» (dn.ensemble.md:1) y «In this memo» (memo:182) pasan a «In this section» (DOCX 76); «It reports» (memo:45) pasa a «This section reports» (DOCX 5).
- **N22 · Supresión del MCE (alcance del informe del otro autor).** DOCX 82 dice «– the probabilistic spectrum of each evaluated return period –» donde dn.ensemble.md:7 dice «-- the probabilistic spectrum of each evaluated return period and the MCE scenario --». Además, DOCX 82 omite «Two inputs feed that sample.» y «, and the MCE input is the rock spectrum of each scenario», y DOCX 112 omite «and the MCE» (dn.uncertainty.md:11). Es contenido de alcance, no gramática.
- **N23 · Pies, mayúsculas de título y formato de código.** Los pies de figura y de la Tabla 10‑2 van en mayúsculas de título (DOCX 171, 179, 187, 195). El pie del memo nombra el sitio («for site %1$s», _local/fig.kh.md:1) y el DOCX lo omite. Los identificadores que escribimos como código (`ensemble`, `IDn`, `rigid`, `JB07`, `SR08`, `ST20`, …) pierden ese formato, y «--» pasa a «–». Es estilo del documento del otro autor.
- **N24 · Títulos y estructura.** Encabezados del DOCX: «# Slope Design Parameters» (3), «## Definitions» (9), «### Seismic Design Criteria for Slopes» (11), «### Fundamental Period of the Embankment» (17; el nuestro es «## Dynamic Properties of Slopes», _docx/gmdp.qmd:10), «### Seismic (Pseudo-Static) Coefficients» (74; el nuestro es «## Performance-Based Seismic Coefficient», _docx/gmdp.qmd:44), «## Fundamental Periods of the Crawford Embankments» (114) y «Seismic Coefficients» (143, fusionado por la conversión). La tabla de períodos pasa a una subsección propia y la tabla de correlaciones al Apéndice E. Es estructura de su informe; no los cuento como oraciones.
- **N25 · Artefactos de conversión del texto.** Hay «Notes:» seguidos de viñetas vacías (DOCX 134–141) y repetidos en 173, 181, 189 y 197. La nota de la Tabla 10‑1 quedó fusionada con el título en la línea 143 y perdió los punto y coma («both in m$s$ is», «dimensionless$a_{1}$», «dimensionless$V_{S}^{o}$»). Quedan marcas de negrita «**[****Eq.». La cabecera de la línea 1 dice «0 image embeds removed», pero el archivo conserva tres enlaces de imagen (177, 185 y 193).

## Partes del DOCX sin contraparte

- **Con contraparte sólo en el memo** (`_local/gmdp.memo.en.qmd`, `_local/tbl.Ts.md`, `_local/fig.kh.md`, `_local/tbl.kh.md`):
  - SA01 (DOCX 5): «This section reports the dynamic properties of the slopes analyzed, the permanent displacements induced by the design earthquakes accumulate in their potential sliding masses, and the performance-based seismic coefficients derived from those displacements.»
  - SA02 (DOCX 132): «Fundamental periods and mean dynamic properties of the evaluated slope scenarios»
  - SA03 (DOCX 179, 187 y 195): «Mean Values of $k_{h}$ [% of PGA] for Return Period $T_{R} = 2,475$ yr, as a Function of the Allowable Permanent Displacement Relative to Slope Height, $D_{a}/H$ [%].»
  - SA04 (DOCX 179, 187 y 195): «The Curves Represent the Scenarios S135, S50, S32, S27, S35 Evaluated with the Rigid, Ensemble, and Flexible Sets.»
  - SA05 (DOCX 183, 191 y 199): «The coefficient is expressed as $100\, k_{\max}/PGA(V_{S30})$.»
  - SA06 (DOCX 183, 191 y 199): «Color identifies the scenario and line pattern identifies the set: solid for rigid, short dashes for ensemble, and long dashes for flexible.»
  - SA07 (DOCX 183, 191 y 199): «The shaded bands are delimited by the damage thresholds $D_{a}/H = 0.1,0.4,1.0,2.5$ %.»
  - SA08 (DOCX 175): «The column headings give the allowable permanent displacement relative to the slope height, expressed as a percentage.»
  - SA09 (DOCX 175): «The fundamental period of the slope is in seconds and the time-averaged shear-wave velocity of the upper 30 m is in m/s.»
- **Sin contraparte en ningún texto del proyecto:**
  - SB01 (DOCX 51): «For hydrostatic groundwater conditions, the bulk unit weight is used above the groundwater table and the submerged unit weight below it; layers intersected by the groundwater table are subdivided accordingly.»
  - SB02 (DOCX 66): «The parameters of the stiffness correlations are listed in [Table E‑1](#section-4).»
  - SB03 (DOCX 78): «A factor of safety of at least unity under this applied coefficient indicates that the calculated yield coefficient meets or exceeds the required threshold.»
  - SB04 (DOCX 116): «[Table 10‑1](#_Ref_gmdp_tbl_periods) presents the fundamental periods and the mean dynamic properties of the slope scenarios evaluated for the Crawford facilities.»
  - SB05 (DOCX 116): «Each scenario is named with the letter S followed by its slope height in meters.»
  - SB06 (DOCX 116): «The scenarios are S135, S50, S32, S27, and S35, which correspond to material identifiers (IDm) U1 to U5 in [Table 10‑1](#_Ref_gmdp_tbl_periods), respectively.»
  - SB07 (DOCX 145): «[Figure 10‑1](#_Ref_gmdp_fig_kh_1) through [Figure 10‑3](#_Ref_gmdp_fig_kh_3) show the performance-based horizontal seismic coefficient, expressed as a percentage of the PGA, as a function of the allowable permanent displacement relative to the slope height, for design earthquakes with AEPs of 1:475, 1:2,475, and 1:10,000 years.»
  - SB08 (DOCX 145): «[Table 10‑2](#_Ref_gmdp_tbl_summary) lists the coefficients of the ensemble set at the four relative displacement limits for the 1:2,475 and 1:10,000-year return period design earthquakes.»
  - SB09 (DOCX 145): «The coefficients of the rigid and flexible sets, and the coefficients in acceleration units, are included in [**11Appendix E**](#section-2).»
  - SB10 (DOCX 171): «Seismic Coefficients [% of PGA] of the Ensemble Set for Design Earthquakes with AEPs of 1:2,475 and 1:10,000 Years»
  - SB11 (DOCX 175): «Values are for the ensemble set.»

## Contenido nuestro ausente del DOCX

- **O1.** _chapters/deq.criteria.md no aparece en la sección extraída. El memo (_local/gmdp.memo.en.qmd:64) incluía su primer párrafo y la oración «In this report, the MDE is represented by the probabilistic spectrum for a 10,000-year return period, whereas the MCE is represented by the deterministic envelope.»
- **O2.** Falta el párrafo de _chapters/deq.kmax.md:3 (NCHRP Report 611 y Eurocode 8), que también estaba en memo:68.
- **O3.** Falta la conclusión de deq.kmax.md:1 «so the coefficient results from the conditions of each project instead of a single value applicable to all of them» (E06).
- **O4.** Falta en deq.kmax.md:5 el origen de los umbrales: «derived from ninety case histories of earthquake damage to embankment dams» (E08).
- **O5.** La tabla de correlaciones de rigidez que incluye ts.model.md:80 se movió al Apéndice E del DOCX (SB02).
- **O6.** Faltan las oraciones del MCE de dn.ensemble.md:7 y dn.uncertainty.md:11 (N22).
- **O7.** _results/dn.inputs.qmd:12 (formulaciones, pesos, demandas, alturas y malla) no tiene contraparte en el capítulo del DOCX.
- **O8.** _chapters/dn.appendix.md corresponde al «Appendix E» del DOCX, que está fuera de la sección extraída. No lo comparé.
- **O9.** El memo genera figuras y tablas de $k_{max}$ y $k_h$ por demanda y por escenario (_local/gmdp.memo.en.qmd:229–266). El capítulo del DOCX trae sólo tres figuras de $k_h$ y su propia Tabla 10‑2.

## Observaciones para el coordinador

- **Archivo que cambió durante la sesión.** `_chapters/ts.model.md` pasó de 6044 a 6406 bytes mientras trabajaba. La versión citada (sha256 `58de3be2a981…`) define $H=H_s/(1-\lambda_o)$ desde el ápice en las líneas 4, 7 y 37. No lo modifiqué.
- **Memo como testigo.** El memo `_local/gmdp.memo.en.qmd` no está en la lista de insumos del estado. Lo leí completo, sólo para lectura, como testigo. Muestra que el otro autor recibió esa versión: el DOCX coincide con el memo en «Those layer moduli», «preceding sections», «that JB07 and SR08 require», «; that interval», «$D_a/H_s$ … %» y en los pies de figura y tabla.
- **Oración del ápice (DOCX 23).** No está en el memo ni en las fuentes actuales. Sin Git no puedo fechar su origen (N08).
- **Períodos de retorno.** Los períodos 475 y 2,475 del DOCX no coinciden con el 500 y el 2,500 del memo ni con el texto alternativo de sus propias imágenes (N06).
- **Cita de BM19.** En DOCX 7, BM19 aparece citado como «(Bray, Macedo, & Travasauro, 2018)» (N03).
- **«crest» y «berm».** E12 introduce «crest width» en la misma oración y párrafo donde se definen «berm and base widths»; si se porta, hay que elegir un solo término.
- **Uso del inventario.** Las entradas marcadas «contenido técnico» cambian contenido y requieren decisión del propietario. Las marcadas «error introducido» no se copian literal. El resto es redacción.

## Insumos leídos completos

| sha256 (12) | Bytes | Archivo |
|---|---:|---|
| `a1039d482924` | 30789 | `docx/CAPR003324_Crawford_SeismicHazard_Final.slope-design-parameters.md` |
| `4cba543a0280` | 6172 | `_chapters/deq.criteria.md` |
| `385c18cb8f83` | 2854 | `_chapters/deq.kmax.md` |
| `58de3be2a981` | 6406 | `_chapters/ts.model.md` |
| `b8fd331e9dda` | 5218 | `_chapters/dn.ensemble.md` |
| `04961b5912cc` | 2041 | `_chapters/dn.model.md` |
| `d62795bf18df` | 3760 | `_chapters/dn.uncertainty.md` |
| `c742fc249db8` | 5610 | `_chapters/dn.appendix.md` |
| `8fc427c0994b` | 1464 | `_results/dn.inputs.qmd` |
| `90a338676023` | 4496 | `_docx/sdc.qmd` |
| `017c66d8c98c` | 2169 | `_docx/gmdp.qmd` |
| `fbd266ec8ce5` | 910 | `_results/ts.results.qmd` |
| `61ce786f8950` | 846 | `_results/dn.results.qmd` |
| `90bfd1474ac3` | 712 | `_results/kmax.results.qmd` |
| `5e3762fd1c18` | 822 | `_captions/tbl.Ts.md` |
| `130e188fb2b8` | 661 | `_captions/fig.kh.md` |
| `4ef10a8ad7de` | 714 | `_captions/tbl.kh.md` |
| `00e27276a79f` | 485 | `_captions/tbl.kh.sites.md` |
| `7e0a6a048225` | 31511 | `_local/gmdp.memo.en.qmd` |
| `ce37888646c0` | 568 | `_local/fig.kh.md` |
| `f25f5106fa74` | 520 | `_local/tbl.kh.md` |
| `85f8685246e5` | 655 | `_local/tbl.Ts.md` |
| `321394b7ca0f` | 4135 | `_chapters/intro.objectives.md` |
| `c59e263d57e3` | 639 | `_chapters/executive.opening.md` |

Las búsquedas de contraparte cubrieron además `_chapters/*.md`, `_results/*.qmd`, `_captions/*.md` y `_local/*` con grep. Los archivos con coincidencias pertinentes se leyeron completos y figuran en la tabla. Otras coincidencias de grep sobre temas ajenos (pies de figura de $k_{max}$, $D_n$ y MCE con «line pattern», `_captions/fig.srs.ps.md`, `_chapters/srs.model.md`) se descartaron por su nombre y su línea, sin leerlos completos.
