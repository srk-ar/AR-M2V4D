Each active formulation estimates the Newmark permanent displacement [-@Newmark1965] of the sliding mass from the yield acceleration and the intensity measures of its regression, and all of them express the positive displacement $D_n$, in centimeters, through

$$
D_n=\exp\!\left(\mu_{\ln D}+\epsilon\sigma_{\ln D}\right), \qquad \epsilon\sim\mathcal N (0,1),
$${#eq-newmark-lognormal}

where $\mu_{\ln D}$ and $\sigma_{\ln D}$ are the mean and standard deviation of $\ln D_n$ defined by each model, and $\epsilon$ is a standard-normal residual. Some source formulations contain a discrete branch of zero or negligible displacement; the implemented evaluation uses exclusively the positive lognormal branch. In every formulation, $k_y$, PGA, and $S_a$ are expressed in units of $g$ -- the acceleration of gravity -- $I_A$ in m/s, and $T_s$ in seconds; the Arias intensity is derived from the PGA of each realization according to [-@eq-newmark-arias], and the reference magnitude assigned to each seismic demand is applied to its geometry--material combinations. The published form of each formulation is reproduced in Appendix [-@sec-newmark-appendix]. The performance-based seismic coefficient is defined by

$$
k_{\max} (p_e\mid D_a)
=\inf\left\{k_y:P[D_n (k_y)>D_a]\leq p_e\right\}.
$${#eq-kmax-criterion}

where $p_e$ is the target probability that $D_n$ exceeds $D_a$: $k_{\max}$ is the smallest $k_y$ for which the probability of exceeding the allowable displacement is at most $p_e$. The normalized coefficient, reported as a percentage of the PGA [% of PGA], is calculated using the site-condition PGA transformed to the $V_{S30}$ of the geometry--material combination evaluated for each demand:

$$
k_h=100\,\frac{k_{\max}}{\mathrm{PGA} (V_{S30})}.
$${#eq-kh-normalization}

$k_{\max}$ is expressed in units of $g$ and $k_h$ as a percentage of the PGA of the corresponding site condition. These two quantities express the displacement criterion as the horizontal action of the pseudostatic verification.
