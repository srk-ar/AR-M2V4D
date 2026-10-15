# Aceptación del ajuste de ancho

**Aceptado el ajuste de ancho de las tablas**, para `docx/docx.en.docx` SHA-256 `7b1096f0f6223b024f3b2c2a3dd9af50835743fdfa1154848fe447a94418c760`. Se verificó `diana-sources/render-report-3.exit = 0`, la conservación estructural del contenido y la presencia completa de las columnas de las 28 tablas numeradas en el render nuevo. Esta aceptación se limita al cambio de ancho; conserva los límites documentales anteriores y los observados abajo.

## Conservación comprobada

Baseline: `/private/tmp/diana-delivery-check.QSbzK8/report-before-width.docx`, SHA-256 `c1c31b8847512bcc411b3c80c1bc1b5ed1bdfc630a8fadb25b331f35a2f88fdb`.

- Ambos paquetes tienen las mismas 23 partes ZIP. Sólo difieren `word/document.xml`, `docProps/core.xml` y `word/srk-composition.json`.
- `document.xml` conserva los 156330 elementos en el mismo orden. Sus únicas 28 diferencias son el atributo `w:w` de `w:tblW`, tipo `pct`, de `0` a `5000`. Al normalizar esas 28 diferencias en memoria, el XML entero serializado es idéntico.
- Se compararon además explícitamente todos los nodos de texto, los objetos matemáticos y el texto de las 39 tablas: iguales. Medios, relaciones y todas las otras partes permanecen byte a byte iguales.
- `core.xml` sólo cambia sus dos marcas temporales. `srk-composition.json` sólo cambia `contentSha256`.
- El hash del DOCX se reobservó al finalizar: no cambió durante la revisión.

## Comprobación visual

`documents/render_docx.py` terminó con exit 0 usando el runtime y LibreOffice empaquetados. Produjo 81 páginas en `/private/tmp/diana-delivery-check.QSbzK8/report-width-pages`; la versión anterior tenía 76. El PDF de QA tiene SHA-256 `5772f7be08e04b1f350970c0c08a8694218ab531ee03faea9560070a467b8d50`.

Se abrieron directamente los PNG de todas las páginas con cuerpos de tablas numeradas y sus continuaciones. Las columnas extremas ahora quedan dentro de la página:

| Tablas | Páginas físicas revisadas |
|---|---|
| 1.1–1.4 | 8–10 |
| 3.1 | 16 |
| 3.2–3.3 | 23 |
| 3.4 | 24 |
| 3.5 | 27–30 |
| 4.1–4.4 | 36–40 |
| 4.5–4.8 | 43–45 |
| 4.9 | 49 |
| 5.1–5.3 | 51–55 |
| 5.4 | 59 |
| 6.1–6.3 | 73–75 |
| 6.4–6.5 | 77 |
| 6.6 | 78 |

También se abrieron las páginas 31, 48, 57, 58 y 76 para revisar la continuidad cercana. La ecuación 5.14 completa está en la página 57; el párrafo de magnitudes por demanda y la tabla 5.4 están en la página 59. No se repitió la revisión científica ni se afirmó una nueva inspección integral de las 81 páginas.

## Límites que permanecen

- Al caber las columnas, el texto de algunas celdas se reparte en varias líneas. En la tabla 5.3, páginas 54–55, el último decimal de `a1` pasa a otra línea. En la tabla 3.5, páginas 27–30, los identificadores y nombres largos se parten en líneas; algunas filas de esa tabla y de la 5.1 cruzan página. Las cifras no fueron alteradas.
- En la tabla 3.1, página 16, la fila superior de períodos no agrupa visualmente los pares Mw/R de manera uniforme. La estructura de celdas y combinaciones está idéntica al baseline; esta revisión no cambia ni acepta esa distribución como correcta.
- Permanecen los defectos independientes registrados en `../report-review/RESULTADO.md`: página de logo, índice sin entradas, encabezados sin cuerpo y ampersands visibles en ecuaciones. No se repararon ni se consideran resueltos por el ajuste de ancho.

Se escribió únicamente evidencia propia y el render temporal de QA. No se modificó producto, fuente, datos ni Git.
