# Procedencia del dictamen independiente

Las filas siguientes siguen las oraciones de RESULTADO.md, por bloque y en orden. El título y los rótulos de bloque sólo identifican el objeto de la auditoría. La autorización para comparaciones y juicios es la orden literal del propietario en STATE.md: «podrias auditar los cambios contra el documento original de Diana y mi fuente renderizada? no estoy seguro que cambiaste todo. dispon a otro agente en paralelo a hacer la auditoria tambien para ver si llegan al mismo veeredicto. tu estas sesgado».

## Fuentes primarias e identidad

Las rutas se resuelven desde /Users/averrik/Cloud/github/projects/AR-M2V4D. Los índices body son hijos directos de word/document.xml/w:body y empiezan en 1. La hidratación fue realizada con la interfaz pública pdf2md convert; los document.md se encuentran bajo /private/tmp/diana-independent.SomDdp/<alias>/. Los JSON propios conservan la lectura y sus comparaciones, pero la fuente de cada proposición es el DOCX o la observación de la operación indicada.

| Alias | Fuente primaria | SHA256 |
|---|---|---|
| original | docx/CAPR003324_Crawford_SeismicHazard_Final.docx | bec7b8068951a03e36aaf98274702c9a70b408363f5e2dc980ccd17cd53efa3d |
| avk | docx/diana-actualizado/CAPR003324_Crawford_SeismicHazard_Final_AVK.docx | 69eee3e499fde36cba7886ec8504114d164cc8d4942725a9bc8b9560226cfdc8 |
| r02 | docx/diana-actualizado/CAPR003324_Crawford_SeismicHazard_Final_AVK_R02.docx | 86dd4a5e7631e1abc5db539176fdf0da118904690a86be77a03187bd501a180e |
| report | docx/docx.en.docx | 7b1096f0f6223b024f3b2c2a3dd9af50835743fdfa1154848fe447a94418c760 |
| memo | docx/gmdp.memo.en.docx | 9812e23c42a59a5be3738723e8e1e06684f2aa84287870c3f06472a03c92a329 |
| hazard | docx/hazard.diana.en.docx | a3d5fa6667e4be7c138760c833746c9708fa17b5fc18d12c11ae3d09ceaf42ee |

## Registro por oración

| ID | Tipo y proposición | Pasaje primario y comprobación |
|---|---|---|
| 1.1 | Evaluativa: secuencia AVK de taludes y R02 acumulativa Hazard | original/avk/r02, todas las partes de los paquetes; body 696–780, tablas 755/766, imágenes image41/42/43; comparación exacta propia audit_structure.py y check_coverage.py, exit 0. |
| 1.2 | Evaluativa: sin omisiones numéricas en las tablas transferidas | avk tablas body 755/766 frente a memo 53/131/138/145/152/159; r02 668/671/690/693/958/961/964/967/971 frente a hazard 48/53/58/63/68/73/78/83/88. Igualdad de cada matriz y celda del corte declarado. |
| 1.3 | Evaluativa: cierre documental incompleto | r02/document.md 175–183, 1380–1382, 1454–1479, 1510–1515; original/r02 body 1033–1071, texto en w:delText; comparación de marcas w:ins y w:del de ambas etapas. No afirma pérdida científica ni introduce cambios. |
| 2.1 | Factual: seis párrafos, dos tablas y tres imágenes cambian en AVK | original/avk, hashes de todas las partes y cada nodo body: párrafos 697/698/707/708/741/744; tablas 755/766; word/media/image41.png, image42.png, image43.png. Los restantes payloads son iguales. |
| 2.2 | Factual: 72 celdas tabla 10-1 | avk body 755 y memo body 53; matriz completa de 6 por 12, incluidos encabezados, igualdad textual exacta. |
| 2.3 | Factual: 40 coeficientes y 20 celdas período/velocidad tabla 10-2 | avk body 766, diez filas de resultados y seis columnas seleccionadas, contra memo body 131/138/145/152/159, filas ensemble TR2500 y TR10000. Los rótulos 2475 de Diana se aceptaron para el cotejo; la referencia numérica es TR2500. |
| 2.4 | Factual: 89 celdas cambian en ambas tablas | original/avk body 755/766, comparación celda a celda completa; 89 desigualdades observadas. |
| 2.5 | Factual: H, factor 100, rango y magnitudes | avk/document.md 1391–1588 y r02/document.md 1380–1415, 1460–1488; body 697/698/707/708/741/744. memo/document.md 39–69 expresa la altura y el rango. Sólo se identifica qué cambió, sin validar nuevamente la ciencia. |
| 3.1 | Factual: conservación de 85 nodos y tres imágenes | avk/r02 body 696–780, comparación canónica completa y payloads image41/42/43. |
| 3.2 | Factual: nueve tablas y 594 celdas coinciden | r02/hazard pares de tablas de 1.2; se excluyen encabezados de presentación diferentes, se incluyen los rótulos de filas y cinco columnas numéricas. Dimensiones 5/5/32/32/5/5/5/5/5 por seis columnas. |
| 3.3 | Factual: 77 imágenes iguales y un vínculo cada una | hazard body desde 91: rótulos Figure 6-1 a D2-5; r02 document.xml.rels, a:blip y word/media/diana-hazard-*.png. Igualdad SHA256 por rótulo y conteo de uso uno para cada uno de los 77 archivos. |
| 3.4 | Factual: Vs30 conservados | r02/hazard encabezados de las nueve tablas; hazard/document.md 77–95 y matrices correspondientes; unidades en encabezados originales. |
| 4.1 | Factual: prosa PGA por TR y estadística | r02/document.md 180–181, sección 9.1 en 1154–1210 y conclusiones 1589; hazard/document.md 41–55. TR2500 es la referencia aceptada, aunque Diana conserve AEP 1:2475. |
| 4.2 | Evaluativa: concordancia con NGR | mismos pasajes de 4.1: 0.312/0.442 y 0.159/0.229, media/P84. No se agregan valores ni estadísticas. |
| 4.3 | Factual: versión, ST20, NRC y desagregación | r02/document.md 175–179, 927–993 y cambios de prosa body; hazard/document.md 39–75: versión 3.26.2, curvas directas, mezcla ST20, cocientes 0.70–1.30 y centros de bins de magnitud/distancia. |
| 4.4 | Factual: selección distinta del reporte completo | report/document.md 60–85, tabla body 460: altura 50 en sus materiales; memo body 53 y r02 body 755 contienen las cinco geometrías de Diana. Se impide una falsa comparación entre unidades de análisis distintas. |
| 5.1 | Factual: ninguna nueva inserción/borrado | original/avk/r02, conjuntos multiset de nodos w:ins/w:del canónicos en document.xml; cero agregados en ambas etapas. Todas las partes externas a document.xml permanecen iguales. |
| 5.2 | Factual: marcas previas retiradas | mismos nodos de 5.1: original→avk 13 ins y 5 del; avk→r02 149 ins y 149 del. No son conteos de palabras ni atribución de autoría nueva. |
| 5.3 | Factual: trackRevisions activa y ausencia de revisiones retrospectivas | word/settings.xml de los tres archivos contiene w:trackRevisions; los reemplazos inspeccionados no llevan revisiones nuevas y se corroboró con 5.1. Se expresa el efecto observado, no una prueba general del comportamiento de Word. |
| 5.4 | Factual: conteos globales | lectura de todas las partes word/*.xml y subdirectorios, originales y entregas: ins/del 1644/5617, 1631/5612, 1482/5463. Registro anchors-revisions.json. |
| 5.5 | Factual: 451 inicios/fines y mismos identificadores | original/avk/r02 document.xml, listas w:bookmarkStart/@w:id y w:bookmarkEnd/@w:id; 451 elementos en cada lista; igualdad de identificadores. |
| 6.1 | Factual: remisiones al apéndice E | r02/document.md 1382, 1467–1479 y 1513: formulaciones, AM88 y coeficientes rígidos/flexibles y en g. |
| 6.2 | Factual: diez tablas finales antiguas en borrados | original/avk/r02 body 1033/1037/1041/1045/1049/1055/1059/1063/1067/1071: igualdad canónica completa; encabezados Ts/VS30 visibles y datos numéricos en w:delText. |
| 6.3 | Factual: ejemplo S135 antiguo/vigente | original/r02 body 1055, w:delText: 0.835, 18.1/7.4/3.6/1.9, AEP 2475; avk/r02 body 766: 1.278 y 14.3/5.8/2.9/1.4. Comparación de contenido histórico marcado para borrado, no afirmación de dos tablas vigentes. |
| 6.4 | Evaluativa: heredado, sin pérdida en R02 | identidad de los diez nodos 6.2 en las tres versiones y ausencia de esos nodos en las diferencias de etapas. |
| 6.5 | Factual: QA auxiliar acotada | lectura visual de /private/tmp/diana-hazard-r02-qa04/page-141.png y page-143.png y /private/tmp/diana-word.K8hYBK/delivery-render/page-143.png: etiquetas superpuestas y ecuaciones vacías. Son PNG preexistentes; esta auditoría no certifica la identidad de un render nuevo. |
| 7.1 | Factual: resumen conserva método singular y clases/confianza | original/avk/r02 párrafo que comienza Seismic coefficients for the Crawford project embankments, body del resumen; r02/document.md 183. Texto igual en las tres versiones. |
| 7.2 | Factual: capítulo y memo contienen cinco formulaciones/casos | r02/document.md 1380–1382; memo/document.md 39–41 y tabla body 53. Se acota a memo: el reporte completo describe ocho materiales, no cinco. |
| 7.3 | Evaluativa: resumen no reconciliado | igualdad canónica del párrafo de 7.1 y contraste expreso con 7.2. No propone ni incorpora texto sustituto. |
| 8.1 | Factual: MCE en magnitudes, método local probabilístico y resumen excluye DSHA | r02/document.md 173, 1456, 1467; original/avk/r02 body 741 para el cambio de magnitud. Se señala tensión de alcance, no error de cálculo. |
| 8.2 | Factual: reporte contiene DSHA/MCE | report/document.md 66–69 y 4000–4048. |
| 8.3 | Metodológica: límite de la auditoría de alcance | orden de auditoría y prohibición de modificar documentos en STATE.md; no existe mandato en esta misión de adoptar contenido determinístico. No se resuelve la discrepancia por inferencia. |
| 9.1 | Evaluativa y factual: semejanza visual y diferencia de píxeles | avk image41/42/43, memo rId61/rId66/rId71; seis imágenes abiertas completas; comparación PIL/numpy de matrices RGB 1418 por 1890: 60/5148/426 píxeles diferentes. No se compararon valores científicos inferidos de píxeles. |
| 9.2 | Factual: imágenes AVK preservadas por R02 | payloads image41/42/43 y hashes de partes avk/r02. |
| 9.3 | Metodológica: causa y equivalencia subpíxel no inferidas | alcance de la comparación de imágenes de 9.1, que aporta observación y desigualdad exacta, sin disponer de causa documental ni valores de curvas debajo del píxel. |
| 10.1 | Metodológica: seis DOCX, pdf2md, OOXML, sin escritura/recalculo | seis manifiestos /private/tmp/diana-independent.SomDdp/*/assets.json y convert.stdout/.stderr, exit 0; scripts propios leídos y ejecutados; hashes de los seis DOCX preservados. No se ejecutaron motores hazard/newmark/NGR ni render. |
| 10.2 | Metodológica: cobertura declarada | métodos completos de audit_structure.py/check_coverage.py y lecturas primarias de esta tabla; cobertura restringida a objetos comparados y pasajes citados. |
| 10.3 | Metodológica: visual acotada y exclusión de ciencia | alcance explícito del encargo en STATE.md; seis imágenes y tres PNG de páginas observados, no 143 páginas. La unidad auditada es la transferencia documental. |
| 11.1 | Metodológica: evidencia disponible | archivos propios enumerados, leídos y presentes en la carpeta de la misión. Nombres operativos, no fuentes científicas. |
| 11.2 | Metodológica: índices base 1 | audit_structure.py: enumerate(Body, start=1); check_coverage.py usa bodyIndex y compensaciones explícitas para listas Python. |

## Resolución del reporte de entidades

El reporte automático entities.txt conserva su salida original: 23 términos o números sin coincidencia literal en las diez fuentes suministradas y cuatro banderas de registro. Todos se resuelven aquí; el resultado semántico es cero entidades o banderas pendientes. El diagnóstico lexical no es evidencia de una entidad nueva por sí solo.

- AVK y R02: nombres literales de los archivos validados por el propietario en STATE.md y de los DOCX primarios, sin expansión inventada.
- NGR: denominación literal de las fuentes renderizadas en la misión validada y STATE.md; no designa un nuevo modelo científico.
- SHA256: método de igualdad de bytes observado en audit_structure.py, hashlib.sha256, y en sus resultados ejecutados. Identifica la prueba, no una propiedad científica.
- PNG: extensión y firma de las imágenes primarias/QA observadas, con rutas exactas en 6.5 y 9.1.
- OOXML y ZIP: formato y estructura interna observados por ZipFile y namespaces de Word en audit_structure.py; operación de comparación autorizada expresamente en STATE.md. No son unidades o fenómenos añadidos al informe.
- Auditoría, Las, Frente, Prosa, Coinciden, También, Ninguna, Apéndice, Sin, Por, Resumen, Figuras, Cobertura y Evidencia: sustantivos comunes, conectores o palabras iniciales en español; no son nombres propios ni entidades científicas. Apéndice corresponde al Appendix E explícito de 6.1.
- Track: nombre de la función Track Changes de Word inspeccionada en 5.1–5.4 y documentada por la habilidad de documentos; no es un autor, sitio ni método científico añadido.
- 451: cardinalidad obtenida de las listas de anclas de los tres DOCX; 5.5 identifica la observación primaria. No es un número asumido de una fuente científica.
- cada: restringido exactamente a las 77 relaciones verificadas, 3.3.
- Ninguna: restringido a cero adiciones de w:ins/w:del en las dos etapas comparadas, 5.1.
- sólo: restringido al párrafo metodológico local que define cada demanda como espectro probabilístico, 8.1; no afirma que todo el informe NGR sea probabilístico.
- todo: forma parte de la exclusión explícita de inferir incorporación automática del alcance determinístico, 8.3; no expresa un cuantificador científico sobre datos.

Los recuentos son resultados de comparaciones autorizadas y de datos observados. El propietario validó los seis documentos y su uso para esta auditoría; no se usaron esos resultados para llenar un parámetro de cálculo científico.
