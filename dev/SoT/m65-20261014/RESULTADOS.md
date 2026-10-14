# Resultados: productos Newmark combinados por TR con Mw 5.5 y Mw 6.5

Tarea `dev/SoT/m65-20261014/`, 2026-10-14. Proyecto AR-M2V4D, sitio CFD. Productor newmark 1.7.1, data.table 1.18.6.1, R con `Rscript --vanilla`. Estado en `STATE.md`.

## Resumen

- Commit base antes de cambiar nada: `fffd4d65089c86a00cea20347c882244de9aab0e`, «Freeze the project before the M6.5 Newmark recalculation», autor y committer Alejandro Verri Kozlowski, sin atribución a IA, 1091 rutas; push a `origin/main` con 464 objetos LFS (606 MB). Log `push-20261014.log`. Quedaron sin seguimiento `html/`, `.idea/`, `.claude/` y `.agents/`.
- Reparto de magnitudes del propietario (`magnitude-map.csv`): TR 100, 200, 500, 1000, 2000 y 2500 con Mw 5.5; TR 5000, 10000 y MCE con Mw 6.5. Sustituye al reparto del brief inicial (Mw 7 hasta TR 5000), cuya combinación se publicó y verificó primero y fue reemplazada sin commit.
- `newmark.json` y `data/newmark/ShearTable.Rds` no se modificaron. `newmark-M65.json` y `newmark-M55.json` difieren de `newmark.json` sólo en `path.products` y `Mw.gmdp`.
- Corridas `newmark process newmark-M65.json --root . --steps dn,kmax --seed 20260915` (17:29:51 a 17:35:35) y `newmark process newmark-M55.json ...` (ver log), ambas exit 0. `--seed` sólo gobierna `ts`, que no se corrió; se pasó por instrucción.
- `PGATable.csv` de ambas corridas es idéntico byte a byte al actual; las filas de desplazamiento de los modelos con Mw (BT07, BM19 y, por ellos, `flexible` y `ensemble`) cambian; AM88, JB07, SR08 y `rigid` no cambian.
- Combinación publicada en `data/newmark/` con `scripts/combine2.R` y verificada con `scripts/postCheck2.R`, con `PROCEDENCIA.md` al lado. Sin commit de productos: pendiente de la palabra del propietario.

## SHA-256 antes y después de cada producto de `data/newmark/`

| Archivo | Antes (Mw 7, 2026-10-12) | Corrida Mw 5.5 | Corrida Mw 6.5 | Después (combinado) | Filas por magnitud |
|---|---|---|---|---|---|
| `ShearTable.Rds` | `334359667159dd8f928c54d4f40484af1162372a0e4114aee666691104b3cf29` | `334359667159dd8f928c54d4f40484af1162372a0e4114aee666691104b3cf29` | `334359667159dd8f928c54d4f40484af1162372a0e4114aee666691104b3cf29` | `334359667159dd8f928c54d4f40484af1162372a0e4114aee666691104b3cf29` | sin cambio |
| `M2V4D/CFD/PGATable.csv` | `325fb141ea5126a46bd0baf82b89a76d03a4cc86adc36f3b74ac770f9b6c8cbf` | `325fb141ea5126a46bd0baf82b89a76d03a4cc86adc36f3b74ac770f9b6c8cbf` | `325fb141ea5126a46bd0baf82b89a76d03a4cc86adc36f3b74ac770f9b6c8cbf` | `325fb141ea5126a46bd0baf82b89a76d03a4cc86adc36f3b74ac770f9b6c8cbf` | sin cambio |
| `M2V4D/CFD/DnDraws.Rds` | `91854c3eed722d46f957a9e7db24aafcc7bbac93f0669af9671c93cb914d9254` | `057752d97987c1d1f21d554b46f13982ab61b165b81a1d4661c017e4b796ef21` | `7ab47777aaf5c983f7548a23f1d7631fa31bd89485b9bc2582aebf3c6b35704c` | `672b43170c22e1a165ef635352c0f1ccc92a2a0106f7a0775cb3b69808d81bac` | 10 800 000 (5.5) + 5 400 000 (6.5) = 16 200 000 |
| `M2V4D/CFD/DnTable.Rds` | `965496bed913989bc4f473d538bbcb736a2fa266fa42606ff18fab489ccb2d02` | `65f7fd737546d2dd56502aec1b87bd69a046ec63832e352082f9e3653a310a08` | `68ef561846ea73c4665f20b702c0c6d996f54c2b13cdb00ed2dd57abd936db91` | `5ee864387c77b973c3d8227b53841147beb2b97dc085a022b8ef033056e4c18c` | 460 800 (5.5) + 230 400 (6.5) = 691 200 |
| `M2V4D/CFD/kmaxTable.Rds` | `138d031b9ab093e736f9a6480485c24ea5349c47dcdd092293e3316abc52f2f7` | `5eddd88a8e489dc4d463e70d3880f3ec9bfbcda0b4c6d6e6054d84caf5841e09` | `c15f44b54b4a91e3d6820787f79790d5b4542ecfed1b12aab75459ab1d311bab` | `56e8efd3d10e56cf2f676adb3bc31a747316d7557c99a781bf63ecd8d54b7b9a` | 491 520 (5.5) + 245 760 (6.5) = 737 280 |
| `DnTable.Rds` | `965496bed913989bc4f473d538bbcb736a2fa266fa42606ff18fab489ccb2d02` | `65f7fd737546d2dd56502aec1b87bd69a046ec63832e352082f9e3653a310a08` | `68ef561846ea73c4665f20b702c0c6d996f54c2b13cdb00ed2dd57abd936db91` | `5ee864387c77b973c3d8227b53841147beb2b97dc085a022b8ef033056e4c18c` | 460 800 (5.5) + 230 400 (6.5) = 691 200 |
| `DnPlotTable.Rds` | `4c8a6d43d13003b598e916fa12b7ab80abc10f62a4b767096f1d029d419a2eb2` | `1ff0a942172904e17250a16a608166f2c78969e0eaa447de6842f8f317e58c7f` | `242957280305088709c66e75ad8b51c056f6096604c63ff550732c135067e40a` | `40337a6e3449efca08fd3ab4d3ef943b9b9e932edd90de81244b43af767b7596` | 38 590 (5.5) + 25 826 (6.5) = 64 416 |
| `kmaxTable.Rds` | `138d031b9ab093e736f9a6480485c24ea5349c47dcdd092293e3316abc52f2f7` | `5eddd88a8e489dc4d463e70d3880f3ec9bfbcda0b4c6d6e6054d84caf5841e09` | `c15f44b54b4a91e3d6820787f79790d5b4542ecfed1b12aab75459ab1d311bab` | `56e8efd3d10e56cf2f676adb3bc31a747316d7557c99a781bf63ecd8d54b7b9a` | 491 520 (5.5) + 245 760 (6.5) = 737 280 |

`DnPlotTable.Rds` no conserva el número de filas de la generación anterior porque la librería omite las filas con Dn ≤ 1e-4 cm; los bloques por TR se tomaron completos de cada corrida.

## Logs de las corridas

### Mw 6.5: dry-run (`newmark-M65-dryrun.log`)

```
>> Dn models: subduction = FALSE -> BM17 off, BM19 on
dry run: /Users/averrik/Cloud/github/projects/AR-M2V4D/newmark-M65.json
steps: dn, kmax
sites: CFD
dn: writes /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M65/M2V4D/CFD/DnDraws.Rds
dn: writes /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M65/M2V4D/CFD/PGATable.csv
dn: writes /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M65/M2V4D/CFD/DnTable.Rds
dn: writes /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M65/DnPlotTable.Rds
dn: writes /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M65/DnTable.Rds
kmax: writes /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M65/M2V4D/CFD/kmaxTable.Rds
kmax: writes /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M65/kmaxTable.Rds
dry-run exit=0
```

### Mw 6.5: corrida (`newmark-M65-run.log`)

```
command: newmark process newmark-M65.json --root . --steps dn,kmax --seed 20260915
start: 2026-10-14 17:29:51 -0300
>> Dn models: subduction = FALSE -> BM17 off, BM19 on
dn: wrote site CFD
kmax: wrote site CFD
Warning messages:
1: siteID=CFD: 94168/737280 kmax rows use roots beyond sampled support (max beyond=0.3333; max kmax=0.9093 g at siteID=CFD ID=MCE IDg=S32 IDm=U4 IDn=SR08 p=0.95 Da=1.35) 
2: global: 94168/737280 kmax rows use roots beyond sampled support (max beyond=0.3333; max kmax=0.9093 g at siteID=CFD ID=MCE IDg=S32 IDm=U4 IDn=SR08 p=0.95 Da=1.35) 
end: 2026-10-14 17:35:35 -0300
exit=0
```

### Mw 6.5: verificación contra la generación Mw 7 (`verifyRun-M65.log`)

```
verifyRun.R ORIG=data/newmark (generación Mw 7, antes de combinar) RUN=data/newmark-M65
== ShearTable ==
sha orig: 334359667159dd8f928c54d4f40484af1162372a0e4114aee666691104b3cf29 
sha M65 : 334359667159dd8f928c54d4f40484af1162372a0e4114aee666691104b3cf29 

== PGATable.csv ==
sha orig: 325fb141ea5126a46bd0baf82b89a76d03a4cc86adc36f3b74ac770f9b6c8cbf 
sha M65 : 325fb141ea5126a46bd0baf82b89a76d03a4cc86adc36f3b74ac770f9b6c8cbf 
identical content: TRUE 

== DnTable.Rds ==
dim orig: 691200x12  dim M65: 691200x12 
same names: TRUE  same classes: TRUE  same key: TRUE 
same attribute names: TRUE 
rows matched by key: 691200 of 691200 
       ID TRlabel     n nDiff    maxRel
   <char>  <char> <int> <int>     <num>
1:  M2V4D     100 76800 33889 0.2602922
2:  M2V4D    1000 76800 35569 0.2602922
3:  M2V4D   10000 76800 36036 0.2602922
4:  M2V4D     200 76800 34121 0.2602922
5:  M2V4D    2000 76800 35937 0.2602922
6:  M2V4D    2500 76800 35960 0.2602922
7:  M2V4D     500 76800 34899 0.2602922
8:  M2V4D    5000 76800 36098 0.2602922
9:    MCE     MCE 76800 34459 0.2602922

== kmaxTable.Rds ==
dim orig: 737280x18  dim M65: 737280x18 
same names: TRUE  same classes: TRUE  same key: TRUE 
same attribute names: TRUE 
rows matched by key: 737280 of 737280 
       ID TRlabel     n nDiff maxRel
   <char>  <char> <int> <int>  <num>
1:  M2V4D     100 81920  6745      1
2:  M2V4D    1000 81920 22782      1
3:  M2V4D   10000 81920 33282      1
4:  M2V4D     200 81920 10294      1
5:  M2V4D    2000 81920 26461      1
6:  M2V4D    2500 81920 27613      1
7:  M2V4D     500 81920 17521      1
8:  M2V4D    5000 81920 30863      1
9:    MCE     MCE 81920 20510      1

== DnPlotTable.Rds ==
dim orig: 64943x8  dim M65: 64752x8 
same names: TRUE  same classes: TRUE  same key: TRUE 
same attribute names: TRUE 
rows matched by key: 59234 of 64943 
       ID TRlabel     n nDiff    maxRel
   <char>  <char> <int> <int>     <num>
1:  M2V4D     100  2351  1607 0.3387000
2:  M2V4D    1000  6733  3740 0.2602922
3:  M2V4D   10000  8862  4554 0.4260396
4:  M2V4D     200  3596  2127 0.2602922
5:  M2V4D    2000  7661  4154 0.2602922
6:  M2V4D    2500  8021  4375 0.6157879
7:  M2V4D     500  5680  3315 0.2602922
8:  M2V4D    5000  8438  4431 0.2602922
9:    MCE     MCE  7892  3568 0.2602922

== ky grids per cell identical between runs? ==
cells: 360  identical ky grids: 360 
one common grid across all cells (orig): TRUE 

== DnDraws: sampled PGA.s identical between runs (same random stream)? ==
dim orig: 16200000x11  dim M65: 16200000x11  same key: TRUE 
       ID TRlabel     n samePGAs sameDnAM88
   <char>  <char> <int>    <int>      <int>
1:  M2V4D     100 12000    12000      12000
2:  M2V4D    1000 12000    12000      12000
3:  M2V4D   10000 12000    12000      12000
4:  M2V4D     200 12000    12000      12000
5:  M2V4D    2000 12000    12000      12000
6:  M2V4D    2500 12000    12000      12000
7:  M2V4D     500 12000    12000      12000
8:  M2V4D    5000 12000    12000      12000
9:    MCE     MCE 12000    12000      12000
       ID TRlabel     n sameDnBM19    maxRel
   <char>  <char> <int>      <int>     <num>
1:  M2V4D     100 12000          0 0.2602922
2:  M2V4D    1000 12000          0 0.2602922
3:  M2V4D   10000 12000          0 0.2602922
4:  M2V4D     200 12000          0 0.2602922
5:  M2V4D    2000 12000          0 0.2602922
6:  M2V4D    2500 12000          0 0.2602922
7:  M2V4D     500 12000          0 0.2602922
8:  M2V4D    5000 12000          0 0.2602922
9:    MCE     MCE 12000          0 0.2602922
```

### Mw 5.5: dry-run (`newmark-M55-dryrun.log`)

```
>> Dn models: subduction = FALSE -> BM17 off, BM19 on
dry run: /Users/averrik/Cloud/github/projects/AR-M2V4D/newmark-M55.json
steps: dn, kmax
sites: CFD
dn: writes /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M55/M2V4D/CFD/DnDraws.Rds
dn: writes /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M55/M2V4D/CFD/PGATable.csv
dn: writes /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M55/M2V4D/CFD/DnTable.Rds
dn: writes /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M55/DnPlotTable.Rds
dn: writes /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M55/DnTable.Rds
kmax: writes /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M55/M2V4D/CFD/kmaxTable.Rds
kmax: writes /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M55/kmaxTable.Rds
dry-run exit=0
```

### Mw 5.5: corrida (`newmark-M55-run.log`)

```
command: newmark process newmark-M55.json --root . --steps dn,kmax --seed 20260915
start: 2026-10-14 17:48:19 -0300
>> Dn models: subduction = FALSE -> BM17 off, BM19 on
dn: wrote site CFD
kmax: wrote site CFD
Warning messages:
1: siteID=CFD: 93608/737280 kmax rows use roots beyond sampled support (max beyond=0.3333; max kmax=0.9093 g at siteID=CFD ID=MCE IDg=S32 IDm=U4 IDn=SR08 p=0.95 Da=1.35) 
2: global: 93608/737280 kmax rows use roots beyond sampled support (max beyond=0.3333; max kmax=0.9093 g at siteID=CFD ID=MCE IDg=S32 IDm=U4 IDn=SR08 p=0.95 Da=1.35) 
end: 2026-10-14 17:53:56 -0300
exit=0
```

### Mw 5.5: verificación contra la generación Mw 7 (`verifyRun-M55.log`)

```
verifyRun.R ORIG=<copia Mw 7 de data/newmark antes de combinar, scratchpad> RUN=data/newmark-M55 (las etiquetas 'M65' del script designan la corrida verificada, aquí Mw 5.5)
== ShearTable ==
sha orig: 334359667159dd8f928c54d4f40484af1162372a0e4114aee666691104b3cf29 
sha M65 : 334359667159dd8f928c54d4f40484af1162372a0e4114aee666691104b3cf29 

== PGATable.csv ==
sha orig: 325fb141ea5126a46bd0baf82b89a76d03a4cc86adc36f3b74ac770f9b6c8cbf 
sha M65 : 325fb141ea5126a46bd0baf82b89a76d03a4cc86adc36f3b74ac770f9b6c8cbf 
identical content: TRUE 

== DnTable.Rds ==
dim orig: 691200x12  dim M65: 691200x12 
same names: TRUE  same classes: TRUE  same key: TRUE 
same attribute names: TRUE 
rows matched by key: 691200 of 691200 
       ID TRlabel     n nDiff    maxRel
   <char>  <char> <int> <int>     <num>
1:  M2V4D     100 76800 33958 0.5952558
2:  M2V4D    1000 76800 35779 0.5952558
3:  M2V4D   10000 76800 36208 0.5952558
4:  M2V4D     200 76800 34191 0.5952558
5:  M2V4D    2000 76800 36084 0.5952558
6:  M2V4D    2500 76800 36140 0.5952558
7:  M2V4D     500 76800 35139 0.5952558
8:  M2V4D    5000 76800 36244 0.5952558
9:    MCE     MCE 76800 34531 0.5952558

== kmaxTable.Rds ==
dim orig: 737280x18  dim M65: 737280x18 
same names: TRUE  same classes: TRUE  same key: TRUE 
same attribute names: TRUE 
rows matched by key: 737280 of 737280 
       ID TRlabel     n nDiff maxRel
   <char>  <char> <int> <int>  <num>
1:  M2V4D     100 81920  6801      1
2:  M2V4D    1000 81920 22830      1
3:  M2V4D   10000 81920 33458      1
4:  M2V4D     200 81920 10294      1
5:  M2V4D    2000 81920 26519      1
6:  M2V4D    2500 81920 27748      1
7:  M2V4D     500 81920 17526      1
8:  M2V4D    5000 81920 30999      1
9:    MCE     MCE 81920 20634      1

== DnPlotTable.Rds ==
dim orig: 64943x8  dim M65: 64361x8 
same names: TRUE  same classes: TRUE  same key: TRUE 
same attribute names: TRUE 
rows matched by key: 55034 of 64943 
       ID TRlabel     n nDiff    maxRel
   <char>  <char> <int> <int>     <num>
1:  M2V4D     100  1753  1011 0.5952558
2:  M2V4D    1000  6178  3196 0.5952558
3:  M2V4D   10000  8766  4464 0.5952558
4:  M2V4D     200  2929  1467 0.5952558
5:  M2V4D    2000  7397  3895 0.5952558
6:  M2V4D    2500  7694  4052 0.5952558
7:  M2V4D     500  4907  2556 0.5952558
8:  M2V4D    5000  8228  4224 0.5952558
9:    MCE     MCE  7182  2860 0.5952558

== ky grids per cell identical between runs? ==
cells: 360  identical ky grids: 360 
one common grid across all cells (orig): TRUE 

== DnDraws: sampled PGA.s identical between runs (same random stream)? ==
dim orig: 16200000x11  dim M65: 16200000x11  same key: TRUE 
       ID TRlabel     n samePGAs sameDnAM88
   <char>  <char> <int>    <int>      <int>
1:  M2V4D     100 12000    12000      12000
2:  M2V4D    1000 12000    12000      12000
3:  M2V4D   10000 12000    12000      12000
4:  M2V4D     200 12000    12000      12000
5:  M2V4D    2000 12000    12000      12000
6:  M2V4D    2500 12000    12000      12000
7:  M2V4D     500 12000    12000      12000
8:  M2V4D    5000 12000    12000      12000
9:    MCE     MCE 12000    12000      12000
       ID TRlabel     n sameDnBM19    maxRel
   <char>  <char> <int>      <int>     <num>
1:  M2V4D     100 12000          0 0.5952558
2:  M2V4D    1000 12000          0 0.5952558
3:  M2V4D   10000 12000          0 0.5952558
4:  M2V4D     200 12000          0 0.5952558
5:  M2V4D    2000 12000          0 0.5952558
6:  M2V4D    2500 12000          0 0.5952558
7:  M2V4D     500 12000          0 0.5952558
8:  M2V4D    5000 12000          0 0.5952558
9:    MCE     MCE 12000          0 0.5952558
```

Lectura de las verificaciones: `nDiff` cuenta las filas cuyo valor cambia respecto de Mw 7. En `DnTable` cambian las filas de BT07, BM19, `flexible` y `ensemble`; las de AM88, JB07, SR08 y `rigid` son idénticas porque esos modelos no usan Mw. Las grillas `ky` son idénticas en las 360 celdas y comunes a todas (PGA media < 0.8 g). En `DnDraws`, `PGA.s` y los `Dn` de AM88 son idénticos en todas las celdas: la corriente aleatoria por celda no depende de Mw. `maxRel` = 1 en `kmaxTable` corresponde a filas con kmax que cae a 0 o a valores del orden de 1e-4 g en demandas bajas y `Da` grandes (`inspectKmaxZeros.log`, calculado para Mw 6.5).

### Combinación (`combine2.log`)

```
M2V4D/CFD/DnDraws.Rds        newmark-M55=10800000 newmark-M65=5400000  total  16200000  sha 2893284007e6 -> 672b43170c22
M2V4D/CFD/DnTable.Rds        newmark-M55=460800 newmark-M65=230400  total    691200  sha 8bace6278d2c -> 5ee864387c77
M2V4D/CFD/kmaxTable.Rds      newmark-M55=491520 newmark-M65=245760  total    737280  sha 53262120f8f5 -> 56e8efd3d10e
DnTable.Rds                  newmark-M55=460800 newmark-M65=230400  total    691200  sha 8bace6278d2c -> 5ee864387c77
DnPlotTable.Rds              newmark-M55=38590 newmark-M65=25826  total     64416  sha f2d7686850e7 -> 40337a6e3449
kmaxTable.Rds                newmark-M55=491520 newmark-M65=245760  total    737280  sha 53262120f8f5 -> 56e8efd3d10e
PGATable.csv: 325fb141ea5126a46bd0baf82b89a76d03a4cc86adc36f3b74ac770f9b6c8cbf 
ShearTable.Rds: 334359667159dd8f928c54d4f40484af1162372a0e4114aee666691104b3cf29
```

### Verificación independiente del publicado (`postCheck2.log`)

```
M2V4D/CFD/DnDraws.Rds        rows  16200000  schema/key/attrs TRUE  key order TRUE  all rows mapped TRUE
   blocks: newmark-M55[100,200,500,1000,2000,2500]=TRUE  newmark-M65[5000,10000,MCE]=TRUE
   rows by ID,TR: M2V4D/100=1800000 M2V4D/200=1800000 M2V4D/500=1800000 M2V4D/1000=1800000 M2V4D/2000=1800000 M2V4D/2500=1800000 M2V4D/5000=1800000 M2V4D/10000=1800000 MCE/NA=1800000
M2V4D/CFD/DnTable.Rds        rows    691200  schema/key/attrs TRUE  key order TRUE  all rows mapped TRUE
   blocks: newmark-M55[100,200,500,1000,2000,2500]=TRUE  newmark-M65[5000,10000,MCE]=TRUE
   rows by ID,TR: M2V4D/100=76800 M2V4D/200=76800 M2V4D/500=76800 M2V4D/1000=76800 M2V4D/2000=76800 M2V4D/2500=76800 M2V4D/5000=76800 M2V4D/10000=76800 MCE/NA=76800
M2V4D/CFD/kmaxTable.Rds      rows    737280  schema/key/attrs TRUE  key order TRUE  all rows mapped TRUE
   blocks: newmark-M55[100,200,500,1000,2000,2500]=TRUE  newmark-M65[5000,10000,MCE]=TRUE
   rows by ID,TR: M2V4D/100=81920 M2V4D/200=81920 M2V4D/500=81920 M2V4D/1000=81920 M2V4D/2000=81920 M2V4D/2500=81920 M2V4D/5000=81920 M2V4D/10000=81920 MCE/NA=81920
DnTable.Rds                  rows    691200  schema/key/attrs TRUE  key order TRUE  all rows mapped TRUE
   blocks: newmark-M55[100,200,500,1000,2000,2500]=TRUE  newmark-M65[5000,10000,MCE]=TRUE
   rows by ID,TR: M2V4D/100=76800 M2V4D/200=76800 M2V4D/500=76800 M2V4D/1000=76800 M2V4D/2000=76800 M2V4D/2500=76800 M2V4D/5000=76800 M2V4D/10000=76800 MCE/NA=76800
DnPlotTable.Rds              rows     64416  schema/key/attrs TRUE  key order TRUE  all rows mapped TRUE
   blocks: newmark-M55[100,200,500,1000,2000,2500]=TRUE  newmark-M65[5000,10000,MCE]=TRUE
   rows by ID,TR: M2V4D/100=3851 M2V4D/200=5015 M2V4D/500=6402 M2V4D/1000=7277 M2V4D/2000=7937 M2V4D/2500=8108 M2V4D/5000=8537 M2V4D/10000=8862 MCE/NA=8427
kmaxTable.Rds                rows    737280  schema/key/attrs TRUE  key order TRUE  all rows mapped TRUE
   blocks: newmark-M55[100,200,500,1000,2000,2500]=TRUE  newmark-M65[5000,10000,MCE]=TRUE
   rows by ID,TR: M2V4D/100=81920 M2V4D/200=81920 M2V4D/500=81920 M2V4D/1000=81920 M2V4D/2000=81920 M2V4D/2500=81920 M2V4D/5000=81920 M2V4D/10000=81920 MCE/NA=81920

PGATable.csv == backup: TRUE 
ShearTable.Rds == backup: TRUE 

ALL CHECKS PASSED: TRUE
```

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

## Tablas comparativas: generación Mw 7 frente a los productos publicados

Celdas `Mw 7 / Mw nuevo (diferencia relativa %)`, con la diferencia relativa definida como 100·(nuevo − Mw 7)/Mw 7. kmax y Dn son los del modelo `ensemble` con `p = mean`, el estadístico que publican las tablas del informe. Para kmax, cada geometría se muestra en sus propios objetivos relativos `Da = signif(DaH·Hs, 6)` con `DaH` del contrato; para Dn se muestran siete de los 30 `ky` de la grilla común. Resúmenes para las nueve demandas; tablas por celda para TR 10000 y MCE, como pedía el brief; todas las celdas en `kmax-compare.csv` y `dn-compare.csv` (`scripts/compareTables2.R`).


### Resumen por demanda: diferencia relativa (%) de kmax (ensemble, media) por geometría, [mín, mediana, máx] sobre materiales y Da/H

| Demanda | Mw | S135 | S27 | S32 | S35 | S50 |
|---|---|---|---|---|---|---|
| TR 100 | 5.5 | [-31.1, 0.0, 0.0] | [-52.2, -30.8, 0.0] | [-51.6, -23.1, 0.0] | [-51.6, -18.6, 0.0] | [-51.1, -11.5, 0.0] |
| TR 200 | 5.5 | [-26.5, 0.0, 0.0] | [-40.8, -32.8, 0.0] | [-37.7, -30.1, 0.0] | [-39.3, -29.7, 0.0] | [-49.0, -21.7, 0.0] |
| TR 500 | 5.5 | [-18.1, -5.3, 0.0] | [-24.9, -20.2, -3.5] | [-23.9, -19.8, -2.1] | [-24.0, -20.1, -2.5] | [-21.0, -16.5, 0.0] |
| TR 1000 | 5.5 | [-13.5, -6.4, 0.0] | [-18.4, -15.9, -7.1] | [-18.7, -15.0, -5.0] | [-18.1, -15.1, -3.6] | [-16.2, -13.3, -0.4] |
| TR 2000 | 5.5 | [-11.0, -7.2, 0.0] | [-15.5, -13.5, -8.2] | [-14.8, -12.7, -6.0] | [-14.9, -12.8, -5.1] | [-13.4, -11.3, -2.0] |
| TR 2500 | 5.5 | [-10.1, -7.1, 0.0] | [-14.6, -12.9, -8.8] | [-14.1, -12.1, -6.8] | [-13.9, -12.2, -5.8] | [-12.9, -10.8, -2.5] |
| TR 5000 | 6.5 | [-3.7, -2.9, -0.5] | [-5.1, -4.2, -3.9] | [-4.8, -4.0, -3.2] | [-4.8, -4.0, -2.6] | [-4.5, -3.6, -1.9] |
| TR 10000 | 6.5 | [-3.5, -2.9, -0.8] | [-4.8, -3.9, -3.5] | [-4.3, -3.7, -3.1] | [-4.3, -3.7, -2.9] | [-3.8, -3.3, -2.8] |
| MCE | 6.5 | [-1.0, -0.6, 0.0] | [-2.8, -1.8, -0.8] | [-2.4, -1.4, -0.3] | [-2.5, -1.5, -0.5] | [-1.8, -1.0, -0.1] |

Celdas kmax con 0 en ambas generaciones (contadas como 0 %): 1 ; celdas con 0 sólo en una (sin diferencia definida): 0 

### Resumen por demanda: diferencia relativa (%) de Dn (ensemble, media) por geometría, [mín, mediana, máx] sobre materiales y los 30 ky

| Demanda | Mw | S135 | S27 | S32 | S35 | S50 |
|---|---|---|---|---|---|---|
| TR 100 | 5.5 | [-59.4, -57.7, -24.6] | [-58.1, -52.4, -34.4] | [-58.5, -53.3, -33.9] | [-58.5, -53.2, -33.7] | [-58.7, -54.6, -33.3] |
| TR 200 | 5.5 | [-59.1, -56.2, -14.3] | [-57.4, -50.5, -23.1] | [-58.0, -51.5, -21.5] | [-57.7, -51.4, -22.7] | [-58.3, -53.2, -20.9] |
| TR 500 | 5.5 | [-58.3, -44.1, -5.5] | [-55.2, -45.7, -7.9] | [-56.4, -46.6, -8.1] | [-56.5, -45.7, -6.1] | [-57.2, -45.7, -7.0] |
| TR 1000 | 5.5 | [-55.6, -16.1, -0.9] | [-53.7, -29.1, -1.8] | [-55.0, -27.4, -1.5] | [-55.3, -27.3, -1.5] | [-55.3, -20.6, -0.1] |
| TR 2000 | 5.5 | [-50.6, -7.3, -0.2] | [-51.3, -16.5, -0.3] | [-52.6, -14.7, -0.2] | [-52.2, -15.0, -0.2] | [-52.2, -11.2, -0.2] |
| TR 2500 | 5.5 | [-49.3, -6.4, -0.1] | [-51.0, -14.1, -0.1] | [-51.4, -12.8, -0.2] | [-51.6, -11.6, -0.1] | [-51.7, -9.5, -0.1] |
| TR 5000 | 6.5 | [-18.3, -1.7, -0.0] | [-20.1, -3.2, -0.0] | [-20.1, -2.9, -0.0] | [-20.3, -2.6, -0.0] | [-19.5, -2.0, -0.0] |
| TR 10000 | 6.5 | [-15.4, -1.0, -0.0] | [-16.7, -1.5, -0.0] | [-15.6, -1.3, -0.0] | [-16.4, -1.4, -0.0] | [-17.9, -1.1, -0.0] |
| MCE | 6.5 | [-0.3, -0.0, -0.0] | [-2.2, -0.1, -0.0] | [-1.0, -0.1, -0.0] | [-2.1, -0.1, -0.0] | [-0.5, -0.0, -0.0] |

### kmax (ensemble, p = mean) [g], TR 10000: Mw 7 / Mw 6.5 (diferencia relativa)

| siteID | IDg | Hs | IDm | Da/H 0.05% | Da/H 0.1% | Da/H 0.25% | Da/H 0.4% | Da/H 0.5% | Da/H 1% | Da/H 2.5% |
|---|---|---|---|---|---|---|---|---|---|---|
| CFD | S135 | 135 | U1 | 0.100 / 0.097 (-2.6%) | 0.076 / 0.074 (-2.7%) | 0.049 / 0.048 (-3.1%) | 0.037 / 0.036 (-2.8%) | 0.032 / 0.031 (-2.9%) | 0.020 / 0.019 (-3.4%) | 0.010 / 0.010 (-2.0%) |
| CFD | S135 | 135 | U2 | 0.104 / 0.101 (-2.8%) | 0.079 / 0.077 (-2.9%) | 0.051 / 0.050 (-3.0%) | 0.039 / 0.038 (-3.4%) | 0.034 / 0.033 (-3.1%) | 0.021 / 0.020 (-3.1%) | 0.011 / 0.011 (-2.0%) |
| CFD | S135 | 135 | U3 | 0.109 / 0.106 (-2.7%) | 0.084 / 0.081 (-2.8%) | 0.055 / 0.053 (-2.9%) | 0.043 / 0.041 (-3.0%) | 0.037 / 0.036 (-3.0%) | 0.023 / 0.022 (-3.4%) | 0.012 / 0.011 (-2.2%) |
| CFD | S135 | 135 | U4 | 0.114 / 0.111 (-2.7%) | 0.087 / 0.085 (-2.8%) | 0.057 / 0.055 (-3.0%) | 0.043 / 0.042 (-3.0%) | 0.038 / 0.036 (-3.3%) | 0.023 / 0.023 (-2.3%) | 0.012 / 0.012 (-0.8%) |
| CFD | S135 | 135 | U5 | 0.114 / 0.111 (-2.8%) | 0.087 / 0.085 (-2.9%) | 0.057 / 0.055 (-3.1%) | 0.044 / 0.042 (-3.5%) | 0.038 / 0.037 (-3.3%) | 0.024 / 0.023 (-3.3%) | 0.012 / 0.012 (-1.6%) |
| CFD | S135 | 135 | U6 | 0.107 / 0.104 (-2.8%) | 0.081 / 0.079 (-2.9%) | 0.052 / 0.051 (-3.2%) | 0.040 / 0.039 (-3.1%) | 0.035 / 0.034 (-3.1%) | 0.021 / 0.020 (-3.1%) | 0.011 / 0.011 (-1.5%) |
| CFD | S135 | 135 | U7 | 0.100 / 0.098 (-2.6%) | 0.076 / 0.074 (-2.5%) | 0.050 / 0.048 (-2.7%) | 0.038 / 0.037 (-2.7%) | 0.033 / 0.032 (-2.7%) | 0.020 / 0.020 (-2.9%) | 0.010 / 0.010 (-1.8%) |
| CFD | S135 | 135 | U8 | 0.103 / 0.100 (-2.6%) | 0.079 / 0.077 (-2.6%) | 0.052 / 0.050 (-3.0%) | 0.040 / 0.038 (-2.9%) | 0.035 / 0.034 (-2.8%) | 0.021 / 0.021 (-2.7%) | 0.011 / 0.011 (-1.7%) |
| CFD | S27 | 27 | U1 | 0.195 / 0.187 (-3.7%) | 0.156 / 0.150 (-3.6%) | 0.111 / 0.107 (-3.6%) | 0.092 / 0.088 (-3.7%) | 0.083 / 0.080 (-3.6%) | 0.059 / 0.057 (-3.9%) | 0.033 / 0.032 (-3.9%) |
| CFD | S27 | 27 | U2 | 0.206 / 0.198 (-3.9%) | 0.164 / 0.158 (-3.8%) | 0.117 / 0.113 (-3.7%) | 0.097 / 0.093 (-3.8%) | 0.087 / 0.084 (-3.8%) | 0.062 / 0.060 (-4.1%) | 0.035 / 0.033 (-4.2%) |
| CFD | S27 | 27 | U3 | 0.206 / 0.198 (-3.8%) | 0.165 / 0.159 (-3.7%) | 0.119 / 0.114 (-3.7%) | 0.098 / 0.094 (-3.7%) | 0.089 / 0.085 (-3.7%) | 0.064 / 0.061 (-4.0%) | 0.036 / 0.035 (-4.0%) |
| CFD | S27 | 27 | U4 | 0.240 / 0.230 (-4.2%) | 0.191 / 0.183 (-4.1%) | 0.136 / 0.131 (-4.1%) | 0.112 / 0.108 (-4.1%) | 0.102 / 0.097 (-4.1%) | 0.072 / 0.069 (-4.3%) | 0.041 / 0.039 (-4.8%) |
| CFD | S27 | 27 | U5 | 0.225 / 0.216 (-4.0%) | 0.180 / 0.172 (-3.9%) | 0.129 / 0.124 (-3.9%) | 0.106 / 0.102 (-3.9%) | 0.096 / 0.092 (-3.9%) | 0.069 / 0.066 (-4.1%) | 0.039 / 0.038 (-4.2%) |
| CFD | S27 | 27 | U6 | 0.214 / 0.205 (-4.0%) | 0.171 / 0.164 (-3.9%) | 0.122 / 0.117 (-3.8%) | 0.100 / 0.096 (-3.9%) | 0.091 / 0.087 (-4.0%) | 0.064 / 0.062 (-4.2%) | 0.036 / 0.035 (-4.4%) |
| CFD | S27 | 27 | U7 | 0.196 / 0.188 (-3.7%) | 0.157 / 0.151 (-3.6%) | 0.113 / 0.109 (-3.5%) | 0.093 / 0.090 (-3.6%) | 0.084 / 0.081 (-3.6%) | 0.060 / 0.058 (-3.9%) | 0.034 / 0.033 (-3.8%) |
| CFD | S27 | 27 | U8 | 0.192 / 0.185 (-3.7%) | 0.154 / 0.148 (-3.6%) | 0.110 / 0.106 (-3.6%) | 0.091 / 0.088 (-3.6%) | 0.082 / 0.079 (-3.6%) | 0.058 / 0.056 (-3.9%) | 0.033 / 0.032 (-3.6%) |
| CFD | S32 | 32 | U1 | 0.176 / 0.170 (-3.4%) | 0.141 / 0.136 (-3.3%) | 0.101 / 0.097 (-3.3%) | 0.083 / 0.080 (-3.4%) | 0.075 / 0.072 (-3.3%) | 0.053 / 0.051 (-3.6%) | 0.029 / 0.028 (-3.3%) |
| CFD | S32 | 32 | U2 | 0.190 / 0.182 (-3.8%) | 0.151 / 0.145 (-3.7%) | 0.107 / 0.103 (-3.6%) | 0.088 / 0.085 (-3.7%) | 0.079 / 0.076 (-3.7%) | 0.056 / 0.053 (-4.0%) | 0.031 / 0.029 (-4.2%) |
| CFD | S32 | 32 | U3 | 0.185 / 0.178 (-3.6%) | 0.148 / 0.143 (-3.5%) | 0.106 / 0.102 (-3.5%) | 0.087 / 0.084 (-3.5%) | 0.079 / 0.076 (-3.5%) | 0.056 / 0.054 (-3.8%) | 0.031 / 0.030 (-3.8%) |
| CFD | S32 | 32 | U4 | 0.218 / 0.209 (-4.0%) | 0.173 / 0.166 (-3.9%) | 0.123 / 0.118 (-3.9%) | 0.101 / 0.097 (-3.9%) | 0.091 / 0.088 (-4.0%) | 0.064 / 0.062 (-4.2%) | 0.036 / 0.034 (-4.1%) |
| CFD | S32 | 32 | U5 | 0.201 / 0.193 (-3.9%) | 0.160 / 0.154 (-3.8%) | 0.114 / 0.109 (-3.8%) | 0.093 / 0.089 (-3.8%) | 0.084 / 0.081 (-3.8%) | 0.059 / 0.057 (-4.1%) | 0.033 / 0.031 (-4.0%) |
| CFD | S32 | 32 | U6 | 0.192 / 0.184 (-3.9%) | 0.152 / 0.146 (-3.8%) | 0.107 / 0.103 (-3.8%) | 0.087 / 0.084 (-3.8%) | 0.079 / 0.076 (-3.9%) | 0.055 / 0.052 (-4.2%) | 0.030 / 0.028 (-4.3%) |
| CFD | S32 | 32 | U7 | 0.175 / 0.169 (-3.4%) | 0.140 / 0.135 (-3.2%) | 0.100 / 0.097 (-3.2%) | 0.083 / 0.080 (-3.3%) | 0.075 / 0.072 (-3.3%) | 0.053 / 0.051 (-3.5%) | 0.029 / 0.028 (-3.2%) |
| CFD | S32 | 32 | U8 | 0.177 / 0.171 (-3.4%) | 0.142 / 0.137 (-3.3%) | 0.102 / 0.098 (-3.3%) | 0.084 / 0.081 (-3.3%) | 0.076 / 0.073 (-3.3%) | 0.053 / 0.051 (-3.5%) | 0.030 / 0.029 (-3.1%) |
| CFD | S35 | 35 | U1 | 0.175 / 0.168 (-3.5%) | 0.139 / 0.135 (-3.4%) | 0.099 / 0.096 (-3.4%) | 0.081 / 0.079 (-3.4%) | 0.074 / 0.071 (-3.4%) | 0.051 / 0.050 (-3.7%) | 0.028 / 0.027 (-3.4%) |
| CFD | S35 | 35 | U2 | 0.182 / 0.176 (-3.8%) | 0.145 / 0.139 (-3.7%) | 0.102 / 0.098 (-3.7%) | 0.083 / 0.080 (-3.7%) | 0.075 / 0.072 (-3.8%) | 0.052 / 0.050 (-4.0%) | 0.028 / 0.027 (-4.1%) |
| CFD | S35 | 35 | U3 | 0.178 / 0.172 (-3.6%) | 0.142 / 0.137 (-3.5%) | 0.100 / 0.097 (-3.5%) | 0.082 / 0.079 (-3.6%) | 0.074 / 0.071 (-3.6%) | 0.052 / 0.050 (-3.8%) | 0.028 / 0.027 (-3.5%) |
| CFD | S35 | 35 | U4 | 0.212 / 0.204 (-4.0%) | 0.168 / 0.161 (-3.9%) | 0.119 / 0.114 (-3.9%) | 0.097 / 0.093 (-4.0%) | 0.087 / 0.084 (-4.0%) | 0.061 / 0.058 (-4.3%) | 0.033 / 0.032 (-3.9%) |
| CFD | S35 | 35 | U5 | 0.197 / 0.190 (-3.9%) | 0.157 / 0.151 (-3.8%) | 0.111 / 0.106 (-3.8%) | 0.090 / 0.087 (-3.9%) | 0.081 / 0.078 (-3.9%) | 0.057 / 0.054 (-4.2%) | 0.031 / 0.030 (-4.0%) |
| CFD | S35 | 35 | U6 | 0.197 / 0.189 (-3.8%) | 0.157 / 0.151 (-3.7%) | 0.111 / 0.107 (-3.7%) | 0.091 / 0.087 (-3.8%) | 0.082 / 0.079 (-3.8%) | 0.057 / 0.055 (-4.2%) | 0.031 / 0.030 (-3.9%) |
| CFD | S35 | 35 | U7 | 0.170 / 0.165 (-3.4%) | 0.136 / 0.132 (-3.3%) | 0.097 / 0.094 (-3.2%) | 0.080 / 0.077 (-3.4%) | 0.072 / 0.069 (-3.4%) | 0.050 / 0.048 (-3.7%) | 0.027 / 0.027 (-2.9%) |
| CFD | S35 | 35 | U8 | 0.174 / 0.168 (-3.4%) | 0.139 / 0.134 (-3.3%) | 0.099 / 0.095 (-3.3%) | 0.081 / 0.078 (-3.3%) | 0.073 / 0.071 (-3.4%) | 0.051 / 0.049 (-3.7%) | 0.028 / 0.027 (-3.5%) |
| CFD | S50 | 50 | U1 | 0.154 / 0.149 (-3.1%) | 0.123 / 0.119 (-3.1%) | 0.086 / 0.084 (-3.0%) | 0.070 / 0.068 (-3.1%) | 0.063 / 0.061 (-3.3%) | 0.043 / 0.042 (-3.2%) | 0.023 / 0.022 (-2.9%) |
| CFD | S50 | 50 | U2 | 0.154 / 0.149 (-3.3%) | 0.121 / 0.117 (-3.2%) | 0.084 / 0.082 (-3.3%) | 0.068 / 0.066 (-3.4%) | 0.061 / 0.059 (-3.5%) | 0.041 / 0.039 (-3.7%) | 0.021 / 0.020 (-3.0%) |
| CFD | S50 | 50 | U3 | 0.151 / 0.146 (-3.2%) | 0.120 / 0.116 (-3.1%) | 0.083 / 0.081 (-3.2%) | 0.067 / 0.065 (-3.4%) | 0.060 / 0.058 (-3.5%) | 0.041 / 0.039 (-3.5%) | 0.021 / 0.021 (-3.1%) |
| CFD | S50 | 50 | U4 | 0.179 / 0.172 (-3.6%) | 0.141 / 0.136 (-3.6%) | 0.098 / 0.095 (-3.6%) | 0.079 / 0.076 (-3.7%) | 0.071 / 0.068 (-3.8%) | 0.048 / 0.046 (-3.8%) | 0.025 / 0.024 (-3.5%) |
| CFD | S50 | 50 | U5 | 0.168 / 0.162 (-3.5%) | 0.132 / 0.128 (-3.4%) | 0.092 / 0.089 (-3.4%) | 0.075 / 0.072 (-3.6%) | 0.067 / 0.064 (-3.6%) | 0.045 / 0.044 (-3.7%) | 0.024 / 0.023 (-3.3%) |
| CFD | S50 | 50 | U6 | 0.159 / 0.153 (-3.4%) | 0.125 / 0.121 (-3.3%) | 0.087 / 0.084 (-3.4%) | 0.070 / 0.068 (-3.4%) | 0.063 / 0.060 (-3.5%) | 0.042 / 0.041 (-3.7%) | 0.022 / 0.021 (-3.1%) |
| CFD | S50 | 50 | U7 | 0.145 / 0.140 (-3.1%) | 0.114 / 0.111 (-3.0%) | 0.080 / 0.077 (-3.1%) | 0.064 / 0.062 (-3.1%) | 0.058 / 0.056 (-3.3%) | 0.039 / 0.037 (-3.3%) | 0.020 / 0.019 (-3.2%) |
| CFD | S50 | 50 | U8 | 0.146 / 0.142 (-3.1%) | 0.115 / 0.112 (-3.1%) | 0.080 / 0.078 (-3.1%) | 0.065 / 0.063 (-3.2%) | 0.058 / 0.056 (-3.4%) | 0.039 / 0.038 (-3.5%) | 0.020 / 0.019 (-2.8%) |

### kmax (ensemble, p = mean) [g], MCE: Mw 7 / Mw 6.5 (diferencia relativa)

| siteID | IDg | Hs | IDm | Da/H 0.05% | Da/H 0.1% | Da/H 0.25% | Da/H 0.4% | Da/H 0.5% | Da/H 1% | Da/H 2.5% |
|---|---|---|---|---|---|---|---|---|---|---|
| CFD | S135 | 135 | U1 | 0.098 / 0.097 (-0.9%) | 0.077 / 0.076 (-0.8%) | 0.052 / 0.052 (-0.6%) | 0.041 / 0.041 (-0.5%) | 0.037 / 0.037 (-0.5%) | 0.025 / 0.024 (-0.5%) | 0.014 / 0.014 (-0.2%) |
| CFD | S135 | 135 | U2 | 0.101 / 0.100 (-0.9%) | 0.079 / 0.078 (-0.8%) | 0.054 / 0.053 (-0.8%) | 0.043 / 0.042 (-0.7%) | 0.038 / 0.038 (-0.5%) | 0.025 / 0.025 (-0.4%) | 0.014 / 0.014 (-0.1%) |
| CFD | S135 | 135 | U3 | 0.100 / 0.099 (-1.0%) | 0.078 / 0.078 (-0.9%) | 0.053 / 0.053 (-0.7%) | 0.042 / 0.042 (-0.7%) | 0.038 / 0.037 (-0.5%) | 0.025 / 0.025 (-0.4%) | 0.014 / 0.014 (-0.3%) |
| CFD | S135 | 135 | U4 | 0.107 / 0.106 (-0.9%) | 0.083 / 0.083 (-0.8%) | 0.057 / 0.056 (-0.6%) | 0.045 / 0.045 (-0.5%) | 0.040 / 0.040 (-0.3%) | 0.027 / 0.027 (-0.2%) | 0.014 / 0.014 (+0.0%) |
| CFD | S135 | 135 | U5 | 0.105 / 0.104 (-1.0%) | 0.082 / 0.081 (-0.9%) | 0.056 / 0.055 (-0.8%) | 0.044 / 0.044 (-0.7%) | 0.039 / 0.039 (-0.5%) | 0.026 / 0.026 (-0.4%) | 0.014 / 0.014 (-0.1%) |
| CFD | S135 | 135 | U6 | 0.098 / 0.097 (-1.0%) | 0.076 / 0.076 (-0.8%) | 0.051 / 0.051 (-0.6%) | 0.040 / 0.040 (-0.4%) | 0.036 / 0.036 (-0.4%) | 0.024 / 0.024 (-0.3%) | 0.013 / 0.013 (-0.1%) |
| CFD | S135 | 135 | U7 | 0.098 / 0.097 (-0.8%) | 0.077 / 0.076 (-0.7%) | 0.052 / 0.052 (-0.6%) | 0.041 / 0.041 (-0.6%) | 0.037 / 0.036 (-0.6%) | 0.024 / 0.024 (-0.4%) | 0.013 / 0.013 (-0.2%) |
| CFD | S135 | 135 | U8 | 0.095 / 0.095 (-0.9%) | 0.074 / 0.074 (-0.8%) | 0.050 / 0.050 (-0.6%) | 0.040 / 0.040 (-0.8%) | 0.035 / 0.035 (-0.6%) | 0.023 / 0.023 (-0.6%) | 0.012 / 0.012 (-0.2%) |
| CFD | S27 | 27 | U1 | 0.166 / 0.162 (-1.9%) | 0.137 / 0.134 (-1.8%) | 0.102 / 0.100 (-1.7%) | 0.085 / 0.084 (-1.6%) | 0.078 / 0.077 (-1.6%) | 0.057 / 0.057 (-1.2%) | 0.036 / 0.035 (-0.9%) |
| CFD | S27 | 27 | U2 | 0.174 / 0.171 (-2.1%) | 0.144 / 0.141 (-2.0%) | 0.106 / 0.104 (-1.9%) | 0.089 / 0.087 (-1.9%) | 0.081 / 0.080 (-1.9%) | 0.059 / 0.058 (-1.7%) | 0.036 / 0.036 (-0.9%) |
| CFD | S27 | 27 | U3 | 0.170 / 0.167 (-2.0%) | 0.140 / 0.138 (-1.9%) | 0.104 / 0.102 (-1.8%) | 0.087 / 0.085 (-1.8%) | 0.079 / 0.078 (-1.7%) | 0.058 / 0.057 (-1.6%) | 0.036 / 0.035 (-1.2%) |
| CFD | S27 | 27 | U4 | 0.210 / 0.204 (-2.8%) | 0.172 / 0.167 (-2.6%) | 0.126 / 0.123 (-2.6%) | 0.106 / 0.103 (-2.4%) | 0.097 / 0.094 (-2.4%) | 0.071 / 0.069 (-2.4%) | 0.044 / 0.043 (-1.8%) |
| CFD | S27 | 27 | U5 | 0.191 / 0.186 (-2.4%) | 0.156 / 0.153 (-2.3%) | 0.115 / 0.113 (-2.2%) | 0.096 / 0.094 (-2.2%) | 0.088 / 0.086 (-2.1%) | 0.064 / 0.063 (-1.9%) | 0.039 / 0.039 (-1.7%) |
| CFD | S27 | 27 | U6 | 0.182 / 0.178 (-2.3%) | 0.149 / 0.146 (-2.2%) | 0.110 / 0.108 (-2.1%) | 0.092 / 0.090 (-2.1%) | 0.084 / 0.083 (-2.1%) | 0.062 / 0.060 (-1.8%) | 0.038 / 0.037 (-1.3%) |
| CFD | S27 | 27 | U7 | 0.166 / 0.163 (-1.9%) | 0.138 / 0.135 (-1.7%) | 0.103 / 0.101 (-1.6%) | 0.086 / 0.085 (-1.6%) | 0.079 / 0.078 (-1.6%) | 0.058 / 0.058 (-1.3%) | 0.036 / 0.036 (-0.8%) |
| CFD | S27 | 27 | U8 | 0.158 / 0.155 (-1.8%) | 0.130 / 0.128 (-1.7%) | 0.096 / 0.095 (-1.6%) | 0.081 / 0.079 (-1.6%) | 0.074 / 0.072 (-1.5%) | 0.054 / 0.053 (-1.2%) | 0.033 / 0.033 (-0.9%) |
| CFD | S32 | 32 | U1 | 0.153 / 0.151 (-1.5%) | 0.127 / 0.125 (-1.5%) | 0.094 / 0.093 (-1.4%) | 0.079 / 0.078 (-1.2%) | 0.073 / 0.072 (-1.1%) | 0.054 / 0.053 (-0.8%) | 0.033 / 0.033 (-0.5%) |
| CFD | S32 | 32 | U2 | 0.165 / 0.162 (-1.9%) | 0.136 / 0.133 (-1.7%) | 0.101 / 0.099 (-1.6%) | 0.084 / 0.083 (-1.6%) | 0.077 / 0.076 (-1.6%) | 0.056 / 0.056 (-1.3%) | 0.035 / 0.034 (-0.8%) |
| CFD | S32 | 32 | U3 | 0.157 / 0.154 (-1.6%) | 0.130 / 0.128 (-1.6%) | 0.096 / 0.095 (-1.5%) | 0.080 / 0.079 (-1.3%) | 0.073 / 0.072 (-1.3%) | 0.054 / 0.053 (-1.0%) | 0.033 / 0.033 (-0.6%) |
| CFD | S32 | 32 | U4 | 0.196 / 0.191 (-2.4%) | 0.160 / 0.157 (-2.3%) | 0.118 / 0.115 (-2.3%) | 0.099 / 0.096 (-2.1%) | 0.090 / 0.088 (-2.1%) | 0.066 / 0.064 (-2.0%) | 0.040 / 0.040 (-1.4%) |
| CFD | S32 | 32 | U5 | 0.183 / 0.179 (-2.1%) | 0.150 / 0.147 (-2.0%) | 0.111 / 0.109 (-1.8%) | 0.094 / 0.092 (-1.8%) | 0.085 / 0.084 (-1.8%) | 0.063 / 0.062 (-1.6%) | 0.039 / 0.038 (-1.2%) |
| CFD | S32 | 32 | U6 | 0.170 / 0.167 (-2.0%) | 0.140 / 0.137 (-2.0%) | 0.103 / 0.101 (-1.8%) | 0.086 / 0.084 (-1.8%) | 0.078 / 0.077 (-1.7%) | 0.057 / 0.056 (-1.4%) | 0.035 / 0.035 (-1.2%) |
| CFD | S32 | 32 | U7 | 0.151 / 0.148 (-1.4%) | 0.125 / 0.123 (-1.3%) | 0.093 / 0.092 (-1.2%) | 0.078 / 0.077 (-1.1%) | 0.071 / 0.071 (-1.0%) | 0.053 / 0.052 (-0.8%) | 0.032 / 0.032 (-0.3%) |
| CFD | S32 | 32 | U8 | 0.152 / 0.150 (-1.5%) | 0.126 / 0.124 (-1.4%) | 0.094 / 0.092 (-1.2%) | 0.078 / 0.077 (-1.2%) | 0.072 / 0.071 (-1.1%) | 0.053 / 0.052 (-0.9%) | 0.033 / 0.032 (-0.4%) |
| CFD | S35 | 35 | U1 | 0.151 / 0.149 (-1.5%) | 0.125 / 0.123 (-1.5%) | 0.093 / 0.091 (-1.3%) | 0.077 / 0.077 (-1.1%) | 0.071 / 0.070 (-1.1%) | 0.052 / 0.051 (-0.9%) | 0.032 / 0.032 (-0.5%) |
| CFD | S35 | 35 | U2 | 0.156 / 0.153 (-1.9%) | 0.127 / 0.125 (-1.8%) | 0.093 / 0.092 (-1.7%) | 0.077 / 0.076 (-1.6%) | 0.070 / 0.069 (-1.5%) | 0.051 / 0.050 (-1.2%) | 0.030 / 0.030 (-0.5%) |
| CFD | S35 | 35 | U3 | 0.156 / 0.153 (-1.7%) | 0.129 / 0.126 (-1.6%) | 0.095 / 0.093 (-1.5%) | 0.079 / 0.078 (-1.4%) | 0.072 / 0.071 (-1.3%) | 0.053 / 0.052 (-1.1%) | 0.032 / 0.032 (-0.7%) |
| CFD | S35 | 35 | U4 | 0.193 / 0.188 (-2.5%) | 0.157 / 0.153 (-2.4%) | 0.115 / 0.112 (-2.2%) | 0.096 / 0.093 (-2.2%) | 0.087 / 0.085 (-2.2%) | 0.063 / 0.062 (-2.1%) | 0.038 / 0.038 (-1.6%) |
| CFD | S35 | 35 | U5 | 0.174 / 0.170 (-2.1%) | 0.143 / 0.140 (-2.0%) | 0.105 / 0.103 (-1.9%) | 0.087 / 0.086 (-1.8%) | 0.080 / 0.078 (-1.8%) | 0.058 / 0.057 (-1.7%) | 0.035 / 0.035 (-0.9%) |
| CFD | S35 | 35 | U6 | 0.165 / 0.162 (-2.0%) | 0.135 / 0.133 (-1.9%) | 0.099 / 0.097 (-1.9%) | 0.082 / 0.081 (-1.8%) | 0.075 / 0.073 (-1.7%) | 0.054 / 0.053 (-1.4%) | 0.032 / 0.032 (-0.9%) |
| CFD | S35 | 35 | U7 | 0.149 / 0.147 (-1.4%) | 0.123 / 0.122 (-1.4%) | 0.091 / 0.090 (-1.2%) | 0.077 / 0.076 (-1.2%) | 0.070 / 0.069 (-1.0%) | 0.051 / 0.051 (-0.9%) | 0.032 / 0.032 (-0.5%) |
| CFD | S35 | 35 | U8 | 0.147 / 0.145 (-1.5%) | 0.121 / 0.119 (-1.5%) | 0.089 / 0.088 (-1.3%) | 0.075 / 0.074 (-1.2%) | 0.068 / 0.067 (-1.1%) | 0.050 / 0.049 (-0.8%) | 0.030 / 0.030 (-0.5%) |
| CFD | S50 | 50 | U1 | 0.131 / 0.129 (-1.2%) | 0.107 / 0.105 (-1.1%) | 0.077 / 0.077 (-1.0%) | 0.064 / 0.063 (-0.8%) | 0.058 / 0.058 (-0.8%) | 0.042 / 0.041 (-0.4%) | 0.025 / 0.024 (-0.2%) |
| CFD | S50 | 50 | U2 | 0.133 / 0.131 (-1.2%) | 0.108 / 0.106 (-1.1%) | 0.078 / 0.077 (-0.9%) | 0.064 / 0.063 (-1.0%) | 0.058 / 0.057 (-0.9%) | 0.041 / 0.041 (-0.4%) | 0.024 / 0.024 (-0.1%) |
| CFD | S50 | 50 | U3 | 0.136 / 0.134 (-1.2%) | 0.111 / 0.109 (-1.1%) | 0.081 / 0.080 (-1.0%) | 0.067 / 0.066 (-0.8%) | 0.061 / 0.060 (-0.8%) | 0.044 / 0.043 (-0.5%) | 0.026 / 0.026 (-0.4%) |
| CFD | S50 | 50 | U4 | 0.161 / 0.158 (-1.8%) | 0.131 / 0.129 (-1.6%) | 0.095 / 0.093 (-1.5%) | 0.078 / 0.077 (-1.5%) | 0.071 / 0.070 (-1.3%) | 0.051 / 0.051 (-1.2%) | 0.031 / 0.030 (-0.5%) |
| CFD | S50 | 50 | U5 | 0.138 / 0.136 (-1.5%) | 0.112 / 0.110 (-1.4%) | 0.080 / 0.079 (-1.3%) | 0.066 / 0.065 (-1.2%) | 0.060 / 0.059 (-1.1%) | 0.042 / 0.042 (-0.7%) | 0.025 / 0.024 (-0.3%) |
| CFD | S50 | 50 | U6 | 0.139 / 0.137 (-1.3%) | 0.113 / 0.112 (-1.3%) | 0.082 / 0.081 (-1.1%) | 0.068 / 0.067 (-1.0%) | 0.061 / 0.061 (-0.9%) | 0.044 / 0.044 (-0.6%) | 0.026 / 0.026 (-0.3%) |
| CFD | S50 | 50 | U7 | 0.131 / 0.129 (-1.2%) | 0.107 / 0.106 (-1.0%) | 0.078 / 0.077 (-0.9%) | 0.064 / 0.064 (-0.9%) | 0.058 / 0.058 (-0.8%) | 0.042 / 0.041 (-0.5%) | 0.024 / 0.024 (-0.2%) |
| CFD | S50 | 50 | U8 | 0.133 / 0.131 (-1.2%) | 0.108 / 0.107 (-1.1%) | 0.079 / 0.078 (-1.0%) | 0.065 / 0.065 (-0.9%) | 0.059 / 0.059 (-0.8%) | 0.042 / 0.042 (-0.5%) | 0.025 / 0.025 (-0.2%) |

### Dn (ensemble, p = mean) [cm], TR 10000: Mw 7 / Mw 6.5 (diferencia relativa), ky seleccionados de la grilla común

| siteID | IDg | IDm | ky 0.010 g | ky 0.021 g | ky 0.045 g | ky 0.096 g | ky 0.205 g | ky 0.437 g | ky 0.800 g |
|---|---|---|---|---|---|---|---|---|---|
| CFD | S135 | U1 | 98031.86 / 98023.35 (-0.0%) | 5482.86 / 5478.80 (-0.1%) | 331.85 / 330.36 (-0.5%) | 27.66 / 27.24 (-1.5%) | 3.15 / 3.06 (-2.9%) | 0.26 / 0.24 (-6.0%) | 0.02 / 0.02 (-13.1%) |
| CFD | S135 | U2 | 204746.17 / 204736.94 (-0.0%) | 11383.45 / 11379.04 (-0.0%) | 660.13 / 658.54 (-0.2%) | 46.84 / 46.41 (-0.9%) | 4.56 / 4.47 (-2.0%) | 0.38 / 0.37 (-3.8%) | 0.03 / 0.03 (-8.6%) |
| CFD | S135 | U3 | 122152.39 / 122141.39 (-0.0%) | 6829.92 / 6824.67 (-0.1%) | 412.42 / 410.52 (-0.5%) | 34.18 / 33.66 (-1.5%) | 3.84 / 3.73 (-2.8%) | 0.28 / 0.26 (-6.4%) | 0.02 / 0.02 (-15.4%) |
| CFD | S135 | U4 | 273611.06 / 273603.27 (-0.0%) | 15194.91 / 15191.07 (-0.0%) | 875.02 / 873.61 (-0.2%) | 60.83 / 60.44 (-0.6%) | 5.84 / 5.76 (-1.4%) | 0.46 / 0.45 (-2.7%) | 0.03 / 0.03 (-7.8%) |
| CFD | S135 | U5 | 170132.14 / 170122.13 (-0.0%) | 9482.06 / 9476.98 (-0.1%) | 560.52 / 558.57 (-0.3%) | 43.27 / 42.70 (-1.3%) | 4.69 / 4.56 (-2.7%) | 0.39 / 0.36 (-5.5%) | 0.03 / 0.03 (-13.6%) |
| CFD | S135 | U6 | 144580.33 / 144571.55 (-0.0%) | 8061.00 / 8056.66 (-0.1%) | 477.64 / 476.02 (-0.3%) | 37.08 / 36.62 (-1.2%) | 4.02 / 3.92 (-2.4%) | 0.33 / 0.32 (-4.7%) | 0.03 / 0.03 (-9.6%) |
| CFD | S135 | U7 | 116762.25 / 116753.34 (-0.0%) | 6520.35 / 6516.29 (-0.1%) | 390.19 / 388.80 (-0.4%) | 31.44 / 31.08 (-1.1%) | 3.53 / 3.46 (-2.0%) | 0.27 / 0.26 (-3.9%) | 0.02 / 0.02 (-11.0%) |
| CFD | S135 | U8 | 185347.67 / 185338.23 (-0.0%) | 10313.67 / 10309.25 (-0.0%) | 601.48 / 599.89 (-0.3%) | 43.44 / 43.00 (-1.0%) | 4.23 / 4.13 (-2.2%) | 0.35 / 0.33 (-4.3%) | 0.03 / 0.03 (-8.5%) |
| CFD | S27 | U1 | 81574.22 / 81567.35 (-0.0%) | 4576.37 / 4572.39 (-0.1%) | 284.21 / 282.51 (-0.6%) | 25.92 / 25.39 (-2.1%) | 3.17 / 3.04 (-3.9%) | 0.25 / 0.23 (-8.6%) | 0.03 / 0.02 (-16.2%) |
| CFD | S27 | U2 | 63301.98 / 63294.56 (-0.0%) | 3570.99 / 3566.56 (-0.1%) | 230.73 / 228.77 (-0.8%) | 23.67 / 23.04 (-2.7%) | 3.20 / 3.05 (-4.7%) | 0.28 / 0.25 (-9.7%) | 0.03 / 0.03 (-16.6%) |
| CFD | S27 | U3 | 428490.27 / 428482.63 (-0.0%) | 23752.06 / 23747.47 (-0.0%) | 1348.73 / 1346.68 (-0.2%) | 87.27 / 86.59 (-0.8%) | 7.42 / 7.26 (-2.2%) | 0.61 / 0.58 (-4.9%) | 0.06 / 0.05 (-10.3%) |
| CFD | S27 | U4 | 207969.40 / 207960.84 (-0.0%) | 11578.70 / 11573.14 (-0.0%) | 681.90 / 679.24 (-0.4%) | 52.46 / 51.53 (-1.8%) | 5.80 / 5.56 (-4.1%) | 0.54 / 0.49 (-8.6%) | 0.06 / 0.05 (-15.4%) |
| CFD | S27 | U5 | 212029.02 / 212020.69 (-0.0%) | 11798.85 / 11793.62 (-0.0%) | 691.38 / 688.96 (-0.4%) | 51.80 / 50.98 (-1.6%) | 5.52 / 5.31 (-3.8%) | 0.51 / 0.47 (-7.6%) | 0.06 / 0.05 (-13.4%) |
| CFD | S27 | U6 | 96737.67 / 96730.05 (-0.0%) | 5421.88 / 5417.19 (-0.1%) | 335.15 / 333.03 (-0.6%) | 30.38 / 29.67 (-2.3%) | 3.80 / 3.63 (-4.5%) | 0.33 / 0.30 (-9.3%) | 0.04 / 0.03 (-16.7%) |
| CFD | S27 | U7 | 143120.01 / 143113.01 (-0.0%) | 7978.83 / 7974.80 (-0.1%) | 473.41 / 471.69 (-0.4%) | 37.12 / 36.58 (-1.5%) | 4.08 / 3.95 (-3.1%) | 0.34 / 0.32 (-6.5%) | 0.03 / 0.03 (-14.8%) |
| CFD | S27 | U8 | 92526.82 / 92520.11 (-0.0%) | 5180.21 / 5176.37 (-0.1%) | 316.97 / 315.34 (-0.5%) | 27.73 / 27.21 (-1.9%) | 3.39 / 3.27 (-3.5%) | 0.30 / 0.27 (-7.1%) | 0.03 / 0.02 (-15.5%) |
| CFD | S32 | U1 | 140953.04 / 140946.54 (-0.0%) | 7856.68 / 7853.15 (-0.0%) | 464.88 / 463.45 (-0.3%) | 35.78 / 35.35 (-1.2%) | 3.77 / 3.67 (-2.6%) | 0.31 / 0.29 (-5.4%) | 0.02 / 0.02 (-13.9%) |
| CFD | S32 | U2 | 98578.79 / 98571.27 (-0.0%) | 5519.77 / 5515.37 (-0.1%) | 338.26 / 336.36 (-0.6%) | 29.68 / 29.07 (-2.1%) | 3.60 / 3.45 (-4.0%) | 0.31 / 0.28 (-8.4%) | 0.04 / 0.03 (-15.3%) |
| CFD | S32 | U3 | 242383.33 / 242375.95 (-0.0%) | 13465.89 / 13461.69 (-0.0%) | 777.96 / 776.18 (-0.2%) | 54.74 / 54.18 (-1.0%) | 5.43 / 5.30 (-2.4%) | 0.48 / 0.46 (-4.8%) | 0.04 / 0.04 (-10.6%) |
| CFD | S32 | U4 | 213852.37 / 213843.76 (-0.0%) | 11903.60 / 11898.12 (-0.0%) | 699.65 / 697.07 (-0.4%) | 53.56 / 52.67 (-1.7%) | 5.98 / 5.75 (-3.8%) | 0.56 / 0.51 (-7.7%) | 0.06 / 0.05 (-15.6%) |
| CFD | S32 | U5 | 205736.19 / 205728.43 (-0.0%) | 11445.04 / 11440.39 (-0.0%) | 668.25 / 666.20 (-0.3%) | 49.05 / 48.39 (-1.3%) | 5.04 / 4.88 (-3.1%) | 0.45 / 0.43 (-6.2%) | 0.05 / 0.05 (-11.2%) |
| CFD | S32 | U6 | 109838.94 / 109831.80 (-0.0%) | 6139.13 / 6134.82 (-0.1%) | 371.71 / 369.79 (-0.5%) | 31.54 / 30.91 (-2.0%) | 3.80 / 3.65 (-4.0%) | 0.34 / 0.31 (-8.1%) | 0.04 / 0.03 (-15.1%) |
| CFD | S32 | U7 | 144512.42 / 144506.17 (-0.0%) | 8051.72 / 8048.32 (-0.0%) | 475.23 / 473.84 (-0.3%) | 36.38 / 35.96 (-1.2%) | 3.91 / 3.82 (-2.5%) | 0.35 / 0.33 (-4.8%) | 0.03 / 0.03 (-10.2%) |
| CFD | S32 | U8 | 124093.21 / 124086.40 (-0.0%) | 6926.91 / 6923.09 (-0.1%) | 414.75 / 413.15 (-0.4%) | 33.70 / 33.20 (-1.5%) | 3.88 / 3.77 (-3.0%) | 0.34 / 0.32 (-6.2%) | 0.03 / 0.03 (-12.7%) |
| CFD | S35 | U1 | 104303.84 / 104297.02 (-0.0%) | 5833.92 / 5830.15 (-0.1%) | 354.27 / 352.71 (-0.4%) | 30.10 / 29.63 (-1.6%) | 3.51 / 3.40 (-3.1%) | 0.28 / 0.26 (-6.9%) | 0.02 / 0.02 (-15.8%) |
| CFD | S35 | U2 | 165928.06 / 165920.81 (-0.0%) | 9239.15 / 9234.92 (-0.0%) | 542.92 / 541.09 (-0.3%) | 40.73 / 40.14 (-1.5%) | 4.24 / 4.10 (-3.4%) | 0.38 / 0.36 (-6.8%) | 0.04 / 0.03 (-14.1%) |
| CFD | S35 | U3 | 152514.09 / 152507.08 (-0.0%) | 8497.58 / 8493.60 (-0.0%) | 501.86 / 500.18 (-0.3%) | 38.60 / 38.08 (-1.4%) | 4.12 / 4.00 (-3.0%) | 0.34 / 0.31 (-6.4%) | 0.04 / 0.03 (-11.5%) |
| CFD | S35 | U4 | 158790.60 / 158782.24 (-0.0%) | 8858.82 / 8853.51 (-0.1%) | 530.01 / 527.53 (-0.5%) | 43.51 / 42.66 (-2.0%) | 5.21 / 5.00 (-4.1%) | 0.49 / 0.45 (-8.3%) | 0.06 / 0.05 (-15.0%) |
| CFD | S35 | U5 | 133696.55 / 133688.42 (-0.0%) | 7468.03 / 7463.10 (-0.1%) | 450.08 / 447.88 (-0.5%) | 37.50 / 36.78 (-1.9%) | 4.37 / 4.19 (-4.0%) | 0.36 / 0.33 (-8.9%) | 0.04 / 0.03 (-16.4%) |
| CFD | S35 | U6 | 148024.05 / 148016.06 (-0.0%) | 8258.55 / 8253.78 (-0.1%) | 493.12 / 491.02 (-0.4%) | 39.74 / 39.06 (-1.7%) | 4.60 / 4.43 (-3.6%) | 0.43 / 0.40 (-6.9%) | 0.04 / 0.04 (-13.8%) |
| CFD | S35 | U7 | 125482.23 / 125475.63 (-0.0%) | 7002.24 / 6998.62 (-0.1%) | 417.79 / 416.31 (-0.4%) | 33.16 / 32.71 (-1.4%) | 3.60 / 3.50 (-2.9%) | 0.29 / 0.27 (-6.1%) | 0.03 / 0.02 (-12.6%) |
| CFD | S35 | U8 | 86818.67 / 86811.89 (-0.0%) | 4867.56 / 4863.85 (-0.1%) | 300.60 / 299.09 (-0.5%) | 27.00 / 26.54 (-1.7%) | 3.27 / 3.16 (-3.2%) | 0.25 / 0.23 (-7.2%) | 0.02 / 0.02 (-15.5%) |
| CFD | S50 | U1 | 219334.75 / 219327.19 (-0.0%) | 12193.67 / 12189.75 (-0.0%) | 707.57 / 706.05 (-0.2%) | 50.56 / 50.12 (-0.9%) | 4.95 / 4.85 (-2.0%) | 0.39 / 0.38 (-4.1%) | 0.03 / 0.03 (-10.2%) |
| CFD | S50 | U2 | 87538.32 / 87530.98 (-0.0%) | 4906.46 / 4902.47 (-0.1%) | 302.33 / 300.72 (-0.5%) | 26.88 / 26.39 (-1.8%) | 3.20 / 3.10 (-3.4%) | 0.24 / 0.23 (-7.5%) | 0.02 / 0.02 (-16.1%) |
| CFD | S50 | U3 | 372385.32 / 372378.29 (-0.0%) | 20643.24 / 20639.52 (-0.0%) | 1171.56 / 1170.08 (-0.1%) | 75.10 / 74.66 (-0.6%) | 6.16 / 6.06 (-1.6%) | 0.50 / 0.49 (-3.4%) | 0.06 / 0.05 (-6.1%) |
| CFD | S50 | U4 | 273079.23 / 273070.87 (-0.0%) | 15172.37 / 15167.38 (-0.0%) | 877.99 / 875.77 (-0.3%) | 62.60 / 61.87 (-1.2%) | 6.38 / 6.20 (-2.8%) | 0.59 / 0.56 (-5.7%) | 0.05 / 0.05 (-13.4%) |
| CFD | S50 | U5 | 337511.47 / 337503.43 (-0.0%) | 18725.99 / 18721.48 (-0.0%) | 1070.30 / 1068.42 (-0.2%) | 71.23 / 70.65 (-0.8%) | 6.32 / 6.19 (-2.1%) | 0.54 / 0.52 (-4.3%) | 0.06 / 0.06 (-7.7%) |
| CFD | S50 | U6 | 125116.54 / 125108.84 (-0.0%) | 6986.76 / 6982.48 (-0.1%) | 419.27 / 417.49 (-0.4%) | 34.10 / 33.54 (-1.6%) | 3.80 / 3.67 (-3.4%) | 0.31 / 0.29 (-7.3%) | 0.03 / 0.02 (-16.0%) |
| CFD | S50 | U7 | 83450.77 / 83444.16 (-0.0%) | 4674.79 / 4671.43 (-0.1%) | 286.39 / 285.11 (-0.4%) | 24.76 / 24.40 (-1.5%) | 2.86 / 2.78 (-2.7%) | 0.23 / 0.21 (-5.5%) | 0.02 / 0.02 (-12.0%) |
| CFD | S50 | U8 | 54595.26 / 54588.33 (-0.0%) | 3082.08 / 3078.52 (-0.1%) | 199.06 / 197.70 (-0.7%) | 20.04 / 19.65 (-1.9%) | 2.48 / 2.40 (-3.3%) | 0.16 / 0.15 (-8.5%) | 0.01 / 0.01 (-17.9%) |

### Dn (ensemble, p = mean) [cm], MCE: Mw 7 / Mw 6.5 (diferencia relativa), ky seleccionados de la grilla común

| siteID | IDg | IDm | ky 0.010 g | ky 0.021 g | ky 0.045 g | ky 0.096 g | ky 0.205 g | ky 0.437 g | ky 0.800 g |
|---|---|---|---|---|---|---|---|---|---|
| CFD | S135 | U1 | 905023.05 / 905020.99 (-0.0%) | 50070.21 / 50069.43 (-0.0%) | 2800.50 / 2800.27 (-0.0%) | 169.39 / 169.33 (-0.0%) | 13.60 / 13.59 (-0.1%) | 1.28 / 1.28 (-0.1%) | 0.12 / 0.12 (-0.2%) |
| CFD | S135 | U2 | 724024.24 / 724022.21 (-0.0%) | 40069.99 / 40069.22 (-0.0%) | 2247.93 / 2247.70 (-0.0%) | 138.92 / 138.87 (-0.0%) | 11.94 / 11.93 (-0.1%) | 1.17 / 1.17 (-0.1%) | 0.10 / 0.10 (-0.2%) |
| CFD | S135 | U3 | 667038.74 / 667036.48 (-0.0%) | 36921.13 / 36920.25 (-0.0%) | 2073.78 / 2073.51 (-0.0%) | 129.24 / 129.18 (-0.0%) | 11.37 / 11.36 (-0.1%) | 1.13 / 1.13 (-0.1%) | 0.10 / 0.10 (-0.3%) |
| CFD | S135 | U4 | 845848.60 / 845847.08 (-0.0%) | 46802.71 / 46802.12 (-0.0%) | 2621.57 / 2621.40 (-0.0%) | 160.46 / 160.42 (-0.0%) | 13.45 / 13.44 (-0.0%) | 1.34 / 1.34 (-0.1%) | 0.13 / 0.13 (-0.1%) |
| CFD | S135 | U5 | 987049.66 / 987047.58 (-0.0%) | 54603.38 / 54602.56 (-0.0%) | 3052.08 / 3051.83 (-0.0%) | 184.32 / 184.26 (-0.0%) | 15.13 / 15.12 (-0.1%) | 1.57 / 1.57 (-0.1%) | 0.18 / 0.18 (-0.1%) |
| CFD | S135 | U6 | 634743.03 / 634741.28 (-0.0%) | 35131.39 / 35130.71 (-0.0%) | 1972.45 / 1972.25 (-0.0%) | 122.56 / 122.51 (-0.0%) | 10.73 / 10.72 (-0.1%) | 1.11 / 1.11 (-0.1%) | 0.12 / 0.12 (-0.1%) |
| CFD | S135 | U7 | 917220.23 / 917218.31 (-0.0%) | 50741.17 / 50740.45 (-0.0%) | 2836.36 / 2836.15 (-0.0%) | 171.02 / 170.97 (-0.0%) | 13.70 / 13.69 (-0.1%) | 1.33 / 1.32 (-0.1%) | 0.13 / 0.13 (-0.1%) |
| CFD | S135 | U8 | 411340.86 / 411338.64 (-0.0%) | 22788.21 / 22787.34 (-0.0%) | 1289.66 / 1289.40 (-0.0%) | 84.22 / 84.16 (-0.1%) | 8.22 / 8.21 (-0.1%) | 0.83 / 0.83 (-0.2%) | 0.07 / 0.07 (-0.3%) |
| CFD | S27 | U1 | 771893.27 / 771890.84 (-0.0%) | 42711.26 / 42710.07 (-0.0%) | 2391.95 / 2391.51 (-0.0%) | 145.62 / 145.50 (-0.1%) | 11.80 / 11.78 (-0.2%) | 1.12 / 1.11 (-0.4%) | 0.11 / 0.11 (-0.7%) |
| CFD | S27 | U2 | 311862.80 / 311859.87 (-0.0%) | 17295.74 / 17294.25 (-0.0%) | 987.80 / 987.23 (-0.1%) | 67.86 / 67.70 (-0.2%) | 7.24 / 7.20 (-0.5%) | 0.74 / 0.73 (-0.8%) | 0.05 / 0.05 (-2.2%) |
| CFD | S27 | U3 | 229911.34 / 229908.54 (-0.0%) | 12768.48 / 12767.10 (-0.0%) | 737.29 / 736.78 (-0.1%) | 53.13 / 52.99 (-0.3%) | 5.87 / 5.84 (-0.5%) | 0.57 / 0.57 (-0.8%) | 0.04 / 0.04 (-2.1%) |
| CFD | S27 | U4 | 2355805.37 / 2355800.76 (-0.0%) | 130238.88 / 130236.08 (-0.0%) | 7238.72 / 7237.43 (-0.0%) | 419.56 / 419.11 (-0.1%) | 29.79 / 29.67 (-0.4%) | 2.80 / 2.78 (-0.8%) | 0.34 / 0.34 (-1.5%) |
| CFD | S27 | U5 | 747443.01 / 747439.49 (-0.0%) | 41367.10 / 41365.14 (-0.0%) | 2321.58 / 2320.75 (-0.0%) | 143.76 / 143.50 (-0.2%) | 12.51 / 12.45 (-0.5%) | 1.33 / 1.32 (-0.9%) | 0.15 / 0.14 (-1.6%) |
| CFD | S27 | U6 | 536372.40 / 536369.12 (-0.0%) | 29705.03 / 29703.30 (-0.0%) | 1676.31 / 1675.61 (-0.0%) | 107.29 / 107.08 (-0.2%) | 9.98 / 9.94 (-0.5%) | 1.02 / 1.01 (-0.8%) | 0.09 / 0.09 (-1.8%) |
| CFD | S27 | U7 | 523643.97 / 523641.45 (-0.0%) | 28998.37 / 28997.16 (-0.0%) | 1635.39 / 1634.95 (-0.0%) | 104.08 / 103.96 (-0.1%) | 9.37 / 9.35 (-0.3%) | 0.89 / 0.88 (-0.4%) | 0.07 / 0.07 (-1.0%) |
| CFD | S27 | U8 | 578799.28 / 578797.25 (-0.0%) | 32036.31 / 32035.33 (-0.0%) | 1798.97 / 1798.62 (-0.0%) | 111.70 / 111.61 (-0.1%) | 9.71 / 9.69 (-0.2%) | 0.98 / 0.98 (-0.3%) | 0.09 / 0.09 (-0.7%) |
| CFD | S32 | U1 | 1416132.59 / 1416130.52 (-0.0%) | 78307.29 / 78306.35 (-0.0%) | 4360.25 / 4359.93 (-0.0%) | 255.62 / 255.54 (-0.0%) | 18.57 / 18.55 (-0.1%) | 1.67 / 1.67 (-0.2%) | 0.18 / 0.18 (-0.3%) |
| CFD | S32 | U2 | 589524.44 / 589521.77 (-0.0%) | 32642.09 / 32640.80 (-0.0%) | 1838.89 / 1838.41 (-0.0%) | 116.52 / 116.38 (-0.1%) | 10.50 / 10.48 (-0.3%) | 1.03 / 1.02 (-0.4%) | 0.10 / 0.10 (-0.9%) |
| CFD | S32 | U3 | 701130.87 / 701128.82 (-0.0%) | 38801.48 / 38800.54 (-0.0%) | 2176.05 / 2175.72 (-0.0%) | 134.01 / 133.93 (-0.1%) | 11.40 / 11.39 (-0.2%) | 1.15 / 1.15 (-0.2%) | 0.12 / 0.12 (-0.4%) |
| CFD | S32 | U4 | 3192958.00 / 3192953.70 (-0.0%) | 176491.00 / 176488.54 (-0.0%) | 9794.16 / 9793.10 (-0.0%) | 560.64 / 560.30 (-0.1%) | 37.49 / 37.41 (-0.2%) | 3.21 / 3.19 (-0.5%) | 0.39 / 0.39 (-0.8%) |
| CFD | S32 | U5 | 1331798.86 / 1331795.32 (-0.0%) | 73663.14 / 73661.27 (-0.0%) | 4111.61 / 4110.86 (-0.0%) | 245.25 / 245.03 (-0.1%) | 18.85 / 18.80 (-0.3%) | 1.75 / 1.74 (-0.5%) | 0.19 / 0.19 (-0.9%) |
| CFD | S32 | U6 | 725565.13 / 725562.12 (-0.0%) | 40158.76 / 40157.22 (-0.0%) | 2254.84 / 2254.25 (-0.0%) | 140.20 / 140.03 (-0.1%) | 12.35 / 12.31 (-0.3%) | 1.27 / 1.26 (-0.5%) | 0.11 / 0.11 (-1.0%) |
| CFD | S32 | U7 | 967015.44 / 967013.79 (-0.0%) | 53490.82 / 53490.12 (-0.0%) | 2987.65 / 2987.43 (-0.0%) | 179.19 / 179.14 (-0.0%) | 14.15 / 14.14 (-0.1%) | 1.37 / 1.37 (-0.1%) | 0.14 / 0.14 (-0.2%) |
| CFD | S32 | U8 | 698652.07 / 698650.16 (-0.0%) | 38664.48 / 38663.62 (-0.0%) | 2168.53 / 2168.25 (-0.0%) | 133.65 / 133.58 (-0.1%) | 11.32 / 11.31 (-0.1%) | 1.10 / 1.10 (-0.2%) | 0.10 / 0.10 (-0.4%) |
| CFD | S35 | U1 | 1299910.95 / 1299908.91 (-0.0%) | 71886.04 / 71885.10 (-0.0%) | 4005.57 / 4005.24 (-0.0%) | 236.15 / 236.06 (-0.0%) | 17.59 / 17.58 (-0.1%) | 1.62 / 1.62 (-0.2%) | 0.17 / 0.17 (-0.3%) |
| CFD | S35 | U2 | 583710.50 / 583708.06 (-0.0%) | 32314.60 / 32313.44 (-0.0%) | 1817.48 / 1817.07 (-0.0%) | 113.77 / 113.66 (-0.1%) | 9.97 / 9.94 (-0.2%) | 0.97 / 0.97 (-0.4%) | 0.09 / 0.09 (-0.8%) |
| CFD | S35 | U3 | 1070651.25 / 1070648.95 (-0.0%) | 59220.10 / 59219.02 (-0.0%) | 3305.76 / 3305.37 (-0.0%) | 197.22 / 197.12 (-0.1%) | 15.22 / 15.19 (-0.1%) | 1.44 / 1.44 (-0.2%) | 0.15 / 0.15 (-0.4%) |
| CFD | S35 | U4 | 907289.01 / 907284.69 (-0.0%) | 50209.72 / 50207.21 (-0.0%) | 2816.39 / 2815.30 (-0.0%) | 174.25 / 173.89 (-0.2%) | 15.25 / 15.16 (-0.6%) | 1.60 / 1.59 (-1.0%) | 0.16 / 0.16 (-2.1%) |
| CFD | S35 | U5 | 1204522.84 / 1204519.42 (-0.0%) | 66626.15 / 66624.36 (-0.0%) | 3720.16 / 3719.46 (-0.0%) | 222.80 / 222.59 (-0.1%) | 17.67 / 17.62 (-0.3%) | 1.73 / 1.72 (-0.4%) | 0.17 / 0.17 (-0.9%) |
| CFD | S35 | U6 | 871468.17 / 871465.35 (-0.0%) | 48216.53 / 48215.09 (-0.0%) | 2698.39 / 2697.84 (-0.0%) | 163.99 / 163.83 (-0.1%) | 13.62 / 13.59 (-0.3%) | 1.42 / 1.41 (-0.4%) | 0.16 / 0.15 (-0.7%) |
| CFD | S35 | U7 | 987628.65 / 987626.87 (-0.0%) | 54632.71 / 54631.93 (-0.0%) | 3052.25 / 3051.99 (-0.0%) | 183.38 / 183.31 (-0.0%) | 14.56 / 14.55 (-0.1%) | 1.43 / 1.43 (-0.1%) | 0.16 / 0.16 (-0.2%) |
| CFD | S35 | U8 | 971381.14 / 971379.16 (-0.0%) | 53732.78 / 53731.88 (-0.0%) | 3001.26 / 3000.95 (-0.0%) | 179.97 / 179.89 (-0.0%) | 14.13 / 14.11 (-0.1%) | 1.31 / 1.30 (-0.2%) | 0.12 / 0.12 (-0.4%) |
| CFD | S50 | U1 | 662742.39 / 662740.67 (-0.0%) | 36680.15 / 36679.43 (-0.0%) | 2058.41 / 2058.17 (-0.0%) | 127.18 / 127.12 (-0.0%) | 10.78 / 10.77 (-0.1%) | 1.02 / 1.02 (-0.1%) | 0.09 / 0.09 (-0.3%) |
| CFD | S50 | U2 | 785787.78 / 785786.33 (-0.0%) | 43475.05 / 43474.46 (-0.0%) | 2432.89 / 2432.71 (-0.0%) | 147.98 / 147.94 (-0.0%) | 12.16 / 12.16 (-0.1%) | 1.16 / 1.16 (-0.1%) | 0.11 / 0.11 (-0.2%) |
| CFD | S50 | U3 | 976386.34 / 976384.61 (-0.0%) | 54012.64 / 54011.93 (-0.0%) | 3018.31 / 3018.09 (-0.0%) | 181.48 / 181.43 (-0.0%) | 14.36 / 14.35 (-0.1%) | 1.37 / 1.37 (-0.1%) | 0.14 / 0.14 (-0.2%) |
| CFD | S50 | U4 | 5567193.58 / 5567190.56 (-0.0%) | 307663.15 / 307661.63 (-0.0%) | 17040.98 / 17040.40 (-0.0%) | 961.33 / 961.16 (-0.0%) | 59.92 / 59.89 (-0.1%) | 4.54 / 4.53 (-0.1%) | 0.53 / 0.53 (-0.2%) |
| CFD | S50 | U5 | 448252.33 / 448250.53 (-0.0%) | 24828.37 / 24827.58 (-0.0%) | 1403.21 / 1402.95 (-0.0%) | 90.79 / 90.72 (-0.1%) | 8.61 / 8.60 (-0.2%) | 0.86 / 0.86 (-0.2%) | 0.08 / 0.08 (-0.5%) |
| CFD | S50 | U6 | 841253.51 / 841251.71 (-0.0%) | 46545.60 / 46544.81 (-0.0%) | 2605.61 / 2605.35 (-0.0%) | 158.76 / 158.69 (-0.0%) | 13.14 / 13.13 (-0.1%) | 1.30 / 1.30 (-0.1%) | 0.13 / 0.13 (-0.3%) |
| CFD | S50 | U7 | 665559.21 / 665557.75 (-0.0%) | 36833.09 / 36832.50 (-0.0%) | 2065.90 / 2065.73 (-0.0%) | 127.49 / 127.45 (-0.0%) | 11.05 / 11.04 (-0.1%) | 1.17 / 1.17 (-0.1%) | 0.13 / 0.13 (-0.1%) |
| CFD | S50 | U8 | 499443.78 / 499442.16 (-0.0%) | 27658.14 / 27657.48 (-0.0%) | 1560.30 / 1560.10 (-0.0%) | 100.07 / 100.02 (-0.0%) | 9.43 / 9.42 (-0.1%) | 0.96 / 0.95 (-0.1%) | 0.08 / 0.08 (-0.3%) |

ky grid (g): 0.0100, 0.0116, 0.0135, 0.0157, 0.0183, 0.0213, 0.0248, 0.0288, 0.0335, 0.0390, 0.0453, 0.0527, 0.0613, 0.0713, 0.0829, 0.0965, 0.1122, 0.1305, 0.1518, 0.1765, 0.2053, 0.2388, 0.2778, 0.3231, 0.3758, 0.4371, 0.5084, 0.5913, 0.6878, 0.8000

## Desagregación consultada

A pedido del propietario se resumió la desagregación propia del proyecto (`data/hazard/disagg/M2V4D/CFD/RMwTable.Rds`) en `disagg-Mw-by-TR.csv` y `disagg-Mw-by-TR.log` (Mw media, modal, mediana y percentil 84 por período y TR); los períodos de los taludes están en `shear-periods.log`. El reparto de magnitudes es decisión del propietario; estos resúmenes no lo modifican. El DOCX de desagregación anunciado no fue entregado durante la tarea.

## Archivos de la tarea

- Estado y entrega: `STATE.md`, `RESULTADOS.md`, `paso5-citas.md`, `newmark-1.7.1-functions.txt`, `magnitude-map.csv`.
- Hashes: `sha-before.txt`, `sha-M65.txt`, `sha-M55.txt`, `sha-after.txt`, `combine-log.csv` (primera combinación, superada), `combine2-log.csv`.
- Logs: `push-20261014.log`, `newmark-M65-dryrun.log`, `newmark-M65-run.log`, `newmark-M55-dryrun.log`, `newmark-M55-run.log`, `verifyRun-M65.log`, `verifyRun-M55.log`, `combine.log` y `postCheck.log` (primera combinación), `combine2.log`, `postCheck2.log`, `inspectKmaxZeros.log`, `disagg-Mw-by-TR.log`, `shear-periods.log`.
- Scripts R (`scripts/`): `inspectLibrary.R`, `dumpFunctions.R`, `scanSeed.R`, `dumpMore.R`, `inspectProducts.R`, `verifyRun.R`, `combine.R`, `postCheck.R`, `compareTables.R`, `inspectKmaxZeros.R`, `disaggMw.R`, `combine2.R`, `postCheck2.R`, `compareTables2.R`; generador de este informe `writeDocs.py`.
- Comparaciones: `compare-tables.md`, `kmax-compare.csv`, `dn-compare.csv`, `disagg-Mw-by-TR.csv`.
