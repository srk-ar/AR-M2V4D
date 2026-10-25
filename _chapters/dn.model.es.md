Cada formulación activa estima el desplazamiento permanente de Newmark [-@Newmark1965] de la masa deslizante a partir de la aceleración de fluencia y de las medidas de intensidad de su regresión, y todas expresan el desplazamiento positivo $D_n$, en centímetros, mediante

$$
D_n=\exp\!\left(\mu_{\ln D}+\epsilon\sigma_{\ln D}\right), \qquad \epsilon\sim\mathcal N (0,1),
$${#eq-newmark-lognormal}

donde $\mu_{\ln D}$ y $\sigma_{\ln D}$ son la media y la desviación estándar de $\ln D_n$ definidas por cada modelo, y $\epsilon$ es un residuo normal estándar. Algunas formulaciones fuente contienen una rama discreta de desplazamiento nulo o despreciable; la evaluación implementada utiliza exclusivamente la rama lognormal positiva, sin truncarla en el umbral de desplazamiento despreciable, de modo que, a medidas de intensidad fijas, su probabilidad de excedencia es la condicional a un desplazamiento no nulo, no menor que la de la formulación con su rama discreta. En todas las formulaciones, $k_y$, PGA y $S_a$ se expresan en unidades de $g$ —la aceleración de la gravedad—, $I_A$ en m/s y $T_s$ en segundos; la intensidad de Arias se deriva de la PGA de cada realización según [-@eq-newmark-arias], y la magnitud de referencia asignada a cada demanda sísmica se aplica a sus combinaciones de geometría y material. La forma publicada de cada formulación se reproduce en el Apéndice [-@sec-newmark-appendix]. El coeficiente sísmico basado en desempeño se define mediante

$$
k_{\max} (p_e\mid D_a)
=\inf\left\{k_y:P[D_n (k_y)>D_a]\leq p_e\right\}.
$${#eq-kmax-criterion}

donde $p_e$ es la probabilidad objetivo de que $D_n$ exceda $D_a$: $k_{\max}$ es el menor $k_y$ para el cual la probabilidad de exceder el desplazamiento admisible es a lo sumo $p_e$. El coeficiente normalizado, reportado como porcentaje de la PGA [% de la PGA], se calcula con la PGA media de cada demanda transformada al $V_{S30}$ de la combinación de geometría y material evaluada:

$$
k_h=100\,\frac{k_{\max}}{\mathrm{PGA} (V_{S30})}.
$${#eq-kh-normalization}

$k_{\max}$ se expresa en unidades de $g$ y $k_h$ como porcentaje de la PGA de la condición de sitio correspondiente. Estas dos magnitudes expresan el criterio de desplazamiento como la acción horizontal de la verificación pseudoestática.
