# Ediciones del otro autor en «Slope Design Parameters» (CAPR003324): extracción A1

Inventario oración por oración de las ediciones de gramática, fluidez y legibilidad que el otro autor hizo en el capítulo «Slope Design Parameters» del DOCX `CAPR003324_Crawford_SeismicHazard_Final`, comparadas con nuestros textos fuente. Las ecuaciones, los números, las citas y las remisiones no se tocan: van en la lista «no es edición a portar» de `SUMMARY.md` (N01–N25), y aquí sólo se remite a ella.

## Cómo leer este inventario

- Insumo editado: `docx/CAPR003324_Crawford_SeismicHazard_Final.slope-design-parameters.md`, con citas por número de línea («DOCX 13»).
- Las secciones siguen el orden de ensamblado de nuestro Word (`_master/docx.en.qmd:8–14`): resumen ejecutivo, sdc, gmdp y apéndices. Dentro de cada sección se agrupa por archivo fuente.
- Cada entrada (E01–E32) es una oración nuestra que el otro autor editó. Trae la oración original actual (archivo y línea), la versión del memo que recibió el otro autor, la oración editada y la lista de cambios. Cada cambio lleva una clase: gramática, fluidez, terminología, puntuación o reordenamiento.
- Testigo: `_local/gmdp.memo.en.qmd` (memo del 2026-09-24). Donde la fuente actual difiere, el DOCX coincide con el memo, por lo que el memo es la versión que editó el otro autor. Cuando la fuente actual cambió después, la diferencia es nuestra y no del otro autor (N10–N20). Los cambios marcados «sobre el texto del memo» se leen contra la cita del memo.
- Marcas: «contenido técnico» si el cambio altera o agrega contenido, no sólo redacción, y lo decide el propietario. «Error introducido» si el texto del DOCX trae un error que no debe copiarse literal. «Ya cubierta» si la fuente actual ya dice lo mismo.
- Las citas en inglés están copiadas textualmente de los archivos. Las de la fuente actual corresponden a `_chapters/ts.model.md` en su versión de 6406 bytes (cambió durante la sesión; ver `SUMMARY.md`).

## 1. Resumen ejecutivo — `_docx/executive.site.qmd:48–52`

### `_results/ts.results.qmd`

Sin ediciones del otro autor. La segunda oración de DOCX 5 corresponde a la primera de ts.results.qmd:6 tal como la compuso el memo (_local/gmdp.memo.en.qmd:45); el resto son números renderizados (N05, N20).

### `_results/dn.results.qmd` (2 oraciones editadas)

#### E01 · `_results/dn.results.qmd:7` · DOCX 7

Clase principal: **terminología** · Marcas: error introducido

Original actual (`_results/dn.results.qmd:7`):

> The Newmark permanent displacement $D_n$ quantifies the deformation an earthquake accumulates in the sliding mass and is the performance measure from which the seismic coefficients are derived.

Memo recibido (`_local/gmdp.memo.en.qmd:53`): idéntica.

Editada (DOCX línea 7):

> The Newmark permanent displacement $D_{n}$ quantifies the displacement induced by an earthquake accumulates in the sliding mass and is the performance measure from which the seismic coefficients are derived.

Cambios:

- **E01a** · terminología · «quantifies the deformation» → «quantifies the displacement». «displacement» en lugar de «deformation».
- **E01b** · gramática [error introducido] · «an earthquake accumulates» → «induced by an earthquake accumulates». «accumulates» queda sin sujeto. Si se adopta «displacement», la frase debe reescribirse (p. ej. «the displacement an earthquake accumulates»).

#### E02 · `_results/dn.results.qmd:7` · DOCX 7

Clase principal: **gramática**

Original actual (`_results/dn.results.qmd:7`):

> The $D_n(k_y)$ curves relate, for each combination of geometry, material, and design scenario, the yield acceleration $k_y$ to the expected permanent displacement; they were computed with the `ensemble` set of `AM88`, `JB07`, `SR08`, `BT07`, and `r BM.code`, with the reference magnitude $M_w$ = `r .fmt(Mw.gmdp, 1)` and `r .fmti(NS)` realizations per demand, and are read at the fractiles $q = 1 - p_e$.

Memo recibido (`_local/gmdp.memo.en.qmd:53`): idéntica.

Editada (DOCX línea 7):

> The $D_{n}(k_{y})$ curves relate, for each combination of geometry, material, and design scenario, the yield acceleration $k_{y}$ to the expected permanent displacement; they were computed with an ensemble set of AM88 (Ambraseys & Menu, 1988), JB07 (Jibson, 2007), SR08 (Saygili & Rathje, 2008), BT07 (Bray & Travasarou, 2007), and BM19 (Bray, Macedo, & Travasauro, 2018), with the reference magnitude $M_{w}$ = 7.0 and 300 realizations per demand and are read at the fractiles $q = 1 - p_{e}$.

Cambios:

- **E02a** · gramática · «with the `ensemble` set of» → «with an ensemble set of». Artículo indefinido y sin formato de identificador. Nuestro texto nombra el conjunto `ensemble` que define dn.uncertainty.md:1.
- **E02b** · puntuación · «per demand, and are read» → «per demand and are read». Suprime la coma antes de «and».

Nota: Las citas añadidas a cada modelo y los valores 7.0 y 300 no son ediciones a portar (N03, N05).

### `_results/kmax.results.qmd` (1 oración editada)

#### E03 · `_results/kmax.results.qmd:6` · DOCX 7

Clase principal: **gramática**

Original actual (`_results/kmax.results.qmd:6`):

> The horizontal pseudostatic coefficient $k_h$ is derived from the allowable permanent displacement $D_a$ of the potentially sliding mass [@BrayTravasarou2009; @MacedoEtAl2018]. The coefficients are reported at four relative displacement limits, $D_a/H_s$ = `r paste(.fmt(DAMAGE.CUTS, 1), collapse = ", ")`%. Table [-@`r TBL.KH`] reports, for the MCE and the geometries analysed, the range of the coefficient across the material scenarios at each limit, expressed as a percentage of the PGA.

Memo recibido (`_local/gmdp.memo.en.qmd:53`):

> The horizontal pseudostatic coefficient $k_h$ is in turn derived from the allowable permanent displacement $D_a$ of the potentially sliding mass [@BrayTravasarou2009; @MacedoEtAl2018]; the coefficients are reported at four relative displacement limits, $D_a/H_s$ = `r paste(.fmt(DAMAGE.CUTS, 1), collapse = ", ")`%, and the tables in Section [-@sec-kh-tables] report, for the demands and scenarios analysed, the coefficient at each limit, expressed as a percentage of the PGA.

Editada (DOCX línea 7):

> The horizontal pseudostatic coefficient $k_{h}$ is in turn derived from the allowable permanent displacement $D_{a}$ of the potentially sliding mass (Bray & Travasarou, Pseudostatic Coefficient for Use in Simplified Seismic Slope Stability Evaluation, 2009; Macedo, Bray, Abrahamson, & Travasarou, 2018); the coefficients are reported at four relative displacement limits, $D_{a}/H_{s}$ = 0.1, 0.4, 1.0, 2.5%, and the tables in Section [**10.3**](#idm-identifies-the-material-scenario-and-uscs-the-classification-of-the-slope-materials.-h_s-is-the-slope-height-and-b-the-berm-width-both-in-ms-is-the-slope-ratio-tanbeta-1s-and-lambda_o-the-truncation-ratio-both-dimensionless-g_o-is-the-shear-modulus-of-the-profile-at-zh_s-1-in-mpa-and-m_o-the-exponent-of-its-power-law-dimensionlessa_1-is-the-first-modal-root-dimensionlessv_so-is-the-basal-shear-wave-velocity-and-v_s30-the-travel-time-averaged-shear-wave-velocity-in-the-uppermost-30-m-both-in-ms.seismic-coefficients) and [**11Appendix E**](#section-2) report, for the demands and scenarios analyzed, the coefficient at each limit, expressed as a percentage of the PGA.

Cambios:

- **E03a** · gramática (sobre el texto del memo) · «scenarios analysed» → «scenarios analyzed». Ortografía estadounidense. En la fuente actual la palabra aparece en «the geometries analysed».

Nota: La composición en una sola oración viene del memo (N20). Las remisiones a 10.3 y al Apéndice E son numeración de Word (N01).

## 2. Seismic Design Criteria for Slopes — `_docx/sdc.qmd:89–93`

### `_chapters/deq.criteria.md`

Ninguna oración aparece en la sección extraída del DOCX (O1).

### `_chapters/deq.kmax.md` (7 oraciones editadas)

El párrafo deq.kmax.md:3 (NCHRP/Eurocode) no aparece en el DOCX (O2).

#### E04 · `_chapters/deq.kmax.md:1` · DOCX 13

Clase principal: **fluidez** · Marcas: contenido técnico, error introducido

Original actual (`_chapters/deq.kmax.md:1`):

> The verification of the slopes under those design earthquakes follows the practice that ICOLD and FEMA frame for dams and embankments through successive tiers of analysis: pseudostatic checks, simplified deformation estimates, and dynamic analyses when the consequence, the anticipated response, or the complexity of the mechanism requires them [@ICOLD2016; @FEMA2005].

Memo recibido (`_local/gmdp.memo.en.qmd:66`): idéntica.

Editada (DOCX línea 13):

> Slope Performance under the design earthquakes is evaluated through successive tiers of analysis including pseudostatic stability checks, simplified estimates of permanent deformation, and dynamic analyses where warranted by the consequences of failure, anticipated response, or complexity of the failure mechanism (International Commission on Large Dams, 2016; Federal Emergency Management Agency, 2005).

Cambios:

- **E04a** · fluidez [contenido técnico] [error introducido] · «The verification of the slopes under those design earthquakes follows the practice that ICOLD and FEMA frame for dams and embankments through» → «Slope Performance under the design earthquakes is evaluated through». Pasa el sujeto a «Slope Performance» y el verbo a voz pasiva. Saca del texto la atribución a ICOLD y FEMA y el ámbito «for dams and embankments», que quedan sólo en la cita. Cambia «those» por «the» porque el DOCX no trae el párrafo anterior (deq.criteria.md). La mayúscula de «Performance» es una errata.
- **E04b** · puntuación · «tiers of analysis: pseudostatic» → «tiers of analysis including pseudostatic». La lista ya no va tras dos puntos: la introduce «including».
- **E04c** · terminología · «pseudostatic checks, simplified deformation estimates,» → «pseudostatic stability checks, simplified estimates of permanent deformation,». Precisa «stability» y «permanent deformation».
- **E04d** · fluidez · «when the consequence, the anticipated response, or the complexity of the mechanism requires them» → «where warranted by the consequences of failure, anticipated response, or complexity of the failure mechanism». Usa «where warranted by». También cambia términos: «consequences of failure» y «failure mechanism».

#### E05 · `_chapters/deq.kmax.md:1` · DOCX 13

Clase principal: **reordenamiento** · Marcas: error introducido

Original actual (`_chapters/deq.kmax.md:1`):

> Within this framework, the Newmark method provides a deformation-based estimate that complements the limit-equilibrium verification, and the pseudostatic coefficient of that verification is a project-specific quantity rather than a universal property of the structure type.

Memo recibido (`_local/gmdp.memo.en.qmd:66`): idéntica.

Editada (DOCX línea 13):

> Within this framework, the Newmark method provides a deformation-based assessment that complements the limit-equilibrium analysis. The pseudostatic seismic coefficient is a project-specific value rather than assigned as a universal value for a particular structure type.

Cambios:

- **E05a** · reordenamiento · «, and the pseudostatic coefficient of that verification is» → «. The pseudostatic seismic coefficient is». Parte la oración en dos. La segunda pierde el vínculo «of that verification» y agrega «seismic».
- **E05b** · terminología · «deformation-based estimate» → «deformation-based assessment».
- **E05c** · terminología · «limit-equilibrium verification» → «limit-equilibrium analysis». Nuestro capítulo usa «verification» para la comprobación pseudoestática (dn.ensemble.md:3, dn.model.md:20), así que el cambio rompe esa coherencia.
- **E05d** · terminología · «project-specific quantity» → «project-specific value».
- **E05e** · gramática [error introducido] · «rather than a universal property of the structure type» → «rather than assigned as a universal value for a particular structure type». «is a … value rather than assigned as» no es paralelo. Si se adopta la idea, hay que corregir la sintaxis.

#### E06 · `_chapters/deq.kmax.md:1` · DOCX 13

Clase principal: **fluidez** · Marcas: contenido técnico, error introducido

Original actual (`_chapters/deq.kmax.md:1`):

> The USACE manuals EM 1110-2-1902 and EM 1110-2-2100 include pseudostatic analysis among the methods applicable to dams and earthworks and address the sliding block for estimating permanent seismic deformation; they tie the selection of the coefficient to the site-specific hazard, the potential failure mechanism, and the performance criteria of the project, so the coefficient results from the conditions of each project instead of a single value applicable to all of them [@USACE2003; @USACE2005].

Memo recibido (`_local/gmdp.memo.en.qmd:66`): idéntica.

Editada (DOCX línea 13):

> USACE manuals EM 1110-2-1902 and EM 1110-2-2100 discuss pseudostatic analysis sliding block methods for evaluating seismic stability and permanent deformation Selection of the coefficient considers the site-specific seismic hazard, potential failure mechanism, and project performance criteria (U.S. Army Corps of Engineers, 2003; U.S. Army Corps of Engineers, 2005).

Cambios:

- **E06a** · gramática · «The USACE manuals» → «USACE manuals». Omite el artículo inicial.
- **E06b** · fluidez [contenido técnico] [error introducido] · «include pseudostatic analysis among the methods applicable to dams and earthworks and address the sliding block for estimating permanent seismic deformation» → «discuss pseudostatic analysis sliding block methods for evaluating seismic stability and permanent deformation». Condensa la frase y pierde «applicable to dams and earthworks». Error introducido: falta una conjunción entre «pseudostatic analysis» y «sliding block methods».
- **E06c** · puntuación [error introducido] · «deformation; they tie» → «deformation Selection». Falta el punto antes de «Selection» y el DOCX une dos oraciones.
- **E06d** · fluidez · «they tie the selection of the coefficient to the site-specific hazard, the potential failure mechanism, and the performance criteria of the project» → «Selection of the coefficient considers the site-specific seismic hazard, potential failure mechanism, and project performance criteria». Usa el verbo «considers» en lugar de «tie … to», suprime los artículos de la enumeración y escribe «site-specific seismic hazard».
- **E06e** · fluidez [contenido técnico] · supresión de «, so the coefficient results from the conditions of each project instead of a single value applicable to all of them». Es la conclusión de la oración.

#### E07 · `_chapters/deq.kmax.md:5` · DOCX 15

Clase principal: **fluidez**

Original actual (`_chapters/deq.kmax.md:5`):

> That objective is expressed as an allowable permanent displacement relative to the slope height.

Memo recibido (`_local/gmdp.memo.en.qmd:70`): idéntica.

Editada (DOCX línea 15):

> The allowable permanent displacement is expressed as a percentage of the reference slope height.

Cambios:

- **E07a** · fluidez · «That objective is expressed as an allowable permanent displacement» → «The allowable permanent displacement is expressed». Quita la anáfora «That objective», que en nuestro texto remite al párrafo deq.kmax.md:3 que el DOCX omite.
- **E07b** · terminología · «relative to the slope height» → «as a percentage of the reference slope height». Escribe «reference slope height» y anticipa que se expresa en porcentaje.

#### E08 · `_chapters/deq.kmax.md:5` · DOCX 15

Clase principal: **fluidez** · Marcas: contenido técnico, error introducido

Original actual (`_chapters/deq.kmax.md:5`):

> The coefficients of this report are read against four damage thresholds of the relative permanent displacement, $D_a/H$ = `r paste(.fmt(DAMAGE.CUTS, 1), collapse = ", ")`%: the crest-settlement ratios derived from ninety case histories of earthquake damage to embankment dams and associated with the Operational, Damage, Life Safety and Collapse limit states of the Italian dam code NTD14 [@Aliberti2019].

Memo recibido (`_local/gmdp.memo.en.qmd:70`): idéntica.

Editada (DOCX línea 15):

> This report evaluates four relative displacement thresholds, $D_{a}/H$ = 0.1, 0.4, 1.0, 2.5%, based on the crest-settlement ratios reported by Alberti et. al. (Aliberti, Biondi, Cascone, & Rampello, 2019).

Cambios:

- **E08a** · fluidez · «The coefficients of this report are read against four damage thresholds of the relative permanent displacement» → «This report evaluates four relative displacement thresholds». Pone «This report» como sujeto con el verbo «evaluates» y omite «damage».
- **E08b** · fluidez [contenido técnico] [error introducido] · «: the crest-settlement ratios derived from ninety case histories of earthquake damage to embankment dams and associated with the Operational, Damage, Life Safety and Collapse limit states of the Italian dam code NTD14» → «, based on the crest-settlement ratios reported by Alberti et. al.». Omite de dónde salen los umbrales (noventa casos históricos y estados límite de NTD14). En «Alberti et. al.» el apellido está mal escrito y «et al.» mal puntuado (N04).

Nota: Los valores 0.1, 0.4, 1.0 y 2.5 % son números renderizados (N05).

#### E09 · `_chapters/deq.kmax.md:5` · DOCX 15

Clase principal: **fluidez**

Original actual (`_chapters/deq.kmax.md:5`):

> Their denominator, the embankment height plus the thickness of the deformable foundation, is the slope height used here.

Memo recibido (`_local/gmdp.memo.en.qmd:70`): idéntica.

Editada (DOCX línea 15):

> The reference height includes the embankment height and the thickness of the deformable foundation and is adopted here as the slope height for normalization.

Cambios:

- **E09a** · terminología · «Their denominator, the embankment height plus» → «The reference height includes the embankment height and». Escribe «reference height» en lugar de «Their denominator».
- **E09b** · fluidez · «, is the slope height used here.» → «and is adopted here as the slope height for normalization.». Explicita el propósito: «for normalization».

#### E10 · `_chapters/deq.kmax.md:5` · DOCX 15

Clase principal: **reordenamiento**

Original actual (`_chapters/deq.kmax.md:5`):

> The coefficient tables are reported at those thresholds and the coefficient figures shade the intervals they delimit; the derivation of the coefficients from the allowable displacement is developed in Chapter [-@sec-coefficients].

Memo recibido (`_local/gmdp.memo.en.qmd:70`):

> The coefficient tables are reported at those thresholds; the derivation of the coefficients from the allowable displacement is developed in Section [-@sec-coefficients].

Editada (DOCX línea 15):

> The seismic coefficient tables are presented for these four thresholds. Section [**10.1.3**](#seismic-pseudo-static-coefficients) describes the derivation of the coefficients from the allowable displacement.

Cambios:

- **E10a** · reordenamiento (sobre el texto del memo) · «; the derivation of the coefficients from the allowable displacement is developed in» → «. Section [**10.1.3**](#seismic-pseudo-static-coefficients) describes the derivation of the coefficients from the allowable displacement.». Parte la oración en dos y pasa la segunda a voz activa, con la sección como sujeto. La remisión es numeración de Word (N01).
- **E10b** · terminología (sobre el texto del memo) · «The coefficient tables are reported at those thresholds» → «The seismic coefficient tables are presented for these four thresholds». Cambia «reported at those thresholds» por «presented for these four thresholds» y agrega «seismic».

Nota: La frase «and the coefficient figures shade the intervals they delimit» falta en el DOCX porque la agregamos después del memo (N10); no es una supresión del otro autor.

## 3. Dynamic Properties of Slopes — `_docx/gmdp.qmd:10–42`

### `_chapters/ts.model.md` (6 oraciones editadas)

Las oraciones de ts.model.md:1 (segunda), 7, 13 (primera), 19, 25, 31 (segunda), 37, 47, 55 (tercera), 65, 71 y 90 no tienen ediciones del otro autor. Las diferencias que aparecen en ellas son citas, ecuaciones o reescrituras nuestras (N02, N07, N08, N12).

#### E11 · `_chapters/ts.model.md:1` · DOCX 19

Clase principal: **fluidez** · Marcas: contenido técnico, error introducido

Original actual (`_chapters/ts.model.md:1`):

> Flexible sliding-block models account for the dynamic response of the potential sliding mass through spectral acceleration evaluated at a period proportional to its fundamental period, so each slope geometry--material combination needs $T_s$, which is derived from the geometry and the depth-dependent small-strain shear stiffness, described by $G_o$, $m_o$, and $V_S^o$; the mean values of $T_s$ and $V_{S30}$ provide the dynamic inputs to the permanent-displacement models.

Memo recibido (`_local/gmdp.memo.en.qmd:76`): idéntica.

Editada (DOCX línea 19):

> Flexible sliding-block models account for the dynamic response of the potential sliding mass through spectral acceleration evaluated at a period proportional to its fundamental period, so each slope geometry–material combination needs $T_{s}$, which is derived from the geometry and the depth-dependent small-strain shear stiffness, described by $G_{o}$, $m_{o}$, and $V_{S}^{o}$; the mean value of $T_{s}$ provides a dynamic input to the permanent-displacement models, while $V_{S30}$ the site conditions used to determine the seismic demand.

Cambios:

- **E11a** · fluidez [contenido técnico] · «the mean values of $T_s$ and $V_{S30}$ provide the dynamic inputs to the permanent-displacement models» → «the mean value of $T_{s}$ provides a dynamic input to the permanent-displacement models, while $V_{S30}$ the site conditions used to determine the seismic demand». Separa los papeles: $T_s$ es el insumo dinámico de los modelos de desplazamiento y $V_{S30}$ define la condición de sitio de la demanda. Es una aclaración de contenido.
- **E11b** · gramática [error introducido] · inserción de «while $V_{S30}$ the site conditions used to determine the seismic demand». Falta el verbo (p. ej. «characterizes»).

#### E12 · `_chapters/ts.model.md:13` · DOCX 27

Clase principal: **terminología** · Marcas: contenido técnico

Original actual (`_chapters/ts.model.md:13`):

> The equivalent truncated section in the Dakoulas--Gazetas model [-@DakoulasGazetas1985Inhomogeneous] is specified by the height $H_s$, slope ratio $s$, and truncation ratio $\lambda_o$; with $\tan\beta=1/s$, where $\beta$ is the slope angle, the berm width is

Memo recibido (`_local/gmdp.memo.en.qmd:88`): idéntica.

Editada (DOCX línea 27):

> The equivalent truncated section in the Dakoulas–Gazetas model (1985) is specified by the height $H_{s}$, slope ratio $s$, expressed as horizontal to vertical, and truncation ratio $\lambda_{o}$; with $\tan\beta = 1/s$, where $\beta$ is the slope angle, the crest width is given, for a symmetric section, by

Cambios:

- **E12a** · terminología [contenido técnico] · «slope ratio $s$, and truncation ratio» → «slope ratio $s$, expressed as horizontal to vertical, and truncation ratio». Declara la convención horizontal:vertical de $s$.
- **E12b** · terminología [contenido técnico] · «the berm width is» → «the crest width is given, for a symmetric section, by». Cambia «berm» por «crest» y agrega la condición de sección simétrica. «crest» no coincide con «berm and base widths» de la oración anterior (también en el DOCX) ni con «$b$ the berm width» de la nota de la Tabla 10‑1. Hay que decidir un solo término.

Nota: La cita «(1985)» frente a [-@DakoulasGazetas1985Inhomogeneous] es estilo de cita (N02).

#### E13 · `_chapters/ts.model.md:31` · DOCX 39

Clase principal: **fluidez**

Original actual (`_chapters/ts.model.md:31`):

> where $G_o$ is the fitted small-strain shear modulus at the base, $g$ is the acceleration of gravity, and $\gamma_{\mathrm{sat}}^{(k_{\mathrm{b}})}$ is the saturated unit weight of the basal layer, whose index is $k_{\mathrm{b}}$; all quantities are expressed in consistent units.

Memo recibido (`_local/gmdp.memo.en.qmd:106`): idéntica.

Editada (DOCX línea 39):

> where $G_{o}$ is the fitted small-strain shear modulus at the base, $g$ is the acceleration of gravity, and $\gamma_{sat}^{(k_{b})}$ is the saturated unit weight of the basal layer, indexed by $k_{b}$; all quantities are expressed in consistent units.

Cambios:

- **E13a** · fluidez · «whose index is» → «indexed by». Usa un participio más breve.

#### E14 · `_chapters/ts.model.md:55` · DOCX 51

Clase principal: **terminología**

Original actual (`_chapters/ts.model.md:55`):

> where $K_0$ is the at-rest lateral earth pressure coefficient, $\gamma^{(\ell)}$ and $h^{(\ell)}$ are the unit weight adopted for the groundwater condition and the thickness of layer $\ell$, and $\ell<k$ denotes the overlying layers.

Memo recibido (`_local/gmdp.memo.en.qmd:130`): idéntica.

Editada (DOCX línea 51):

> where $K_{0}$ is the at-rest lateral earth pressure coefficient, $\gamma^{(\mathcal{l})}$ and $h^{(\mathcal{l})}$ are the effective unit weight adopted for the groundwater condition and the thickness of layer $\mathcal{l}$, and $\mathcal{l} < k$ denotes the overlying layers.

Cambios:

- **E14a** · terminología · «are the unit weight adopted» → «are the effective unit weight adopted». Escribe «effective unit weight», en coherencia con la tensión efectiva de la Eq. 10‑8.

Nota: El cambio de \ell a \mathcal{l} viene de la conversión (N07).

#### E15 · `_chapters/ts.model.md:55` · DOCX 51, 55

Clase principal: **terminología** · Marcas: contenido técnico, error introducido

Original actual (`_chapters/ts.model.md:55`):

> The layer overconsolidation ratio is $\mathrm{OCR}^{(k)}=\max[(p_m^{(k)}+\mathrm{POP})/p_m^{(k)},1]$, where $\mathrm{POP}$ is the preconsolidation pressure; for fine-grained soils, $m_1^{(k)}=f_{\mathrm{IP}}(\mathrm{IP}^{(k)})$, whereas for sands and gravels $m_1^{(k)}=0$ and the OCR multiplier is therefore unity.

Memo recibido (`_local/gmdp.memo.en.qmd:130`): idéntica.

Editada (DOCX línea 51):

> The layer overconsolidation ratio is

Editada (DOCX línea 55):

> where $POP$ is the preconsolidation pressure increment, expressed on the same mean-effective-stress basis as $p_{m}^{(k)}$; for fine-grained soils, $m_{1}^{(k)} = f_{IP}({IP}^{(k)})$, where ${IP}^{(k)}$is the plasticity index, whereas for sands and gravels $m_{1}^{(k)} = 0$ and the OCR multiplier is therefore unity.

Cambios:

- **E15a** · terminología [contenido técnico] · «where $\mathrm{POP}$ is the preconsolidation pressure;» → «where $POP$ is the preconsolidation pressure increment, expressed on the same mean-effective-stress basis as $p_{m}^{(k)}$;». Define POP como un incremento y fija su base de tensión media efectiva.
- **E15b** · fluidez [contenido técnico] [error introducido] · inserción de «, where ${IP}^{(k)}$is the plasticity index». Define el símbolo IP. En el DOCX falta el espacio antes de «is».

Nota: Que la ecuación en línea pase a la Eq. 10‑9 numerada es maquetación (N09).

#### E16 · `_chapters/ts.model.md:82` · DOCX 68

Clase principal: **fluidez**

Original actual (`_chapters/ts.model.md:82`):

> For each geometry--material combination, the analysis generates $N$ synthetic realizations of the layered profile, and each of $G_o$, $m_o$, $V_S^o$, and $V_{S30}$ is summarized by its mean and selected marginal fractiles; for the mean and for each reported fractile, $a_1$ and $T_s$ are evaluated from the corresponding $m_o$ and $V_S^o$ values, and the mean estimates provide the dynamic properties used in the displacement analysis.

Memo recibido (`_local/gmdp.memo.en.qmd:157`): idéntica.

Editada (DOCX línea 68):

> For each geometry–material combination, the analysis generates $N$ synthetic realizations of the layered profile, and each of $G_{o}$, $m_{o}$, $V_{S}^{o}$, and $V_{S30}$ is summarized by its mean and selected marginal fractiles; for the mean and for each reported fractile, $a_{1}$ and $T_{s}$ are evaluated from the corresponding $m_{o}$ and $V_{S}^{o}$ values, and the estimates calculated from the mean parameter values provide the dynamic properties used in the displacement analysis.

Cambios:

- **E16a** · fluidez · «and the mean estimates provide» → «and the estimates calculated from the mean parameter values provide». Aclara que las estimaciones se calculan con los valores medios de los parámetros.

### `_captions/tbl.Ts.md`

La nota de la Tabla 10‑1 (DOCX 143) coincide con la nuestra salvo una reescritura nuestra (N19) y artefactos de conversión (N25). El título de la tabla va en SA02.

## 4. Performance-Based Seismic Coefficient — `_docx/gmdp.qmd:44–85`

### `_chapters/dn.ensemble.md` (8 oraciones editadas)

#### E17 · `_chapters/dn.ensemble.md:1` · DOCX 76

Clase principal: **terminología** · Marcas: contenido técnico, error introducido

Original actual (`_chapters/dn.ensemble.md:1`):

> In this report the coefficient is derived from displacement-based performance: the Newmark permanent displacement $D_n$ is the slope-deformation performance measure, and the coefficient $k_{\max}$ is the lowest yield acceleration $k_y$ consistent with a performance objective defined by the allowable displacement $D_a$ and the target probability $p_e$ that $D_n$ exceeds $D_a$.

Memo recibido (`_local/gmdp.memo.en.qmd:182`):

> In this memo the coefficient is derived from displacement-based performance: the Newmark permanent displacement $D_n$ is the slope-deformation performance measure, and the coefficient $k_{\max}$ is the lowest yield acceleration $k_y$ consistent with a performance objective defined by the allowable displacement $D_a$ and the target probability $p_e$ that $D_n$ exceeds $D_a$.

Editada (DOCX línea 76):

> In this section the coefficient is derived from displacement-based performance: the Newmark permanent displacement $D_{n}$ is the slope-deformation performance measure, and the coefficient $k_{\max}$ is the lowest yield coefficient $k_{y}$ consistent with a performance objective defined by the allowable displacement $D_{a}$ and the target maximum exceedance probability $p_{e}$, such that $D_{n}$ exceeds $D_{a}$.

Cambios:

- **E17a** · terminología · «the lowest yield acceleration $k_y$» → «the lowest yield coefficient $k_{y}$». Llama «coefficient» a $k_y$ (adimensional) y reserva «acceleration» para $a_y$. El mismo patrón aparece en E19.
- **E17b** · terminología [contenido técnico] [error introducido] · «the target probability $p_e$ that $D_n$ exceeds $D_a$» → «the target maximum exceedance probability $p_{e}$, such that $D_{n}$ exceeds $D_{a}$». «maximum exceedance probability» expresa la cota superior. En cambio, «, such that $D_{n}$ exceeds $D_{a}$» se lee como una condición sobre $D_n$ y altera el sentido. No portar literal.

Nota: «report»/«memo» → «section» es adaptación al documento del otro autor (N21).

#### E18 · `_chapters/dn.ensemble.md:1` · DOCX 76

Clase principal: **terminología** · Marcas: contenido técnico

Original actual (`_chapters/dn.ensemble.md:1`):

> The normalized coefficient $k_h$ expresses $k_{\max}$ as a percentage of the PGA after site response is accounted for in each geometry--material combination, and the coefficients are reported by geometry, material and seismic demand.

Memo recibido (`_local/gmdp.memo.en.qmd:182`): idéntica.

Editada (DOCX línea 76):

> The normalized coefficient $k_{h}$ expresses $k_{\max}$ as a percentage of the site-adjusted PGA expressed in units of (g) after site response is accounted for in each geometry–material combination, and the coefficients are reported by geometry, material and seismic demand.

Cambios:

- **E18a** · terminología · «a percentage of the PGA» → «a percentage of the site-adjusted PGA». Escribe «site-adjusted PGA». El mismo patrón aparece en E26.
- **E18b** · fluidez [contenido técnico] · inserción de «expressed in units of (g)». Inserción redundante con «percentage», con «(g)» entre paréntesis.

#### E19 · `_chapters/dn.ensemble.md:3` · DOCX 78

Clase principal: **terminología** · Marcas: contenido técnico

Original actual (`_chapters/dn.ensemble.md:3`):

> The seismic demand and the fundamental periods established in the preceding chapters allow the $D_n (k_y)$ relations between the Newmark permanent displacement and the yield acceleration to be computed; their inversion yields $k_{\max}$, and its normalization by the PGA transformed to the $V_{S30}$ of each geometry--material combination yields $k_h$, so that the result traceably links the deformation objective to the horizontal action employed in the stability verification.

Memo recibido (`_local/gmdp.memo.en.qmd:184`):

> The seismic demand and the fundamental periods established in the preceding sections allow the $D_n (k_y)$ relations between the Newmark permanent displacement and the yield acceleration to be computed; their inversion yields $k_{\max}$, and its normalization by the PGA transformed to the $V_{S30}$ of each geometry--material combination yields $k_h$, so that the result traceably links the deformation objective to the horizontal action employed in the stability verification.

Editada (DOCX línea 78):

> The seismic demand and the fundamental periods established in the preceding sections allow the $D_{n}(k_{y})$ relations between the Newmark permanent displacement and the yield coefficient to be computed; their inversion at the target exceedance probability yields $k_{\max}$, and its normalization by the PGA transformed to the $V_{S30}$ of each geometry–material combination yields $k_{h}$, so that the result traceably links the deformation objective to the horizontal action employed in the stability verification.

Cambios:

- **E19a** · terminología · «and the yield acceleration to be computed» → «and the yield coefficient to be computed». Es el mismo patrón que E17.
- **E19b** · fluidez [contenido técnico] · «their inversion yields» → «their inversion at the target exceedance probability yields». Explicita a qué probabilidad se invierte.

Nota: «preceding chapters» (fuente actual) frente a «preceding sections» (memo y DOCX) es una reescritura nuestra (N11).

#### E20 · `_chapters/dn.ensemble.md:3` · DOCX 78

Clase principal: **terminología** · Marcas: contenido técnico

Original actual (`_chapters/dn.ensemble.md:3`):

> The yield acceleration $a_y$ represents the acceleration level that mobilizes the available resistance along the potential failure mechanism, and its dimensionless form is $k_y=a_y/g$; for each allowable displacement and target exceedance probability, the analysis determines the $k_y$ threshold that satisfies the performance criterion, and that threshold is $k_{\max}$, the coefficient of the pseudostatic limit-equilibrium verification.

Memo recibido (`_local/gmdp.memo.en.qmd:184`): idéntica.

Editada (DOCX línea 78):

> The yield acceleration $a_{y}$ represents the acceleration level at which the limit-equilibrium factor of safety equals unity and its dimensionless form is $k_{y} = a_{y}/g$; for each allowable displacement and target exceedance probability, the analysis determines the minimum $k_{y}$ threshold that satisfies the performance criterion, and that threshold is $k_{\max}$, the coefficient applied in the pseudostatic limit-equilibrium verification.

Cambios:

- **E20a** · terminología [contenido técnico] · «that mobilizes the available resistance along the potential failure mechanism» → «at which the limit-equilibrium factor of safety equals unity». Sustituye la definición por la habitual: factor de seguridad igual a uno.
- **E20b** · puntuación · «mechanism, and its dimensionless form» → «unity and its dimensionless form». Suprime la coma antes de «and».
- **E20c** · terminología [contenido técnico] · «determines the $k_y$ threshold» → «determines the minimum $k_{y}$ threshold». Agrega «minimum», en coherencia con el ínfimo de la Eq. 10‑14.
- **E20d** · fluidez · «the coefficient of the pseudostatic» → «the coefficient applied in the pseudostatic».

Nota: Tras esta oración, el DOCX agrega una oración sin contraparte (SB03).

#### E21 · `_chapters/dn.ensemble.md:5` · DOCX 80

Clase principal: **fluidez**

Original actual (`_chapters/dn.ensemble.md:5`):

> In the Newmark sliding-block method [@Newmark1965], the wedge in potential sliding is a rigid block resting on an inclined plane: relative motion begins when the driving acceleration exceeds the yield acceleration $a_y=k_y g$ and continues until the relative velocity returns to zero, and the permanent displacement is the sum of those episodes over the duration of the earthquake motion, obtained by double integration of the acceleration excess.

Memo recibido (`_local/gmdp.memo.en.qmd:186`): idéntica.

Editada (DOCX línea 80):

> In the Newmark sliding-block method (Newmark, 1965), the potentially sliding wedge is represented as a rigid block resting on an inclined plane: relative motion begins when the driving acceleration exceeds the yield acceleration $a_{y} = k_{y}g$ and continues until the relative velocity returns to zero, and the permanent displacement is the sum of those episodes over the duration of the earthquake motion, obtained by double integration of the acceleration excess.

Cambios:

- **E21a** · fluidez · «the wedge in potential sliding is a rigid block» → «the potentially sliding wedge is represented as a rigid block». Antepone el adjetivo y usa «is represented as» para marcar la idealización.

#### E22 · `_chapters/dn.ensemble.md:7` · DOCX 82

Clase principal: **terminología** · Marcas: contenido técnico

Original actual (`_chapters/dn.ensemble.md:7`):

> Two inputs feed that sample. The probabilistic input of each return period is the reference-rock UHS, which for 10,000 years is the MDE, and the MCE input is the rock spectrum of each scenario; both retain the complete distribution of the rock demand, and both are defined for $V_{S30}=V_{\mathrm{ref}}=760$ m/s.

Memo recibido (`_local/gmdp.memo.en.qmd:188`): idéntica.

Editada (DOCX línea 82):

> The input for each return period is the reference-rock UHS, which for 10,000 years represents the MDE; it specifies spectral acceleration ordinates at a common annual exceedance rate and is defined for $V_{S30} = V_{ref} = 760$ m/s.

Cambios:

- **E22a** · fluidez · «The probabilistic input of each return period» → «The input for each return period». Usa «for» en lugar de «of». La supresión de «probabilistic» va con la eliminación del MCE (N22).
- **E22b** · terminología · «which for 10,000 years is the MDE» → «which for 10,000 years represents the MDE».
- **E22c** · fluidez [contenido técnico] · «both retain the complete distribution of the rock demand, and both are defined for» → «it specifies spectral acceleration ordinates at a common annual exceedance rate and is defined for». Reemplaza la retención de la distribución completa por una definición de UHS, lo que cambia el contenido.

Nota: Suprimir «Two inputs feed that sample.» y la frase del MCE es adaptación de alcance (N22).

#### E23 · `_chapters/dn.ensemble.md:9` · DOCX 84

Clase principal: **fluidez** · Marcas: ya cubierta en la fuente actual

Original actual (`_chapters/dn.ensemble.md:9`):

> The Arias intensity used by `JB07` and `SR08` completes the set of intensity measures; it is estimated for each realization from the PGA [@Verri2023a], and the relation is applied deterministically, so that each PGA realization determines a single value of $I_A$ and the displacement sample propagates the PGA variability.

Memo recibido (`_local/gmdp.memo.en.qmd:190`):

> The Arias intensity that `JB07` and `SR08` require completes the set of intensity measures; it is estimated for each realization from the PGA, so that each PGA realization determines a single value of $I_A$ and the displacement sample propagates the PGA variability.

Editada (DOCX línea 84):

> The Arias intensity that JB07 and SR08 require completes the set of intensity measures; it is estimated deterministically for each realization from the PGA, so that each PGA realization determines a single value of $I_{A}$ and the displacement sample propagates the PGA variability.

Cambios:

- **E23a** · fluidez [ya cubierta en la fuente actual] (sobre el texto del memo) · «it is estimated for each realization» → «it is estimated deterministically for each realization». Ya cubierta: la fuente actual dice «and the relation is applied deterministically» (reescritura nuestra posterior, N13).

#### E24 · `_chapters/dn.ensemble.md:11` · DOCX 86

Clase principal: **terminología**

Original actual (`_chapters/dn.ensemble.md:11`):

> For each scenario, 30 values of $k_y$ are evaluated, logarithmically distributed between 0.01 and $\max (\overline{\mathrm{PGA}},0.80)$, where $\overline{\mathrm{PGA}}$ is the mean site-condition PGA of the scenario. That interval establishes the computed support of the $D_n (k_y)$ relations, on which the formulations are evaluated and the inversion to $k_{\max}$ operates.

Memo recibido (`_local/gmdp.memo.en.qmd:192`):

> For each scenario, 30 values of $k_y$ are evaluated, logarithmically distributed between 0.01 and $\max (\overline{\mathrm{PGA}},0.80)$, where $\overline{\mathrm{PGA}}$ is the mean site-condition PGA of the scenario; that interval establishes the computed support of the $D_n (k_y)$ relations, on which the formulations are evaluated and the inversion to $k_{\max}$ operates.

Editada (DOCX línea 86):

> For each scenario, 30 values of $k_{y}$ are evaluated, logarithmically spaced between 0.01 and $max(\overline{PGA},0.80)$, where $\overline{PGA}$ is the mean site-condition PGA of the scenario; that interval establishes the computed range of the $D_{n}(k_{y})$ relations, over which the formulations are evaluated and the inversion to $k_{\max}$ operates.

Cambios:

- **E24a** · terminología · «logarithmically distributed» → «logarithmically spaced».
- **E24b** · terminología · «the computed support of» → «the computed range of». Escribe «range» en lugar de «support». El mismo patrón aparece en E30 y E32.
- **E24c** · fluidez · «on which the formulations» → «over which the formulations».

Nota: Punto («. That», fuente actual) frente a punto y coma («; that», memo y DOCX): reescritura nuestra (N14).

### `_chapters/dn.model.md` (2 oraciones editadas)

#### E25 · `_chapters/dn.model.md:7` · DOCX 92

Clase principal: **fluidez** · Marcas: contenido técnico

Original actual (`_chapters/dn.model.md:7`):

> Some source formulations contain a discrete branch of zero or negligible displacement; the implemented evaluation uses exclusively the positive lognormal branch.

Memo recibido (`_local/gmdp.memo.en.qmd:200`): idéntica.

Editada (DOCX línea 92):

> Some source formulations contain a discrete branch of zero or negligible displacement; the implemented evaluation uses exclusively the positive lognormal branch, conditional on displacement exceeding the model’s zero-or-negligible-displacement threshold.

Cambios:

- **E25a** · fluidez [contenido técnico] · «the positive lognormal branch.» → «the positive lognormal branch, conditional on displacement exceeding the model’s zero-or-negligible-displacement threshold.». Agrega la condición de la rama positiva. Es una aclaración de contenido.

#### E26 · `_chapters/dn.model.md:14` · DOCX 96

Clase principal: **terminología**

Original actual (`_chapters/dn.model.md:14`):

> The normalized coefficient, reported as a percentage of the PGA [% of PGA], is calculated with the PGA transformed to the $V_{S30}$ of the geometry--material combination evaluated for each demand:

Memo recibido (`_local/gmdp.memo.en.qmd:207`): idéntica.

Editada (DOCX línea 96):

> The normalized coefficient, reported as a percentage of the PGA [% of PGA], is calculated using the site-adjusted PGA transformed to the $V_{S30}$ of the geometry–material combination evaluated for each demand:

Cambios:

- **E26a** · fluidez · «calculated with the» → «calculated using the».
- **E26b** · terminología · «the PGA transformed» → «the site-adjusted PGA transformed». Es el mismo patrón que E18.

### `_chapters/dn.uncertainty.md` (6 oraciones editadas)

#### E27 · `_chapters/dn.uncertainty.md:1` · DOCX 102

Clase principal: **terminología**

Original actual (`_chapters/dn.uncertainty.md:1`):

> The displacement model provides individual realizations for AM88, JB07, SR08, BT07, and a fifth formulation selected by the tectonic context: BM17 for projects with subduction control and BM19 for projects with crustal control.

Memo recibido (`_local/gmdp.memo.en.qmd:215`): idéntica.

Editada (DOCX línea 102):

> The displacement model provides individual realizations for AM88, JB07, SR08, BT07, and a fifth formulation selected by the tectonic context: BM17 for projects with subduction control and BM19 for projects with shallow crustal control.

Cambios:

- **E27a** · terminología · «projects with crustal control» → «projects with shallow crustal control». Coincide con «ordinary shallow crustal motions» de dn.appendix.md:54.

#### E28 · `_chapters/dn.uncertainty.md:3` · DOCX 104

Clase principal: **fluidez**

Original actual (`_chapters/dn.uncertainty.md:3`):

> All models receive the same joint sample of PGA and spectral accelerations, and a single realization of $\epsilon$ is shared across the models and across all values of $k_y$; each formulation scales that residual through its own $\sigma_{\ln D}$, and the sampled PGA is retained with each realization so that the inversion keeps its demand state.

Memo recibido (`_local/gmdp.memo.en.qmd:217`): idéntica.

Editada (DOCX línea 104):

> All models receive the same joint sample of PGA and spectral accelerations, and a single realization of $\epsilon$ is shared across the models and across all values of $k_{y}$; each formulation scales that residual through its own $\sigma_{\ln D}$, and the sampled PGA is retained with each realization so that the inversion preserves the pairing between displacement and seismic demand.

Cambios:

- **E28a** · fluidez · «so that the inversion keeps its demand state» → «so that the inversion preserves the pairing between displacement and seismic demand».

#### E29 · `_chapters/dn.uncertainty.md:3` · DOCX 104

Clase principal: **terminología** · Marcas: error introducido

Original actual (`_chapters/dn.uncertainty.md:3`):

> The realizations of $D_n$ are calculated for each material class with its mean dynamic properties; the fractiles of the stiffness profiles and of $T_s$ are reported in Chapter [-@sec-slope_periods] and are not propagated as additional realizations in the displacement calculation, and each material class is kept as an independent input through the inversion to $k_{\max}$, so the displacement curves are not averaged across materials before that operation.

Memo recibido (`_local/gmdp.memo.en.qmd:217`):

> The realizations of $D_n$ are calculated for each material class with its mean dynamic properties; the fractiles of the stiffness profiles and of $T_s$ are not propagated as additional realizations in the displacement calculation, and each material class is kept as an independent input through the inversion to $k_{\max}$, so the displacement curves are not averaged across materials before that operation.

Editada (DOCX línea 104):

> The realizations of $D_{n}$ are calculated for each material class with its mean dynamic properties; the fractiles of the stiffness profiles and of $T_{s}$ are not propagated as additional realizations in the displacement calculation, and each material class is kept as an separate scenario through the inversion to $k_{\max}$, so the displacement curves are not averaged across materials before that operation.

Cambios:

- **E29a** · terminología · «kept as an independent input» → «kept as an separate scenario». Escribe «separate scenario» en lugar de «independent input».
- **E29b** · gramática [error introducido] · inserción de «an separate». Error introducido en el artículo. Si se adopta: «a separate scenario».

Nota: «are reported in Chapter [-@sec-slope_periods] and» lo agregamos nosotros después del memo (N16).

#### E30 · `_chapters/dn.uncertainty.md:5` · DOCX 106

Clase principal: **terminología**

Original actual (`_chapters/dn.uncertainty.md:5`):

> For each model and realization, the computed $D_n (k_y)$ relation is projected onto a non-increasing curve and inverted in the $(\ln D_n,\ln k_y)$ plane to solve the criterion of [-@eq-kmax-criterion]; when $D_a$ falls outside the calculated support, the relation is extended in that plane from the two points at the corresponding end, with the single exception of the AM88 limit treated in Appendix [-@sec-newmark-appendix].

Memo recibido (`_local/gmdp.memo.en.qmd:219`): idéntica salvo «Section» por «Appendix» (N11).

Editada (DOCX línea 106):

> For each model and realization, the computed $D_{n}(k_{y})$ relation is projected onto a non-increasing curve and inverted in the $(lnD_{n},lnk_{y})$ plane to solve the criterion of [**Eq. 10‑14**](#_Ref_gmdp_eq_eq_kmax_criterion); when $D_{a}$ falls outside the calculated range, the relation is extrapolated in that plane from the two points at the corresponding end, with the single exception of the AM88 limit treated in [**11Appendix E**](#section-2).

Cambios:

- **E30a** · terminología · «outside the calculated support» → «outside the calculated range».
- **E30b** · terminología · «the relation is extended in that plane» → «the relation is extrapolated in that plane».

Nota: Las remisiones Eq. 10‑14 y Apéndice E y el marcado $(lnD_{n},lnk_{y})$ no son ediciones (N01, N07).

#### E31 · `_chapters/dn.uncertainty.md:5` · DOCX 106

Clase principal: **fluidez**

Original actual (`_chapters/dn.uncertainty.md:5`):

> The inversion is performed first per model within each realization.

Memo recibido (`_local/gmdp.memo.en.qmd:219`): idéntica.

Editada (DOCX línea 106):

> The inversion is performed first for each model within each realization.

Cambios:

- **E31a** · fluidez · «first per model» → «first for each model».

#### E32 · `_chapters/dn.uncertainty.md:11` · DOCX 112

Clase principal: **terminología**

Original actual (`_chapters/dn.uncertainty.md:11`):

> This grid contains, for every slope height, the damage thresholds $D_a/H$ = `r paste(.fmt(DAMAGE.CUTS, 1), collapse = ", ")`% of Chapter [-@sec-criteria], at which the coefficient tables are reported and which the coefficient figures shade; values of $D_a$ that exceed the calculated support of a realization are obtained through the logarithmic extension defined above.

Memo recibido (`_local/gmdp.memo.en.qmd:227`):

> This grid contains, for every slope height, the damage thresholds $D_a/H$ = `r paste(.fmt(DAMAGE.CUTS, 1), collapse = ", ")`% of Section [-@sec-criteria], at which the coefficient tables are reported; values of $D_a$ that exceed the calculated support of a realization are obtained through the logarithmic extension defined above.

Editada (DOCX línea 112):

> This grid contains, for every slope height, the damage thresholds $D_{a}/H$ = 0.1, 0.4, 1.0, 2.5% of Section [**10.1.1**](#seismic-design-criteria-for-slopes), at which the coefficient tables are reported; values of $D_{a}$ that exceed the calculated range of a realization are obtained through the logarithmic extrapolation defined above.

Cambios:

- **E32a** · terminología · «the calculated support of a realization» → «the calculated range of a realization».
- **E32b** · terminología · «the logarithmic extension defined above» → «the logarithmic extrapolation defined above».

Nota: «and which the coefficient figures shade» lo agregamos nosotros después del memo (N18). La remisión 10.1.1 es numeración de Word (N01).

### `_results/dn.inputs.qmd`

Sin contraparte en el DOCX (O7).

### `_captions/tbl.kh.sites.md`

La Tabla 10‑2 del DOCX es una tabla del otro autor y no la nuestra. Su pie y sus notas van en SA08, SA09, SB10 y SB11.

## 5. Apéndice — `_docx/dn.appendix.qmd:9`

### `_chapters/dn.appendix.md`

Corresponde al «Appendix E» del DOCX, fuera de la sección extraída. No lo comparé (O8).

## 6. Sin contraparte en las fuentes actuales

Oraciones del DOCX que no tienen contraparte en las fuentes listadas en el estado ni en `_chapters/*.md`, `_results/*.qmd` o `_captions/*.md`. Se dan el párrafo nuestro más cercano y la razón probable.

### 6.1 Con contraparte sólo en el memo (`_local/`): 9 oraciones únicas, 19 apariciones

#### SA01 · DOCX 5

Editada (DOCX línea 5):

> This section reports the dynamic properties of the slopes analyzed, the permanent displacements induced by the design earthquakes accumulate in their potential sliding masses, and the performance-based seismic coefficients derived from those displacements.

Memo (`_local/gmdp.memo.en.qmd:45`):

> It reports the dynamic properties of the slopes analysed, the permanent displacements the design earthquakes accumulate in their potential sliding masses, and the performance-based seismic coefficients derived from those displacements.

Párrafo nuestro más cercano (`_chapters/executive.opening.md:1`):

> and derived from that assessment the design earthquakes, the seismic design criteria for the tailings storage facilities and for conventional structures, and the dynamic properties and seismic coefficients of the slopes

Razón probable: Oración que escribimos para el memo (_local/gmdp.memo.en.qmd:45). Ninguna fuente del informe la contiene.

Cambios respecto del memo:

- **SA01a** · no portar (sobre el texto del memo) · «It reports» → «This section reports». Adaptación al documento del otro autor (N21).
- **SA01b** · gramática (sobre el texto del memo) · «slopes analysed» → «slopes analyzed». Ortografía estadounidense, como en E03.
- **SA01c** · gramática [error introducido] (sobre el texto del memo) · «the permanent displacements the design earthquakes accumulate» → «the permanent displacements induced by the design earthquakes accumulate». En la enumeración, «accumulate» queda sin sujeto (como en E01).

#### SA02 · DOCX 132

Editada (DOCX línea 132):

> Fundamental periods and mean dynamic properties of the evaluated slope scenarios

Memo (`_local/tbl.Ts.md:1`):

> Fundamental periods $T_s \approx T_1$ [s] and mean dynamic properties of the evaluated scenarios.

Párrafo nuestro más cercano (`_captions/tbl.Ts.md:1`):

> Fundamental periods in [s] and shear moduli in [MPa] for a slope of %d m height, for material classifications (USCS) representative of tailings storage facilities (TSF) and waste rock dumps (WRD).

Razón probable: Título del pie de la tabla de períodos del memo. El pie del informe (_captions/tbl.Ts.md, ensamblado en _docx/gmdp.qmd:39) abre con otra oración.

Cambios respecto del memo:

- **SA02a** · terminología (sobre el texto del memo) · «of the evaluated scenarios.» → «of the evaluated slope scenarios». Agrega «slope».
- **SA02b** · no portar (sobre el texto del memo) · «Fundamental periods $T_s \approx T_1$ [s] and» → «Fundamental periods and». Suprime el símbolo y la unidad (ecuación/unidad, fuera del alcance).

#### SA03 · DOCX 179, 187 y 195

Editada (DOCX línea 187):

> Mean Values of $k_{h}$ [% of PGA] for Return Period $T_{R} = 2,475$ yr, as a Function of the Allowable Permanent Displacement Relative to Slope Height, $D_{a}/H$ [%].

Memo (`_local/fig.kh.md:1`):

> Mean values of $k_h$ [%% of PGA] for site %1$s and return period $T_R=%3$s$ yr, as a function of the allowable permanent displacement relative to slope height, $D_a/H$ [%%].

Párrafo nuestro más cercano (`_captions/fig.kh.md:1`):

> The ordinates are the coefficients $k_h = 100\,k_{\max}/\mathrm{PGA}(V_{S30})$ [%% $\mathrm{PGA}$]; the abscissa is the allowable permanent displacement relative to the slope height, $D_a/H$ [%%].

Razón probable: Pie de figura del memo, uno por figura; sólo cambia $T_R$. El Word del informe no ensambla _captions/fig.kh.md (sólo lo usa el libro, _book/dn.qmd:73).

Cambios respecto del memo:

- **SA03a** · no portar (sobre el texto del memo) · «for site %1$s and return period» → «for Return Period». Omite el sitio y usa mayúsculas de título: adaptación (N23).

#### SA04 · DOCX 179, 187 y 195

Editada (DOCX línea 187):

> The Curves Represent the Scenarios S135, S50, S32, S27, S35 Evaluated with the Rigid, Ensemble, and Flexible Sets.

Memo (`_local/fig.kh.md:1`):

> The curves represent the scenarios %2$s evaluated with the `rigid`, `ensemble`, and `flexible` sets.

Párrafo nuestro más cercano (`_captions/fig.kh.md:1`):

> each series is one material–geometry combination, identified in the legend as `IDm.IDg`

Razón probable: Pie de figura del memo.

Cambios respecto del memo:

- **SA04a** · no portar (sobre el texto del memo) · «The curves represent the scenarios» → «The Curves Represent the Scenarios». Mayúsculas de título; la lista de escenarios es valor renderizado (N23, N05).

#### SA05 · DOCX 183, 191 y 199

Editada (DOCX línea 183):

> The coefficient is expressed as $100\, k_{\max}/PGA(V_{S30})$.

Memo (`_local/fig.kh.md:1`):

> The coefficient is expressed as $100\,k_{\max}/\mathrm{PGA}(V_{S30})$.

Párrafo nuestro más cercano (`_captions/fig.kh.md:1`):

> The ordinates are the coefficients $k_h = 100\,k_{\max}/\mathrm{PGA}(V_{S30})$ [%% $\mathrm{PGA}$]

Razón probable: Nota del pie de figura del memo. Es idéntica salvo el marcado de la fórmula (N07).

Cambios respecto del memo: ninguno de redacción.

#### SA06 · DOCX 183, 191 y 199

Editada (DOCX línea 183):

> Color identifies the scenario and line pattern identifies the set: solid for rigid, short dashes for ensemble, and long dashes for flexible.

Memo (`_local/fig.kh.md:1`):

> Color identifies the scenario and line pattern identifies the set: solid for `rigid`, short dashes for `ensemble`, and long dashes for `flexible`.

Párrafo nuestro más cercano (`_captions/fig.kh.md:1`):

> color identifies the material and line pattern and width identify the geometry

Razón probable: Nota del pie de figura del memo. Es idéntica salvo el formato de código (N23).

Cambios respecto del memo: ninguno de redacción.

#### SA07 · DOCX 183, 191 y 199

Editada (DOCX línea 183):

> The shaded bands are delimited by the damage thresholds $D_{a}/H = 0.1,0.4,1.0,2.5$ %.

Memo (`_local/fig.kh.md:1`):

> The shaded bands are delimited by the damage thresholds $D_a/H=%4$s$ %%.

Párrafo nuestro más cercano (`_captions/fig.kh.md:1`):

> The bands of the abscissa are delimited at $D_a/H$ = %6$s %%.

Razón probable: Nota del pie de figura del memo. Es idéntica salvo los números renderizados (N05).

Cambios respecto del memo: ninguno de redacción.

#### SA08 · DOCX 175

Editada (DOCX línea 175):

> The column headings give the allowable permanent displacement relative to the slope height, expressed as a percentage.

Memo (`_local/tbl.kh.md:1`):

> The coefficient columns report the mean estimate at each allowable permanent displacement relative to slope height, $D_a/H$ [%%], expressed as $100\,k_{\max}/\mathrm{PGA}(V_{S30})$.

Párrafo nuestro más cercano (`_captions/tbl.kh.sites.md:1`):

> The remaining column headings are the relative displacement limits $D_a/H_s$ [%].

Razón probable: Nota de la Tabla 10‑2, que es una tabla resumen del otro autor. La adaptó de la nota de las tablas por escenario del memo.

Cambios respecto del memo:

- **SA08a** · fluidez [contenido técnico] (sobre el texto del memo) · «The coefficient columns report the mean estimate at each allowable permanent displacement» → «The column headings give the allowable permanent displacement». La nota describe ahora los encabezados y no el contenido de las celdas (adaptación a su tabla).
- **SA08b** · gramática (sobre el texto del memo) · «relative to slope height» → «relative to the slope height». Agrega el artículo.

#### SA09 · DOCX 175

Editada (DOCX línea 175):

> The fundamental period of the slope is in seconds and the time-averaged shear-wave velocity of the upper 30 m is in m/s.

Memo (`_local/tbl.kh.md:1`):

> $T_s$ is the fundamental period of the slope [s] and $V_{S30}$ the shear-wave velocity of the evaluated condition [m/s].

Párrafo nuestro más cercano (`_captions/tbl.kh.md:1`):

> $T_s$ is the fundamental period of the slope, in seconds, and $V_{S30}$ the shear-wave velocity of the evaluated condition, in m/s.

Razón probable: Nota de la Tabla 10‑2 del otro autor, adaptada de la nota del memo.

Cambios respecto del memo:

- **SA09a** · no portar (sobre el texto del memo) · «$T_s$ is the fundamental period of the slope [s] and» → «The fundamental period of the slope is in seconds and». Quita los símbolos y escribe las unidades con palabras (ecuación/unidad).
- **SA09b** · terminología (sobre el texto del memo) · «the shear-wave velocity of the evaluated condition» → «the time-averaged shear-wave velocity of the upper 30 m». Define $V_{S30}$ en lugar de remitir a la condición evaluada.

### 6.2 Sin contraparte en ningún texto del proyecto: 11 oraciones

#### SB01 · DOCX 51

Editada (DOCX línea 51):

> For hydrostatic groundwater conditions, the bulk unit weight is used above the groundwater table and the submerged unit weight below it; layers intersected by the groundwater table are subdivided accordingly.

Párrafo nuestro más cercano (`_chapters/ts.model.md:55`):

> where $K_0$ is the at-rest lateral earth pressure coefficient, $\gamma^{(\ell)}$ and $h^{(\ell)}$ are the unit weight adopted for the groundwater condition and the thickness of layer $\ell$, and $\ell<k$ denotes the overlying layers.

Razón probable: Añadido técnico del otro autor: pesos unitarios sobre y bajo el nivel freático y subdivisión de capas. Es contenido y lo decide el propietario.

#### SB02 · DOCX 66

Editada (DOCX línea 66):

> The parameters of the stiffness correlations are listed in [Table E‑1](#section-4).

Párrafo nuestro más cercano (`_chapters/ts.model.md:80`):

> {{< include /_tbl/SiteGo.qmd >}}

Razón probable: El otro autor llevó la tabla de correlaciones al Apéndice E y agregó esta remisión. Es numeración de Word y no se porta literal.

#### SB03 · DOCX 78

Editada (DOCX línea 78):

> A factor of safety of at least unity under this applied coefficient indicates that the calculated yield coefficient meets or exceeds the required threshold.

Párrafo nuestro más cercano (`_chapters/dn.ensemble.md:3`):

> for each allowable displacement and target exceedance probability, the analysis determines the $k_y$ threshold that satisfies the performance criterion, and that threshold is $k_{\max}$, the coefficient of the pseudostatic limit-equilibrium verification.

Razón probable: Añadido técnico del otro autor sobre la lectura del factor de seguridad. Es contenido.

#### SB04 · DOCX 116

Editada (DOCX línea 116):

> [Table 10‑1](#_Ref_gmdp_tbl_periods) presents the fundamental periods and the mean dynamic properties of the slope scenarios evaluated for the Crawford facilities.

Párrafo nuestro más cercano (`_captions/tbl.Ts.md:1`):

> Fundamental periods in [s] and shear moduli in [MPa] for a slope of %d m height, for material classifications (USCS) representative of tailings storage facilities (TSF) and waste rock dumps (WRD).

Razón probable: Introducción del otro autor a su tabla, con el nombre del proyecto. Nuestro Word inserta la tabla sin frase introductoria (_docx/gmdp.qmd:32–42).

#### SB05 · DOCX 116

Editada (DOCX línea 116):

> Each scenario is named with the letter S followed by its slope height in meters.

Párrafo nuestro más cercano (`_captions/tbl.Ts.md:1`):

> `IDm` identifies the material scenario and `USCS` the classification of the slope materials.

Razón probable: Convención de nombres S135 … S35 del otro autor.

#### SB06 · DOCX 116

Editada (DOCX línea 116):

> The scenarios are S135, S50, S32, S27, and S35, which correspond to material identifiers (IDm) U1 to U5 in [Table 10‑1](#_Ref_gmdp_tbl_periods), respectively.

Párrafo nuestro más cercano (`_captions/tbl.Ts.md:1`):

> `IDm` identifies the material scenario and `USCS` the classification of the slope materials.

Razón probable: Correspondencia entre sus escenarios y nuestros IDm, escrita por el otro autor.

#### SB07 · DOCX 145

Editada (DOCX línea 145):

> [Figure 10‑1](#_Ref_gmdp_fig_kh_1) through [Figure 10‑3](#_Ref_gmdp_fig_kh_3) show the performance-based horizontal seismic coefficient, expressed as a percentage of the PGA, as a function of the allowable permanent displacement relative to the slope height, for design earthquakes with AEPs of 1:475, 1:2,475, and 1:10,000 years.

Párrafo nuestro más cercano (`_local/fig.kh.md:1`):

> Mean values of $k_h$ [%% of PGA] for site %1$s and return period $T_R=%3$s$ yr, as a function of the allowable permanent displacement relative to slope height, $D_a/H$ [%%].

Razón probable: Introducción del otro autor a las figuras. AEP y numeración están fuera del alcance (N05, N06, N01).

#### SB08 · DOCX 145

Editada (DOCX línea 145):

> [Table 10‑2](#_Ref_gmdp_tbl_summary) lists the coefficients of the ensemble set at the four relative displacement limits for the 1:2,475 and 1:10,000-year return period design earthquakes.

Párrafo nuestro más cercano (`_results/kmax.results.qmd:6`):

> Table [-@`r TBL.KH`] reports, for the MCE and the geometries analysed, the range of the coefficient across the material scenarios at each limit, expressed as a percentage of the PGA.

Razón probable: Introducción del otro autor a su Tabla 10‑2, que resume el conjunto ensemble en dos AEP.

#### SB09 · DOCX 145

Editada (DOCX línea 145):

> The coefficients of the rigid and flexible sets, and the coefficients in acceleration units, are included in [**11Appendix E**](#section-2).

Párrafo nuestro más cercano (`_docx/gmdp.qmd:68`):

> The seismic coefficients $k_{max}$ and $k_h$ are developed in the %s annex.

Razón probable: Remisión del otro autor a su Apéndice E.

#### SB10 · DOCX 171

Editada (DOCX línea 171):

> Seismic Coefficients [% of PGA] of the Ensemble Set for Design Earthquakes with AEPs of 1:2,475 and 1:10,000 Years

Párrafo nuestro más cercano (`_captions/tbl.kh.sites.md:1`):

> MCE seismic coefficients $k_h$ [% of PGA] from the ensemble model.

Razón probable: Pie de la Tabla 10‑2, que es del otro autor. Nuestra tabla resumen del Word (_docx/gmdp.qmd:78) es otra: rangos del MCE.

#### SB11 · DOCX 175

Editada (DOCX línea 175):

> Values are for the ensemble set.

Párrafo nuestro más cercano (`_captions/tbl.kh.sites.md:1`):

> MCE seismic coefficients $k_h$ [% of PGA] from the ensemble model.

Razón probable: Nota de la Tabla 10‑2 del otro autor.
