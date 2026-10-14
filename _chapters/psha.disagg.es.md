El PSHA agrega las contribuciones de todos los escenarios plausibles de sismo en la tasa total de excedencia, ocultando las combinaciones específicas de magnitud ($M$), distancia fuente-sitio ($R$) y residuo del movimiento del suelo ($\varepsilon$) que controlan la amenaza del sitio. La **desagregación de amenaza** cuantifica la contribución relativa de cada clase de escenario, agrupada por magnitud $m_k$, distancia $r_j$ y residuo $\varepsilon_\ell$, a la frecuencia anual de excedencia en un umbral especificado de movimiento del suelo $i^*$ [@Bazzurro1999].

La desagregación se realiza para un nivel de amenaza objetivo, definido por una probabilidad anual de excedencia o período de retorno. Esto produce distribuciones de probabilidad condicional sobre intervalos de escenario e identifica los parámetros de escenario que controlan la amenaza del sitio [@Kramer1997]. La tasa conjunta de excedencia para el escenario $(m_k, r_j, \varepsilon_\ell)$ de la fuente $s$ es

$$
\Delta\lambda_{I}(i^{*},m_k,r_j,\varepsilon)^{(s)} =
\mathbf 1_{\{\varepsilon\ge\varepsilon^{*}(m_k,r_j)\}}
\,
\varphi(\varepsilon)\,
f_{M,s}(m_k)\,
f_{\mathbf R\mid M,s}(r_j\mid m_k)\,
\nu_{0}^{(s)},
$${#eq-disagg-rate}

donde $\varphi$ es la función de densidad de probabilidad normal estándar y $\mathbf 1_{{\cdot}}$ es la función indicadora; la probabilidad de excedencia del movimiento del suelo y la tasa anual total de excedencia que intervienen en la formulación son las definidas en el análisis de amenaza (véanse [-@eq-hazard-integral], [-@eq-epsilon-star]). La integración sobre $\varepsilon$ produce la formulación bidimensional ($M$-$R$). Al particionar el espacio de parámetros en intervalos de magnitud $m_k$, intervalos de distancia $r_j$ e intervalos residuales $\varepsilon_\ell$, la contribución del intervalo $(k,j,\ell)$ es

$$
\lambda_{k,j,\ell}(i^{*})=
\sum_{s=1}^{N_{S}}
\int_{m_k}
\int_{r_j}
\int_{\varepsilon_\ell}
\Delta\lambda_{I}(i^{*},m_k,r_j,\varepsilon)^{(s)}
d\varepsilon\,dr\,dm
$${#eq-disagg-bin}

La desagregación de amenaza aplica el teorema de Bayes a la distribución conjunta de los parámetros del escenario y la excedencia del movimiento del suelo: la probabilidad condicional de que la excedencia de $i^*$ sea producida por este intervalo es

$$
P[M=m_k,R=r_j,\varepsilon=\varepsilon_\ell\mid I> i^{*}]
= \theta_{k,j,\ell}
=
\frac{\lambda_{k,j,\ell}(i^{*})}{\lambda_{I}(i^{*})}
$${#eq-disagg-prob}

y las probabilidades marginales se obtienen por doble sumatoria sobre los otros índices, sobre distancia y residuo para la magnitud,

$$
P\left[M \in m_k\mid I> i^{*}\right] = \sum_{j}\sum_{\ell}\theta_{k,j,\ell}
$${#eq-disagg-marginal-M}

sobre magnitud y residuo para la distancia,

$$
P\left[R \in r_j\mid I> i^{*}\right] = \sum_{k}\sum_{\ell}\theta_{k,j,\ell}
$${#eq-disagg-marginal-R}

y sobre magnitud y distancia para el residuo, cuya distribución marginal cuantifica la contribución de los intervalos residuales del movimiento del suelo a la excedencia:

$$
P\left[\varepsilon \in \varepsilon_\ell\mid I> i^{*}\right] = \sum_{k}\sum_{j}\theta_{k,j,\ell}
$${#eq-disagg-marginal-eps}

El **escenario modal** es el intervalo $(k,j,\ell)$ para el cual $\theta_{k,j,\ell}$ de [-@eq-disagg-prob] alcanza su máximo. El **escenario medio** es el par magnitud--distancia promedio de la distribución condicional, ponderado por esas contribuciones.

En este informe, las salidas de desagregación de OpenQuake se presentan como matrices magnitud-distancia (`Mag_Dist`). El cálculo usa intervalos de magnitud de 0.1 $M_w$, intervalos de distancia de 10 km, y las medidas de intensidad PGA, $S_a(0.10\,\mathrm{s})$, $S_a(0.20\,\mathrm{s})$, $S_a(0.50\,\mathrm{s})$ y $S_a(1.00\,\mathrm{s})$. Por lo tanto, los mapas de calor y la tabla modal reportados resumen la superficie de contribución bidimensional $M$-$R$ para cada período de retorno y período del oscilador seleccionados. La desagregación proporciona una base respaldada por datos para la selección de escenarios en el análisis de ingeniería. El *escenario modal* y los intervalos de mayor probabilidad identificados mediante la desagregación corresponden a las características de los sismos que más contribuyen a la excedencia del nivel de demanda sísmica de diseño.
