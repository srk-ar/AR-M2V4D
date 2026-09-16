## Objective

Preparación Crawford y prueba CAN/TRT interrumpidas por orden del propietario. Cerrar el trabajo y registrar el incidente del agente; la prueba científica no se completó.

## Rulings

- Autoridad de cierre: el propietario indicó «reporta el bug de tu agente y la falta de iteligencia y cerramos aca» el 2026-09-15.
- No continuar cálculos, diagnósticos, preparación ni esperas. Cualquier reanudación requiere una nueva instrucción del propietario.
- Se conserva la prohibición expresa de intervenir el entorno Python de OpenQuake o saltarse la entrada pública de oqt. No cambiar runtime ni DB.
- El cierre no acepta CAN/TRT ni declara completada la preparación. No realizar mutaciones Git, publicación, limpieza ni envíos externos por inferencia.

## Evidence and no-repeat

NEXT-CLOSED {"evidence":"El propietario ordenó reportar el fallo del agente y cerrar. La espera de cell 146 se terminó con functions.wait terminate=true: Script terminated. Consultas de cierre no encontraron M2V4D/firma en la DB habitual; DB aislada sólo contiene 1 y 2 failed/is_running=0; manifest ausente. Se creó el reporte local y se preservó el estado anterior mediante copia comprobada con cmp, exit 0.","id":"run-oqt-with-datastore-access-20260915"}

- Reporte: dev/bugs/INCIDENT-AGENT-OQT-20260915.md.
- Copia histórica exacta del estado anterior al cierre: dev/bugs/INCIDENT-AGENT-OQT-20260915-STATE-BEFORE-CLOSE.md. Contiene decisiones, archivos preparados y evidencia previa; no es autoridad para reactivar su Next.
- Paquete conservado: dev/SoT/prepare-crawford-20260915/can-trt-test/run/classical/M2V4D/M2V4D.CFD.760.zip. Firma d7ed2282fbee7f31. No hay cálculo aceptado.
- Última ejecución efectiva: session_id 48136, exit 1, can-trt-test/run-auto.log: fallo al insertar job por DB de sólo lectura.
- No volver a esperar cells 112, 134 o 146 ni la sesión 48136. Se cerraron sus esperas o terminó el comando.
- Al cierre no hay cálculo nuevo observado en la DB habitual /Users/averrik/Cloud/nx88530/kashimaDB/openquake/oqdata/db.sqlite3. La DB aislada can-trt-test/oqdata/db.sqlite3 contiene sólo 1 y 2 failed, is_running=0. run/_manifest.json ausente.

## Effects

Reporte local escrito por solicitud del propietario. No se envió a soporte ni se creó un ticket externo.

Espera cell 146 terminada: Script terminated. No había devuelto sesión, aprobación, rechazo ni salida del comando. No se infiere de esa respuesta una cancelación de componentes externos no observables; si hubiera una nueva instrucción de continuación, reconciliar efectos tardíos antes de ejecutar.

Los archivos preparados y los logs se conservan. El agente no efectuó mutaciones Git ni publicó durante el cierre.

## Blocker

No aplica a una continuación: tarea cancelada por el propietario. La prueba quedó sin completar, con fallo observado de escritura en la DB bajo los permisos de esta sesión.

## Next

none

## Status

CANCELLED
