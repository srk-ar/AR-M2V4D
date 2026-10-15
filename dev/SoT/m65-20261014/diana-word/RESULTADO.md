# Copia actualizada del Word de Diana

Entregable: `CAPR003324_Crawford_SeismicHazard_Final.docx` en esta carpeta, 128718790 bytes. SHA256 definitivo: `69eee3e499fde36cba7886ec8504114d164cc8d4942725a9bc8b9560226cfdc8`.

El original `docx/CAPR003324_Crawford_SeismicHazard_Final.docx` sigue intacto: SHA256 `bec7b8068951a03e36aaf98274702c9a70b408363f5e2dc980ccd17cd53efa3d`. No se modificaron los sources del proyecto, los datos ni Hazard.

## Cambios aplicados

- Tablas 10-1 y 10-2: 89 celdas numéricas actualizadas desde el memo NGR. Se conserva la estructura, formato, rótulos y notas de Diana. Cada correspondencia está en `changes.json`.
- Figuras 10-1, 10-2 y 10-3: imágenes del memo para TR500, TR2500 y TR10000, conservando los rótulos editoriales 475/2475/10000 aceptados por el propietario y las dimensiones de las figuras originales.
- Introducción: rango Ts transferido del memo, 0.22–1.28 s.
- Dos afirmaciones de magnitud: 5.5 para las demandas hasta TR2500 y 6.5 para TR5000/10000/MCE, conforme a PROCEDENCIA y contratos M55/M65. Es la excepción literal autorizada por el propietario para esta copia.
- Ecuación 10-1 con H desde el ápice y definición explícita H = Hs/(1−lambda), copiadas como ecuaciones nativas del memo.
- Ecuación 10-15 con factor 100, copiada del memo corregido. Las demás palabras de Diana se conservan.

## Verificación observada

`complete_word.py` terminó exit 0. Respecto del primer candidato de tablas/figuras, cambian únicamente seis párrafos XML, índices 1572, 1573, 1582, 1583, 1616 y 1619. Los demás párrafos y partes ZIP son idénticos. Respecto del original, las únicas partes modificadas son `word/document.xml` y las tres imágenes `image41.png`, `image42.png`, `image43.png`. No se alteraron relaciones, estilos, campos, encabezados ni pies.

El texto de las seis sustituciones pasó `writing/scripts/audit.py deliver`; candidato y auditoría están junto a este archivo. La extracción `pdf2md convert` de la copia técnica terminó exit 0; se leyeron los seis pasajes. Después sólo se corrigió el espacio visible entre la fórmula H y la oración siguiente, sin cambio semántico.

Render final `documents/render_docx.py` con LibreOffice empaquetado: exit 0, 143 páginas. Se revisaron visualmente las páginas afectadas 79–90; las dos tablas completas están en la página 87 y las tres figuras en 88–90. La revisión abarca las ecuaciones nuevas y el reparto de magnitudes. El ajuste final de espacio sólo cambia píxeles en la página 80, revisada nuevamente. `delivery-render-check.json` acredita que las 131 páginas fuera de 79–90 son pixel a pixel idénticas al original: Hazard queda también visualmente intacto. No aumentó la paginación total.

## Límites conservados por instrucción

El render de LibreOffice muestra defectos preexistentes: campos de numeración que sustituyen el número de capítulo por el título; referencias no resueltas; citas duplicadas; glifos de ecuaciones incrustadas faltantes en notas y leyendas, incluidas figuras 10-2/10-3. Esos campos, objetos y textos no fueron corregidos. No se declara que el documento entero esté libre de esos defectos ni que su apariencia en Word haya sido inspeccionada. Las figuras nuevas y las tablas actualizadas sí se ven completas y sin recorte en este render.

Los auxiliares se conservan en `/private/tmp/diana-word.K8hYBK`: `original-render`, `final-render` (primer candidato), `technical-render` y `delivery-render` (entregable definitivo). El baseline de tablas/figuras queda en `tablas-figuras.baseline.docx`. No se hizo Git ni publicación.

El coordinador puede entregar esta copia con los límites anteriores. No queda otra edición dentro del alcance delegado; falta su revisión e integración de la entrega.
