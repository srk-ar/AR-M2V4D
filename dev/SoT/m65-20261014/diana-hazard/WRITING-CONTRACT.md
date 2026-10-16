# Actualización de resultados Hazard en Diana

## Product and surfaces
Una copia nueva de CAPR003324_Crawford_SeismicHazard_Final_AVK.docx, inglés. Sustituciones puntuales de resultados en resumen, capítulos6–9, conclusiones y anexosC/D. Transferencia por _local/hazard.diana.en.qmd, _results/hazard.diana.qmd y captions de identificación de objetos. Se conserva el texto restante, sus ecuaciones, citas, estilos y el capítulo10 aceptado.

## Reader and purpose
Diana y los revisores del informe de Crawford: disponer de resultados vigentes del modelo del proyecto, con las mismas condiciones Vs30 de su documento y la redacción existente. El documento de transferencia es un intermedio de implementación; la entrega es su Word actualizado.

## Sources
|Source|Class|Access level|Location read|
|---|---|---|---|
|Diana original, extracción pública pdf2md CAPR003324_Crawford_SeismicHazard_Final.md|Texto del proyecto designado por el propietario|Lectura dirigida|Líneas166–185,873–1004,1093–1188,1215–1240,1599–1606 y tablas completas en OOXML|
|Copia AVK aceptada|Texto del proyecto y base de preservación|Lectura dirigida del OOXML y QA previo|word/document.xml, párrafos24–27,543,593,633,651,672,786,788; tablas9-1..4/D1-1..5; figuras y capítulo10|
|_results/site.results.qmd|Fuente interna aprobada del proyecto|Completa|Descripción de mezcla de evaluación directa y transformación ST20, condicionada por PGA de la misma realización|
|data/hazard/tables/UHSTable.Rds y RMwTable.Rds|Datos auditados del proyecto|Lectura del esquema y selección exacta|CFD, M2V4D, SaF en g; RMw Tn0 y cinco TR de Diana. Pendiente incorporar y auditar nuevas celdas antes de obtener el texto definitivo|
|nrc2020-request.json y nrc2020-response.json|Fuente externa oficial autorizada|Respuesta completa|Consulta NBC2020 oficial a coordenadas CFD y cinco Vs30; valores medios a PoE50 2,5,10|
|diana-hazard/submit.log|Recibo de ejecución científica|Completa|Engine3.26.2 y cálculos90/91/92; versión se lee con R|

## Unit of analysis
Resultados por Vs30, período espectral, período de retorno y estadístico. Media distinta de P50. La desagregación distingue máximos conjuntos y marginales. La comparación NRC se limita a períodos comunes y Vs1500/760/220 mostrados en las figuras8-1..3.

## Language direction
Inglés del Word de Diana como fuente explícita; no se traduce ni se reescribe el capítulo. Vocabulario adicional de la descripción de respuesta de sitio ya aprobada en _results/site.results.qmd. Los números proceden de R.

## Length and structure
Mantener párrafos, captions y estructura editorial existentes. Sustituir cifras y sólo las oraciones metodológicas incompatibles con los productos actuales. Sin resumen nuevo ni conclusiones ajenas a la comparación solicitada.

## Acceptor and delivery order
El propietario autorizó «Actualiza una copia de su Word manteniendo su redacción y las correcciones de taludes». La aceptación de esta operación está dada; no se introduce una ronda adicional de permiso para las sustituciones comprendidas. Auditar el texto exacto computado antes del render final y revisar el Word completo afectado. Respuesta AEP: «Conservar curvas completas del cálculo directo». Respuesta NRC: «Consultar NRC 2020 oficial».

## Assembly identity
Master _local/hazard.diana.en.qmd SHA256 b5bc007e90da4f6968e9f9bf39b3aaf891efeb599eb234f0d114bbc29f83030d incluye _results/hazard.diana.qmd SHA256 cb5f7e005075dbc94fdecd5f10f7e5d1b7300752e70487a0a753bf8be9edddcc. Texto expandido prose-candidate.md SHA256 bb0c1d97f26d9146d85d3e0e33d009b048e221bebeed066a6b014fd11612bfef. NGR WIP exit0; la copia de trabajo se renderiza sólo para QA hasta terminar la auditoría. Los encabezados de transferencia son claves internas; el Word final conserva sus encabezados y captions.

## Exclusions
«no rompas nada», «no hardcodear números», «Conserva los Vs30 de Diana», «usa la grilla espectral del modelo», «manteniendo su redacción y las correcciones de taludes». Sin Newmark, sin global hydrate, sin Git/deploy nuevo, sin reparar residuos o referencias preexistentes ajenos a la actualización.
