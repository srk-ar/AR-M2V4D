## Objective
Añadir al plan la verificación explícita de los TRT de CAN antes de pack/run y realizar el cruce XML preliminar.

## Rulings
- Propietario: CAN no se usó antes en los proyectos activos SAM/ARB/XAF; comprobar su propia integración.
- Parámetros comunes, mapper desde params.yml y S1 provisional permanecen vigentes.
- Verificar árbol SSM, fuentes/grupos, mapa JSON, selectores GMM y tratamiento por motor/consumidores.
- El resultado estático no acepta la integración completa ni autoriza adelantar pack/run.
- SSM/GMM/Crawford no modificados.

## Evidence and no-repeat
- Estado previo dev/SoT/crawford-project-plan-revision-20260914/STATE.md leído DONE.
- ssmLT_CAN.xml y seis archivos referenciados analizados mediante XML; fuentes/grupos y selectores de cinco semillas generales coinciden: ASC,SCC,SIF,SIS30,SIS55.
- Ocurrencias en archivos únicos:ASC58,SCC138,SIF13,SIS30=1,SIS55=4. Pesos SSM y cada semilla suman1.
- Cotejo con NRC legacy: sin diferencias TRT en IDs coincidentes; ocho IDs árticos tienen contrapartes con sufijo_ARC, conservar trazabilidad sin calificarlos como TRT erróneos.
- NEXT-CLOSED {"evidence":"Sección3 de PLAN.md ampliada y releída; SHA256 c091e56c6670319cc319feeb84ddeca89e231411e94cf1c3b629dcf6ee5c61bc. TRT-AUDIT.json generado con rutas/hashes, SHA256 c047d905f8eadbcbe9269a55a8d6e6ff19d5ae36ce7fe77df15d54c935bfdbd6.","id":"crawford-can-trt-check-20260914"}

## Effects
- Plan actualizado: dev/SoT/crawford-can-migration-analysis-20260914/PLAN.md.
- Evidencia nueva: dev/SoT/crawford-can-trt-preflight-20260914/TRT-AUDIT.json.
- No pack/run/process ni cambios de modelo.

## Delegations
none

## Blocker
none para esta actualización del plan; verificación integral motor/consumidores pendiente en el plan.

## Next
none

## Status
DONE
