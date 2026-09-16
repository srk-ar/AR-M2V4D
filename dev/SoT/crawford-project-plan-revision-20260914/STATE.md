## Objective
Corregir el plan de Crawford con parámetros comunes, mapper desde params.yml, preparación completa antes de pack/run y escenario provisional S1 para MCE.

## Rulings
- Corrección explícita del propietario: adoptar TR, Vs30, Vref y convenciones comunes de los proyectos actuales, sin volver a seleccionarlos ni sustituirlos por legacy.
- TR [100,200,500,1000,2000,2500,5000,10000], Vs30 [180,270,360,560,760,800,1250,1500], Vref760. Vs30 adicionales después.
- Mapper utiliza la implementación común hidratada con propiedades Crawford de params.yml.
- Completar scaffold/configuración, integración CAN/GMM, JSON de todos los modos, data.R y consumidores antes de pack/run.
- El propietario autoriza inventar S1 provisional para MCE. No se exige rationale previo ni resultados de desagregación para prepararlo.
- CAN actual y GMM generales por TRT se conservan.
- Esta revisión prepara el plan; no inicia ejecución.

## Evidence and no-repeat
- Selector anterior leído: dev/SoT/crawford-can-migration-analysis-20260914/STATE.md, DONE. Su plan se leyó íntegramente antes de editar.
- Lectura completa de los seis oq/data/data.R confirmó TR y Vref comunes; mapper/run.py y params.yml de SAC00 releídos.
- NEXT-CLOSED {"evidence":"PLAN.md revisado según la corrección del propietario; SHA256 2fe1c5feb471acb35b8d009e7ad4237a120bca12781d7efdad786bb325fd6cb1. Verificada ausencia de los tres JSON propios supersedidos mediante test, exit0.","id":"crawford-plan-revision-20260914"}
- Matriz prevista tras preparar S1:8classical+1disaggregation+8scenario=17; aún no empaquetada.
- El punto6 del comentario no traía contenido; no atribuirle una decisión adicional.

## Effects
- Plan actualizado en dev/SoT/crawford-can-migration-analysis-20260914/PLAN.md.
- Retirados exactamente los tres JSON propios supersedidos de candidate/oq; no estaban integrados en Crawford.
- No se ejecutaron pack/run/extract/process/render ni se modificó Crawford en esta revisión.

## Delegations
none

## Blocker
none

## Next
none

## Status
DONE
