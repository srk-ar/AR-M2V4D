# Plan de actualización de Hazard en el reporte de Diana

Preparado el 2026-10-15 por la orden «prepara un plan para actualizar el reporte de Diana tambien conlos datos de hazard». Este documento propone la actualización; no la ejecuta.

## Base y fuente de resultados

La base es la copia ya corregida en taludes, `docx/diana-actualizado/CAPR003324_Crawford_SeismicHazard_Final_AVK.docx`, SHA-256 `69eee3e499fde36cba7886ec8504114d164cc8d4942725a9bc8b9560226cfdc8`. El nombre actual incorpora `_AVK`; el hash coincide con la entrega aceptada. El original permanece separado.

Se conservan las correcciones de taludes, la redacción de Diana, el formato y los datos de campo. Los resultados se trasladan desde datos auditados, preparados por R y renderizados mediante NGR. No se editan cifras en `_chapters/`, ni se completa una celda por proximidad a otra velocidad o período. El plan no autoriza cambiar hipótesis científicas ni repetir las corridas ya aceptadas.

El cotejo existente, `diana-sources/hazard-sanity.csv`, cubre 16 PGA: Vs30 760/1500 m/s, media/P84 y cuatro demandas. Por ejemplo, a Vs30 1500 y TR2475/2500, la media pasa de 0.1098 a 0.12613013 g y P84 de 0.1438 a 0.18033563 g. El rango observado de diferencias relativas en esas 16 celdas va de -9.16 % a +34.74 %. No demuestra que todos los cambios sean pequeños ni verifica todavía el resto del documento.

## Dos incompatibilidades que deben resolverse antes de llenar tablas

La inspección de `data/hazard/tables/UHSTable.Rds` encontró 49 152 filas, sitio CFD, IDs `M2V4D`, `M2V4D.oq` y `M2V4D.site`. Sus condiciones Vs30 son 180, 270, 360, 560, 760, 800, 1250 y 1500 m/s. Diana presenta 220, 580, 760, 910 y 1500 m/s. Por tanto, **220, 580 y 910 no están disponibles en la tabla actual**; 560 no reemplaza a 580 y 800 no reemplaza a 910.

La propuesta es conservar los Vs30 del documento, especialmente los 220 m/s sustentados por los SCPT, y obtener mediante el CLI Hazard los productos exactos faltantes bajo el mismo modelo auditado. Antes de ejecutarlo hay que aprobar el alcance de esas condiciones adicionales y comprobar qué pasos públicos hacen falta; no se presupone que baste un postproceso ni se lanza una nueva corrida desde este plan. Los productos actuales y Newmark permanecen preservados. Una alternativa es cambiar las columnas a la grilla actual, pero requiere una decisión técnica expresa y no debe alterar los Vs30 medidos de la sección geotécnica.

Las tablas espectrales de Diana también contienen períodos ausentes de la grilla vigente, por ejemplo 0.07, 0.17, 0.80 y 1.20 s; la grilla auditada contiene, entre otros, 0.075, 0.180, 0.750/0.850 y 1.250 s. La propuesta es regenerar las tablas y curvas con los períodos del modelo, conservando su estructura editorial. No renombrar ni interpolar ordenadas silenciosamente.

La comparación mantiene las correspondencias ya aceptadas 475/500 y 2475/2500, sin recálculo para reproducir los rótulos. La matriz de sustitución registrará también la fila 975 y su correspondencia propuesta con 1000 antes de ejecutarla. Media y percentil 50 son distintos; tampoco se intercambiarán P84, P90 y P95.

## Lugares que deben reconciliarse

Los localizadores siguientes se leyeron en la extracción pública pdf2md del Word original; son números editoriales, no páginas físicas. La entrega de taludes preservó el contenido de Hazard. Antes de editar, se reubicarán sus anclas en la copia `_AVK`.

| Lugar de Diana | Acción propuesta | Evidencia leída |
|---|---|---|
| Capítulo 6, figuras 6-1 a 6-8 | Reemplazar curvas AEP y UHS para Vs30 1500/760, conservando media/P84 y las demandas correspondientes. | Extracción, líneas 921–961. |
| Capítulo 6, figuras 6-9 a 6-13 y «Controlling Scenarios» | Cotejar la desagregación vigente y actualizar figuras y afirmaciones sobre magnitud/distancia sólo si lo sustentan sus productos. No deducirlos de una tabla PGA. | Líneas 983–999. |
| Capítulo 7, figuras 7-7 y 7-8 | Actualizar UHS a Vs30 220 cuando exista el producto exacto. Conservar SCPT, perfiles, tabla 7-3 y clasificación de sitio. Revisar la compatibilidad de la explicación de amplificación con el método vigente. | Líneas 1063–1123. |
| Capítulo 8, figuras 8-1 a 8-3 | Actualizar la serie del proyecto en la comparación con NRC. Preservar la referencia NRC y su procedencia; revisar la frase «good agreement» después del cotejo. No sustituir las curvas de referencia por resultados del proyecto. | Líneas 1125–1158. |
| Capítulo 9, tablas 9-1 y 9-2 | Reemplazar PGA por llave sitio, ID de producto, Vs30, TR y estadístico; mantener g y la precisión editorial. | Líneas 1168–1216. |
| Capítulo 9, tablas 9-3 y 9-4 y figuras 9-1 a 9-4 | Reemplazar espectros y ordenadas de TR10000 y TR2475/2500; verificar PGA como Tn=0, media y P84, Vs30 y grilla de períodos. | Líneas 1218–1390. |
| Resumen ejecutivo, párrafo después de tabla 9-2 y conclusiones | Reconciliar todas las repeticiones de PGA, demandas y resultados. Mantener las frases de Diana con valores procedentes de R. | Líneas 180–181, 1216 y 1603. |
| Apéndices C1 y C2 | Reemplazar las familias de AEP/UHS de las cinco condiciones y sus estadísticos; evitar que el anexo conserve la generación vieja. C1 repite una imagen bajo captions P84/P90 y un caption P90: verificar identidad real, no guiarse sólo por su número. | Tramo de apéndices leído, líneas 1960–2194. |
| Apéndice D1, tablas D1-1 a D1-5 | Reconciliar PGA media, P50, P84, P90 y P95, usando la misma matriz que las tablas 9-1/9-2. | Líneas 2195–2306. |
| Apéndice D2 | Completar el inventario visual de sus objetos: el texto extraído sólo identifica el encabezado. No se considera cotejado ni se asigna un número de figuras sin inspección. | Líneas 2308 en adelante. |

Los capítulos de metodología no se reescriben por completo. Se revisan las afirmaciones que pudieran quedar incompatibles con los productos nuevos —motor declarado, tratamiento de amplificación y escenarios— y se proponen correcciones puntuales con fuente verificable. No se traslada automáticamente al Word de Diana una sección DSHA/MCE del reporte del proyecto.

## Secuencia de implementación propuesta

1. Congelar hashes de la copia `_AVK`, los Word NGR y las tablas científicas. Crear un candidato separado, sin sobrescribir el original ni la entrega aceptada.
2. Construir una matriz completa de reemplazo: ancla/celda/imagen de Diana, sitio, ID, Vs30, TR, estadístico, Tn, unidad, valor original, dato auditado y recurso NGR. Resolver allí las condiciones y períodos ausentes; no llenar huecos con otra rama (`.oq` o `.site`).
3. Preparar en los sources locales las tablas, figuras y resultados con la redacción de Diana. `_chapters/` conserva prosa; `_results/` y `_captions/` generan los valores con R. Reutilizar los builders existentes y adaptar sólo la presentación que el destino requiera.
4. Renderizar mediante NGR un documento de transferencia con todas las figuras embebidas y las tablas seleccionadas. El Word completo actual remite parte de las figuras a anexos HTML, por lo que copiar sólo ese DOCX no cubre todo el alcance.
5. Trasladar esos objetos y los fragmentos variables al candidato de Diana preservando estilos, marcadores, captions y referencias. Dejar intacto el capítulo 10 ya entregado, salvo una dependencia numérica demostrada y resuelta expresamente.
6. Verificar las celdas contra los datos y las curvas contra sus series; comprobar duplicados entre cuerpo, resumen, conclusiones y anexos. Renderizar el candidato para QA visual de todas las páginas afectadas y comprobar que las secciones fuera del alcance no cambiaron.
7. Entregar el Word actualizado y una relación de cambios por tabla/figura/párrafo, con los hashes y límites de revisión. Acordar el nombre de la nueva revisión antes de sustituir una entrega.

## Builders y límites comprobados

Se leyeron `_master/docx.en.qmd`, `_docx/sha.qmd`, `_docx/sdc.qmd`, `_book/psha.qmd`, `_book/executive.site.qmd`, `_tbl/PGA.TR.qmd`, `_tbl/PSA.qmd`, `_fig/AEP.qmd`, `_fig/AEPS.qmd`, `_results/hazard.results.qmd`, `_results/hazard.uncertainty.qmd` y `_results/site.results.qmd`.

`_tbl/PGA.TR.qmd` toma `SaF` de UHSTable para la selección de ID/sitio/Vs30/TR; presenta las medias y agrega P84 para MDE, no una matriz completa de percentiles para todos los TR. `_tbl/PSA.qmd` usa por defecto Vs30=800 y cm/s² en DOCX. Esos defaults no representan las cinco columnas de Diana: la transferencia debe fijar explícitamente los destinos y unidades correctos. `_fig/AEP.qmd` y `_fig/AEPS.qmd` son bloques HTML; su existencia no acredita una figura embebida en Word.

La extracción consultada está en `/private/tmp/claude-501/-Users-averrik-Cloud-github-projects-AR-M2V4D/bc6bc387-e4e1-4ab5-a8cb-3e5e18735788/scratchpad/pdf2md-crawford-final-20261015/out/CAPR003324_Crawford_SeismicHazard_Final.md`. Es auxiliar de esta sesión; para ejecutar el plan se reutilizará si sigue disponible o se obtendrá otra extracción por la CLI pdf2md, preservando el DOCX original.

Quedan por decidir la obtención de Vs30 exactos faltantes, la presentación de la grilla espectral y el nombre de la nueva revisión. Hasta entonces este plan no se considera autorización para producir datos nuevos ni modificar Hazard en la entrega de Diana.
