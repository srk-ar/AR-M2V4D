The Newmark permanent displacement $D_{n}$ quantifies the displacement induced by an earthquake and accumulated in the sliding mass and is the performance measure from which the seismic coefficients are derived. The $D_{n}(k_{y})$ curves relate, for each combination of geometry, material, and design scenario, the yield acceleration $k_{y}$ to the expected permanent displacement; they were computed with the ensemble set of AM88, JB07, SR08, BT07, and BM19, with the reference magnitude assigned to each seismic demand and 300 realizations per demand and are read at the fractiles $q = 1 - p_{e}$.

The Newmark permanent displacement $D_{n}$ quantifies the displacement induced by an earthquake accumulates in the sliding mass and is the performance measure from which the seismic coefficients are derived. The $D_{n}(k_{y})$ curves relate, for each combination of geometry, material, and design scenario, the yield acceleration $k_{y}$ to the expected permanent displacement; they were computed with an ensemble set of AM88 (Ambraseys & Menu, 1988), JB07 (Jibson, 2007), SR08 (Saygili & Rathje, 2008), BT07 (Bray & Travasarou, 2007), and BM19 (Bray & Macedo, 2019), with reference magnitudes $M_{w}$ = 5.5 and $M_{w}$ = 6.5 assigned according to the seismic demand and 300 realizations per demand and are read at the fractiles $q = 1 - p_{e}$. The horizontal pseudostatic coefficient $k_{h}$ is in turn derived from the allowable permanent displacement $D_{a}$ of the potentially sliding mass (Bray & Travasarou, Pseudostatic Coefficient for Use in Simplified Seismic Slope Stability Evaluation, 2009; Macedo, Bray, Abrahamson, & Travasarou, 2018); the coefficients are reported at four relative displacement limits, $D_{a}/H_{s}$ = 0.1, 0.4, 1.0, 2.5%, and the tables in Section **10.3** and **Appendix E** report, for the demands and scenarios analyzed, the coefficient at each limit, expressed as a percentage of the PGA.

where $\mu_{\ln D}$ and $\sigma_{\ln D}$ are the mean and standard deviation of $\ln D_{n}$ defined by each model, and $\epsilon$ is a standard-normal residual. Some source formulations contain a discrete branch of zero or negligible displacement; the implemented evaluation uses exclusively the positive lognormal branch, conditional on displacement exceeding the model’s zero-or-negligible-displacement threshold. In every formulation, $k_{y}$, PGA, and $S_{a}$ are expressed in units of $g$ – the acceleration of gravity – $I_{A}$ in m/s, and $T_{s}$ in seconds; the Arias intensity is derived from the PGA of each realization, and the reference magnitude is $M_{w} =$ 5.5 for return periods up to 2,500 years and $M_{w} =$ 6.5 for return periods of 5,000 and 10,000 years. Within each demand, that magnitude is common to the geometry, material and site combinations evaluated. The published form of each formulation is reproduced in **Appendix E**. The performance-based seismic coefficient is defined by

# Appendix E Seismic Coefficients

: Table E-1: Shear Stiffness Parameters for Gravels, Sands, and Fines

## E1 Newmark Permanent-Displacement Formulations

The seismic-coefficient section applies five Newmark permanent-displacement formulations: three rigid-block models, two flexible-block models and, among the latter, the BM branch selected by the tectonic control of the project. This section reproduces the published form of each formulation, including both BM branches, and states the rule that defines the active configuration. The rigid-block formulations relate the displacement to measures of the base excitation, whereas the flexible-block formulations additionally incorporate the dynamic response of the sliding mass through its fundamental period $\mathbf{T}_{\mathbf{s}}$ and the spectral acceleration evaluated at a period proportional to $\mathbf{T}_{\mathbf{s}}$.

Rigid-Block Models

The AM88 formulation (Ambraseys & Menu, 1988) uses the ratio of yield acceleration to PGA, capped to preserve the logarithmic domain, $\mathbf{r}^{\mathbf{\star}}\mathbf{= min(}\mathbf{k}_{\mathbf{y}}\mathbf{/PGA,}\mathbf{0.9999}\mathbf{)}$:

$\begin{array}{r}
\mu_{\ln D} = \ln(10)\left\lbrack 0.90 + \log_{10}\left( (1 - r^{\star})^{2.53}(r^{\star})^{- 1.09} \right) \right\rbrack, \\
\sigma_{\ln D} = 0.30\ln(10).
\end{array}$ (E1-1)

The two remaining rigid-block formulations, JB07 and SR08, use the Arias intensity, which is estimated for each realization from the PGA; $\mathbf{I}_{\mathbf{A}}$ is expressed in m/s and PGA in units of $\mathbf{g}$, and the estimate is applied deterministically, so that each PGA realization determines a single value of $\mathbf{I}_{\mathbf{A}}$ and the displacement sample propagates the PGA variability. The JB07 formulation (Jibson, 2007) incorporates the Arias intensity and the ratio $\mathbf{k}_{\mathbf{y}}\mathbf{/PGA}$:

$\begin{array}{r}
\mu_{\ln D} = \ln(10)\left\lbrack 0.561\log_{10}I_{A} - 3.833\log_{10}\left( \frac{k_{y}}{PGA} \right) - 1.474 \right\rbrack, \\
\sigma_{\ln D} = 0.616\ln(10).
\end{array}$ (E1-2)

The SR08 formulation (Saygili & Rathje, 2008) defines $\mathbf{r}\mathbf{=}\mathbf{k}_{\mathbf{y}}\mathbf{/PGA}$ and combines PGA and Arias intensity:

$\begin{array}{r}
\mu_{\ln D} = 2.39 - 5.24r - 18.78r^{2} + 42.01r^{3} - 29.15r^{4} \\
 - 1.56\ln PGA + 1.38\ln I_{A}, \\
\sigma_{\ln D} = 0.46 + 0.56r.
\end{array}$ (E1-3)

The logarithmic extension of the $\mathbf{D}_{\mathbf{n}}\mathbf{(}\mathbf{k}_{\mathbf{y}}\mathbf{)}$ relations beyond their computed support has one exception, the AM88 limit. If the sampled PGA of a realization, $\mathbf{PGA}_{\mathbf{s}}$, is smaller than the lower end of the grid, all stored points may satisfy $\mathbf{k}_{\mathbf{y}}\mathbf{/}\mathbf{PGA}_{\mathbf{s}}\mathbf{\geq}\mathbf{r}_{\mathbf{\max}}\mathbf{=}\mathbf{0.9999}$ and form a plateau $\mathbf{D}_{\mathbf{0}\mathbf{,}\mathbf{s}}$. In that case the physical branch $\mathbf{0}\mathbf{<}\mathbf{r}\mathbf{<}\mathbf{r}_{\mathbf{\max}}$ of Eq. E1-1 is solved for $\mathbf{D}_{\mathbf{a}}\mathbf{>}\mathbf{D}_{\mathbf{0}\mathbf{,}\mathbf{s}}$, instead of extrapolating the plateau or assigning $\mathbf{k}_{\mathbf{\max}}\mathbf{=}\mathbf{0}$:

$\mu_{\ln D}(r) = \ln D_{a} - \ln D_{0,s} + \mu_{\ln D}(r_{\max}),\quad\quad k_{\max,s} = {PGA}_{s}r.$ (E1-4)

The random residual cancels between $\mathbf{D}_{\mathbf{a}}$ and $\mathbf{D}_{\mathbf{0}\mathbf{,}\mathbf{s}}$, and $\mathbf{d}\mathbf{\mu}_{\mathbf{\ln}\mathbf{D}}\mathbf{/d}\mathbf{r}\mathbf{= -}\mathbf{2.53}\mathbf{/(}\mathbf{1}\mathbf{-}\mathbf{r}\mathbf{) -}\mathbf{1.09}\mathbf{/}\mathbf{r}\mathbf{<}\mathbf{0}$, so the root is unique. An AM88 plateau is accepted only when the original curve is exactly constant and $\mathbf{PGA}_{\mathbf{s}}$ itself shows that the entire grid reached that limit; a flat curve from another model, or a target $\mathbf{D}_{\mathbf{a}}\mathbf{\leq}\mathbf{D}_{\mathbf{0}\mathbf{,}\mathbf{s}}$, is rejected as non-identifiable support.

Flexible-Block Models

The flexible-block formulations evaluate the spectral acceleration at a period proportional to the fundamental period $\mathbf{T}_{\mathbf{s}}$ of the sliding mass. The BT07 formulation (Bray & Travasarou, Simplified Procedure for Estimating Earthquake-Induced Deviatoric Slope Displacements, 2007) employs $\mathbf{S}_{\mathbf{a}}\mathbf{=}\mathbf{S}_{\mathbf{a}}\mathbf{(}\mathbf{1.5}\mathbf{T}_{\mathbf{s}}\mathbf{)}$ and $\mathbf{M}_{\mathbf{w}}$:

$\begin{array}{r}
\mu_{\ln D} = a_{0} - 2.83\ln k_{y} - 0.333(\ln k_{y})^{2} + 0.566\ln k_{y}\ln S_{a} \\
 + 3.04\ln S_{a} - 0.244(\ln S_{a})^{2} + 1.50T_{s} + 0.278(M_{w} - 7), \\
a_{0} = \left\{ \begin{matrix}
 - 0.22, & T_{s} < 0.05\ s, \\
 - 1.10, & T_{s} \geq 0.05\ s,
\end{matrix} \right.\  \\
\sigma_{\ln D} = 0.66.
\end{array}$ (E1-5)

The BM17 formulation (Bray, Macedo, & Travasauro, Simplified procedure for estimating seismic slope displacements for subduction and crustal earthquakes, 2018) represents subduction-interface motions with $\mathbf{S}_{\mathbf{a}}\mathbf{=}\mathbf{S}_{\mathbf{a}}\mathbf{(}\mathbf{1.5}\mathbf{T}_{\mathbf{s}}\mathbf{)}$:

$\begin{array}{r}
\mu_{\ln D} = a_{0} + a_{1}\ln S_{a} - 0.225(\ln S_{a})^{2}, \\
a_{1} = 3.060 + 0.538\ln k_{y}, \\
a_{0, <} = - 5.864 + 0.550M_{w} - 9.421T_{s} \\
 - 3.353\ln k_{y} - 0.390(\ln k_{y})^{2}, \\
a_{0, \geq} = - 6.896 + 0.550M_{w} + 3.081T_{s} - 0.803T_{s}^{2} \\
 - 3.353\ln k_{y} - 0.390(\ln k_{y})^{2}, \\
a_{0} = \left\{ \begin{matrix}
a_{0, <}, & T_{s} < 0.1\ s, \\
a_{0, \geq}, & T_{s} \geq 0.1\ s,
\end{matrix} \right.\  \\
\sigma_{\ln D} = 0.73.
\end{array}$ (E1-6)

The BM19 formulation (Bray & Macedo, Procedure for Estimating Shear-Induced Seismic Slope Displacement for Shallow Crustal Earthquakes, 2019) represents ordinary shallow crustal motions with $\mathbf{S}_{\mathbf{a}}\mathbf{=}\mathbf{S}_{\mathbf{a}}\mathbf{(}\mathbf{1.3}\mathbf{T}_{\mathbf{s}}\mathbf{)}$:

$\begin{array}{r}
\mu_{\ln D} = a_{0} + \left( 2.649 + 0.344\ln k_{y} \right)\ln S_{a} - 0.090(\ln S_{a})^{2}, \\
a_{0, <} = - 4.684 + 0.603M_{w} - 9.471T_{s} \\
 - 2.482\ln k_{y} - 0.244(\ln k_{y})^{2}, \\
a_{0, \geq} = - 5.981 + 0.603M_{w} + 3.223T_{s} - 0.945T_{s}^{2} \\
 - 2.482\ln k_{y} - 0.244(\ln k_{y})^{2}, \\
a_{0} = \left\{ \begin{matrix}
a_{0, <}, & T_{s} < 0.1\ s, \\
a_{0, \geq}, & T_{s} \geq 0.1\ s,
\end{matrix} \right.\  \\
\sigma_{\ln D} = 0.72.
\end{array}$ (E1-7)

Ensemble

The active configuration applies five formulations: AM88, JB07, SR08, BT07, and one BM branch – BM17 when the project declares subduction control, BM19 when it declares crustal control; each evaluation therefore applies five formulations, never both BM branches at once. The predictors and dispersions are applied in the published form of each model, and the five formulations are combined with the equal weights and the rigid and flexible families defined in Section 10.1.3.

## E2 Seismic Coefficient in Acceleration Units

Figure E2-1 to Figure E2-3 show the horizontal seismic coefficient in units of g, as a function of the allowable permanent displacement relative to the slope height, for design earthquakes with AEPs of 1:500, 1:2,500, and 1:10,000 years. Table E2-1 to Table E2-5 list the coefficient in cm/s² for each scenario at the four relative displacement limits. The tables include the rigid, ensemble, and flexible sets.

Figure E2-1: Mean values of $\mathbf{k}_{\mathbf{\max}}$ [$\mathbf{g}$] for return period $\mathbf{T}_{\mathbf{R}}\mathbf{= 500}$ yr, as a function of the allowable permanent displacement relative to slope height, $\mathbf{D}_{\mathbf{a}}\mathbf{/}\mathbf{H}$ [%]. The curves represent the scenarios S135, S50, S32, S27, S35 evaluated with the rigid, ensemble, and flexible sets.

Notes:

> Color identifies the scenario and line pattern identifies the set: solid for rigid, short dashes for ensemble, and long dashes for flexible. The shaded bands are delimited by the damage thresholds $\mathbf{D}_{\mathbf{a}}\mathbf{/}\mathbf{H}\mathbf{=}\mathbf{0.1}\mathbf{,}\mathbf{0.4}\mathbf{,}\mathbf{1.0}\mathbf{,}\mathbf{2.5}$ %.

Figure E2-2: Mean values of $\mathbf{k}_{\mathbf{\max}}$ [$\mathbf{g}$] for return period $\mathbf{T}_{\mathbf{R}}\mathbf{= 2,500}$ yr, as a function of the allowable permanent displacement relative to slope height, $\mathbf{D}_{\mathbf{a}}\mathbf{/}\mathbf{H}$ [%]. The curves represent the scenarios S135, S50, S32, S27, S35 evaluated with the rigid, ensemble, and flexible sets.

Notes:

> Color identifies the scenario and line pattern identifies the set: solid for rigid, short dashes for ensemble, and long dashes for flexible. The shaded bands are delimited by the damage thresholds $\mathbf{D}_{\mathbf{a}}\mathbf{/}\mathbf{H}\mathbf{=}\mathbf{0.1}\mathbf{,}\mathbf{0.4}\mathbf{,}\mathbf{1.0}\mathbf{,}\mathbf{2.5}$ %.

Figure E2-3: Mean values of $\mathbf{k}_{\mathbf{\max}}$ [$\mathbf{g}$] for return period $\mathbf{T}_{\mathbf{R}}\mathbf{= 10,000}$ yr, as a function of the allowable permanent displacement relative to slope height, $\mathbf{D}_{\mathbf{a}}\mathbf{/}\mathbf{H}$ [%]. The curves represent the scenarios S135, S50, S32, S27, S35 evaluated with the rigid, ensemble, and flexible sets.

Notes:

> Color identifies the scenario and line pattern identifies the set: solid for rigid, short dashes for ensemble, and long dashes for flexible. The shaded bands are delimited by the damage thresholds $\mathbf{D}_{\mathbf{a}}\mathbf{/}\mathbf{H}\mathbf{=}\mathbf{0.1}\mathbf{,}\mathbf{0.4}\mathbf{,}\mathbf{1.0}\mathbf{,}\mathbf{2.5}$ %.

: Table E2-1: Mean values of $\mathbf{k}_{\mathbf{\max}}$ [cm/s²] for scenario S135 and return periods $\mathbf{T}_{\mathbf{R}}\mathbf{= 500,\ 2,500,\ 10,000}$ yr.

Notes:

> ID identifies the seismic demand and IDn the model set (rigid, ensemble, or flexible). $\mathbf{T}_{\mathbf{s}}$ is the fundamental period of the slope [s] and $\mathbf{V}_{\mathbf{S30}}$ the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the arithmetic mean at each allowable permanent displacement relative to slope height, $\mathbf{D}_{\mathbf{a}}\mathbf{/}\mathbf{H}$ [%]. The fractiles associated with the exceedance target $\mathbf{p}_{\mathbf{e}}$ are defined in the seismic-coefficient section.

: Table E2-2: Mean values of $\mathbf{k}_{\mathbf{\max}}$ [cm/s²] for scenario S50 and return periods $\mathbf{T}_{\mathbf{R}}\mathbf{= 500,\ 2,500,\ 10,000}$ yr.

Notes:

> ID identifies the seismic demand and IDn the model set (rigid, ensemble, or flexible). $\mathbf{T}_{\mathbf{s}}$ is the fundamental period of the slope [s] and $\mathbf{V}_{\mathbf{S30}}$ the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the arithmetic mean at each allowable permanent displacement relative to slope height, $\mathbf{D}_{\mathbf{a}}\mathbf{/}\mathbf{H}$ [%]. The fractiles associated with the exceedance target $\mathbf{p}_{\mathbf{e}}$ are defined in the seismic-coefficient section.

: Table E2-3: Mean values of $\mathbf{k}_{\mathbf{\max}}$ [cm/s²] for scenario S32 and return periods $\mathbf{T}_{\mathbf{R}}\mathbf{= 500,\ 2,500,\ 10,000}$ yr.

Notes:

> ID identifies the seismic demand and IDn the model set (rigid, ensemble, or flexible). $\mathbf{T}_{\mathbf{s}}$ is the fundamental period of the slope [s] and $\mathbf{V}_{\mathbf{S30}}$ the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the arithmetic mean at each allowable permanent displacement relative to slope height, $\mathbf{D}_{\mathbf{a}}\mathbf{/}\mathbf{H}$ [%]. The fractiles associated with the exceedance target $\mathbf{p}_{\mathbf{e}}$ are defined in the seismic-coefficient section.

: Table E2-4: Mean values of $\mathbf{k}_{\mathbf{\max}}$ [cm/s²] for scenario S27 and return periods $\mathbf{T}_{\mathbf{R}}\mathbf{= 500,\ 2,500,\ 10,000}$ yr.

Notes:

> ID identifies the seismic demand and IDn the model set (rigid, ensemble, or flexible). $\mathbf{T}_{\mathbf{s}}$ is the fundamental period of the slope [s] and $\mathbf{V}_{\mathbf{S30}}$ the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the arithmetic mean at each allowable permanent displacement relative to slope height, $\mathbf{D}_{\mathbf{a}}\mathbf{/}\mathbf{H}$ [%]. The fractiles associated with the exceedance target $\mathbf{p}_{\mathbf{e}}$ are defined in the seismic-coefficient section.

: Table E2-5: Mean values of $\mathbf{k}_{\mathbf{\max}}$ [cm/s²] for scenario S35 and return periods $\mathbf{T}_{\mathbf{R}}\mathbf{= 500,\ 2,500,\ 10,000}$ yr.

Notes:

> ID identifies the seismic demand and IDn the model set (rigid, ensemble, or flexible). $\mathbf{T}_{\mathbf{s}}$ is the fundamental period of the slope [s] and $\mathbf{V}_{\mathbf{S30}}$ the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the arithmetic mean at each allowable permanent displacement relative to slope height, $\mathbf{D}_{\mathbf{a}}\mathbf{/}\mathbf{H}$ [%]. The fractiles associated with the exceedance target $\mathbf{p}_{\mathbf{e}}$ are defined in the seismic-coefficient section.

## E3 Seismic Coefficient as a Percentage of PGA

Table E3-1 to Table E3-5 list the horizontal seismic coefficient, expressed as a percentage of the PGA, for each scenario at the four relative displacement limits. The tables include the rigid, ensemble, and flexible sets. The coefficients of the ensemble set for the 1:2,500 and 1:10,000 year design earthquakes are also summarized in Table 10-2.

: Table E3-1: Mean values of $\mathbf{k}_{\mathbf{h}}$ [% of PGA] for scenario S135 and return periods $\mathbf{T}_{\mathbf{R}}\mathbf{= 500,\ 2,500,\ 10,000}$ yr.

Notes:

> ID identifies the seismic demand and IDn the model set (rigid, ensemble, or flexible). $\mathbf{T}_{\mathbf{s}}$ is the fundamental period of the slope [s] and $\mathbf{V}_{\mathbf{S30}}$ the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the mean estimate at each allowable permanent displacement relative to slope height, $\mathbf{D}_{\mathbf{a}}\mathbf{/}\mathbf{H}$ [%], expressed as $\mathbf{100}\mathbf{}\mathbf{k}_{\mathbf{\max}}\mathbf{/PGA(}\mathbf{V}_{\mathbf{S30}}\mathbf{)}$.

: Table E3-2: Mean values of $\mathbf{k}_{\mathbf{h}}$ [% of PGA] for scenario S50 and return periods $\mathbf{T}_{\mathbf{R}}\mathbf{= 500,\ 2,500,\ 10,000}$ yr.

Notes:

> ID identifies the seismic demand and IDn the model set (rigid, ensemble, or flexible). $\mathbf{T}_{\mathbf{s}}$ is the fundamental period of the slope [s] and $\mathbf{V}_{\mathbf{S30}}$ the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the mean estimate at each allowable permanent displacement relative to slope height, $\mathbf{D}_{\mathbf{a}}\mathbf{/}\mathbf{H}$ [%], expressed as $\mathbf{100}\mathbf{}\mathbf{k}_{\mathbf{\max}}\mathbf{/PGA(}\mathbf{V}_{\mathbf{S30}}\mathbf{)}$.

: Table E3-3: Mean values of $\mathbf{k}_{\mathbf{h}}$ [% of PGA] for scenario S32 and return periods $\mathbf{T}_{\mathbf{R}}\mathbf{= 500,\ 2,500,\ 10,000}$ yr.

Notes:

> ID identifies the seismic demand and IDn the model set (rigid, ensemble, or flexible). $\mathbf{T}_{\mathbf{s}}$ is the fundamental period of the slope [s] and $\mathbf{V}_{\mathbf{S30}}$ the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the mean estimate at each allowable permanent displacement relative to slope height, $\mathbf{D}_{\mathbf{a}}\mathbf{/}\mathbf{H}$ [%], expressed as $\mathbf{100}\mathbf{}\mathbf{k}_{\mathbf{\max}}\mathbf{/PGA(}\mathbf{V}_{\mathbf{S30}}\mathbf{)}$.

: Table E3-4: Mean values of $\mathbf{k}_{\mathbf{h}}$ [% of PGA] for scenario S27 and return periods $\mathbf{T}_{\mathbf{R}}\mathbf{= 500,\ 2,500,\ 10,000}$ yr.

Notes:

> ID identifies the seismic demand and IDn the model set (rigid, ensemble, or flexible). $\mathbf{T}_{\mathbf{s}}$ is the fundamental period of the slope [s] and $\mathbf{V}_{\mathbf{S30}}$ the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the mean estimate at each allowable permanent displacement relative to slope height, $\mathbf{D}_{\mathbf{a}}\mathbf{/}\mathbf{H}$ [%], expressed as $\mathbf{100}\mathbf{}\mathbf{k}_{\mathbf{\max}}\mathbf{/PGA(}\mathbf{V}_{\mathbf{S30}}\mathbf{)}$.

: Table E3-5: Mean values of $\mathbf{k}_{\mathbf{h}}$ [% of PGA] for scenario S35 and return periods $\mathbf{T}_{\mathbf{R}}\mathbf{= 500,\ 2,500,\ 10,000}$ yr.

Notes:

> ID identifies the seismic demand and IDn the model set (rigid, ensemble, or flexible). $\mathbf{T}_{\mathbf{s}}$ is the fundamental period of the slope [s] and $\mathbf{V}_{\mathbf{S30}}$ the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the mean estimate at each allowable permanent displacement relative to slope height, $\mathbf{D}_{\mathbf{a}}\mathbf{/}\mathbf{H}$ [%], expressed as $\mathbf{100}\mathbf{}\mathbf{k}_{\mathbf{\max}}\mathbf{/PGA(}\mathbf{V}_{\mathbf{S30}}\mathbf{)}$.
