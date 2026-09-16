## Objective

Preparar AR-M2V4D para su flujo actual: excluir SRS, no inventar capítulos SSM, generar los productos requeridos bajo `oq/data` mediante la interfaz pública instalada de OQT y cerrar los cambios propios con commit y push en la rama actual.

## Rulings

- Instrucción directa del propietario, 2026-09-16: «commit push de este repositorio. genera los resultados de oq/data. el proyecto no lleva SRS. no tenemos por ahora los capitulos ssm».
- SRS queda fuera del contrato de publicación y del libro del proyecto; no se eliminan semillas compartidas del scaffold que no estén incluidas ni publicadas.
- La ausencia temporal de capítulos SSM no autoriza inventarlos ni escribir contenido científico sustituto.
- Mientras esos cuatro capítulos CAN no existan, el libro no incluye el contenedor `_book/ssm.qmd`; `params.ssm: CAN` se conserva para el modelo y una incorporación editorial futura.
- OQT se opera desde `/Users/averrik/Cloud/github/projects/AR-M2V4D/oq` mediante el CLI público instalado, con su runtime normal. No administrar ni sustituir la DB, el entorno o los helpers internos.
- La matriz y las etapas de proceso se derivan de los JSON, `data.R` y consumidores vivos antes de iniciar corridas; no se inventan cuantiles, selectores, modelos o parámetros.
- No se autorizó render, inicialización ni despliegue Netlify.
- Commit y push están autorizados para el conjunto coherente de preparación y resultados versionables de esta tarea; preservar cualquier trabajo ajeno o ignorado no perteneciente al alcance.
- Instrucción directa posterior del propietario: «ya borré ese docx. continúa». Selecciona retirar `CAPR003324_Crawford_SeismicHazard_20260831.docx` de los dos commits locales no publicados y autoriza continuar la reescritura local necesaria y el push ya solicitado; no selecciona Git LFS.

## Evidence and no-repeat

- La cadena anterior `dev/SoT/reinitialize-openquake-db-20260915/STATE.md` está `DONE`, declara retirada de los paquetes fallidos y prohíbe reabrir aquella ejecución; esta es una tarea nueva por instrucción posterior del propietario.
- Observación inicial: rama `main`, upstream `origin/main`, HEAD `cb8002d`, rama local adelantada un commit sobre `origin/main`, índice vacío y numerosos archivos de scaffold/preparación aún sin seguimiento.
- Remote observado: `origin git@github.com:kanameishi/AR-M2V4D.git`; identidad Git configurada: Alejandro Verri Kozlowski `<averri@fi.uba.ar>`.
- NEXT-CLOSED {"evidence":"Leídos params.yml, qrt.manifest.json, book.en.qmd, los contratos OQ, data.R, consumidores y salidas existentes. Los tres dry-run de pack terminaron exit 0 y enumeraron 8 classical + 1 disaggregation + 8 scenario. OQT instalado es 7bd7faf-dirty; servidor observado http://127.0.0.1:8800 con Engine 3.26.2.","id":"generate-oq-data-20260916.audit.v1"}
- Las ocho celdas classical están completas en el servidor y manifiesto local, calc_id 5–12, firmas concordantes y extracciones presentes. El cálculo disaggregation histórico se identifica como 1751 dentro de los ZIP, pero ese ID ya no existe en el servidor actual; se preservan sus extracción y RMwTable sin atribuirles una corrida nueva.
- Productos globales presentes antes de esta tarea: AEPSTable, AEPTable, DEQTable, RMwTable, SSMTable, UHSRock y UHSTable. Faltan ScenarioTable/MCETable/ASCETable/ShearTable/DnTable/kmaxTable y sus dependencias locales.
- La receta classical declara media y los siete cuantiles requeridos; `data.R` fija M2V4D, CFD, ocho TR, ocho Vs30 y Vref 760. La familia scenario seleccionada es S1/CFD en esos ocho Vs30.
- Los cuatro capítulos CAN referenciados por `_book/ssm.qmd` no existen. El libro y manifiesto originales sí incluían SSM y doce artefactos de la familia SRS, respectivamente.
- Ocho paquetes scenario S1/CFD fueron creados con firmas 29f4c4ec3d1b4172, c850bbce0a5ea5d2, cdc314ed9272b6e8, fc39ae14efba5b54, c535cd487f0fe9f6, cae3343984595c31, 0051bb7f0d43a18c y 493b8b28adef8686 para Vs30 180,270,360,560,760,800,1250,1500. CRC pasó en los ocho; cada uno contiene exactamente los siete miembros esperados y cubre 192 claves requeridas = 1 ruptura × 6 GMM × 32 IMT, sin duplicados y con pesos por IMT iguales a uno.
- NEXT-CLOSED {"evidence":"La sesión arm2v4d-scenario-20260916 terminó con __OQT_EXIT_0__. El listado público del servidor reconcilió las ocho celdas S1/CFD como complete, no running, con IDs 16–23, Engine 3.26.2 y firmas de descripción concordantes con cada paquete. La interfaz remota actual conserva esas identidades bajo run/_remote; el antiguo run/_manifest.json no recibió entradas scenario y no se usa como prueba de esta generación.","id":"generate-oq-data-20260916.scenario-run.v1"}
- `qrt render --manifest qrt.manifest.json --dry-run` terminó exit 0 y planificó exactamente nueve trabajos no SRS con rutas neutrales concordantes.
- La extracción pública scenario terminó exit 0 y publicó ocho familias bajo `output/scenario/S1/CFD`, con mapeo 1250→16, 1500→17, 180→18, 270→19, 360→20, 560→21, 760→22 y 800→23. Cada familia tiene exactamente un GMF y los sidecars actuales de eventos, realizaciones, sigma, sitio, variantes, distancias y estadísticas GMM; no hay calcID mezclados.
- El dry-run conjunto de `mce,mcer,ts,dn,kmax,deq` enumeró las ocho celdas directas y ocho blancos ST20 con ancla 760. Se detuvo correctamente antes de mcer porque dry-run no crea MCETable; por eso las etapas se ejecutarán y aceptarán una por una según dependencias.
- MCE terminó con `__MCE_EXIT_0__`: ocho blancos ST20 convergieron, el agregador publicó MCEBranchTable 1536, ScenarioTable 1, MCETable 9472 y ScenarioGMPETable 513 filas. MCETable cubre CFD, los ocho Vs30, 37 períodos, ocho estadísticos y los cuatro IDs S1/S1.oq/S1.site/MCE sin pérdida de la triada directa/sitio.
- MCER terminó exit 0 y publicó ASCETable con 768 filas/256 celdas.
- NEXT-CLOSED {"evidence":"Extracción scenario y MCE/MCER completaron; ts se ejecutó una vez y falló antes de escribir ShearTable con `Error: object 'lo.min' not found`. data.R sólo declara ID, sitio, TR, Vs30/Vref y Hs/NTS. El resto de procesos queda pendiente; no se relanzó ni se inventaron parámetros.","id":"generate-oq-data-20260916.extract-process.v1"}
- DEQ terminó exit 0 y publicó `oq/data/DEQTable.Rds` con 49.152 filas para ANCOLD, CDA y GISTM.
- NEXT-CLOSED {"evidence":"Se agotó el contrato vivo y el historial propio del proyecto. `legacy/R/dataset.R` conserva cinco alturas y valores de geometría/material que apuntan a RI/RB/SSI/CI/TMF, pero su constructor actual mezcla siete ID con cinco filas y es inválido. Las versiones históricas coherentes describen otra geometría de siete estructuras. Además, el `runTs.R` instalado sólo admite rangos lineales `lo.min/lo.max` y `s.min/s.max`, por lo que no puede reproducir sin pérdida la geometría irregular de cinco estructuras. No existe autoridad inequívoca para `Mw.gmdp`, `NS`, `subduction`, `Da.gmdp` ni para sustituir ese contrato con defaults de otro proyecto.","id":"generate-oq-data-20260916.data-contract.v1"}
- El snapshot staged contiene 1.391 rutas dentro de las raíces autorizadas de preparación del proyecto; el índice previo estaba vacío, no quedan cambios de worktree ni archivos no ignorados fuera del índice, no se incluyó `oq/run`, scratch, logs OQT ni bytecode Python. Los cuatro JSON OQ parsean; el manifiesto contiene nueve artefactos y cero alias SRS; el libro no referencia SRS ni SSM.
- NEXT-CLOSED {"evidence":"El snapshot se creó como commit local ac745352d591b320ec8f5a9a1787651b1fc0e81e (`prepare Crawford hazard project`). Dos intentos de push terminaron sin efecto remoto: GitHub rechazó la rama porque el commit local previo cb8002d contiene `CAPR003324_Crawford_SeismicHazard_20260831.docx`, blob 203d6731b2ad21acc8189d0ce4c59a7a19c460c1 de 135.391.521 bytes, superior al límite de 100 MiB. `origin/main` permanece en 832314f y la rama local está dos commits adelante.","id":"generate-oq-data-20260916.git-closeout.v1"}
- NEXT-CLOSED {"evidence":"El propietario eligió retirar el DOCX y continuar. Observación posterior: el path ya no existe en el worktree; aparece como eliminación no staged, el índice está vacío, `origin/main` permanece en 832314f y los únicos cambios vivos son esa eliminación y esta actualización de STATE.md.","id":"generate-oq-data-20260916.large-file-policy.v1"}
- La reconstrucción usó `git reset --soft 832314f...`, que movió sólo HEAD y preservó índice/worktree. Tras stagear exactamente el DOCX ausente y STATE.md, el índice tiene 1.619 rutas contra origin; comparado con el árbol preparado `ac74535`, difiere sólo por la eliminación del DOCX y esta actualización de continuidad. No quedan cambios unstaged ni untracked; el mayor archivo del snapshot es 24.992.500 bytes y ninguno alcanza 100 MiB.

## Effects

- Cadena de estado nueva declarada.
- `qrt.manifest.json` conserva nueve artefactos no SRS; se retiraron las doce declaraciones SRS. `_master/book.en.qmd` ya no incluye `_book/srs.qmd` ni el contenedor SSM temporalmente incompleto.
- Los ocho paquetes scenario aceptados están bajo `oq/run/scenario/S1/`.
- Corrida scenario completada en `arm2v4d-scenario-20260916`, pane `%71`, PID inicial 59563, cwd `/Users/averrik/Cloud/github/projects/AR-M2V4D/oq`, comando `oqt --run --server http://127.0.0.1:8800 --mode scenario --model S1 --site CFD`; sin `--force` ni overrides. Cálculos 16–23 observados completos.
- La sesión tmux ya inactiva `arm2v4d-scenario-20260916` fue retirada después de observar su pane en `zsh`; no quedan cálculos locales bajo esa sesión.
- Ocho familias scenario aceptadas en `oq/output/scenario/S1/CFD/`.
- `.gitignore` ahora limita el ignore de `data` a `/data/`, permite versionar `oq/data` y excluye solamente scratch/run/logs de OpenQuake.
- `oqt --process --steps mce` completó y publicó productos bajo `oq/mce/` y `oq/data/`.
- `oqt --process --steps mcer` completó y publicó `oq/data/ASCETable.Rds`.
- `oqt --process --steps deq` completó y publicó `oq/data/DEQTable.Rds`.
- `oqt --process --steps ts` falló por contrato incompleto (`lo.min` ausente); no existe todavía `ShearTable` nuevo y no se lanzaron dn/kmax.
- El snapshot reconstruido conserva el archivado `report`/`oq` anterior bajo `legacy/` y la preparación/resultados nuevos, pero excluye `CAPR003324_Crawford_SeismicHazard_20260831.docx` tanto del worktree como del índice.

## Blocker

La familia geotécnica/Newmark no puede completarse sin parámetros científicos aprobados y, para conservar las cinco geometrías irregulares, sin ampliar el contrato público de `oqt --process --steps ts`; faltan `lo.min`, `lo.max`, `s.min`, `s.max`, `uscs`, `IDm`, `Mw.gmdp`, `NS`, `subduction` y `Da.gmdp`. No se copiarán defaults de otros proyectos.

## Next

NEXT-ID {"action":"Si HEAD/upstream todavía no contienen el snapshot reconstruido y revisado, crear una vez su commit y push fast-forward; cuando sean iguales, no repetir y esperar el contrato científico requerido para ts,dn,kmax.","id":"generate-oq-data-20260916.rewrite-push.v1"}

## Status

ACTIVE
