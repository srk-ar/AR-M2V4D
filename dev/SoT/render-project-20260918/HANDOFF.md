# Handoff — AR-M2V4D — 2026-09-18

**Trabajo detenido por instrucción del propietario: «olvidalo. fallaste. deja un handoff. no podemos seguir». El proyecto NO está terminado. No continuar automáticamente.**

## Identidad y límites

- Checkout: `/Users/averrik/Cloud/github/projects/AR-M2V4D`.
- Rama: `main`.
- HEAD y origin/main observados: `0947dabeb2f705037f5be047406a929ad8d666b8`.
- Selector: [dev/SoT/ACTIVE.md](/Users/averrik/Cloud/github/projects/AR-M2V4D/dev/SoT/ACTIVE.md).
- Estado seleccionado: [STATE.md](/Users/averrik/Cloud/github/projects/AR-M2V4D/dev/SoT/render-project-20260918/STATE.md).
- Los dos renders lanzados en este trabajo terminaron. No queda ejecución propia pendiente; la comprobación de procesos no mostró R, Quarto, Pandoc, QRT u OQT activos.
- No se ejecutaron borrados, reinicializaciones, restauraciones, commits ni pushes en la etapa de render y las aclaraciones posteriores.
- La expresión del propietario sobre «dinamitar el repositorio» NO fue interpretada como autorización para borrarlo.

## Instrucciones que deben conservarse

1. **Prohibido modificar el código de su librería**, incluido Newmark, o alterar herramientas para hacer pasar este proyecto.
2. Operar OQT mediante su CLI público desde `/Users/averrik/Cloud/github/projects/AR-M2V4D/oq`; no usar un CLI Newmark separado, helpers internos ni cambiar la DB/runtime.
3. S1 es definitivo por instrucción explícita del propietario. Se corrigió únicamente la descripción del JSON; no sus parámetros numéricos.
4. Conservar `Hs <- c(135, 50, 32, 27, 35)`.
5. Los textos CAN no están disponibles. No inventarlos.
6. El propietario insistió en utilizar los ejemplos reales de data.R de proyectos vecinos. No reutilizar el Crawford viejo ni las propuestas de geometrías/pares que ya rechazó.
7. Retirada la pregunta sobre «valores vigentes». Esa formulación y las inferencias del agente NO son una decisión científica del propietario.
8. Sólo retomar trabajo técnico si llega una nueva instrucción del propietario.

## Resultado real del render

- `qrt render --manifest qrt.manifest.json`: exit 1. Generó toc y falló en report.
- Error del libro: `object 'IDg.gmdp' not found`, durante executive.qmd:109–120. [Log exacto](/Users/averrik/Cloud/github/projects/AR-M2V4D/dev/SoT/render-project-20260918/qrt-manifest.log:129).
- Continuación: `qrt render --manifest qrt.manifest.json --except toc,report,ts,dn,kmax,kh`: exit 0; 15 trabajos completados. [Cierre del log](/Users/averrik/Cloud/github/projects/AR-M2V4D/dev/SoT/render-project-20260918/qrt-available.log:1486).
- Total: **16/21 HTML generados**, con archivos finales comprobados entre 00:18:54 y 00:47:11 UTC−03 del 18 de septiembre.
- Completados: toc, gmdp, sdc, sha, srs, at, vt, dt, ai, cav, cav5, psa, psv, sd, its, ipsa.
- Pendientes: report, ts, dn, kmax, kh. Sólo report fue intentado en este render; los otros cuatro no se intentaron.
- [Listado de salidas con enlaces locales](/Users/averrik/Cloud/github/projects/AR-M2V4D/dev/SoT/render-project-20260918/resultado-render.md).
- No repetir esos 16 renders por continuidad automática. La generación no equivale a aceptación científica.
- QA realizada: archivos finales, fechas/tamaños, contenido estático seleccionado y recursos locales referenciados. **No hubo QA visual**: el navegador bloqueó file:// por política de URL. No eludir esa restricción.
- Los índices HTML contienen los dominios de publicación configurados; no se desplegó nada.

## Estado de entradas y productos

[oq/data/data.R](/Users/averrik/Cloud/github/projects/AR-M2V4D/oq/data/data.R) sigue teniendo ocho líneas: ID M2V4D, sitio CFD, ocho TR/Vs30, Vref=760, las cinco alturas y NTS derivado. No fue modificado durante el render.

Última comprobación: faltan ShearTable.Rds, DnTable.Rds, kmaxTable.Rds y GMPETable.Rds. IDg.gmdp se deriva de DnTable en scripts/setup/global.R; no es un identificador que el propietario tenga que entregar manualmente.

El registro histórico [state-before-audit-close-20260917.md](/Users/averrik/Cloud/github/projects/AR-M2V4D/dev/SoT/generate-oq-data-20260916/state-before-audit-close-20260917.md:54) consigna un intento anterior de `oqt --process --steps ts` que terminó con `object 'lo.min' not found`. No se repitió ese cálculo sin modificar sus entradas. No se demostró un defecto de la librería.

**La configuración clásica del proyecto y la producción de esas tablas quedaron sin completar.** No convertir esa omisión del agente en una supuesta obligación del propietario de entregar tablas calculadas, ni adoptar automáticamente las conclusiones anteriores sobre qué debe preguntar el próximo agente.

El análisis científico SRS y la definición de la grilla GMPE no fueron resueltos por este render. El [informe anterior](/Users/averrik/Cloud/github/projects/AR-M2V4D/dev/SoT/generate-oq-data-20260916/render-readiness-20260917.md) conserva observaciones que deben distinguirse de una aceptación científica; no se revalidaron ahora todas sus conclusiones.

## Cambios observados y límite de la revisión de contaminación

**La revisión de posible contaminación fue interrumpida y NO quedó terminada. No hay base para certificar que todo el repositorio está correcto.** Un archivo sin diff frente a HEAD tampoco acredita la validez científica del contenido ya comprometido.

Se leyó el diff actual de los siguientes archivos funcionales:

| Archivo | Diferencia observada frente a HEAD |
|---|---|
| _master/book.en.qmd | Añade _book/srs.qmd a los capítulos. |
| qrt.manifest.json | Añade 12 artefactos de la familia SRS. |
| params.yml | Añade metadatos de cliente/consultores/autores, año, URL y selección SRS CFD. La procedencia de todos esos metadatos no fue revalidada en la revisión interrumpida. |
| oq/calcs/scenario/CFD/S1.json | Sólo cambia la descripción de provisional a definitivo. |
| oq/data/data.R | Sin diff. |
| scripts/setup/global.R | Sin diff. |

Los cambios en master, params y manifiesto ya estaban presentes al comenzar el render del 18 de septiembre. Este hecho no demuestra su autoría ni aceptación científica.

También hay modificaciones de continuidad en dev/SoT/ACTIVE.md y dev/SoT/generate-oq-data-20260916/STATE.md; archivos nuevos de logs, auditorías y estados bajo dev/SoT; y árboles **gmsp/** y **html/** sin seguimiento en Git. No limpiar ni restaurar esos árboles indiscriminadamente. gmsp contiene configuraciones y productos; html contiene los renders.

En esta etapa se escribieron los HTML mediante QRT, logs y documentos de continuidad; en el turno anterior de S1 se editó su descripción. No se ejecutaron escrituras en código de librerías. No se realizó una auditoría histórica completa de otras sesiones o autores.

## Ejemplos localizados: lectura comparativa pendiente

En el último turno interrumpido se localizaron estos archivos y se consultaron sus tamaños. **No se leyeron completos en esa revisión interrumpida; no presentar la comparación como realizada.** Son localizadores para una eventual revisión autorizada, no parámetros aprobados para copiar:

- [AR-S2C1R](/Users/averrik/Cloud/github/projects/AR-S2C1R/oq/data/data.R)
- [AR-SACU0](/Users/averrik/Cloud/github/projects/AR-SACU0/oq/data/data.R)
- [AR-SABP0](/Users/averrik/Cloud/github/projects/AR-SABP0/oq/data/data.R)
- [AR-S2L1W](/Users/averrik/Cloud/github/projects/AR-S2L1W/oq/data/data.R)
- [AR-SAC00](/Users/averrik/Cloud/github/projects/AR-SAC00/oq/data/data.R)
- [AR-S2J2E](/Users/averrik/Cloud/github/projects/AR-S2J2E/oq/data/data.R)
- [AR-S2P30](/Users/averrik/Cloud/github/projects/AR-S2P30/oq/data/data.R)
- [AR-GAC30](/Users/averrik/Cloud/github/projects/AR-GAC30/oq/data/data.R)

Se leyeron completos los SKILL.md instalados de QRT y OQT durante esta sesión y sus referencias pertinentes. No se encontró SKILL.md de PSHA en las raíces inspeccionadas, aunque /usr/local/bin/psha existe y se leyó su ayuda. La revisión interrumpida también leyó los SKILL.md de code/r, pero no llegó a leer cards.md ni a completar la revisión de implementación.

## Identidades para distinguir esta entrega

SHA-256 comprobados al preparar el handoff:

- oq/data/data.R: `5786331a9718841e1c72b0963195f872273920c8276bf5ab1d2de419ebb1d100`
- qrt.manifest.json: `569bdf7e5b2eaac884e88590f3b8540d04131353837832b847f5c6936ce90ef6`
- gmsp/match.json: `59974d1fd1863fbc912887779261148c4d5547fd2fbcdc0c2791bd20a19cf99b`
- resultado-render.md: `aa0577fd8238a018e05a49cfcdd66d0d38f3eb9c9a6584182cb83e1aedd8ea59`

El handoff conserva un resultado parcial y sus límites; no acredita entrega integral ni autoriza nuevas ejecuciones.
