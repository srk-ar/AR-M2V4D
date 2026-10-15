# Revisión visual del reporte completo

Se inspeccionaron directamente las 76 imágenes del render `/private/tmp/diana-delivery-check.QSbzK8/report-pages/page-1.png` a `page-76.png`, producidas a partir de `docx/docx.en.docx`. El SHA-256 del DOCX se reobservó antes y después de la revisión: `c1c31b8847512bcc411b3c80c1bc1b5ed1bdfc630a8fadb25b331f35a2f88fdb`.

**Veredicto visual: esta versión no pasa para entrega tal como se ve en el render, por el desborde horizontal de las tablas numeradas.** Los cambios puntuales de magnitudes y factor100 de kh sí son legibles y coinciden con el Markdown hidratado. No se alteró ningún documento, fuente, dato ni archivo de Git.

## Tablas

Las tablas numeradas se extienden más allá de los lados físicos de la página; quedan visibles sólo una o dos columnas centrales, o fragmentos de texto. Las páginas indicadas son físicas del PDF/PNG, no la numeración impresa del cuerpo.

| Tablas | Páginas físicas con el defecto |
|---|---|
| 1.1–1.4 | 8–10 |
| 3.1 | 16 |
| 3.2–3.4 | 23–24 |
| 3.5 | 27–28 |
| 4.1–4.4 | 34–38 |
| 4.5–4.8 | 41–43 |
| 4.9 | 46–47 |
| 5.1–5.3 | 49–51 |
| 5.4 | 56 |
| 6.1–6.6 | 69–74 |

Las tablas de notación de las páginas61–63 caben en la página; el hallazgo no se aplica a toda tabla de Word. Las figuras enlazadas a annex/decks responden al diseño del master NGR y no se trataron como figuras faltantes.

## Cambios acotados comprobados

- Página8, resumen ejecutivo, y página53, método: se lee la magnitud de referencia asignada a cada demanda sísmica, sin declarar una única magnitud para todas las demandas.
- Página54, ecuación5.14: `kh = 100 kmax / PGA(VS30)` se muestra completa y legible.
- Página55: se lee Mw5.5 para TR100,200,500,1000,2000,2500 y Mw6.5 para TR5000,10000 y MCE. El párrafo entero está dentro de página.
- Los pasajes se cotejaron con la lectura de `/private/tmp/diana-delivery-check.QSbzK8/report/docx.en.md`, líneas4006–4045, en particular4016,4022,4036–4038. Esta revisión comprueba correspondencia documental y legibilidad; no recalcula los datos científicos.

## Otros hallazgos visibles

- Página3: sólo logo en la parte superior; el resto está vacío.
- Página4: título `Table of Contents` sin entradas.
- Página17: encabezados3.2.1–3.2.4 consecutivos, sin cuerpo antes de3.3.
- Página27, ecuación3.35, y página45, ecuación4.24: ampersands visibles dentro de la ecuación.
- Páginas74–76, ecuaciones6.2,6.4,6.5,6.7–6.9: ampersands visibles en varias líneas. En el resto del texto inspeccionado no se observó recorte general del cuerpo ni glifos matemáticos ausentes.

## Atribución frente al documento previo

Se leyó el OOXML del baseline `/private/tmp/claude-501/-Users-averrik-Cloud-github-projects-AR-M2V4D/bc6bc387-e4e1-4ab5-a8cb-3e5e18735788/scratchpad/docx.en.before-gmpe.docx`, SHA-256 `9345f198bf9c7349b70f15aad95c36fa9f9c4c99d61b76c0d5063c73886d387d`, y el OOXML del reporte actual.

- Las39 propiedades `w:tblPr` son byte a byte idénticas entre ambos documentos. Ambos contienen28 `w:tblW` de tipo `pct` con valor0 y11 tablas con `w:tblGrid`.
- Los8 objetos `m:oMath` que contienen ampersands son byte a byte idénticos entre ambos documentos; contienen31 caracteres `&` en nodos `m:t`.

Por tanto, esas propiedades de tablas y esos objetos matemáticos ya existían en el baseline. No se atribuyen a las correcciones puntuales de magnitud y kh. No se renderizó el baseline, conforme a la indicación del coordinador; no se afirma equivalencia visual de sus páginas. El origen temporal de la página de logo, el índice vacío y los encabezados sin cuerpo queda sin clasificar.

La evidencia cubre exclusivamente el DOCX identificado por su hash. El coordinador está evaluando una copia con ajuste de ancho; este veredicto no evalúa ni acepta esa copia.
