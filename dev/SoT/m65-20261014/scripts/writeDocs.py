"""Write data/newmark/PROCEDENCIA.md and dev/SoT/m65-20261014/RESULTADOS.md
from the task's logs, hashes and the magnitude map. Run after combine2.R,
postCheck2.R and compareTables2.R."""
import csv, pathlib, collections
T = pathlib.Path('dev/SoT/m65-20261014')
def read(p): return pathlib.Path(p).read_text(encoding='utf-8')
def shamap(p):
    out = {}
    for line in read(p).splitlines():
        h, f = line.split('  ', 1); out[f.lstrip('./')] = h
    return out
before = shamap(T/'sha-before.txt'); m65 = shamap(T/'sha-M65.txt'); m55 = shamap(T/'sha-M55.txt'); after = shamap(T/'sha-after.txt')
mapRows = list(csv.DictReader(open(T/'magnitude-map.csv')))
mw = {'data/newmark-M55': '5.5', 'data/newmark-M65': '6.5'}
bySource = collections.OrderedDict()
for r in mapRows: bySource.setdefault(r['source'], []).append(r['demand'])
log = list(csv.DictReader(open(T/'combine2-log.csv')))
files = ['ShearTable.Rds','M2V4D/CFD/PGATable.csv','M2V4D/CFD/DnDraws.Rds','M2V4D/CFD/DnTable.Rds','M2V4D/CFD/kmaxTable.Rds','DnTable.Rds','DnPlotTable.Rds','kmaxTable.Rds']
def fmt(n): return f'{int(n):,}'.replace(',', ' ')
def rowsOf(prod):
    parts = [r for r in log if r['product'] == prod]
    return ' + '.join(f"{fmt(r['rows'])} ({mw[r['source']]})" for r in parts) + f" = {fmt(parts[0]['total'])}" if parts else 'sin cambio'
runlog55 = read(T/'newmark-M55-run.log'); runlog65 = read(T/'newmark-M65-run.log')
warn = lambda s: [l for l in s.splitlines() if 'beyond sampled support' in l and l.startswith('2:')][0].strip()

P = []; A = P.append
A('# Procedencia de los productos Newmark de data/newmark/'); A('')
A('Fecha de combinación: 2026-10-14. Productor: newmark 1.7.1 (CLI `/usr/local/libexec/newmark/main.R`, librería R newmark 1.7.1, data.table 1.18.6.1). Tarea: `dev/SoT/m65-20261014/`.'); A('')
A('## Qué contiene cada archivo'); A('')
A('Los productos de este directorio son una **combinación por período de retorno de dos corridas** de `newmark process --steps dn,kmax` sobre el mismo `ShearTable.Rds`, los mismos `UHSRock.Rds` y `MCETable.Rds` de hazard y el mismo `specs/calcs/classical/M2V4D.json`, con contratos que sólo difieren de `newmark.json` en `Mw.gmdp` y `path.products`. Magnitudes asignadas por el propietario el 2026-10-14 («quiero 5000 a 10000 y MCE con 6.5 y 500 a 2500 con 5.5»; «100 y 200, tambien 5.5»). Ninguna fila conserva la generación Mw 7 anterior, que queda en el commit `fffd4d6`.'); A('')
A('| Filas (`ID`, `TR`) | Corrida de origen | Contrato | `Mw.gmdp` | SHA-256 de la corrida |'); A('|---|---|---|---|---|')
for src, dems in bySource.items():
    tag = src.split('-')[-1]
    A(f"| `M2V4D`, TR {', '.join(d for d in dems if d != 'MCE')}{' y `MCE` (TR `NA`)' if 'MCE' in dems else ''} | `{src}/`, corrida del 2026-10-14 | `newmark-{tag}.json` | {mw[src]} | `dev/SoT/m65-20261014/sha-{tag}.txt` |")
A(''); A('Archivos combinados, filas por magnitud y SHA-256 del combinado:'); A('')
A('| Archivo | Filas | SHA-256 |'); A('|---|---|---|')
for f in files: A(f'| `{f}` | {rowsOf(f)} | `{after[f]}` |')
A(''); A(f"Sin cambios respecto de la generación anterior: `ShearTable.Rds` (`{after['ShearTable.Rds']}`) y `M2V4D/CFD/PGATable.csv` (`{after['M2V4D/CFD/PGATable.csv']}`); las dos corridas produjeron un `PGATable.csv` byte a byte idéntico, porque la PGA de sitio no depende de la magnitud.")
A(''); A('## Semilla'); A('')
A('Ambas corridas se lanzaron con `--seed 20260915`, el valor indicado por el propietario como el de los productos actuales. Según `newmark --help` y el código instalado (`runProcess`, líneas 19–20 y 41–42 del volcado `dev/SoT/m65-20261014/newmark-1.7.1-functions.txt`), `--seed` sólo gobierna el paso `ts`, que no se corrió; `dn` fija su semilla por celda con `.dnSeed(sitio, demanda, TR)`, sin intervención de la magnitud. Se verificó que las realizaciones muestreadas (`PGA.s` y los `Dn` de AM88, que no dependen de Mw) de `DnDraws.Rds` son idénticas entre las corridas en todas las celdas (`verifyRun-M65.log`, `verifyRun-M55.log`), de modo que la combinación usa, celda por celda, las mismas realizaciones aleatorias que una corrida única.')
A(''); A('## Advertencia'); A('')
A('**Una corrida de `newmark process` con los pasos `dn` o `kmax` sobre `newmark.json`, que declara un único `Mw.gmdp`, reemplaza estos archivos y deshace la combinación**: volvería a escribir todos los TR y el MCE con esa única magnitud. Para regenerar esta combinación hay que repetir las corridas por magnitud y la combinación documentadas en `dev/SoT/m65-20261014/` (`scripts/combine2.R` con `magnitude-map.csv`), o declarar antes con el propietario otro procedimiento.')
A(''); A('Advertencias del productor sobre raíces fuera del soporte muestreado, conservadas en los logs de la tarea:'); A('')
A(f'- Mw 6.5 (`newmark-M65-run.log`): `{warn(runlog65)}`'); A(f'- Mw 5.5 (`newmark-M55-run.log`): `{warn(runlog55)}`')
A('- Mw 7 (generación anterior, auditoría del 2026-09-22): 95 696/737 280 filas.')
pathlib.Path('data/newmark/PROCEDENCIA.md').write_text('\n'.join(P) + '\n', encoding='utf-8')

R = []; A = R.append
A('# Resultados: productos Newmark combinados por TR con Mw 5.5 y Mw 6.5'); A('')
A('Tarea `dev/SoT/m65-20261014/`, 2026-10-14. Proyecto AR-M2V4D, sitio CFD. Productor newmark 1.7.1, data.table 1.18.6.1, R con `Rscript --vanilla`. Estado en `STATE.md`.'); A('')
A('## Resumen'); A('')
A('- Commit base antes de cambiar nada: `fffd4d65089c86a00cea20347c882244de9aab0e`, «Freeze the project before the M6.5 Newmark recalculation», autor y committer Alejandro Verri Kozlowski, sin atribución a IA, 1091 rutas; push a `origin/main` con 464 objetos LFS (606 MB). Log `push-20261014.log`. Quedaron sin seguimiento `html/`, `.idea/`, `.claude/` y `.agents/`.')
A('- Reparto de magnitudes del propietario (`magnitude-map.csv`): TR 100, 200, 500, 1000, 2000 y 2500 con Mw 5.5; TR 5000, 10000 y MCE con Mw 6.5. Sustituye al reparto del brief inicial (Mw 7 hasta TR 5000), cuya combinación se publicó y verificó primero y fue reemplazada sin commit.')
A('- `newmark.json` y `data/newmark/ShearTable.Rds` no se modificaron. `newmark-M65.json` y `newmark-M55.json` difieren de `newmark.json` sólo en `path.products` y `Mw.gmdp`.')
A('- Corridas `newmark process newmark-M65.json --root . --steps dn,kmax --seed 20260915` (17:29:51 a 17:35:35) y `newmark process newmark-M55.json ...` (ver log), ambas exit 0. `--seed` sólo gobierna `ts`, que no se corrió; se pasó por instrucción.')
A('- `PGATable.csv` de ambas corridas es idéntico byte a byte al actual; las filas de desplazamiento de los modelos con Mw (BT07, BM19 y, por ellos, `flexible` y `ensemble`) cambian; AM88, JB07, SR08 y `rigid` no cambian.')
A('- Combinación publicada en `data/newmark/` con `scripts/combine2.R` y verificada con `scripts/postCheck2.R`, con `PROCEDENCIA.md` al lado. Sin commit de productos: pendiente de la palabra del propietario.'); A('')
A('## SHA-256 antes y después de cada producto de `data/newmark/`'); A('')
A('| Archivo | Antes (Mw 7, 2026-10-12) | Corrida Mw 5.5 | Corrida Mw 6.5 | Después (combinado) | Filas por magnitud |'); A('|---|---|---|---|---|---|')
for f in files: A(f'| `{f}` | `{before[f]}` | `{m55[f]}` | `{m65[f]}` | `{after[f]}` | {rowsOf(f)} |')
A(''); A('`DnPlotTable.Rds` no conserva el número de filas de la generación anterior porque la librería omite las filas con Dn ≤ 1e-4 cm; los bloques por TR se tomaron completos de cada corrida.'); A('')
A('## Logs de las corridas'); A('')
for tag, name in (('M65', 'Mw 6.5'), ('M55', 'Mw 5.5')):
    A(f'### {name}: dry-run (`newmark-{tag}-dryrun.log`)'); A(''); A('```'); A(read(T/f'newmark-{tag}-dryrun.log').rstrip()); A('```'); A('')
    A(f'### {name}: corrida (`newmark-{tag}-run.log`)'); A(''); A('```'); A(read(T/f'newmark-{tag}-run.log').rstrip()); A('```'); A('')
    A(f'### {name}: verificación contra la generación Mw 7 (`verifyRun-{tag}.log`)'); A(''); A('```'); A(read(T/f'verifyRun-{tag}.log').rstrip()); A('```'); A('')
A('Lectura de las verificaciones: `nDiff` cuenta las filas cuyo valor cambia respecto de Mw 7. En `DnTable` cambian las filas de BT07, BM19, `flexible` y `ensemble`; las de AM88, JB07, SR08 y `rigid` son idénticas porque esos modelos no usan Mw. Las grillas `ky` son idénticas en las 360 celdas y comunes a todas (PGA media < 0.8 g). En `DnDraws`, `PGA.s` y los `Dn` de AM88 son idénticos en todas las celdas: la corriente aleatoria por celda no depende de Mw. `maxRel` = 1 en `kmaxTable` corresponde a filas con kmax que cae a 0 o a valores del orden de 1e-4 g en demandas bajas y `Da` grandes (`inspectKmaxZeros.log`, calculado para Mw 6.5).'); A('')
A('### Combinación (`combine2.log`)'); A(''); A('```'); A(read(T/'combine2.log').rstrip()); A('```'); A('')
A('### Verificación independiente del publicado (`postCheck2.log`)'); A(''); A('```'); A(read(T/'postCheck2.log').rstrip()); A('```'); A('')
A(read(T/'paso5-citas.md').rstrip()); A('')
A('## Tablas comparativas: generación Mw 7 frente a los productos publicados'); A('')
A('Celdas `Mw 7 / Mw nuevo (diferencia relativa %)`, con la diferencia relativa definida como 100·(nuevo − Mw 7)/Mw 7. kmax y Dn son los del modelo `ensemble` con `p = mean`, el estadístico que publican las tablas del informe. Para kmax, cada geometría se muestra en sus propios objetivos relativos `Da = signif(DaH·Hs, 6)` con `DaH` del contrato; para Dn se muestran siete de los 30 `ky` de la grilla común. Resúmenes para las nueve demandas; tablas por celda para TR 10000 y MCE, como pedía el brief; todas las celdas en `kmax-compare.csv` y `dn-compare.csv` (`scripts/compareTables2.R`).'); A('')
A(read(T/'compare-tables.md').rstrip()); A('')
A('## Desagregación consultada'); A('')
A('A pedido del propietario se resumió la desagregación propia del proyecto (`data/hazard/disagg/M2V4D/CFD/RMwTable.Rds`) en `disagg-Mw-by-TR.csv` y `disagg-Mw-by-TR.log` (Mw media, modal, mediana y percentil 84 por período y TR); los períodos de los taludes están en `shear-periods.log`. El reparto de magnitudes es decisión del propietario; estos resúmenes no lo modifican. El DOCX de desagregación anunciado no fue entregado durante la tarea.'); A('')
A('## Archivos de la tarea'); A('')
A('- Estado y entrega: `STATE.md`, `RESULTADOS.md`, `paso5-citas.md`, `newmark-1.7.1-functions.txt`, `magnitude-map.csv`.')
A('- Hashes: `sha-before.txt`, `sha-M65.txt`, `sha-M55.txt`, `sha-after.txt`, `combine-log.csv` (primera combinación, superada), `combine2-log.csv`.')
A('- Logs: `push-20261014.log`, `newmark-M65-dryrun.log`, `newmark-M65-run.log`, `newmark-M55-dryrun.log`, `newmark-M55-run.log`, `verifyRun-M65.log`, `verifyRun-M55.log`, `combine.log` y `postCheck.log` (primera combinación), `combine2.log`, `postCheck2.log`, `inspectKmaxZeros.log`, `disagg-Mw-by-TR.log`, `shear-periods.log`.')
A('- Scripts R (`scripts/`): `inspectLibrary.R`, `dumpFunctions.R`, `scanSeed.R`, `dumpMore.R`, `inspectProducts.R`, `verifyRun.R`, `combine.R`, `postCheck.R`, `compareTables.R`, `inspectKmaxZeros.R`, `disaggMw.R`, `combine2.R`, `postCheck2.R`, `compareTables2.R`; generador de este informe `writeDocs.py`.')
A('- Comparaciones: `compare-tables.md`, `kmax-compare.csv`, `dn-compare.csv`, `disagg-Mw-by-TR.csv`.')
(T/'RESULTADOS.md').write_text('\n'.join(R) + '\n', encoding='utf-8')
print('PROCEDENCIA.md and RESULTADOS.md written')
