# Memo AR-M2V4D: revisión EN/ES y pendientes

Los masters incorporan la revisión de prosa continua de Newmark, coeficientes y períodos fundamentales. El usuario pidió revisar, renderizar y publicar el memo EN/ES, sus recursos y las salidas HTML/Word en AR-M2V4D/main. Esta entrega conserva los escenarios provisionales y las limitaciones de formato indicadas abajo.

## Documentos

- [HTML EN](../html/gmdp.memo.en/index.html) y [HTML ES](../html/gmdp.memo.es/index.html).
- [DOCX EN](../docx/gmdp.memo.en.docx) y [DOCX ES](../docx/gmdp.memo.es.docx).

Los masters, captions, builders y demás recursos propios del memo están juntos en `_local`. Los builders consumen los helpers de `scripts/fig` y `scripts/tbl` del proyecto. Los datos, parámetros y recursos compartidos siguen siendo dependencias del proyecto; este paquete no contiene una copia de los datos científicos.

## Texto y procedencia

**La prosa revisada vive en los masters locales; no se incluye dinámicamente desde `_chapters`.** Los comentarios `sources` y `fuentes` identifican su procedencia, pero no sincronizan cambios del scaffold. La revisión actual ya no conserva los antiguos cuatro bloques delimitados por comentarios sha.

En ambos masters, la sección `sec-coefficients` integra `dn.ensemble`, `dn.model` y `dn.uncertainty`. La sección `sec-newmark-appendix` y las secciones H2 `sec-newmark-rigid`, `sec-newmark-flexible` y `sec-newmark-ensemble` desarrollan las formulaciones. Ts permanece completo bajo `sec-slope_periods`.

Los masters coinciden byte por byte con `candidate.gmdp.memo.{en,es}.qmd` de la revisión editorial registrada en `agents/dev/SoT/newmark-memo-fluency-20260924`. Sus ledgers documentan la procedencia por idioma. La revisión de render no modificó esa prosa ni tradujo una versión para producir la otra. Los captions de kmax/kh también contienen la revisión editorial local.

La retirada expresa de `eq-newmark-arias` y `Verri2023a` se conserva. Permanecen las fórmulas JB07/SR08 que usan Arias y la referencia distinta `VerriKozlowski2026Newmark`.

## Comprobaciones de esta revisión

Los cuatro renders NGR terminaron correctamente. Las 22 ecuaciones conservan las expresiones de la baseline editorial de cada idioma, aunque su orden fue ajustado por la revisión. Las anclas y referencias internas están resueltas.

HTML contiene ocho figuras de medias con quince curvas cada una: cinco pares × rigid/ensemble/flexible, para kmax y kh, con TR500, TR2500, MDE/TR10000 y MCE separados. Las series coinciden entre idiomas y con el oracle numérico conservado, usando la serialización de htmlwidgets sin tolerancia añadida. Hay un H1, once H2 y ningún H3.

HTML y DOCX contienen doce tablas de contenido, incluida una única Ts de cinco filas. Las once tablas de resultados tienen las mismas celdas EN/ES. Word contiene las ocho figuras; los elementos gráficos de portada se cuentan por separado. La plantilla local coincide byte por byte con `styles/reference.docx` del proyecto.

Verificadores y logs de esta revisión: `reports/dev/plan/m2v4d-memo-publication`. Las comprobaciones anteriores permanecen en `reports/dev/SoT/m2v4d-memo-repair`; no sustituyen la comprobación del texto y los renders actuales.

## Limitaciones pendientes

1. **Composición gráfica:** los builders locales sourcean `scripts/fig/kmax.R` y `kh.R` por modelo y reúnen sus salidas, pero también intervienen nombres, leyenda, tooltip y trazos. El rechazo previo de esa intervención no se convierte en aceptación por publicar esta revisión. No promoverla a SHA como formato aprobado.
2. **Word:** la inspección mediante LibreOffice mantiene el desborde horizontal de Ts (ES, página física 9), leyendas pequeñas y truncadas (EN 13, ES 20) y captions partidos entre páginas (ES 20). La salida Word sigue siendo provisional. No se aisló la causa ni se introdujo un formato alternativo.
3. **Ciencia y escenarios:** los pares de `gmdp.memo.scenarios.csv` siguen siendo provisionales para revisar formatos. No se aplicaron las cinco geometrías definitivas, pendientes, lambdas ni una nueva asociación de materiales. Esta revisión no recalculó datos.
4. **Incertidumbre:** esta entrega contiene las ocho figuras de medias. La composición de figuras con incertidumbre sigue pendiente.

## Continuación

Resolver la composición gráfica mediante los recursos de producción y corregir el ancho de tablas, la legibilidad de leyendas y la paginación de Word. Después aplicar las entradas científicas validadas y repetir solo las comprobaciones afectadas. Las futuras revisiones de texto deben conservar las anclas, ecuaciones, captions separados y callers de `knitBlock`, y deben partir de las fuentes y ledgers de cada idioma.

Naming del paquete: `gmdp.memo` identifica el producto; `Ts`, `kmax`, `kh` y `SiteGo` conservan las identidades existentes. Prefijos `tbl.` y `fig.` distinguen capas en la carpeta plana. Builders sin idioma, captions EN sin sufijo y ES con `.ES.md`, masters `.en.qmd` y `.es.qmd`.

Los PDF/PNG de inspección y el perfil temporal de LibreOffice no forman parte de la entrega ni del commit. Se conservan únicamente los recursos del memo y sus HTML/DOCX; los otros cambios de hidratación y datos del proyecto quedan fuera de esta publicación.
