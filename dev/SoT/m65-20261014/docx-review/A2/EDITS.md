# A2 · Ediciones del otro autor en «Slope Design Parameters» (DOCX CAPR003324)

Inventario oración por oración de las diferencias entre la sección «Slope Design Parameters» del DOCX y los textos fuente del proyecto. Las oraciones citadas se copian textualmente de los archivos leídos (inglés). Las líneas del DOCX remiten a `docx/CAPR003324_Crawford_SeismicHazard_Final.slope-design-parameters.md`.

## Insumos leídos

Lectura completa de cada archivo en esta sesión (2026-10-15). SHA-256 truncado a 16 caracteres.

| Archivo | Bytes | SHA-256 | Papel |
|---|---:|---|---|
| `docx/CAPR003324_Crawford_SeismicHazard_Final.slope-design-parameters.md` | 30789 | `a1039d4829249121` | insumo editado (estado) |
| `_chapters/deq.criteria.md` | 6172 | `4cba543a0280505e` | fuente nombrada |
| `_chapters/deq.kmax.md` | 2854 | `385c18cb8f839fc9` | fuente nombrada |
| `_chapters/ts.model.md` | 6406 | `58de3be2a981e858` | fuente nombrada |
| `_chapters/dn.ensemble.md` | 5218 | `b8fd331e9dda05ad` | fuente nombrada |
| `_chapters/dn.model.md` | 2041 | `04961b5912ccf7c7` | fuente nombrada |
| `_chapters/dn.uncertainty.md` | 3760 | `d62795bf18df6626` | fuente nombrada |
| `_chapters/dn.appendix.md` | 5610 | `c742fc249db84b6b` | fuente nombrada |
| `_results/dn.inputs.qmd` | 1464 | `8fc427c0994b5526` | fuente nombrada |
| `_docx/sdc.qmd` | 4496 | `90a33867602334e7` | ensamblado nombrado |
| `_docx/gmdp.qmd` | 2169 | `017c66d8c98c51fa` | ensamblado nombrado |
| `_results/ts.results.qmd` | 910 | `fbd266ec8ce58fa5` | búsqueda en _results/ |
| `_results/dn.results.qmd` | 846 | `61ce786f89507979` | búsqueda en _results/ |
| `_results/kmax.results.qmd` | 712 | `90bfd1474ac3c260` | búsqueda en _results/ |
| `_chapters/executive.opening.md` | 639 | `c59e263d57e3a644` | búsqueda en _chapters/ |
| `_master/docx.en.qmd` | 278 | `d061b135cc989b8b` | orden de ensamblado |
| `_docx/executive.site.qmd` | 3646 | `7e8885a9c4c81b71` | orden de ensamblado |
| `_captions/tbl.Ts.md` | 822 | `5e3762fd1c18cf32` | leyenda del Word propio (gmdp.qmd:39) |
| `_captions/tbl.kh.sites.md` | 485 | `00e27276a79f5e02` | leyenda más cercana (S10-S12) |
| `_captions/fig.kh.md` | 661 | `130e188fb2b8436f` | leyenda leída, sin uso en el DOCX |
| `_local/gmdp.memo.en.qmd` | 31511 | `7e0a6a04822551a4` | testigo auxiliar (fuera de la lista) |
| `_local/gmdp.memo.plan.md` | 5693 | `e90d5da3c0007582` | testigo auxiliar (fuera de la lista) |
| `_local/tbl.Ts.md` | 655 | `85f8685246e5cbfa` | testigo auxiliar (fuera de la lista) |
| `_local/tbl.kh.md` | 520 | `f25f5106fa74dc01` | testigo auxiliar (fuera de la lista) |
| `_local/fig.kh.md` | 568 | `ce37888646c0d95a` | testigo auxiliar (fuera de la lista) |
| `_local/gmdp.memo.scenarios.csv` | 44 | `48aa7a05810f2795` | testigo auxiliar (fuera de la lista) |

Búsquedas de texto sin lectura completa (para declarar ausencias): `grep` de frases del DOCX en `_chapters/`, `_results/`, `_captions/`, `_tbl/`, `_docx/`, `_master/`, `_local/`, `_scope/`, `_book/`, `_revealjs/`, `_fig/`, `specs/`, `dev/` e `index.qmd`, y extracción de las leyendas de `html/gmdp.memo.en/index.html` (801493 bytes, 2026-09-24 23:38).

`_chapters/ts.model.md` cambió en disco durante la sesión: la primera lectura tenía 6044 bytes y $T_s$ con $H_s$ en el numerador; la versión actual (6406 bytes, modificada 2026-10-12 19:29) usa $H=H_s/(1-\lambda_o)$. El inventario usa la versión actual.

## Método

1. Cada oración del DOCX se emparejó con su contraparte en las fuentes nombradas en el estado, por el orden de ensamblado del Word propio (`_master/docx.en.qmd` → `_docx/executive.qmd` → `_docx/executive.site.qmd`, `_docx/sdc.qmd`, `_docx/gmdp.qmd`). Para las oraciones sin contraparte se buscó en `_chapters/*.md` y `_results/*.qmd`.

2. **Testigo auxiliar (inferencia de esta extracción, a validar por el coordinador).** La sección del DOCX sigue la estructura y la redacción de `_local/gmdp.memo.en.qmd` (memo del 2026-09-24): la apertura de la línea 5 sólo existe allí, «Those layer moduli» sólo existe allí y las leyendas de figura del DOCX coinciden con `_local/fig.kh.md`. El memo se usó como testigo de la versión anterior: si el DOCX coincide con el memo y difiere del capítulo, la diferencia es nuestra y se registra como «no es edición a portar». El memo no está en la lista de insumos del estado; esa atribución depende de esta inferencia.

3. La detección usó una comparación por palabras con normalización de formato (llaves y espacios de LaTeX, `\mathrm`, acentos graves, citas, guiones). La normalización sólo sirvió para detectar diferencias; las citas de este inventario son textuales y el generador comprobó que cada fragmento citado existe en su archivo.

4. Clases de cambio: gramática (incluye ortografía y errores introducidos), fluidez, terminología, puntuación, reordenamiento. **Extensión:** la etiqueta «contenido» marca los cambios que añaden, quitan o redefinen una afirmación técnica; no es una edición de gramática ni de fluidez y requiere decisión del propietario. Cada registro E corresponde a una oración del DOCX (o a un grupo cuando el otro autor partió o fundió oraciones) y enumera sus cambios; cada cambio lleva una sola etiqueta.

5. Las diferencias de números, ecuaciones, citas, referencias cruzadas, conversión, adaptación al documento receptor y reescrituras nuestras se registran aparte (N01-N36).

## 1. Ediciones por archivo fuente (orden de ensamblado del Word)

### _results/ts.results.qmd

Ensamblado: _docx/executive.site.qmd:48 (resumen ejecutivo).

Sin ediciones del otro autor: la oración del DOCX (línea 5) reproduce el memo (N01).

### _results/dn.results.qmd

Ensamblado: _docx/executive.site.qmd:50.

#### E01 · DOCX línea 7 · `_results/dn.results.qmd:7`

Original (`_results/dn.results.qmd:7`):

```text
The Newmark permanent displacement $D_n$ quantifies the deformation an earthquake accumulates in the sliding mass and is the performance measure from which the seismic coefficients are derived.
```

Editada (DOCX línea 7):

```text
The Newmark permanent displacement $D_{n}$ quantifies the displacement induced by an earthquake accumulates in the sliding mass and is the performance measure from which the seismic coefficients are derived.
```

Cambios:

- [terminología] `deformation` → `displacement`.
- [gramática] en la editada: `displacement induced by an earthquake accumulates`. Se inserta «induced by» y se conserva «accumulates»: quedan dos predicados y la oración editada es agramatical.

Clases: gramática, terminología.

Nota: Mismo patrón que E35. Sólo la sustitución de término es candidata; la construcción con «induced by» no se puede portar tal cual.

#### E02 · DOCX línea 7 · `_results/dn.results.qmd:7`

Original (`_results/dn.results.qmd:7`):

```text
The $D_n(k_y)$ curves relate, for each combination of geometry, material, and design scenario, the yield acceleration $k_y$ to the expected permanent displacement; they were computed with the `ensemble` set of `AM88`, `JB07`, `SR08`, `BT07`, and `r BM.code`, with the reference magnitude $M_w$ = `r .fmt(Mw.gmdp, 1)` and `r .fmti(NS)` realizations per demand, and are read at the fractiles $q = 1 - p_e$.
```

Editada (DOCX línea 7):

```text
The $D_{n}(k_{y})$ curves relate, for each combination of geometry, material, and design scenario, the yield acceleration $k_{y}$ to the expected permanent displacement; they were computed with an ensemble set of AM88 (Ambraseys & Menu, 1988), JB07 (Jibson, 2007), SR08 (Saygili & Rathje, 2008), BT07 (Bray & Travasarou, 2007), and BM19 (Bray, Macedo, & Travasauro, 2018), with the reference magnitude $M_{w}$ = 7.0 and 300 realizations per demand and are read at the fractiles $q = 1 - p_{e}$.
```

Cambios:

- [gramática] `` the `ensemble` set `` → `an ensemble set`. El artículo indefinido deja de remitir al conjunto nombrado `ensemble`.
- [puntuación] `per demand, and are read` → `per demand and are read`. Coma suprimida antes del segundo predicado.

Clases: gramática, puntuación.

Nota: Las citas añadidas a cada código de modelo y los valores numéricos se registran en N23 y N30.

### _results/kmax.results.qmd

Ensamblado: _docx/executive.site.qmd:52.

#### E03 · DOCX línea 7 · `_results/kmax.results.qmd:6`

Original (`_results/kmax.results.qmd:6`):

```text
The horizontal pseudostatic coefficient $k_h$ is derived from the allowable permanent displacement $D_a$ of the potentially sliding mass [@BrayTravasarou2009; @MacedoEtAl2018]. The coefficients are reported at four relative displacement limits, $D_a/H_s$ = `r paste(.fmt(DAMAGE.CUTS, 1), collapse = ", ")`%. Table [-@`r TBL.KH`] reports, for the MCE and the geometries analysed, the range of the coefficient across the material scenarios at each limit, expressed as a percentage of the PGA.
```

Testigo memo (`_local/gmdp.memo.en.qmd:53`):

```text
The horizontal pseudostatic coefficient $k_h$ is in turn derived from the allowable permanent displacement $D_a$ of the potentially sliding mass [@BrayTravasarou2009; @MacedoEtAl2018]; the coefficients are reported at four relative displacement limits, $D_a/H_s$ = `r paste(.fmt(DAMAGE.CUTS, 1), collapse = ", ")`%, and the tables in Section [-@sec-kh-tables] report, for the demands and scenarios analysed, the coefficient at each limit, expressed as a percentage of the PGA.
```

Editada (DOCX línea 7):

```text
The horizontal pseudostatic coefficient $k_{h}$ is in turn derived from the allowable permanent displacement $D_{a}$ of the potentially sliding mass (Bray & Travasarou, Pseudostatic Coefficient for Use in Simplified Seismic Slope Stability Evaluation, 2009; Macedo, Bray, Abrahamson, & Travasarou, 2018); the coefficients are reported at four relative displacement limits, $D_{a}/H_{s}$ = 0.1, 0.4, 1.0, 2.5%, and the tables in Section [**10.3**](#idm-identifies-the-material-scenario-and-uscs-the-classification-of-the-slope-materials.-h_s-is-the-slope-height-and-b-the-berm-width-both-in-ms-is-the-slope-ratio-tanbeta-1s-and-lambda_o-the-truncation-ratio-both-dimensionless-g_o-is-the-shear-modulus-of-the-profile-at-zh_s-1-in-mpa-and-m_o-the-exponent-of-its-power-law-dimensionlessa_1-is-the-first-modal-root-dimensionlessv_so-is-the-basal-shear-wave-velocity-and-v_s30-the-travel-time-averaged-shear-wave-velocity-in-the-uppermost-30-m-both-in-ms.seismic-coefficients) and [**11Appendix E**](#section-2) report, for the demands and scenarios analyzed, the coefficient at each limit, expressed as a percentage of the PGA.
```

Cambios:

- [gramática] `analysed` → `analyzed`. Ortografía estadounidense; la misma sustitución aparece en E35.

Clases: gramática.

Nota: El DOCX reproduce la oración única del memo (_local/gmdp.memo.en.qmd:53), no las tres oraciones del bloque de resultados (N02). La única edición del otro autor frente al memo es la ortografía.

### _chapters/deq.criteria.md

Ensamblado: _docx/sdc.qmd:91.

Sin contraparte en la sección del DOCX (X01, X06).

### _chapters/deq.kmax.md

Ensamblado: _docx/sdc.qmd:93.

#### E04 · DOCX línea 13 · `_chapters/deq.kmax.md:1`

Original (`_chapters/deq.kmax.md:1`):

```text
The verification of the slopes under those design earthquakes follows the practice that ICOLD and FEMA frame for dams and embankments through successive tiers of analysis: pseudostatic checks, simplified deformation estimates, and dynamic analyses when the consequence, the anticipated response, or the complexity of the mechanism requires them [@ICOLD2016; @FEMA2005].
```

Editada (DOCX línea 13):

```text
Slope Performance under the design earthquakes is evaluated through successive tiers of analysis including pseudostatic stability checks, simplified estimates of permanent deformation, and dynamic analyses where warranted by the consequences of failure, anticipated response, or complexity of the failure mechanism (International Commission on Large Dams, 2016; Federal Emergency Management Agency, 2005).
```

Cambios:

- [fluidez] `The verification of the slopes under those design earthquakes follows the practice that ICOLD and FEMA frame for dams and embankments through` → `Slope Performance under the design earthquakes is evaluated through`. Reestructuración: nuevo sujeto y voz pasiva; la atribución narrada a ICOLD y FEMA queda sólo en la cita.
- [contenido] `for dams and embankments` → (suprimido). Se suprime el ámbito «dams and embankments».
- [gramática] `those design earthquakes` → `the design earthquakes`. El deíctico pierde su antecedente porque el DOCX omite el párrafo anterior del memo (X01).
- [puntuación] `successive tiers of analysis:` → `successive tiers of analysis including`. Los dos puntos que introducen la enumeración se sustituyen por «including».
- [terminología] `pseudostatic checks` → `pseudostatic stability checks`.
- [terminología] `simplified deformation estimates` → `simplified estimates of permanent deformation`.
- [fluidez] `when the consequence, the anticipated response, or the complexity of the mechanism requires them` → `where warranted by the consequences of failure, anticipated response, or complexity of the failure mechanism`.
- [gramática] en la editada: `Slope Performance`. Mayúscula indebida en «Performance» (error introducido).

Clases: gramática, fluidez, terminología, puntuación, contenido.

#### E05 · DOCX línea 13 · `_chapters/deq.kmax.md:1`

Original (`_chapters/deq.kmax.md:1`):

```text
Within this framework, the Newmark method provides a deformation-based estimate that complements the limit-equilibrium verification, and the pseudostatic coefficient of that verification is a project-specific quantity rather than a universal property of the structure type.
```

Editada (DOCX línea 13):

```text
Within this framework, the Newmark method provides a deformation-based assessment that complements the limit-equilibrium analysis. The pseudostatic seismic coefficient is a project-specific value rather than assigned as a universal value for a particular structure type.
```

Cambios:

- [fluidez] `verification, and the pseudostatic coefficient` → `analysis. The pseudostatic seismic coefficient`. La oración se divide en dos.
- [terminología] `deformation-based estimate` → `deformation-based assessment`.
- [terminología] `limit-equilibrium verification` → `limit-equilibrium analysis`.
- [terminología] `the pseudostatic coefficient of that verification is a project-specific quantity` → `The pseudostatic seismic coefficient is a project-specific value`.
- [gramática] `rather than a universal property of the structure type` → `rather than assigned as a universal value for a particular structure type`. Construcción no paralela («is a ... value rather than assigned as»), error introducido.

Clases: gramática, fluidez, terminología.

#### E06 · DOCX línea 13 · `_chapters/deq.kmax.md:1`

Original (`_chapters/deq.kmax.md:1`):

```text
The USACE manuals EM 1110-2-1902 and EM 1110-2-2100 include pseudostatic analysis among the methods applicable to dams and earthworks and address the sliding block for estimating permanent seismic deformation; they tie the selection of the coefficient to the site-specific hazard, the potential failure mechanism, and the performance criteria of the project, so the coefficient results from the conditions of each project instead of a single value applicable to all of them [@USACE2003; @USACE2005].
```

Editada (DOCX línea 13):

```text
USACE manuals EM 1110-2-1902 and EM 1110-2-2100 discuss pseudostatic analysis sliding block methods for evaluating seismic stability and permanent deformation Selection of the coefficient considers the site-specific seismic hazard, potential failure mechanism, and project performance criteria (U.S. Army Corps of Engineers, 2003; U.S. Army Corps of Engineers, 2005).
```

Cambios:

- [gramática] `The USACE manuals` → `USACE manuals`. Se suprime el artículo.
- [fluidez] `include pseudostatic analysis among the methods applicable to dams and earthworks and address the sliding block for estimating permanent seismic deformation` → `discuss pseudostatic analysis sliding block methods for evaluating seismic stability and permanent deformation`. Condensación.
- [contenido] `applicable to dams and earthworks` → `seismic stability`. Se suprime el ámbito y se añade «seismic stability».
- [gramática] en la editada: `pseudostatic analysis sliding block methods`. Falta la coordinación entre «pseudostatic analysis» y «sliding block methods» (error introducido).
- [puntuación] `deformation; they tie` → `deformation Selection`. Falta el punto entre las dos oraciones (error introducido).
- [fluidez] `they tie the selection of the coefficient to the site-specific hazard, the potential failure mechanism, and the performance criteria of the project` → `Selection of the coefficient considers the site-specific seismic hazard, potential failure mechanism, and project performance criteria`.
- [contenido] `so the coefficient results from the conditions of each project instead of a single value applicable to all of them` → (suprimido). Cláusula final suprimida.

Clases: gramática, fluidez, puntuación, contenido.

Nota: La conversión partió esta oración en tres fragmentos en «U.S.» (línea 13); en el DOCX es una sola oración sin punto intermedio.

#### E07 · DOCX línea 15 · `_chapters/deq.kmax.md:5`

Original (`_chapters/deq.kmax.md:5`):

```text
That objective is expressed as an allowable permanent displacement relative to the slope height.
```

Editada (DOCX línea 15):

```text
The allowable permanent displacement is expressed as a percentage of the reference slope height.
```

Cambios:

- [reordenamiento] `That objective is expressed as an allowable permanent displacement` → `The allowable permanent displacement is expressed as`. El complemento pasa a sujeto porque el DOCX omite el párrafo que daba antecedente a «That objective» (X02).
- [terminología] `relative to the slope height` → `a percentage of the reference slope height`.

Clases: terminología, reordenamiento.

#### E08 · DOCX línea 15 · `_chapters/deq.kmax.md:5`

Original (`_chapters/deq.kmax.md:5`):

```text
The coefficients of this report are read against four damage thresholds of the relative permanent displacement, $D_a/H$ = `r paste(.fmt(DAMAGE.CUTS, 1), collapse = ", ")`%: the crest-settlement ratios derived from ninety case histories of earthquake damage to embankment dams and associated with the Operational, Damage, Life Safety and Collapse limit states of the Italian dam code NTD14 [@Aliberti2019].
```

Editada (DOCX línea 15):

```text
This report evaluates four relative displacement thresholds, $D_{a}/H$ = 0.1, 0.4, 1.0, 2.5%, based on the crest-settlement ratios reported by Alberti et. al. (Aliberti, Biondi, Cascone, & Rampello, 2019).
```

Cambios:

- [fluidez] `The coefficients of this report are read against` → `This report evaluates`.
- [terminología] `damage thresholds of the relative permanent displacement` → `relative displacement thresholds`.
- [puntuación] `%: the crest-settlement` → `%, based on the crest-settlement`. Los dos puntos se sustituyen por «, based on».
- [contenido] `derived from ninety case histories of earthquake damage to embankment dams and associated with the Operational, Damage, Life Safety and Collapse limit states of the Italian dam code NTD14` → `reported by Alberti et. al.`. Se suprimen la procedencia (noventa casos) y los estados límite NTD14.

Clases: fluidez, terminología, puntuación, contenido.

Nota: La mención narrada del autor y su ortografía se registran en N25.

#### E09 · DOCX línea 15 · `_chapters/deq.kmax.md:5`

Original (`_chapters/deq.kmax.md:5`):

```text
Their denominator, the embankment height plus the thickness of the deformable foundation, is the slope height used here.
```

Editada (DOCX línea 15):

```text
The reference height includes the embankment height and the thickness of the deformable foundation and is adopted here as the slope height for normalization.
```

Cambios:

- [fluidez] `Their denominator, the embankment height plus the thickness of the deformable foundation, is the slope height used here.` → `The reference height includes the embankment height and the thickness of the deformable foundation and is adopted here as the slope height for normalization.`.

Clases: fluidez.

#### E10 · DOCX línea 15 · `_chapters/deq.kmax.md:5`

Original (`_chapters/deq.kmax.md:5`):

```text
The coefficient tables are reported at those thresholds and the coefficient figures shade the intervals they delimit; the derivation of the coefficients from the allowable displacement is developed in Chapter [-@sec-coefficients].
```

Testigo memo (`_local/gmdp.memo.en.qmd:70`):

```text
The coefficient tables are reported at those thresholds; the derivation of the coefficients from the allowable displacement is developed in Section [-@sec-coefficients].
```

Editada (DOCX línea 15):

```text
The seismic coefficient tables are presented for these four thresholds. Section [**10.1.3**](#seismic-pseudo-static-coefficients) describes the derivation of the coefficients from the allowable displacement.
```

Cambios:

- [fluidez] `thresholds;` → `thresholds. Section`. La oración se divide en dos.
- [terminología] `The coefficient tables are reported at those thresholds` → `The seismic coefficient tables are presented for these four thresholds`.
- [reordenamiento] `the derivation of the coefficients from the allowable displacement is developed in` → `describes the derivation of the coefficients from the allowable displacement`. Voz activa con la referencia como sujeto.

Clases: fluidez, terminología, reordenamiento.

Nota: El memo (línea 70) no tiene «and the coefficient figures shade the intervals they delimit» (N03); los cambios se miden contra el memo.

### _chapters/ts.model.md

Ensamblado: _docx/gmdp.qmd:12.

#### E11 · DOCX línea 19 · `_chapters/ts.model.md:1`

Original (`_chapters/ts.model.md:1`):

```text
Flexible sliding-block models account for the dynamic response of the potential sliding mass through spectral acceleration evaluated at a period proportional to its fundamental period, so each slope geometry--material combination needs $T_s$, which is derived from the geometry and the depth-dependent small-strain shear stiffness, described by $G_o$, $m_o$, and $V_S^o$; the mean values of $T_s$ and $V_{S30}$ provide the dynamic inputs to the permanent-displacement models.
```

Editada (DOCX línea 19):

```text
Flexible sliding-block models account for the dynamic response of the potential sliding mass through spectral acceleration evaluated at a period proportional to its fundamental period, so each slope geometry–material combination needs $T_{s}$, which is derived from the geometry and the depth-dependent small-strain shear stiffness, described by $G_{o}$, $m_{o}$, and $V_{S}^{o}$; the mean value of $T_{s}$ provides a dynamic input to the permanent-displacement models, while $V_{S30}$ the site conditions used to determine the seismic demand.
```

Cambios:

- [contenido] `the mean values of $T_s$ and $V_{S30}$ provide the dynamic inputs` → `the mean value of $T_{s}$ provides a dynamic input`. $V_{S30}$ deja de figurar como entrada de los modelos de desplazamiento.
- [contenido] (nada) → `while $V_{S30}$ the site conditions used to determine the seismic demand`. Se atribuye a $V_{S30}$ la condición de sitio de la demanda.
- [gramática] en la editada: `while $V_{S30}$ the site conditions`. La cláusula carece de verbo (error introducido).

Clases: gramática, contenido.

Nota: Cambia una afirmación técnica: requiere decisión del propietario.

#### E12 · DOCX línea 27 · `_chapters/ts.model.md:13`

Original (`_chapters/ts.model.md:13`):

```text
The equivalent truncated section in the Dakoulas--Gazetas model [-@DakoulasGazetas1985Inhomogeneous] is specified by the height $H_s$, slope ratio $s$, and truncation ratio $\lambda_o$; with $\tan\beta=1/s$, where $\beta$ is the slope angle, the berm width is
```

Editada (DOCX línea 27):

```text
The equivalent truncated section in the Dakoulas–Gazetas model (1985) is specified by the height $H_{s}$, slope ratio $s$, expressed as horizontal to vertical, and truncation ratio $\lambda_{o}$; with $\tan\beta = 1/s$, where $\beta$ is the slope angle, the crest width is given, for a symmetric section, by
```

Cambios:

- [contenido] `slope ratio $s$, and` → `slope ratio $s$, expressed as horizontal to vertical, and`. Se añade la convención de $s$.
- [terminología] `the berm width is` → `the crest width is`. «crest» no coincide con «berm» de la oración anterior del DOCX (línea 27) ni con la nota de la Tabla 10-1 (línea 143).
- [contenido] (nada) → `for a symmetric section`. Se añade la condición de simetría.
- [fluidez] `the berm width is` → `the crest width is given, for a symmetric section, by`.

Clases: fluidez, terminología, contenido.

#### E13 · DOCX línea 39 · `_chapters/ts.model.md:31`

Original (`_chapters/ts.model.md:31`):

```text
where $G_o$ is the fitted small-strain shear modulus at the base, $g$ is the acceleration of gravity, and $\gamma_{\mathrm{sat}}^{(k_{\mathrm{b}})}$ is the saturated unit weight of the basal layer, whose index is $k_{\mathrm{b}}$; all quantities are expressed in consistent units.
```

Editada (DOCX línea 39):

```text
where $G_{o}$ is the fitted small-strain shear modulus at the base, $g$ is the acceleration of gravity, and $\gamma_{sat}^{(k_{b})}$ is the saturated unit weight of the basal layer, indexed by $k_{b}$; all quantities are expressed in consistent units.
```

Cambios:

- [fluidez] `whose index is $k_{\mathrm{b}}$` → `indexed by $k_{b}$`.

Clases: fluidez.

#### E14 · DOCX línea 51 · `_chapters/ts.model.md:55`

Original (`_chapters/ts.model.md:55`):

```text
where $K_0$ is the at-rest lateral earth pressure coefficient, $\gamma^{(\ell)}$ and $h^{(\ell)}$ are the unit weight adopted for the groundwater condition and the thickness of layer $\ell$, and $\ell<k$ denotes the overlying layers.
```

Editada (DOCX línea 51):

```text
where $K_{0}$ is the at-rest lateral earth pressure coefficient, $\gamma^{(\mathcal{l})}$ and $h^{(\mathcal{l})}$ are the effective unit weight adopted for the groundwater condition and the thickness of layer $\mathcal{l}$, and $\mathcal{l} < k$ denotes the overlying layers.
```

Cambios:

- [contenido] `are the unit weight adopted` → `are the effective unit weight adopted`. Precisa la magnitud; acompaña a la oración añadida S01.

Clases: contenido.

#### E15 · DOCX línea 51, 53, 55 · `_chapters/ts.model.md:55`

Original (`_chapters/ts.model.md:55`):

```text
The layer overconsolidation ratio is $\mathrm{OCR}^{(k)}=\max[(p_m^{(k)}+\mathrm{POP})/p_m^{(k)},1]$, where $\mathrm{POP}$ is the preconsolidation pressure; for fine-grained soils, $m_1^{(k)}=f_{\mathrm{IP}}(\mathrm{IP}^{(k)})$, whereas for sands and gravels $m_1^{(k)}=0$ and the OCR multiplier is therefore unity.
```

Editada (DOCX línea 51, 53, 55):

```text
[línea 51] The layer overconsolidation ratio is
[línea 53] ${OCR}^{(k)} = max\lbrack(p_{m}^{(k)} + POP)/p_{m}^{(k)},1\rbrack$, **[Eq.** **10‑9]**
[línea 55] where $POP$ is the preconsolidation pressure increment, expressed on the same mean-effective-stress basis as $p_{m}^{(k)}$; for fine-grained soils, $m_{1}^{(k)} = f_{IP}({IP}^{(k)})$, where ${IP}^{(k)}$is the plasticity index, whereas for sands and gravels $m_{1}^{(k)} = 0$ and the OCR multiplier is therefore unity.
```

Cambios:

- [contenido] `is the preconsolidation pressure;` → `is the preconsolidation pressure increment, expressed on the same mean-effective-stress basis as $p_{m}^{(k)}$;`. Precisión técnica añadida.
- [contenido] (nada) → `where ${IP}^{(k)}$is the plasticity index,`. Definición de símbolo añadida.

Clases: contenido.

Nota: El DOCX pasa la expresión de OCR de línea a ecuación numerada (N28): la oración editada abarca la línea 51 («The layer overconsolidation ratio is»), la ecuación de la línea 53 y la línea 55.

#### E16 · DOCX línea 68 · `_chapters/ts.model.md:82`

Original (`_chapters/ts.model.md:82`):

```text
For each geometry--material combination, the analysis generates $N$ synthetic realizations of the layered profile, and each of $G_o$, $m_o$, $V_S^o$, and $V_{S30}$ is summarized by its mean and selected marginal fractiles; for the mean and for each reported fractile, $a_1$ and $T_s$ are evaluated from the corresponding $m_o$ and $V_S^o$ values, and the mean estimates provide the dynamic properties used in the displacement analysis.
```

Editada (DOCX línea 68):

```text
For each geometry–material combination, the analysis generates $N$ synthetic realizations of the layered profile, and each of $G_{o}$, $m_{o}$, $V_{S}^{o}$, and $V_{S30}$ is summarized by its mean and selected marginal fractiles; for the mean and for each reported fractile, $a_{1}$ and $T_{s}$ are evaluated from the corresponding $m_{o}$ and $V_{S}^{o}$ values, and the estimates calculated from the mean parameter values provide the dynamic properties used in the displacement analysis.
```

Cambios:

- [fluidez] `the mean estimates provide` → `the estimates calculated from the mean parameter values provide`.

Clases: fluidez.

### _captions/tbl.Ts.md

Ensamblado: _docx/gmdp.qmd:39.

Sin ediciones del otro autor: la leyenda del DOCX sigue a _local/tbl.Ts.md (N16).

### _chapters/dn.ensemble.md

Ensamblado: _docx/gmdp.qmd:46.

#### E17 · DOCX línea 76 · `_chapters/dn.ensemble.md:1`

Original (`_chapters/dn.ensemble.md:1`):

```text
In this report the coefficient is derived from displacement-based performance: the Newmark permanent displacement $D_n$ is the slope-deformation performance measure, and the coefficient $k_{\max}$ is the lowest yield acceleration $k_y$ consistent with a performance objective defined by the allowable displacement $D_a$ and the target probability $p_e$ that $D_n$ exceeds $D_a$.
```

Testigo memo (`_local/gmdp.memo.en.qmd:182`):

```text
In this memo the coefficient is derived from displacement-based performance: the Newmark permanent displacement $D_n$ is the slope-deformation performance measure, and the coefficient $k_{\max}$ is the lowest yield acceleration $k_y$ consistent with a performance objective defined by the allowable displacement $D_a$ and the target probability $p_e$ that $D_n$ exceeds $D_a$.
```

Editada (DOCX línea 76):

```text
In this section the coefficient is derived from displacement-based performance: the Newmark permanent displacement $D_{n}$ is the slope-deformation performance measure, and the coefficient $k_{\max}$ is the lowest yield coefficient $k_{y}$ consistent with a performance objective defined by the allowable displacement $D_{a}$ and the target maximum exceedance probability $p_{e}$, such that $D_{n}$ exceeds $D_{a}$.
```

Cambios:

- [terminología] `lowest yield acceleration $k_y$` → `lowest yield coefficient $k_{y}$`.
- [terminología] `the target probability $p_e$` → `the target maximum exceedance probability $p_{e}$`.
- [gramática] `$p_e$ that $D_n$ exceeds $D_a$` → `$p_{e}$, such that $D_{n}$ exceeds $D_{a}$`. «such that» desplaza la relación: el original define $p_e$ como la probabilidad de que $D_n$ exceda $D_a$.

Clases: gramática, terminología.

Nota: «In this report» (memo: «In this memo») pasa a «In this section»: adaptación al documento receptor (N18).

#### E18 · DOCX línea 76 · `_chapters/dn.ensemble.md:1`

Original (`_chapters/dn.ensemble.md:1`):

```text
The normalized coefficient $k_h$ expresses $k_{\max}$ as a percentage of the PGA after site response is accounted for in each geometry--material combination, and the coefficients are reported by geometry, material and seismic demand.
```

Editada (DOCX línea 76):

```text
The normalized coefficient $k_{h}$ expresses $k_{\max}$ as a percentage of the site-adjusted PGA expressed in units of (g) after site response is accounted for in each geometry–material combination, and the coefficients are reported by geometry, material and seismic demand.
```

Cambios:

- [terminología] `percentage of the PGA after` → `percentage of the site-adjusted PGA expressed in units of (g) after`. «site-adjusted» repite lo que dice «after site response is accounted for».
- [contenido] (nada) → `expressed in units of (g)`. Se añade la unidad.

Clases: terminología, contenido.

#### E19 · DOCX línea 78 · `_chapters/dn.ensemble.md:3`

Original (`_chapters/dn.ensemble.md:3`):

```text
The seismic demand and the fundamental periods established in the preceding chapters allow the $D_n (k_y)$ relations between the Newmark permanent displacement and the yield acceleration to be computed; their inversion yields $k_{\max}$, and its normalization by the PGA transformed to the $V_{S30}$ of each geometry--material combination yields $k_h$, so that the result traceably links the deformation objective to the horizontal action employed in the stability verification.
```

Testigo memo (`_local/gmdp.memo.en.qmd:184`):

```text
The seismic demand and the fundamental periods established in the preceding sections allow the $D_n (k_y)$ relations between the Newmark permanent displacement and the yield acceleration to be computed; their inversion yields $k_{\max}$, and its normalization by the PGA transformed to the $V_{S30}$ of each geometry--material combination yields $k_h$, so that the result traceably links the deformation objective to the horizontal action employed in the stability verification.
```

Editada (DOCX línea 78):

```text
The seismic demand and the fundamental periods established in the preceding sections allow the $D_{n}(k_{y})$ relations between the Newmark permanent displacement and the yield coefficient to be computed; their inversion at the target exceedance probability yields $k_{\max}$, and its normalization by the PGA transformed to the $V_{S30}$ of each geometry–material combination yields $k_{h}$, so that the result traceably links the deformation objective to the horizontal action employed in the stability verification.
```

Cambios:

- [terminología] `and the yield acceleration to be computed` → `and the yield coefficient to be computed`.
- [contenido] `their inversion yields` → `their inversion at the target exceedance probability yields`. Precisión añadida.

Clases: terminología, contenido.

Nota: «preceding sections» frente a «preceding chapters» viene del memo (N08).

#### E20 · DOCX línea 78 · `_chapters/dn.ensemble.md:3`

Original (`_chapters/dn.ensemble.md:3`):

```text
The yield acceleration $a_y$ represents the acceleration level that mobilizes the available resistance along the potential failure mechanism, and its dimensionless form is $k_y=a_y/g$; for each allowable displacement and target exceedance probability, the analysis determines the $k_y$ threshold that satisfies the performance criterion, and that threshold is $k_{\max}$, the coefficient of the pseudostatic limit-equilibrium verification.
```

Editada (DOCX línea 78):

```text
The yield acceleration $a_{y}$ represents the acceleration level at which the limit-equilibrium factor of safety equals unity and its dimensionless form is $k_{y} = a_{y}/g$; for each allowable displacement and target exceedance probability, the analysis determines the minimum $k_{y}$ threshold that satisfies the performance criterion, and that threshold is $k_{\max}$, the coefficient applied in the pseudostatic limit-equilibrium verification.
```

Cambios:

- [contenido] `that mobilizes the available resistance along the potential failure mechanism` → `at which the limit-equilibrium factor of safety equals unity`. Otra definición de $a_y$.
- [puntuación] `failure mechanism, and its dimensionless` → `equals unity and its dimensionless`. Coma suprimida.
- [contenido] `determines the $k_y$ threshold` → `determines the minimum $k_{y}$ threshold`. Se añade «minimum».
- [fluidez] `the coefficient of the pseudostatic` → `the coefficient applied in the pseudostatic`.

Clases: fluidez, puntuación, contenido.

#### E21 · DOCX línea 80 · `_chapters/dn.ensemble.md:5`

Original (`_chapters/dn.ensemble.md:5`):

```text
In the Newmark sliding-block method [@Newmark1965], the wedge in potential sliding is a rigid block resting on an inclined plane: relative motion begins when the driving acceleration exceeds the yield acceleration $a_y=k_y g$ and continues until the relative velocity returns to zero, and the permanent displacement is the sum of those episodes over the duration of the earthquake motion, obtained by double integration of the acceleration excess.
```

Editada (DOCX línea 80):

```text
In the Newmark sliding-block method (Newmark, 1965), the potentially sliding wedge is represented as a rigid block resting on an inclined plane: relative motion begins when the driving acceleration exceeds the yield acceleration $a_{y} = k_{y}g$ and continues until the relative velocity returns to zero, and the permanent displacement is the sum of those episodes over the duration of the earthquake motion, obtained by double integration of the acceleration excess.
```

Cambios:

- [reordenamiento] `the wedge in potential sliding` → `the potentially sliding wedge`.
- [fluidez] `is a rigid block` → `is represented as a rigid block`.

Clases: fluidez, reordenamiento.

#### E22 · DOCX línea 82 · `_chapters/dn.ensemble.md:7`

Original (`_chapters/dn.ensemble.md:7`):

```text
For each geometry, material and seismic demand -- the probabilistic spectrum of each evaluated return period and the MCE scenario -- a joint sample of the intensity measures required by the rigid-block and flexible formulations is constructed; that sample is common to all models, so their differences represent the displacement formulation rather than incompatible seismic demands.
```

Editada (DOCX línea 82):

```text
For each geometry, material and seismic demand – the probabilistic spectrum of each evaluated return period – a joint sample of the intensity measures required by the rigid-block and flexible formulations is constructed; that sample is common to all models, so their differences represent the displacement formulation rather than incompatible seismic demands.
```

Cambios:

- [contenido] `each evaluated return period and the MCE scenario --` → `each evaluated return period –`. Se suprime la demanda MCE.

Clases: contenido.

Nota: El guion «--» convertido en «–» es conversión (N33).

#### E23 · DOCX línea 82 · `_chapters/dn.ensemble.md:7`

Original (`_chapters/dn.ensemble.md:7`):

```text
Two inputs feed that sample. The probabilistic input of each return period is the reference-rock UHS, which for 10,000 years is the MDE, and the MCE input is the rock spectrum of each scenario; both retain the complete distribution of the rock demand, and both are defined for $V_{S30}=V_{\mathrm{ref}}=760$ m/s.
```

Editada (DOCX línea 82):

```text
The input for each return period is the reference-rock UHS, which for 10,000 years represents the MDE; it specifies spectral acceleration ordinates at a common annual exceedance rate and is defined for $V_{S30} = V_{ref} = 760$ m/s.
```

Cambios:

- [contenido] `Two inputs feed that sample.` → (suprimido). Oración suprimida.
- [fluidez] `The probabilistic input of each return period` → `The input for each return period`.
- [terminología] `which for 10,000 years is the MDE` → `which for 10,000 years represents the MDE`.
- [contenido] `and the MCE input is the rock spectrum of each scenario; both retain the complete distribution of the rock demand,` → (suprimido). Se suprimen la entrada MCE y «both retain the complete distribution of the rock demand»; «both are defined» pasa a «is defined».
- [contenido] (nada) → `it specifies spectral acceleration ordinates at a common annual exceedance rate`. Se añade una definición del UHS.

Clases: fluidez, terminología, contenido.

#### E24 · DOCX línea 84 · `_chapters/dn.ensemble.md:9`

Original (`_chapters/dn.ensemble.md:9`):

```text
The Arias intensity used by `JB07` and `SR08` completes the set of intensity measures; it is estimated for each realization from the PGA [@Verri2023a], and the relation is applied deterministically, so that each PGA realization determines a single value of $I_A$ and the displacement sample propagates the PGA variability.
```

Testigo memo (`_local/gmdp.memo.en.qmd:190`):

```text
The Arias intensity that `JB07` and `SR08` require completes the set of intensity measures; it is estimated for each realization from the PGA, so that each PGA realization determines a single value of $I_A$ and the displacement sample propagates the PGA variability.
```

Editada (DOCX línea 84):

```text
The Arias intensity that JB07 and SR08 require completes the set of intensity measures; it is estimated deterministically for each realization from the PGA, so that each PGA realization determines a single value of $I_{A}$ and the displacement sample propagates the PGA variability.
```

Cambios:

- [fluidez] `it is estimated for each realization from the PGA,` → `it is estimated deterministically for each realization from the PGA,`. Inserción frente al memo; el capítulo ya dice «and the relation is applied deterministically».

Clases: fluidez.

Nota: El memo (línea 190) difiere del capítulo: «that ... require» en lugar de «used by», y sin la cita ni la cláusula determinista (N09). El capítulo expresa lo mismo con «[@Verri2023a], and the relation is applied deterministically».

#### E25 · DOCX línea 86 · `_chapters/dn.ensemble.md:11`

Original (`_chapters/dn.ensemble.md:11`):

```text
For each scenario, 30 values of $k_y$ are evaluated, logarithmically distributed between 0.01 and $\max (\overline{\mathrm{PGA}},0.80)$, where $\overline{\mathrm{PGA}}$ is the mean site-condition PGA of the scenario. That interval establishes the computed support of the $D_n (k_y)$ relations, on which the formulations are evaluated and the inversion to $k_{\max}$ operates.
```

Testigo memo (`_local/gmdp.memo.en.qmd:192`):

```text
For each scenario, 30 values of $k_y$ are evaluated, logarithmically distributed between 0.01 and $\max (\overline{\mathrm{PGA}},0.80)$, where $\overline{\mathrm{PGA}}$ is the mean site-condition PGA of the scenario; that interval establishes the computed support of the $D_n (k_y)$ relations, on which the formulations are evaluated and the inversion to $k_{\max}$ operates.
```

Editada (DOCX línea 86):

```text
For each scenario, 30 values of $k_{y}$ are evaluated, logarithmically spaced between 0.01 and $max(\overline{PGA},0.80)$, where $\overline{PGA}$ is the mean site-condition PGA of the scenario; that interval establishes the computed range of the $D_{n}(k_{y})$ relations, over which the formulations are evaluated and the inversion to $k_{\max}$ operates.
```

Cambios:

- [terminología] `logarithmically distributed` → `logarithmically spaced`.
- [terminología] `computed support` → `computed range`.
- [gramática] `on which the formulations` → `over which the formulations`. Preposición.

Clases: gramática, terminología.

Nota: La fusión de las dos oraciones del capítulo con punto y coma viene del memo (N10).

### _chapters/dn.model.md

Ensamblado: _docx/gmdp.qmd:48.

#### E26 · DOCX línea 92 · `_chapters/dn.model.md:7`

Original (`_chapters/dn.model.md:7`):

```text
Some source formulations contain a discrete branch of zero or negligible displacement; the implemented evaluation uses exclusively the positive lognormal branch.
```

Editada (DOCX línea 92):

```text
Some source formulations contain a discrete branch of zero or negligible displacement; the implemented evaluation uses exclusively the positive lognormal branch, conditional on displacement exceeding the model’s zero-or-negligible-displacement threshold.
```

Cambios:

- [contenido] `positive lognormal branch.` → `positive lognormal branch, conditional on displacement exceeding the model’s zero-or-negligible-displacement threshold.`. Cláusula añadida; no aparece en ninguna fuente leída.

Clases: contenido.

#### E27 · DOCX línea 96 · `_chapters/dn.model.md:14`

Original (`_chapters/dn.model.md:14`):

```text
The normalized coefficient, reported as a percentage of the PGA [% of PGA], is calculated with the PGA transformed to the $V_{S30}$ of the geometry--material combination evaluated for each demand:
```

Editada (DOCX línea 96):

```text
The normalized coefficient, reported as a percentage of the PGA [% of PGA], is calculated using the site-adjusted PGA transformed to the $V_{S30}$ of the geometry–material combination evaluated for each demand:
```

Cambios:

- [fluidez] `is calculated with the PGA` → `is calculated using the site-adjusted PGA`.
- [terminología] `the PGA transformed` → `the site-adjusted PGA transformed`. «site-adjusted» repite «transformed to the $V_{S30}$».

Clases: fluidez, terminología.

### _chapters/dn.uncertainty.md

Ensamblado: _docx/gmdp.qmd:50.

#### E28 · DOCX línea 102 · `_chapters/dn.uncertainty.md:1`

Original (`_chapters/dn.uncertainty.md:1`):

```text
The displacement model provides individual realizations for AM88, JB07, SR08, BT07, and a fifth formulation selected by the tectonic context: BM17 for projects with subduction control and BM19 for projects with crustal control.
```

Editada (DOCX línea 102):

```text
The displacement model provides individual realizations for AM88, JB07, SR08, BT07, and a fifth formulation selected by the tectonic context: BM17 for projects with subduction control and BM19 for projects with shallow crustal control.
```

Cambios:

- [terminología] `projects with crustal control` → `projects with shallow crustal control`. Dn.appendix.md:54 usa «ordinary shallow crustal motions» para BM19.

Clases: terminología.

#### E29 · DOCX línea 104 · `_chapters/dn.uncertainty.md:3`

Original (`_chapters/dn.uncertainty.md:3`):

```text
All models receive the same joint sample of PGA and spectral accelerations, and a single realization of $\epsilon$ is shared across the models and across all values of $k_y$; each formulation scales that residual through its own $\sigma_{\ln D}$, and the sampled PGA is retained with each realization so that the inversion keeps its demand state.
```

Editada (DOCX línea 104):

```text
All models receive the same joint sample of PGA and spectral accelerations, and a single realization of $\epsilon$ is shared across the models and across all values of $k_{y}$; each formulation scales that residual through its own $\sigma_{\ln D}$, and the sampled PGA is retained with each realization so that the inversion preserves the pairing between displacement and seismic demand.
```

Cambios:

- [fluidez] `so that the inversion keeps its demand state.` → `so that the inversion preserves the pairing between displacement and seismic demand.`.

Clases: fluidez.

#### E30 · DOCX línea 104 · `_chapters/dn.uncertainty.md:3`

Original (`_chapters/dn.uncertainty.md:3`):

```text
The realizations of $D_n$ are calculated for each material class with its mean dynamic properties; the fractiles of the stiffness profiles and of $T_s$ are reported in Chapter [-@sec-slope_periods] and are not propagated as additional realizations in the displacement calculation, and each material class is kept as an independent input through the inversion to $k_{\max}$, so the displacement curves are not averaged across materials before that operation.
```

Testigo memo (`_local/gmdp.memo.en.qmd:217`):

```text
The realizations of $D_n$ are calculated for each material class with its mean dynamic properties; the fractiles of the stiffness profiles and of $T_s$ are not propagated as additional realizations in the displacement calculation, and each material class is kept as an independent input through the inversion to $k_{\max}$, so the displacement curves are not averaged across materials before that operation.
```

Editada (DOCX línea 104):

```text
The realizations of $D_{n}$ are calculated for each material class with its mean dynamic properties; the fractiles of the stiffness profiles and of $T_{s}$ are not propagated as additional realizations in the displacement calculation, and each material class is kept as an separate scenario through the inversion to $k_{\max}$, so the displacement curves are not averaged across materials before that operation.
```

Cambios:

- [terminología] `an independent input` → `an separate scenario`.
- [gramática] en la editada: `an separate`. Artículo «an» ante consonante (error introducido).

Clases: gramática, terminología.

Nota: «are reported in Chapter [-@sec-slope_periods] and» falta también en el memo (N12).

#### E31 · DOCX línea 106 · `_chapters/dn.uncertainty.md:5`

Original (`_chapters/dn.uncertainty.md:5`):

```text
For each model and realization, the computed $D_n (k_y)$ relation is projected onto a non-increasing curve and inverted in the $(\ln D_n,\ln k_y)$ plane to solve the criterion of [-@eq-kmax-criterion]; when $D_a$ falls outside the calculated support, the relation is extended in that plane from the two points at the corresponding end, with the single exception of the AM88 limit treated in Appendix [-@sec-newmark-appendix].
```

Testigo memo (`_local/gmdp.memo.en.qmd:219`):

```text
For each model and realization, the computed $D_n (k_y)$ relation is projected onto a non-increasing curve and inverted in the $(\ln D_n,\ln k_y)$ plane to solve the criterion of [-@eq-kmax-criterion]; when $D_a$ falls outside the calculated support, the relation is extended in that plane from the two points at the corresponding end, with the single exception of the AM88 limit treated in Section [-@sec-newmark-appendix].
```

Editada (DOCX línea 106):

```text
For each model and realization, the computed $D_{n}(k_{y})$ relation is projected onto a non-increasing curve and inverted in the $(lnD_{n},lnk_{y})$ plane to solve the criterion of [**Eq. 10‑14**](#_Ref_gmdp_eq_eq_kmax_criterion); when $D_{a}$ falls outside the calculated range, the relation is extrapolated in that plane from the two points at the corresponding end, with the single exception of the AM88 limit treated in [**11Appendix E**](#section-2).
```

Cambios:

- [terminología] `the calculated support` → `the calculated range`.
- [terminología] `the relation is extended` → `the relation is extrapolated`.

Clases: terminología.

Nota: Referencias cruzadas en N26; matemática convertida en N29.

#### E32 · DOCX línea 106 · `_chapters/dn.uncertainty.md:5`

Original (`_chapters/dn.uncertainty.md:5`):

```text
The inversion is performed first per model within each realization.
```

Editada (DOCX línea 106):

```text
The inversion is performed first for each model within each realization.
```

Cambios:

- [fluidez] `first per model` → `first for each model`.

Clases: fluidez.

#### E33 · DOCX línea 112 · `_chapters/dn.uncertainty.md:11`

Original (`_chapters/dn.uncertainty.md:11`):

```text
The evaluation uses `r .fmti(NS)` realizations for each demand -- the probabilistic spectrum of each return period $T_R$ = `r paste(prettyNum(round(sort(TR.gmdp), 0), big.mark = ","), collapse = ", ")` years and the MCE -- and a grid of allowable displacements $D_a$ ranging from `r paste(format(range(Da.gmdp), trim = TRUE, scientific = FALSE), collapse = " to ")` cm.
```

Testigo memo (`_local/gmdp.memo.en.qmd:227`):

```text
The evaluation uses `r .fmti(NS)` realizations for each demand -- the probabilistic spectrum of each return period $T_R$ = `r paste(prettyNum(round(sort(TR.target), 0), big.mark = ","), collapse = ", ")` years and the MCE -- and a grid of allowable displacements $D_a/H_s$ ranging from `r paste(format(range(DaH.gmdp), trim = TRUE, scientific = FALSE), collapse = " to ")` %.
```

Editada (DOCX línea 112):

```text
The evaluation uses 300 realizations for each demand – the probabilistic spectrum of each return period $T_{R}$ = 475, 2,475, 10,000 years – and a grid of allowable displacements $D_{a}/H_{s}$ ranging from 0.05 to 2.50 %.
```

Cambios:

- [contenido] `years and the MCE --` → `years –`. Se suprime la demanda MCE.

Clases: contenido.

Nota: «$D_a/H_s$ ... %» frente a «$D_a$ ... cm» viene del memo (N14); valores en N30 y N31.

#### E34 · DOCX línea 112 · `_chapters/dn.uncertainty.md:11`

Original (`_chapters/dn.uncertainty.md:11`):

```text
This grid contains, for every slope height, the damage thresholds $D_a/H$ = `r paste(.fmt(DAMAGE.CUTS, 1), collapse = ", ")`% of Chapter [-@sec-criteria], at which the coefficient tables are reported and which the coefficient figures shade; values of $D_a$ that exceed the calculated support of a realization are obtained through the logarithmic extension defined above.
```

Testigo memo (`_local/gmdp.memo.en.qmd:227`):

```text
This grid contains, for every slope height, the damage thresholds $D_a/H$ = `r paste(.fmt(DAMAGE.CUTS, 1), collapse = ", ")`% of Section [-@sec-criteria], at which the coefficient tables are reported; values of $D_a$ that exceed the calculated support of a realization are obtained through the logarithmic extension defined above.
```

Editada (DOCX línea 112):

```text
This grid contains, for every slope height, the damage thresholds $D_{a}/H$ = 0.1, 0.4, 1.0, 2.5% of Section [**10.1.1**](#seismic-design-criteria-for-slopes), at which the coefficient tables are reported; values of $D_{a}$ that exceed the calculated range of a realization are obtained through the logarithmic extrapolation defined above.
```

Cambios:

- [terminología] `the calculated support of a realization` → `the calculated range of a realization`.
- [terminología] `logarithmic extension` → `logarithmic extrapolation`.

Clases: terminología.

Nota: «and which the coefficient figures shade» falta también en el memo (N15).

### _results/dn.inputs.qmd

Ensamblado: _docx/gmdp.qmd:52.

Sin contraparte en el DOCX (X05).

### _local/gmdp.memo.en.qmd

Ensamblado: fuera del Word propio: master del memo.

#### E35 · DOCX línea 5 · `_local/gmdp.memo.en.qmd:45`

Original (`_local/gmdp.memo.en.qmd:45`):

```text
It reports the dynamic properties of the slopes analysed, the permanent displacements the design earthquakes accumulate in their potential sliding masses, and the performance-based seismic coefficients derived from those displacements.
```

Editada (DOCX línea 5):

```text
This section reports the dynamic properties of the slopes analyzed, the permanent displacements induced by the design earthquakes accumulate in their potential sliding masses, and the performance-based seismic coefficients derived from those displacements.
```

Cambios:

- [gramática] `analysed` → `analyzed`. Ortografía estadounidense.
- [gramática] en la editada: `the permanent displacements induced by the design earthquakes accumulate`. Se inserta «induced by» y se conserva «accumulate»: la oración editada es agramatical (mismo patrón que E01).

Clases: gramática.

Nota: Fuera de la lista nombrada: no tiene contraparte en _chapters/ ni en _results/ (el bloque más cercano, _chapters/executive.opening.md:1, es otra oración). «It reports» pasa a «This section reports» por adaptación (N18).

### _local/tbl.Ts.md

Ensamblado: fuera del Word propio: leyenda del memo.

#### E36 · DOCX línea 132 · `_local/tbl.Ts.md:1`

Original (`_local/tbl.Ts.md:1`):

```text
Fundamental periods $T_s \approx T_1$ [s] and mean dynamic properties of the evaluated scenarios.
```

Editada (DOCX línea 132):

```text
Table 10‑1: Fundamental periods and mean dynamic properties of the evaluated slope scenarios
```

Cambios:

- [contenido] `Fundamental periods $T_s \approx T_1$ [s] and` → `Fundamental periods and`. Se suprimen el símbolo y la unidad.
- [terminología] `the evaluated scenarios.` → `the evaluated slope scenarios`.

Clases: terminología, contenido.

Nota: Fuera de la lista nombrada: leyenda del memo. El prefijo «Table 10-1:» y la falta de punto final son estilo del documento receptor (N20).

### _local/fig.kh.md

Ensamblado: fuera del Word propio: leyenda del memo.

Sin ediciones de redacción: sólo estilo de leyenda y números (N17, N20, N31).

## 2. Sin contraparte

Oraciones del DOCX sin contraparte en `_chapters/*.md` ni en `_results/*.qmd`. Se da la oración nuestra más cercana (leída en esta sesión) y la razón probable.

### S01 · DOCX línea 51

Oración del DOCX:

```text
For hydrostatic groundwater conditions, the bulk unit weight is used above the groundwater table and the submerged unit weight below it; layers intersected by the groundwater table are subdivided accordingly.
```

Más cercana (`_chapters/ts.model.md:55`):

```text
where $K_0$ is the at-rest lateral earth pressure coefficient, $\gamma^{(\ell)}$ and $h^{(\ell)}$ are the unit weight adopted for the groundwater condition and the thickness of layer $\ell$, and $\ell<k$ denotes the overlying layers.
```

Razón probable: Adición del otro autor: explica el peso unitario por encima y por debajo del nivel freático. Ninguna fuente leída lo dice; acompaña al cambio de E14.

### S02 · DOCX línea 66

Oración del DOCX:

```text
The parameters of the stiffness correlations are listed in [Table E‑1](#section-4).
```

Más cercana (`_chapters/ts.model.md:71`):

```text
where $G_m^{(k)}$ is the adopted layer modulus and $\gamma_{\mathrm{sat}}^{(k)}$ is its saturated unit weight; all quantities are expressed in consistent units.
```

Más cercana (`_chapters/ts.model.md:80`):

```text
{{< include /_tbl/SiteGo.qmd >}}
```

Razón probable: Remisión del otro autor a la tabla de correlaciones, que el DOCX lleva al apéndice; nuestro capítulo la incluye en línea (ts.model.md:73-80) inmediatamente después de esta oración, sin oración que la introduzca (N21).

### S03 · DOCX línea 78

Oración del DOCX:

```text
A factor of safety of at least unity under this applied coefficient indicates that the calculated yield coefficient meets or exceeds the required threshold.
```

Más cercana (`_chapters/dn.ensemble.md:3`):

```text
The yield acceleration $a_y$ represents the acceleration level that mobilizes the available resistance along the potential failure mechanism, and its dimensionless form is $k_y=a_y/g$; for each allowable displacement and target exceedance probability, the analysis determines the $k_y$ threshold that satisfies the performance criterion, and that threshold is $k_{\max}$, the coefficient of the pseudostatic limit-equilibrium verification.
```

Razón probable: Adición del otro autor: interpreta el factor de seguridad bajo el coeficiente aplicado; acompaña a la nueva definición de $a_y$ de E20.

### S04 · DOCX línea 116

Oración del DOCX:

```text
[Table 10‑1](#_Ref_gmdp_tbl_periods) presents the fundamental periods and the mean dynamic properties of the slope scenarios evaluated for the Crawford facilities.
```

Más cercana (`_local/tbl.Ts.md:1`):

```text
Fundamental periods $T_s \approx T_1$ [s] and mean dynamic properties of the evaluated scenarios.
```

Razón probable: Párrafo del otro autor que presenta la Tabla 10-1. La oración más cercana es la leyenda del memo; el Word propio no tiene párrafo de presentación.

### S05 · DOCX línea 116

Oración del DOCX:

```text
Each scenario is named with the letter S followed by its slope height in meters.
```

Más cercana (`_local/gmdp.memo.scenarios.csv:2`):

```text
S135,U1
```

Razón probable: Explica la nomenclatura S<altura>. Los nombres S135 ... S35 son nuestros (pares IDg,IDm del memo); la oración es del otro autor.

### S06 · DOCX línea 116

Oración del DOCX:

```text
The scenarios are S135, S50, S32, S27, and S35, which correspond to material identifiers (IDm) U1 to U5 in [Table 10‑1](#_Ref_gmdp_tbl_periods), respectively.
```

Más cercana (`_local/gmdp.memo.scenarios.csv:1`):

```text
IDg,IDm
```

Razón probable: Correspondencia IDg-IDm escrita por el otro autor a partir de nuestros pares; no hay oración nuestra equivalente.

### S07 · DOCX línea 145

Oración del DOCX:

```text
[Figure 10‑1](#_Ref_gmdp_fig_kh_1) through [Figure 10‑3](#_Ref_gmdp_fig_kh_3) show the performance-based horizontal seismic coefficient, expressed as a percentage of the PGA, as a function of the allowable permanent displacement relative to the slope height, for design earthquakes with AEPs of 1:475, 1:2,475, and 1:10,000 years.
```

Más cercana (`_local/fig.kh.md:1`):

```text
Mean values of $k_h$ [%% of PGA] for site %1$s and return period $T_R=%3$s$ yr, as a function of the allowable permanent displacement relative to slope height, $D_a/H$ [%%].
```

Razón probable: Párrafo del otro autor que presenta las figuras; la más cercana es la leyenda del memo. Usa los períodos 475 y 2,475 (N31).

### S08 · DOCX línea 145

Oración del DOCX:

```text
[Table 10‑2](#_Ref_gmdp_tbl_summary) lists the coefficients of the ensemble set at the four relative displacement limits for the 1:2,475 and 1:10,000-year return period design earthquakes.
```

Más cercana (`_results/kmax.results.qmd:6`):

```text
Table [-@`r TBL.KH`] reports, for the MCE and the geometries analysed, the range of the coefficient across the material scenarios at each limit, expressed as a percentage of the PGA.
```

Razón probable: Presenta la Tabla 10-2, que es del otro autor (conjunto ensemble, 1:2,475 y 1:10,000); la oración nuestra más cercana presenta la tabla de rangos MCE.

### S09 · DOCX línea 145

Oración del DOCX:

```text
The coefficients of the rigid and flexible sets, and the coefficients in acceleration units, are included in [**11Appendix E**](#section-2).
```

Más cercana (`_chapters/dn.uncertainty.md:1`):

```text
The five formulations are evaluated individually and combined into the three sets that the tables and figures identify as `IDn`: `rigid`, `flexible` and `ensemble`.
```

Razón probable: Remisión del otro autor a su Apéndice E; sin oración nuestra equivalente.

### S10 · DOCX línea 171

Oración del DOCX:

```text
Table 10‑2: Seismic Coefficients [% of PGA] of the Ensemble Set for Design Earthquakes with AEPs of 1:2,475 and 1:10,000 Years
```

Más cercana (`_local/tbl.kh.md:1`):

```text
Mean values of $k_h$ [%% of PGA] for site %3$s, scenario %1$s, under the MCE demand and return periods $T_R=%2$s$ yr.
```

Más cercana (`_captions/tbl.kh.sites.md:1`):

```text
MCE seismic coefficients $k_h$ [% of PGA] from the ensemble model.
```

Razón probable: Leyenda de la tabla nueva del otro autor; las leyendas nuestras más cercanas son la del memo (por escenario, MCE y períodos) y la del resumen ejecutivo (rangos MCE).

### S11 · DOCX línea 175

Oración del DOCX:

```text
Values are for the ensemble set.
```

Más cercana (`_captions/tbl.kh.sites.md:1`):

```text
MCE seismic coefficients $k_h$ [% of PGA] from the ensemble model.
```

Razón probable: Nota de la tabla nueva.

### S12 · DOCX línea 175

Oración del DOCX:

```text
The column headings give the allowable permanent displacement relative to the slope height, expressed as a percentage.
```

Más cercana (`_captions/tbl.kh.sites.md:1`):

```text
The remaining column headings are the relative displacement limits $D_a/H_s$ [%].
```

Más cercana (`_local/tbl.kh.md:1`):

```text
The coefficient columns report the mean estimate at each allowable permanent displacement relative to slope height, $D_a/H$ [%%], expressed as $100\,k_{\max}/\mathrm{PGA}(V_{S30})$.]
```

Razón probable: Nota de la tabla nueva; reformula nuestras notas de columnas.

### S13 · DOCX línea 175

Oración del DOCX:

```text
The fundamental period of the slope is in seconds and the time-averaged shear-wave velocity of the upper 30 m is in m/s.
```

Más cercana (`_local/tbl.kh.md:1`):

```text
$T_s$ is the fundamental period of the slope [s] and $V_{S30}$ the shear-wave velocity of the evaluated condition [m/s].
```

Razón probable: Nota de la tabla nueva; reformula la nota del memo («time-averaged ... of the upper 30 m» frente a «of the evaluated condition»).

## 3. No es edición a portar

Diferencias que no son ediciones de gramática o fluidez del otro autor. Cada entrada nombra las líneas del DOCX y la explicación.

| Id | Motivo | Líneas DOCX | Explicación |
|---|---|---|---|
| N01 | reescritura nuestra (memo) | 5 | La oración del DOCX reproduce la del memo (_local/gmdp.memo.en.qmd:45), que une en una sola oración lo que _results/ts.results.qmd:6 dice en tres («material scenarios over ... slope geometries», período por clase de material en la ladera más baja y en la más alta). |
| N02 | reescritura nuestra (memo) | 7 | La oración del DOCX sigue al memo (_local/gmdp.memo.en.qmd:53: «is in turn derived», «for the demands and scenarios analysed»), no a las tres oraciones de _results/kmax.results.qmd:6 («for the MCE and the geometries analysed, the range of the coefficient across the material scenarios»). |
| N03 | reescritura nuestra (memo) | 15 | «and the coefficient figures shade the intervals they delimit» está en _chapters/deq.kmax.md:5 y no en el memo (línea 70); su ausencia en el DOCX no es edición del otro autor. |
| N04 | ecuación; reescritura nuestra posterior | 21, 23 | Eq. 10-1 lleva $H_{s}$ en el numerador y la oración siguiente empieza «where $H_{s}$ is the slope height», como el memo (líneas 79 y 82). La fuente actual (_chapters/ts.model.md:4 y 7) usa $H$ y la define como «$H=H_s/(1-\lambda_o)$ is the height of the truncated wedge from the apex of the extended slopes to the base». El archivo cambió en disco durante esta sesión (6044 a 6406 bytes; fecha de modificación 2026-10-12 19:29). |
| N05 | contenido ya integrado en la fuente actual | 23 | «The height from the virtual apex to the base of the equivalent wedge is $\frac{H_{s}}{(1 - \lambda_{o})}.» no está en el memo (línea 82), ni en su HTML (html/gmdp.memo.en/index.html), ni en ninguna otra fuente leída; la fuente actual ya integra esa altura en la definición de $H$ (_chapters/ts.model.md:7). Con los archivos leídos no se puede saber si la oración es del otro autor o de una versión nuestra no conservada. |
| N06 | reescritura nuestra posterior | 43 | La cláusula «the characteristic equation corresponds to the power law with depth measured from the apex of the extended slopes and normalized by $H$ [...] so evaluating $a_1$ with the exponent fitted from the crest is an approximation» de _chapters/ts.model.md:37 no está en el memo (línea 112) ni en el DOCX. |
| N07 | reescritura nuestra (memo) | 43 | «Those layer moduli» (DOCX y memo, línea 112) frente a «The layer moduli» (_chapters/ts.model.md:37). |
| N08 | reescritura nuestra (memo) | 78 | «established in the preceding sections» (DOCX y memo, línea 184) frente a «preceding chapters» (_chapters/dn.ensemble.md:3). |
| N09 | reescritura nuestra (memo) | 84 | «The Arias intensity that JB07 and SR08 require» viene del memo (línea 190); el capítulo dice «used by `JB07` and `SR08`» y añade «[@Verri2023a], and the relation is applied deterministically», que el memo no tiene (_local/gmdp.memo.plan.md:20 registra la retirada de `eq-newmark-arias` y `Verri2023a` en el memo). |
| N10 | reescritura nuestra (memo) | 86 | Las dos oraciones de _chapters/dn.ensemble.md:11 aparecen unidas con punto y coma en el memo (línea 192) y en el DOCX. |
| N11 | reescritura nuestra (memo) | 92 | «according to [-@eq-newmark-arias]» (_chapters/dn.model.md:7) no está en el memo (línea 200) ni en el DOCX. |
| N12 | reescritura nuestra (memo) | 104 | «are reported in Chapter [-@sec-slope_periods] and» (_chapters/dn.uncertainty.md:3) no está en el memo (línea 217) ni en el DOCX. |
| N13 | reescritura nuestra (memo) | 106, 108 | El párrafo de _chapters/dn.uncertainty.md:5 aparece dividido en dos en el memo (líneas 219 y 221) y en el DOCX (líneas 106 y 108). |
| N14 | reescritura nuestra (memo) | 112 | «a grid of allowable displacements $D_{a}/H_{s}$ ranging from ... %» sigue al memo (línea 227); el capítulo dice «$D_a$ ranging from ... cm» (_chapters/dn.uncertainty.md:11). |
| N15 | reescritura nuestra (memo) | 112 | «and which the coefficient figures shade» (_chapters/dn.uncertainty.md:11) no está en el memo (línea 227) ni en el DOCX. |
| N16 | reescritura nuestra (leyenda del memo) | 132, 143 | La leyenda y las notas de la Tabla 10-1 provienen de _local/tbl.Ts.md:1 (leyenda del memo), no de _captions/tbl.Ts.md:1 (leyenda del Word propio, gmdp.qmd:39). Las diferencias entre ambas son nuestras: «$b$ the berm width» frente a «$b$ the geometric parameter», y la cláusula final «and $T_s \approx T_1$ is the fundamental period, in seconds» sólo en _captions/tbl.Ts.md. |
| N17 | reescritura nuestra (leyenda del memo) | 179-199 | Las leyendas y notas de las Figuras 10-1 a 10-3 provienen de _local/fig.kh.md:1 (leyenda del memo); el Word propio (_docx/gmdp.qmd:44-80) no incluye esa figura. Fuera de N20 y N31 no hay cambios de redacción. |
| N18 | adaptación al documento receptor | 5, 76 | «It reports» (memo, línea 45) pasa a «This section reports»; «In this report» (_chapters/dn.ensemble.md:1; memo: «In this memo», línea 182) pasa a «In this section». |
| N19 | estructura del documento receptor | 3, 9, 11, 17, 74, 114, 143 | Encabezados del otro autor: «Slope Design Parameters» (memo: «Ground-Motion Design Parameters», línea 13), «Definitions» (sin contraparte), «Seismic Design Criteria for Slopes» (igual a _docx/sdc.qmd:89 y memo línea 60), «Fundamental Period of the Embankment» (_docx/gmdp.qmd:10: «Dynamic Properties of Slopes»), «Seismic (Pseudo-Static) Coefficients» (_docx/gmdp.qmd:44: «Performance-Based Seismic Coefficient»), «Fundamental Periods of the Crawford Embankments» (sin contraparte) y «Seismic Coefficients» (fundido por la conversión con las notas de la Tabla 10-1, línea 143). |
| N20 | estilo de leyenda del documento receptor | 132, 179, 187, 195 | Prefijos «Table 10-1:» y «Figure 10-x:», mayúscula inicial en cada palabra de las leyendas de figura («Mean Values ... as a Function of the Allowable Permanent Displacement Relative to Slope Height»), sin punto final en la leyenda de la Tabla 10-1 y sin «for site %1$s» (documento de un solo sitio). |
| N21 | estructura del documento receptor | 66 | La tabla de correlaciones que nuestro capítulo incluye en línea (_chapters/ts.model.md:73-80, leyenda tbl.SiteGo) aparece en el DOCX como «Table E-1» del apéndice; la oración que remite a ella es S02. |
| N22 | estilo de cita | 7, 13, 15, 19, 27, 43, 47, 55, 78, 80, 82, 84, 88, 108 | Citas (Autor, Año) o «Autor (Año)» en lugar de claves [@Clave]/[-@Clave]: líneas 7, 13 (dos oraciones), 15, 19, 27, 43, 47, 55, 78, 80 (dos oraciones), 82, 84, 88 y 108; 16 oraciones. |
| N23 | citas añadidas | 7 | El DOCX añade una cita a cada código de modelo: «AM88 (Ambraseys & Menu, 1988), JB07 (Jibson, 2007), SR08 (Saygili & Rathje, 2008), BT07 (Bray & Travasarou, 2007), and BM19 (Bray, Macedo, & Travasauro, 2018)». La de BM19 escribe «Travasauro» y el año 2018; _chapters/dn.appendix.md:54 cita BM19 con [@BrayMacedo2019] y BM17 con [@BrayEtAl2018] (línea 48). |
| N24 | cita: año distinto | 43, 55 | «Ishihara (1997)» frente a la clave [-@Ishihara1996] de _chapters/ts.model.md:37 y 55. |
| N25 | cita narrada | 15 | «reported by Alberti et. al. (Aliberti, Biondi, Cascone, & Rampello, 2019)»: el autor narrado aparece como «Alberti» y con «et. al.»; la fuente cita sólo [@Aliberti2019]. |
| N26 | referencia cruzada (numeración de Word) | 7, 15, 82, 92, 106, 108, 112 | Referencias numeradas del documento receptor en lugar de [-@sec-...]/[-@eq-...]: «Section 10.3» y «11Appendix E» (línea 7), «Section 10.1.3» (15), «Section 10.1.2» (82), «11Appendix E» (92 y 106), «Eq. 10-14» (106), «Eq. 10-16» sin la palabra «expression» (108), «Section 10.1.1» (112). El ancla de «Section 10.3» (línea 7) quedó corrupta en la conversión. |
| N27 | numeración de ecuaciones | 21-110 | Las 16 ecuaciones llevan la numeración de Word «Eq. 10-1» a «Eq. 10-16» en lugar de los identificadores {#eq-...}. |
| N28 | ecuación: forma de presentación | 51-55 | La expresión de OCR, en línea en _chapters/ts.model.md:55, pasa a ecuación numerada (Eq. 10-9, línea 53); su contenido no cambia. |
| N29 | artefactos de conversión en la matemática | 23, 49, 51, 53, 55, 60, 70, 84, 86, 90, 92, 94, 106, 179 | Pérdida de \mathrm y de las barras invertidas de exp, max e inf (líneas 53, 70, 86, 90, 94); \mathcal{l} en lugar de \ell (líneas 49 y 51); «\$» sobrante (23 y 60); «$\ln{(S}_{a})$» (84); «$(lnD_{n},lnk_{y})$» (106); «${IP}^{(k)}$is» sin espacio (55); «$M_{w} =$ 7.0» (92); negritas en la matemática de la leyenda de la Figura 10-1 (179). |
| N30 | números renderizados | 5, 7, 92, 112, 183, 191, 199 | Valores calculados en lugar del código R en línea: 5 escenarios, 27 y 135 m, 0.19 y 0.83 s (línea 5); $M_{w}$ = 7.0 (7, 92) y 300 realizaciones (7, 112); 0.1, 0.4, 1.0, 2.5% (7, 15, 112, 183, 191, 199); 0.05 a 2.50 % (112). Los valores corresponden a la corrida que recibió el otro autor; esta extracción no los coteja. |
| N31 | número: período de retorno | 112, 145, 150-168, 171, 179, 187 | El DOCX rotula 475 y 2,475 años donde el memo usa 500 y 2,500 (TR.target en _local/gmdp.memo.en.qmd:24) y donde el texto alternativo de las propias imágenes del DOCX dice «TR=500 yr» (línea 177) y «TR=2,500 yr» (línea 185). Es un cambio de números del otro autor, contrario a la premisa de que no tocó números; no se porta y queda para decisión del coordinador. |
| N32 | formato perdido en la conversión | 7, 82, 84, 102, 143, 179-199 | Se pierden los acentos graves de código: `ensemble`, `rigid`, `flexible`, `IDn`, `IDm`, `USCS`, `ST20`, `JB07`, `SR08`. |
| N33 | conversión de guiones | 5, 19, 27, 55, 68, 76, 78, 82, 92, 96, 112 | «--» pasa a «–» («geometry–material», «Dakoulas–Gazetas», «Shibata–Soelarno», incisos de las líneas 82, 92 y 112). |
| N34 | conversión de la lista de notas | 134-143 | Las notas de la Tabla 10-1 eran una lista de seis viñetas: la conversión deja seis viñetas vacías (líneas 136-141), funde el texto con el encabezado «Seismic Coefficients» (línea 143) y pierde los punto y coma entre elementos («both in m$s$», «dimensionless$a_{1}$», «dimensionless$V_{S}^{o}$»). |
| N35 | texto alternativo de imágenes | 177, 185, 193 | El texto alternativo de las tres imágenes conserva nuestras leyendas del memo truncadas, numeradas «Fig. 5» a «Fig. 7» (línea 177: «Mean values of kh [% of PGA] for site CFD and return period TR=500 yr, ...»). |
| N36 | artefactos de anclas | 94, 110, 132, 171, 179, 187, 195 | Spans de ancla «[]{#_Ref_gmdp_... .anchor}» y restos «${}_{}$» (187, 195) de la conversión. |

## 4. Contenido nuestro sin contraparte en la sección del DOCX

| Id | Fuente | Observación |
|---|---|---|
| X01 | `_local/gmdp.memo.en.qmd:64 (de _chapters/deq.criteria.md:1 y :9)` | El párrafo del marco OBE/SEE y la definición de MDE y MCE con que el memo abre «Seismic Design Criteria for Slopes» no aparece en la sección del DOCX. Supresión o traslado del otro autor; el DOCX puede tratarlo en otro capítulo que este extracto no contiene. |
| X02 | `_chapters/deq.kmax.md:3 (memo línea 68)` | El párrafo de NCHRP Report 611 y Eurocode 8 (tres oraciones) no aparece en el DOCX. Supresión del otro autor; deja sin antecedente «That objective» (E07). |
| X03 | `_local/gmdp.memo.en.qmd:229-266` | Las figuras y tablas del memo para $k_{max}$, para la demanda MCE y por escenario no aparecen; el DOCX pone sus Figuras 10-1 a 10-3 ($k_h$, tres períodos) y su Tabla 10-2. |
| X04 | `_chapters/dn.appendix.md (memo líneas 268-327)` | Las formulaciones están en el Apéndice E del DOCX, fuera del extracto; no se compararon. |
| X05 | `_results/dn.inputs.qmd:12` | Bloque del Word propio (_docx/gmdp.qmd:52) que el memo no incluye; bajo la inferencia del punto 2 del método, el otro autor no lo recibió. |
| X06 | `_chapters/deq.criteria.md:3-11 (salvo :9 primera oración)` | Capítulo del Word propio (_docx/sdc.qmd:91) que el memo no incluye. |

## 5. Cobertura

Cada oración del DOCX, en orden, con su resultado. Las ecuaciones (líneas 21-110) se tratan en N04, N27, N28 y N29; las celdas de las Tablas 10-1 y 10-2 son números y quedan fuera de la extracción.

| # | Línea | Inicio | Resultado |
|---:|---:|---|---|
| 1 | 5 | `This section reports` | E35 |
| 2 | 5 | `The flexible sliding-block` | sin edición (N01, N30) |
| 3 | 7 | `The Newmark permanent` | E01 |
| 4 | 7 | `The $D_{n}(k_{y})$ curves` | E02 |
| 5 | 7 | `The horizontal pseudostatic` | E03 |
| 6 | 13 | `Slope Performance` | E04 |
| 7 | 13 | `Within this framework` | E05 |
| 8 | 13 | `The pseudostatic seismic coefficient` | E05 |
| 9 | 13 | `USACE manuals` | E06 |
| 10 | 15 | `The allowable permanent displacement` | E07 |
| 11 | 15 | `This report evaluates` | E08 |
| 12 | 15 | `The reference height` | E09 |
| 13 | 15 | `The seismic coefficient tables` | E10 |
| 14 | 15 | `Section [**10.1.3**]` | E10 |
| 15 | 19 | `Flexible sliding-block` | E11 |
| 16 | 19 | `The fundamental period of the potential` | sin edición (N22) |
| 17 | 23 | `where $H_{s}$ is the slope height` | sin edición (N04) |
| 18 | 23 | `The height from the virtual apex` | sin edición (N05) |
| 19 | 23 | `The modal root` | sin edición (N29) |
| 20 | 27 | `where $b$` | sin diferencias de redacción |
| 21 | 27 | `The equivalent truncated` | E12 |
| 22 | 31 | `and the base width is` | sin diferencias de redacción |
| 23 | 35 | `For each profile realization` | sin diferencias de redacción |
| 24 | 39 | `where $G_{o}$` | E13 |
| 25 | 39 | `The depth dependence` | sin diferencias de redacción |
| 26 | 43 | `where $z$` | sin edición (N06) |
| 27 | 43 | `Those layer moduli` | sin edición (N07, N22, N24) |
| 28 | 47 | `Here $A^{(j)}$` | sin diferencias de redacción |
| 29 | 47 | `Under at-rest` | sin edición (N22) |
| 30 | 51 | `where $K_{0}$` | E14 |
| 31 | 51 | `For hydrostatic` | S01 |
| 32 | 51 | `The layer overconsolidation ratio is` | E15 |
| 33 | 55 | `The void ratio` | sin edición (N22, N24, N33) |
| 34 | 62 | `The shear-wave velocity of layer` | sin diferencias de redacción |
| 35 | 66 | `where $G_{m}^{(k)}$` | sin diferencias de redacción |
| 36 | 66 | `The parameters of the stiffness` | S02 |
| 37 | 68 | `For each geometry` | E16 |
| 38 | 68 | `$V_{S30}$ is the travel` | sin diferencias de redacción |
| 39 | 72 | `In this expression` | sin diferencias de redacción |
| 40 | 76 | `Pseudostatic seismic design` | sin diferencias de redacción |
| 41 | 76 | `In this section` | E17 |
| 42 | 76 | `The normalized coefficient $k_{h}$` | E18 |
| 43 | 76 | `For the slopes considered` | sin diferencias de redacción |
| 44 | 78 | `The horizontal pseudostatic coefficient is derived` | sin edición (N22) |
| 45 | 78 | `The seismic demand and` | E19 |
| 46 | 78 | `The yield acceleration $a_{y}$` | E20 |
| 47 | 78 | `A factor of safety` | S03 |
| 48 | 80 | `In the Newmark sliding-block` | E21 |
| 49 | 80 | `The extension of the procedure` | sin edición (N22) |
| 50 | 80 | `The adopted empirical` | sin diferencias de redacción |
| 51 | 82 | `The displacement calculation uses` | sin edición (N26) |
| 52 | 82 | `For each geometry, material` | E22 |
| 53 | 82 | `The input for each return period` | E23 |
| 54 | 82 | `For each geometry and material scenario` | sin edición (N22, N32) |
| 55 | 84 | `At the site condition` | sin diferencias de redacción |
| 56 | 84 | `The three measures` | sin edición (N22, N29) |
| 57 | 84 | `The Arias intensity` | E24 |
| 58 | 86 | `For each scenario, 30` | E25 |
| 59 | 88 | `Each active formulation` | sin edición (N22) |
| 60 | 92 | `where $\mu_{\ln D}$` | sin diferencias de redacción |
| 61 | 92 | `Some source formulations` | E26 |
| 62 | 92 | `In every formulation` | sin edición (N11, N29, N30) |
| 63 | 92 | `The published form` | sin edición (N26) |
| 64 | 92 | `The performance-based seismic coefficient is defined by` | sin diferencias de redacción |
| 65 | 96 | `where $p_{e}$` | sin diferencias de redacción |
| 66 | 96 | `The normalized coefficient, reported` | E27 |
| 67 | 100 | `$k_{\max}$ is expressed` | sin diferencias de redacción |
| 68 | 100 | `These two quantities` | sin diferencias de redacción |
| 69 | 102 | `The five formulations` | sin edición (N32) |
| 70 | 102 | `The displacement model provides` | E28 |
| 71 | 102 | `The overall design set` | sin edición (N32) |
| 72 | 102 | `The rigid family thus` | sin diferencias de redacción |
| 73 | 102 | `For each $k_{y}$` | sin diferencias de redacción |
| 74 | 104 | `All models receive` | E29 |
| 75 | 104 | `The realizations of` | E30 |
| 76 | 106 | `For each model and realization` | E31 |
| 77 | 106 | `The inversion is performed` | E32 |
| 78 | 108 | `The root distributions` | sin edición (N13, N22) |
| 79 | 108 | `Because of the decreasing` | sin edición (N26) |
| 80 | 112 | `The $q$ fractiles` | sin diferencias de redacción |
| 81 | 112 | `The evaluation uses` | E33 |
| 82 | 112 | `This grid contains` | E34 |
| 83 | 116 | `[Table 10‑1](#_Ref_gmdp_tbl_periods) presents` | S04 |
| 84 | 116 | `Each scenario is named` | S05 |
| 85 | 116 | `The scenarios are S135` | S06 |
| 86 | 132 | `Table 10‑1: ` | E36 |
| 87 | 143 | `IDm identifies` | sin edición (N16, N32, N34) |
| 88 | 143 | `$H_{s}$ is the slope` | sin edición (N16, N34) |
| 89 | 145 | `[Figure 10‑1]` | S07 |
| 90 | 145 | `[Table 10‑2]` | S08 |
| 91 | 145 | `The coefficients of the rigid` | S09 |
| 92 | 171 | `Table 10‑2: ` | S10 |
| 93 | 175 | `Values are for` | S11 |
| 94 | 175 | `The column headings` | S12 |
| 95 | 175 | `The fundamental period of the slope` | S13 |
| 96 | 179 | `Figure 10‑1: ` | sin edición (N17, N20, N29, N31) |
| 97 | 179 | `The Curves` | sin edición (N20) |
| 98 | 183 | `The coefficient is expressed` | sin edición (N29) |
| 99 | 183 | `Color identifies` | sin edición (N32) |
| 100 | 183 | `The shaded bands` | sin edición (N30) |
| 101 | 187 | `Figure 10‑2: ` | sin edición (N20, N31) |
| 102 | 187 | `The Curves` | sin edición (N20) |
| 103 | 191 | `The coefficient is expressed` | sin edición (N29) |
| 104 | 191 | `Color identifies` | sin edición (N32) |
| 105 | 191 | `The shaded bands` | sin edición (N30) |
| 106 | 195 | `Figure 10‑3: ` | sin edición (N20) |
| 107 | 195 | `The Curves` | sin edición (N20) |
| 108 | 199 | `The coefficient is expressed` | sin edición (N29) |
| 109 | 199 | `Color identifies` | sin edición (N32) |
| 110 | 199 | `The shaded bands` | sin edición (N30) |
