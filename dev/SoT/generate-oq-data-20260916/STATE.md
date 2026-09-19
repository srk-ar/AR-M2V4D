## Objective

Auditar la preparación actual de AR-M2V4D para renderizar todo el proyecto y comunicar insumos presentes, faltantes y límites. Instrucción nueva del propietario del 2026-09-17: «revisa este repositorio ... revisa los sklls qrt, spt, y psha ... Estamso en condiciones de renderizar todo ete proyecto? tengo todos los insumos? que no tengo? que me falta?».

## Rulings

- La instrucción actual es una auditoría. No reanuda cálculos, renders, modificaciones científicas, commit, push ni despliegues de la tarea histórica.
- El manifiesto y los masters vigentes definen el conjunto auditado: 21 artefactos HTML.
- Conservar los cambios preexistentes en _master/book.en.qmd, params.yml, qrt.manifest.json, gmsp/ y html/.
- No completar parámetros científicos a partir del escenario provisional, fósiles rechazados o proyectos vecinos. Los valores de data.R no fueron modificados.
- Las interfaces consumidoras revisadas son qrt render --manifest --dry-run, psha help/version/doctor/status, spt help/version y oqt help/version. No se ejecutaron helpers internos.
- Rutas usadas: qrt (render/plan y status), spt (lectura de productos match y contrato), oqt (contrato público process y lecturas suplementarias), code/r (revisión de consumidores R). No existe skill psha en el catálogo aprobado ni en las raíces instaladas inspeccionadas.

## Evidence and no-repeat

- Informe actual: dev/SoT/generate-oq-data-20260916/render-readiness-20260917.md. Registra comandos, resultados, rutas leídas, faltantes y límites de validación.
- El estado extenso anterior se conserva sólo como archivo frío: dev/SoT/generate-oq-data-20260916/state-before-audit-close-20260917.md. Contiene cierres e identidades de las ejecuciones previas; no es una segunda cadena activa ni una autorización para reanudarlas.
- NEXT-CLOSED {"evidence":"La instrucción nueva del propietario seleccionó esta auditoría; ts/dn/kmax y los renders pendientes no se ejecutaron.","id":"generate-oq-data-20260917.classic-data-contract.v1"}
- NEXT-CLOSED {"evidence":"Auditoría documentada: QRT dry-run exit 0 con 21 trabajos; 16 HTML presentes y cinco ausentes; RDS leídos; 11 parámetros Newmark ausentes; cinco CSV SRS cubren 30 registros; blanco coincide con UHS con residuo relativo máximo 3.34e-15; compatibilidad SRS requiere revisión; S1 provisional y textos CAN/antecedentes ausentes.","id":"generate-oq-data-20260917.render-readiness-audit.v1"}
- No repetir select/rank/match ni los 16 renders existentes por continuidad automática. La auditoría verificó materialización SRS, no aprobó su compatibilidad científica: compatibility.csv informa 27/30 PGA bajo envolvente; mean.csv tiene 17/32 ordenadas fuera; stage.csv solved no cambia este límite.
- QRT planifica 21 trabajos. Las salidas presentes son toc,gmdp,sdc,sha,srs,at,vt,dt,ai,cav,cav5,psa,psv,sd,its,ipsa. Las ausentes son report,ts,dn,kmax,kh. Presencia/título no constituye QA visual nueva.
- data.R conserva ID=M2V4D, CFD, ocho TR/Vs30, Vref=760 y Hs=c(135,50,32,27,35). Faltan lo.min,lo.max,s.min,s.max,uscs,IDm,Mw.gmdp,NS,subduction,Dn_weights,Da.gmdp.
- Ausentes ShearTable, DnTable y kmaxTable globales, DnDraws.Rds y PGATable.csv del sitio. Los RDS de amenaza/MCE/ASCE/DEQ/desagregación/SSM sí se leyeron; no se comprobó el servidor OQ ni se reaceptó toda su procedencia.
- oq/calcs/scenario/CFD/S1.json declara escenario sintético provisional no calibrado a desagregación. El master inglés excluye SSM; faltan los cuatro textos CAN. _local/intro.background.md y la bibliografía local sólo contienen comentarios. GMPETable ausente provoca omisión condicional de figuras generales GMM.
- psha doctor exit 0; qrt status exit 1 sin salida, inconcluso. Runtime: Quarto 1.9.35, R 4.6.1, SPT 0.1.2, PSHA 1bb0769f-dirty, OQT 7bd7faf-dirty; 17 paquetes R consultados disponibles. No se instalaron herramientas.

## Effects

- Reparado el formato de Next al iniciar la auditoría, separando los cierres de la única acción pendiente.
- Creado el informe de auditoría y archivada la vista histórica del estado.
- No se modificaron configuraciones científicas, código, resultados, índice Git ni servicios.

## Blocker

Ninguno para la auditoría, que está terminada. El render integral y la entrega científica siguen pendientes de los insumos y revisiones identificados en el informe.

## Next

none

## Status

DONE
