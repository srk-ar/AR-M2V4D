# B · Parche propuesto (no aplicado)

Sólo las ediciones con decisión «portar» o «portar corregida» de `MAP.md`. Por archivo, en orden de línea: oración actual textual y oración propuesta, lista para pegar en la misma posición. Las propuestas reemplazan palabras; ecuaciones, números, citas `[@…]`, referencias `@eq-…`/`[-@…]` y expresiones `r` quedan como están. Nada se aplicó y ninguna propuesta pasó todavía por las compuertas de entrega de la skill `writing` (ver `SUMMARY.md`).

Primero las fuentes del Word (capítulos y bloques de resultados) y después el memo (`_local/`), cuyas copias de las mismas oraciones llevan el mismo cambio sobre su propio texto.

## `_results/dn.results.qmd`

### B01 · `_results/dn.results.qmd:7` · ediciones B01a, B01b

Actual:

```text
The Newmark permanent displacement $D_n$ quantifies the deformation an earthquake accumulates in the sliding mass and is the performance measure from which the seismic coefficients are derived.
```

Propuesta:

```text
The Newmark permanent displacement $D_n$ quantifies the displacement induced by an earthquake and accumulated in the sliding mass and is the performance measure from which the seismic coefficients are derived.
```

### B02 · `_results/dn.results.qmd:7` · ediciones B02c

Actual:

```text
The $D_n(k_y)$ curves relate, for each combination of geometry, material, and design scenario, the yield acceleration $k_y$ to the expected permanent displacement; they were computed with the `ensemble` set of `AM88`, `JB07`, `SR08`, `BT07`, and `r BM.code`, with the reference magnitude $M_w$ = `r .fmt(Mw.gmdp, 1)` and `r .fmti(NS)` realizations per demand, and are read at the fractiles $q = 1 - p_e$.
```

Propuesta:

```text
The $D_n(k_y)$ curves relate, for each combination of geometry, material, and design scenario, the yield acceleration $k_y$ to the expected permanent displacement; they were computed with the `ensemble` set of `AM88`, `JB07`, `SR08`, `BT07`, and `r BM.code`, with the reference magnitude $M_w$ = `r .fmt(Mw.gmdp, 1)` and `r .fmti(NS)` realizations per demand and are read at the fractiles $q = 1 - p_e$.
```

## `_results/kmax.results.qmd`

### B03 · `_results/kmax.results.qmd:6` · ediciones B03a

Actual:

```text
Table [-@`r TBL.KH`] reports, for the MCE and the geometries analysed, the range of the coefficient across the material scenarios at each limit, expressed as a percentage of the PGA.
```

Propuesta:

```text
Table [-@`r TBL.KH`] reports, for the MCE and the geometries analyzed, the range of the coefficient across the material scenarios at each limit, expressed as a percentage of the PGA.
```

## `_chapters/deq.kmax.md`

### B05 · `_chapters/deq.kmax.md:1` · ediciones B05b, B05c, B05d, B05e

Actual:

```text
The verification of the slopes under those design earthquakes follows the practice that ICOLD and FEMA frame for dams and embankments through successive tiers of analysis: pseudostatic checks, simplified deformation estimates, and dynamic analyses when the consequence, the anticipated response, or the complexity of the mechanism requires them [@ICOLD2016; @FEMA2005].
```

Propuesta:

```text
The verification of the slopes under those design earthquakes follows the practice that ICOLD and FEMA frame for dams and embankments through successive tiers of analysis including pseudostatic stability checks, simplified estimates of permanent deformation, and dynamic analyses where warranted by the consequences of failure, anticipated response, or complexity of the failure mechanism [@ICOLD2016; @FEMA2005].
```

### B06 · `_chapters/deq.kmax.md:1` · ediciones B06a, B06b, B06c, B06d, B06e

Actual:

```text
Within this framework, the Newmark method provides a deformation-based estimate that complements the limit-equilibrium verification, and the pseudostatic coefficient of that verification is a project-specific quantity rather than a universal property of the structure type.
```

Propuesta:

```text
Within this framework, the Newmark method provides a deformation-based assessment that complements the limit-equilibrium analysis. The pseudostatic seismic coefficient is a project-specific value rather than a universal value assigned to a particular structure type.
```

### B07 · `_chapters/deq.kmax.md:1` · ediciones B07a, B07c, B07d, B07e

Actual:

```text
The USACE manuals EM 1110-2-1902 and EM 1110-2-2100 include pseudostatic analysis among the methods applicable to dams and earthworks and address the sliding block for estimating permanent seismic deformation; they tie the selection of the coefficient to the site-specific hazard, the potential failure mechanism, and the performance criteria of the project, so the coefficient results from the conditions of each project instead of a single value applicable to all of them [@USACE2003; @USACE2005].
```

Propuesta:

```text
USACE manuals EM 1110-2-1902 and EM 1110-2-2100 include pseudostatic analysis among the methods applicable to dams and earthworks and address the sliding block for estimating permanent seismic deformation. Selection of the coefficient considers the site-specific seismic hazard, potential failure mechanism, and project performance criteria, so the coefficient results from the conditions of each project instead of a single value applicable to all of them [@USACE2003; @USACE2005].
```

### B10 · `_chapters/deq.kmax.md:5` · ediciones B10a

Actual:

```text
The coefficients of this report are read against four damage thresholds of the relative permanent displacement, $D_a/H$ = `r paste(.fmt(DAMAGE.CUTS, 1), collapse = ", ")`%: the crest-settlement ratios derived from ninety case histories of earthquake damage to embankment dams and associated with the Operational, Damage, Life Safety and Collapse limit states of the Italian dam code NTD14 [@Aliberti2019].
```

Propuesta:

```text
This report evaluates the coefficients at four damage thresholds of the relative permanent displacement, $D_a/H$ = `r paste(.fmt(DAMAGE.CUTS, 1), collapse = ", ")`%: the crest-settlement ratios derived from ninety case histories of earthquake damage to embankment dams and associated with the Operational, Damage, Life Safety and Collapse limit states of the Italian dam code NTD14 [@Aliberti2019].
```

### B11 · `_chapters/deq.kmax.md:5` · ediciones B11a, B11b

Actual:

```text
Their denominator, the embankment height plus the thickness of the deformable foundation, is the slope height used here.
```

Propuesta:

```text
Their denominator, the reference height, includes the embankment height and the thickness of the deformable foundation and is adopted here as the slope height for normalization.
```

### B12 · `_chapters/deq.kmax.md:5` · ediciones B12a, B12b

Actual:

```text
The coefficient tables are reported at those thresholds and the coefficient figures shade the intervals they delimit; the derivation of the coefficients from the allowable displacement is developed in Chapter [-@sec-coefficients].
```

Propuesta:

```text
The seismic coefficient tables are presented for these four thresholds and the coefficient figures shade the intervals they delimit. Chapter [-@sec-coefficients] describes the derivation of the coefficients from the allowable displacement.
```

## `_chapters/ts.model.md`

### B15 · `_chapters/ts.model.md:13` · ediciones B15d

Actual:

```text
The equivalent truncated section in the Dakoulas--Gazetas model [-@DakoulasGazetas1985Inhomogeneous] is specified by the height $H_s$, slope ratio $s$, and truncation ratio $\lambda_o$; with $\tan\beta=1/s$, where $\beta$ is the slope angle, the berm width is
```

Propuesta:

```text
The equivalent truncated section in the Dakoulas--Gazetas model [-@DakoulasGazetas1985Inhomogeneous] is specified by the height $H_s$, slope ratio $s$, and truncation ratio $\lambda_o$; with $\tan\beta=1/s$, where $\beta$ is the slope angle, the berm width is given by
```

### B16 · `_chapters/ts.model.md:31` · ediciones B16a

Actual:

```text
where $G_o$ is the fitted small-strain shear modulus at the base, $g$ is the acceleration of gravity, and $\gamma_{\mathrm{sat}}^{(k_{\mathrm{b}})}$ is the saturated unit weight of the basal layer, whose index is $k_{\mathrm{b}}$; all quantities are expressed in consistent units.
```

Propuesta:

```text
where $G_o$ is the fitted small-strain shear modulus at the base, $g$ is the acceleration of gravity, and $\gamma_{\mathrm{sat}}^{(k_{\mathrm{b}})}$ is the saturated unit weight of the basal layer, indexed by $k_{\mathrm{b}}$; all quantities are expressed in consistent units.
```

### B21 · `_chapters/ts.model.md:82` · ediciones B21a

Actual:

```text
For each geometry--material combination, the analysis generates $N$ synthetic realizations of the layered profile, and each of $G_o$, $m_o$, $V_S^o$, and $V_{S30}$ is summarized by its mean and selected marginal fractiles; for the mean and for each reported fractile, $a_1$ and $T_s$ are evaluated from the corresponding $m_o$ and $V_S^o$ values, and the mean estimates provide the dynamic properties used in the displacement analysis.
```

Propuesta:

```text
For each geometry--material combination, the analysis generates $N$ synthetic realizations of the layered profile, and each of $G_o$, $m_o$, $V_S^o$, and $V_{S30}$ is summarized by its mean and selected marginal fractiles; for the mean and for each reported fractile, $a_1$ and $T_s$ are evaluated from the corresponding $m_o$ and $V_S^o$ values, and the estimates calculated from the mean parameter values provide the dynamic properties used in the displacement analysis.
```

## `_chapters/dn.ensemble.md`

### B25 · `_chapters/dn.ensemble.md:1` · ediciones B25b, B25c

Actual:

```text
In this report the coefficient is derived from displacement-based performance: the Newmark permanent displacement $D_n$ is the slope-deformation performance measure, and the coefficient $k_{\max}$ is the lowest yield acceleration $k_y$ consistent with a performance objective defined by the allowable displacement $D_a$ and the target probability $p_e$ that $D_n$ exceeds $D_a$.
```

Propuesta:

```text
In this report the coefficient is derived from displacement-based performance: the Newmark permanent displacement $D_n$ is the slope-deformation performance measure, and the coefficient $k_{\max}$ is the lowest yield coefficient $k_y$ consistent with a performance objective defined by the allowable displacement $D_a$ and the target maximum probability $p_e$ that $D_n$ exceeds $D_a$.
```

### B26 · `_chapters/dn.ensemble.md:1` · ediciones B26a

Actual:

```text
The normalized coefficient $k_h$ expresses $k_{\max}$ as a percentage of the PGA after site response is accounted for in each geometry--material combination, and the coefficients are reported by geometry, material and seismic demand.
```

Propuesta:

```text
The normalized coefficient $k_h$ expresses $k_{\max}$ as a percentage of the site-condition PGA after site response is accounted for in each geometry--material combination, and the coefficients are reported by geometry, material and seismic demand.
```

### B27 · `_chapters/dn.ensemble.md:3` · ediciones B27a

Actual:

```text
The seismic demand and the fundamental periods established in the preceding chapters allow the $D_n (k_y)$ relations between the Newmark permanent displacement and the yield acceleration to be computed; their inversion yields $k_{\max}$, and its normalization by the PGA transformed to the $V_{S30}$ of each geometry--material combination yields $k_h$, so that the result traceably links the deformation objective to the horizontal action employed in the stability verification.
```

Propuesta:

```text
The seismic demand and the fundamental periods established in the preceding chapters allow the $D_n (k_y)$ relations between the Newmark permanent displacement and the yield coefficient to be computed; their inversion yields $k_{\max}$, and its normalization by the PGA transformed to the $V_{S30}$ of each geometry--material combination yields $k_h$, so that the result traceably links the deformation objective to the horizontal action employed in the stability verification.
```

### B28 · `_chapters/dn.ensemble.md:3` · ediciones B28d

Actual:

```text
The yield acceleration $a_y$ represents the acceleration level that mobilizes the available resistance along the potential failure mechanism, and its dimensionless form is $k_y=a_y/g$; for each allowable displacement and target exceedance probability, the analysis determines the $k_y$ threshold that satisfies the performance criterion, and that threshold is $k_{\max}$, the coefficient of the pseudostatic limit-equilibrium verification.
```

Propuesta:

```text
The yield acceleration $a_y$ represents the acceleration level that mobilizes the available resistance along the potential failure mechanism, and its dimensionless form is $k_y=a_y/g$; for each allowable displacement and target exceedance probability, the analysis determines the $k_y$ threshold that satisfies the performance criterion, and that threshold is $k_{\max}$, the coefficient applied in the pseudostatic limit-equilibrium verification.
```

### B30 · `_chapters/dn.ensemble.md:5` · ediciones B30a, B30b

Actual:

```text
In the Newmark sliding-block method [@Newmark1965], the wedge in potential sliding is a rigid block resting on an inclined plane: relative motion begins when the driving acceleration exceeds the yield acceleration $a_y=k_y g$ and continues until the relative velocity returns to zero, and the permanent displacement is the sum of those episodes over the duration of the earthquake motion, obtained by double integration of the acceleration excess.
```

Propuesta:

```text
In the Newmark sliding-block method [@Newmark1965], the potentially sliding wedge is represented as a rigid block resting on an inclined plane: relative motion begins when the driving acceleration exceeds the yield acceleration $a_y=k_y g$ and continues until the relative velocity returns to zero, and the permanent displacement is the sum of those episodes over the duration of the earthquake motion, obtained by double integration of the acceleration excess.
```

### B33 · `_chapters/dn.ensemble.md:7` · ediciones B33a, B33c

Actual:

```text
The probabilistic input of each return period is the reference-rock UHS, which for 10,000 years is the MDE, and the MCE input is the rock spectrum of each scenario; both retain the complete distribution of the rock demand, and both are defined for $V_{S30}=V_{\mathrm{ref}}=760$ m/s.
```

Propuesta:

```text
The probabilistic input for each return period is the reference-rock UHS, which for 10,000 years represents the MDE, and the MCE input is the rock spectrum of each scenario; both retain the complete distribution of the rock demand, and both are defined for $V_{S30}=V_{\mathrm{ref}}=760$ m/s.
```

### B35 · `_chapters/dn.ensemble.md:11` · ediciones B35a, B35b, B35c

Actual:

```text
For each scenario, 30 values of $k_y$ are evaluated, logarithmically distributed between 0.01 and $\max (\overline{\mathrm{PGA}},0.80)$, where $\overline{\mathrm{PGA}}$ is the mean site-condition PGA of the scenario. That interval establishes the computed support of the $D_n (k_y)$ relations, on which the formulations are evaluated and the inversion to $k_{\max}$ operates.
```

Propuesta:

```text
For each scenario, 30 values of $k_y$ are evaluated, logarithmically spaced between 0.01 and $\max (\overline{\mathrm{PGA}},0.80)$, where $\overline{\mathrm{PGA}}$ is the mean site-condition PGA of the scenario. That interval establishes the computed range of the $D_n (k_y)$ relations, over which the formulations are evaluated and the inversion to $k_{\max}$ operates.
```

## `_chapters/dn.model.md`

### B37 · `_chapters/dn.model.md:14` · ediciones B37a, B37b

Actual:

```text
The normalized coefficient, reported as a percentage of the PGA [% of PGA], is calculated with the PGA transformed to the $V_{S30}$ of the geometry--material combination evaluated for each demand:
```

Propuesta:

```text
The normalized coefficient, reported as a percentage of the PGA [% of PGA], is calculated using the site-condition PGA transformed to the $V_{S30}$ of the geometry--material combination evaluated for each demand:
```

## `_chapters/dn.uncertainty.md`

### B38 · `_chapters/dn.uncertainty.md:1` · ediciones B38a

Actual:

```text
The displacement model provides individual realizations for AM88, JB07, SR08, BT07, and a fifth formulation selected by the tectonic context: BM17 for projects with subduction control and BM19 for projects with crustal control.
```

Propuesta:

```text
The displacement model provides individual realizations for AM88, JB07, SR08, BT07, and a fifth formulation selected by the tectonic context: BM17 for projects with subduction control and BM19 for projects with shallow crustal control.
```

### B39 · `_chapters/dn.uncertainty.md:3` · ediciones B39a

Actual:

```text
All models receive the same joint sample of PGA and spectral accelerations, and a single realization of $\epsilon$ is shared across the models and across all values of $k_y$; each formulation scales that residual through its own $\sigma_{\ln D}$, and the sampled PGA is retained with each realization so that the inversion keeps its demand state.
```

Propuesta:

```text
All models receive the same joint sample of PGA and spectral accelerations, and a single realization of $\epsilon$ is shared across the models and across all values of $k_y$; each formulation scales that residual through its own $\sigma_{\ln D}$, and the sampled PGA is retained with each realization so that the inversion preserves the pairing between displacement and seismic demand.
```

### B40 · `_chapters/dn.uncertainty.md:3` · ediciones B40a

Actual:

```text
The realizations of $D_n$ are calculated for each material class with its mean dynamic properties; the fractiles of the stiffness profiles and of $T_s$ are reported in Chapter [-@sec-slope_periods] and are not propagated as additional realizations in the displacement calculation, and each material class is kept as an independent input through the inversion to $k_{\max}$, so the displacement curves are not averaged across materials before that operation.
```

Propuesta:

```text
The realizations of $D_n$ are calculated for each material class with its mean dynamic properties; the fractiles of the stiffness profiles and of $T_s$ are reported in Chapter [-@sec-slope_periods] and are not propagated as additional realizations in the displacement calculation, and each material class is kept as a separate scenario through the inversion to $k_{\max}$, so the displacement curves are not averaged across materials before that operation.
```

### B41 · `_chapters/dn.uncertainty.md:5` · ediciones B41a, B41b

Actual:

```text
For each model and realization, the computed $D_n (k_y)$ relation is projected onto a non-increasing curve and inverted in the $(\ln D_n,\ln k_y)$ plane to solve the criterion of [-@eq-kmax-criterion]; when $D_a$ falls outside the calculated support, the relation is extended in that plane from the two points at the corresponding end, with the single exception of the AM88 limit treated in Appendix [-@sec-newmark-appendix].
```

Propuesta:

```text
For each model and realization, the computed $D_n (k_y)$ relation is projected onto a non-increasing curve and inverted in the $(\ln D_n,\ln k_y)$ plane to solve the criterion of [-@eq-kmax-criterion]; when $D_a$ falls outside the calculated range, the relation is extrapolated in that plane from the two points at the corresponding end, with the single exception of the AM88 limit treated in Appendix [-@sec-newmark-appendix].
```

### B42 · `_chapters/dn.uncertainty.md:5` · ediciones B42a

Actual:

```text
The inversion is performed first per model within each realization.
```

Propuesta:

```text
The inversion is performed first for each model within each realization.
```

### B44 · `_chapters/dn.uncertainty.md:11` · ediciones B44a, B44b

Actual:

```text
This grid contains, for every slope height, the damage thresholds $D_a/H$ = `r paste(.fmt(DAMAGE.CUTS, 1), collapse = ", ")`% of Chapter [-@sec-criteria], at which the coefficient tables are reported and which the coefficient figures shade; values of $D_a$ that exceed the calculated support of a realization are obtained through the logarithmic extension defined above.
```

Propuesta:

```text
This grid contains, for every slope height, the damage thresholds $D_a/H$ = `r paste(.fmt(DAMAGE.CUTS, 1), collapse = ", ")`% of Chapter [-@sec-criteria], at which the coefficient tables are reported and which the coefficient figures shade; values of $D_a$ that exceed the calculated range of a realization are obtained through the logarithmic extrapolation defined above.
```

## `_local/gmdp.memo.en.qmd`

### B45 · `_local/gmdp.memo.en.qmd:45` · ediciones B45b, B45c

Actual:

```text
It reports the dynamic properties of the slopes analysed, the permanent displacements the design earthquakes accumulate in their potential sliding masses, and the performance-based seismic coefficients derived from those displacements.
```

Propuesta:

```text
It reports the dynamic properties of the slopes analyzed, the permanent displacements induced by the design earthquakes and accumulated in their potential sliding masses, and the performance-based seismic coefficients derived from those displacements.
```

### B01 · `_local/gmdp.memo.en.qmd:53` · ediciones B01a, B01b

Actual:

```text
The Newmark permanent displacement $D_n$ quantifies the deformation an earthquake accumulates in the sliding mass and is the performance measure from which the seismic coefficients are derived.
```

Propuesta:

```text
The Newmark permanent displacement $D_n$ quantifies the displacement induced by an earthquake and accumulated in the sliding mass and is the performance measure from which the seismic coefficients are derived.
```

### B02 · `_local/gmdp.memo.en.qmd:53` · ediciones B02c

Actual:

```text
The $D_n(k_y)$ curves relate, for each combination of geometry, material, and design scenario, the yield acceleration $k_y$ to the expected permanent displacement; they were computed with the `ensemble` set of `AM88`, `JB07`, `SR08`, `BT07`, and `r BM.code`, with the reference magnitude $M_w$ = `r .fmt(Mw.gmdp, 1)` and `r .fmti(NS)` realizations per demand, and are read at the fractiles $q = 1 - p_e$.
```

Propuesta:

```text
The $D_n(k_y)$ curves relate, for each combination of geometry, material, and design scenario, the yield acceleration $k_y$ to the expected permanent displacement; they were computed with the `ensemble` set of `AM88`, `JB07`, `SR08`, `BT07`, and `r BM.code`, with the reference magnitude $M_w$ = `r .fmt(Mw.gmdp, 1)` and `r .fmti(NS)` realizations per demand and are read at the fractiles $q = 1 - p_e$.
```

### B03 · `_local/gmdp.memo.en.qmd:53` · ediciones B03a

Actual:

```text
The horizontal pseudostatic coefficient $k_h$ is in turn derived from the allowable permanent displacement $D_a$ of the potentially sliding mass [@BrayTravasarou2009; @MacedoEtAl2018]; the coefficients are reported at four relative displacement limits, $D_a/H_s$ = `r paste(.fmt(DAMAGE.CUTS, 1), collapse = ", ")`%, and the tables in Section [-@sec-kh-tables] report, for the demands and scenarios analysed, the coefficient at each limit, expressed as a percentage of the PGA.
```

Propuesta:

```text
The horizontal pseudostatic coefficient $k_h$ is in turn derived from the allowable permanent displacement $D_a$ of the potentially sliding mass [@BrayTravasarou2009; @MacedoEtAl2018]; the coefficients are reported at four relative displacement limits, $D_a/H_s$ = `r paste(.fmt(DAMAGE.CUTS, 1), collapse = ", ")`%, and the tables in Section [-@sec-kh-tables] report, for the demands and scenarios analyzed, the coefficient at each limit, expressed as a percentage of the PGA.
```

### B05 · `_local/gmdp.memo.en.qmd:66` · ediciones B05b, B05c, B05d, B05e

Actual:

```text
The verification of the slopes under those design earthquakes follows the practice that ICOLD and FEMA frame for dams and embankments through successive tiers of analysis: pseudostatic checks, simplified deformation estimates, and dynamic analyses when the consequence, the anticipated response, or the complexity of the mechanism requires them [@ICOLD2016; @FEMA2005].
```

Propuesta:

```text
The verification of the slopes under those design earthquakes follows the practice that ICOLD and FEMA frame for dams and embankments through successive tiers of analysis including pseudostatic stability checks, simplified estimates of permanent deformation, and dynamic analyses where warranted by the consequences of failure, anticipated response, or complexity of the failure mechanism [@ICOLD2016; @FEMA2005].
```

### B06 · `_local/gmdp.memo.en.qmd:66` · ediciones B06a, B06b, B06c, B06d, B06e

Actual:

```text
Within this framework, the Newmark method provides a deformation-based estimate that complements the limit-equilibrium verification, and the pseudostatic coefficient of that verification is a project-specific quantity rather than a universal property of the structure type.
```

Propuesta:

```text
Within this framework, the Newmark method provides a deformation-based assessment that complements the limit-equilibrium analysis. The pseudostatic seismic coefficient is a project-specific value rather than a universal value assigned to a particular structure type.
```

### B07 · `_local/gmdp.memo.en.qmd:66` · ediciones B07a, B07c, B07d, B07e

Actual:

```text
The USACE manuals EM 1110-2-1902 and EM 1110-2-2100 include pseudostatic analysis among the methods applicable to dams and earthworks and address the sliding block for estimating permanent seismic deformation; they tie the selection of the coefficient to the site-specific hazard, the potential failure mechanism, and the performance criteria of the project, so the coefficient results from the conditions of each project instead of a single value applicable to all of them [@USACE2003; @USACE2005].
```

Propuesta:

```text
USACE manuals EM 1110-2-1902 and EM 1110-2-2100 include pseudostatic analysis among the methods applicable to dams and earthworks and address the sliding block for estimating permanent seismic deformation. Selection of the coefficient considers the site-specific seismic hazard, potential failure mechanism, and project performance criteria, so the coefficient results from the conditions of each project instead of a single value applicable to all of them [@USACE2003; @USACE2005].
```

### B10 · `_local/gmdp.memo.en.qmd:70` · ediciones B10a

Actual:

```text
The coefficients of this report are read against four damage thresholds of the relative permanent displacement, $D_a/H$ = `r paste(.fmt(DAMAGE.CUTS, 1), collapse = ", ")`%: the crest-settlement ratios derived from ninety case histories of earthquake damage to embankment dams and associated with the Operational, Damage, Life Safety and Collapse limit states of the Italian dam code NTD14 [@Aliberti2019].
```

Propuesta:

```text
This report evaluates the coefficients at four damage thresholds of the relative permanent displacement, $D_a/H$ = `r paste(.fmt(DAMAGE.CUTS, 1), collapse = ", ")`%: the crest-settlement ratios derived from ninety case histories of earthquake damage to embankment dams and associated with the Operational, Damage, Life Safety and Collapse limit states of the Italian dam code NTD14 [@Aliberti2019].
```

### B11 · `_local/gmdp.memo.en.qmd:70` · ediciones B11a, B11b

Actual:

```text
Their denominator, the embankment height plus the thickness of the deformable foundation, is the slope height used here.
```

Propuesta:

```text
Their denominator, the reference height, includes the embankment height and the thickness of the deformable foundation and is adopted here as the slope height for normalization.
```

### B12 · `_local/gmdp.memo.en.qmd:70` · ediciones B12a, B12b

Actual:

```text
The coefficient tables are reported at those thresholds; the derivation of the coefficients from the allowable displacement is developed in Section [-@sec-coefficients].
```

Propuesta:

```text
The seismic coefficient tables are presented for these four thresholds. Section [-@sec-coefficients] describes the derivation of the coefficients from the allowable displacement.
```

### B15 · `_local/gmdp.memo.en.qmd:88` · ediciones B15d

Actual:

```text
The equivalent truncated section in the Dakoulas--Gazetas model [-@DakoulasGazetas1985Inhomogeneous] is specified by the height $H_s$, slope ratio $s$, and truncation ratio $\lambda_o$; with $\tan\beta=1/s$, where $\beta$ is the slope angle, the berm width is
```

Propuesta:

```text
The equivalent truncated section in the Dakoulas--Gazetas model [-@DakoulasGazetas1985Inhomogeneous] is specified by the height $H_s$, slope ratio $s$, and truncation ratio $\lambda_o$; with $\tan\beta=1/s$, where $\beta$ is the slope angle, the berm width is given by
```

### B16 · `_local/gmdp.memo.en.qmd:106` · ediciones B16a

Actual:

```text
where $G_o$ is the fitted small-strain shear modulus at the base, $g$ is the acceleration of gravity, and $\gamma_{\mathrm{sat}}^{(k_{\mathrm{b}})}$ is the saturated unit weight of the basal layer, whose index is $k_{\mathrm{b}}$; all quantities are expressed in consistent units.
```

Propuesta:

```text
where $G_o$ is the fitted small-strain shear modulus at the base, $g$ is the acceleration of gravity, and $\gamma_{\mathrm{sat}}^{(k_{\mathrm{b}})}$ is the saturated unit weight of the basal layer, indexed by $k_{\mathrm{b}}$; all quantities are expressed in consistent units.
```

### B21 · `_local/gmdp.memo.en.qmd:157` · ediciones B21a

Actual:

```text
For each geometry--material combination, the analysis generates $N$ synthetic realizations of the layered profile, and each of $G_o$, $m_o$, $V_S^o$, and $V_{S30}$ is summarized by its mean and selected marginal fractiles; for the mean and for each reported fractile, $a_1$ and $T_s$ are evaluated from the corresponding $m_o$ and $V_S^o$ values, and the mean estimates provide the dynamic properties used in the displacement analysis.
```

Propuesta:

```text
For each geometry--material combination, the analysis generates $N$ synthetic realizations of the layered profile, and each of $G_o$, $m_o$, $V_S^o$, and $V_{S30}$ is summarized by its mean and selected marginal fractiles; for the mean and for each reported fractile, $a_1$ and $T_s$ are evaluated from the corresponding $m_o$ and $V_S^o$ values, and the estimates calculated from the mean parameter values provide the dynamic properties used in the displacement analysis.
```

### B25 · `_local/gmdp.memo.en.qmd:182` · ediciones B25b, B25c

Actual:

```text
In this memo the coefficient is derived from displacement-based performance: the Newmark permanent displacement $D_n$ is the slope-deformation performance measure, and the coefficient $k_{\max}$ is the lowest yield acceleration $k_y$ consistent with a performance objective defined by the allowable displacement $D_a$ and the target probability $p_e$ that $D_n$ exceeds $D_a$.
```

Propuesta:

```text
In this memo the coefficient is derived from displacement-based performance: the Newmark permanent displacement $D_n$ is the slope-deformation performance measure, and the coefficient $k_{\max}$ is the lowest yield coefficient $k_y$ consistent with a performance objective defined by the allowable displacement $D_a$ and the target maximum probability $p_e$ that $D_n$ exceeds $D_a$.
```

### B26 · `_local/gmdp.memo.en.qmd:182` · ediciones B26a

Actual:

```text
The normalized coefficient $k_h$ expresses $k_{\max}$ as a percentage of the PGA after site response is accounted for in each geometry--material combination, and the coefficients are reported by geometry, material and seismic demand.
```

Propuesta:

```text
The normalized coefficient $k_h$ expresses $k_{\max}$ as a percentage of the site-condition PGA after site response is accounted for in each geometry--material combination, and the coefficients are reported by geometry, material and seismic demand.
```

### B27 · `_local/gmdp.memo.en.qmd:184` · ediciones B27a

Actual:

```text
The seismic demand and the fundamental periods established in the preceding sections allow the $D_n (k_y)$ relations between the Newmark permanent displacement and the yield acceleration to be computed; their inversion yields $k_{\max}$, and its normalization by the PGA transformed to the $V_{S30}$ of each geometry--material combination yields $k_h$, so that the result traceably links the deformation objective to the horizontal action employed in the stability verification.
```

Propuesta:

```text
The seismic demand and the fundamental periods established in the preceding sections allow the $D_n (k_y)$ relations between the Newmark permanent displacement and the yield coefficient to be computed; their inversion yields $k_{\max}$, and its normalization by the PGA transformed to the $V_{S30}$ of each geometry--material combination yields $k_h$, so that the result traceably links the deformation objective to the horizontal action employed in the stability verification.
```

### B28 · `_local/gmdp.memo.en.qmd:184` · ediciones B28d

Actual:

```text
The yield acceleration $a_y$ represents the acceleration level that mobilizes the available resistance along the potential failure mechanism, and its dimensionless form is $k_y=a_y/g$; for each allowable displacement and target exceedance probability, the analysis determines the $k_y$ threshold that satisfies the performance criterion, and that threshold is $k_{\max}$, the coefficient of the pseudostatic limit-equilibrium verification.
```

Propuesta:

```text
The yield acceleration $a_y$ represents the acceleration level that mobilizes the available resistance along the potential failure mechanism, and its dimensionless form is $k_y=a_y/g$; for each allowable displacement and target exceedance probability, the analysis determines the $k_y$ threshold that satisfies the performance criterion, and that threshold is $k_{\max}$, the coefficient applied in the pseudostatic limit-equilibrium verification.
```

### B30 · `_local/gmdp.memo.en.qmd:186` · ediciones B30a, B30b

Actual:

```text
In the Newmark sliding-block method [@Newmark1965], the wedge in potential sliding is a rigid block resting on an inclined plane: relative motion begins when the driving acceleration exceeds the yield acceleration $a_y=k_y g$ and continues until the relative velocity returns to zero, and the permanent displacement is the sum of those episodes over the duration of the earthquake motion, obtained by double integration of the acceleration excess.
```

Propuesta:

```text
In the Newmark sliding-block method [@Newmark1965], the potentially sliding wedge is represented as a rigid block resting on an inclined plane: relative motion begins when the driving acceleration exceeds the yield acceleration $a_y=k_y g$ and continues until the relative velocity returns to zero, and the permanent displacement is the sum of those episodes over the duration of the earthquake motion, obtained by double integration of the acceleration excess.
```

### B33 · `_local/gmdp.memo.en.qmd:188` · ediciones B33a, B33c

Actual:

```text
The probabilistic input of each return period is the reference-rock UHS, which for 10,000 years is the MDE, and the MCE input is the rock spectrum of each scenario; both retain the complete distribution of the rock demand, and both are defined for $V_{S30}=V_{\mathrm{ref}}=760$ m/s.
```

Propuesta:

```text
The probabilistic input for each return period is the reference-rock UHS, which for 10,000 years represents the MDE, and the MCE input is the rock spectrum of each scenario; both retain the complete distribution of the rock demand, and both are defined for $V_{S30}=V_{\mathrm{ref}}=760$ m/s.
```

### B35 · `_local/gmdp.memo.en.qmd:192` · ediciones B35a, B35b, B35c

Actual:

```text
For each scenario, 30 values of $k_y$ are evaluated, logarithmically distributed between 0.01 and $\max (\overline{\mathrm{PGA}},0.80)$, where $\overline{\mathrm{PGA}}$ is the mean site-condition PGA of the scenario; that interval establishes the computed support of the $D_n (k_y)$ relations, on which the formulations are evaluated and the inversion to $k_{\max}$ operates.
```

Propuesta:

```text
For each scenario, 30 values of $k_y$ are evaluated, logarithmically spaced between 0.01 and $\max (\overline{\mathrm{PGA}},0.80)$, where $\overline{\mathrm{PGA}}$ is the mean site-condition PGA of the scenario; that interval establishes the computed range of the $D_n (k_y)$ relations, over which the formulations are evaluated and the inversion to $k_{\max}$ operates.
```

### B37 · `_local/gmdp.memo.en.qmd:207` · ediciones B37a, B37b

Actual:

```text
The normalized coefficient, reported as a percentage of the PGA [% of PGA], is calculated with the PGA transformed to the $V_{S30}$ of the geometry--material combination evaluated for each demand:
```

Propuesta:

```text
The normalized coefficient, reported as a percentage of the PGA [% of PGA], is calculated using the site-condition PGA transformed to the $V_{S30}$ of the geometry--material combination evaluated for each demand:
```

### B38 · `_local/gmdp.memo.en.qmd:215` · ediciones B38a

Actual:

```text
The displacement model provides individual realizations for AM88, JB07, SR08, BT07, and a fifth formulation selected by the tectonic context: BM17 for projects with subduction control and BM19 for projects with crustal control.
```

Propuesta:

```text
The displacement model provides individual realizations for AM88, JB07, SR08, BT07, and a fifth formulation selected by the tectonic context: BM17 for projects with subduction control and BM19 for projects with shallow crustal control.
```

### B39 · `_local/gmdp.memo.en.qmd:217` · ediciones B39a

Actual:

```text
All models receive the same joint sample of PGA and spectral accelerations, and a single realization of $\epsilon$ is shared across the models and across all values of $k_y$; each formulation scales that residual through its own $\sigma_{\ln D}$, and the sampled PGA is retained with each realization so that the inversion keeps its demand state.
```

Propuesta:

```text
All models receive the same joint sample of PGA and spectral accelerations, and a single realization of $\epsilon$ is shared across the models and across all values of $k_y$; each formulation scales that residual through its own $\sigma_{\ln D}$, and the sampled PGA is retained with each realization so that the inversion preserves the pairing between displacement and seismic demand.
```

### B40 · `_local/gmdp.memo.en.qmd:217` · ediciones B40a

Actual:

```text
The realizations of $D_n$ are calculated for each material class with its mean dynamic properties; the fractiles of the stiffness profiles and of $T_s$ are not propagated as additional realizations in the displacement calculation, and each material class is kept as an independent input through the inversion to $k_{\max}$, so the displacement curves are not averaged across materials before that operation.
```

Propuesta:

```text
The realizations of $D_n$ are calculated for each material class with its mean dynamic properties; the fractiles of the stiffness profiles and of $T_s$ are not propagated as additional realizations in the displacement calculation, and each material class is kept as a separate scenario through the inversion to $k_{\max}$, so the displacement curves are not averaged across materials before that operation.
```

### B41 · `_local/gmdp.memo.en.qmd:219` · ediciones B41a, B41b

Actual:

```text
For each model and realization, the computed $D_n (k_y)$ relation is projected onto a non-increasing curve and inverted in the $(\ln D_n,\ln k_y)$ plane to solve the criterion of [-@eq-kmax-criterion]; when $D_a$ falls outside the calculated support, the relation is extended in that plane from the two points at the corresponding end, with the single exception of the AM88 limit treated in Section [-@sec-newmark-appendix].
```

Propuesta:

```text
For each model and realization, the computed $D_n (k_y)$ relation is projected onto a non-increasing curve and inverted in the $(\ln D_n,\ln k_y)$ plane to solve the criterion of [-@eq-kmax-criterion]; when $D_a$ falls outside the calculated range, the relation is extrapolated in that plane from the two points at the corresponding end, with the single exception of the AM88 limit treated in Section [-@sec-newmark-appendix].
```

### B42 · `_local/gmdp.memo.en.qmd:219` · ediciones B42a

Actual:

```text
The inversion is performed first per model within each realization.
```

Propuesta:

```text
The inversion is performed first for each model within each realization.
```

### B44 · `_local/gmdp.memo.en.qmd:227` · ediciones B44a, B44b

Actual:

```text
This grid contains, for every slope height, the damage thresholds $D_a/H$ = `r paste(.fmt(DAMAGE.CUTS, 1), collapse = ", ")`% of Section [-@sec-criteria], at which the coefficient tables are reported; values of $D_a$ that exceed the calculated support of a realization are obtained through the logarithmic extension defined above.
```

Propuesta:

```text
This grid contains, for every slope height, the damage thresholds $D_a/H$ = `r paste(.fmt(DAMAGE.CUTS, 1), collapse = ", ")`% of Section [-@sec-criteria], at which the coefficient tables are reported; values of $D_a$ that exceed the calculated range of a realization are obtained through the logarithmic extrapolation defined above.
```

## `_local/tbl.Ts.md`

### B46 · `_local/tbl.Ts.md:1` · ediciones B46b

Actual:

```text
Fundamental periods $T_s \approx T_1$ [s] and mean dynamic properties of the evaluated scenarios.
```

Propuesta:

```text
Fundamental periods $T_s \approx T_1$ [s] and mean dynamic properties of the evaluated slope scenarios.
```
