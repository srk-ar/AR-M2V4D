# Entrega acumulativa Diana R03 — 2026-10-16

## Archivos

- Documento: `docx/diana-actualizado/CAPR003324_Diana_R03.docx`; SHA256 `b99c80fad1f56c91b82c12304b68a8e33f43a69fe880225e341c14bb0221896b`.
- Comparación original→R03: `docx/diana-actualizado/CAPR003324_Diana_R03_Comparacion.docx`; SHA256 `90ad8e0f05b41b0b9bbb006c31d176c43e9e0b098e7520b3a65636e62eb5b503`.
- Se crearon exclusivamente como archivos nuevos; hashes de original, AVK y R02 reobservados intactos después de copiar.

## Cobertura comprobada

| Superficie | Fuente y comprobación | Resultado |
| --- | --- | --- |
| Nueve tablas de Hazard | `docx/hazard.diana.en.docx`; `verification08.json` y `check_revision_layout.py:74` | 594 celdas coincidentes, incluidos rótulos; 495 aceleraciones. Conserva Vs30 1500, 910, 760, 580 y 220. |
| Figuras de Hazard | Transferencia R02 previamente comprobada contra la fuente NGR; orden y bytes revalidados en R03 | Se conserva la actualización de capítulos 6–9 y apéndices C/D; curvas AEP completas del cálculo directo y espectros/tablas de diseño combinado. |
| Tablas del capítulo 10 | Tabla de propiedades contra memo; tabla de coeficientes idéntica a R02, previamente cotejada con memo | Se conserva la actualización de 40 coeficientes y 20 celdas Ts/Vs30. |
| Apéndice E | Diez tablas contra `docx/gmdp.memo.en.docx`, filtrando sus demandas probabilísticas | 800 celdas, incluidos encabezados, coincidentes; nueve filas por tabla, conjuntos rigid/flexible/ensemble y TR500/2500/10000. El apéndice ya es visible; antes estaba en borrados. |
| Figuras de taludes | Tres figuras del capítulo 10 y tres del apéndice E contra el memo | Seis payloads PNG idénticos a la fuente. |
| Fórmulas del apéndice E | Siete fórmulas OMML contra el memo | Tokens matemáticos iguales después de excluir los marcadores de alineación `&` de la fuente. |
| Prosa revisada | `provenance.md`, `prose-audit.json`, `writing-verdict.json`; organización en archivos `organization-*` | Auditoría de 69 bloques y tres párrafos de organización terminada; ambos `audit.py deliver` emitieron `ready`. Los textos emitidos y candidatos son byteidénticos. |

La revisión actual conserva los resultados de R02 y cierra las omisiones documentales identificadas: resumen de Newmark, alcance probabilístico, apéndice E visible y actualizado, referencia BM19 y recuento de apéndices. Las magnitudes permanecen diferenciadas por demanda. Los resultados corresponden al TR2500 del modelo; los rótulos históricos 2475 de Diana no motivaron interpolación, según instrucción expresa.

## Contenidos no trasladados

- DSHA, resultados MCE/MCER y los productos de diseño estructural asociados: excluidos por la respuesta del propietario «Conservar el alcance probabilístico de Diana».
- Selección de registros y series temporales: pertenecen a otro producto del reporte completo, fuera de los capítulos actualizados de Diana.
- Otras combinaciones de geometría, material o Vs30 del reporte completo: se preservan las condiciones de Diana. El memo suministra las cinco combinaciones de taludes correspondientes; no se igualan celdas de escenarios diferentes por su posición.
- No se sustituyeron las curvas AEP completas del cálculo directo por puntos unidos del producto de diseño; el propietario eligió conservar esas curvas. El método del documento distingue curvas directas de tablas/UHS combinados.

Lecturas primarias de este cierre: reporte completo convertido, `/private/tmp/diana-audit-root.25nVLM/report/document.md:60-100`; memo `document.md:400-446`; transferencia Hazard `document.md:37-80`. El detalle de pasajes del texto revisado está en `provenance.md` y `organization-evidence.md`.

## Comparación y revisión visual

- Comparación05: 3375 revisiones nuevas con autor `Codex revision acumulativa`, identificadores únicos y sin anidamientos del mismo tipo. Las tablas de Hazard aparecen como tabla anterior borrada y tabla nueva insertada para separar sus distintas grillas espectrales.
- El comprobador OOXML verifica que aceptar las nuevas revisiones recupera el texto, tokens matemáticos y las 104 imágenes de R03; rechazarlas recupera el texto y las 101 imágenes del original. No se afirma identidad binaria del archivo ni restauración exacta del formato o del historial previo de revisiones.
- Render mediante `documents/render_docx.py` y LibreOffice incluido en el runtime. R03: 155 páginas; comparación: 217 páginas. No se ejecutó un nuevo render científico NGR ni un recálculo.
- Cobertura R03: revisión06 más comparación pixel a pixel y revisión de páginas 28/29 en 07 (`page-coverage06.json`, `page-differences07.json`). Cobertura comparación05: 191 cuerpos de página pixelidénticos a comparación04 revisada y 26 cuerpos cambiados inspeccionados (`page-coverage08.json`), páginas 87,88,89,98,99,100,102,103,128,129,193,194,195,205,206,207,208,209,210,211,212,213,214,215,216,217. La comparación de cuerpos excluye encabezados/pies variables.
- Las casillas vacías del apéndice y los valores espectrales concatenados observados en comparación04 quedaron resueltos en comparación05. Las fórmulas, tablas y figuras intervenidas son legibles, sin recortes observados.

## Límites de la entrega

- Persisten defectos editoriales heredados del documento fuera de las correcciones realizadas: campos de referencias rotos, rótulos automáticos irregulares, algunas citas y residuos de ecuaciones vacías en D2. La comparación conserva espacios y algunos captions separados de sus tablas. Esta revisión no certifica un saneamiento editorial global.
- No se completó una prueba de aceptación/rechazo dentro de Microsoft Word: la automatización de la aplicación dejó de responder. El control de extremos es OOXML y la inspección visual es del render LibreOffice. No se cerraron procesos del usuario.
- La auditoría independiente examinó AVK/R02 e identificó los mismos pendientes que la auditoría principal. Las correcciones finales R03 y su comparación fueron verificadas por el agente principal; no se atribuye a la auditoría independiente una revisión de R03 que no realizó.
- R03 conserva las revisiones históricas que quedaron en la base. La comparación agrega las revisiones acumulativas identificables por su autor; no reconstruye todo el historial editorial perdido en las primeras sustituciones.
- No hubo commit, push, deploy ni cambios a los datos auditados en este cierre.
