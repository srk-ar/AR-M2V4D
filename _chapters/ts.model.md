Flexible sliding-block models account for the dynamic response of the potential sliding mass through spectral acceleration evaluated at a period proportional to its fundamental period, so each slope geometry--material combination needs $T_s$, which is derived from the geometry and the depth-dependent small-strain shear stiffness, described by $G_o$, $m_o$, and $V_S^o$; the mean values of $T_s$ and $V_{S30}$ provide the dynamic inputs to the permanent-displacement models. The fundamental period of the potential sliding mass is estimated from the first mode of the truncated inhomogeneous shear-beam model of Dakoulas and Gazetas [-@DakoulasGazetas1985Inhomogeneous] as

$$
T_s=\frac{4\pi H}{a_1(2-m_o)V_S^o},
$${#eq-slope-period}

where $H=H_s/(1-\lambda_o)$ is the height of the truncated wedge from the apex of the extended slopes to the base, $H_s$ is the slope height, $V_S^o$ is the basal shear-wave velocity associated with $G_o$, $m_o$ is the inhomogeneity factor governing the shear-modulus profile, and $a_1$ is the first modal root of the characteristic equation. The modal root depends jointly on $m_o$ and the truncation ratio $\lambda_o$, which geometric similarity gives as

$$
\lambda_o=\frac{b}{b_{\max}},
$${#eq-slope-truncation}

where $b$ and $b_{\max}$ are the berm and base widths, respectively. The equivalent truncated section in the Dakoulas--Gazetas model [-@DakoulasGazetas1985Inhomogeneous] is specified by the height $H_s$, slope ratio $s$, and truncation ratio $\lambda_o$; with $\tan\beta=1/s$, where $\beta$ is the slope angle, the berm width is

$$
b=\frac{2H_s s}{1/\lambda_o-1}.
$${#eq-slope-berm-width}

and the base width is

$$
b_{\max}=b+2H_s s.
$${#eq-slope-base-width}

For each profile realization, the basal shear-wave velocity is

$$
V_S^o=\left(\frac{gG_o}{\gamma_{\mathrm{sat}}^{(k_{\mathrm{b}})}}\right)^{1/2},
$${#eq-slope-basal-velocity}

where $G_o$ is the fitted small-strain shear modulus at the base, $g$ is the acceleration of gravity, and $\gamma_{\mathrm{sat}}^{(k_{\mathrm{b}})}$ is the saturated unit weight of the basal layer, whose index is $k_{\mathrm{b}}$; all quantities are expressed in consistent units. The depth dependence of small-strain shear stiffness is represented for each realization by the power-law profile

$$
G(z)=G_o\left(\frac{z}{H_s}\right)^{m_o},
$${#eq-slope-profile}

where $z$ is depth below the crest, $G_o$ is the fitted shear modulus at the base ($z/H_s=1$), and $m_o$ is obtained from a logarithmic fit to the layer moduli $G_m^{(k)}$; the characteristic equation corresponds to the power law with depth measured from the apex of the extended slopes and normalized by $H$ [-@DakoulasGazetas1985Inhomogeneous], so evaluating $a_1$ with the exponent fitted from the crest is an approximation. The layer moduli come from the soil classification: the USCS classification assigned to layer $k$ selects its soil family and the associated set of $J^{(k)}$ small-strain shear-modulus correlations compiled by Ishihara [-@Ishihara1996], and the layer modulus is taken as their arithmetic mean,

$$
G_m^{(k)}=\frac{1}{J^{(k)}}\sum_{j=1}^{J^{(k)}}
A^{(j)}F_e^{(k,j)}
\left[\mathrm{OCR}^{(k)}\right]^{m_1^{(k)}}
p_{\mathrm{ref}}^{n^{(j)}}
\left(\frac{p_m^{(k)}}{p_{\mathrm{ref}}}\right)^{n^{(j)}}.
$${#eq-slope-modulus}

Here $A^{(j)}$ and $n^{(j)}$ are tabulated correlation parameters, $F_e^{(k,j)}$ is the void-ratio function, $m_1^{(k)}$ is the overconsolidation exponent, $p_m^{(k)}$ is the layer-averaged effective octahedral normal stress, and $p_{\mathrm{ref}}=100$ kPa is the reference pressure. Under at-rest conditions, the layer-averaged effective octahedral normal stress $p_m^{(k)}$ [-@HardinBlack1968; -@HardinDrnevich1972] is

$$
p_m^{(k)}=\frac{1+2K_0}{3}
\left(\sum_{\ell=1}^{k-1}\gamma^{(\ell)}h^{(\ell)}
+\frac{\gamma^{(k)}h^{(k)}}{2}\right),
$${#eq-slope-mean-pressure}

where $K_0$ is the at-rest lateral earth pressure coefficient, $\gamma^{(\ell)}$ and $h^{(\ell)}$ are the unit weight adopted for the groundwater condition and the thickness of layer $\ell$, and $\ell<k$ denotes the overlying layers. The layer overconsolidation ratio is $\mathrm{OCR}^{(k)}=\max[(p_m^{(k)}+\mathrm{POP})/p_m^{(k)},1]$, where $\mathrm{POP}$ is the preconsolidation pressure; for fine-grained soils, $m_1^{(k)}=f_{\mathrm{IP}}(\mathrm{IP}^{(k)})$, whereas for sands and gravels $m_1^{(k)}=0$ and the OCR multiplier is therefore unity. The void ratio $e_0^{(k)}$ enters all three soil families through $F_e^{(k,j)}$, which the correlations compiled by Ishihara [-@Ishihara1996] define in terms of $e_0^{(k)}$ and $C_e^{(j)}$, with the index $j_{\mathrm{SS75}}$ identifying the Shibata--Soelarno formulation [-@ShibataSoelarno1975]:

$$
F_e^{(k,j)}=
\begin{cases}
C_e^{(j)}-\dfrac{e_0^{(k)}}{1+e_0^{(k)}}, & j=j_{\mathrm{SS75}},\\[6pt]
\dfrac{\left(C_e^{(j)}-e_0^{(k)}\right)^2}{1+e_0^{(k)}}, & j\ne j_{\mathrm{SS75}}.
\end{cases}
$${#eq-slope-void-factor}

The shear-wave velocity of layer $k$ then follows from

$$
V_S^{(k)}=\left(\frac{gG_m^{(k)}}{\gamma_{\mathrm{sat}}^{(k)}}\right)^{1/2},
$${#eq-slope-layer-velocity}

where $G_m^{(k)}$ is the adopted layer modulus and $\gamma_{\mathrm{sat}}^{(k)}$ is its saturated unit weight; all quantities are expressed in consistent units.

```{r}
#| include: false
CAP <- readCaption("tbl.SiteGo")
SiteGo.headers <- c("Formulation", "Family", "Reference material", "Author")
SiteGo.groups <- c(Sands = "Sands", Fines = "Fines", Gravels = "Gravels")
```

{{< include /_tbl/SiteGo.qmd >}}

For each geometry--material combination, the analysis generates $N$ synthetic realizations of the layered profile, and each of $G_o$, $m_o$, $V_S^o$, and $V_{S30}$ is summarized by its mean and selected marginal fractiles; for the mean and for each reported fractile, $a_1$ and $T_s$ are evaluated from the corresponding $m_o$ and $V_S^o$ values, and the mean estimates provide the dynamic properties used in the displacement analysis. $V_{S30}$ is the travel-time-averaged shear-wave velocity in the uppermost 30 m:

$$
V_{S30}=\frac{30}{
\displaystyle\sum_i\frac{h_{30}^{(i)}}{V_S^{(i)}}
+\dfrac{\max(30-H_s,0)}{V_{\mathrm{ref}}}}.
$${#eq-slope-vs30}

In this expression, $h_{30}^{(i)}$ is the portion of layer $i$ within the uppermost 30 m and $V_S^{(i)}$ is its shear-wave velocity; when $H_s<30$ m, the reference velocity $V_{\mathrm{ref}}$ is assigned to the remaining thickness.
