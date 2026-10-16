# Verificaciones del dictamen

Candidate: RESULTADO.md, SHA256 92f5f1825daf0597bf8838ecf64b5618faf324d6ccbd531f3e6d7097f83f6061.

La revisión semántica cubre los 12 bloques completos, incluidos título y evidencia. El registro provenance.md enlaza cada oración con el DOCX primario, pasaje hidratado o efecto observado que la sostiene. Las comparaciones están autorizadas por la orden literal del propietario preservada en el contrato y el estado.

Ejecuciones observadas:

- pdf2md convert para los seis DOCX: exit 0; assets.json y salidas bajo /private/tmp/diana-independent.SomDdp. No hay pretensión de lectura visual integral.
- audit_structure.py: exit 0. Comparó cada parte del paquete y los nodos del cuerpo; preservó hashes y marcas. No modifica los archivos DOCX.
- check_coverage.py: exit 0. Nueve tablas Hazard iguales, 594 celdas comparadas; 77 imágenes iguales con un vínculo por imagen; tabla 10-1, 72 celdas iguales; tabla 10-2, 60 celdas seleccionadas iguales; capítulo 10 idéntico AVK/R02.
- Diagnóstico de diferencias de imágenes con PIL/numpy: exit 0; matrices y límites en slope-image-diff.json. El intento previo que requería scipy falló por módulo ausente antes de escribir y no forma parte de la prueba.
- check_entities.py: exit 1 por coincidencias léxicas ausentes y banderas. Se conserva íntegro entities.txt; todas sus 23 incidencias y cuatro banderas están resueltas, una por una o mediante grupos explícitos, en provenance.md. Cero incidencias semánticas abiertas; no se altera el reporte automático para simular exit 0.
- Las seis imágenes de coeficientes fueron abiertas y comparadas completas. Se abrieron sólo las páginas auxiliares especificadas en provenance.md; no hubo render ni aceptación visual de 143 páginas.

Correcciones de prosa frente a result-draft01.md: se restituyeron espacios entre nombres, cifras y unidades sin cambiar cantidades. La frase «las fuentes NGR» se restringió a «el memo NGR» porque el reporte completo tiene ocho escenarios de material, mientras el memo tiene cinco combinaciones. Se releíeron ambos contextos después de corregir.

No corresponden compilación de Quarto, render de Word, traducción, prueba ASCII de inglés ni resolución de citas bibliográficas: el único producto es un dictamen de auditoría en español sin citas nuevas ni ecuaciones nuevas. H, Ts y los cocientes se usan para identificar expresiones o valores existentes del Word, no para introducir una formulación matemática. No se convierte un defecto heredado en un defecto causado por R02; no se decide adoptar MCE ni actualizar apéndices.

audit.py deliver es la comprobación final pendiente de ejecución; su salida stderr deberá archivarse en writing-verdict.json. Este registro no establece por sí solo ready.
