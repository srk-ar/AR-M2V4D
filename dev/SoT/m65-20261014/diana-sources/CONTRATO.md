# Corrección mínima de magnitudes y normalización

## Product and surfaces

Capítulo inglés existente _local/gmdp.memo.en.qmd y sus fuentes inglesas _chapters/dn.model.md, _results/dn.results.qmd y _results/dn.inputs.qmd. Se conserva la redacción editorial aprobada e integrada en 21d4c7a. Se añade _results/dn.magnitudes.qmd para representar el reparto de magnitudes de la combinación auditada mediante R. Render del memo por NGR, DOCX, mismo master y perfil ya empleado por el proyecto. No se rehace la estructura del capítulo.

## Reader and purpose

Diana Reyes y el propietario: disponer de las magnitudes realmente usadas y de una fórmula consistente con el porcentaje publicado en tablas y figuras. El DOCX del memo sirve para copiar y pegar el capítulo. El trabajo paralelo sobre la copia de Diana sólo cambia tablas y figuras.

## Sources

| Source | Class | Access level | Location read |
| --- | --- | --- | --- |
| data/newmark/PROCEDENCIA.md | project truth | full text | líneas 1–40: combinación y contratos por demanda |
| dev/SoT/m65-20261014/magnitude-map.csv | project truth | full text | filas 1–10, reparto aprobado por el propietario |
| newmark-M55.json, newmark-M65.json | project truth | full text | path.products, Mw.gmdp, TR.gmdp, NS y parámetros iguales restantes |
| docx/CAPR003324_Crawford_SeismicHazard_Final.slope-design-parameters.md | approved report wording, extraction | targeted read | líneas 1–115: frases originales con magnitud única y definición porcentual |
| _local/gmdp.memo.en.qmd | approved project text | full text | líneas 1–332: correcciones de Diana ya incorporadas, ecuación del ápice correcta |
| _chapters/dn.model.md | approved project text | full text | líneas 1–20 |
| _results/dn.results.qmd, _results/dn.inputs.qmd | approved project text | full text | bloques completos |
| scripts/tbl/kh.R | internal technical | full text | conversión Kh = 100 * Kh, selección y unidades |
| data/newmark/kmaxTable.Rds | project truth | targeted read | columnas ID, TR, units.Kh: ratio en las nueve demandas |

## Unit of analysis

La magnitud pertenece a cada demanda de la combinación, compartida por geometrías y materiales de esa demanda; no existe una magnitud única para el proyecto. El factor 100 convierte una razón a porcentaje y no cambia el resultado científico.

## Language direction

Inglés de Diana ya incorporado al proyecto. No traducción ni edición de la versión española. Se conserva la terminología existente salvo el alcance falso de la magnitud.

## Length and structure

Mismo memo y estructura; sustituir las cláusulas de magnitud constante por asignación por demanda y un párrafo de resultados generado mediante R. No reescritura editorial general, nueva bibliografía ni nuevos resultados. Fórmula kh con el factor porcentual que ya aplica el builder.

## Acceptor and delivery order

El propietario ordenó «ok, procede. Corrige los sources conservando la redacción de Diana y generando los valores con R desde los datos auditados. Renderiza el DOCX del capítulo con tablas y figuras para que ella lo copie y pegue» y luego «eso yalo habia hecho el otro agente... cuidado.. revisa bien», «no rompas nada». Se aplica sólo la diferencia comprobada después de verificar el parche anterior. Esta orden autoriza la integración local y render; no commit/push ni promoción a otros proyectos.

## Exclusions

«no hay que tocsr nada del documento de Diana relacionado con Hazard»; «hardcodear numeros en texto esta prohbido»; «no hay una magnitud unica»; «ignora las diferencias entre 475 o 500». Sin recálculos, sin editar los productos RDS y sin reaplicar el parche de 54 bloques.
