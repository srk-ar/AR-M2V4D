The seismic-coefficient chapter applies five Newmark permanent-displacement formulations: three rigid-block models, two flexible-block models and, among the latter, the BM branch selected by the tectonic control of the project. This appendix reproduces the published form of each formulation, including both BM branches, and states the rule that defines the active configuration. The rigid-block formulations relate the displacement to measures of the base excitation, whereas the flexible-block formulations additionally incorporate the dynamic response of the sliding mass through its fundamental period $T_s$ and the spectral acceleration evaluated at a period proportional to $T_s$.

## Rigid-Block Models {#sec-newmark-rigid}

The `AM88` formulation [@AmbraseysMenu1988] uses the ratio of yield acceleration to PGA, capped to preserve the logarithmic domain, $r^\star=\min (k_y/\mathrm{PGA},0.9999)$^[The numerical support of $k_y$ corresponds to the interval defined in Chapter [-@sec-coefficients]; when a complete AM88 realization reaches the limit $r^\star=0.9999$, its inversion retains the sampled PGA and recovers the physical branch according to @eq-kmax-am88-limit.]:

$$
\begin{aligned} \mu_{\ln D} &=\ln (10)\left[0.90+\log_{10}\!\left((1-r^\star)^{2.53} (r^\star)^{-1.09}\right)\right],\\ \sigma_{\ln D}&=0.30\ln (10). \end{aligned}
$${#eq-newmark-am88}

The two remaining rigid-block formulations, JB07 and SR08, use the Arias intensity, which is estimated for each realization from the PGA [@Verri2023a]:

$$
I_A=\exp(2.6109)\,\mathrm{PGA}^{1.9228}.
$${#eq-newmark-arias}

where $I_A$ is expressed in m/s and PGA in units of $g$. The relation is the median of the rock group of the source, without its corrections for the other site groups, and it is applied to the PGA of the site condition of each scenario deterministically, without its dispersion, so that each PGA realization determines a single value of $I_A$ and the displacement sample propagates the PGA variability. The `JB07` formulation [@Jibson2007] incorporates the Arias intensity and the ratio $k_y/\mathrm{PGA}$:

$$
\begin{aligned} \mu_{\ln D} &=\ln (10)\left[0.561\log_{10}I_A -3.833\log_{10}\!\left(\frac{k_y}{\mathrm{PGA}}\right)-1.474\right],\\ \sigma_{\ln D}&=0.616\ln (10). \end{aligned}
$${#eq-newmark-jb07}

The `SR08` formulation [@SaygiliRathje2008] defines $r=k_y/\mathrm{PGA}$ and combines PGA and Arias intensity:

$$
\begin{aligned} \mu_{\ln D} ={}&2.39-5.24r-18.78r^2+42.01r^3-29.15r^4\\ &-1.56\ln\mathrm{PGA}+1.38\ln I_A,\\ \sigma_{\ln D}={}&0.46+0.56r. \end{aligned}
$${#eq-newmark-sr08}

Beyond the computed support, the inversion of AM88 has a rule of its own, the AM88 limit. If the sampled PGA of a realization, $\mathrm{PGA}_s$, is smaller than the lower end of the grid, all stored points may satisfy $k_y/\mathrm{PGA}_s\geq r_{\max}=0.9999$ and form a plateau $D_{0,s}$. In that case the physical branch $0<r<r_{\max}$ of @eq-newmark-am88 is solved for $D_a>D_{0,s}$, instead of extrapolating the plateau or assigning $k_{\max}=0$:

$$
\mu_{\ln D}(r)
=\ln D_a-\ln D_{0,s}+\mu_{\ln D}(r_{\max}),
\qquad
k_{\max,s}=\mathrm{PGA}_s r .
$${#eq-kmax-am88-limit}

The random residual cancels between $D_a$ and $D_{0,s}$, and $\mathrm{d}\mu_{\ln D}/\mathrm{d}r=-2.53/(1-r)-1.09/r<0$, so the root is unique. An AM88 plateau is accepted only when the original curve is exactly constant and $\mathrm{PGA}_s$ itself shows that the entire grid reached that limit; a target $D_a\leq D_{0,s}$ is rejected as non-identifiable support, and so is a flat curve of another model when $D_a$ does not exceed its constant value; a flat curve of another model gives $k_{\max}=0$ when $D_a$ exceeds that value or when the curve lies below the numerical floor of $10^{-4}$ cm.

## Flexible-Block Models {#sec-newmark-flexible}

The flexible-block formulations evaluate the spectral acceleration at a period proportional to the fundamental period $T_s$ of the sliding mass. The `BT07` formulation [@BrayTravasarou2007] employs $S_a=S_a (1.5T_s)$ and $M_w$:

$$
\begin{aligned} \mu_{\ln D}={}&a_0-2.83\ln k_y-0.333 (\ln k_y)^2 +0.566\ln k_y\ln S_a\\ &+3.04\ln S_a-0.244 (\ln S_a)^2 +1.50T_s+0.278 (M_w-7),\\ a_0={}& \begin{cases} -0.22, & T_s<0.05\ \mathrm{s},\\ -1.10, & T_s\geq0.05\ \mathrm{s}, \end{cases}\\ \sigma_{\ln D}={}&0.66. \end{aligned}
$${#eq-newmark-bt07}

The `BM17` formulation [@BrayEtAl2018] represents subduction-interface motions with $S_a=S_a (1.5T_s)$:

$$
\begin{aligned} \mu_{\ln D}&=a_0+\left(3.060+0.538\ln k_y\right)\ln S_a-0.225 (\ln S_a)^2,\\ a_{0,<}={}&-5.864+0.550M_w-9.421T_s\\ &-3.353\ln k_y-0.390 (\ln k_y)^2,\\ a_{0,\geq}={}&-6.896+0.550M_w+3.081T_s-0.803T_s^2\\ &-3.353\ln k_y-0.390 (\ln k_y)^2,\\ a_0&= \begin{cases} a_{0,<}, & T_s<0.1\ \mathrm{s},\\ a_{0,\geq}, & T_s\geq0.1\ \mathrm{s}, \end{cases}\\ \sigma_{\ln D}&=0.73. \end{aligned}
$${#eq-newmark-bm17}

The `BM19` formulation [@BrayMacedo2019] represents ordinary shallow crustal motions with $S_a=S_a (1.3T_s)$:

$$
\begin{aligned} \mu_{\ln D}&=a_0+\left(2.649+0.344\ln k_y\right)\ln S_a -0.090 (\ln S_a)^2,\\ a_{0,<}={}&-4.684+0.603M_w-9.471T_s\\ &-2.482\ln k_y-0.244 (\ln k_y)^2,\\ a_{0,\geq}={}&-5.981+0.603M_w+3.223T_s-0.945T_s^2\\ &-2.482\ln k_y-0.244 (\ln k_y)^2,\\ a_0&= \begin{cases} a_{0,<}, & T_s<0.1\ \mathrm{s},\\ a_{0,\geq}, & T_s\geq0.1\ \mathrm{s}, \end{cases}\\ \sigma_{\ln D}&=0.72. \end{aligned}
$${#eq-newmark-bm19}

## Ensemble {#sec-newmark-ensemble}

The active configuration applies five formulations: `AM88`, `JB07`, `SR08`, `BT07`, and one BM branch -- `BM17` when the project declares subduction control, `BM19` when it declares crustal control; each evaluation therefore applies five formulations, never both BM branches at once. The predictors and dispersions are applied in the published form of each model, and the five formulations are combined with the equal weights and the rigid and flexible families defined in Chapter [-@sec-coefficients].
