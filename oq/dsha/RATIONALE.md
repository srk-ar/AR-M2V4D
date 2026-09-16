# Crawford: base de rationale y alcance GMM

Fecha: 2026-09-15. Sitio **CFD**, 48.794912° N, −81.340633°.
Estado: evidencia inicial para revisión del propietario. No establece escenarios
MCE, Mmax, tasas, geometrías de ruptura ni una grilla GMPE aprobada.

## 1. Decisión vigente: GMM sólo SCC

**Lista de TRT que se preparará para GMM: `SCC`.**

El propietario excluyó SIS y SIF y pidió resolver SCC frente a SCC+ASC leyendo
CAN. Como la PSHA ya fue ejecutada, indicó aplicar la exclusión a la lista futura
de GMM. Quedan fuera ASC, SIF, SIS, SIS30 y SIS55. Se conservan los contratos,
paquetes y resultados de la generación calculada.

### Evidencia del modelo [OBS]

Se leyó [ssmLT_CAN.xml](/Users/averrik/kashimaDB/openquake/ssm/CAN/model/ssmLT_CAN.xml)
y se analizaron los seis archivos XML que realmente referencia, sin incorporar
los archivos collapsed que no selecciona. El árbol combina seis ramas nacionales
con pesos 0.24, 0.16, 0.24, 0.16, 0.12 y 0.08.

| Archivo de fuentes incluido | TRT y número de ocurrencias de fuentes |
|---|---|
| SouthEasternCanada_H2 | SCC: 37 |
| SouthEasternCanada_HY | SCC: 45 |
| SouthEasternCanada_R2 | SCC: 17 |
| EasternArctic_H | SCC: 21 |
| EasternArctic_R | SCC: 13 |
| WesternCanada | SCC: 5; ASC: 58; SIF: 13; SIS30: 1; SIS55: 4 |

Son ocurrencias por archivo, no una suma de fuentes independientes: hay fuentes
compartidas entre alternativas regionales. La tabla SSM del proyecto contiene
202 proveedores únicos, de los cuales 126 son SCC.

### Participación en CFD [OBS]

El [contrato clásico](/Users/averrik/Cloud/github/projects/AR-M2V4D/oq/calcs/classical/M2V4D.json)
fija distancia máxima de 1000 km. Lectura de SSMTable y enlace de AEPSTable por
`ID, siteID, providerID`, con unicidad y correspondencia completa comprobadas:

| TRT | Menor Rrup de SSM (km) | Proveedores AEP observados, Vs30=760 |
|---|---:|---:|
| SCC | 0.000 | 70 |
| ASC | 2274.565 | 0 |
| SIS55 | 2941.893 | 0 |
| SIF | 3043.846 | 0 |
| SIS30 | 3067.534 | 0 |

Los 70 proveedores con Rrup ≤ 1000 km son SCC y coinciden con los 70 proveedores
de AEPSTable; el más distante está a 979.759 km. La comparación GMM local queda
en SCC por esta participación, no porque el modelo nacional carezca de ASC.

El [árbol SCC actualmente referenciado](/Users/averrik/kashimaDB/openquake/gmm/TRT/SCC/gmmLT_SCC.xml)
contiene Atkinson2008prime, AtkinsonBoore2006Modified2011, PezeshkEtAl2011,
ESHM20Craton, SomervilleEtAl2009YilgarnCraton_SS14 y CollapsedNGAEastUSGS:
cinco pesos 0.16667 y el último 0.16665. Esta lectura identifica el insumo existente;
no demuestra por sí sola la adecuación de cada ecuación o de una geometría nueva.

## 2. Mapper y evidencia histórica

[Abrir mapper](http://127.0.0.1:52795/).
Archivos: [mapa](/Users/averrik/Cloud/github/projects/AR-M2V4D/mapper/byEvent/index.html)
y [catálogo](/Users/averrik/Cloud/github/projects/AR-M2V4D/mapper/byEvent/epicenters.csv).

Ejecución exitosa del mapper existente con radio 500 km; filtro de magnitudes
3.5–7.5 preservado. Produjo 134 filas: USGS 45, ISC 88 y GCMT 1, entre 1935 y 2026.
Las etiquetas de magnitud son heterogéneas; el nombre del filtro no convierte
ML, mb, mblg, MB1, Mwc, etc. en Mw. No es un catálogo histórico completo.

Se encargó una investigación independiente y se leyó su
[dossier completo](/Users/averrik/Cloud/github/tools/oqt/dev/SoT/m2v4d-gmpe-reference-study-20260915/historical-research/RESEARCH.md).
Se verificaron las tablas oficiales de los tres antecedentes siguientes y su
presencia/ausencia en el CSV. Las distancias [DER] son epicentrales aproximadas,
calculadas con haversine y radio terrestre 6371.0088 km; no equivalen a Rrup.

| Antecedente [OBS] | Distancia a CFD [DER] | Correlación con mapper |
|---|---:|---|
| 1928-12-01, Kapuskasing–Cochrane, ML 5.0 | 134.5 km | Ausente |
| 1935-11-01, Timiskaming, Mw 6.1 | 281.0 km | Presente con otra solución: Mw 6.17, 286.7 km |
| 1958-05-14, oeste de Québec, ML 5.0 | 410.8 km | Ausente |

Fuentes primarias: [NRCan, Kapuskasing](https://www.earthquakescanada.nrcan.gc.ca/recent/2020/20201014.1348/seismicity-en.php),
[NRCan, Timiskaming1935](https://www.earthquakescanada.nrcan.gc.ca/historic-historique/events/19351101-en.php),
[NRCan, oeste de Québec](https://www.earthquakescanada.nrcan.gc.ca/recent/2025/20250217.1624/seismicity-en.php).

La consulta NEDB del investigador devolvió 75 registros de magnitud preferida ≥ 3:
42 earthquake, 29 rock burst, 3 mining explosion y 1 induced or triggered event.
Se comprobaron esos conteos contra el XML original. El servicio consultado no
proporciona una historia completa desde 1600 aunque se solicitó esa fecha inicial.

El [cruce documentado](/Users/averrik/Cloud/github/tools/oqt/dev/SoT/m2v4d-gmpe-reference-study-20260915/historical-research/MAPPER-CROSSCHECK.json)
contiene 72 parejas candidatas únicas dentro de ±60 s, verificadas contra el CSV.
Treinta tienen clasificación minera o inducida en NRCan. Esto no clasifica
automáticamente como naturales las otras 104 filas del mapa.

Los dos puntos más próximos del mapper, 2009-01-06 y 2011-09-13, corresponden a
eventos clasificados rock burst por NRCan. El dossier aporta además la
investigación original sobre Kidd Creek. Sus posiciones y magnitudes difieren
entre catálogos: se conservan separadas, sin promediarlas.

También hay un evento NEDB clasificado earthquake, 2005-06-11, MwN 1.47, a 4.5 km,
por debajo del filtro del mapa. La ausencia de puntos cercanos filtrados no
demuestra ausencia de sismicidad. El evento de Shawville de 2013 queda a 507.5 km con
epicentro NRCan y 499.0 km con centroide GCMT; el dossier distingue ambas posiciones.

## 3. Método y decisiones pendientes

Se revisaron las secciones de evidencia de los seis rationale de referencia;
su [comparación metodológica](/Users/averrik/Cloud/github/tools/oqt/dev/SoT/m2v4d-gmpe-reference-study-20260915/RATIONALE-REFERENCES.md)
separa observación, derivación, inferencia y decisión del propietario.

La lista SCC está resuelta. Para convertir esta base en receta falta contrastar
la revisión manual del mapa con las fuentes y mecanismos documentados y
fundamentar magnitudes, distancias, profundidad/geometría y modelos/pesos.
Los valores repetidos en otras recetas no adquieren aceptación para Crawford
por repetición. El máximo histórico observado tampoco determina Mmax ni la
distancia mínima de una ruptura futura.

El [hallazgo SIS](/Users/averrik/Cloud/github/tools/oqt/dev/SoT/m2v4d-gmpe-reference-study-20260915/SIS-FINDING.md)
identifica SiEtAl2020SSlab como ecuación retirada de SIS y todavía presente en
SIS30/SIS55. La exclusión de subducción de la futura comparación local resuelve
su alcance en este proyecto; no repara ni valida los árboles externos.

No se generó GMPETable, no se copiaron recetas, no se ejecutó MCE ni se repitió OQ.
