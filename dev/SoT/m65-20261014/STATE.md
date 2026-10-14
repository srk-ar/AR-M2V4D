## Objective

Recalcular DnTable y kmaxTable con Mw 6.5 para TR 10000 y MCE, manteniendo Mw 7 para TR 100 a 5000, y publicar los productos combinados en data/newmark/, según el brief de ocho pasos del propietario del 2026-10-14.

## Rulings

- Brief del 2026-10-14: traer newmark, continuity, git y datatable; estado en dev/SoT/m65-20261014/STATE.md; antes de cambiar nada, commit y push del estado actual del proyecto con identidad humana y sin atribución a IA; no modificar newmark.json ni ShearTable.Rds (validación externa en curso); newmark-M65.json copia de newmark.json con Mw.gmdp 6.5 y path.products data/newmark-M65; copiar ShearTable.Rds a data/newmark-M65/ y verificar SHA-256 igual; correr newmark process newmark-M65.json --root . --steps dn,kmax --seed 20260915; verificar PGATable.csv igual y filas Dn distintas; imprimir newmark:::buildDnTables y newmark:::buildKmaxTable y citar líneas de seed por (sitio, demanda, TR) y de inversión kmax por (ID, TR, IDg, IDm); combinar por TR con data.table preservando claves, columnas y atributos; publicar en data/newmark/ con PROCEDENCIA.md; entregar RESULTADOS.md; sin instalar, sin tocar librerías, R en scripts; commit final de productos sólo con la palabra del propietario; preguntar toda duda no verificable con la línea que la origina.
- Mensaje posterior del propietario: «queremos recalcular kmax, Dn etc, con M=6.5 en lugar de M=7». Se lee como resumen del brief. Si significara reemplazo total de todos los TR por Mw 6.5, es decisión pendiente del propietario; no se infiere.
- El checkout real es /Users/averrik/Cloud/github/projects/AR-M2V4D; /Users/averrik/github es symlink a Cloud/github. El comando de skills se corre como lo imprime el catálogo.
- Los nombres exactos de los pasos según newmark --help y el skill son dn y kmax. --seed sólo afecta ts; dn usa seeds propios por celda de demanda. Se pasa --seed 20260915 por instrucción y se documenta que no gobierna dn ni kmax.
- Alcance del commit inicial: contenido del proyecto rastreado y sin seguimiento. Se excluyen html/ sin seguimiento (declarado «ignored at tip» en .gitattributes), .idea/, .claude/ y .agents/ (copias de skills y configuración IDE, no rastreadas en proyectos hermanos). Exclusión informada al propietario; puede ampliarla.
- El estado render-project-20260918 queda sin seleccionar por el brief; no se cierra ni se ejecuta su Next.
- Hashes SHA-256 de data/newmark/ antes de cambiar nada (archivos del 2026-10-12 18:04–18:10): DnPlotTable.Rds 4c8a6d43d13003b598e916fa12b7ab80abc10f62a4b767096f1d029d419a2eb2; DnTable.Rds 965496bed913989bc4f473d538bbcb736a2fa266fa42606ff18fab489ccb2d02; kmaxTable.Rds 138d031b9ab093e736f9a6480485c24ea5349c47dcdd092293e3316abc52f2f7; M2V4D/CFD/DnDraws.Rds 91854c3eed722d46f957a9e7db24aafcc7bbac93f0669af9671c93cb914d9254; M2V4D/CFD/DnTable.Rds 965496be…; M2V4D/CFD/kmaxTable.Rds 138d031b…; M2V4D/CFD/PGATable.csv 325fb141ea5126a46bd0baf82b89a76d03a4cc86adc36f3b74ac770f9b6c8cbf; ShearTable.Rds 334359667159dd8f928c54d4f40484af1162372a0e4114aee666691104b3cf29. Difieren de newmark-audit-20260922.json: hubo un recálculo posterior no commiteado.

## Evidence and no-repeat

- Skills traídos y leídos el 2026-10-14: continuity afc7857f, newmark 0f23adf7, git c8bf4136, datatable d741e112.
- Selector dev/SoT/ACTIVE.md apuntado a este estado.

## Effects

none

## Blocker

none

## Next

NEXT-ID {"action":"Paso 1: commit y push del estado actual del proyecto con el skill git, identidad humana configurada, sin atribución a IA, excluyendo html/ sin seguimiento, .idea/, .claude/ y .agents/; registrar el hash.","id":"m65-20261014.commit-baseline.v1"}

## Status

ACTIVE
