## Objective

Actualizar sólo las tablas y figuras del capítulo Slope Design Parameters en una copia del Word de Diana a partir de los Word generados por NGR, preservando su texto y todo Hazard.

## Rulings

- Ampliación del propietario verificada en Rulings del coordinador: «en el texto de Diana si puedes hardcodear numeros en este caso extermo de las magnitudes» y «a Diana le va,os a dar las dos cosas: el reporte full mio actualizado y su reporte actualizado en el capitulo de parametros de diseno sismico de taludes». El coordinador delega además corregir las dos afirmaciones de magnitud, trasladar el rango de Ts del memo renderizado y las ecuaciones de Ts/H y kh corregidas, preservando la redacción restante. La exclusión anterior de esas correcciones queda sustituida. No corregir defectos preexistentes de campos, referencias ni estilos. Hazard queda intacto.
- Autorización del propietario: preguntó «si te pido corregir tablas y figuras del DOCX de Diana a partir de docx/docx.en.docx es algo facil de hacer?» y luego ordenó «en paralelo, a lo que estas haicendo». El coordinador explicó que docx.en.docx enlaza figuras y que docx/gmdp.memo.en.docx las incorpora; el propietario pidió hacerlo en paralelo. Crear una copia en este write_root, nunca sobrescribir el original. El coordinador la entregará tras verificarla.
- Original validado: docx/CAPR003324_Crawford_SeismicHazard_Final.docx. Fuentes: docx/docx.en.docx y docx/gmdp.memo.en.docx. Leer antes de describir o cambiar. El capítulo ya convertido está en docx/CAPR003324_Crawford_SeismicHazard_Final.slope-design-parameters.md, localizador; corroborar con originales. Todo Hazard está expresamente excluido. Actualizar tablas 10-1, 10-2, figuras 10-1, 10-2, 10-3 y las seis correcciones técnicas autorizadas arriba; preservar todo el resto. Mantener leyendas, rótulos y formato de Diana salvo ajuste material indispensable de tamaño.
- El propietario ordenó «no rompas nada» y avisó que el otro agente ya había trabajado. Reutilizar los productos y no rehacer los análisis ni render NGR. Los 54 bloques editoriales ya están integrados en el proyecto: no reaplicarlos. El original y todas las fuentes son de sólo lectura para esta misión.
- Resultados sólo desde productos auditados o sus Word ya generados. Prohibido introducir números científicos literales en textos o scripts. Las tablas de Diana pueden actualizarse mediante correspondencias verificadas con los valores del Word generado; no inferir ni calcular nuevos resultados. Se acepta la equivalencia editorial 475/500 y 2475/2500 por instrucción expresa; no renombrar ni preguntar por ella.
- Cargar skills pertinentes del catálogo con el comando exacto: continuity antes de estado; pdf2md para extracción de DOCX por CLI; documents para edición y verificación visual; code y python si hace falta código. No modificar librerías ni instalar software. Escrituras exclusivamente en este write_root y scratch temporal. Sin Git, mensajes a otros chats ni modificación del estado coordinador.
- Antes de entregar, verificar que todas las partes del paquete Word ajenas a los cambios previstos sean idénticas, que el texto fuera de las celdas a actualizar se conserve, y que tablas/figuras reemplazadas correspondan a las demandas y escenarios correctos. Generar comprobación visual si el runtime disponible lo permite; reportar límites reales. No afirmar equivalencia visual sin verla.

## Evidence and no-repeat

- Primer candidato conservado como tablas-figuras.baseline.docx para la ampliación. Con el mismo basename que el original, render original y candidato tienen 143 páginas y sólo difieren en píxeles las páginas 86–90: las dos tablas y tres figuras. Las otras 138 páginas son idénticas. Revisión visual de las cinco páginas confirma objetos completos, y limitaciones preexistentes de campos/referencias y algunas celdas contiguas en LibreOffice. No declarar saneamiento visual de todo el documento.
- SoT de ampliación: baseline tablas-figuras.baseline.docx; candidato CAPR003324_Crawford_SeismicHazard_Final.docx dentro de este write_root. Diferencia: únicamente seis párrafos técnicos y sus ecuaciones, además de los objetos ya actualizados. Oracle: extracción pdf2md de los pasajes, exactitud de los valores respecto del memo/PROCEDENCIA y contratos; paquete y elementos fuera del capítulo idénticos; render comparado y revisado en páginas afectadas. Contrato de escritura y auditoría en writing-contract.md y archivos asociados.
- Leídos mediante extracciones pdf2md 1.0.0 el capítulo original (archivo de extracción anterior, líneas 1503–1589), los valores del memo (memo-current.md:157–390 y 635–847) y el reporte principal (report.md:203 y tabla 5.3). El memo contiene los cinco escenarios y las demandas necesarios; el reporte principal declara figuras sólo en HTML y su tabla de períodos es sólo para altura 50 m. Se usará el memo existente para los dos objetos tabulares y las tres imágenes.
- Identidad original reobservada: SHA256 bec7b8068951a03e36aaf98274702c9a70b408363f5e2dc980ccd17cd53efa3d. Las otras dos identidades coinciden con las indicadas debajo. Tablas Word originales con índices XML 13 y 14; imágenes image41.png/image42.png/image43.png con relaciones rId71/rId72/rId73.
- SHA256 observado por coordinador para memo: c861b12bbfe331c32175c280078d565c810c6906a471421d6bc57f43eba701f6; docx.en: 4a05922f853bf1548680dc178d4325d8511dce59a1842ca7790f894a2a1c4421. No son sustituto de lectura propia.

- NEXT-CLOSED {"evidence":"Primera copia generada y verificada: changes.json y render-check.json; baseline conservado. La ampliación requiere seis correcciones técnicas.","id":"diana-word.update-tables-figures.v1"}

- NEXT-CLOSED {"evidence":"Copia69eee3e4 verificada por technical-check, delivery-package-check y delivery-render-check; RESULTADO.md entregado con límites.","id":"diana-word.complete-technical-copy.v1"}

## Effects

Entregable final CAPR003324_Crawford_SeismicHazard_Final.docx, SHA256 69eee3e499fde36cba7886ec8504114d164cc8d4942725a9bc8b9560226cfdc8. Original bec7b806 intacto. technical-check.json: seis párrafos técnicos adicionales al baseline, resto idéntico. delivery-package-check.json: sólo document.xml y tres imágenes cambian frente al original. Extracción pdf2md exit 0, pasajes leídos. Render final exit 0, 143 páginas; revisión visual de páginas79–90, tablas y figuras completas. delivery-render-check.json: las131 páginas restantes son pixel idénticas al original, incluido Hazard. Auxiliares en /private/tmp/diana-word.K8hYBK; delivery-render es el definitivo. RESULTADO.md contiene alcance, controles y defectos preexistentes conservados. No queda edición dentro del alcance; copia preparada para revisión e integración del coordinador.

## Delegations

none

## Blocker

none

## Next

NEXT-ID {"action":"Entregar al coordinador RESULTADO.md y la copia verificada69eee3e4 para su revisión e integración. Conservar baseline y evidencia hasta la aceptación; no repetir renders ni ampliar cambios.","id":"diana-word.coordinator-acceptance.v1"}

## Status

ACTIVE
