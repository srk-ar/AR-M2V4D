# Render local de AR-M2V4D — 2026-09-18

**16 de los 21 artefactos del manifiesto fueron generados en esta ejecución. El proyecto completo sigue pendiente.**

Los archivos finales se comprobaron después de terminar QRT: todos los de la tabla son nuevos de esta ejecución, entre 00:18:54 y 00:47:11 (UTC−03).

| Alias | HTML generado |
|---|---|
| toc | [Índice](/Users/averrik/Cloud/github/projects/AR-M2V4D/html/toc/index.html) |
| gmdp | [Índice GMDP](/Users/averrik/Cloud/github/projects/AR-M2V4D/html/gmdp/index.html) |
| sdc | [Criterios sísmicos](/Users/averrik/Cloud/github/projects/AR-M2V4D/html/sdc/index.html) |
| sha | [Amenaza sísmica](/Users/averrik/Cloud/github/projects/AR-M2V4D/html/sha/index.html) |
| srs | [Índice SRS](/Users/averrik/Cloud/github/projects/AR-M2V4D/html/srs/index.html) |
| at | [Aceleraciones](/Users/averrik/Cloud/github/projects/AR-M2V4D/html/srs.at/index.html) |
| vt | [Velocidades](/Users/averrik/Cloud/github/projects/AR-M2V4D/html/srs.vt/index.html) |
| dt | [Desplazamientos](/Users/averrik/Cloud/github/projects/AR-M2V4D/html/srs.dt/index.html) |
| ai | [Intensidad de Arias](/Users/averrik/Cloud/github/projects/AR-M2V4D/html/srs.ai/index.html) |
| cav | [CAV](/Users/averrik/Cloud/github/projects/AR-M2V4D/html/srs.cav/index.html) |
| cav5 | [CAV5](/Users/averrik/Cloud/github/projects/AR-M2V4D/html/srs.cav5/index.html) |
| psa | [PSA](/Users/averrik/Cloud/github/projects/AR-M2V4D/html/srs.psa/index.html) |
| psv | [PSV](/Users/averrik/Cloud/github/projects/AR-M2V4D/html/srs.psv/index.html) |
| sd | [Desplazamiento espectral](/Users/averrik/Cloud/github/projects/AR-M2V4D/html/srs.sd/index.html) |
| its | [ITS](/Users/averrik/Cloud/github/projects/AR-M2V4D/html/srs.its/index.html) |
| ipsa | [IPSA](/Users/averrik/Cloud/github/projects/AR-M2V4D/html/srs.ipsa/index.html) |

| Alias pendiente | Resultado de esta ejecución |
|---|---|
| report | Intentado; falla en executive.qmd:109–120 con `object 'IDg.gmdp' not found`. No hay HTML final. |
| ts | No intentado; falta ShearTable.Rds. |
| dn | No intentado; falta DnTable.Rds y sus dependencias. |
| kmax | No intentado; falta kmaxTable.Rds y sus dependencias. |
| kh | No intentado; falta kmaxTable.Rds y sus dependencias. |

`IDg.gmdp` se deriva de DnTable en scripts/setup/global.R. No es una tabla ni un identificador que el propietario tenga que entregar manualmente. La preparación clásica de data.R y la producción de las tablas Newmark quedaron incompletas.

## Ejecuciones y comprobaciones

CWD: `/Users/averrik/Cloud/github/projects/AR-M2V4D`.

1. `qrt render --manifest qrt.manifest.json`: exit 1; toc terminado y report fallido. [Registro](/Users/averrik/Cloud/github/projects/AR-M2V4D/dev/SoT/render-project-20260918/qrt-manifest.log).
2. `qrt render --manifest qrt.manifest.json --except toc,report,ts,dn,kmax,kh`: exit 0; QRT informa 15 trabajos terminados y 15 salidas presentes. [Registro](/Users/averrik/Cloud/github/projects/AR-M2V4D/dev/SoT/render-project-20260918/qrt-available.log).

Se comprobaron los HTML finales, sus fechas y tamaños y la existencia no vacía de los recursos locales src/href extraídos (scripts, estilos, imágenes e iframe). Se leyeron las secciones principales de SHA/SDC y títulos de galerías. No se realizó QA visual: el navegador bloqueó la URL local file://. Los índices conservan los dominios de publicación definidos en el proyecto; los enlaces de esta tabla abren directamente los archivos locales.

Los hashes de oq/data/data.R, gmsp/match.json y qrt.manifest.json son idénticos antes y después del lote. No se modificaron parámetros científicos ni se ejecutaron borrados, reinicializaciones, instalaciones o publicaciones.

Se releyeron los SKILL.md instalados de QRT y OQT y sus referencias pertinentes. No se encontró un skill PSHA instalado en las raíces de agents, Codex, Claude o plugins, ni en el checkout de PSHA; el programa /usr/local/bin/psha sí existe y se leyó su ayuda.

El render no resuelve la revisión científica SRS ya documentada ni las figuras GMM condicionadas a GMPETable, que sigue ausente. S1 permanece definitivo y no se inventaron los textos CAN.
