La copia R02 está en `docx/diana-actualizado/CAPR003324_Crawford_SeismicHazard_Final_AVK_R02.docx`.
SHA-256: `86dd4a5e7631e1abc5db539176fdf0da118904690a86be77a03187bd501a180e`.
Tamaño: 144362238 bytes. Es idéntica a candidate04 y a la entrada del render QA04.

Comprobaciones observadas el 2026-10-15:

- `check_word.py` terminó con exit0: nueve tablas, 594 celdas cotejadas con `product-verification.json` y 77 imágenes cotejadas con los payloads de NGR.
- El capítulo 10 completo conserva el OOXML de la copia AVK aceptada. Todos los objetos fuera de los índices intervenidos son idénticos. Los ZIPparts originales, salvo `document.xml` y sus relaciones, conservan sus bytes.
- Se reobservaron los hashes del original de Diana y de la entrega AVK anterior; coinciden con los registrados en `word-verification.json` y STATE.md.
- `render-qa04.log` terminó con exit0 y produjo 143 páginas. QA interno en `/private/tmp/diana-hazard-r02-qa04`.
- `final-page-diff.json` identifica 58 páginas con diferencias en el cuerpo; las otras 85 conservan los mismos píxeles antes del pie. La comparación excluye desde y1875 en páginas verticales y y1420 en apaisadas, donde están los pies cuyo campo de nombre cambia con R02. La portada interior muestra el nombre final completo.
- La inspección visual cubrió las páginas intervenidas: 2,7,45–51,53–55,65–78,91,106–118,120–132,135–136,138–140. Tablas completas y cifras legibles; figuras con ejes y leyendas visibles. El detalle de la tabla77 se cotejó además mediante un recorte a resolución original.
- Se corrigió una leyenda UHS que perdía la etiqueta10000 en las figuras estrechas. NGR regeneró la transferencia con leyenda en dos filas y título encima. Candidate04 cambia sólo31 imágenes respecto de candidate03; los demás ZIPparts son idénticos. La comparación de renders identifica sólo17 páginas diferentes, todas inspeccionadas:49–51,66,120–132; las otras126 son pixelidénticas.
- La prosa dinámica mantiene el SHA aprobado por `prose-verdict.json`, status ready. El cambio posterior fue sólo la presentación de las leyendas.

La revisión estructural de los sources y adaptadores conservó las interfaces locales existentes. Los datos se seleccionan por Vs30, estadístico, período espectral y retorno; las tablas y valores del texto provienen de R. Los adaptadores editan una copia, rechazan destinos existentes y verifican la preservación del contenido ajeno al alcance. No se cambió la producción científica durante los ajustes visuales.

Límites: se conservaron los defectos previos de campos, referencias, citas y residuos de los apéndices fuera del alcance. No se declara saneamiento editorial global del Word. Los pies y las fechas que son campos pueden actualizarse según la aplicación que abra el documento. Los archivos PDF y PNG son únicamente evidencia de QA.

Esta entrega no incluye nuevas operaciones Git ni publicación HTML. El cierre administrativo y cualquier retirada de auxiliares requieren una orden y lista aprobada. Antes de retirar esta tarea deben resolverse las dependencias de `scripts/setup/hazardDiana.R` sobre la respuesta NRC2020 y el registro de versión actualmente citados bajo `dev/`; no eliminar esos datos mientras el master los consume.
