# CAN: qué árbol GMM reproducía NRCan y cómo usar NBCC en el entorno nuevo

Lectura del 2026-10-14, sólo inspección: `~/kashimaDB/openquake/gmm`, `legacy/oq` de este repositorio, las salidas de la corrida actual M2V4D y el motor instalado. Scripts en `scripts/gmmTrees.py`, `scripts/compareHazard.py`, `scripts/gmpeSCC.R`; salidas en `gmm-trees-summary.txt`, `compare-hazard-nrc-vs-current.txt`, `gmpe-scc-medians.log`. GEM queda fuera por instrucción del propietario.

## 1. Qué era cada cosa

| Nombre | Qué es | Dónde está |
|---|---|---|
| `nrc` | Corrida de 2024 de este repo (OpenQuake 3.19.1) con el modelo oficial CanadaSHM6/NBCC 2020: SSM del sureste de Canadá (H2 0.4, HY 0.4, R2 0.2) y el árbol GMM oficial `CanadaSHM6-GMM-LT.xml` (GSC Open File 8924). Es la corrida que reproducía NRCan. | `legacy/oq/model/nrc.zip`, `legacy/oq/run/nrc/nrc_<Vs30>.zip`, curvas en `legacy/oq/output/nrc/<Vs30>/` |
| `nbcc` | El mismo árbol GMM oficial, con los nombres canónicos de TRT (SCC, ASC, SIF, SIS30, SIS55). Byte a byte igual al de `nrc` salvo espacios (diff verificado). | `~/kashimaDB/openquake/gmm/legacy/nbcc/gmmLT_NBCC.xml` y, troceado por TRT, `~/kashimaDB/openquake/gmm/TRT/{SCC,ASC,SIF,SIS30,SIS55}/gmmLT_NBCC.xml` |
| `shm6` | Variante del árbol oficial: el SCC es idéntico (16 ramas), pero ASC, SIF y SIS fueron ampliados con modelos modernos (9, 8 y 7 ramas). Para Crawford da lo mismo que `nbcc`: sólo contribuye SCC. | `~/kashimaDB/openquake/gmm/legacy/shm6/gmmLT_SHM6.xml` |
| `nsha`, `nshas` | Árboles del modelo australiano NSHA23 (NGA-East backbone a 760). No aplican a Canadá. | `~/kashimaDB/openquake/gmm/legacy/nsha*` |
| SCC1, SCC2, SCC3 | Historia del seed SCC: SCC1 = 3 modelos (ESHM20, RietbrockEdwards2019, ShahjoueiPezeshk2016); SCC2 = NGA-East USGS, 23 ramas; SCC3 = el SCC de CanadaSHM6, 16 ramas. | `~/kashimaDB/openquake/gmm/docs/legacy/SCC/` |
| SCC actual | 6 modelos generales con pesos uniformes: Atkinson2008prime, AtkinsonBoore2006Modified2011, PezeshkEtAl2011, ESHM20Craton, SomervilleEtAl2009YilgarnCraton_SS14, CollapsedNGAEastUSGS (colapso del SCC2). | `~/kashimaDB/openquake/gmm/TRT/SCC/gmmLT_SCC.xml` |

El SCC oficial de CanadaSHM6 son 13 submodelos `CanadaSHM6_StableCrust_NGAEast` (NGA-East, pesos distintos por período) más `CanadaSHM6_StableCrust_AA13` alto, central y bajo (0.15, 0.25, 0.10). En Crawford sólo contribuye SCC: la desagregación por TRT de la corrida vieja a 760 y la tabla de fuentes de la corrida actual (todas SCC dentro de 1000 km) lo confirman.

## 2. Cuánto cambió el hazard y por qué

Sa media [g] a 2 % en 50 años (TR 2475), Vs30 760, de las curvas exportadas:

| | PGA | Sa(0.1) | Sa(0.2) | Sa(0.3) | Sa(0.5) | Sa(1.0) | Sa(2.0) |
|---|---|---|---|---|---|---|---|
| `nrc` 2024 (NBCC, SSM SE Canadá) | 0.106 | 0.310 | 0.206 | 0.136 | 0.093 | 0.044 | 0.019 |
| Actual (GMM generales, SSM nacional) | 0.159 | 0.346 | 0.225 | 0.153 | 0.091 | 0.042 | 0.022 |
| Actual / `nrc` | 1.51 | 1.12 | 1.09 | 1.13 | 0.97 | 0.96 | 1.18 |
| Actual con sólo los archivos SE Canadá / `nrc` | 1.39 | 1.04 | 1.01 | 1.05 | 0.91 | 0.90 | 1.10 |

Dos causas separables:

1. **SSM nacional combinado, +7 % en todos los períodos.** Barrido de los seis archivos (214 fuentes): seis fuentes aparecen con geometría y MFD idénticos en más de una región (James Bay, Stable Cratonic Core Eastern Canada H y R, Eastern Arctic H East, Western Canada, Eastern Continental Margin) y dos más con la misma geometría y otra MFD (Arctic y Eastern Continental Margin). Son zonas que cruzan los límites regionales y que el GSC incluye en cada modelo regional para que cada región sea completa por sí sola; las regiones son disjuntas, los archivos no. La corrida `nrc` usó sólo el modelo regional SE y por eso tenía una copia por rama. La fusión pone los tres archivos en cada rama y OpenQuake suma las copias; en las ramas mixtas conviven además la variante H de una región con la variante R de otra para la misma zona. `ssmLT_CAN.xml` es el producto correcto de las tres regiones (SE 0.4/0.4/0.2 × Ártico 0.6/0.4, Oeste en todas), pero cada rama incluye los tres archivos regionales, y la zona de fondo «Stable Cratonic Core Eastern Canada H» aparece tres veces con la misma MFD (a 5.7065, b 1.324): `SCCECH` en SE_H2, `SCCECH_ARC` en EasternArctic_H y `SCCECHW` en WesternCanada. En Crawford esas copias extra aportan el 9.4 % de la tasa anual de PGA; con sólo los archivos SE la ordenada de 2475 años baja un 7 %. La corrida `nrc` usaba sólo el SSM SE, como hace NRCan para un sitio de Ontario. La nota del propietario `ssm/CAN/support/ssm_diff.md` describe la combinación «garage» que generó esto.
2. **Árbol GMM, el resto.** Con el mismo alcance de fuentes, los seis modelos generales suben la PGA un 39 %, dejan Sa(0.2) igual, bajan Sa(0.5) y Sa(1.0) un 10 % y suben Sa(2.0) un 10 %.

Quién empuja dentro del SCC actual, mediana de cada modelo sobre la mediana del ensamble a Mw 6.0 y Repi 27 km, Vs30 760 (celda típica de la desagregación a 2500 años: Mw media 5.6, p84 6.6, R media 26 km):

| Modelo | PGA | Sa(0.2) | Sa(1.0) |
|---|---|---|---|
| Atkinson2008prime | 1.45 | 1.13 | 0.80 |
| AtkinsonBoore2006Modified2011 | 0.53 | 0.72 | 0.80 |
| PezeshkEtAl2011 | 0.76 | 0.64 | 0.64 |
| ESHM20Craton | 1.03 | 1.26 | 1.28 |
| SomervilleEtAl2009YilgarnCraton_SS14 | 1.36 | 1.27 | 2.02 |
| CollapsedNGAEastUSGS | 1.06 | 1.17 | 1.06 |

Somerville 2009 (cratón de Yilgarn, Australia) y Atkinson 2008' son los que más levantan la PGA; Somerville duplica el ensamble a 1 s. Esta tabla sale de `GMPETable.Rds` (receta `GMPESCC`, Vs30 760, profundidad 15 km); no mide la influencia de cada rama en la curva de hazard, que exigiría una corrida con `individual_curves` o una receta GMPE con el árbol NBCC para comparar medianas. La corrida actual sólo exportó la media.

## 3. Cómo usaría NBCC en el entorno nuevo

No hace falta recrear ningún TRT custom: los seeds ya existen y el motor los entiende.

- **Mapa de TRT de la receta.** Según la skill `hazard` (`specs-and-pack.md`), `"TRT": {"SCC": "<token>"}` resuelve `<gmmDir>/SCC/gmmLT_<token>.xml`. Una receta classical copia de `specs/calcs/classical/M2V4D.json` con `"TRT": {"ASC": "NBCC", "SCC": "NBCC", "SIF": "NBCC", "SIS30": "NBCC", "SIS55": "NBCC"}` tomaría `~/kashimaDB/openquake/gmm/TRT/<TRT>/gmmLT_NBCC.xml`, que existen desde el 1 de mayo para los cinco TRT.
- **Motor.** `~/opt/openquake/oq-3.26.2` incluye `hazardlib/gsim/can20/` con las 18 clases `CanadaSHM6_*` y las tablas `NGA-East-13` y `AA13` empaquetadas; es la misma versión 3.26.2 que corre en tms9900 según `CALCULATION-STATUS.md`. Las 16 ramas SCC son submodelos de dos clases: el árbol no necesita el `gmm.gmpe` custom.
- **Pesos por período.** `TRT/SCC/gmmLT_NBCC.xml` del 1 de mayo perdió los `uncertaintyWeight imt="..."`: conserva sólo el peso base, que es el de PGA, para las 16 ramas (232 líneas en el `.bak` frente a 89). El árbol oficial pondera distinto cada período. Para replicar NRCan hay que usar la versión del `.bak` o verificar que el empaquetador conserva ese atributo; es una decisión del propietario y, si se restaura, una prueba de `pack` antes de correr.
- **SSM.** Para replicar NRCan en Crawford, el SSM debería ser sólo el sureste de Canadá, como en `nrc` (3 ramas), o bien el nacional sin las copias duplicadas de las zonas de fondo. Hoy el contrato apunta a `ssmLT_CAN.xml` nacional. Cambiarlo es decisión del propietario; el modelo regional SE ya está en `ssm_CAN/` (los tres archivos) y sólo falta un `ssmLT` regional.
- **Resto de la receta.** `nrc` usaba distancia máxima 600 km (hoy 1000), discretización de áreas 10 km (hoy 5) y `complex_fault_mesh_spacing` 20 (hoy 10). Efecto menor esperable, pero son diferencias que una réplica exacta debería alinear o justificar.

## 4. Lo que no está verificado

- No se consultaron los valores publicados por NRCan; la afirmación de que `nrc` los reproducía es del propietario. Las curvas `nrc` sí están en el repo y son la referencia usada aquí.
- No se corrió nada: ni `pack`, ni `gmpe`, ni cálculo. Todo lo anterior es lectura de archivos y de salidas existentes.
- Si el `.bak` con pesos por período se empaqueta correctamente con `hazard pack` es una incógnita hasta probarlo.

## 5. Piloto del SSM deduplicado (2026-10-14, aprobado por el propietario)

Modelo `ssm/CAN` reescrito en su lugar (rama `issue/CAN-dedup-backgrounds` del repositorio `ssm`, anterior en `CAN/legacy/v2020.1.4`), misma receta `M2V4D.json`, mismos seeds GMM, misma firma de árbol GMM. Celda classical CFD 760: cálculo 34 en tms9900, completo, extraído a un directorio aparte y comparado con la familia commiteada en `dddf10b` (cálculo 5, motor local). Cociente piloto / commiteado de la Sa media:

| TR | PGA | Sa(0.1) | Sa(0.2) | Sa(0.3) | Sa(0.5) | Sa(1.0) | Sa(2.0) |
|---|---|---|---|---|---|---|---|
| 475 | 0.866 | 0.865 | 0.873 | 0.880 | 0.892 | 0.919 | 0.922 |
| 2475 | 0.930 | 0.929 | 0.932 | 0.933 | 0.936 | 0.947 | 0.946 |
| 10000 | 0.949 | 0.949 | 0.955 | 0.954 | 0.958 | 0.961 | 0.954 |

A TR 2475 coincide con la predicción del reparto por fuentes (0.930 a 0.947), lo que confirma que el 7 % venía de las copias duplicadas y de nada más. El efecto es mayor a períodos de retorno cortos, donde el fondo pesa más, y menor a 10 000 años. Tablas en `pilot-vs-committed-760.txt`; logs `hazard-ssm-20261014.log`, `hazard-pack-760-20261014.log`, `hazard-run-760-20261014.log`, `hazard-extract-760-20261014.log`.
