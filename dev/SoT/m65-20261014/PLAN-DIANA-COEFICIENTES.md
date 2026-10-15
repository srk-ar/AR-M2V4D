# Plan de actualización del capítulo de coeficientes sísmicos de Diana

Fecha: 2026-10-15. Entrega de identificación y plan; no se ha editado el Word ni las fuentes del informe durante este cotejo.

## Alcance y método fijados por el propietario

El objeto es el capítulo 10, «Slope Design Parameters», del archivo [de Diana](/Users/averrik/Cloud/github/projects/AR-M2V4D/docx/CAPR003324_Crawford_SeismicHazard_Final.docx). Se actualizan sus resultados de coeficientes sísmicos y las fórmulas necesarias, conservando su redacción mejorada. Todo el contenido de Hazard queda fuera. La coincidencia de Hazard se toma como contexto dado por el propietario; este plan no la vuelve a auditar.

La secuencia es **datos auditados → fuentes → render → actualización del capítulo de Diana**. Toda modificación textual se resuelve primero en los sources para que sea reproducible. Está prohibido pegar cifras en la prosa o corregirlas directamente en Word: los valores variables se obtienen mediante expresiones R de los bloques de resultados y el mecanismo de leyendas. Las cifras consignadas abajo son evidencia del cotejo, no texto para pegar en el informe.

El propietario resolvió expresamente que 475/500 y 2475/2500 no constituyen un conflicto. Se utilizan las demandas de los productos vigentes; no se interpolan resultados, no se recalcula y no se abre una tarea de renombrado por esas diferencias.

## Evidencia y separación de las fuentes

Se leyó completo el [capítulo extraído con pdf2md](/Users/averrik/Cloud/github/projects/AR-M2V4D/docx/CAPR003324_Crawford_SeismicHazard_Final.slope-design-parameters.md), desde «Slope Design Parameters» hasta antes de «Conclusions». Sus líneas son los localizadores de este plan; no son páginas físicas de Word. Se leyeron los masters y bloques que producen los resultados, la procedencia, los contratos de ambas corridas y el mapa de combinación. También se convirtió el memo Word actual mediante pdf2md 1.0.0 y se cotejaron sus tablas con los RDS publicados.

Identidades observadas:

| Insumo | SHA-256 |
|---|---|
| Word original de Diana | `bec7b8068951a03e36aaf98274702c9a70b408363f5e2dc980ccd17cd53efa3d` |
| `docx/gmdp.memo.en.docx` | `c861b12bbfe331c32175c280078d565c810c6906a471421d6bc57f43eba701f6` |
| `data/newmark/ShearTable.Rds` | `334359667159dd8f928c54d4f40484af1162372a0e4114aee666691104b3cf29` |
| `data/newmark/kmaxTable.Rds` | `32653b7158e0a8899e9ac16313124d5a3dc27a112428a386216adcacf99a3fc5` |

Los hashes de los dos RDS coinciden con [PROCEDENCIA.md](/Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark/PROCEDENCIA.md). La lectura por data.table produjo cinco filas de propiedades y cuarenta celdas de coeficientes seleccionados, sin ausencias ni duplicados en sus claves.

La estructura real revisada del scaffold está en `/Users/averrik/Cloud/github/libraries/reports/sha/`; la ruta histórica `/Users/averrik/github/reports/sha` no existe en este equipo.

| Capa | Función observada y tratamiento previsto |
|---|---|
| `_chapters/` | Metodología, símbolos, ecuaciones y redacción reutilizable. Conservar aquí las mejoras editoriales de Diana y las correcciones metodológicas; las afirmaciones de resultados específicos deben quedar servidas por los bloques de resultados. |
| `_results/` | Párrafos parametrizados con R: selección de modelos, magnitudes, demandas, cantidades de escenarios y rangos. Se revisaron `dn.inputs.qmd`, `dn.results.qmd`, `ts.results.qmd` y `kmax.results.qmd` tanto en el proyecto como en el scaffold. |
| `_captions/` | Plantillas de leyendas con marcadores de formato. `readCaption()` lee la plantilla y los bloques consumidores suministran los valores. Se revisaron las leyendas de `kh` y `Ts` y sus consumidores locales. |
| `_local/gmdp.memo.en.qmd` | Contiene copias de prosa y expresiones R, no inclusiones dinámicas de todos los capítulos. Sus comentarios `sources` no sincronizan el texto. Debe consumir los resultados parametrizados y conservar la redacción concordada; corregir sólo `_chapters/` no basta. |
| `_local/tbl.Ts.qmd`, `_local/tbl.kh.one.qmd`, `_local/fig.kh.one.qmd` | Construyen los objetos específicos del memo con los pares de geometría/material del capítulo. Los builders toman los valores de las tablas publicadas. |

El [master general](/Users/averrik/Cloud/github/projects/AR-M2V4D/_master/docx.en.qmd) incorpora varias secciones ajenas a este alcance. Su bloque `_docx/gmdp.qmd` remite a figuras mediante notas a los decks y utiliza una tabla de coeficientes MCE. Por eso su salida no es un sustituto directo de las tablas y figuras del capítulo de Diana. El [memo local](/Users/averrik/Cloud/github/projects/AR-M2V4D/_local/gmdp.memo.en.qmd) sí genera los cinco pares y las figuras necesarias.

## Qué y dónde corregir

Los enlaces de la primera columna abren el lugar del capítulo extraído. Los reemplazos se producirán desde las fuentes indicadas, no mediante edición numérica manual del Word.

| Lugar de Diana | Hallazgo | Cambio que debe producir la cadena de fuentes y render |
|---|---|---|
| [Ecuación 10-1 y definición posterior, líneas 21–23](/Users/averrik/Cloud/github/projects/AR-M2V4D/docx/CAPR003324_Crawford_SeismicHazard_Final.slope-design-parameters.md:21) | La expresión todavía usa la altura del talud en el numerador; el proyecto ya usa la altura desde el ápice. | Trasladar la ecuación corregida y su definición de altura desde `_chapters/ts.model.md:4,7` y el correspondiente bloque del memo. Conservar la redacción restante. |
| [Párrafo posterior a ecuación 10-6, línea 43](/Users/averrik/Cloud/github/projects/AR-M2V4D/docx/CAPR003324_Crawford_SeismicHazard_Final.slope-design-parameters.md:43) | La fuente actual explica que el exponente se ajusta desde la cresta y que usarlo en la ecuación característica referida al ápice es una aproximación. Esa precisión no está en este párrafo de Diana. | Reconciliar sólo esta precisión técnica, ya presente en `_chapters/ts.model.md:37` y el memo:112, con su frase. No sustituir todo el desarrollo del modelo. |
| [Tabla 10-1, líneas 119–132](/Users/averrik/Cloud/github/projects/AR-M2V4D/docx/CAPR003324_Crawford_SeismicHazard_Final.slope-design-parameters.md:119) | Cambian propiedades dinámicas y períodos de los cinco pares. | Regenerar las filas desde `ShearTable.Rds`, estadístico `mean`, con la selección de `_local/gmdp.memo.scenarios.csv`; el bloque existente es `_local/tbl.Ts.qmd`. Preservar orden, identidad y formato de la tabla de Diana. |
| [Primer párrafo, línea 5](/Users/averrik/Cloud/github/projects/AR-M2V4D/docx/CAPR003324_Crawford_SeismicHazard_Final.slope-design-parameters.md:5) | El rango de períodos pertenece a los resultados anteriores. | Expresar el rango mediante R a partir de las mismas filas seleccionadas para la tabla. El memo ya obtiene mínimo y máximo de `Periods` en sus líneas 36–45; conservar esa selección, sin sustituirla por el rango de todas las combinaciones del informe general. |
| [Introducción y párrafo posterior a ecuación 10-13, líneas 7 y 92](/Users/averrik/Cloud/github/projects/AR-M2V4D/docx/CAPR003324_Crawford_SeismicHazard_Final.slope-design-parameters.md:7) | La declaración de una magnitud constante no describe los productos combinados vigentes. También persiste en nuestros sources y en el memo renderizado. | Obtener la relación demanda–magnitud de la procedencia auditada y renderizarla mediante un bloque de `_results/`. Conservar el resto de la frase de Diana. No sustituir una cifra fija por otras cifras fijas. |
| [Ecuación 10-15 y unidades, líneas 98–100](/Users/averrik/Cloud/github/projects/AR-M2V4D/docx/CAPR003324_Crawford_SeismicHazard_Final.slope-design-parameters.md:98) | La ecuación muestra un cociente, mientras tablas, figuras y texto expresan porcentaje de PGA. El scaffold actual ya explicita el factor de conversión a porcentaje. | Reconciliar la notación en `_chapters/dn.model.md`, su copia del memo y las leyendas. Los productos guardan `Kh` con unidad `ratio`; los builders ya convierten a porcentaje. No modificar esos valores ni aplicar la conversión dos veces. |
| [Tabla 10-2, líneas 148–175](/Users/averrik/Cloud/github/projects/AR-M2V4D/docx/CAPR003324_Crawford_SeismicHazard_Final.slope-design-parameters.md:148) | Las cuarenta celdas de coeficientes y las columnas de período y velocidad corresponden a la generación anterior. | Producir la tabla resumida mediante R con los pares existentes, `ensemble`, `mean`, las dos demandas de esa tabla y los cuatro umbrales ya adoptados. Reutilizar selección y unidades del builder; no transcribir valores del plan al Word. |
| [Figuras 10-1, 10-2 y 10-3, líneas 177–199](/Users/averrik/Cloud/github/projects/AR-M2V4D/docx/CAPR003324_Crawford_SeismicHazard_Final.slope-design-parameters.md:177) | Los gráficos insertados contienen las curvas anteriores. | Reemplazar sus imágenes por las figuras correspondientes del render de los sources actualizados, usando `_local/fig.kh.one.qmd` y los productos vigentes. Conservar la identidad de las figuras, sus remisiones y la redacción de sus captions. |

No se abre una nueva corrección de los umbrales de desplazamiento, la cantidad de realizaciones, las geometrías o la asociación de materiales: el cotejo usa las selecciones ya existentes del capítulo. Los artefactos de extracción de fórmulas o notas no se consideran errores de Word sin comprobarlos en el documento.

## Magnitudes: corrección del consumidor de resultados

La [procedencia](/Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark/PROCEDENCIA.md), el [mapa de combinación](/Users/averrik/Cloud/github/projects/AR-M2V4D/dev/SoT/m65-20261014/magnitude-map.csv) y los contratos [M55](/Users/averrik/Cloud/github/projects/AR-M2V4D/newmark-M55.json) y [M65](/Users/averrik/Cloud/github/projects/AR-M2V4D/newmark-M65.json) documentan las magnitudes distintas por demanda. No hay una magnitud única para estos resultados.

El problema localizado en el render es la lectura de un escalar: `scripts/setup/setup.R:48` obtiene `Mw.gmdp` de `newmark.json`, y varias plantillas lo presentan como constante para todas las demandas. Los productos combinados no contienen una columna `Mw` en `kmaxTable.Rds`; no se puede inferir la magnitud de los coeficientes ni del nombre de una carpeta.

La corrección prevista es conectar el bloque de resultados a la relación auditada entre demanda, corrida de origen y valor del contrato de esa corrida. Ese vínculo debe formar parte de los datos de procedencia accesibles al render, con cobertura completa de las demandas presentadas. Las fórmulas R deben construir el texto desde ese vínculo. No se cambia el contrato de cálculo para maquillar la narración, no se añade una magnitud por defecto y no se vuelven a ejecutar las corridas.

Puntos concretos que deben dejar de afirmar una magnitud constante:

- [_results/dn.inputs.qmd:12](/Users/averrik/Cloud/github/projects/AR-M2V4D/_results/dn.inputs.qmd:12): declaración de entradas usadas.
- [_results/dn.results.qmd:7](/Users/averrik/Cloud/github/projects/AR-M2V4D/_results/dn.results.qmd:7): resumen de desplazamientos.
- [_chapters/dn.model.md:7](/Users/averrik/Cloud/github/projects/AR-M2V4D/_chapters/dn.model.md:7): separar la explicación metodológica de la selección particular de magnitudes, que debe comunicar el bloque de resultados.
- [_local/gmdp.memo.en.qmd:53](/Users/averrik/Cloud/github/projects/AR-M2V4D/_local/gmdp.memo.en.qmd:53) y línea 200: consumir la misma información parametrizada, conservando la frase editorial que corresponda.

Hay afirmaciones equivalentes en el memo español, líneas 53 y 194. Quedan identificadas para mantener la coherencia del proyecto; la actualización del Word de Diana se prepara en inglés y no exige traducir sus mejoras editoriales al español.

## Valores observados para cotejar el render

Estas tablas registran resultados leídos, no son una nueva entrada del cálculo ni una fuente de constantes para el texto.

La tabla de propiedades actual reproduce las filas seleccionadas de `ShearTable.Rds` y la tabla 2 del memo renderizado. Las columnas de geometría y clasificación se conservan; las propiedades que se cotejarán son:

| Escenario / material | T_s de Diana → actual [s] | m_o actual | a_1 actual | G_o actual [MPa] | V_S^o actual [m/s] | V_S30 actual [m/s] |
|---|---:|---:|---:|---:|---:|---:|
| S135 / U1 | 0.835 → 1.278 | 0.484 | 3.6538 | 263.8 | 368.8 | 194.0 |
| S50 / U2 | 0.377 → 0.526 | 0.479 | 3.3699 | 213.4 | 324.7 | 218.0 |
| S32 / U3 | 0.308 → 0.392 | 0.464 | 3.1306 | 147.6 | 271.3 | 205.7 |
| S27 / U4 | 0.187 → 0.219 | 0.546 | 3.1036 | 365.1 | 400.1 | 309.9 |
| S35 / U5 | 0.280 → 0.305 | 0.506 | 2.9528 | 272.7 | 353.1 | 251.6 |

El rango que genera el memo con esos pares es 0.22–1.28 s; Diana conserva 0.19–0.83 s. El formato se aplica con R sobre los resultados, no escribiendo este rango en el source.

Para la tabla 10-2, estos son los valores actuales de `100 * Kh`, redondeados como el builder a un decimal, para `p = mean` e `IDn = ensemble`. Se cotejaron con las tablas 8–12 del memo. La correspondencia de rótulos de retorno ya fue resuelta por el propietario.

| Escenario | TR del producto [años] | 0.1% | 0.4% | 1.0% | 2.5% |
|---|---:|---:|---:|---:|---:|
| S135 | 2500 | 14.3 | 5.8 | 2.9 | 1.4 |
| S135 | 10000 | 18.6 | 8.5 | 4.3 | 2.3 |
| S50 | 2500 | 25.2 | 11.4 | 5.6 | 2.6 |
| S50 | 10000 | 32.5 | 17.4 | 9.8 | 4.8 |
| S32 | 2500 | 33.1 | 16.6 | 8.8 | 4.2 |
| S32 | 10000 | 41.5 | 23.5 | 14.3 | 7.5 |
| S27 | 2500 | 39.4 | 20.4 | 11.2 | 5.2 |
| S27 | 10000 | 49.3 | 27.9 | 17.3 | 9.3 |
| S35 | 2500 | 33.3 | 16.2 | 8.4 | 3.8 |
| S35 | 10000 | 42.6 | 23.6 | 14.1 | 7.2 |

Correspondencias de las imágenes extraídas por pdf2md:

| Diana | Imagen anterior | Figura del memo actual | Imagen actual |
|---|---|---|---|
| Figura 10-1 | `image41.png` | Figura 5, kh, primera demanda | `rId61.png` |
| Figura 10-2 | `image42.png` | Figura 6, kh, segunda demanda | `rId66.png` |
| Figura 10-3 | `image43.png` | Figura 7, kh, MDE | `rId71.png` |

Se abrieron visualmente `image42.png` y `rId66.png`: muestran las mismas familias y escenarios con curvas distintas. El cotejo visual completo de las tres figuras y de las páginas del Word será parte de la ejecución. Los nombres de medios son localizadores de esta extracción, no identificadores que deban suponerse estables después de otro render.

## Secuencia de ejecución propuesta

1. **Fijar la base editorial y los datos.** Conservar el Word original y las identidades de los productos. Reutilizar el mapeo B y el log de sus 54 bloques aplicados; no reaplicar el parche. Comparar el remanente de redacción con Diana por pasaje, sin revertir correcciones técnicas.
2. **Corregir las fuentes por su función.** Mantener metodología y fórmulas en `_chapters/`; expresar las selecciones y resultados mediante R en `_results/`; conservar las leyendas como plantillas con valores suministrados por los builders. Integrar la redacción de Diana en esas plantillas. El memo debe consumir los mismos resultados parametrizados, sin una segunda declaración numérica independiente.
3. **Resolver el consumidor de magnitudes y la tabla resumida.** Hacer accesible al render la procedencia por demanda ya auditada y utilizarla en las frases señaladas. Producir mediante R la disposición de la tabla 10-2 de Diana, seleccionando los mismos datos que las tablas de kh existentes. No copiar sus cuarenta cifras manualmente ni alterar la población de escenarios.
4. **Reconciliar las fórmulas.** Mantener la altura desde el ápice en el período y su precisión metodológica; hacer coherente la normalización porcentual de kh entre ecuación, unidades y salidas. Comprobar que el factor de porcentaje se aplica una sola vez en la representación y que los RDS permanecen intactos.
5. **Renderizar el alcance afectado mediante NGR.** Generar el capítulo/memo y los objetos de reemplazo desde las fuentes, usando el flujo instalado. Comparar texto renderizado con Diana y resultados con las tablas auditadas. No repetir cálculos de hazard/Newmark ni un render global por inercia.
6. **Actualizar una copia del Word de Diana.** Trasladar los objetos y fragmentos técnicos aceptados que produjo el render, manteniendo estilos, numeración, referencias y redacción. El cuerpo de Hazard permanece fuera de la operación. No usar el informe general completo como sustituto del capítulo.
7. **Verificar y entregar.** Cotejar las celdas y curvas con las fuentes; revisar visualmente las páginas afectadas y sus saltos; comprobar ecuaciones, enlaces y remisiones. Entregar el Word candidato y una lista breve de cambios con su ubicación y procedencia.

## Controles y límites de aceptación

- Ninguna cifra de resultado nueva escrita literalmente en los sources narrativos: cada magnitud, rango, coeficiente y leyenda variable se vincula con datos auditados mediante R o la plantilla existente.
- La declaración de magnitudes coincide con la combinación real, incluyendo cobertura de todas las demandas que se describan; no queda una afirmación global de magnitud constante.
- Las filas de tablas conservan la identidad geometría/material y el estadístico; no se confunden medias con fractiles.
- El capítulo reproduce la redacción de Diana salvo los fragmentos técnicos identificados y revisados desde los sources; no se reescribe todo el capítulo.
- Los documentos y resultados de Hazard no cambian. La integridad de ese contenido se comprobará al construir el Word candidato, diferenciándola de la repaginación que pueda producir el editor.
- Las referencias al Apéndice E se preservan. Sus resultados vinculados requieren un cotejo separado antes de declarar actualizado el informe completo; este inventario cubre el cuerpo del capítulo 10 y no acredita una revisión integral del apéndice.

Al leer el scaffold se observaron modificaciones locales sin commit en `sha/_chapters/dn.model.md`, `sha/_chapters/ts.model.md` y `sha/_captions/fig.kh.md`. Incluyen cambios técnicos además de redacción. No se realizó una hidratación global ni se adoptaron por su sola presencia: la reconciliación debe conservar las mejoras editoriales locales y verificar qué cambios técnicos corresponden a los productos publicados. La promoción al scaffold queda después de verificar la integración local.

Los auxiliares de la extracción actual están en `/private/tmp/diana-coefficients-plan.GxJs0p/` (Markdown del memo, manifiesto y medios). La extracción anterior de Diana se reutilizó desde la ruta que registra `pdf2md-crawford-final-20261015.log`. No se borraron auxiliares ni se modificaron documentos originales.
