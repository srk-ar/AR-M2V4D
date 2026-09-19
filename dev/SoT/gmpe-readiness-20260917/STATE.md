## Objective

Resolver la consulta nueva del propietario: S1 es definitivo, no dispone de los textos CAN y quiere saber por qué falta GMPETable y cómo resolverlo.

## Rulings

- Instrucción directa del propietario del 2026-09-17: «S1 es definitivo. los textos de CAN no los tengo. porque falta GMPE Table? sabes como resolverlo?».
- S1 queda científicamente definitivo por esa instrucción; el texto provisional del JSON está desactualizado. No cambiar parámetros numéricos ni relanzar scenario por una corrección descriptiva.
- Los textos CAN no están disponibles; no inventarlos ni reintroducir un capítulo roto.
- Revisar el contrato público instalado de OQT para gmpe y resolver insumos/configuración antes de cualquier producción. No inventar una grilla científica ni ejecutar helpers privados.
- Ruta activa: oqt; operación pública --process --steps gmpe. Workspace: /Users/averrik/Cloud/github/projects/AR-M2V4D/oq.

## Evidence and no-repeat

- Cadena anterior dev/SoT/generate-oq-data-20260916/STATE.md leída, DONE; no reabrirla. Informe de auditoría: dev/SoT/generate-oq-data-20260916/render-readiness-20260917.md.
- oqt --process --help leído: gmpe es adicional, requiere calcs/gmpe/<modelID>.json y usa hazardlib sin requerir extracciones OpenQuake.
- Se preservan cambios preexistentes en master, params, manifiesto, gmsp y html. No reanudar otras tareas por esta consulta.
- El dry-run público `oqt --process --steps gmpe --dry-run`, desde oq, terminó exit 1: falta calcs/gmpe. No ejecutó R de producción. Existen los cinco XML de ASC/SCC/SIF/SIS30/SIS55 declarados por classical.
- Leída la sección 3.1 del esquema público docs/SCHEMA-CALC.md en commit OQT 7bd7faf y contrastada con runGMPE.R/gmpe_grid.py instalados: una TRT por JSON, grillas Mw/Repi, profundidad y mecanismo. No hay un contrato GMPE propio del proyecto ni autoridad para copiar los valores del ejemplo.
- Diagnóstico y procedimiento: dev/SoT/gmpe-readiness-20260917/gmpe-diagnosis.md. La diferencia editorial SIS versus SIS30/SIS55 también debe resolverse para las figuras del apéndice; no se normalizaron esas identidades.
- NEXT-CLOSED {"evidence":"Causa demostrada por dry-run público y ausencia del contrato; árboles existentes verificados; procedimiento documentado. S1 se corrigió sólo en descripción y el check R confirmó todos los demás campos idénticos a HEAD. No se generó GMPETable porque la grilla científica no está definida.","id":"gmpe-readiness-20260917.contract.v1"}

## Effects

- Actualizada únicamente la descripción de oq/calcs/scenario/CFD/S1.json para reflejar la decisión definitiva del propietario. El check jsonlite frente a HEAD, excluyendo description, terminó exit 0 con objetos idénticos.
- Actualizado el informe anterior para reconocer S1 definitivo, CAN no disponible y el diagnóstico GMPE; creado gmpe-diagnosis.md.
- No se ejecutaron cálculos, renders, Git mutations ni instalaciones.

## Blocker

none

## Next

none

## Status

DONE
