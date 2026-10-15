# B · Decisiones del propietario

Ediciones de Diana Reyes con decisión «no portar: contenido» o «no portar: números» en `MAP.md`. Cada punto da su oración, la nuestra y la pregunta cerrada. Ninguna de estas ediciones está en `PATCH.md`; si el propietario acepta alguna, la oración se redacta después sobre la fuente actual. Las oraciones en inglés están copiadas de los archivos.

16 puntos, 41 ediciones (35 de contenido y 6 de números).

## D01 · Bloque ejecutivo de desplazamientos

Ediciones: B02a (no portar: contenido), B02b (no portar: contenido).

Oración de ella (DOCX 7):

```text
The $D_{n}(k_{y})$ curves relate, for each combination of geometry, material, and design scenario, the yield acceleration $k_{y}$ to the expected permanent displacement; they were computed with an ensemble set of AM88 (Ambraseys & Menu, 1988), JB07 (Jibson, 2007), SR08 (Saygili & Rathje, 2008), BT07 (Bray & Travasarou, 2007), and BM19 (Bray, Macedo, & Travasauro, 2018), with the reference magnitude $M_{w}$ = 7.0 and 300 realizations per demand and are read at the fractiles $q = 1 - p_{e}$.
```

Nuestra (_results/dn.results.qmd:7):

```text
The $D_n(k_y)$ curves relate, for each combination of geometry, material, and design scenario, the yield acceleration $k_y$ to the expected permanent displacement; they were computed with the `ensemble` set of `AM88`, `JB07`, `SR08`, `BT07`, and `r BM.code`, with the reference magnitude $M_w$ = `r .fmt(Mw.gmdp, 1)` and `r .fmti(NS)` realizations per demand, and are read at the fractiles $q = 1 - p_e$.
```

Qué decidir:

- ¿Se mantiene «the `ensemble` set», que nombra el conjunto definido en dn.uncertainty.md:1, o se adopta su «an ensemble set», que lo vuelve genérico?
- ¿Se agrega una cita por modelo en el bloque ejecutivo? Si se agrega, BM19 corresponde a la clave [@BrayMacedo2019] de dn.appendix.md:54; su DOCX escribe «(Bray, Macedo, & Travasauro, 2018)».

## D02 · Párrafos suprimidos del capítulo de criterios

Ediciones: B04a (no portar: contenido), B08a (no portar: contenido), B09a (no portar: contenido).

Oración de ella: (suprimida)

Nuestra (_chapters/deq.criteria.md:1 y :9):

```text
The seismic design of tailings storage facilities is based on the two-level performance framework consolidated by dam-safety practice: an Operating Basis Earthquake (OBE), which the facility must withstand without operational interruption, and a Safety Evaluation Earthquake (SEE), under which it must not release tailings. ICOLD Bulletin 148 formalizes this framework for embankment structures [@ICOLD2016; @ANCOLD2012], and the USACE Engineer Regulation ER 1110-2-1806 expresses it in terms of the OBE and the Maximum Design Earthquake (MDE) [@USACE1995]. […] In this report, the MDE is represented by the probabilistic spectrum for a 10,000-year return period, whereas the MCE is represented by the deterministic envelope.
```

Oración de ella: (suprimida)

Nuestra (_chapters/deq.kmax.md:3):

```text
Two further references relate the pseudostatic verification to the permanent deformation. NCHRP Report 611 formulates the seismic analysis of slopes and transportation infrastructure in terms of displacement-based performance and uses simplified Newmark correlations to relate demand to permanent deformation [@AndersonEtAl2008], and Eurocode 8 ties the pseudostatic action to the design seismic acceleration and the consequence class and admits Newmark displacement calculations when the ratio between the critical acceleration and the design acceleration justifies a deformation-based verification [@CEN2004]. These references provide the framing and the comparison criteria for the coefficients of this report; their indicative values serve that comparison, and the displacement objective defined for the project governs the coefficients themselves.
```

Oración de ella (DOCX 15):

```text
The allowable permanent displacement is expressed as a percentage of the reference slope height.
```

Nuestra (_chapters/deq.kmax.md:5):

```text
That objective is expressed as an allowable permanent displacement relative to the slope height.
```

Qué decidir:

- ¿Se conservan en nuestras fuentes el párrafo OBE/SEE con la oración «In this report, the MDE is represented by the probabilistic spectrum for a 10,000-year return period, whereas the MCE is represented by the deterministic envelope.» (deq.criteria.md:1 y :9), que su capítulo no trae?
- ¿Se conserva el párrafo de NCHRP Report 611 y Eurocode 8 (deq.kmax.md:3)?
- Si se suprime ese párrafo, «That objective» queda sin antecedente: ¿se adopta entonces su oración «The allowable permanent displacement is expressed as a percentage of the reference slope height.»?

## D03 · Ámbito y atribución en deq.kmax.md:1

Ediciones: B05a (no portar: contenido), B07b (no portar: contenido), B07f (no portar: contenido).

Oración de ella (DOCX 13):

```text
Slope Performance under the design earthquakes is evaluated through successive tiers of analysis including pseudostatic stability checks, simplified estimates of permanent deformation, and dynamic analyses where warranted by the consequences of failure, anticipated response, or complexity of the failure mechanism (International Commission on Large Dams, 2016; Federal Emergency Management Agency, 2005).
```

Nuestra (_chapters/deq.kmax.md:1):

```text
The verification of the slopes under those design earthquakes follows the practice that ICOLD and FEMA frame for dams and embankments through successive tiers of analysis: pseudostatic checks, simplified deformation estimates, and dynamic analyses when the consequence, the anticipated response, or the complexity of the mechanism requires them [@ICOLD2016; @FEMA2005].
```

Oración de ella (DOCX 13):

```text
USACE manuals EM 1110-2-1902 and EM 1110-2-2100 discuss pseudostatic analysis sliding block methods for evaluating seismic stability and permanent deformation Selection of the coefficient considers the site-specific seismic hazard, potential failure mechanism, and project performance criteria (U.S. Army Corps of Engineers, 2003; U.S. Army Corps of Engineers, 2005).
```

Nuestra (_chapters/deq.kmax.md:1):

```text
The USACE manuals EM 1110-2-1902 and EM 1110-2-2100 include pseudostatic analysis among the methods applicable to dams and earthworks and address the sliding block for estimating permanent seismic deformation; they tie the selection of the coefficient to the site-specific hazard, the potential failure mechanism, and the performance criteria of the project, so the coefficient results from the conditions of each project instead of a single value applicable to all of them [@USACE2003; @USACE2005].
```

Qué decidir:

- ¿Se suprime «follows the practice that ICOLD and FEMA frame for dams and embankments», de modo que ICOLD y FEMA queden sólo en la cita y desaparezca el ámbito «for dams and embankments»? (La propuesta de PATCH.md conserva nuestra estructura y porta sólo la enumeración editada.)
- ¿Se reemplaza «include pseudostatic analysis among the methods applicable to dams and earthworks and address the sliding block for estimating permanent seismic deformation» por su versión, que suprime «applicable to dams and earthworks» y agrega «seismic stability»? Su redacción necesita además la conjunción que falta entre «pseudostatic analysis» y «sliding block methods».
- ¿Se suprime la conclusión «so the coefficient results from the conditions of each project instead of a single value applicable to all of them»?

## D04 · Umbrales de daño y su procedencia

Ediciones: B10b (no portar: contenido), B10c (no portar: contenido).

Oración de ella (DOCX 15):

```text
This report evaluates four relative displacement thresholds, $D_{a}/H$ = 0.1, 0.4, 1.0, 2.5%, based on the crest-settlement ratios reported by Alberti et. al. (Aliberti, Biondi, Cascone, & Rampello, 2019).
```

Nuestra (_chapters/deq.kmax.md:5):

```text
The coefficients of this report are read against four damage thresholds of the relative permanent displacement, $D_a/H$ = `r paste(.fmt(DAMAGE.CUTS, 1), collapse = ", ")`%: the crest-settlement ratios derived from ninety case histories of earthquake damage to embankment dams and associated with the Operational, Damage, Life Safety and Collapse limit states of the Italian dam code NTD14 [@Aliberti2019].
```

Antecedente leído en esta sesión: el caso 9 de la skill `writing` (`.claude/skills/writing/references/cases.md`) registra que el propietario rechazó una versión anterior de esta oración que narraba a los autores y que la razón incluyó «a count of cases, a dam code» como entidades que la oración no necesitaba (ticket 20); la redacción aceptada allí fue «the coefficients are reported at four relative displacement limits». La fuente actual conserva el conteo y el código.

Qué decidir:

- ¿Se reemplaza «four damage thresholds of the relative permanent displacement» por «four relative displacement thresholds»? dn.uncertainty.md:11 y las notas de figura del memo los llaman «damage thresholds».
- ¿Se suprime la procedencia «derived from ninety case histories of earthquake damage to embankment dams and associated with the Operational, Damage, Life Safety and Collapse limit states of the Italian dam code NTD14» y queda sólo la cita [@Aliberti2019]?

## D05 · Papel de $V_{S30}$ en ts.model.md:1

Ediciones: B13a (no portar: contenido).

Oración de ella (DOCX 19):

```text
Flexible sliding-block models account for the dynamic response of the potential sliding mass through spectral acceleration evaluated at a period proportional to its fundamental period, so each slope geometry–material combination needs $T_{s}$, which is derived from the geometry and the depth-dependent small-strain shear stiffness, described by $G_{o}$, $m_{o}$, and $V_{S}^{o}$; the mean value of $T_{s}$ provides a dynamic input to the permanent-displacement models, while $V_{S30}$ the site conditions used to determine the seismic demand.
```

Nuestra (_chapters/ts.model.md:1):

```text
Flexible sliding-block models account for the dynamic response of the potential sliding mass through spectral acceleration evaluated at a period proportional to its fundamental period, so each slope geometry--material combination needs $T_s$, which is derived from the geometry and the depth-dependent small-strain shear stiffness, described by $G_o$, $m_o$, and $V_S^o$; the mean values of $T_s$ and $V_{S30}$ provide the dynamic inputs to the permanent-displacement models.
```

Qué decidir:

- ¿Se separan los papeles como propone ella: $T_s$ como entrada de los modelos de desplazamiento y $V_{S30}$ como condición de sitio de la demanda?

Candidata de B si se acepta (a su cláusula le falta el verbo; «defines» es elección de B y requiere validación):

```text
the mean value of $T_s$ provides a dynamic input to the permanent-displacement models, while $V_{S30}$ defines the site condition used to determine the seismic demand.
```

## D06 · Geometría de la sección truncada

Ediciones: B15a (no portar: contenido), B15b (no portar: contenido), B15c (no portar: contenido).

Oración de ella (DOCX 27):

```text
The equivalent truncated section in the Dakoulas–Gazetas model (1985) is specified by the height $H_{s}$, slope ratio $s$, expressed as horizontal to vertical, and truncation ratio $\lambda_{o}$; with $\tan\beta = 1/s$, where $\beta$ is the slope angle, the crest width is given, for a symmetric section, by
```

Nuestra (_chapters/ts.model.md:13):

```text
The equivalent truncated section in the Dakoulas--Gazetas model [-@DakoulasGazetas1985Inhomogeneous] is specified by the height $H_s$, slope ratio $s$, and truncation ratio $\lambda_o$; with $\tan\beta=1/s$, where $\beta$ is the slope angle, the berm width is
```

Qué decidir:

- ¿Se declara que $s$ se expresa como horizontal a vertical? (Coincide con $\tan\beta=1/s$.)
- ¿$b$ se llama «crest width», como escribe ella, o «berm width», como dicen la oración anterior de ts.model.md:13 y la nota del memo? _captions/tbl.Ts.md:1 lo llama «the geometric parameter».
- ¿Se agrega la hipótesis «for a symmetric section»?

## D07 · Pesos unitarios y nivel freático

Ediciones: B17a (no portar: contenido), B18a (no portar: contenido).

Oración de ella (DOCX 51):

```text
where $K_{0}$ is the at-rest lateral earth pressure coefficient, $\gamma^{(\mathcal{l})}$ and $h^{(\mathcal{l})}$ are the effective unit weight adopted for the groundwater condition and the thickness of layer $\mathcal{l}$, and $\mathcal{l} < k$ denotes the overlying layers.
```

Nuestra (_chapters/ts.model.md:55):

```text
where $K_0$ is the at-rest lateral earth pressure coefficient, $\gamma^{(\ell)}$ and $h^{(\ell)}$ are the unit weight adopted for the groundwater condition and the thickness of layer $\ell$, and $\ell<k$ denotes the overlying layers.
```

Oración de ella (DOCX 51):

```text
For hydrostatic groundwater conditions, the bulk unit weight is used above the groundwater table and the submerged unit weight below it; layers intersected by the groundwater table are subdivided accordingly.
```

Nuestra: sin oración equivalente (nueva, tras ts.model.md:55 (primera oración)).

Qué decidir:

- ¿El cálculo de $p_m^{(k)}$ usa el peso total sobre el nivel freático y el sumergido debajo, con las capas subdivididas en el nivel freático, como dice su oración nueva?
- Si es así, ¿se adoptan «effective unit weight» y su oración nueva? Sin esa oración, «effective unit weight» puede leerse como peso sumergido en todas las capas.

## D08 · POP e IP

Ediciones: B19b (no portar: contenido), B19c (no portar: contenido).

Oración de ella (DOCX 51):

```text
The layer overconsolidation ratio is
```

Oración de ella (DOCX 53):

```text
${OCR}^{(k)} = max\lbrack(p_{m}^{(k)} + POP)/p_{m}^{(k)},1\rbrack$, **[Eq.** **10‑9]**
```

Oración de ella (DOCX 55):

```text
where $POP$ is the preconsolidation pressure increment, expressed on the same mean-effective-stress basis as $p_{m}^{(k)}$; for fine-grained soils, $m_{1}^{(k)} = f_{IP}({IP}^{(k)})$, where ${IP}^{(k)}$is the plasticity index, whereas for sands and gravels $m_{1}^{(k)} = 0$ and the OCR multiplier is therefore unity.
```

Nuestra (_chapters/ts.model.md:55):

```text
The layer overconsolidation ratio is $\mathrm{OCR}^{(k)}=\max[(p_m^{(k)}+\mathrm{POP})/p_m^{(k)},1]$, where $\mathrm{POP}$ is the preconsolidation pressure; for fine-grained soils, $m_1^{(k)}=f_{\mathrm{IP}}(\mathrm{IP}^{(k)})$, whereas for sands and gravels $m_1^{(k)}=0$ and the OCR multiplier is therefore unity.
```

Qué decidir:

- ¿POP es el incremento de presión de preconsolidación expresado en la misma base de tensión media efectiva que $p_m^{(k)}$, como escribe ella? Nuestra fórmula suma POP a $p_m^{(k)}$ y nuestra oración lo llama «the preconsolidation pressure».
- ¿Se define IP como índice de plasticidad? notation.md no lo define. Su DOCX omite el espacio antes de «is»; con nuestro marcado sería «, where $\mathrm{IP}^{(k)}$ is the plasticity index,».

## D09 · Nombres de los escenarios

Ediciones: B23a (no portar: contenido), B24a (no portar: contenido).

Oración de ella (DOCX 116):

```text
Each scenario is named with the letter S followed by its slope height in meters.
```

Nuestra: sin oración equivalente (nueva, antes de su Tabla 10-1).

Oración de ella (DOCX 116):

```text
The scenarios are S135, S50, S32, S27, and S35, which correspond to material identifiers (IDm) U1 to U5 in [Table 10‑1](#_Ref_gmdp_tbl_periods), respectively.
```

Nuestra: sin oración equivalente (nueva, antes de su Tabla 10-1).

Qué decidir:

- ¿Se agregan al memo sus dos oraciones que explican la convención S<altura> y la correspondencia S135–U1 … S35–U5 (coinciden con _local/gmdp.memo.scenarios.csv)?

## D10 · Definición del coeficiente y de $a_y$

Ediciones: B26b (no portar: contenido), B27b (no portar: contenido), B28a (no portar: contenido), B28b (no portar: contenido), B28c (no portar: contenido), B29a (no portar: contenido).

Oración de ella (DOCX 76):

```text
The normalized coefficient $k_{h}$ expresses $k_{\max}$ as a percentage of the site-adjusted PGA expressed in units of (g) after site response is accounted for in each geometry–material combination, and the coefficients are reported by geometry, material and seismic demand.
```

Nuestra (_chapters/dn.ensemble.md:1):

```text
The normalized coefficient $k_h$ expresses $k_{\max}$ as a percentage of the PGA after site response is accounted for in each geometry--material combination, and the coefficients are reported by geometry, material and seismic demand.
```

Oración de ella (DOCX 78):

```text
The seismic demand and the fundamental periods established in the preceding sections allow the $D_{n}(k_{y})$ relations between the Newmark permanent displacement and the yield coefficient to be computed; their inversion at the target exceedance probability yields $k_{\max}$, and its normalization by the PGA transformed to the $V_{S30}$ of each geometry–material combination yields $k_{h}$, so that the result traceably links the deformation objective to the horizontal action employed in the stability verification.
```

Nuestra (_chapters/dn.ensemble.md:3):

```text
The seismic demand and the fundamental periods established in the preceding chapters allow the $D_n (k_y)$ relations between the Newmark permanent displacement and the yield acceleration to be computed; their inversion yields $k_{\max}$, and its normalization by the PGA transformed to the $V_{S30}$ of each geometry--material combination yields $k_h$, so that the result traceably links the deformation objective to the horizontal action employed in the stability verification.
```

Oración de ella (DOCX 78):

```text
The yield acceleration $a_{y}$ represents the acceleration level at which the limit-equilibrium factor of safety equals unity and its dimensionless form is $k_{y} = a_{y}/g$; for each allowable displacement and target exceedance probability, the analysis determines the minimum $k_{y}$ threshold that satisfies the performance criterion, and that threshold is $k_{\max}$, the coefficient applied in the pseudostatic limit-equilibrium verification.
```

Nuestra (_chapters/dn.ensemble.md:3):

```text
The yield acceleration $a_y$ represents the acceleration level that mobilizes the available resistance along the potential failure mechanism, and its dimensionless form is $k_y=a_y/g$; for each allowable displacement and target exceedance probability, the analysis determines the $k_y$ threshold that satisfies the performance criterion, and that threshold is $k_{\max}$, the coefficient of the pseudostatic limit-equilibrium verification.
```

Oración de ella (DOCX 78):

```text
A factor of safety of at least unity under this applied coefficient indicates that the calculated yield coefficient meets or exceeds the required threshold.
```

Nuestra: sin oración equivalente (nueva, tras dn.ensemble.md:3).

Qué decidir:

- ¿Se agrega «expressed in units of (g)» a la PGA de la normalización? En una frase en porcentaje puede leerse como unidad de $k_h$.
- ¿Se agrega «at the target exceedance probability» a «their inversion yields»? La oración siguiente ya nombra la probabilidad objetivo.
- ¿Se redefine $a_y$ como «the acceleration level at which the limit-equilibrium factor of safety equals unity» en lugar de «the acceleration level that mobilizes the available resistance along the potential failure mechanism»? Su supresión de la coma depende de este cambio.
- ¿Se agrega «minimum» a «the $k_y$ threshold»? Coincide con el ínfimo de @eq-kmax-criterion.
- ¿Se agrega su oración nueva sobre el factor de seguridad bajo el coeficiente aplicado?

## D11 · Demanda MCE

Ediciones: B31a (no portar: contenido), B32a (no portar: contenido), B33b (no portar: contenido), B33d (no portar: contenido), B43a (no portar: contenido), B54a (no portar: contenido).

Oración de ella (DOCX 82):

```text
For each geometry, material and seismic demand – the probabilistic spectrum of each evaluated return period – a joint sample of the intensity measures required by the rigid-block and flexible formulations is constructed; that sample is common to all models, so their differences represent the displacement formulation rather than incompatible seismic demands.
```

Nuestra (_chapters/dn.ensemble.md:7):

```text
For each geometry, material and seismic demand -- the probabilistic spectrum of each evaluated return period and the MCE scenario -- a joint sample of the intensity measures required by the rigid-block and flexible formulations is constructed; that sample is common to all models, so their differences represent the displacement formulation rather than incompatible seismic demands.
```

Oración de ella: (suprimida)

Nuestra (_chapters/dn.ensemble.md:7):

```text
Two inputs feed that sample.
```

Oración de ella (DOCX 82):

```text
The input for each return period is the reference-rock UHS, which for 10,000 years represents the MDE; it specifies spectral acceleration ordinates at a common annual exceedance rate and is defined for $V_{S30} = V_{ref} = 760$ m/s.
```

Nuestra (_chapters/dn.ensemble.md:7):

```text
The probabilistic input of each return period is the reference-rock UHS, which for 10,000 years is the MDE, and the MCE input is the rock spectrum of each scenario; both retain the complete distribution of the rock demand, and both are defined for $V_{S30}=V_{\mathrm{ref}}=760$ m/s.
```

Oración de ella (DOCX 112):

```text
The evaluation uses 300 realizations for each demand – the probabilistic spectrum of each return period $T_{R}$ = 475, 2,475, 10,000 years – and a grid of allowable displacements $D_{a}/H_{s}$ ranging from 0.05 to 2.50 %.
```

Nuestra (_chapters/dn.uncertainty.md:11):

```text
The evaluation uses `r .fmti(NS)` realizations for each demand -- the probabilistic spectrum of each return period $T_R$ = `r paste(prettyNum(round(sort(TR.gmdp), 0), big.mark = ","), collapse = ", ")` years and the MCE -- and a grid of allowable displacements $D_a$ ranging from `r paste(format(range(Da.gmdp), trim = TRUE, scientific = FALSE), collapse = " to ")` cm.
```

Oración de ella: (suprimida)

Nuestra: sin oración equivalente (_local/gmdp.memo.en.qmd:229-266 (bloque R que genera esas figuras y tablas)).

Qué decidir:

- Su informe no incluye la demanda MCE: suprime la entrada MCE, «Two inputs feed that sample.», «probabilistic», «both retain the complete distribution of the rock demand», «and the MCE» y las figuras y tablas MCE y de $k_{max}$ del memo. ¿Nuestras fuentes conservan esas oraciones como están?

## D12 · Definición del UHS

Ediciones: B33e (no portar: contenido).

Oración de ella (DOCX 82):

```text
The input for each return period is the reference-rock UHS, which for 10,000 years represents the MDE; it specifies spectral acceleration ordinates at a common annual exceedance rate and is defined for $V_{S30} = V_{ref} = 760$ m/s.
```

Nuestra (_chapters/dn.ensemble.md:7):

```text
The probabilistic input of each return period is the reference-rock UHS, which for 10,000 years is the MDE, and the MCE input is the rock spectrum of each scenario; both retain the complete distribution of the rock demand, and both are defined for $V_{S30}=V_{\mathrm{ref}}=760$ m/s.
```

Qué decidir:

- ¿Se agrega «it specifies spectral acceleration ordinates at a common annual exceedance rate»? En su oración reemplaza a «both retain the complete distribution of the rock demand», que se refiere también a la entrada MCE.

## D13 · Rama lognormal

Ediciones: B36a (no portar: contenido).

Oración de ella (DOCX 92):

```text
Some source formulations contain a discrete branch of zero or negligible displacement; the implemented evaluation uses exclusively the positive lognormal branch, conditional on displacement exceeding the model’s zero-or-negligible-displacement threshold.
```

Nuestra (_chapters/dn.model.md:7):

```text
Some source formulations contain a discrete branch of zero or negligible displacement; the implemented evaluation uses exclusively the positive lognormal branch.
```

Qué decidir:

- ¿Se agrega «conditional on displacement exceeding the model’s zero-or-negligible-displacement threshold»? Ninguna fuente leída lo dice.

## D14 · Rótulos de período de retorno

Ediciones: B43b (no portar: números), B48a (no portar: números), B49a (no portar: números), B50a (no portar: números), B52a (no portar: números).

Oración de ella (DOCX 112):

```text
The evaluation uses 300 realizations for each demand – the probabilistic spectrum of each return period $T_{R}$ = 475, 2,475, 10,000 years – and a grid of allowable displacements $D_{a}/H_{s}$ ranging from 0.05 to 2.50 %.
```

Nuestra (_chapters/dn.uncertainty.md:11):

```text
The evaluation uses `r .fmti(NS)` realizations for each demand -- the probabilistic spectrum of each return period $T_R$ = `r paste(prettyNum(round(sort(TR.gmdp), 0), big.mark = ","), collapse = ", ")` years and the MCE -- and a grid of allowable displacements $D_a$ ranging from `r paste(format(range(Da.gmdp), trim = TRUE, scientific = FALSE), collapse = " to ")` cm.
```

Oración de ella (DOCX 179):

```text
Mean Values of $\mathbf{k}_{\mathbf{h}}$ [% of PGA] for Return Period $\mathbf{T}_{\mathbf{R}}\mathbf{= 475}$ yr
```

Oración de ella (DOCX 187):

```text
Mean Values of $k_{h}$ [% of PGA] for Return Period $T_{R} = 2,475$ yr
```

Nuestra (_local/fig.kh.md:1):

```text
Mean values of $k_h$ [%% of PGA] for site %1$s and return period $T_R=%3$s$ yr
```

Oración de ella (DOCX 145):

```text
[Figure 10‑1](#_Ref_gmdp_fig_kh_1) through [Figure 10‑3](#_Ref_gmdp_fig_kh_3) show the performance-based horizontal seismic coefficient, expressed as a percentage of the PGA, as a function of the allowable permanent displacement relative to the slope height, for design earthquakes with AEPs of 1:475, 1:2,475, and 1:10,000 years.
```

Nuestra: sin oración equivalente (nueva, presenta sus Figuras 10-1 a 10-3).

Oración de ella (DOCX 145):

```text
[Table 10‑2](#_Ref_gmdp_tbl_summary) lists the coefficients of the ensemble set at the four relative displacement limits for the 1:2,475 and 1:10,000-year return period design earthquakes.
```

Nuestra: sin oración equivalente (nueva, presenta su Tabla 10-2).

Oración de ella (DOCX 171):

```text
Seismic Coefficients [% of PGA] of the Ensemble Set for Design Earthquakes with AEPs of 1:2,475 and 1:10,000 Years
```

Nuestra: sin oración equivalente (leyenda de su Tabla 10-2).

Qué decidir:

- El memo rotula las demandas 500 y 2,500 años (TR.target, _local/gmdp.memo.en.qmd:24) y el texto alternativo de sus propias imágenes conserva «TR=500 yr» y «TR=2,500 yr» (DOCX 177 y 185); ella rotula 475 y 2,475 (AEP 1:475 y 1:2,475) en el texto, las leyendas y su Tabla 10-2. ¿Qué rótulo corresponde a esas demandas en las fuentes?

## D15 · Leyenda de la tabla de períodos del memo

Ediciones: B46a (no portar: contenido).

Oración de ella (DOCX 132):

```text
Table 10‑1: Fundamental periods and mean dynamic properties of the evaluated slope scenarios
```

Nuestra (_local/tbl.Ts.md:1):

```text
Fundamental periods $T_s \approx T_1$ [s] and mean dynamic properties of the evaluated scenarios.
```

Qué decidir:

- ¿Se suprime «$T_s \approx T_1$ [s]» de la leyenda, como hizo ella? La propuesta de PATCH.md porta sólo «slope scenarios».

## D16 · Decimales de $a_1$

Ediciones: B47a (no portar: números).

Oración de ella (DOCX):

```text
3.656 · 3.370 · 3.116 · 3.105 · 2.976 (DOCX 121-129)
```

Nuestra (memo:222, 260, 298, 336, 374 (columna $a_1$ de la Tabla 2)):

```text
3.6559 · 3.3699 · 3.1162 · 3.1052 · 2.9759
```

Qué decidir:

- ¿La tabla de períodos del memo publica $a_1$ con tres decimales, como su Tabla 10-1, o con cuatro, como hoy?
