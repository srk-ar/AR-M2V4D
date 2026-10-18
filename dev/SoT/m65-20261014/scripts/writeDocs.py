"""Write data/newmark/PROCEDENCIA.md and dev/SoT/m65-20261014/RESULTADOS.md
from the task's logs, hashes and the magnitude map, for the generation of
2026-10-15 (hazard NBCC + CAN deduplicated; same magnitude map as 2026-10-14).
Run after combine2.R, postCheck2.R and compareTables2.R. The 2026-10-14
version of this generator is kept in logs-m65-20261014-old-hazard/."""
import csv, pathlib, collections
T = pathlib.Path('dev/SoT/m65-20261014')
def read(p): return pathlib.Path(p).read_text(encoding='utf-8')
def shamap(p):
    out = {}
    for line in read(p).splitlines():
        h, f = line.split('  ', 1); out[f.lstrip('./')] = h
    return out
before = shamap(T/'sha-before-20261015.txt'); m65 = shamap(T/'sha-M65.txt'); m55 = shamap(T/'sha-M55.txt'); after = shamap(T/'sha-after.txt')
mapRows = list(csv.DictReader(open(T/'magnitude-map.csv')))
mw = {'data/newmark-M55': '5.5', 'data/newmark-M65': '6.5'}
bySource = collections.OrderedDict()
for r in mapRows: bySource.setdefault(r['source'], []).append(r['demand'])
log = list(csv.DictReader(open(T/'combine2-log.csv')))
files = ['ShearTable.Rds','M2V4D/CFD/PGATable.csv','M2V4D/CFD/DnDraws.Rds','M2V4D/CFD/DnTable.Rds','M2V4D/CFD/kmaxTable.Rds','DnTable.Rds','DnPlotTable.Rds','kmaxTable.Rds']
def fmt(n): return f'{int(n):,}'.replace(',', ' ')
def rowsOf(prod):
    parts = [r for r in log if r['product'] == prod]
    return ' + '.join(f"{fmt(r['rows'])} ({mw[r['source']]})" for r in parts) + f" = {fmt(parts[0]['total'])}" if parts else 'copiado de la corrida (idéntico en ambas)' if prod == 'M2V4D/CFD/PGATable.csv' else 'sin cambio'
runlog55 = read(T/'newmark-M55-run.log'); runlog65 = read(T/'newmark-M65-run.log')
warn = lambda s: [l for l in s.splitlines() if 'beyond sampled support' in l and l.startswith('2:')][0].strip()
HazardNote = ('Insumos de hazard de la generación del 2026-10-15: modelo de fuentes `ssm/CAN` deduplicado (zonas de fondo del cratón sin triple conteo, rama `issue/CAN-dedup-backgrounds` de `~/kashimaDB/openquake/ssm`, commit `87643c7`), árboles GMM oficiales NBCC 2020 (`gmm/TRT/<TRT>/gmmLT_NBCC.xml`) con el seed SCC extendido a los 32 períodos de la casa por interpolación en log(T) de los pesos oficiales (`scripts/interpolateNBCCWeights.R`), 24 celdas clásicas y de escenario más la desagregación calculadas en OpenQuake 3.26.2 (tms9900 cálculos 59–71, motor local 78–89), extraídas el 2026-10-15 y procesadas con hazard 0.2.0 (AEP, UHS, DEQ, SAEP, RMw a la 01:28; MCE y MCER a las 09:47 tras la corrección del lector de realizations, commit `88d3aee` de hazard). `UHSRock.Rds` y `MCETable.Rds` consumidos por newmark son los de esas horas. Extensión del 2026-10-17 (orden del propietario, brief del 2026-10-17): los escenarios S1 y S2 se calcularon también en Vs30 220, 580 y 910 (motor local, cálculos 93–98) y `hazard process --steps mce,mcer,deq` con hazard 0.2.1 (Packaged 2026-10-17) extendió `MCETable.Rds` (22 792 filas, 11 Vs30, SHA-256 `9e9a6b8c4dfdaaa67daec504cc75da8a1bd429bb29acc2f77a8fad2aed0530ae`), `ASCETable.Rds` (1056 filas, `9c5d83f5531e7bda566776d4008879edee95875711af2a713f0c0671750efdd7`) y `DEQTable.Rds` (67 584 filas, `da620981899c42bc5af4dcde652f3f149176a8e6e611980abb3dd2e700c4cad6`) a las 21:50 del 2026-10-17; las filas de los ocho Vs30 anteriores, incluidas las de 760 que consume newmark, son idénticas a las previas (`dev/SoT/m65-20261014/checkMcerExtension-20261017.log`), y `UHSRock.Rds`, `UHSTable.Rds`, `AEPTable.Rds`, `RMwTable.Rds` y todos los productos de este directorio conservan su SHA-256. Los productos Newmark no se recalcularon ni cambiaron.')

P = []; A = P.append
A('# Procedencia de los productos Newmark de data/newmark/'); A('')
A('Fecha de combinación: 2026-10-15. Productor: newmark 1.7.1 (CLI `/usr/local/libexec/newmark/main.R`, librería R newmark 1.7.1, data.table 1.18.6.1). Tarea: `dev/SoT/m65-20261014/`. Reemplaza la combinación del 2026-10-14 (commit `dddf10b`), calculada sobre el hazard anterior con el mismo reparto de magnitudes.'); A('')
A('## Qué contiene cada archivo'); A('')
A('Los productos de este directorio son una **combinación por período de retorno de dos corridas** de `newmark process --steps dn,kmax` sobre el mismo `ShearTable.Rds`, los mismos `UHSRock.Rds` y `MCETable.Rds` de hazard y el mismo `specs/calcs/classical/M2V4D.json`, con contratos que sólo difieren de `newmark.json` en `Mw.gmdp` y `path.products`. Magnitudes asignadas por el propietario el 2026-10-14 («quiero 5000 a 10000 y MCE con 6.5 y 500 a 2500 con 5.5»; «100 y 200, tambien 5.5»). ' + HazardNote); A('')
A('| Filas (`ID`, `TR`) | Corrida de origen | Contrato | `Mw.gmdp` | SHA-256 de la corrida |'); A('|---|---|---|---|---|')
for src, dems in bySource.items():
    tag = src.split('-')[-1]
    A(f"| `M2V4D`, TR {', '.join(d for d in dems if d != 'MCE')}{' y `MCE` (TR `NA`)' if 'MCE' in dems else ''} | `{src}/`, corrida del 2026-10-15 | `newmark-{tag}.json` | {mw[src]} | `dev/SoT/m65-20261014/sha-{tag}.txt` |")
A(''); A('Archivos combinados, filas por magnitud y SHA-256 del combinado:'); A('')
A('| Archivo | Filas | SHA-256 |'); A('|---|---|---|')
for f in files: A(f'| `{f}` | {rowsOf(f)} | `{after[f]}` |')
A(''); A(f"`ShearTable.Rds` (`{after['ShearTable.Rds']}`) no cambia: es el del 2026-10-12, calculado con newmark 1.7.1 y el período del talud medido desde el ápice. `M2V4D/CFD/PGATable.csv` (`{after['M2V4D/CFD/PGATable.csv']}`) sí cambia respecto de la generación anterior porque la PGA de sitio viene del hazard nuevo; las dos corridas produjeron un `PGATable.csv` byte a byte idéntico, porque la PGA de sitio no depende de la magnitud, y se publicó el de la corrida.")
A(''); A('## Semilla'); A('')
A('Ambas corridas se lanzaron con `--seed 20260915`, el valor indicado por el propietario como el de los productos actuales. Según `newmark --help` y el código instalado (`runProcess`, líneas 19–20 y 41–42 del volcado `dev/SoT/m65-20261014/newmark-1.7.1-functions.txt`), `--seed` sólo gobierna el paso `ts`, que no se corrió; `dn` fija su semilla por celda con `.dnSeed(sitio, demanda, TR)`, sin intervención de la magnitud ni del hazard, de modo que la combinación usa, celda por celda, las mismas realizaciones aleatorias que una corrida única.')
A(''); A('## Advertencia'); A('')
A('**Una corrida de `newmark process` con los pasos `dn` o `kmax` sobre `newmark.json`, que declara un único `Mw.gmdp`, reemplaza estos archivos y deshace la combinación**: volvería a escribir todos los TR y el MCE con esa única magnitud. Para regenerar esta combinación hay que repetir las corridas por magnitud y la combinación documentadas en `dev/SoT/m65-20261014/` (`scripts/combine2.R` con `magnitude-map.csv`, luego copiar `PGATable.csv` de una corrida), o declarar antes con el propietario otro procedimiento.')
A(''); A('Advertencias del productor sobre raíces fuera del soporte muestreado, conservadas en los logs de la tarea:'); A('')
A(f'- Mw 6.5 (`newmark-M65-run.log`): `{warn(runlog65)}`'); A(f'- Mw 5.5 (`newmark-M55-run.log`): `{warn(runlog55)}`')
pathlib.Path('data/newmark/PROCEDENCIA.md').write_text('\n'.join(P) + '\n', encoding='utf-8')

R = []; A = R.append
A('# Resultados: generación de hazard NBCC 2020 con CAN deduplicado y productos Newmark combinados por TR'); A('')
A('Tarea `dev/SoT/m65-20261014/`, 2026-10-14 y 2026-10-15. Proyecto AR-M2V4D, sitio CFD. Productores hazard 0.2.0 (reinstalada el 2026-10-15 con la corrección del lector de realizations), newmark 1.7.1, data.table 1.18.6.1, OpenQuake 3.26.2, R con `Rscript --vanilla`. Estado en `STATE.md`; hallazgos sobre los árboles y el modelo de fuentes en `can-trt-hallazgos.md`. La entrega anterior de esta tarea (combinación por magnitudes sobre el hazard anterior, 2026-10-14) está en el commit `dddf10b` y sus logs en `logs-m65-20261014-old-hazard/`.'); A('')
A('## Resumen'); A('')
A('- Modelo de fuentes: `ssm/CAN` reescrito sin el triple conteo de las zonas de fondo del cratón (piloto cálculo 34 en tms9900: cocientes 0.930–0.947 a TR 2475 frente a la generación commiteada; detalle en `can-trt-hallazgos.md` §5). El modelo anterior queda en `CAN/legacy/v2020.1.4`.')
A('- Árboles GMM: tokens `NBCC` en los cinco TRT de las recetas clásica, de escenario y de desagregación (`specs/calcs/`). El seed SCC trae los pesos oficiales por IMT y, desde el 2026-10-15, un peso interpolado en log(T) para cada uno de los 32 períodos de la casa (`scripts/interpolateNBCCWeights.R`; nodos oficiales intactos; suma exacta 0.5 por período). Sin esa extensión OpenQuake aplicaba el peso base en los 21 períodos no listados y el espectro salía aserrado; esa generación se abortó y se reemplazó (§7 de los hallazgos).')
A('- Cálculos: 25 celdas lanzadas el 2026-10-14 a las 23:51 y terminadas a la 01:24 (tms9900: clásicas 59–62 para Vs30 1250, 180, 360 y 760, escenarios 63–70, desagregación 71; motor local: clásicas 78–81 para 1500, 270, 560 y 800, escenarios 82–89). Extraídas a `data/hazard/output` reemplazando las familias de `dddf10b`, que quedan en git.')
A('- Celda 760 frente a la corrida 2024 (`nbcc-interp-vs-nrc2024-760.txt`): espectro liso en los 32 períodos; a TR 2475, PGA 1.10, SA 0.05–0.3 s entre 0.80 y 0.94, SA 0.35–4 s entre 0.79 y 0.89.')
A('- Posproceso: `hazard process` con AEP, UHS, DEQ, SAEP y RMw (01:28) y, tras la corrección de hazard (`88d3aee`, defecto `BUG-MCE-REALIZATIONS-MULTILINE-20261015`), MCE y MCER (09:47). Sin el paso `gmpe` (`GMPETable.Rds` sigue siendo del 2026-09-23 por el defecto del token reportado el 2026-10-14) ni `rmw` previo distinto del corrido.')
A('- Newmark: corridas `newmark process newmark-M65.json --root . --steps dn,kmax --seed 20260915` (09:48–09:54) y `newmark-M55.json` (09:54–10:00), ambas exit 0, con el mismo reparto de magnitudes del 2026-10-14 (`magnitude-map.csv`). Combinación publicada en `data/newmark/` con `scripts/combine2.R`, `PGATable.csv` publicado desde la corrida, verificada con `scripts/postCheck2.R` (`ALL CHECKS PASSED: TRUE`), `PROCEDENCIA.md` al lado.')
A('- Capítulos `_chapters/ts.model.md` y `.es.md` rehidratados desde el scaffold `reports/sha` (ecuación de T_s con la altura desde el ápice, coherente con `ShearTable.Rds`).')
A('- Sin commit de productos: pendiente de la palabra del propietario. Render pendiente de la selección de artefactos.'); A('')
A('## SHA-256 antes y después de cada producto de `data/newmark/`'); A('')
A('| Archivo | Antes (hazard anterior, `dddf10b`, 2026-10-14) | Corrida Mw 5.5 | Corrida Mw 6.5 | Después (combinado) | Filas por magnitud |'); A('|---|---|---|---|---|---|')
for f in files: A(f'| `{f}` | `{before[f]}` | `{m55[f]}` | `{m65[f]}` | `{after[f]}` | {rowsOf(f)} |')
A(''); A('`DnPlotTable.Rds` no conserva el número de filas de la generación anterior porque la librería omite las filas con Dn ≤ 1e-4 cm; los bloques por TR se tomaron completos de cada corrida.'); A('')
A('## Logs de las corridas'); A('')
for tag, name in (('M65', 'Mw 6.5'), ('M55', 'Mw 5.5')):
    A(f'### {name}: dry-run (`newmark-{tag}-dryrun.log`)'); A(''); A('```'); A(read(T/f'newmark-{tag}-dryrun.log').rstrip()); A('```'); A('')
    A(f'### {name}: corrida (`newmark-{tag}-run.log`)'); A(''); A('```'); A(read(T/f'newmark-{tag}-run.log').rstrip()); A('```'); A('')
    A(f'### {name}: verificación contra la corrida del 2026-10-14 con la misma magnitud (`verifyRun-{tag}.log`)'); A(''); A('```'); A(read(T/f'verifyRun-{tag}.log').rstrip()); A('```'); A('')
A('Lectura de las verificaciones: la referencia es la corrida de la misma magnitud sobre el hazard anterior, así que `nDiff` cuenta las filas cuyo valor cambia por el hazard; la estructura, las clases y la clave son las mismas y todas las filas de `DnTable` y `kmaxTable` se emparejan por clave. `DnPlotTable` empareja menos filas porque su contenido depende de los valores.'); A('')
A('### Combinación (`combine2.log`)'); A(''); A('```'); A(read(T/'combine2.log').rstrip()); A('```'); A('')
A('### Verificación independiente del publicado (`postCheck2.log`)'); A(''); A('```'); A(read(T/'postCheck2.log').rstrip()); A('```'); A('')
A('## Tablas comparativas: combinación del 2026-10-14 (hazard anterior) frente a la publicada (hazard NBCC)'); A('')
A('Celdas `anterior / nuevo (diferencia relativa %)`, con la diferencia relativa definida como 100·(nuevo − anterior)/anterior y la misma magnitud en ambos lados. kmax y Dn son los del modelo `ensemble` con `p = mean`, el estadístico que publican las tablas del informe. Para kmax, cada geometría se muestra en sus propios objetivos relativos `Da = signif(DaH·Hs, 6)` con `DaH` del contrato; para Dn se muestran siete de los 30 `ky` de la grilla común. Resúmenes para las nueve demandas; tablas por celda para TR 10000 y MCE; todas las celdas en `kmax-compare.csv` y `dn-compare.csv` (`scripts/compareTables2.R`, referencia = respaldo de `data/newmark` de `dddf10b`). En TR 100 y 200 las diferencias relativas de kmax son erráticas porque muchas celdas tienen kmax casi nulo en una u otra generación; las medianas de TR 500 en adelante y las de Dn describen el cambio.'); A('')
A(read(T/'compare-tables.md').rstrip()); A('')
A('## Archivos de la tarea'); A('')
A('- Estado y entrega: `STATE.md`, `RESULTADOS.md`, `can-trt-hallazgos.md`, `magnitude-map.csv`, `paso5-citas.md`, `newmark-1.7.1-functions.txt`.')
A('- Hashes: `sha-before-20261015.txt` (combinación del 2026-10-14), `sha-M65.txt`, `sha-M55.txt`, `sha-after.txt`, `combine2-log.csv`; los del 2026-10-14 en `logs-m65-20261014-old-hazard/`.')
A('- Logs de hazard: `hazard-pack-*-nbcc-interp-20261014.log`, `hazard-run-{remote,local}-nbcc-interp-20261014.log`, `hazard-abort-sawtooth-20261014.log`, `hazard-extract-760-nbcc-interp-20261015.log`, `hazard-extract-all-nbcc-interp-20261015.log`, `hazard-process-nbcc-interp-20261015.log`, `hazard-process-mce-mcer-nbcc-interp-20261015.log`, `codex-audit-mce-20261015.{log,md}`, `ngr-pull-ts-model-20261015.log`.')
A('- Logs de newmark: `newmark-chain-nbcc-20261015.log`, `newmark-M65-dryrun.log`, `newmark-M65-run.log`, `newmark-M55-dryrun.log`, `newmark-M55-run.log`, `verifyRun-M65.log`, `verifyRun-M55.log`, `combine2.log`, `postCheck2.log`.')
A('- Comparaciones: `nbcc-interp-vs-nrc2024-760.txt`, `nbcc-vs-nrc2024-760.txt` (generación aserrada), `pilot-vs-committed-760.txt`, `compare-tables.md`, `kmax-compare.csv`, `dn-compare.csv`.')
A('- Scripts (`scripts/`): `interpolateNBCCWeights.R`, `dedupCAN.py`, `compareNBCC.py`, `comparePilot.py`, `compareHazard.py`, `gmmTrees.py`, `verifyRun.R`, `combine2.R`, `postCheck2.R`, `compareTables2.R`; generador de este informe `writeDocs.py`.')
A('- Revisión del DOCX de Diana Reyes: `docx-review/` (inventarios A1 y A2, base `base/gmdp.memo.en.md`, mapeo B).')
(T/'RESULTADOS.md').write_text('\n'.join(R) + '\n', encoding='utf-8')
print('PROCEDENCIA.md and RESULTADOS.md written')
