# Procedencia de las sustituciones

El texto auditado es prose-candidate.md, expandido por R desde _results/hazard.diana.qmd. Las rutas siguientes son relativas al repositorio; los índices OOXML son posiciones del body, base cero. No se adopta el inventario como fuente científica.

|Fila|Unidad o sentencia|Tipo|Fuente primaria leída y relación exacta|
|---|---|---|---|
|P1|Engine / 3.26.2|Factual|diana-hazard/submit.log:1 identifica Engine3.26.2 y líneas2–4 los cálculos90–92. Sustituye las versiones antiguas en body24,543,786 del AVK, leídos.|
|P2|PGA10000mean /0.312|Factual|data/hazard/tables/UHSTable.Rds, ID=M2V4D,siteID=CFD,Vs30=220,Tn=0,TR=10000,p=mean:SaF0.3123115g. Tres decimales como en body27,672,788.|
|P3|PGA10000P84 /0.442|Factual|Misma selección P2,p=0.84:SaF0.4423981g. P84 es la clave de transferencia de 84th percentile, no otra estadística.|
|P4|PGA2500mean /0.159|Factual|Misma selección P2,TR=2500,p=mean:SaF0.1587537g. El propietario acepta los rótulos2475/2500; se conserva2475 en Diana.|
|P5|PGA2500P84 /0.229|Factual|Misma selección P4,p=0.84:SaF0.2287538g. Conserva unidad y población.|
|P6|The design demands combine...|Metodológica|_results/site.results.qmd:17, descripción aprobada de evaluación directa y transformación ST20 condicionada por PGA de la misma realización. UHSTable.Vref=760 en la selección; no se teclea como resultado en la fuente nueva.|
|P7|The AEP curves present...|Metodológica|Orden literal «Conservar curvas completas del cálculo directo» y ZIP públicos hazard_curves.M2V4D.CFD.<Vs>.zip. scripts/setup/hazardDiana.R:readDianaCurves consume sus POE; no se interpola UHS para formar las curvas.|
|P8|The tabulated design values and UHS combine...|Metodológica|Misma fuente P6; distingue los productos baseM2V4D design-mixture de las curvas directas según orden P7.|
|P9|The ratios of the PSHA...0.70to1.30...|Comparativa|Orden «actualizar el reporte de Diana tambien conlos datos de hazard» y «Consultar NRC2020 oficial» para rehacer8-1..3. UHSTable baseM2V4D,pmean frente a nrc2020-response.json:1 (respuestaNBC2020), Vs1500/760/220,TR500/1000/2500 y9períodos comunes0..5s. R divide SaF.project/SaF.nrc y toma rango0.70–1.30 a2decimales. No afirma acuerdo ni fiabilidad.|
|P10|The deaggregation plots show...|Comparativa|Actualización autorizada del párrafo593 que declara el control de PGA. RMwTable.Rds,ID=M2V4D,siteID=CFD,Tn=0,TR500/1000/2500/5000/10000. Máximos conjuntos (Mw,R):4.875/31.25,5.125/31.25,5.125/18.75,5.125/18.75,5.125/18.75. Se llaman centros de bins, no magnitudes de diseño Newmark.|
|P11|The magnitudes at the peaks...|Factual|Misma selecciónP10, sum(p)porTR/Mw: máximos marginales5.125para500/1000/2500 y6.875para5000/10000. Conserva pluralidad de magnitudes; no modifica mapaNewmark5.5/6.5.|
|P12|Structural periods...|Factual|nrc2020-response.json:1, campos pga,sa0p05,sa0p1,sa0p2,sa0p3,sa0p5,sa1p0,sa2p0,sa5p0,sa10p0. El párrafo649 describe la disponibilidad del servicio; la comparación usa la intersección con el modelo hasta5s.|

## Entidades y términos
PGA, AEP, UHS, PSHA y NRC se conservaron del Word: body24,26,543,649,651. ST20 procede de site.results.qmd:17. Engine es etiqueta de transferencia del recibo, y Controlling scenarios identifica el párrafo593; no se incorporan como encabezados nuevos a Diana. Structural periods es la apertura literal de body649. Los números decimales con ceros finales del listado de períodos son format() de los campos NRC, no entradas inventadas.

El primer check_entities marcó14 entidades y2 expresiones de registro. Cada línea queda resuelta: P84 por P3/P5; AEP/UHS por body24/543; NRC/PSHA/2020 por body26/651; Controlling por la clave de destino593; Structural por649; siete números con ceros finales porP12. «each» conserva el alcance por condición de site.results; «largest» identifica el argmax observado enP10 bajo la actualización autorizada de ese mismo párrafo. No se elimina la distinción conjunta/marginal para silenciar una bandera léxica.

## Aplicación al Word
En body25 se conserva la secuencia editorial y se corrige sólo la unión que produciría «conditions and were presented»: «The resulting UHS for these site-specific conditions were presented». En633 se limita la descripción antigua de los GMMs al cálculo directo y se añadeP6, conservando la cita y lista. En651 se sustituye únicamente la afirmación antigua de good agreement/reliability porP9. En593 se mantienen la última oración sobre fallas y la estructura; los símbolos de las dos oraciones reemplazadas dejan de ser objetos sueltos. En856 el rótulo90th se corrige a95th para la figuraC1-5, seleccionada conp0.95. El resto de captions, tablas deSCPT, capítulo10, ecuaciones y citas es idéntico al baseline por OOXML/ZIP.

## Límites
No se reauditan ni corrigen las normas, citas y defectos de campo heredados del texto conservado. La auditoría cubre las sustituciones de resultados y metodología; la prueba de preservación cubre el resto. No hay traducción nueva ni nuevas referencias bibliográficas.
