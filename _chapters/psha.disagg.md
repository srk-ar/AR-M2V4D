The PSHA aggregates the contributions of all plausible earthquake scenarios in the total exceedance rate, obscuring the specific combinations of magnitude ($M$), source-to-site distance ($R$), and ground-motion residual ($\varepsilon$) that control site hazard. **Hazard disaggregation** quantifies the relative contribution of each scenario class, binned by magnitude $m_k$, distance $r_j$, and residual $\varepsilon_\ell$, to the annual frequency of exceedance at a specified ground-motion threshold $i^*$ [@Bazzurro1999].

Disaggregation is performed at a target hazard level, defined by an annual exceedance probability or return period. This produces conditional probability distributions over scenario bins and identifies controlling scenario parameters responsible for site hazard [@Kramer1997]. The joint exceedance rate for scenario $(m_k, r_j, \varepsilon_\ell)$ from source $s$ is

$$
\Delta\lambda_{I}(i^{*},m_k,r_j,\varepsilon)^{(s)} =
\mathbf 1_{\{\varepsilon\ge\varepsilon^{*}(m_k,r_j)\}}
\,
\varphi(\varepsilon)\,
f_{M,s}(m_k)\,
f_{\mathbf R\mid M,s}(r_j\mid m_k)\,
\nu_{0}^{(s)},
$${#eq-disagg-rate}

where $\varphi$ is the standard normal probability density function and $\mathbf 1_{{\cdot}}$ is the indicator function; the ground-motion exceedance probability and the total annual exceedance rate that enter the formulation are those defined in the hazard analysis (see [-@eq-hazard-integral], [-@eq-epsilon-star]). Integration over $\varepsilon$ yields the two-dimensional ($M$-$R$) formulation. Partitioning parameter space into magnitude bins $m_k$, distance bins $r_j$, and residual bins $\varepsilon_\ell$, the contribution from bin $(k,j,\ell)$ is

$$
\lambda_{k,j,\ell}(i^{*})=
\sum_{s=1}^{N_{S}}
\int_{m_k}
\int_{r_j}
\int_{\varepsilon_\ell}
\Delta\lambda_{I}(i^{*},m_k,r_j,\varepsilon)^{(s)}
d\varepsilon\,dr\,dm
$${#eq-disagg-bin}

Hazard disaggregation applies Bayes' theorem to the joint distribution of scenario parameters and ground-motion exceedance: the conditional probability that exceedance of $i^*$ is produced by this bin is

$$
P[M=m_k,R=r_j,\varepsilon=\varepsilon_\ell\mid I> i^{*}]
= \theta_{k,j,\ell}
=
\frac{\lambda_{k,j,\ell}(i^{*})}{\lambda_{I}(i^{*})}
$${#eq-disagg-prob}

and the marginal probabilities are obtained by double summation over the other indices, over distance and residual for the magnitude,

$$
P\left[M \in m_k\mid I> i^{*}\right] = \sum_{j}\sum_{\ell}\theta_{k,j,\ell}
$${#eq-disagg-marginal-M}

over magnitude and residual for the distance,

$$
P\left[R \in r_j\mid I> i^{*}\right] = \sum_{k}\sum_{\ell}\theta_{k,j,\ell}
$${#eq-disagg-marginal-R}

and over magnitude and distance for the residual, whose marginal distribution quantifies the contribution of ground-motion residual bins to the exceedance:

$$
P\left[\varepsilon \in \varepsilon_\ell\mid I> i^{*}\right] = \sum_{k}\sum_{j}\theta_{k,j,\ell}
$${#eq-disagg-marginal-eps}

The **modal scenario** is the $(k,j,\ell)$ bin for which $\theta_{k,j,\ell}$ of [-@eq-disagg-prob] attains its maximum. The **mean scenario** is the average magnitude--distance pair of the conditional distribution, weighted by those contributions.

In this report, the OpenQuake disaggregation outputs are presented as magnitude-distance (`Mag_Dist`) matrices. The calculation uses magnitude bins of 0.1 $M_w$, distance bins of 10 km, and the intensity measures PGA, $S_a(0.10\,\mathrm{s})$, $S_a(0.20\,\mathrm{s})$, $S_a(0.50\,\mathrm{s})$, and $S_a(1.00\,\mathrm{s})$. The reported heatmaps and modal table therefore summarize the two-dimensional $M$-$R$ contribution surface for each selected return period and oscillator period. Disaggregation provides a data-driven basis for scenario selection in engineering analysis. The *modal scenario* and the highest-probability bins identified through disaggregation correspond to the earthquake characteristics most responsible for exceedance at the design ground-motion level.
