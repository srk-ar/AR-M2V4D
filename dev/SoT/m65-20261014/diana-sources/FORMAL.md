# Comprobaciones focales

Fase: diagnóstico focal de la diferencia solicitada, sin commit ni certificación de una librería.

- checkCandidate.R terminó con exit 0: las cláusulas se expandieron con knitr; el bloque de magnitudes dio Mw 5.5 para TR 100, 200, 500, 1000, 2000, 2500 y Mw 6.5 para TR 5000, 10000 y MCE; sin NA. Es el reparto de PROCEDENCIA.md:11–12.
- El mapa candidato es idéntico byte a byte al mapa auditado. No se cambia ninguna decisión científica.
- El baseline de los cuatro archivos usa Mw.gmdp en las cláusulas revisadas; el candidato ya no lo usa. El baseline no cumple el reparto por demanda, pues setup.R:48 lo lee de newmark.json, cuyo valor único no representa la combinación.
- Inglés ASCII comprobado en candidate.md. No se cambian citas ni identificadores de ecuaciones. El factor de porcentaje es el mismo que scripts/tbl/kh.R ya aplica.
- Los dos avisos de formato numérico del gate de entidades se resuelven en PROVENANCE.md; el informe original entities.txt se conserva.
- Alcance del audit.py: párrafos alterados y fórmula, expandidos con R, conservando el contexto suficiente para revisar las cláusulas. No se presenta candidate.md como capítulo independiente. El master y sus bloques heredados se leyeron antes del cambio; no se rehace su edición aprobada.
- El render NGR y su cotejo de tablas/figuras se ejecutan después de integrar exclusivamente el candidato aprobado; ese control de ensamblado no se sustituye por este knit focal.
