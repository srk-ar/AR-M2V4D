# Cotejo acotado de Hazard

Los valores comparados no son idénticos. Este cotejo es de lectura; no modifica el capítulo de Hazard de Diana ni los productos del modelo.

Fuentes leídas: extracción pública pdf2md del original de Diana, tablas 9-1 y 9-2, líneas 1160–1216; docx.en.docx actualizado por NGR, tabla 4.2, extracción en /private/tmp/diana-delivery-check.QSbzK8/report/docx.en.md:814–844. El builder _tbl/PGA.TR.qmd selecciona UHSTable, ID M2V4D, sitio CFD y SaF para la PGA por condición de sitio. Se cotejaron 16 celdas de UHSTable.Rds con Diana, restringidas a Vs30 760 y 1500 m/s, medias y percentil84, TR500,2500,5000,10000. Se aceptaron 475/500 y 2475/2500 según instrucción expresa; no se interpoló ni se compararon condiciones Vs30 distintas. La tabla 4.2 del Word presenta directamente Vs30=1500; los valores a 760 se cotejan con sus datos consumidos y con el resumen de roca de referencia.

Ejemplos de PGA media a Vs30=1500 m/s:

| TR Diana / proyecto | Diana (g) | Proyecto (g, dato) | Proyecto (g, Word) | Diferencia relativa |
| --- | ---: | ---: | ---: | ---: |
| 2475 / 2500 | 0.1098 | 0.12613013 | 0.126 | +14.87% |
| 10000 / 10000 | 0.3139 | 0.28515457 | 0.285 | -9.16% |

Los datos y las diferencias de las 16 celdas están en hazard-sanity.csv, reproducibles mediante checkHazard.R. No se atribuye aquí la causa de las diferencias, ni se afirma una auditoría exhaustiva de espectros, fuentes, escenarios o figuras. Las tablas espectrales de Diana visibles en las páginas físicas 77 y 78 del render conservan, redondeadas, esas mismas PGA medias. El capítulo de Hazard se preserva aunque el cotejo no confirme igualdad numérica.
