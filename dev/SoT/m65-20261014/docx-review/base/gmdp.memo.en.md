+-----------+-------------------------------------------------+------------------------------------------+
|           | **Ground-Motion Design Parameters**             |                                          |
+===========+=================================================+==========================================+
|           | **Prepared for**                                                                           |
|           |                                                                                            |
|           | Canada Nickel Co.                                                                          |
+-----------+--------------------------------------------------------------------------------------------+
|           | **Prepared by**                                                                            |
|           |                                                                                            |
|           | ![SRK Consulting logo](./media/srk-na-logo.wmf){width="3.67in" height="0.42in"}            |
|           |                                                                                            |
|           | SRK Consulting (Canada), Inc. and Paterson & Cooke                                         |
|           |                                                                                            |
|           | AR-M2V4D                                                                                   |
|           |                                                                                            |
|           | 24/09/2026                                                                                 |
+-----------+--------------------------------------------------------------------------------------------+

+----+-----------------------------------------------------------------------------------------------+
|    | Ground-Motion Design Parameters                                                               |
+====+==========================================+====================================================+
|    | 24/09/2026                                                                                    |
+----+------------------------------------------+----------------------------------------------------+
|    | **Prepared for**                         | **Prepared by**                                    |
+----+------------------------------------------+----------------------------------------------------+
|    | Canada Nickel Co.                        | SRK Consulting (Canada), Inc. and Paterson & Cooke |
+----+------------------------------------------+----------------------------------------------------+
|    |                                          | Web: https://www.srk.com/                          |
+----+------------------------------------------+----------------------------------------------------+
|    | Project No.: AR-M2V4D                                                                         |
|    |                                                                                               |
|    | File Name: gmdp.memo.en.docx                                                                  |
+----+-----------------------------------------------------------------------------------------------+
|    | ![SRK Consulting logo](./media/srk-na-logo.wmf){width="3.67in" height="0.42in"}               |
+----+-----------------------------------------------------------------------------------------------+

# Ground-Motion Design Parameters

SRK Consulting (Canada), Inc. and Paterson & Cooke prepared this report for Canada Nickel Co. under project AR-M2V4D, located in Timmins, Ontario, Canada. It reports the dynamic properties of the slopes analysed, the permanent displacements the design earthquakes accumulate in their potential sliding masses, and the performance-based seismic coefficients derived from those displacements. The flexible sliding-block displacement models require the fundamental period of each potential sliding mass and the dynamic soil stiffness that determines it: the analyses considered 5 geometry–material scenarios with heights between 27 and 135 m, and the estimated fundamental period varies between 0.19 and 0.83 s.

The Newmark permanent displacement $D_{n}$ quantifies the deformation an earthquake accumulates in the sliding mass and is the performance measure from which the seismic coefficients are derived. The $D_{n}(k_{y})$ curves relate, for each combination of geometry, material, and design scenario, the yield acceleration $k_{y}$ to the expected permanent displacement; they were computed with the `ensemble` set of `AM88`, `JB07`, `SR08`, `BT07`, and `BM19`, with the reference magnitude $M_{w}$ = 7.0 and 300 realizations per demand, and are read at the fractiles $q = 1 - p_{e}$. The horizontal pseudostatic coefficient $k_{h}$ is in turn derived from the allowable permanent displacement $D_{a}$ of the potentially sliding mass ([Bray and Travasarou 2009](#ref-BrayTravasarou2009); [Macedo et al. 2018](#ref-MacedoEtAl2018)); the coefficients are reported at four relative displacement limits, $D_{a}/H_{s}$ = 0.1, 0.4, 1.0, 2.5%, and the tables in Section [1.5](#sec-kh-tables) report, for the demands and scenarios analysed, the coefficient at each limit, expressed as a percentage of the PGA.

## Seismic Design Criteria for Slopes

The seismic design of tailings storage facilities is based on the two-level performance framework consolidated by dam-safety practice: an Operating Basis Earthquake (OBE), which the facility must withstand without operational interruption, and a Safety Evaluation Earthquake (SEE), under which it must not release tailings. ICOLD Bulletin 148 formalizes this framework for embankment structures ([International Commission on Large Dams 2016](#ref-ICOLD2016); [Australian National Committee on Large Dams 2012](#ref-ANCOLD2012)), and the USACE Engineer Regulation ER 1110-2-1806 expresses it in terms of the OBE and the Maximum Design Earthquake (MDE) ([U.S. Army Corps of Engineers 1995](#ref-USACE1995)). In this report, the MDE is represented by the probabilistic spectrum for a 10,000-year return period, whereas the MCE is represented by the deterministic envelope.

The verification of the slopes under those design earthquakes follows the practice that ICOLD and FEMA frame for dams and embankments through successive tiers of analysis: pseudostatic checks, simplified deformation estimates, and dynamic analyses when the consequence, the anticipated response, or the complexity of the mechanism requires them ([International Commission on Large Dams 2016](#ref-ICOLD2016); [Federal Emergency Management Agency 2005](#ref-FEMA2005)). Within this framework, the Newmark method provides a deformation-based estimate that complements the limit-equilibrium verification, and the pseudostatic coefficient of that verification is a project-specific quantity rather than a universal property of the structure type. The USACE manuals EM 1110-2-1902 and EM 1110-2-2100 include pseudostatic analysis among the methods applicable to dams and earthworks and address the sliding block for estimating permanent seismic deformation; they tie the selection of the coefficient to the site-specific hazard, the potential failure mechanism, and the performance criteria of the project, so the coefficient results from the conditions of each project instead of a single value applicable to all of them ([U.S. Army Corps of Engineers 2003](#ref-USACE2003), [2005](#ref-USACE2005)).

Two further references relate the pseudostatic verification to the permanent deformation. NCHRP Report 611 formulates the seismic analysis of slopes and transportation infrastructure in terms of displacement-based performance and uses simplified Newmark correlations to relate demand to permanent deformation ([Anderson et al. 2008](#ref-AndersonEtAl2008)), and Eurocode 8 ties the pseudostatic action to the design seismic acceleration and the consequence class and admits Newmark displacement calculations when the ratio between the critical acceleration and the design acceleration justifies a deformation-based verification ([European Committee for Standardization 2004](#ref-CEN2004)). These references provide the framing and the comparison criteria for the coefficients of this report; their indicative values serve that comparison, and the displacement objective defined for the project governs the coefficients themselves.

That objective is expressed as an allowable permanent displacement relative to the slope height. The coefficients of this report are read against four damage thresholds of the relative permanent displacement, $D_{a}/H$ = 0.1, 0.4, 1.0, 2.5%: the crest-settlement ratios derived from ninety case histories of earthquake damage to embankment dams and associated with the Operational, Damage, Life Safety and Collapse limit states of the Italian dam code NTD14 ([Aliberti et al. 2019](#ref-Aliberti2019)). Their denominator, the embankment height plus the thickness of the deformable foundation, is the slope height used here. The coefficient tables are reported at those thresholds; the derivation of the coefficients from the allowable displacement is developed in Section [1.3](#sec-coefficients).

## Dynamic Properties of Slopes

Flexible sliding-block models account for the dynamic response of the potential sliding mass through spectral acceleration evaluated at a period proportional to its fundamental period, so each slope geometry–material combination needs $T_{s}$, which is derived from the geometry and the depth-dependent small-strain shear stiffness, described by $G_{o}$, $m_{o}$, and $V_{S}^{o}$; the mean values of $T_{s}$ and $V_{S30}$ provide the dynamic inputs to the permanent-displacement models. The fundamental period of the potential sliding mass is estimated from the first mode of the truncated inhomogeneous shear-beam model of Dakoulas and Gazetas ([1985](#ref-DakoulasGazetas1985Inhomogeneous)) as

$T_{s} = \frac{4\pi H_{s}}{a_{1}(2 - m_{o})V_{S}^{o}},$ (1)

where $H_{s}$ is the slope height, $V_{S}^{o}$ is the basal shear-wave velocity associated with $G_{o}$, $m_{o}$ is the inhomogeneity factor governing the shear-modulus profile, and $a_{1}$ is the first modal root of the characteristic equation. The modal root depends jointly on $m_{o}$ and the truncation ratio $\lambda_{o}$, which geometric similarity gives as

$\lambda_{o} = \frac{b}{b_{\max}},$ (2)

where $b$ and $b_{\max}$ are the berm and base widths, respectively. The equivalent truncated section in the Dakoulas–Gazetas model ([1985](#ref-DakoulasGazetas1985Inhomogeneous)) is specified by the height $H_{s}$, slope ratio $s$, and truncation ratio $\lambda_{o}$; with $\tan\beta = 1/s$, where $\beta$ is the slope angle, the berm width is

$b = \frac{2H_{s}s}{1/\lambda_{o} - 1}.$ (3)

and the base width is

$b_{\max} = b + 2H_{s}s.$ (4)

For each profile realization, the basal shear-wave velocity is

$V_{S}^{o} = \left( \frac{gG_{o}}{\gamma_{sat}^{(k_{b})}} \right)^{1/2},$ (5)

where $G_{o}$ is the fitted small-strain shear modulus at the base, $g$ is the acceleration of gravity, and $\gamma_{sat}^{(k_{b})}$ is the saturated unit weight of the basal layer, whose index is $k_{b}$; all quantities are expressed in consistent units. The depth dependence of small-strain shear stiffness is represented for each realization by the power-law profile

$G(z) = G_{o}\left( \frac{z}{H_{s}} \right)^{m_{o}},$ (6)

where $z$ is depth below the crest, $G_{o}$ is the fitted shear modulus at the base ($z/H_{s} = 1$), and $m_{o}$ is obtained from a logarithmic fit to the layer moduli $G_{m}^{(k)}$. Those layer moduli come from the soil classification: the USCS classification assigned to layer $k$ selects its soil family and the associated set of $J^{(k)}$ small-strain shear-modulus correlations compiled by Ishihara ([1996](#ref-Ishihara1996)), and the layer modulus is taken as their arithmetic mean,

[]{#eq-slope-modulus .anchor} $G_{m}^{(k)} = \frac{1}{J^{(k)}}\sum_{j = 1}^{J^{(k)}}A^{(j)}F_{e}^{(k,j)}\left\lbrack {OCR}^{(k)} \right\rbrack^{m_{1}^{(k)}}p_{ref}^{n^{(j)}}\left( \frac{p_{m}^{(k)}}{p_{ref}} \right)^{n^{(j)}}.$ (7)

Here $A^{(j)}$ and $n^{(j)}$ are tabulated correlation parameters, $F_{e}^{(k,j)}$ is the void-ratio function, $m_{1}^{(k)}$ is the overconsolidation exponent, $p_{m}^{(k)}$ is the layer-averaged effective octahedral normal stress, and $p_{ref} = 100$ kPa is the reference pressure. Under at-rest conditions, the layer-averaged effective octahedral normal stress $p_{m}^{(k)}$ ([1968](#ref-HardinBlack1968); [1972](#ref-HardinDrnevich1972)) is

$p_{m}^{(k)} = \frac{1 + 2K_{0}}{3}\left( \sum_{\ell = 1}^{k - 1}\gamma^{(\ell)}h^{(\ell)} + \frac{\gamma^{(k)}h^{(k)}}{2} \right),$ (8)

where $K_{0}$ is the at-rest lateral earth pressure coefficient, $\gamma^{(\ell)}$ and $h^{(\ell)}$ are the unit weight adopted for the groundwater condition and the thickness of layer $\ell$, and $\ell < k$ denotes the overlying layers. The layer overconsolidation ratio is ${OCR}^{(k)} = \max\lbrack(p_{m}^{(k)} + POP)/p_{m}^{(k)},1\rbrack$, where $POP$ is the preconsolidation pressure; for fine-grained soils, $m_{1}^{(k)} = f_{IP}({IP}^{(k)})$, whereas for sands and gravels $m_{1}^{(k)} = 0$ and the OCR multiplier is therefore unity. The void ratio $e_{0}^{(k)}$ enters all three soil families through $F_{e}^{(k,j)}$, which the correlations compiled by Ishihara ([1996](#ref-Ishihara1996)) define in terms of $e_{0}^{(k)}$ and $C_{e}^{(j)}$, with the index $j_{SS75}$ identifying the Shibata–Soelarno formulation ([1975](#ref-ShibataSoelarno1975)):

$F_{e}^{(k,j)} = \left\{ \begin{matrix}
C_{e}^{(j)} - \frac{e_{0}^{(k)}}{1 + e_{0}^{(k)}}, & j = j_{SS75}, \\
\frac{\left( C_{e}^{(j)} - e_{0}^{(k)} \right)^{2}}{1 + e_{0}^{(k)}}, & j \neq j_{SS75}.
\end{matrix} \right.\$ (9)

The shear-wave velocity of layer $k$ then follows from

$V_{S}^{(k)} = \left( \frac{gG_{m}^{(k)}}{\gamma_{sat}^{(k)}} \right)^{1/2},$ (10)

where $G_{m}^{(k)}$ is the adopted layer modulus and $\gamma_{sat}^{(k)}$ is its saturated unit weight; all quantities are expressed in consistent units.

 

+-------------------+--------------+--------------------------------+---------------------------+---------+-----------+---------+
| > **Formulation** | > **Family** | > **Reference material**       | > **Author**              | > **A** | > $C_{e}$ | > **n** |
+:=================:+==============+================================+===========================+=========+===========+=========+
| > HR63A           | > Sands      | > Angular-grain crushed sand   | > Hardin & Richart (1963) | > 3.27  | > 2.973   | > 0.50  |
+-------------------+--------------+--------------------------------+---------------------------+---------+-----------+---------+
| > HR63R           | > Sands      | > Round-grain Ottawa sand      | > Hardin & Richart (1963) | > 7.00  | > 2.174   | > 0.50  |
+-------------------+--------------+--------------------------------+---------------------------+---------+-----------+---------+
| > IW78            | > Sands      | > Several sands                | > Iwasaki et al.(1978)    | > 9.00  | > 2.174   | > 0.38  |
+-------------------+--------------+--------------------------------+---------------------------+---------+-----------+---------+
| > KO80            | > Sands      | > Toyoura sand                 | > Kokusho (1980)          | > 8.40  | > 2.173   | > 0.50  |
+-------------------+--------------+--------------------------------+---------------------------+---------+-----------+---------+
| > LO93            | > Sands      | > Ticino sands                 | > Lo Presti et.al (1993)  | > 7.10  | > 2.270   | > 0.43  |
+-------------------+--------------+--------------------------------+---------------------------+---------+-----------+---------+
| > SS75            | > Sands      | > Several sands                | > Shibata-Soelarno (1975) | > 42.00 | > 0.670   | > 0.50  |
+-------------------+--------------+--------------------------------+---------------------------+---------+-----------+---------+
| > YR84            | > Sands      | > Several sands                | > Yu-Richart (1984)       | > 7.00  | > 2.173   | > 0.50  |
+-------------------+--------------+--------------------------------+---------------------------+---------+-----------+---------+
| > HB68            | > Fines      | > Several undisturbed NC Clays | > Hardin & Black (1968)   | > 3.27  | > 2.973   | > 0.50  |
+-------------------+--------------+--------------------------------+---------------------------+---------+-----------+---------+
| > KU82C           | > Fines      | > Undisturbed NC Clay          | > Kokusho et al.(1982)    | > 0.14  | > 7.320   | > 0.60  |
+-------------------+--------------+--------------------------------+---------------------------+---------+-----------+---------+
| > MW72B           | > Fines      | > Reconstituted NC Bentonite   | > Marcuson & Wahls (1972) | > 0.45  | > 4.400   | > 0.50  |
+-------------------+--------------+--------------------------------+---------------------------+---------+-----------+---------+
| > MW72K           | > Fines      | > Reconstituted NC Kaoline     | > Marcuson & Wahls (1972) | > 4.50  | > 2.973   | > 0.50  |
+-------------------+--------------+--------------------------------+---------------------------+---------+-----------+---------+
| > ZU78A           | > Fines      | > Clay remolded IP=0-50%       | > Zen-Umehara (1978)      | > 2.00  | > 2.973   | > 0.50  |
+-------------------+--------------+--------------------------------+---------------------------+---------+-----------+---------+
| > ZU78B           | > Fines      | > Clay remolded IP=0-50%       | > Zen-Umehara (1978)      | > 3.00  | > 2.973   | > 0.50  |
+-------------------+--------------+--------------------------------+---------------------------+---------+-----------+---------+
| > ZU78C           | > Fines      | > Clay remolded IP=0-50%       | > Zen-Umehara (1978)      | > 4.00  | > 2.973   | > 0.50  |
+-------------------+--------------+--------------------------------+---------------------------+---------+-----------+---------+
| > GO87            | > Gravels    | > Gravel                       | > Goto et al.(1987)       | > 1.22  | > 2.170   | > 0.85  |
+-------------------+--------------+--------------------------------+---------------------------+---------+-----------+---------+
| > KE81G           | > Gravels    | > Rounded Gravel               | > Kokusho-Esashi (1981)   | > 8.40  | > 2.170   | > 0.60  |
+-------------------+--------------+--------------------------------+---------------------------+---------+-----------+---------+
| > KE81R           | > Gravels    | > Crushed Rock                 | > Kokusho-Esashi (1981)   | > 13.00 | > 2.170   | > 0.55  |
+-------------------+--------------+--------------------------------+---------------------------+---------+-----------+---------+
| > NI85            | > Gravels    | > Gravel                       | > Nishio et al.(1985)     | > 9.36  | > 2.170   | > 0.44  |
+-------------------+--------------+--------------------------------+---------------------------+---------+-----------+---------+
| > PR81            | > Gravels    | > Balast                       | > Prange (1981)           | > 7.23  | > 2.970   | > 0.38  |
+-------------------+--------------+--------------------------------+---------------------------+---------+-----------+---------+
| > TA87            | > Gravels    | > Gravel                       | > Tanaka et al.(1987)     | > 3.08  | > 2.170   | > 0.60  |
+-------------------+--------------+--------------------------------+---------------------------+---------+-----------+---------+

: Table 1: Parameters of the small-strain stiffness formulations for gravels, sands, and fine-grained soils, used in expression [7](#eq-slope-modulus) with $p_{m}^{(k)}$ and $p_{ref}$ in kPa and $G_{m}^{(k)}$ in MPa.

 

For each geometry–material combination, the analysis generates $N$ synthetic realizations of the layered profile, and each of $G_{o}$, $m_{o}$, $V_{S}^{o}$, and $V_{S30}$ is summarized by its mean and selected marginal fractiles; for the mean and for each reported fractile, $a_{1}$ and $T_{s}$ are evaluated from the corresponding $m_{o}$ and $V_{S}^{o}$ values, and the mean estimates provide the dynamic properties used in the displacement analysis. $V_{S30}$ is the travel-time-averaged shear-wave velocity in the uppermost 30 m:

$V_{S30} = \frac{30}{\sum_{i}^{}\frac{h_{30}^{(i)}}{V_{S}^{(i)}} + \frac{\max(30 - H_{s},0)}{V_{ref}}}.$ (11)

In this expression, $h_{30}^{(i)}$ is the portion of layer $i$ within the uppermost 30 m and $V_{S}^{(i)}$ is its shear-wave velocity; when $H_{s} < 30$ m, the reference velocity $V_{ref}$ is assigned to the remaining thickness.

<table>
<caption><p>Table 2: Fundamental periods <math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>T</mi><mi>s</mi></msub><mo>≈</mo><msub><mi>T</mi><mn>1</mn></msub></mrow><annotation encoding="application/x-tex">T_{s} \approx T_{1}</annotation></semantics></math> [s] and mean dynamic properties of the evaluated scenarios.<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></p></caption>
<thead>
<tr>
<th style="text-align: center;"><blockquote>
<p><strong>IDm</strong></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><strong>USCS</strong></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>H</mi><mi>s</mi></msub><annotation encoding="application/x-tex">H_{s}</annotation></semantics></math></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mi>b</mi><annotation encoding="application/x-tex">b</annotation></semantics></math></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mi>s</mi><annotation encoding="application/x-tex">s</annotation></semantics></math></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>λ</mi><mi>o</mi></msub><annotation encoding="application/x-tex">\lambda_{o}</annotation></semantics></math></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>m</mi><mi>o</mi></msub><annotation encoding="application/x-tex">m_{o}</annotation></semantics></math></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>a</mi><mn>1</mn></msub><annotation encoding="application/x-tex">a_{1}</annotation></semantics></math></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>G</mi><mi>o</mi></msub><annotation encoding="application/x-tex">G_{o}</annotation></semantics></math></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msubsup><mi>V</mi><mi>S</mi><mi>o</mi></msubsup><annotation encoding="application/x-tex">V_{S}^{o}</annotation></semantics></math></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>V</mi><mrow><mi>S</mi><mn>30</mn></mrow></msub><annotation encoding="application/x-tex">V_{S30}</annotation></semantics></math></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>T</mi><mi>s</mi></msub><annotation encoding="application/x-tex">T_{s}</annotation></semantics></math></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><blockquote>
<p>U1</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>ML MH</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>135</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>363</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>2.50</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>0.350</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>0.485</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>3.6559</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>261.8</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>366.7</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>193.0</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>0.835</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>U2</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>SP SM</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>50</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>108</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>2.75</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>0.282</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>0.479</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>3.3699</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>212.6</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>324.8</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>217.5</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>0.377</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>U3</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>SP SM ML MH</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>32</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>52</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>3.00</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>0.213</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>0.455</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>3.1162</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>146.2</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>271.5</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>205.6</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>0.308</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>U4</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>GP GW</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>27</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>29</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>3.25</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>0.142</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>0.547</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>3.1052</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>366.7</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>402.5</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>310.6</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>0.187</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>U5</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>GP GW SP SM</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>35</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>20</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>3.50</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>0.075</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>0.522</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>2.9759</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>276.9</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>357.5</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>251.4</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>0.280</p>
</blockquote></td>
</tr>
</tbody>
</table>
<section id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p><code>IDm</code> identifies the material scenario and <code>USCS</code> the classification of the slope materials. <math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>H</mi><mi>s</mi></msub><annotation encoding="application/x-tex">H_{s}</annotation></semantics></math> is the slope height and <math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mi>b</mi><annotation encoding="application/x-tex">b</annotation></semantics></math> the berm width, both in m; <math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mi>s</mi><annotation encoding="application/x-tex">s</annotation></semantics></math> is the slope ratio (<math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mrow><mi mathvariant="normal">tan</mi><mo>&#8289;</mo></mrow><mi>β</mi><mo>=</mo><mn>1</mn><mi>/</mi><mi>s</mi></mrow><annotation encoding="application/x-tex">\tan\beta = 1/s</annotation></semantics></math>) and <math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>λ</mi><mi>o</mi></msub><annotation encoding="application/x-tex">\lambda_{o}</annotation></semantics></math> the truncation ratio, both dimensionless; <math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>G</mi><mi>o</mi></msub><annotation encoding="application/x-tex">G_{o}</annotation></semantics></math> is the shear modulus of the profile at <math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>z</mi><mi>/</mi><msub><mi>H</mi><mi>s</mi></msub><mo>=</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">z/H_{s} = 1</annotation></semantics></math>, in MPa, and <math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>m</mi><mi>o</mi></msub><annotation encoding="application/x-tex">m_{o}</annotation></semantics></math> the exponent of its power law, dimensionless; <math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>a</mi><mn>1</mn></msub><annotation encoding="application/x-tex">a_{1}</annotation></semantics></math> is the first modal root, dimensionless; <math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msubsup><mi>V</mi><mi>S</mi><mi>o</mi></msubsup><annotation encoding="application/x-tex">V_{S}^{o}</annotation></semantics></math> is the basal shear-wave velocity and <math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>V</mi><mrow><mi>S</mi><mn>30</mn></mrow></msub><annotation encoding="application/x-tex">V_{S30}</annotation></semantics></math> the travel-time-averaged shear-wave velocity in the uppermost 30 m, both in m/s.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</section>

## Performance-Based Seismic Coefficient

Pseudostatic seismic design of slopes requires a horizontal coefficient representing earthquake loading on the sliding mass. In this memo the coefficient is derived from displacement-based performance: the Newmark permanent displacement $D_{n}$ is the slope-deformation performance measure, and the coefficient $k_{\max}$ is the lowest yield acceleration $k_{y}$ consistent with a performance objective defined by the allowable displacement $D_{a}$ and the target probability $p_{e}$ that $D_{n}$ exceeds $D_{a}$. The normalized coefficient $k_{h}$ expresses $k_{\max}$ as a percentage of the PGA after site response is accounted for in each geometry–material combination, and the coefficients are reported by geometry, material and seismic demand. For the slopes considered, $D_{n}$ is estimated probabilistically by combining empirical regression models within a lognormal framework.

The horizontal pseudostatic coefficient is derived in this assessment from the allowable permanent displacement $D_{a}$ of the potentially sliding mass ([Bray and Travasarou 2009](#ref-BrayTravasarou2009); [Macedo et al. 2018](#ref-MacedoEtAl2018)). The seismic demand and the fundamental periods established in the preceding sections allow the $D_{n}(k_{y})$ relations between the Newmark permanent displacement and the yield acceleration to be computed; their inversion yields $k_{\max}$, and its normalization by the PGA transformed to the $V_{S30}$ of each geometry–material combination yields $k_{h}$, so that the result traceably links the deformation objective to the horizontal action employed in the stability verification. The yield acceleration $a_{y}$ represents the acceleration level that mobilizes the available resistance along the potential failure mechanism, and its dimensionless form is $k_{y} = a_{y}/g$; for each allowable displacement and target exceedance probability, the analysis determines the $k_{y}$ threshold that satisfies the performance criterion, and that threshold is $k_{\max}$, the coefficient of the pseudostatic limit-equilibrium verification.

In the Newmark sliding-block method ([Newmark 1965](#ref-Newmark1965)), the wedge in potential sliding is a rigid block resting on an inclined plane: relative motion begins when the driving acceleration exceeds the yield acceleration $a_{y} = k_{y}g$ and continues until the relative velocity returns to zero, and the permanent displacement is the sum of those episodes over the duration of the earthquake motion, obtained by double integration of the acceleration excess. The extension of the procedure to dams and embankments ([Makdisi and Seed 1978](#ref-MakdisiSeed1978)) derived the equivalent acceleration of the sliding mass from its dynamic response and is the direct antecedent of the flexible formulations. The adopted empirical relations represent the accumulated displacement statistically through two idealizations: rigid-block models relate the displacement to measures of the base excitation, and flexible-block models additionally incorporate the dynamic response of the mass through $T_{s}$ and the spectral acceleration evaluated at a period proportional to $T_{s}$.

The displacement calculation uses the seismic demand and the fundamental periods established in Section [1.2](#sec-slope_periods). For each geometry, material and seismic demand – the probabilistic spectrum of each evaluated return period and the MCE scenario – a joint sample of the intensity measures required by the rigid-block and flexible formulations is constructed; that sample is common to all models, so their differences represent the displacement formulation rather than incompatible seismic demands. Two inputs feed that sample. The probabilistic input of each return period is the reference-rock UHS, which for 10,000 years is the MDE, and the MCE input is the rock spectrum of each scenario; both retain the complete distribution of the rock demand, and both are defined for $V_{S30} = V_{ref} = 760$ m/s. For each geometry and material scenario, the spectral ordinates and the PGA are transformed to the corresponding $V_{S30}$ through the `ST20` amplification model ([Stewart et al. 2020](#ref-Stewart2020); [Hashash et al. 2020](#ref-Hashash2020)).

At the site condition of each scenario, the joint sample comprises PGA, $S_{a}(1.3T_{s})$, and $S_{a}(1.5T_{s})$. The three measures are represented through empirical marginals in $\ln S_{a}$ and a Gaussian copula with the full inter-period correlation matrix ([Baker and Jayaram 2008](#ref-BakerJayaram2008)), and the samples are recentered to preserve the mean of each amplified marginal; in each realization, the three intensities remain paired, and each displacement formulation uses the measures entering its regression. The Arias intensity that `JB07` and `SR08` require completes the set of intensity measures; it is estimated for each realization from the PGA, so that each PGA realization determines a single value of $I_{A}$ and the displacement sample propagates the PGA variability.

For each scenario, 30 values of $k_{y}$ are evaluated, logarithmically distributed between 0.01 and $\max(\overline{PGA},0.80)$, where $\overline{PGA}$ is the mean site-condition PGA of the scenario; that interval establishes the computed support of the $D_{n}(k_{y})$ relations, on which the formulations are evaluated and the inversion to $k_{\max}$ operates.

Each active formulation estimates the Newmark permanent displacement ([1965](#ref-Newmark1965)) of the sliding mass from the yield acceleration and the intensity measures of its regression, and all of them express the positive displacement $D_{n}$, in centimeters, through

$D_{n} = \exp\left( \mu_{\ln D} + \epsilon\sigma_{\ln D} \right),\quad\quad\epsilon \sim \mathcal{N}(0,1),$ (12)

where $\mu_{\ln D}$ and $\sigma_{\ln D}$ are the mean and standard deviation of $\ln D_{n}$ defined by each model, and $\epsilon$ is a standard-normal residual. Some source formulations contain a discrete branch of zero or negligible displacement; the implemented evaluation uses exclusively the positive lognormal branch. In every formulation, $k_{y}$, PGA, and $S_{a}$ are expressed in units of $g$ – the acceleration of gravity – $I_{A}$ in m/s, and $T_{s}$ in seconds; the Arias intensity is derived from the PGA of each realization, and the reference magnitude of the project, $M_{w} =$ 7.0, is applied as a constant input to every demand, geometry, material and site evaluated. The published form of each formulation is reproduced in Section [1.6](#sec-newmark-appendix). The performance-based seismic coefficient is defined by

[]{#eq-kmax-criterion .anchor} $k_{\max}(p_{e} \mid D_{a}) = \inf\left\{ k_{y}:P\lbrack D_{n}(k_{y}) > D_{a}\rbrack \leq p_{e} \right\}.$ (13)

where $p_{e}$ is the target probability that $D_{n}$ exceeds $D_{a}$: $k_{\max}$ is the smallest $k_{y}$ for which the probability of exceeding the allowable displacement is at most $p_{e}$. The normalized coefficient, reported as a percentage of the PGA [% of PGA], is calculated with the PGA transformed to the $V_{S30}$ of the geometry–material combination evaluated for each demand:

$k_{h} = \frac{k_{\max}}{PGA(V_{S30})}.$ (14)

$k_{\max}$ is expressed in units of $g$ and $k_{h}$ as a percentage of the PGA of the corresponding site condition. These two quantities express the displacement criterion as the horizontal action of the pseudostatic verification.

The five formulations are evaluated individually and combined into the three sets that the tables and figures identify as `IDn`: `rigid`, `flexible` and `ensemble`. The displacement model provides individual realizations for AM88, JB07, SR08, BT07, and a fifth formulation selected by the tectonic context: BM17 for projects with subduction control and BM19 for projects with crustal control. The overall design set, identified as `ensemble`, combines AM88, JB07, SR08, BT07, and the active BM branch with equal weights; the rigid family combines AM88, JB07, and SR08, and the flexible family combines BT07 and the active BM branch. The rigid family thus relates the displacement to measures of the base excitation, the flexible family additionally incorporates the dynamic response of the sliding mass through $T_{s}$, and the ensemble is the design set that combines both. For each $k_{y}$, the displacements of a family are summarized from the weighted empirical distribution of the realizations of its models.

All models receive the same joint sample of PGA and spectral accelerations, and a single realization of $\epsilon$ is shared across the models and across all values of $k_{y}$; each formulation scales that residual through its own $\sigma_{\ln D}$, and the sampled PGA is retained with each realization so that the inversion keeps its demand state. The realizations of $D_{n}$ are calculated for each material class with its mean dynamic properties; the fractiles of the stiffness profiles and of $T_{s}$ are not propagated as additional realizations in the displacement calculation, and each material class is kept as an independent input through the inversion to $k_{\max}$, so the displacement curves are not averaged across materials before that operation.

For each model and realization, the computed $D_{n}(k_{y})$ relation is projected onto a non-increasing curve and inverted in the $(\ln D_{n},\ln k_{y})$ plane to solve the criterion of [13](#eq-kmax-criterion); when $D_{a}$ falls outside the calculated support, the relation is extended in that plane from the two points at the corresponding end, with the single exception of the AM88 limit treated in Section [1.6](#sec-newmark-appendix). The inversion is performed first per model within each realization.

The root distributions of the models are then combined with the family weights and summarized through the arithmetic mean and the empirical fractiles $q = 0.05$, 0.10, 0.16, 0.50, 0.84, 0.90, and 0.95 ([Verri Kozlowski 2026](#ref-VerriKozlowski2026Newmark)). Because of the decreasing relation between $D_{n}$ and $k_{y}$, the fractile associated with the exceedance target satisfies expression [15](#eq-kmax-fractile), where $q = 0.84$ corresponds to an exceedance probability of $p_{e} = 16\%$.

[]{#eq-kmax-fractile .anchor} $q = 1 - p_{e}$ (15)

The $q$ fractiles are therefore the statistics associated with the criterion expressed through $p_{e}$; the arithmetic mean summarizes the center of the simulated distribution and does not represent a target probability. The evaluation uses 300 realizations for each demand – the probabilistic spectrum of each return period $T_{R}$ = 500, 2,500, 10,000 years and the MCE – and a grid of allowable displacements $D_{a}/H_{s}$ ranging from 0.05 to 2.50 %. This grid contains, for every slope height, the damage thresholds $D_{a}/H$ = 0.1, 0.4, 1.0, 2.5% of Section [1.1](#sec-criteria), at which the coefficient tables are reported; values of $D_{a}$ that exceed the calculated support of a realization are obtained through the logarithmic extension defined above.

## Performance-Based Seismic Coefficient $k_{max}$

+:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:+
| ![](./media/rId30.png){width="6.3in" height="4.726666666666667in"}                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                          |
| Fig. 1: Mean values of $k_{\max}$ [$g$] for site CFD and return period $T_{R} = 500$ yr, as a function of the allowable permanent displacement relative to slope height, $D_{a}/H$ [%]. The curves represent the scenarios S135, S50, S32, S27, S35 evaluated with the `rigid`, `ensemble`, and `flexible` sets.[^2] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:+
| ![](./media/rId35.png){width="6.3in" height="4.726666666666667in"}                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                            |
| Fig. 2: Mean values of $k_{\max}$ [$g$] for site CFD and return period $T_{R} = 2,500$ yr, as a function of the allowable permanent displacement relative to slope height, $D_{a}/H$ [%]. The curves represent the scenarios S135, S50, S32, S27, S35 evaluated with the `rigid`, `ensemble`, and `flexible` sets.[^3] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:+
| ![](./media/rId40.png){width="6.3in" height="4.726666666666667in"}                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                             |
| Fig. 3: Mean values of $k_{\max}$ [$g$] for site CFD and return period $T_{R} = 10,000$ yr, as a function of the allowable permanent displacement relative to slope height, $D_{a}/H$ [%]. The curves represent the scenarios S135, S50, S32, S27, S35 evaluated with the `rigid`, `ensemble`, and `flexible` sets.[^4] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:+
| ![](./media/rId45.png){width="6.3in" height="4.726666666666667in"}                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                            |
| Fig. 4: Mean values of $k_{\max}$ [$g$] for site CFD under the MCE demand, as a function of the allowable permanent displacement relative to slope height, $D_{a}/H$ [%]. The curves represent the scenarios S135, S50, S32, S27, S35 evaluated with the `rigid`, `ensemble`, and `flexible` sets.[^5] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > **ID**       | > **IDn**  | > $T_{s}$ | > $V_{S30}$ | > **0.1%** | > **0.4%** | > **1%** | > **2.5%** |
+:==============:+============+===========+=============+============+============+==========+============+
| > TR 500 yr    | > ensemble | > 0.835   | > 193       | > 5        | > 1        | > 0      | > 0        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 500 yr    | > flexible | > 0.835   | > 193       | > 3        | > 0        | > 0      | > 0        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 500 yr    | > rigid    | > 0.835   | > 193       | > 6        | > 1        | > 0      | > 0        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > ensemble | > 0.835   | > 193       | > 31       | > 13       | > 6      | > 3        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > flexible | > 0.835   | > 193       | > 17       | > 4        | > 1      | > 0        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > rigid    | > 0.835   | > 193       | > 40       | > 18       | > 10     | > 5        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > ensemble | > 0.835   | > 193       | > 75       | > 36       | > 19     | > 10       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > flexible | > 0.835   | > 193       | > 42       | > 14       | > 4      | > 1        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > rigid    | > 0.835   | > 193       | > 97       | > 51       | > 28     | > 16       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > ensemble | > 0.835   | > 193       | > 75       | > 40       | > 24     | > 13       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > flexible | > 0.835   | > 193       | > 9        | > 2        | > 0      | > 0        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > rigid    | > 0.835   | > 193       | > 119      | > 66       | > 40     | > 22       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+

: Table 3: Mean values of $k_{\max}$ [cm/s2] for site CFD, scenario S135, under the MCE demand and return periods $T_{R} = 500,2,500,10,000$ yr.[^6]

 

 

+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > **ID**       | > **IDn**  | > $T_{s}$ | > $V_{S30}$ | > **0.1%** | > **0.4%** | > **1%** | > **2.5%** |
+:==============:+============+===========+=============+============+============+==========+============+
| > TR 500 yr    | > ensemble | > 0.377   | > 217.5     | > 13       | > 4        | > 1      | > 0        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 500 yr    | > flexible | > 0.377   | > 217.5     | > 16       | > 3        | > 0      | > 0        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 500 yr    | > rigid    | > 0.377   | > 217.5     | > 12       | > 5        | > 2      | > 0        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > ensemble | > 0.377   | > 217.5     | > 53       | > 26       | > 13     | > 6        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > flexible | > 0.377   | > 217.5     | > 48       | > 17       | > 5      | > 1        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > rigid    | > 0.377   | > 217.5     | > 57       | > 32       | > 19     | > 9        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > ensemble | > 0.377   | > 217.5     | > 125      | > 69       | > 41     | > 21       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > flexible | > 0.377   | > 217.5     | > 101      | > 44       | > 20     | > 6        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > rigid    | > 0.377   | > 217.5     | > 140      | > 86       | > 55     | > 31       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > ensemble | > 0.377   | > 217.5     | > 110      | > 64       | > 41     | > 24       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > flexible | > 0.377   | > 217.5     | > 32       | > 11       | > 3      | > 0        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > rigid    | > 0.377   | > 217.5     | > 162      | > 100      | > 66     | > 39       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+

: Table 4: Mean values of $k_{\max}$ [cm/s2] for site CFD, scenario S50, under the MCE demand and return periods $T_{R} = 500,2,500,10,000$ yr.[^7]

 

 

+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > **ID**       | > **IDn**  | > $T_{s}$ | > $V_{S30}$ | > **0.1%** | > **0.4%** | > **1%** | > **2.5%** |
+:==============:+============+===========+=============+============+============+==========+============+
| > TR 500 yr    | > ensemble | > 0.308   | > 205.6     | > 20       | > 8        | > 3      | > 1        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 500 yr    | > flexible | > 0.308   | > 205.6     | > 26       | > 8        | > 2      | > 0        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 500 yr    | > rigid    | > 0.308   | > 205.6     | > 15       | > 7        | > 3      | > 1        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > ensemble | > 0.308   | > 205.6     | > 67       | > 36       | > 20     | > 9        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > flexible | > 0.308   | > 205.6     | > 68       | > 29       | > 12     | > 3        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > rigid    | > 0.308   | > 205.6     | > 67       | > 41       | > 25     | > 14       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > ensemble | > 0.308   | > 205.6     | > 151      | > 88       | > 56     | > 31       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > flexible | > 0.308   | > 205.6     | > 134      | > 62       | > 32     | > 12       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > rigid    | > 0.308   | > 205.6     | > 162      | > 105      | > 72     | > 44       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > ensemble | > 0.308   | > 205.6     | > 133      | > 81       | > 54     | > 33       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > flexible | > 0.308   | > 205.6     | > 54       | > 22       | > 9      | > 2        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > rigid    | > 0.308   | > 205.6     | > 186      | > 121      | > 84     | > 53       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+

: Table 5: Mean values of $k_{\max}$ [cm/s2] for site CFD, scenario S32, under the MCE demand and return periods $T_{R} = 500,2,500,10,000$ yr.[^8]

 

 

+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > **ID**       | > **IDn**  | > $T_{s}$ | > $V_{S30}$ | > **0.1%** | > **0.4%** | > **1%** | > **2.5%** |
+:==============:+============+===========+=============+============+============+==========+============+
| > TR 500 yr    | > ensemble | > 0.187   | > 310.6     | > 21       | > 8        | > 3      | > 1        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 500 yr    | > flexible | > 0.187   | > 310.6     | > 29       | > 9        | > 2      | > 0        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 500 yr    | > rigid    | > 0.187   | > 310.6     | > 15       | > 7        | > 3      | > 1        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > ensemble | > 0.187   | > 310.6     | > 83       | > 45       | > 27     | > 13       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > flexible | > 0.187   | > 310.6     | > 97       | > 44       | > 21     | > 6        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > rigid    | > 0.187   | > 310.6     | > 74       | > 47       | > 30     | > 17       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > ensemble | > 0.187   | > 310.6     | > 194      | > 113      | > 73     | > 41       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > flexible | > 0.187   | > 310.6     | > 207      | > 100      | > 54     | > 23       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > rigid    | > 0.187   | > 310.6     | > 185      | > 122      | > 85     | > 54       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > ensemble | > 0.187   | > 310.6     | > 176      | > 107      | > 72     | > 44       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > flexible | > 0.187   | > 310.6     | > 121      | > 55       | > 28     | > 11       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > rigid    | > 0.187   | > 310.6     | > 212      | > 142      | > 101    | > 66       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+

: Table 6: Mean values of $k_{\max}$ [cm/s2] for site CFD, scenario S27, under the MCE demand and return periods $T_{R} = 500,2,500,10,000$ yr.[^9]

 

 

+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > **ID**       | > **IDn**  | > $T_{s}$ | > $V_{S30}$ | > **0.1%** | > **0.4%** | > **1%** | > **2.5%** |
+:==============:+============+===========+=============+============+============+==========+============+
| > TR 500 yr    | > ensemble | > 0.28    | > 251.4     | > 18       | > 6        | > 2      | > 1        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 500 yr    | > flexible | > 0.28    | > 251.4     | > 24       | > 6        | > 1      | > 0        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 500 yr    | > rigid    | > 0.28    | > 251.4     | > 14       | > 7        | > 3      | > 1        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > ensemble | > 0.28    | > 251.4     | > 66       | > 35       | > 19     | > 9        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > flexible | > 0.28    | > 251.4     | > 67       | > 28       | > 11     | > 3        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > rigid    | > 0.28    | > 251.4     | > 66       | > 40       | > 24     | > 13       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > ensemble | > 0.28    | > 251.4     | > 155      | > 89       | > 56     | > 30       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > flexible | > 0.28    | > 251.4     | > 143      | > 66       | > 34     | > 12       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > rigid    | > 0.28    | > 251.4     | > 163      | > 104      | > 71     | > 43       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > ensemble | > 0.28    | > 251.4     | > 142      | > 87       | > 57     | > 35       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > flexible | > 0.28    | > 251.4     | > 65       | > 27       | > 12     | > 3        |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > rigid    | > 0.28    | > 251.4     | > 193      | > 126      | > 88     | > 55       |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+

: Table 7: Mean values of $k_{\max}$ [cm/s2] for site CFD, scenario S35, under the MCE demand and return periods $T_{R} = 500,2,500,10,000$ yr.[^10]

 

## Performance-Based Seismic Coefficient $k_{h}$

+:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:+
| ![](./media/rId61.png){width="6.3in" height="4.726666666666667in"}                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                             |
| Fig. 5: Mean values of $k_{h}$ [% of PGA] for site CFD and return period $T_{R} = 500$ yr, as a function of the allowable permanent displacement relative to slope height, $D_{a}/H$ [%]. The curves represent the scenarios S135, S50, S32, S27, S35 evaluated with the `rigid`, `ensemble`, and `flexible` sets.[^11] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:+
| ![](./media/rId66.png){width="6.3in" height="4.726666666666667in"}                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                               |
| Fig. 6: Mean values of $k_{h}$ [% of PGA] for site CFD and return period $T_{R} = 2,500$ yr, as a function of the allowable permanent displacement relative to slope height, $D_{a}/H$ [%]. The curves represent the scenarios S135, S50, S32, S27, S35 evaluated with the `rigid`, `ensemble`, and `flexible` sets.[^12] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:+
| ![](./media/rId71.png){width="6.3in" height="4.726666666666667in"}                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                |
| Fig. 7: Mean values of $k_{h}$ [% of PGA] for site CFD and return period $T_{R} = 10,000$ yr, as a function of the allowable permanent displacement relative to slope height, $D_{a}/H$ [%]. The curves represent the scenarios S135, S50, S32, S27, S35 evaluated with the `rigid`, `ensemble`, and `flexible` sets.[^13] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:+
| ![](./media/rId76.png){width="6.3in" height="4.726666666666667in"}                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                               |
| Fig. 8: Mean values of $k_{h}$ [% of PGA] for site CFD under the MCE demand, as a function of the allowable permanent displacement relative to slope height, $D_{a}/H$ [%]. The curves represent the scenarios S135, S50, S32, S27, S35 evaluated with the `rigid`, `ensemble`, and `flexible` sets.[^14] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > **ID**       | > **IDn**  | > $T_{s}$ | > $V_{S30}$ | > **0.1%** | > **0.4%** | > **1%** | > **2.5%** |
+:==============:+============+===========+=============+============+============+==========+============+
| > TR 500 yr    | > ensemble | > 0.835   | > 193       | > 9.0      | > 1.6      | > 0.4    | > 0.1      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 500 yr    | > flexible | > 0.835   | > 193       | > 5.4      | > 0.3      | > 0.0    | > 0.0      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 500 yr    | > rigid    | > 0.835   | > 193       | > 11.3     | > 2.4      | > 0.6    | > 0.2      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > ensemble | > 0.835   | > 193       | > 18.1     | > 7.4      | > 3.6    | > 1.9      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > flexible | > 0.835   | > 193       | > 9.8      | > 2.1      | > 0.4    | > 0.0      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > rigid    | > 0.835   | > 193       | > 23.7     | > 10.9     | > 5.7    | > 3.1      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > ensemble | > 0.835   | > 193       | > 21.3     | > 10.3     | > 5.3    | > 2.7      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > flexible | > 0.835   | > 193       | > 11.9     | > 4.0      | > 1.2    | > 0.2      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > rigid    | > 0.835   | > 193       | > 27.5     | > 14.4     | > 8.0    | > 4.4      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > ensemble | > 0.835   | > 193       | > 19.3     | > 10.4     | > 6.1    | > 3.4      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > flexible | > 0.835   | > 193       | > 2.3      | > 0.6      | > 0.1    | > 0.0      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > rigid    | > 0.835   | > 193       | > 30.6     | > 16.9     | > 10.2   | > 5.7      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+

: Table 8: Mean values of $k_{h}$ [% of PGA] for site CFD, scenario S135, under the MCE demand and return periods $T_{R} = 500,2,500,10,000$ yr.[^15]

 

 

+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > **ID**       | > **IDn**  | > $T_{s}$ | > $V_{S30}$ | > **0.1%** | > **0.4%** | > **1%** | > **2.5%** |
+:==============:+============+===========+=============+============+============+==========+============+
| > TR 500 yr    | > ensemble | > 0.377   | > 217.5     | > 24.8     | > 7.2      | > 2.1    | > 0.4      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 500 yr    | > flexible | > 0.377   | > 217.5     | > 29.3     | > 5.3      | > 0.5    | > 0.0      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 500 yr    | > rigid    | > 0.377   | > 217.5     | > 21.8     | > 8.5      | > 3.1    | > 0.7      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > ensemble | > 0.377   | > 217.5     | > 31.3     | > 15.3     | > 7.7    | > 3.3      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > flexible | > 0.377   | > 217.5     | > 27.8     | > 10.0     | > 3.0    | > 0.3      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > rigid    | > 0.377   | > 217.5     | > 33.6     | > 18.8     | > 10.9   | > 5.4      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > ensemble | > 0.377   | > 217.5     | > 34.7     | > 19.2     | > 11.4   | > 5.8      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > flexible | > 0.377   | > 217.5     | > 28.2     | > 12.2     | > 5.5    | > 1.5      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > rigid    | > 0.377   | > 217.5     | > 39.0     | > 23.8     | > 15.4   | > 8.6      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > ensemble | > 0.377   | > 217.5     | > 27.7     | > 16.2     | > 10.3   | > 6.0      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > flexible | > 0.377   | > 217.5     | > 8.1      | > 2.7      | > 0.8    | > 0.1      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > rigid    | > 0.377   | > 217.5     | > 40.8     | > 25.3     | > 16.7   | > 9.9      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+

: Table 9: Mean values of $k_{h}$ [% of PGA] for site CFD, scenario S50, under the MCE demand and return periods $T_{R} = 500,2,500,10,000$ yr.[^16]

 

 

+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > **ID**       | > **IDn**  | > $T_{s}$ | > $V_{S30}$ | > **0.1%** | > **0.4%** | > **1%** | > **2.5%** |
+:==============:+============+===========+=============+============+============+==========+============+
| > TR 500 yr    | > ensemble | > 0.308   | > 205.6     | > 36.5     | > 14.0     | > 5.2    | > 1.2      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 500 yr    | > flexible | > 0.308   | > 205.6     | > 48.9     | > 15.1     | > 3.7    | > 0.3      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 500 yr    | > rigid    | > 0.308   | > 205.6     | > 28.2     | > 13.3     | > 6.2    | > 1.9      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > ensemble | > 0.308   | > 205.6     | > 39.4     | > 21.1     | > 11.8   | > 5.5      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > flexible | > 0.308   | > 205.6     | > 39.8     | > 16.9     | > 7.1    | > 1.7      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > rigid    | > 0.308   | > 205.6     | > 39.2     | > 23.9     | > 14.9   | > 8.0      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > ensemble | > 0.308   | > 205.6     | > 42.2     | > 24.6     | > 15.6   | > 8.7      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > flexible | > 0.308   | > 205.6     | > 37.5     | > 17.5     | > 9.0    | > 3.3      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > rigid    | > 0.308   | > 205.6     | > 45.4     | > 29.4     | > 20.1   | > 12.2     |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > ensemble | > 0.308   | > 205.6     | > 33.8     | > 20.7     | > 13.7   | > 8.3      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > flexible | > 0.308   | > 205.6     | > 13.6     | > 5.5      | > 2.2    | > 0.6      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > rigid    | > 0.308   | > 205.6     | > 47.2     | > 30.9     | > 21.4   | > 13.4     |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+

: Table 10: Mean values of $k_{h}$ [% of PGA] for site CFD, scenario S32, under the MCE demand and return periods $T_{R} = 500,2,500,10,000$ yr.[^17]

 

 

+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > **ID**       | > **IDn**  | > $T_{s}$ | > $V_{S30}$ | > **0.1%** | > **0.4%** | > **1%** | > **2.5%** |
+:==============:+============+===========+=============+============+============+==========+============+
| > TR 500 yr    | > ensemble | > 0.187   | > 310.6     | > 38.8     | > 15.0     | > 5.3    | > 1.4      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 500 yr    | > flexible | > 0.187   | > 310.6     | > 54.5     | > 17.0     | > 4.0    | > 0.3      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 500 yr    | > rigid    | > 0.187   | > 310.6     | > 28.3     | > 13.6     | > 6.2    | > 2.2      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > ensemble | > 0.187   | > 310.6     | > 47.3     | > 25.8     | > 15.1   | > 7.2      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > flexible | > 0.187   | > 310.6     | > 55.1     | > 24.7     | > 11.8   | > 3.6      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > rigid    | > 0.187   | > 310.6     | > 42.1     | > 26.5     | > 17.2   | > 9.6      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > ensemble | > 0.187   | > 310.6     | > 50.6     | > 29.6     | > 19.0   | > 10.8     |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > flexible | > 0.187   | > 310.6     | > 54.0     | > 26.0     | > 14.1   | > 6.0      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > rigid    | > 0.187   | > 310.6     | > 48.3     | > 31.9     | > 22.3   | > 14.1     |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > ensemble | > 0.187   | > 310.6     | > 40.9     | > 25.0     | > 16.6   | > 10.1     |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > flexible | > 0.187   | > 310.6     | > 28.1     | > 12.9     | > 6.5    | > 2.5      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > rigid    | > 0.187   | > 310.6     | > 49.3     | > 33.0     | > 23.4   | > 15.2     |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+

: Table 11: Mean values of $k_{h}$ [% of PGA] for site CFD, scenario S27, under the MCE demand and return periods $T_{R} = 500,2,500,10,000$ yr.[^18]

 

 

+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > **ID**       | > **IDn**  | > $T_{s}$ | > $V_{S30}$ | > **0.1%** | > **0.4%** | > **1%** | > **2.5%** |
+:==============:+============+===========+=============+============+============+==========+============+
| > TR 500 yr    | > ensemble | > 0.28    | > 251.4     | > 33.6     | > 12.0     | > 4.0    | > 1.2      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 500 yr    | > flexible | > 0.28    | > 251.4     | > 43.6     | > 11.4     | > 2.1    | > 0.1      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 500 yr    | > rigid    | > 0.28    | > 251.4     | > 26.8     | > 12.4     | > 5.3    | > 1.9      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > ensemble | > 0.28    | > 251.4     | > 38.4     | > 20.2     | > 11.0   | > 5.1      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > flexible | > 0.28    | > 251.4     | > 38.8     | > 16.1     | > 6.3    | > 1.5      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 2,500 yr  | > rigid    | > 0.28    | > 251.4     | > 38.1     | > 22.9     | > 14.2   | > 7.4      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > ensemble | > 0.28    | > 251.4     | > 42.1     | > 24.3     | > 15.2   | > 8.3      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > flexible | > 0.28    | > 251.4     | > 38.9     | > 18.1     | > 9.2    | > 3.3      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > TR 10,000 yr | > rigid    | > 0.28    | > 251.4     | > 44.3     | > 28.4     | > 19.3   | > 11.6     |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > ensemble | > 0.28    | > 251.4     | > 34.7     | > 21.2     | > 14.0   | > 8.5      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > flexible | > 0.28    | > 251.4     | > 16.0     | > 6.7      | > 2.9    | > 0.8      |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+
| > MCE          | > rigid    | > 0.28    | > 251.4     | > 47.2     | > 30.9     | > 21.4   | > 13.6     |
+----------------+------------+-----------+-------------+------------+------------+----------+------------+

: Table 12: Mean values of $k_{h}$ [% of PGA] for site CFD, scenario S35, under the MCE demand and return periods $T_{R} = 500,2,500,10,000$ yr.[^19]

 

## Newmark Permanent-Displacement Formulations

The seismic-coefficient section applies five Newmark permanent-displacement formulations: three rigid-block models, two flexible-block models and, among the latter, the BM branch selected by the tectonic control of the project. This section reproduces the published form of each formulation, including both BM branches, and states the rule that defines the active configuration. The rigid-block formulations relate the displacement to measures of the base excitation, whereas the flexible-block formulations additionally incorporate the dynamic response of the sliding mass through its fundamental period $T_{s}$ and the spectral acceleration evaluated at a period proportional to $T_{s}$.

## Rigid-Block Models

The `AM88` formulation ([Ambraseys and Menu 1988](#ref-AmbraseysMenu1988)) uses the ratio of yield acceleration to PGA, capped to preserve the logarithmic domain, $r^{\star} = \min(k_{y}/PGA,0.9999)$[^20]:

[]{#eq-newmark-am88 .anchor} $\begin{aligned}
\mu_{\ln D} & = \ln(10)\left\lbrack 0.90 + \log_{10}\left( (1 - r^{\star})^{2.53}(r^{\star})^{- 1.09} \right) \right\rbrack, \\
\sigma_{\ln D} & = 0.30\ln(10).
\end{aligned}$ (16)

The two remaining rigid-block formulations, JB07 and SR08, use the Arias intensity, which is estimated for each realization from the PGA; $I_{A}$ is expressed in m/s and PGA in units of $g$, and the estimate is applied deterministically, so that each PGA realization determines a single value of $I_{A}$ and the displacement sample propagates the PGA variability. The `JB07` formulation ([Jibson 2007](#ref-Jibson2007)) incorporates the Arias intensity and the ratio $k_{y}/PGA$:

$\begin{aligned}
\mu_{\ln D} & = \ln(10)\left\lbrack 0.561\log_{10}I_{A} - 3.833\log_{10}\left( \frac{k_{y}}{PGA} \right) - 1.474 \right\rbrack, \\
\sigma_{\ln D} & = 0.616\ln(10).
\end{aligned}$ (17)

The `SR08` formulation ([Saygili and Rathje 2008](#ref-SaygiliRathje2008)) defines $r = k_{y}/PGA$ and combines PGA and Arias intensity:

$\begin{aligned}
\mu_{\ln D} = & 2.39 - 5.24r - 18.78r^{2} + 42.01r^{3} - 29.15r^{4} \\
 & - 1.56\ln PGA + 1.38\ln I_{A}, \\
\sigma_{\ln D} = & 0.46 + 0.56r.
\end{aligned}$ (18)

The logarithmic extension of the $D_{n}(k_{y})$ relations beyond their computed support has one exception, the AM88 limit. If the sampled PGA of a realization, ${PGA}_{s}$, is smaller than the lower end of the grid, all stored points may satisfy $k_{y}/{PGA}_{s} \geq r_{\max} = 0.9999$ and form a plateau $D_{0,s}$. In that case the physical branch $0 < r < r_{\max}$ of [eq. 16](#eq-newmark-am88) is solved for $D_{a} > D_{0,s}$, instead of extrapolating the plateau or assigning $k_{\max} = 0$:

[]{#eq-kmax-am88-limit .anchor} $\mu_{\ln D}(r) = \ln D_{a} - \ln D_{0,s} + \mu_{\ln D}(r_{\max}),\quad\quad k_{\max,s} = {PGA}_{s}r.$ (19)

The random residual cancels between $D_{a}$ and $D_{0,s}$, and $d\mu_{\ln D}/dr = - 2.53/(1 - r) - 1.09/r < 0$, so the root is unique. An AM88 plateau is accepted only when the original curve is exactly constant and ${PGA}_{s}$ itself shows that the entire grid reached that limit; a flat curve from another model, or a target $D_{a} \leq D_{0,s}$, is rejected as non-identifiable support.

## Flexible-Block Models

The flexible-block formulations evaluate the spectral acceleration at a period proportional to the fundamental period $T_{s}$ of the sliding mass. The `BT07` formulation ([Bray and Travasarou 2007](#ref-BrayTravasarou2007)) employs $S_{a} = S_{a}(1.5T_{s})$ and $M_{w}$:

$\begin{aligned}
\mu_{\ln D} = & a_{0} - 2.83\ln k_{y} - 0.333(\ln k_{y})^{2} + 0.566\ln k_{y}\ln S_{a} \\
 & + 3.04\ln S_{a} - 0.244(\ln S_{a})^{2} + 1.50T_{s} + 0.278(M_{w} - 7), \\
a_{0} = & \left\{ \begin{matrix}
 - 0.22, & T_{s} < 0.05\ s, \\
 - 1.10, & T_{s} \geq 0.05\ s,
\end{matrix} \right.\  \\
\sigma_{\ln D} = & 0.66.
\end{aligned}$ (20)

The `BM17` formulation ([Bray et al. 2018](#ref-BrayEtAl2018)) represents subduction-interface motions with $S_{a} = S_{a}(1.5T_{s})$:

$\begin{aligned}
\mu_{\ln D} & = a_{0} + a_{1}\ln S_{a} - 0.225(\ln S_{a})^{2}, \\
a_{1} & = 3.060 + 0.538\ln k_{y}, \\
a_{0, <} = & - 5.864 + 0.550M_{w} - 9.421T_{s} \\
 & - 3.353\ln k_{y} - 0.390(\ln k_{y})^{2}, \\
a_{0, \geq} = & - 6.896 + 0.550M_{w} + 3.081T_{s} - 0.803T_{s}^{2} \\
 & - 3.353\ln k_{y} - 0.390(\ln k_{y})^{2}, \\
a_{0} & = \left\{ \begin{matrix}
a_{0, <}, & T_{s} < 0.1\ s, \\
a_{0, \geq}, & T_{s} \geq 0.1\ s,
\end{matrix} \right.\  \\
\sigma_{\ln D} & = 0.73.
\end{aligned}$ (21)

The `BM19` formulation ([Bray and Macedo 2019](#ref-BrayMacedo2019)) represents ordinary shallow crustal motions with $S_{a} = S_{a}(1.3T_{s})$:

$\begin{aligned}
\mu_{\ln D} & = a_{0} + \left( 2.649 + 0.344\ln k_{y} \right)\ln S_{a} - 0.090(\ln S_{a})^{2}, \\
a_{0, <} = & - 4.684 + 0.603M_{w} - 9.471T_{s} \\
 & - 2.482\ln k_{y} - 0.244(\ln k_{y})^{2}, \\
a_{0, \geq} = & - 5.981 + 0.603M_{w} + 3.223T_{s} - 0.945T_{s}^{2} \\
 & - 2.482\ln k_{y} - 0.244(\ln k_{y})^{2}, \\
a_{0} & = \left\{ \begin{matrix}
a_{0, <}, & T_{s} < 0.1\ s, \\
a_{0, \geq}, & T_{s} \geq 0.1\ s,
\end{matrix} \right.\  \\
\sigma_{\ln D} & = 0.72.
\end{aligned}$ (22)

## Ensemble

The active configuration applies five formulations: `AM88`, `JB07`, `SR08`, `BT07`, and one BM branch – `BM17` when the project declares subduction control, `BM19` when it declares crustal control; each evaluation therefore applies five formulations, never both BM branches at once. The predictors and dispersions are applied in the published form of each model, and the five formulations are combined with the equal weights and the rigid and flexible families defined in Section [1.3](#sec-coefficients).

## References

Aliberti, D., G. Biondi, E. Cascone, and S. Rampello. 2019. “Performance Indexes for Seismic Analyses of Earth Dams.” In *Earthquake Geotechnical Engineering for Protection and Development of Environment and Constructions*, edited by F. Silvestri and N. Moraci. Associazione Geotecnica Italiana.

Ambraseys, N. N., and J. M. Menu. 1988. “Earthquake-Induced Ground Displacements.” *Earthquake Engineering & Structural Dynamics* 16 (7): 985–1006. <https://doi.org/10.1002/eqe.4290160704>.

Anderson, Donald G., Geoffrey R. Martin, I. P. Lam, and John N. Wang. 2008. *Seismic Analysis and Design of Retaining Walls, Buried Structures, Slopes, and Embankments*. NCHRP Report No. 611. Transportation Research Board. <https://www.ce.memphis.edu/7137/PDFs/Seismic%20Manual/nchrp_rpt_611.pdf>.

Australian National Committee on Large Dams. 2012. *Guidelines on Tailings Dams: Planning, Design, Construction, Operation and Closure*. Australian National Committee on Large Dams.

Baker, Jack W., and Nirmal Jayaram. 2008. “Correlation of Spectral Acceleration Values from NGA Ground Motion Models.” *Earthquake Spectra* 24 (1): 299–317. <https://doi.org/10.1193/1.2857544>.

Bray, J. D., and Thaleia Travasarou. 2007. “Simplified Procedure for Estimating Earthquake-Induced Deviatoric Slope Displacements.” *Journal of Geotechnical and Geoenvironmental Engineering* 133 (4): 381–92. <https://doi.org/10.1061/(ASCE)1090-0241(2007)133:4(381)>.

Bray, Jonathan D., and Jorge Macedo. 2019. “Procedure for Estimating Shear-Induced Seismic Slope Displacement for Shallow Crustal Earthquakes.” *Journal of Geotechnical and Geoenvironmental Engineering* 145 (12): 04019106. <https://doi.org/10.1061/(ASCE)GT.1943-5606.0002143>.

Bray, Jonathan D., Jorge Macedo, and Thaleia Travasarou. 2018. “Simplified Procedure for Estimating Seismic Slope Displacements for Subduction Zone Earthquakes.” *Journal of Geotechnical and Geoenvironmental Engineering* 144 (3): 04017124. <https://doi.org/10.1061/(ASCE)GT.1943-5606.0001833>.

Bray, Jonathan D., and Thaleia Travasarou. 2009. “Pseudostatic Coefficient for Use in Simplified Seismic Slope Stability Evaluation.” *Journal of Geotechnical and Geoenvironmental Engineering* 135 (9): 1336–40. <https://doi.org/10.1061/(ASCE)GT.1943-5606.0000012>.

Dakoulas, Panos, and George Gazetas. 1985. “A Class of Inhomogeneous Shear Models for Seismic Response of Dams and Embankments.” *International Journal of Soil Dynamics and Earthquake Engineering* 4 (4): 166–82. <https://doi.org/10.1016/0261-7277(85)90037-3>.

European Committee for Standardization. 2004. *Eurocode 8: Design of Structures for Earthquake Resistance – Part 5: Foundations, Retaining Structures and Geotechnical Aspects*. European Standard EN 1998-5. European Committee for Standardization.

Federal Emergency Management Agency. 2005. *Federal Guidelines for Dam Safety: Earthquake Analyses and Design of Dams*. P-65. Federal Emergency Management Agency.

Hardin, Bobby O., and William L. Black. 1968. “Vibration Modulus of Normally Consolidated Clay.” *Journal of the Soil Mechanics and Foundations Division* 94 (2): 353–69. <https://doi.org/10.1061/JSFEAQ.0001100>.

Hardin, Bobby O., and Vincent P. Drnevich. 1972. “Shear Modulus and Damping in Soils: Measurement and Parameter Effects.” *Journal of the Soil Mechanics and Foundations Division* 98 (6): 603–24. <https://doi.org/10.1061/JSFEAQ.0001756>.

Hashash, Youssef M. A., Okan Ilhan, Joseph A. Harmon, et al. 2020. “Nonlinear Site Amplification Model for Ergodic Seismic Hazard Analysis in Central and Eastern North America.” *Earthquake Spectra* 36 (1): 69–86. <https://doi.org/10.1177/8755293019878193>.

International Commission on Large Dams. 2016. *Selecting Seismic Parameters for Large Dams – Guidelines*. Bulletin No. 148. International Commission on Large Dams.

Ishihara, Kenji. 1996. *Soil Behaviour in Earthquake Geotechnics*. Clarendon Press; Oxford University Press. <https://doi.org/10.1093/oso/9780198562245.001.0001>.

Jibson, R. W. 2007. “Regression Models for Estimating Coseismic Landslide Displacement.” *Engineering Geology* 91 (2–4): 209–18. <https://doi.org/10.1016/j.enggeo.2007.01.013>.

Macedo, Jorge, Jonathan D. Bray, Norman A. Abrahamson, and Thaleia Travasarou. 2018. “Performance-Based Probabilistic Seismic Slope Displacement Procedure.” *Earthquake Spectra* 34 (2): 673–95. <https://doi.org/10.1193/122516EQS251M>.

Makdisi, Faiz I., and H. Bolton Seed. 1978. “Simplified Procedure for Estimating Dam and Embankment Earthquake-Induced Deformations.” *Journal of the Geotechnical Engineering Division* 104 (GT7): 849–67. <https://doi.org/10.1061/AJGEB6.0000668>.

Newmark, Nathan M. 1965. “Effects of Earthquakes on Dams and Embankments.” *Géotechnique* 15 (2): 139–60. <https://doi.org/10.1680/geot.1965.15.2.139>.

Saygili, G., and E. M. Rathje. 2008. “Empirical Predictive Models for Earthquake-Induced Sliding Displacements of Slopes.” *Journal of Geotechnical and Geoenvironmental Engineering* 134 (6): 790–803.

Shibata, Toru, and Dojoko S. Soelarno. 1975. “Stress-Strain Characteristics of Sands Under Cyclic Loading.” *Proceedings of the Japan Society of Civil Engineers* 1975 (239): 57–65. <https://doi.org/10.2208/jscej1969.1975.57>.

Stewart, Jonathan P., Grace A. Parker, Gail M. Atkinson, David M. Boore, Youssef M. A. Hashash, and Walter J. Silva. 2020. “Ergodic Site Amplification Model for Central and Eastern North America.” *Earthquake Spectra* 36 (1): 42–68. <https://doi.org/10.1177/8755293019878185>.

U.S. Army Corps of Engineers. 1995. *Earthquake Design and Evaluation for Civil Works Projects*. Engineer Regulation ER 1110-2-1806. U.S. Army Corps of Engineers. <https://www.publications.usace.army.mil/Portals/76/Publications/EngineerRegulations/ER_1110-2-1806.pdf>.

U.S. Army Corps of Engineers. 2003. *Slope Stability*. Engineer Manual EM 1110-2-1902. U.S. Army Corps of Engineers. <https://www.publications.usace.army.mil/Portals/76/Publications/EngineerManuals/EM_1110-2-1902.pdf>.

U.S. Army Corps of Engineers. 2005. *Stability of Concrete Structures*. Engineer Manual EM 1110-2-2100. U.S. Army Corps of Engineers. <https://www.publications.usace.army.mil/portals/76/publications/engineermanuals/em_1110-2-2100.pdf>.

Verri Kozlowski, Alejandro. 2026. “Probabilistic Estimation of Newmark Displacements and Seismic Coefficients Under Hazard Uncertainty.” Unpublished manuscript. In press.

[^1]: `IDm` identifies the material scenario and `USCS` the classification of the slope materials. $H_{s}$ is the slope height and $b$ the berm width, both in m; $s$ is the slope ratio ($\tan\beta = 1/s$) and $\lambda_{o}$ the truncation ratio, both dimensionless; $G_{o}$ is the shear modulus of the profile at $z/H_{s} = 1$, in MPa, and $m_{o}$ the exponent of its power law, dimensionless; $a_{1}$ is the first modal root, dimensionless; $V_{S}^{o}$ is the basal shear-wave velocity and $V_{S30}$ the travel-time-averaged shear-wave velocity in the uppermost 30 m, both in m/s.

[^2]: Color identifies the scenario and line pattern identifies the set: solid for `rigid`, short dashes for `ensemble`, and long dashes for `flexible`. The shaded bands are delimited by the damage thresholds $D_{a}/H = 0.1,0.4,1.0,2.5$ %.

[^3]: Color identifies the scenario and line pattern identifies the set: solid for `rigid`, short dashes for `ensemble`, and long dashes for `flexible`. The shaded bands are delimited by the damage thresholds $D_{a}/H = 0.1,0.4,1.0,2.5$ %.

[^4]: Color identifies the scenario and line pattern identifies the set: solid for `rigid`, short dashes for `ensemble`, and long dashes for `flexible`. The shaded bands are delimited by the damage thresholds $D_{a}/H = 0.1,0.4,1.0,2.5$ %.

[^5]: Color identifies the scenario and line pattern identifies the set: solid for `rigid`, short dashes for `ensemble`, and long dashes for `flexible`. The shaded bands are delimited by the damage thresholds $D_{a}/H = 0.1,0.4,1.0,2.5$ %.

[^6]: `ID` identifies the seismic demand and `IDn` the model set (`rigid`, `ensemble`, or `flexible`). $T_{s}$ is the fundamental period of the slope [s] and $V_{S30}$ the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the arithmetic mean at each allowable permanent displacement relative to slope height, $D_{a}/H$ [%]. The fractiles associated with the exceedance target $p_{e}$ are defined in the seismic-coefficient section.

[^7]: `ID` identifies the seismic demand and `IDn` the model set (`rigid`, `ensemble`, or `flexible`). $T_{s}$ is the fundamental period of the slope [s] and $V_{S30}$ the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the arithmetic mean at each allowable permanent displacement relative to slope height, $D_{a}/H$ [%]. The fractiles associated with the exceedance target $p_{e}$ are defined in the seismic-coefficient section.

[^8]: `ID` identifies the seismic demand and `IDn` the model set (`rigid`, `ensemble`, or `flexible`). $T_{s}$ is the fundamental period of the slope [s] and $V_{S30}$ the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the arithmetic mean at each allowable permanent displacement relative to slope height, $D_{a}/H$ [%]. The fractiles associated with the exceedance target $p_{e}$ are defined in the seismic-coefficient section.

[^9]: `ID` identifies the seismic demand and `IDn` the model set (`rigid`, `ensemble`, or `flexible`). $T_{s}$ is the fundamental period of the slope [s] and $V_{S30}$ the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the arithmetic mean at each allowable permanent displacement relative to slope height, $D_{a}/H$ [%]. The fractiles associated with the exceedance target $p_{e}$ are defined in the seismic-coefficient section.

[^10]: `ID` identifies the seismic demand and `IDn` the model set (`rigid`, `ensemble`, or `flexible`). $T_{s}$ is the fundamental period of the slope [s] and $V_{S30}$ the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the arithmetic mean at each allowable permanent displacement relative to slope height, $D_{a}/H$ [%]. The fractiles associated with the exceedance target $p_{e}$ are defined in the seismic-coefficient section.

[^11]: The coefficient is expressed as $100\, k_{\max}/PGA(V_{S30})$. Color identifies the scenario and line pattern identifies the set: solid for `rigid`, short dashes for `ensemble`, and long dashes for `flexible`. The shaded bands are delimited by the damage thresholds $D_{a}/H = 0.1,0.4,1.0,2.5$ %.

[^12]: The coefficient is expressed as $100\, k_{\max}/PGA(V_{S30})$. Color identifies the scenario and line pattern identifies the set: solid for `rigid`, short dashes for `ensemble`, and long dashes for `flexible`. The shaded bands are delimited by the damage thresholds $D_{a}/H = 0.1,0.4,1.0,2.5$ %.

[^13]: The coefficient is expressed as $100\, k_{\max}/PGA(V_{S30})$. Color identifies the scenario and line pattern identifies the set: solid for `rigid`, short dashes for `ensemble`, and long dashes for `flexible`. The shaded bands are delimited by the damage thresholds $D_{a}/H = 0.1,0.4,1.0,2.5$ %.

[^14]: The coefficient is expressed as $100\, k_{\max}/PGA(V_{S30})$. Color identifies the scenario and line pattern identifies the set: solid for `rigid`, short dashes for `ensemble`, and long dashes for `flexible`. The shaded bands are delimited by the damage thresholds $D_{a}/H = 0.1,0.4,1.0,2.5$ %.

[^15]: `ID` identifies the seismic demand and `IDn` the model set (`rigid`, `ensemble`, or `flexible`). $T_{s}$ is the fundamental period of the slope [s] and $V_{S30}$ the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the mean estimate at each allowable permanent displacement relative to slope height, $D_{a}/H$ [%], expressed as $100,k_{\max}/PGA(V_{S30})$.

[^16]: `ID` identifies the seismic demand and `IDn` the model set (`rigid`, `ensemble`, or `flexible`). $T_{s}$ is the fundamental period of the slope [s] and $V_{S30}$ the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the mean estimate at each allowable permanent displacement relative to slope height, $D_{a}/H$ [%], expressed as $100,k_{\max}/PGA(V_{S30})$.

[^17]: `ID` identifies the seismic demand and `IDn` the model set (`rigid`, `ensemble`, or `flexible`). $T_{s}$ is the fundamental period of the slope [s] and $V_{S30}$ the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the mean estimate at each allowable permanent displacement relative to slope height, $D_{a}/H$ [%], expressed as $100,k_{\max}/PGA(V_{S30})$.

[^18]: `ID` identifies the seismic demand and `IDn` the model set (`rigid`, `ensemble`, or `flexible`). $T_{s}$ is the fundamental period of the slope [s] and $V_{S30}$ the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the mean estimate at each allowable permanent displacement relative to slope height, $D_{a}/H$ [%], expressed as $100,k_{\max}/PGA(V_{S30})$.

[^19]: `ID` identifies the seismic demand and `IDn` the model set (`rigid`, `ensemble`, or `flexible`). $T_{s}$ is the fundamental period of the slope [s] and $V_{S30}$ the shear-wave velocity of the evaluated condition [m/s]. The coefficient columns report the mean estimate at each allowable permanent displacement relative to slope height, $D_{a}/H$ [%], expressed as $100,k_{\max}/PGA(V_{S30})$.

[^20]: The numerical support of $k_{y}$ corresponds to the interval defined in Section [1.3](#sec-coefficients); when a complete AM88 realization reaches the limit $r^{\star} = 0.9999$, its inversion retains the sampled PGA and recovers the physical branch according to [eq. 19](#eq-kmax-am88-limit).
