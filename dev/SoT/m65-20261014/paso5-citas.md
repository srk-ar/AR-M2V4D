## Paso 5: lectura de la librería instalada newmark 1.7.1

`newmark:::buildDnTables` y `newmark:::buildKmaxTable` no existen en el namespace de newmark 1.7.1 (comprobado con `exists()` sobre `asNamespace("newmark")`; script `scripts/inspectLibrary.R`). Las funciones que cumplen esos papeles son `runProcess`, `.dnSeed`, `fitDnProducts`, `.runDnDemand` para el seed, y `fitKmaxProducts`, `.fitKmaxCell`, `fitKmaxScenario` para la inversión. El volcado completo con numeración de líneas está en `newmark-1.7.1-functions.txt` (deparse de cada función; los números de línea citados son los de ese volcado, no los del fuente del paquete, que no se leyó).

### El seed de dn se fija por (sitio, demanda, TR) y no depende de Mw

- `runProcess`, líneas 41–42: `Seeds <- c(vapply(Plan$family, function(tr) .dnSeed(Site, Plan$model, tr), integer(1)), .dnSeed(Site, "MCE", NA_real_))`. Un seed por cada TR del contrato más uno para MCE; los argumentos son el sitio, el identificador del modelo o `"MCE"` y el TR.
- `.dnSeed`, líneas 1–12: `function (siteID, demandID, tr)`; línea 6 `Chars <- utf8ToInt(paste(c(siteID, demandID, Label), collapse = "/"))`; líneas 8–10 hash polinómico módulo 2147483647. Mw no es argumento ni interviene.
- `fitDnProducts`, líneas 16–29: para cada demanda `i` llama `.runDnDemand(..., mw = mw, ..., seed = seeds[[i]])`. Mw entra como escalar separado del seed.
- `.runDnDemand`, líneas 6–8: `if (!is.null(seed)) set.seed(seed)` inmediatamente antes de `fitDnScenarios(...)`.
- `fitDnScenarios`, línea 7: `LIST <- lapply(seq_len(n), function(i) .prepareDnScenario(records[i]))` se ejecuta en serie antes de cualquier `mclapply` (líneas 9–13). `.prepareDnScenario`, líneas 12–13, consume la corriente aleatoria: `.sampleDnScenario(uhs, Ts, NS, zTrunc)` y `eps = stats::rnorm(NS)`. Ninguno recibe Mw.
- `.sampleDnScenario`, líneas 1–50: argumentos `(uhs, Ts, NS, zTrunc)`; muestrea Sa correlacionadas en los períodos 0, 1.3·Ts y 1.5·Ts (líneas 6, 36). Sin Mw.
- Mw sólo aparece en `.drawDnModel`, líneas 4–7, dentro de `Dn_BT07`, `Dn_BM17` y `Dn_BM19`, que reciben `eps` ya sorteado (línea 11–12: `rnorm` sólo si `eps` es NULL; `.fitDnCurvePrepared`, línea 7, siempre pasa `eps`). Por lo tanto, con el mismo ShearTable, UHSRock y MCETable, las realizaciones muestreadas (PGA.s, Sa, eps) de cada celda (sitio, demanda, TR) son idénticas entre una corrida con Mw 7 y otra con Mw 6.5; sólo cambia la transformación determinista de cada realización en Dn.
- `.buildDnRecords`, líneas 6–13 y 25–26: la PGA de `PGATable.csv` sale del ajuste de respuesta de sitio (`.fitSiteProducts` / `.fitSaFConverged`) sin Mw. `getDnKy`, líneas 13–17: la grilla de 30 `ky` depende sólo de la PGA media del UHS (`Ky.max = max(PGA, 0.8)`), no de Mw.

### kmax se invierte por (ID, TR, IDg, IDm)

- `fitKmaxProducts`, líneas 12–17: `Demands` = cada TR del contrato más `("MCE", NA)`; `Cells <- Demands[, .(IDm = Materials), by = .(ID, TR)]`; una llamada a `.fitKmaxCell` por celda (ID, TR, IDm).
- `.fitKmaxCell`, línea 4: `DT <- draws[.(demandID, tr, materialID), on = .(ID, TR, IDm), nomatch = NULL, ...]` toma sólo las realizaciones de esa celda; líneas 12–13 construyen un registro por `IDg`; línea 17 llama `fitKmaxScenarios(records = ScenarioRecords, draws = DT, ...)`.
- `fitKmaxScenario`, línea 17: `DT <- draws[TR == row$TR[[1L]] & IDg == row$IDg[[1L]], ...]`; línea 20 `.buildKmaxScenarioTable(draws = DT, ...)`. `.buildKmaxDraws`, líneas 27 y 65, invierte cada curva por `(IDn, s)` dentro de esa selección. Ninguna otra fila de otro TR entra en la inversión de una celda.
- Globales: `getKmaxTable`, líneas 15–16, `rbindlist` de las tablas por sitio y `setkeyv(DT, KMAXKEY)`; `getDnTables`, líneas 10–12, `rbindlist`, `setkeyv(DT, DNKEY)` y `.buildDnPlotTable(DT)`. `.buildDnPlotTable`, líneas 3–18, agrupa por `c("siteID", "ID", "TR", "IDg", "IDn", "p")` y construye la grilla logarítmica con el `min`/`max` de `ky` del propio grupo (líneas 6–7). Cada fila de los tres globales depende sólo de las filas de su mismo TR, por lo que la combinación fila a fila por TR reproduce lo que produciría la librería con esas mismas filas.

Conclusión verificada en el código instalado: la combinación de TR 100 a 5000 de la corrida Mw 7 con TR 10000 y MCE de la corrida Mw 6.5 usa, para cada celda, las mismas realizaciones aleatorias que una corrida única, y la inversión de kmax de cada (ID, TR, IDg, IDm) no mezcla demandas.
