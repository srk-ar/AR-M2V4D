Los modelos de desplazamiento de bloque flexible evalúan la demanda espectral en períodos proporcionales al período fundamental de la masa potencialmente deslizante, de modo que cada combinación de geometría y material necesita $T_s$, que se obtiene a partir de la geometría del talud y de la variación del módulo de corte de pequeña deformación con la profundidad, representada por $G_o$, $m_o$ y $V_S^o$; los valores medios de $T_s$ y $V_{S30}$ caracterizan la respuesta dinámica empleada en los modelos de desplazamiento del capítulo dedicado a los desplazamientos permanentes. El período fundamental de la masa potencialmente deslizante se representa mediante el primer modo de una viga de corte inhomogénea truncada [-@DakoulasGazetas1985Inhomogeneous]:

$$
T_s=\frac{4\pi H}{a_1(2-m_o)V_S^o}.
$${#eq-slope-period}

En la expresión [-@eq-slope-period], $H=H_s/(1-\lambda_o)$ es la altura de la cuña truncada desde el vértice de los taludes prolongados hasta la base y $H_s$ es la altura del talud; $V_S^o$ es la velocidad de onda de corte correspondiente al módulo basal $G_o$; $m_o$ es el exponente del perfil de rigidez; y $a_1$ es la primera raíz de la ecuación característica. El valor de $a_1$ depende conjuntamente de $m_o$ y de la razón de truncamiento $\lambda_o$, que puede expresarse, por semejanza geométrica, según la expresión [-@eq-slope-truncation], donde $b$ es el ancho de la berma y $b_{\max}$ es el ancho de la base.

$$
\lambda_o=\frac{b}{b_{\max}}.
$${#eq-slope-truncation}

Para la sección truncada equivalente, la altura $H_s$, la relación de talud $s$ y la razón de truncamiento $\lambda_o$ determinan el ancho $b$ de la berma y el ancho $b_{\max}$ de la base según las expresiones [-@eq-slope-berm-width] y [-@eq-slope-base-width], respectivamente; la relación de talud se define por $\tan\beta=1/s$, con $\beta$ el ángulo del talud.

$$
b=\frac{2H_s s}{1/\lambda_o-1}.
$${#eq-slope-berm-width}

$$
b_{\max}=b+2H_s s.
$${#eq-slope-base-width}

La Figura [-@fig-wedge] muestra la sección truncada equivalente con estos parámetros: los taludes prolongados se cortan en el vértice, a la altura $h=\lambda_o H$ sobre la berma, de modo que $H=H_s+h$.

```{r}
#| include: false
CAP <- readCaption("fig.wedge.ES")
```

{{< include /_fig/wedge.qmd >}}

En cada realización, la velocidad basal de onda de corte $V_S^o$ se obtiene según la expresión [-@eq-slope-basal-velocity], donde $G_o$ es el módulo basal ajustado, $g$ es la aceleración de la gravedad y $\gamma_{\mathrm{sat}}^{(k_{\mathrm{b}})}$ es el peso unitario saturado de la capa basal, cuyo índice es $k_{\mathrm{b}}$, con las magnitudes expresadas en unidades consistentes.

$$
V_S^o=\left(\frac{gG_o}{\gamma_{\mathrm{sat}}^{(k_{\mathrm{b}})}}\right)^{1/2}.
$${#eq-slope-basal-velocity}

El perfil de rigidez de cada realización se representa según la expresión [-@eq-slope-profile], donde $z$ es la profundidad medida desde la coronación, $G_o$ es el módulo ajustado en $z/H_s=1$ y $m_o$ es el exponente obtenido del ajuste por mínimos cuadrados de $\ln G_m^{(k)}$ en función de $\ln(z_m^{(k)}/H_s)$ sobre las capas con módulo positivo, con $z_m^{(k)}$ la profundidad del punto medio de la capa $k$; la ecuación característica corresponde a la ley de potencia con la profundidad medida desde el vértice de los taludes prolongados y normalizada por $H$ [-@DakoulasGazetas1985Inhomogeneous], de modo que evaluar $a_1$ con el exponente ajustado desde la coronación es una aproximación.

$$
G(z)=G_o\left(\frac{z}{H_s}\right)^{m_o}.
$${#eq-slope-profile}

Los módulos de capa provienen de la clasificación del suelo: la clasificación USCS de la capa $k$, extraída con probabilidad uniforme y con reemplazo entre las clases del escenario de material, determina su familia constitutiva y las $J^{(k)}$ formulaciones tabuladas de rigidez [-@Ishihara1996], y el módulo adoptado para la capa corresponde a la media aritmética definida por la expresión [-@eq-slope-modulus], donde $A^{(j)}$ y $n^{(j)}$ son parámetros tabulados, $F_e^{(k,j)}$ es el factor de relación de vacíos, $m_1^{(k)}$ es el exponente de sobreconsolidación, $p_m^{(k)}$ es la tensión normal octaédrica efectiva promediada en el espesor de la capa y $p_{\mathrm{ref}}=100$ kPa es la presión de normalización.

$$
G_m^{(k)}=\frac{1}{J^{(k)}}\sum_{j=1}^{J^{(k)}}
A^{(j)}F_e^{(k,j)}
\left[\mathrm{OCR}^{(k)}\right]^{m_1^{(k)}}
p_{\mathrm{ref}}^{n^{(j)}}
\left(\frac{p_m^{(k)}}{p_{\mathrm{ref}}}\right)^{n^{(j)}}.
$${#eq-slope-modulus}

La tensión normal octaédrica efectiva, promediada en el espesor de la capa $k$, $p_m^{(k)}$ [-@HardinBlack1968; -@HardinDrnevich1972], se obtiene, para el estado de esfuerzos en reposo, según la expresión [-@eq-slope-mean-pressure], donde $K_0=0.5$ es el coeficiente de presión lateral en reposo, $\gamma^{(\ell)}$ y $h^{(\ell)}$ son el peso unitario correspondiente a la condición freática y el espesor de la capa $\ell$, y $\ell<k$ identifica las capas suprayacentes; una capa cuyo punto medio queda bajo el nivel freático toma el peso unitario sumergido $\max(\gamma_{\mathrm{sat}}-10\,\mathrm{kN/m^3},0)$, y las realizaciones se generan para una columna seca, de modo que $\gamma^{(\ell)}=\gamma_{\mathrm{sat}}^{(\ell)}$.

$$
p_m^{(k)}=\frac{1+2K_0}{3}
\left(\sum_{\ell=1}^{k-1}\gamma^{(\ell)}h^{(\ell)}
+\frac{\gamma^{(k)}h^{(k)}}{2}\right).
$${#eq-slope-mean-pressure}

La razón de sobreconsolidación $\mathrm{OCR}^{(k)}=\max[(p_m^{(k)}+\mathrm{POP})/p_m^{(k)},1]$, donde $\mathrm{POP}=100$ kPa es la presión de preconsolidación, sólo modifica el módulo de los suelos finos: en ellos $m_1^{(k)}=f_{\mathrm{IP}}(\mathrm{IP}^{(k)})$ [@HardinDrnevich1972b], con $f_{\mathrm{IP}}$ interpolada linealmente entre los nodos $\mathrm{IP}$ = 0, 20, 40, 60, 80 y 100 con $m_1$ = 0, 0.18, 0.30, 0.41, 0.48 y 0.48, mientras que en arenas y gravas $m_1^{(k)}=0$ y $[\mathrm{OCR}^{(k)}]^{m_1^{(k)}}=1$. La relación de vacíos $e_0^{(k)}$ interviene en las tres familias mediante $F_e^{(k,j)}$, que en las formulaciones tabuladas [-@Ishihara1996] se define mediante [-@eq-slope-void-factor] a partir de la relación de vacíos $e_0^{(k)}$ y del parámetro $C_e^{(j)}$; $j_{\mathrm{SS75}}$ identifica la formulación de Shibata y Soelarno [-@ShibataSoelarno1975].

$$
F_e^{(k,j)}=
\begin{cases}
C_e^{(j)}-\dfrac{e_0^{(k)}}{1+e_0^{(k)}}, & j=j_{\mathrm{SS75}},\\[6pt]
\dfrac{\left(C_e^{(j)}-e_0^{(k)}\right)^2}{1+e_0^{(k)}}, & j\ne j_{\mathrm{SS75}}.
\end{cases}
$${#eq-slope-void-factor}

La velocidad de onda de corte $V_S^{(k)}$ de la capa $k$ se obtiene según la expresión [-@eq-slope-layer-velocity], donde $G_m^{(k)}$ es el módulo adoptado para la capa, $\gamma_{\mathrm{sat}}^{(k)}$ es su peso unitario saturado y las magnitudes se expresan en unidades consistentes.

$$
V_S^{(k)}=\left(\frac{gG_m^{(k)}}{\gamma_{\mathrm{sat}}^{(k)}}\right)^{1/2}.
$${#eq-slope-layer-velocity}

```{r}
#| include: false
CAP <- readCaption("tbl.SiteGo.ES")
SiteGo.headers <- c("Formulación", "Familia", "Material de referencia", "Autor")
SiteGo.groups <- c(Sands = "Arenas", Fines = "Finos", Gravels = "Gravas")
```

{{< include /_tbl/SiteGo.qmd >}}

Para cada combinación de geometría y material se generan $N=100$ realizaciones sintéticas del perfil estratificado, con capas de 1 m cuya relación de vacíos, peso unitario saturado y, en los suelos finos, límite líquido e índice de plasticidad se extraen con distribuciones uniformes en intervalos tabulados por clase, y los valores de $G_o$, $m_o$, $V_S^o$ y $V_{S30}$ se resumen separadamente mediante la media y los fractiles marginales 0.02, 0.05, 0.10, 0.16, 0.84, 0.90, 0.95 y 0.98. Para la media y cada fractil marginal, $a_1$ y $T_s$ se evalúan con los valores correspondientes de $m_o$ y $V_S^o$, con $a_1$ dado por un sustituto de regresión ajustado a una tabla de raíces de la ecuación característica para $m_o$ entre 0 y 0.95 y $\lambda_o$ entre 0 y 0.5, que extrapola fuera de ese intervalo; el período de un fractil es así la expresión evaluada con los fractiles de $m_o$ y $V_S^o$, no un fractil del período, y las estimaciones basadas en la media proporcionan las propiedades dinámicas empleadas por los modelos de desplazamiento. El valor de $V_{S30}$ se obtiene por tiempo de viaje según la expresión [-@eq-slope-vs30], donde $h_{30}^{(i)}$ es el espesor de la capa $i$ comprendido en los primeros 30 m, $V_S^{(i)}$ es su velocidad de onda de corte y $V_{\mathrm{ref}}=760$ m/s es la velocidad asignada al espesor complementario cuando $H_s<30$ m.

$$
V_{S30}=\frac{30}{
\displaystyle\sum_i\frac{h_{30}^{(i)}}{V_S^{(i)}}
+\dfrac{\max(30-H_s,0)}{V_{\mathrm{ref}}}}.
$${#eq-slope-vs30}
