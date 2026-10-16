# Contrato del dictamen independiente

## Product and surfaces
RESULTADO.md, dictamen técnico en español de la auditoría independiente solicitada. Ningún texto se integra en los Word o fuentes del informe.

## Reader and purpose
Coordinador y propietario: decidir si las entregas acumulan los cambios y conocer omisiones y límites de revisión.

## Sources
Las seis fuentes validadas son los DOCX original, AVK, R02, docx.en, gmdp.memo.en y hazard.diana.en, cuyas rutas y SHA256 observados constan en los seis archivos *.structure.json. Clase: productos primarios del proyecto. Acceso: hidratación completa por pdf2md1.0.0; lectura dirigida de pasajes pertinentes y comparación exhaustiva de partes ZIP, nodos del cuerpo y tablas seleccionadas mediante OOXML. No se atribuye lectura visual completa de los documentos.

Pasajes de texto leídos en /private/tmp/diana-independent.SomDdp: avk/document.md1391–1588; r02/document.md159–188,927–993,1154–1377,1378–1591,2530–2580; memo/document.md1–145 y el contenido tabular de body53/131/138/145/152/159; report/document.md60–85 y4000–4048 y tabla body314; hazard/document.md39–160,307–455 y nueve tablas body48/53/58/63/68/73/78/83/88. Revisión de estructura original/AVK/R02 incluye el final de apéndices; diez tablas body1033–1071, identificadores exactos en RESULTADO.

Evidencia observada, reproducible: audit_structure.py y check_coverage.py ejecutados con exit0; comparison.json, coverage.json, anchors-revisions.json y slope-image-diff.json son localizadores y registros de esas comparaciones, no sustituyen a los DOCX. Imágenes de figuras10-1/2/3 comparadas con figuras5/6/7 del memo. PNG auxiliares existentes p141/p143 examinados de modo acotado, sin afirmar render nuevo ni validación de todas las páginas.

## Unit of analysis
Dos etapas de entrega y cada objeto de Word: párrafos, ecuaciones, tablas, celdas, figuras, relaciones y marcas de revisión. Se distinguen texto vigente y texto marcado para borrado.

## Language direction
Dictamen solicitado en el contexto de la conversación en español; cita localizada de fuentes inglesas sin traducir ni reemplazar el informe original.

## Length and structure
Un dictamen compacto, con hallazgos paralelos y evidencia específica. El alcance es la auditoría de transferencias, no una exposición científica ni una nueva versión del reporte.

## Acceptor and delivery order
Un resultado al coordinador, para que éste reabra las fuentes antes de reconciliarlo con su auditoría y presentarlo al propietario.

## Exclusions
Orden del propietario registrada en STATE: auditar «los cambios contra el documento original de Diana y mi fuente renderizada» y «otro agente en paralelo». El estado del hijo prohíbe modificar documentos, fuentes, datos, Git o servicios. No se consultaron veredictos previos; no se interpreta que el encargo autorice incorporar MCE o restaurar apéndices.

## Comparison authority
La comparación y el juicio de cobertura se fundan en la orden literal del propietario: «podrias auditar los cambios contra el documento original de Diana y mi fuente renderizada? no estoy seguro que cambiaste todo. dispon a otro agente en paralelo a hacer la auditoria tambien para ver si llegan al mismo veeredicto. tu estas sesgado».
