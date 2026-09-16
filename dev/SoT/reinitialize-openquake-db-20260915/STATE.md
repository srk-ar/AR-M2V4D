## Objective

Documentar el fracaso de este agente, retirar sus artefactos fallidos y cerrar por orden del propietario. Documentación y limpieza completadas; la tarea científica fue cancelada sin resultado CAN/TRT.

## Rulings

- Autoridad de cierre y borrado, 2026-09-15: «grave error. estas expulsado. documenta tu fracaso en dev. borra lo que generaste de manera corrupta y arranco otro agente».
- No continuar cálculos, preparación, diagnósticos, comunicaciones a otra tarea ni esperas. Este agente cesa el trabajo. Una nueva tarea requiere su propia identidad y estado; no reabrir este cierre.
- No intervenir el entorno de OpenQuake ni su DB habitual enlazada por ~/oqdata. OQT administra su runtime. El propietario prohibió --run-dir.
- Se conservaron los documentos, recetas y trabajo de otros agentes. El cierre no valida la preparación científica ni autoriza Git o publicación.

## Evidence and no-repeat

NEXT-CLOSED {"evidence":"El propietario expulsó al agente y sustituyó el reporte a otra tarea por documentación local, retirada de artefactos fallidos y cierre. Los intentos anteriores de entrega no tienen recepción confirmada.","id":"report-unauthorized-oqt-directories-20260915"}
NEXT-CLOSED {"evidence":"rm -r de los seis destinos identificados terminó exit 0; rmdir de los padres vacíos terminó exit 0. La comprobación posterior confirmó ausencia de las cinco rutas bajo can-trt-test y de oq/run. Reporte actualizado con el resultado y archivos conservados.","id":"remove-failed-agent-artifacts-and-close-20260915"}

- Evidencia completa y cierre de limpieza: dev/bugs/INCIDENT-AGENT-OQT-20260915.md, sección «Cierre definitivo y limpieza solicitada».
- Se retiraron de dev/SoT/prepare-crawford-20260915/can-trt-test/: run/, oqdata/, numba/, matplotlib/ y openquake.cfg. La DB retirada era la aislada creada indebidamente por este agente; incluía dos HDF5 fallidos y sus ficheros SQLite.
- Se retiró oq/run/classical/M2V4D/M2V4D.CFD.760.zip y sus padres vacíos hasta oq/run. Antes del borrado ambos ZIP tenían SHA-256 1fcf94d3b1b8952c3b32c5736b3cd7078702c24d6951a3eaaf1a94b7cacd75dd. No existe ya un paquete de esta prueba que pueda reutilizarse.
- No se detectaron symlinks en los árboles de retirada. lsof sobre can-trt-test no mostró archivos abiertos.
- Se conservaron 12 logs e inputs.sha256 en can-trt-test como evidencia. oq/ conserva calcs/, data/ y sites/. El reporte identifica el resto preservado.
- El documento dev/bugs/INCIDENT-AGENT-OQT-20260915-STATE-BEFORE-CLOSE.md y los estados anteriores son historia. Sus menciones de paquetes o DB conservados y aceptación del empaquetado quedaron superadas por la retirada y no autorizan repetir su Next.

## Effects

Limpieza local verificada y reporte final escrito. No se ejecutó OQT ni se modificaron la DB habitual, la instalación, el índice Git o el trabajo del informe durante este cierre.

No hay un cálculo CAN/TRT aceptado ni productos científicos completados por este agente.

Las esperas de mensajes cells 169 y 192 terminaron con Script terminated. La entrega externa de esos mensajes a oqt review (01a0a5b0-d006-7ee3-b2d5-e2748ef82519, host local) sigue UNKNOWN; no hay una espera activa que retomar ni autoridad para nuevos envíos en esta tarea.

## Blocker

none para la documentación y limpieza solicitadas. La tarea científica está cancelada.

## Next

none

## Status

DONE
