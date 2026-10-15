**Veredicto global: PARCIAL.** El fallo está confirmado y lo reproduje en memoria. La explicación de Claude requiere precisiones sobre el lector, los códigos de salida y las modificaciones históricas.

1. **PARCIAL — instalación sin indicios de modificación; OpenQuake declara la misma versión.**

   `cat DESCRIPTION` muestra `hazard 0.2.0`, con `Packaged` y `Built: 2026-10-04 23:29:33 UTC`. Revisé los 32 archivos instalados: **todos sus mtime y ctime son del 4 de octubre**, incluidos `hazard.rdb` y `hazard.rdx`. El ejecutable `/usr/local/bin/hazard` también tiene fecha del 4. [DESCRIPTION leído](/Users/averrik/Library/R/arm64/4.6/library/hazard/DESCRIPTION:24).

   En el checkout, `git status --short` muestra únicamente entradas `??`; `git diff HEAD --` no produce diferencias. Sin embargo, `git log -3 --stat` muestra commits **3272f88, 3a68fd0 y d3ed80d del 14–15 de octubre**, sobre instaladores, configuración AOM y workflow. Por tanto, el checkout sí tuvo cambios; no prueban una modificación de la librería instalada ni permiten atribuirlos a Claude.

   `nl -ba realizations_22.csv` y `nl -ba realizations_66.csv` muestran **`OpenQuake engine 3.26.2`** en ambas cabeceras. Esto confirma la versión declarada, pero no demuestra por sí solo que nadie modificó su código.

2. **CONFIRMADO — lectura corrupta y unión fallida; PARCIAL la atribución a `readLines`.**

   `Rscript --vanilla -e 'print(hazard:::.readOqCsv)'` devuelve:

   ```r
   function (path) {
       FILE <- path
       AUX <- readLines(FILE, warn = FALSE)
       AUX <- AUX[!grepl("^#", AUX)]
       fread(text = paste(AUX, collapse = "\n"))
   }
   ```

   Al ejecutar `str(hazard:::.readOqCsv(...))`:

   | Archivo | Filas | `rlz_id` | `weight` |
   |---|---:|---|---|
   | Septiembre, `realizations_22.csv` | 6 | `int 0 1 2 3 4 5` | numérico |
   | Octubre, `realizations_66.csv` | 32 | `chr`, incluye `"submodel = …"` | lógico, todos `NA` |

   **Los 16 CSV nuevos presentan el mismo defecto.** El archivo 66 contiene realmente 16 registros con campos multilínea entrecomillados. [CSV leído](/Users/averrik/Cloud/github/projects/AR-M2V4D/data/hazard/output/scenario/S1/CFD/760/realizations_66.csv:3).

   Las líneas 24–25 de `deparse(hazard:::.buildBranch)` son:

   ```r
   DT[Events, on = "event_id", `:=`(rup.id = i.rup_id, rlz.id = i.rlz_id)]
   DT[Rlz, on = .(rlz.id = rlz_id), `:=`(model = i.model, weight = i.weight)]
   ```

   Reproduje esa unión con los identificadores leídos: **`Incompatible join types: x.rlz.id (integer) and i.rlz_id (character)`**.

   La precisión causal: **`fread(file=p, skip=1)` también falla**, sin `readLines`. Con `data.table 1.18.6.1`, el problema se reproduce al interpretar este formato concreto. `read.csv(p, skip=1)` y Python `csv` recuperan correctamente las 16 filas; `read.csv` también funciona sobre el texto reconstruido por `readLines` + `paste`.

3. **PARCIAL — regresión coherente, sin constancia explícita de los exit codes.**

   `nl -ba .../{old,new,newflat}/mce.log` muestra:

   | Caso | Evidencia del log |
   |---|---|
   | `old` | `MCETable rows=16576`; `Process complete` |
   | `new` | 16 errores de unión; `ERROR: Process completed with errors` |
   | `newflat` | `MCETable rows=16576`; `Process complete` |

   Esto respalda éxito/fallo/éxito, pero **los logs no registran literalmente los códigos de salida 0/1/0**.

   Los `diff` de `hazard.json` y `specs` entre los tres casos terminaron en **0, sin diferencias**. También coinciden las copias `old` y `new` con sus respectivas exportaciones originales.

   `diff -qr new/data/hazard/output newflat/data/hazard/output` identifica **únicamente los 16 `realizations_*.csv`**: los otros 160 archivos son idénticos. Dentro de esos CSV también se normalizó CRLF→LF y se quitaron algunas comillas exteriores. Comparando los campos mediante un lector CSV, el único cambio de contenido es salto de línea→espacio, en los 16 archivos.

4. **CONFIRMADO — hay omisiones y etiquetas defectuosas.**

   Sustituir **sólo** `"\nsubmodel"` por `" submodel"` en memoria, conservando las comillas originales, produce **16 filas, identificadores enteros y pesos numéricos sin NA**. Esto confirma que el aplanado evita el fallo observado.

   Sin embargo, `readRDS(.../MCEBranchTable.Rds)` muestra 8192 filas y etiquetas como:

   ```text
   CanadaSHM6_StableCrust_NGAEast submodel = """"01""""
   CanadaSHM6_StableCrust_AA13 submodel = """"central
   ```

   Parte de esas comillas anómalas ya está en el CSV original; el aplanado **no resuelve la representación de los nombres**.

   Además, `git diff HEAD -- specs/calcs/scenario/CFD/{S1,S2}.json` muestra el cambio **`"SCC": "SCC"` → `"SCC": "NBCC"`**. Es un cambio relevante del proyecto que introduce los modelos parametrizados y expone el defecto del lector; no hace falta suponer una actualización de OpenQuake para explicar la diferencia.

No modifiqué archivos del proyecto ni de las instalaciones, ni volví a ejecutar `hazard process`.