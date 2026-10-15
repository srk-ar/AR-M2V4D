# Resultados: generación de hazard NBCC 2020 con CAN deduplicado y productos Newmark combinados por TR

Tarea `dev/SoT/m65-20261014/`, 2026-10-14 y 2026-10-15. Proyecto AR-M2V4D, sitio CFD. Productores hazard 0.2.0 (reinstalada el 2026-10-15 con la corrección del lector de realizations), newmark 1.7.1, data.table 1.18.6.1, OpenQuake 3.26.2, R con `Rscript --vanilla`. Estado en `STATE.md`; hallazgos sobre los árboles y el modelo de fuentes en `can-trt-hallazgos.md`. La entrega anterior de esta tarea (combinación por magnitudes sobre el hazard anterior, 2026-10-14) está en el commit `dddf10b` y sus logs en `logs-m65-20261014-old-hazard/`.

## Resumen

- Modelo de fuentes: `ssm/CAN` reescrito sin el triple conteo de las zonas de fondo del cratón (piloto cálculo 34 en tms9900: cocientes 0.930–0.947 a TR 2475 frente a la generación commiteada; detalle en `can-trt-hallazgos.md` §5). El modelo anterior queda en `CAN/legacy/v2020.1.4`.
- Árboles GMM: tokens `NBCC` en los cinco TRT de las recetas clásica, de escenario y de desagregación (`specs/calcs/`). El seed SCC trae los pesos oficiales por IMT y, desde el 2026-10-15, un peso interpolado en log(T) para cada uno de los 32 períodos de la casa (`scripts/interpolateNBCCWeights.R`; nodos oficiales intactos; suma exacta 0.5 por período). Sin esa extensión OpenQuake aplicaba el peso base en los 21 períodos no listados y el espectro salía aserrado; esa generación se abortó y se reemplazó (§7 de los hallazgos).
- Cálculos: 25 celdas lanzadas el 2026-10-14 a las 23:51 y terminadas a la 01:24 (tms9900: clásicas 59–62 para Vs30 1250, 180, 360 y 760, escenarios 63–70, desagregación 71; motor local: clásicas 78–81 para 1500, 270, 560 y 800, escenarios 82–89). Extraídas a `data/hazard/output` reemplazando las familias de `dddf10b`, que quedan en git.
- Celda 760 frente a la corrida 2024 (`nbcc-interp-vs-nrc2024-760.txt`): espectro liso en los 32 períodos; a TR 2475, PGA 1.10, SA 0.05–0.3 s entre 0.80 y 0.94, SA 0.35–4 s entre 0.79 y 0.89.
- Posproceso: `hazard process` con AEP, UHS, DEQ, SAEP y RMw (01:28) y, tras la corrección de hazard (`88d3aee`, defecto `BUG-MCE-REALIZATIONS-MULTILINE-20261015`), MCE y MCER (09:47). Sin el paso `gmpe` (`GMPETable.Rds` sigue siendo del 2026-09-23 por el defecto del token reportado el 2026-10-14) ni `rmw` previo distinto del corrido.
- Newmark: corridas `newmark process newmark-M65.json --root . --steps dn,kmax --seed 20260915` (09:48–09:54) y `newmark-M55.json` (09:54–10:00), ambas exit 0, con el mismo reparto de magnitudes del 2026-10-14 (`magnitude-map.csv`). Combinación publicada en `data/newmark/` con `scripts/combine2.R`, `PGATable.csv` publicado desde la corrida, verificada con `scripts/postCheck2.R` (`ALL CHECKS PASSED: TRUE`), `PROCEDENCIA.md` al lado.
- Capítulos `_chapters/ts.model.md` y `.es.md` rehidratados desde el scaffold `reports/sha` (ecuación de T_s con la altura desde el ápice, coherente con `ShearTable.Rds`).
- Sin commit de productos: pendiente de la palabra del propietario. Render pendiente de la selección de artefactos.

## SHA-256 antes y después de cada producto de `data/newmark/`

| Archivo | Antes (hazard anterior, `dddf10b`, 2026-10-14) | Corrida Mw 5.5 | Corrida Mw 6.5 | Después (combinado) | Filas por magnitud |
|---|---|---|---|---|---|
| `ShearTable.Rds` | `334359667159dd8f928c54d4f40484af1162372a0e4114aee666691104b3cf29` | `334359667159dd8f928c54d4f40484af1162372a0e4114aee666691104b3cf29` | `334359667159dd8f928c54d4f40484af1162372a0e4114aee666691104b3cf29` | `334359667159dd8f928c54d4f40484af1162372a0e4114aee666691104b3cf29` | sin cambio |
| `M2V4D/CFD/PGATable.csv` | `325fb141ea5126a46bd0baf82b89a76d03a4cc86adc36f3b74ac770f9b6c8cbf` | `015a84bc582617676cb9856be21928bd0b7f45a1480b916ed43a19efacb9f24b` | `015a84bc582617676cb9856be21928bd0b7f45a1480b916ed43a19efacb9f24b` | `015a84bc582617676cb9856be21928bd0b7f45a1480b916ed43a19efacb9f24b` | copiado de la corrida (idéntico en ambas) |
| `M2V4D/CFD/DnDraws.Rds` | `672b43170c22e1a165ef635352c0f1ccc92a2a0106f7a0775cb3b69808d81bac` | `d283cbddc35ae1a9e60883092a4c7b8969c0d96e7c4695dc4fb63e0addaca1c4` | `6e2d891d0a584549368ef78ffb9241d684a7a2bc9da835920ae4a076ab89a66d` | `59423c6aa1bd6e7f15c850d495ce078665065b1b40bf57a05813a0253b21f229` | 10 800 000 (5.5) + 5 400 000 (6.5) = 16 200 000 |
| `M2V4D/CFD/DnTable.Rds` | `5ee864387c77b973c3d8227b53841147beb2b97dc085a022b8ef033056e4c18c` | `1802db4b7562269829b669e9a5f90dcc7efd61c0bfb231b79c1f47c2a025fce9` | `322d30704fb5ddbe201db976cb6628d0a2034584a625cd7073628319c926de46` | `f1a03ba421869204846994a3d6aaa590e488847b49168837a9af5ca2d8c3af7f` | 460 800 (5.5) + 230 400 (6.5) = 691 200 |
| `M2V4D/CFD/kmaxTable.Rds` | `56e8efd3d10e56cf2f676adb3bc31a747316d7557c99a781bf63ecd8d54b7b9a` | `e6766743c9275226e61d962997c87cbec6004e966ac0c8a58358b1105b724025` | `b589f1184cd22022da16f4b39c34fe0f5cd85bc948acfb7eb17c8ceeb0c9de06` | `32653b7158e0a8899e9ac16313124d5a3dc27a112428a386216adcacf99a3fc5` | 491 520 (5.5) + 245 760 (6.5) = 737 280 |
| `DnTable.Rds` | `5ee864387c77b973c3d8227b53841147beb2b97dc085a022b8ef033056e4c18c` | `1802db4b7562269829b669e9a5f90dcc7efd61c0bfb231b79c1f47c2a025fce9` | `322d30704fb5ddbe201db976cb6628d0a2034584a625cd7073628319c926de46` | `f1a03ba421869204846994a3d6aaa590e488847b49168837a9af5ca2d8c3af7f` | 460 800 (5.5) + 230 400 (6.5) = 691 200 |
| `DnPlotTable.Rds` | `40337a6e3449efca08fd3ab4d3ef943b9b9e932edd90de81244b43af767b7596` | `41089cf72938c666cc0bdd2e95d6f3c21fcaf9b3e01eec6b03c8c2f6e0865e98` | `a2fdfdd02a0d9c1cbf1f3948f110f5137250f616f11c97b5339c789ba74d4f66` | `880d4251b942ea76d8c005f207c71fc0d453feb2f0ed632887f193d8cd28dda1` | 35 747 (5.5) + 24 790 (6.5) = 60 537 |
| `kmaxTable.Rds` | `56e8efd3d10e56cf2f676adb3bc31a747316d7557c99a781bf63ecd8d54b7b9a` | `e6766743c9275226e61d962997c87cbec6004e966ac0c8a58358b1105b724025` | `b589f1184cd22022da16f4b39c34fe0f5cd85bc948acfb7eb17c8ceeb0c9de06` | `32653b7158e0a8899e9ac16313124d5a3dc27a112428a386216adcacf99a3fc5` | 491 520 (5.5) + 245 760 (6.5) = 737 280 |

`DnPlotTable.Rds` no conserva el número de filas de la generación anterior porque la librería omite las filas con Dn ≤ 1e-4 cm; los bloques por TR se tomaron completos de cada corrida.

## Logs de las corridas

### Mw 6.5: dry-run (`newmark-M65-dryrun.log`)

```
command: newmark process newmark-M65.json --root . --steps dn,kmax --seed 20260915 --dry-run
>> Dn models: subduction = FALSE -> BM17 off, BM19 on
dry run: /Users/averrik/Cloud/github/projects/AR-M2V4D/newmark-M65.json
steps: dn, kmax
sites: CFD
dn: replaces /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M65/M2V4D/CFD/DnDraws.Rds
dn: replaces /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M65/M2V4D/CFD/PGATable.csv
dn: replaces /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M65/M2V4D/CFD/DnTable.Rds
dn: replaces /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M65/DnPlotTable.Rds
dn: replaces /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M65/DnTable.Rds
kmax: replaces /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M65/M2V4D/CFD/kmaxTable.Rds
kmax: replaces /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M65/kmaxTable.Rds
```

### Mw 6.5: corrida (`newmark-M65-run.log`)

```
command: newmark process newmark-M65.json --root . --steps dn,kmax --seed 20260915
start: 2026-10-15 09:48:45 -0300
>> Dn models: subduction = FALSE -> BM17 off, BM19 on
dn: wrote site CFD
kmax: wrote site CFD
Warning messages:
1: siteID=CFD: 79528/737280 kmax rows use roots beyond sampled support (max beyond=0.56; max kmax=0.4563 g at siteID=CFD ID=M2V4D IDg=S35 IDm=U4 IDn=BT07 p=0.95 Da=1.35) 
2: global: 79528/737280 kmax rows use roots beyond sampled support (max beyond=0.56; max kmax=0.4563 g at siteID=CFD ID=M2V4D IDg=S35 IDm=U4 IDn=BT07 p=0.95 Da=1.35) 
end: 2026-10-15 09:54:28 -0300
```

### Mw 6.5: verificación contra la corrida del 2026-10-14 con la misma magnitud (`verifyRun-M65.log`)

```
== ShearTable ==
sha orig: 334359667159dd8f928c54d4f40484af1162372a0e4114aee666691104b3cf29 
sha M65 : 334359667159dd8f928c54d4f40484af1162372a0e4114aee666691104b3cf29 

== PGATable.csv ==
sha orig: 325fb141ea5126a46bd0baf82b89a76d03a4cc86adc36f3b74ac770f9b6c8cbf 
sha M65 : 015a84bc582617676cb9856be21928bd0b7f45a1480b916ed43a19efacb9f24b 
identical content: FALSE 

== DnTable.Rds ==
dim orig: 691200x12  dim M65: 691200x12 
same names: TRUE  same classes: TRUE  same key: TRUE 
same attribute names: TRUE 
rows matched by key: 691200 of 691200 
       ID TRlabel     n nDiff       maxRel
   <char>  <char> <int> <int>        <num>
1:  M2V4D     100 76800 55066 1.000000e+00
2:  M2V4D    1000 76800 66463 1.000000e+00
3:  M2V4D   10000 76800 74181 1.000000e+00
4:  M2V4D     200 76800 58409 5.021205e+12
5:  M2V4D    2000 76800 69338 1.000000e+00
6:  M2V4D    2500 76800 70199 1.000000e+00
7:  M2V4D     500 76800 63192 1.000000e+00
8:  M2V4D    5000 76800 72607 1.000000e+00
9:    MCE     MCE 76800 73886 2.472548e+00

== kmaxTable.Rds ==
dim orig: 737280x18  dim M65: 737280x18 
same names: TRUE  same classes: TRUE  same key: TRUE 
same attribute names: TRUE 
rows matched by key: 737280 of 737280 
       ID TRlabel     n nDiff        maxRel
   <char>  <char> <int> <int>         <num>
1:  M2V4D     100 81920 19700 4.065245e+297
2:  M2V4D    1000 81920 47337  1.000000e+00
3:  M2V4D   10000 81920 71068 3.383820e+295
4:  M2V4D     200 81920 19040 2.227418e+297
5:  M2V4D    2000 81920 57078  1.000000e+00
6:  M2V4D    2500 81920 59769  1.000000e+00
7:  M2V4D     500 81920 35285 3.989255e+294
8:  M2V4D    5000 81920 66720  1.000000e+00
9:    MCE     MCE 81920 60619 1.412200e+298

== DnPlotTable.Rds ==
dim orig: 64752x8  dim M65: 60923x8 
same names: TRUE  same classes: TRUE  same key: TRUE 
same attribute names: TRUE 
rows matched by key: 37666 of 64752 
       ID TRlabel     n nDiff    maxRel
   <char>  <char> <int> <int>     <num>
1:  M2V4D     100  1101  1101 0.9988607
2:  M2V4D    1000  3792  3792 0.9970590
3:  M2V4D   10000  6824  6824 0.9997639
4:  M2V4D     200  1767  1767 1.0831509
5:  M2V4D    2000  5131  5131 0.9979266
6:  M2V4D    2500  5224  5224 0.9988544
7:  M2V4D     500  2936  2936 0.9978281
8:  M2V4D    5000  5777  5777 0.9992611
9:    MCE     MCE  5114  5114 1.1451835

== ky grids per cell identical between runs? ==
cells: 360  identical ky grids: 360 
one common grid across all cells (orig): TRUE 

== DnDraws: sampled PGA.s identical between runs (same random stream)? ==
dim orig: 16200000x11  dim M65: 16200000x11  same key: TRUE 
       ID TRlabel     n samePGAs sameDnAM88
   <char>  <char> <int>    <int>      <int>
1:  M2V4D     100 12000        0       3338
2:  M2V4D    1000 12000        0          0
3:  M2V4D   10000 12000        0          0
4:  M2V4D     200 12000        0        120
5:  M2V4D    2000 12000        0          0
6:  M2V4D    2500 12000        0          0
7:  M2V4D     500 12000        0          0
8:  M2V4D    5000 12000        0          0
9:    MCE     MCE 12000        0          0
       ID TRlabel     n sameDnBM19    maxRel
   <char>  <char> <int>      <int>     <num>
1:  M2V4D     100 12000          0 0.8473586
2:  M2V4D    1000 12000          0 0.6275444
3:  M2V4D   10000 12000          0 0.4812547
4:  M2V4D     200 12000          0 0.7872830
5:  M2V4D    2000 12000          0 0.5111020
6:  M2V4D    2500 12000          0 0.4709510
7:  M2V4D     500 12000          0 0.7244805
8:  M2V4D    5000 12000          0 0.4469181
9:    MCE     MCE 12000          0 0.6863690
```

### Mw 5.5: dry-run (`newmark-M55-dryrun.log`)

```
command: newmark process newmark-M55.json --root . --steps dn,kmax --seed 20260915 --dry-run
>> Dn models: subduction = FALSE -> BM17 off, BM19 on
dry run: /Users/averrik/Cloud/github/projects/AR-M2V4D/newmark-M55.json
steps: dn, kmax
sites: CFD
dn: replaces /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M55/M2V4D/CFD/DnDraws.Rds
dn: replaces /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M55/M2V4D/CFD/PGATable.csv
dn: replaces /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M55/M2V4D/CFD/DnTable.Rds
dn: replaces /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M55/DnPlotTable.Rds
dn: replaces /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M55/DnTable.Rds
kmax: replaces /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M55/M2V4D/CFD/kmaxTable.Rds
kmax: replaces /Users/averrik/Cloud/github/projects/AR-M2V4D/data/newmark-M55/kmaxTable.Rds
```

### Mw 5.5: corrida (`newmark-M55-run.log`)

```
command: newmark process newmark-M55.json --root . --steps dn,kmax --seed 20260915
start: 2026-10-15 09:54:29 -0300
>> Dn models: subduction = FALSE -> BM17 off, BM19 on
dn: wrote site CFD
kmax: wrote site CFD
Warning messages:
1: siteID=CFD: 79032/737280 kmax rows use roots beyond sampled support (max beyond=0.56; max kmax=0.3987 g at siteID=CFD ID=MCE IDg=S27 IDm=U4 IDn=rigid p=0.95 Da=1.35) 
2: global: 79032/737280 kmax rows use roots beyond sampled support (max beyond=0.56; max kmax=0.3987 g at siteID=CFD ID=MCE IDg=S27 IDm=U4 IDn=rigid p=0.95 Da=1.35) 
end: 2026-10-15 10:00:09 -0300
```

### Mw 5.5: verificación contra la corrida del 2026-10-14 con la misma magnitud (`verifyRun-M55.log`)

```
== ShearTable ==
sha orig: 334359667159dd8f928c54d4f40484af1162372a0e4114aee666691104b3cf29 
sha M65 : 334359667159dd8f928c54d4f40484af1162372a0e4114aee666691104b3cf29 

== PGATable.csv ==
sha orig: 325fb141ea5126a46bd0baf82b89a76d03a4cc86adc36f3b74ac770f9b6c8cbf 
sha M65 : 015a84bc582617676cb9856be21928bd0b7f45a1480b916ed43a19efacb9f24b 
identical content: FALSE 

== DnTable.Rds ==
dim orig: 691200x12  dim M65: 691200x12 
same names: TRUE  same classes: TRUE  same key: TRUE 
same attribute names: TRUE 
rows matched by key: 691200 of 691200 
       ID TRlabel     n nDiff       maxRel
   <char>  <char> <int> <int>        <num>
1:  M2V4D     100 76800 55066 1.000000e+00
2:  M2V4D    1000 76800 66463 1.000000e+00
3:  M2V4D   10000 76800 74181 1.000000e+00
4:  M2V4D     200 76800 58409 5.021205e+12
5:  M2V4D    2000 76800 69338 1.000000e+00
6:  M2V4D    2500 76800 70199 1.000000e+00
7:  M2V4D     500 76800 63192 1.000000e+00
8:  M2V4D    5000 76800 72607 1.000000e+00
9:    MCE     MCE 76800 73886 2.472548e+00

== kmaxTable.Rds ==
dim orig: 737280x18  dim M65: 737280x18 
same names: TRUE  same classes: TRUE  same key: TRUE 
same attribute names: TRUE 
rows matched by key: 737280 of 737280 
       ID TRlabel     n nDiff        maxRel
   <char>  <char> <int> <int>         <num>
1:  M2V4D     100 81920 18413 4.065245e+297
2:  M2V4D    1000 81920 44661  1.000000e+00
3:  M2V4D   10000 81920 68227  1.000000e+00
4:  M2V4D     200 81920 17412 2.227418e+297
5:  M2V4D    2000 81920 54420  1.000000e+00
6:  M2V4D    2500 81920 57118  1.000000e+00
7:  M2V4D     500 81920 32780 3.989255e+294
8:  M2V4D    5000 81920 63960  1.000000e+00
9:    MCE     MCE 81920 58338 1.378930e+298

== DnPlotTable.Rds ==
dim orig: 64361x8  dim M65: 60486x8 
same names: TRUE  same classes: TRUE  same key: TRUE 
same attribute names: TRUE 
rows matched by key: 36436 of 64361 
       ID TRlabel     n nDiff    maxRel
   <char>  <char> <int> <int>     <num>
1:  M2V4D     100  1055  1055 0.9988607
2:  M2V4D    1000  3558  3558 0.9970590
3:  M2V4D   10000  6751  6751 0.9997639
4:  M2V4D     200  1671  1671 1.0831509
5:  M2V4D    2000  5006  5006 0.9979266
6:  M2V4D    2500  5107  5107 0.9988544
7:  M2V4D     500  2714  2714 0.9978281
8:  M2V4D    5000  5668  5668 0.9992611
9:    MCE     MCE  4906  4906 0.9999430

== ky grids per cell identical between runs? ==
cells: 360  identical ky grids: 360 
one common grid across all cells (orig): TRUE 

== DnDraws: sampled PGA.s identical between runs (same random stream)? ==
dim orig: 16200000x11  dim M65: 16200000x11  same key: TRUE 
       ID TRlabel     n samePGAs sameDnAM88
   <char>  <char> <int>    <int>      <int>
1:  M2V4D     100 12000        0       3338
2:  M2V4D    1000 12000        0          0
3:  M2V4D   10000 12000        0          0
4:  M2V4D     200 12000        0        120
5:  M2V4D    2000 12000        0          0
6:  M2V4D    2500 12000        0          0
7:  M2V4D     500 12000        0          0
8:  M2V4D    5000 12000        0          0
9:    MCE     MCE 12000        0          0
       ID TRlabel     n sameDnBM19    maxRel
   <char>  <char> <int>      <int>     <num>
1:  M2V4D     100 12000          0 0.8473586
2:  M2V4D    1000 12000          0 0.6275444
3:  M2V4D   10000 12000          0 0.4812547
4:  M2V4D     200 12000          0 0.7872830
5:  M2V4D    2000 12000          0 0.5111020
6:  M2V4D    2500 12000          0 0.4709510
7:  M2V4D     500 12000          0 0.7244805
8:  M2V4D    5000 12000          0 0.4469181
9:    MCE     MCE 12000          0 0.6863690
```

Lectura de las verificaciones: la referencia es la corrida de la misma magnitud sobre el hazard anterior, así que `nDiff` cuenta las filas cuyo valor cambia por el hazard; la estructura, las clases y la clave son las mismas y todas las filas de `DnTable` y `kmaxTable` se emparejan por clave. `DnPlotTable` empareja menos filas porque su contenido depende de los valores.

### Combinación (`combine2.log`)

```
M2V4D/CFD/DnDraws.Rds        newmark-M55=10800000 newmark-M65=5400000  total  16200000  sha 672b43170c22 -> 59423c6aa1bd
M2V4D/CFD/DnTable.Rds        newmark-M55=460800 newmark-M65=230400  total    691200  sha 5ee864387c77 -> f1a03ba42186
M2V4D/CFD/kmaxTable.Rds      newmark-M55=491520 newmark-M65=245760  total    737280  sha 56e8efd3d10e -> 32653b7158e0
DnTable.Rds                  newmark-M55=460800 newmark-M65=230400  total    691200  sha 5ee864387c77 -> f1a03ba42186
DnPlotTable.Rds              newmark-M55=35747 newmark-M65=24790  total     60537  sha 40337a6e3449 -> 880d4251b942
kmaxTable.Rds                newmark-M55=491520 newmark-M65=245760  total    737280  sha 56e8efd3d10e -> 32653b7158e0
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
DnPlotTable.Rds              rows     60537  schema/key/attrs TRUE  key order TRUE  all rows mapped TRUE
   blocks: newmark-M55[100,200,500,1000,2000,2500]=TRUE  newmark-M65[5000,10000,MCE]=TRUE
   rows by ID,TR: M2V4D/100=3361 M2V4D/200=4436 M2V4D/500=5907 M2V4D/1000=6795 M2V4D/2000=7536 M2V4D/2500=7712 M2V4D/5000=8178 M2V4D/10000=8534 MCE/NA=8078
kmaxTable.Rds                rows    737280  schema/key/attrs TRUE  key order TRUE  all rows mapped TRUE
   blocks: newmark-M55[100,200,500,1000,2000,2500]=TRUE  newmark-M65[5000,10000,MCE]=TRUE
   rows by ID,TR: M2V4D/100=81920 M2V4D/200=81920 M2V4D/500=81920 M2V4D/1000=81920 M2V4D/2000=81920 M2V4D/2500=81920 M2V4D/5000=81920 M2V4D/10000=81920 MCE/NA=81920

PGATable.csv == backup: TRUE 
ShearTable.Rds == backup: TRUE 

ALL CHECKS PASSED: TRUE
```

## Tablas comparativas: combinación del 2026-10-14 (hazard anterior) frente a la publicada (hazard NBCC)

Celdas `anterior / nuevo (diferencia relativa %)`, con la diferencia relativa definida como 100·(nuevo − anterior)/anterior y la misma magnitud en ambos lados. kmax y Dn son los del modelo `ensemble` con `p = mean`, el estadístico que publican las tablas del informe. Para kmax, cada geometría se muestra en sus propios objetivos relativos `Da = signif(DaH·Hs, 6)` con `DaH` del contrato; para Dn se muestran siete de los 30 `ky` de la grilla común. Resúmenes para las nueve demandas; tablas por celda para TR 10000 y MCE; todas las celdas en `kmax-compare.csv` y `dn-compare.csv` (`scripts/compareTables2.R`, referencia = respaldo de `data/newmark` de `dddf10b`). En TR 100 y 200 las diferencias relativas de kmax son erráticas porque muchas celdas tienen kmax casi nulo en una u otra generación; las medianas de TR 500 en adelante y las de Dn describen el cambio.


### Resumen por demanda: diferencia relativa (%) de kmax (ensemble, media) por geometría, [mín, mediana, máx] sobre materiales y Da/H

| Demanda | Mw | S135 | S27 | S32 | S35 | S50 |
|---|---|---|---|---|---|---|
| TR 100 | 5.5 | [3.1, 64.0, 87.8] | [-43.4, 17.2, 122.6] | [-42.6, 35.7, 141.9] | [-43.8, 28.9, 89.4] | [-35.2, 45.1, 94.3] |
| TR 200 | 5.5 | [-45.7, 3.0, 1407.6] | [-45.2, -36.8, 249.6] | [-48.2, -34.4, 816.4] | [-45.2, -36.8, 2406.1] | [-50.2, -35.0, 1101.4] |
| TR 500 | 5.5 | [-86.0, -43.2, -30.0] | [-57.2, -36.1, -25.5] | [-63.2, -36.8, -26.2] | [-57.6, -37.8, -26.6] | [-82.3, -39.3, -30.3] |
| TR 1000 | 5.5 | [-54.8, -39.8, -32.0] | [-43.8, -31.8, -22.9] | [-46.0, -32.1, -23.5] | [-45.0, -32.7, -23.7] | [-48.9, -34.5, -26.3] |
| TR 2000 | 5.5 | [-47.2, -37.2, -29.8] | [-39.1, -28.6, -22.3] | [-41.1, -29.6, -22.9] | [-42.4, -30.1, -23.0] | [-42.3, -32.7, -25.2] |
| TR 2500 | 5.5 | [-45.7, -37.2, -29.9] | [-39.4, -28.0, -22.2] | [-39.3, -29.1, -22.7] | [-38.7, -29.2, -22.8] | [-40.9, -32.1, -25.2] |
| TR 5000 | 6.5 | [-41.3, -37.3, -29.2] | [-35.7, -25.8, -21.3] | [-35.9, -26.8, -22.1] | [-36.6, -27.1, -22.1] | [-38.4, -30.2, -24.4] |
| TR 10000 | 6.5 | [-41.2, -37.9, -30.0] | [-34.9, -25.9, -21.2] | [-35.3, -27.0, -22.3] | [-35.8, -27.0, -22.4] | [-38.5, -30.0, -25.0] |
| MCE | 6.5 | [-59.8, -53.9, -46.3] | [-54.0, -42.2, -34.5] | [-54.6, -43.9, -36.1] | [-55.0, -44.3, -36.4] | [-58.6, -47.4, -40.3] |

Celdas kmax con 0 en ambas generaciones (contadas como 0 %): 0 ; celdas con 0 sólo en una (sin diferencia definida): 1 

### Resumen por demanda: diferencia relativa (%) de Dn (ensemble, media) por geometría, [mín, mediana, máx] sobre materiales y los 30 ky

| Demanda | Mw | S135 | S27 | S32 | S35 | S50 |
|---|---|---|---|---|---|---|
| TR 100 | 5.5 | [-79.4, -69.9, -52.0] | [-54.5, -43.6, -39.1] | [-51.4, -45.3, -38.5] | [-50.5, -45.3, -37.7] | [-65.4, -53.9, -42.5] |
| TR 200 | 5.5 | [-71.9, -58.0, -39.3] | [-51.6, -40.3, -34.7] | [-48.1, -40.0, -33.5] | [-47.7, -39.9, -34.2] | [-52.4, -43.3, -36.5] |
| TR 500 | 5.5 | [-62.4, -50.5, -40.9] | [-48.3, -38.6, -31.2] | [-45.2, -39.5, -34.3] | [-44.7, -38.6, -34.6] | [-46.3, -39.7, -34.1] |
| TR 1000 | 5.5 | [-67.5, -54.8, -34.1] | [-56.9, -44.2, -30.5] | [-58.4, -45.1, -32.1] | [-56.4, -44.9, -31.9] | [-58.6, -46.2, -32.0] |
| TR 2000 | 5.5 | [-71.5, -60.3, -42.6] | [-65.5, -50.3, -28.1] | [-66.4, -51.7, -27.5] | [-65.9, -51.5, -28.0] | [-66.0, -54.3, -32.7] |
| TR 2500 | 5.5 | [-74.0, -62.3, -42.4] | [-67.7, -52.0, -25.6] | [-66.5, -52.9, -27.9] | [-67.1, -52.9, -27.8] | [-67.0, -55.4, -33.7] |
| TR 5000 | 6.5 | [-75.6, -66.2, -43.2] | [-71.9, -54.2, -19.3] | [-71.8, -55.0, -23.2] | [-71.1, -56.2, -23.9] | [-70.2, -58.6, -32.2] |
| TR 10000 | 6.5 | [-78.7, -68.3, -63.0] | [-74.1, -61.5, -24.8] | [-72.9, -61.9, -31.4] | [-74.7, -62.0, -27.1] | [-75.0, -63.4, -32.9] |
| MCE | 6.5 | [-98.4, -94.2, -88.4] | [-95.9, -93.0, -85.8] | [-97.3, -94.2, -88.5] | [-97.1, -94.1, -88.7] | [-97.9, -94.3, -88.2] |

### kmax (ensemble, p = mean) [g], TR 10000: hazard anterior (dddf10b) / hazard NBCC 2026-10-15, Mw 6.5 (diferencia relativa)

| siteID | IDg | Hs | IDm | Da/H 0.05% | Da/H 0.1% | Da/H 0.25% | Da/H 0.4% | Da/H 0.5% | Da/H 1% | Da/H 2.5% |
|---|---|---|---|---|---|---|---|---|---|---|
| CFD | S135 | 135 | U1 | 0.097 / 0.065 (-33.1%) | 0.074 / 0.049 (-34.2%) | 0.048 / 0.030 (-36.8%) | 0.036 / 0.022 (-38.7%) | 0.031 / 0.019 (-39.5%) | 0.019 / 0.011 (-41.2%) | 0.010 / 0.006 (-39.4%) |
| CFD | S135 | 135 | U2 | 0.101 / 0.068 (-33.0%) | 0.077 / 0.051 (-34.2%) | 0.050 / 0.031 (-37.1%) | 0.038 / 0.023 (-38.9%) | 0.033 / 0.020 (-39.5%) | 0.020 / 0.012 (-40.2%) | 0.011 / 0.006 (-39.9%) |
| CFD | S135 | 135 | U3 | 0.106 / 0.071 (-33.0%) | 0.081 / 0.054 (-34.1%) | 0.053 / 0.034 (-36.3%) | 0.041 / 0.025 (-38.3%) | 0.036 / 0.022 (-39.1%) | 0.022 / 0.013 (-41.1%) | 0.011 / 0.007 (-39.7%) |
| CFD | S135 | 135 | U4 | 0.111 / 0.078 (-30.0%) | 0.085 / 0.058 (-31.4%) | 0.055 / 0.036 (-34.3%) | 0.042 / 0.027 (-36.2%) | 0.036 / 0.023 (-36.9%) | 0.023 / 0.014 (-39.5%) | 0.012 / 0.007 (-39.4%) |
| CFD | S135 | 135 | U5 | 0.111 / 0.076 (-31.5%) | 0.085 / 0.057 (-32.7%) | 0.055 / 0.036 (-35.3%) | 0.042 / 0.027 (-37.1%) | 0.037 / 0.023 (-37.9%) | 0.023 / 0.014 (-40.3%) | 0.012 / 0.007 (-39.2%) |
| CFD | S135 | 135 | U6 | 0.104 / 0.071 (-32.1%) | 0.079 / 0.053 (-33.4%) | 0.051 / 0.033 (-35.8%) | 0.039 / 0.024 (-38.0%) | 0.034 / 0.020 (-39.4%) | 0.020 / 0.012 (-39.7%) | 0.011 / 0.006 (-40.5%) |
| CFD | S135 | 135 | U7 | 0.098 / 0.065 (-33.0%) | 0.074 / 0.049 (-34.1%) | 0.048 / 0.031 (-36.4%) | 0.037 / 0.023 (-38.5%) | 0.032 / 0.020 (-39.4%) | 0.020 / 0.012 (-40.6%) | 0.010 / 0.006 (-39.4%) |
| CFD | S135 | 135 | U8 | 0.100 / 0.067 (-33.0%) | 0.077 / 0.051 (-34.0%) | 0.050 / 0.032 (-36.5%) | 0.038 / 0.024 (-38.3%) | 0.034 / 0.020 (-39.7%) | 0.021 / 0.012 (-40.8%) | 0.011 / 0.007 (-39.9%) |
| CFD | S27 | 27 | U1 | 0.187 / 0.147 (-21.5%) | 0.150 / 0.116 (-22.8%) | 0.107 / 0.081 (-24.6%) | 0.088 / 0.066 (-25.7%) | 0.080 / 0.059 (-26.3%) | 0.057 / 0.040 (-28.9%) | 0.032 / 0.021 (-33.6%) |
| CFD | S27 | 27 | U2 | 0.198 / 0.155 (-21.6%) | 0.158 / 0.122 (-22.9%) | 0.113 / 0.085 (-24.8%) | 0.093 / 0.069 (-25.8%) | 0.084 / 0.062 (-26.5%) | 0.060 / 0.042 (-29.0%) | 0.033 / 0.022 (-33.8%) |
| CFD | S27 | 27 | U3 | 0.198 / 0.156 (-21.2%) | 0.159 / 0.123 (-22.5%) | 0.114 / 0.086 (-24.3%) | 0.094 / 0.070 (-25.4%) | 0.085 / 0.063 (-25.9%) | 0.061 / 0.044 (-28.2%) | 0.035 / 0.023 (-32.6%) |
| CFD | S27 | 27 | U4 | 0.230 / 0.174 (-24.2%) | 0.183 / 0.137 (-25.3%) | 0.131 / 0.096 (-26.9%) | 0.108 / 0.078 (-27.9%) | 0.097 / 0.070 (-28.4%) | 0.069 / 0.048 (-30.7%) | 0.039 / 0.026 (-34.9%) |
| CFD | S27 | 27 | U5 | 0.216 / 0.167 (-22.5%) | 0.172 / 0.132 (-23.7%) | 0.124 / 0.092 (-25.4%) | 0.102 / 0.075 (-26.4%) | 0.092 / 0.067 (-27.0%) | 0.066 / 0.047 (-29.2%) | 0.038 / 0.025 (-33.7%) |
| CFD | S27 | 27 | U6 | 0.205 / 0.160 (-22.1%) | 0.164 / 0.126 (-23.3%) | 0.117 / 0.088 (-25.1%) | 0.096 / 0.071 (-26.2%) | 0.087 / 0.064 (-26.7%) | 0.062 / 0.044 (-29.2%) | 0.035 / 0.023 (-33.8%) |
| CFD | S27 | 27 | U7 | 0.188 / 0.148 (-21.6%) | 0.151 / 0.117 (-22.9%) | 0.109 / 0.082 (-24.7%) | 0.090 / 0.067 (-25.8%) | 0.081 / 0.060 (-26.4%) | 0.058 / 0.041 (-28.9%) | 0.033 / 0.022 (-33.6%) |
| CFD | S27 | 27 | U8 | 0.185 / 0.145 (-21.6%) | 0.148 / 0.114 (-22.9%) | 0.106 / 0.080 (-24.7%) | 0.088 / 0.065 (-25.8%) | 0.079 / 0.058 (-26.5%) | 0.056 / 0.040 (-28.8%) | 0.032 / 0.021 (-34.0%) |
| CFD | S32 | 32 | U1 | 0.170 / 0.131 (-23.0%) | 0.136 / 0.103 (-24.2%) | 0.097 / 0.072 (-26.0%) | 0.080 / 0.058 (-27.1%) | 0.072 / 0.052 (-27.8%) | 0.051 / 0.035 (-30.5%) | 0.028 / 0.018 (-35.1%) |
| CFD | S32 | 32 | U2 | 0.182 / 0.142 (-22.3%) | 0.145 / 0.111 (-23.6%) | 0.103 / 0.077 (-25.5%) | 0.085 / 0.062 (-26.6%) | 0.076 / 0.056 (-27.3%) | 0.053 / 0.037 (-30.0%) | 0.029 / 0.019 (-35.1%) |
| CFD | S32 | 32 | U3 | 0.178 / 0.138 (-22.5%) | 0.143 / 0.109 (-23.7%) | 0.102 / 0.076 (-25.5%) | 0.084 / 0.062 (-26.6%) | 0.076 / 0.055 (-27.2%) | 0.054 / 0.037 (-30.0%) | 0.030 / 0.020 (-33.9%) |
| CFD | S32 | 32 | U4 | 0.209 / 0.159 (-23.7%) | 0.166 / 0.125 (-24.9%) | 0.118 / 0.087 (-26.7%) | 0.097 / 0.070 (-27.7%) | 0.088 / 0.063 (-28.4%) | 0.062 / 0.043 (-30.9%) | 0.034 / 0.022 (-35.2%) |
| CFD | S32 | 32 | U5 | 0.193 / 0.150 (-22.7%) | 0.154 / 0.117 (-23.9%) | 0.109 / 0.081 (-25.7%) | 0.089 / 0.065 (-26.9%) | 0.081 / 0.059 (-27.5%) | 0.057 / 0.040 (-30.2%) | 0.031 / 0.020 (-34.8%) |
| CFD | S32 | 32 | U6 | 0.184 / 0.143 (-22.4%) | 0.146 / 0.112 (-23.6%) | 0.103 / 0.077 (-25.4%) | 0.084 / 0.062 (-26.7%) | 0.076 / 0.055 (-27.4%) | 0.052 / 0.037 (-30.2%) | 0.028 / 0.018 (-35.0%) |
| CFD | S32 | 32 | U7 | 0.169 / 0.130 (-23.1%) | 0.135 / 0.103 (-24.3%) | 0.097 / 0.072 (-26.1%) | 0.080 / 0.058 (-27.2%) | 0.072 / 0.052 (-27.8%) | 0.051 / 0.035 (-30.5%) | 0.028 / 0.018 (-35.3%) |
| CFD | S32 | 32 | U8 | 0.171 / 0.132 (-22.9%) | 0.137 / 0.104 (-24.2%) | 0.098 / 0.073 (-25.9%) | 0.081 / 0.059 (-27.0%) | 0.073 / 0.053 (-27.8%) | 0.051 / 0.036 (-30.6%) | 0.029 / 0.019 (-34.2%) |
| CFD | S35 | 35 | U1 | 0.168 / 0.130 (-22.7%) | 0.135 / 0.102 (-24.0%) | 0.096 / 0.071 (-25.9%) | 0.079 / 0.057 (-27.1%) | 0.071 / 0.051 (-27.8%) | 0.050 / 0.034 (-30.6%) | 0.027 / 0.018 (-34.9%) |
| CFD | S35 | 35 | U2 | 0.176 / 0.136 (-22.5%) | 0.139 / 0.106 (-23.7%) | 0.098 / 0.073 (-25.6%) | 0.080 / 0.059 (-26.8%) | 0.072 / 0.052 (-27.5%) | 0.050 / 0.035 (-30.5%) | 0.027 / 0.017 (-35.6%) |
| CFD | S35 | 35 | U3 | 0.172 / 0.133 (-22.6%) | 0.137 / 0.104 (-23.9%) | 0.097 / 0.072 (-25.8%) | 0.079 / 0.058 (-27.0%) | 0.071 / 0.052 (-27.7%) | 0.050 / 0.034 (-30.5%) | 0.027 / 0.018 (-35.2%) |
| CFD | S35 | 35 | U4 | 0.204 / 0.155 (-24.0%) | 0.161 / 0.121 (-25.1%) | 0.114 / 0.083 (-26.9%) | 0.093 / 0.067 (-28.0%) | 0.084 / 0.060 (-28.7%) | 0.058 / 0.040 (-31.4%) | 0.032 / 0.020 (-35.8%) |
| CFD | S35 | 35 | U5 | 0.190 / 0.147 (-22.7%) | 0.151 / 0.115 (-23.9%) | 0.106 / 0.079 (-25.8%) | 0.087 / 0.063 (-26.9%) | 0.078 / 0.057 (-27.6%) | 0.054 / 0.038 (-30.3%) | 0.030 / 0.019 (-35.2%) |
| CFD | S35 | 35 | U6 | 0.189 / 0.147 (-22.4%) | 0.151 / 0.115 (-23.6%) | 0.107 / 0.080 (-25.4%) | 0.087 / 0.064 (-26.6%) | 0.079 / 0.057 (-27.3%) | 0.055 / 0.038 (-30.1%) | 0.030 / 0.020 (-34.6%) |
| CFD | S35 | 35 | U7 | 0.165 / 0.126 (-23.2%) | 0.132 / 0.100 (-24.4%) | 0.094 / 0.069 (-26.2%) | 0.077 / 0.056 (-27.4%) | 0.069 / 0.050 (-28.1%) | 0.048 / 0.033 (-31.1%) | 0.027 / 0.017 (-35.3%) |
| CFD | S35 | 35 | U8 | 0.168 / 0.129 (-23.0%) | 0.134 / 0.102 (-24.3%) | 0.095 / 0.071 (-26.1%) | 0.078 / 0.057 (-27.3%) | 0.071 / 0.051 (-27.9%) | 0.049 / 0.034 (-30.7%) | 0.027 / 0.018 (-35.4%) |
| CFD | S50 | 50 | U1 | 0.149 / 0.111 (-25.7%) | 0.119 / 0.087 (-26.7%) | 0.084 / 0.060 (-28.4%) | 0.068 / 0.048 (-29.8%) | 0.061 / 0.042 (-30.4%) | 0.042 / 0.028 (-33.2%) | 0.022 / 0.014 (-36.8%) |
| CFD | S50 | 50 | U2 | 0.149 / 0.111 (-25.7%) | 0.117 / 0.086 (-26.8%) | 0.082 / 0.058 (-28.7%) | 0.066 / 0.046 (-30.1%) | 0.059 / 0.041 (-30.9%) | 0.039 / 0.026 (-34.2%) | 0.020 / 0.013 (-37.7%) |
| CFD | S50 | 50 | U3 | 0.146 / 0.109 (-25.7%) | 0.116 / 0.085 (-26.9%) | 0.081 / 0.058 (-28.7%) | 0.065 / 0.046 (-30.1%) | 0.058 / 0.040 (-30.9%) | 0.039 / 0.026 (-33.5%) | 0.021 / 0.013 (-37.8%) |
| CFD | S50 | 50 | U4 | 0.172 / 0.129 (-25.0%) | 0.136 / 0.100 (-26.2%) | 0.095 / 0.068 (-28.1%) | 0.076 / 0.054 (-29.6%) | 0.068 / 0.048 (-30.2%) | 0.046 / 0.031 (-33.2%) | 0.024 / 0.015 (-37.1%) |
| CFD | S50 | 50 | U5 | 0.162 / 0.121 (-25.3%) | 0.128 / 0.094 (-26.5%) | 0.089 / 0.064 (-28.3%) | 0.072 / 0.051 (-29.7%) | 0.064 / 0.045 (-30.4%) | 0.044 / 0.029 (-33.6%) | 0.023 / 0.014 (-37.1%) |
| CFD | S50 | 50 | U6 | 0.153 / 0.114 (-25.5%) | 0.121 / 0.089 (-26.6%) | 0.084 / 0.060 (-28.6%) | 0.068 / 0.047 (-30.0%) | 0.060 / 0.042 (-30.7%) | 0.041 / 0.027 (-33.9%) | 0.021 / 0.013 (-38.0%) |
| CFD | S50 | 50 | U7 | 0.140 / 0.104 (-26.0%) | 0.111 / 0.081 (-27.2%) | 0.077 / 0.055 (-29.0%) | 0.062 / 0.043 (-30.4%) | 0.056 / 0.038 (-31.2%) | 0.037 / 0.025 (-34.4%) | 0.019 / 0.012 (-38.5%) |
| CFD | S50 | 50 | U8 | 0.142 / 0.105 (-26.0%) | 0.112 / 0.082 (-27.0%) | 0.078 / 0.055 (-28.9%) | 0.063 / 0.044 (-30.4%) | 0.056 / 0.039 (-31.1%) | 0.038 / 0.025 (-34.4%) | 0.019 / 0.012 (-38.2%) |

### kmax (ensemble, p = mean) [g], MCE: hazard anterior (dddf10b) / hazard NBCC 2026-10-15, Mw 6.5 (diferencia relativa)

| siteID | IDg | Hs | IDm | Da/H 0.05% | Da/H 0.1% | Da/H 0.25% | Da/H 0.4% | Da/H 0.5% | Da/H 1% | Da/H 2.5% |
|---|---|---|---|---|---|---|---|---|---|---|
| CFD | S135 | 135 | U1 | 0.097 / 0.052 (-46.7%) | 0.076 / 0.039 (-48.4%) | 0.052 / 0.025 (-51.5%) | 0.041 / 0.019 (-53.2%) | 0.037 / 0.017 (-54.3%) | 0.024 / 0.010 (-57.2%) | 0.014 / 0.006 (-58.1%) |
| CFD | S135 | 135 | U2 | 0.100 / 0.053 (-46.6%) | 0.078 / 0.040 (-48.4%) | 0.053 / 0.026 (-51.5%) | 0.042 / 0.019 (-54.0%) | 0.038 / 0.017 (-55.0%) | 0.025 / 0.011 (-57.8%) | 0.014 / 0.006 (-58.4%) |
| CFD | S135 | 135 | U3 | 0.099 / 0.053 (-46.6%) | 0.078 / 0.040 (-48.4%) | 0.053 / 0.026 (-51.5%) | 0.042 / 0.020 (-53.5%) | 0.037 / 0.017 (-54.5%) | 0.025 / 0.010 (-57.8%) | 0.014 / 0.006 (-58.3%) |
| CFD | S135 | 135 | U4 | 0.106 / 0.056 (-46.7%) | 0.083 / 0.042 (-48.7%) | 0.056 / 0.027 (-52.3%) | 0.045 / 0.020 (-54.6%) | 0.040 / 0.018 (-55.8%) | 0.027 / 0.011 (-59.4%) | 0.014 / 0.006 (-59.5%) |
| CFD | S135 | 135 | U5 | 0.104 / 0.056 (-46.3%) | 0.081 / 0.042 (-48.1%) | 0.055 / 0.027 (-51.5%) | 0.044 / 0.020 (-53.9%) | 0.039 / 0.018 (-55.0%) | 0.026 / 0.011 (-58.2%) | 0.014 / 0.006 (-59.8%) |
| CFD | S135 | 135 | U6 | 0.097 / 0.052 (-46.6%) | 0.076 / 0.039 (-48.5%) | 0.051 / 0.024 (-52.2%) | 0.040 / 0.018 (-54.3%) | 0.036 / 0.016 (-55.3%) | 0.024 / 0.010 (-58.5%) | 0.013 / 0.005 (-58.7%) |
| CFD | S135 | 135 | U7 | 0.097 / 0.052 (-46.9%) | 0.076 / 0.039 (-48.5%) | 0.052 / 0.025 (-51.7%) | 0.041 / 0.019 (-53.8%) | 0.036 / 0.016 (-55.0%) | 0.024 / 0.010 (-57.3%) | 0.013 / 0.006 (-58.4%) |
| CFD | S135 | 135 | U8 | 0.095 / 0.050 (-46.7%) | 0.074 / 0.038 (-48.4%) | 0.050 / 0.024 (-51.6%) | 0.040 / 0.018 (-53.6%) | 0.035 / 0.016 (-54.7%) | 0.023 / 0.010 (-57.8%) | 0.012 / 0.005 (-57.4%) |
| CFD | S27 | 27 | U1 | 0.162 / 0.105 (-35.6%) | 0.134 / 0.084 (-37.8%) | 0.100 / 0.059 (-40.7%) | 0.084 / 0.048 (-42.4%) | 0.077 / 0.043 (-43.5%) | 0.057 / 0.030 (-47.1%) | 0.035 / 0.016 (-53.3%) |
| CFD | S27 | 27 | U2 | 0.171 / 0.112 (-34.6%) | 0.141 / 0.089 (-36.9%) | 0.104 / 0.063 (-39.9%) | 0.087 / 0.051 (-41.7%) | 0.080 / 0.046 (-42.6%) | 0.058 / 0.031 (-46.5%) | 0.036 / 0.017 (-52.8%) |
| CFD | S27 | 27 | U3 | 0.167 / 0.109 (-34.8%) | 0.138 / 0.087 (-37.1%) | 0.102 / 0.061 (-40.1%) | 0.085 / 0.050 (-41.8%) | 0.078 / 0.045 (-42.8%) | 0.057 / 0.031 (-46.3%) | 0.035 / 0.017 (-52.6%) |
| CFD | S27 | 27 | U4 | 0.204 / 0.132 (-35.2%) | 0.167 / 0.105 (-37.4%) | 0.123 / 0.073 (-40.5%) | 0.103 / 0.059 (-42.5%) | 0.094 / 0.053 (-43.5%) | 0.069 / 0.037 (-47.2%) | 0.043 / 0.020 (-53.4%) |
| CFD | S27 | 27 | U5 | 0.186 / 0.122 (-34.6%) | 0.153 / 0.096 (-36.8%) | 0.113 / 0.068 (-40.1%) | 0.094 / 0.055 (-42.0%) | 0.086 / 0.049 (-43.0%) | 0.063 / 0.034 (-46.7%) | 0.039 / 0.018 (-53.1%) |
| CFD | S27 | 27 | U6 | 0.178 / 0.117 (-34.5%) | 0.146 / 0.092 (-36.7%) | 0.108 / 0.065 (-39.9%) | 0.090 / 0.053 (-41.7%) | 0.083 / 0.047 (-42.7%) | 0.060 / 0.032 (-46.7%) | 0.037 / 0.017 (-52.9%) |
| CFD | S27 | 27 | U7 | 0.163 / 0.105 (-35.9%) | 0.135 / 0.084 (-38.0%) | 0.101 / 0.060 (-40.9%) | 0.085 / 0.049 (-42.7%) | 0.078 / 0.044 (-43.6%) | 0.058 / 0.030 (-47.2%) | 0.036 / 0.017 (-53.1%) |
| CFD | S27 | 27 | U8 | 0.155 / 0.099 (-36.1%) | 0.128 / 0.079 (-38.2%) | 0.095 / 0.055 (-41.4%) | 0.079 / 0.045 (-43.1%) | 0.072 / 0.041 (-44.0%) | 0.053 / 0.028 (-47.9%) | 0.033 / 0.015 (-54.0%) |
| CFD | S32 | 32 | U1 | 0.151 / 0.094 (-37.9%) | 0.125 / 0.075 (-39.8%) | 0.093 / 0.053 (-42.7%) | 0.078 / 0.043 (-44.5%) | 0.072 / 0.039 (-45.4%) | 0.053 / 0.027 (-49.0%) | 0.033 / 0.015 (-53.6%) |
| CFD | S32 | 32 | U2 | 0.162 / 0.102 (-36.8%) | 0.133 / 0.081 (-38.9%) | 0.099 / 0.057 (-41.9%) | 0.083 / 0.047 (-43.7%) | 0.076 / 0.042 (-44.6%) | 0.056 / 0.029 (-48.1%) | 0.034 / 0.016 (-54.2%) |
| CFD | S32 | 32 | U3 | 0.154 / 0.096 (-37.7%) | 0.128 / 0.077 (-39.7%) | 0.095 / 0.054 (-42.7%) | 0.079 / 0.044 (-44.5%) | 0.072 / 0.039 (-45.5%) | 0.053 / 0.027 (-48.8%) | 0.033 / 0.015 (-54.6%) |
| CFD | S32 | 32 | U4 | 0.191 / 0.122 (-36.3%) | 0.157 / 0.096 (-38.5%) | 0.115 / 0.067 (-41.7%) | 0.096 / 0.054 (-43.6%) | 0.088 / 0.049 (-44.6%) | 0.064 / 0.033 (-48.4%) | 0.040 / 0.018 (-54.4%) |
| CFD | S32 | 32 | U5 | 0.179 / 0.114 (-36.1%) | 0.147 / 0.091 (-38.3%) | 0.109 / 0.064 (-41.4%) | 0.092 / 0.052 (-43.3%) | 0.084 / 0.047 (-44.2%) | 0.062 / 0.032 (-47.8%) | 0.038 / 0.018 (-53.4%) |
| CFD | S32 | 32 | U6 | 0.167 / 0.106 (-36.3%) | 0.137 / 0.084 (-38.4%) | 0.101 / 0.059 (-41.6%) | 0.084 / 0.048 (-43.5%) | 0.077 / 0.043 (-44.6%) | 0.056 / 0.029 (-48.2%) | 0.035 / 0.016 (-54.2%) |
| CFD | S32 | 32 | U7 | 0.148 / 0.091 (-38.3%) | 0.123 / 0.073 (-40.3%) | 0.092 / 0.052 (-43.2%) | 0.077 / 0.043 (-44.8%) | 0.071 / 0.038 (-45.8%) | 0.052 / 0.027 (-49.1%) | 0.032 / 0.015 (-54.4%) |
| CFD | S32 | 32 | U8 | 0.150 / 0.093 (-38.1%) | 0.124 / 0.074 (-40.1%) | 0.092 / 0.053 (-42.9%) | 0.077 / 0.043 (-44.6%) | 0.071 / 0.039 (-45.5%) | 0.052 / 0.027 (-48.9%) | 0.032 / 0.015 (-54.2%) |
| CFD | S35 | 35 | U1 | 0.149 / 0.092 (-38.0%) | 0.123 / 0.074 (-40.0%) | 0.091 / 0.052 (-43.1%) | 0.077 / 0.042 (-44.8%) | 0.070 / 0.038 (-45.8%) | 0.051 / 0.026 (-49.1%) | 0.032 / 0.014 (-54.4%) |
| CFD | S35 | 35 | U2 | 0.153 / 0.096 (-37.0%) | 0.125 / 0.076 (-39.0%) | 0.092 / 0.053 (-42.2%) | 0.076 / 0.043 (-44.1%) | 0.069 / 0.038 (-45.1%) | 0.050 / 0.026 (-49.1%) | 0.030 / 0.014 (-55.0%) |
| CFD | S35 | 35 | U3 | 0.153 / 0.096 (-37.6%) | 0.126 / 0.076 (-39.6%) | 0.093 / 0.054 (-42.6%) | 0.078 / 0.043 (-44.4%) | 0.071 / 0.039 (-45.5%) | 0.052 / 0.026 (-49.3%) | 0.032 / 0.014 (-54.8%) |
| CFD | S35 | 35 | U4 | 0.188 / 0.120 (-36.4%) | 0.153 / 0.094 (-38.6%) | 0.112 / 0.065 (-41.8%) | 0.093 / 0.053 (-43.8%) | 0.085 / 0.047 (-44.8%) | 0.062 / 0.032 (-48.5%) | 0.038 / 0.017 (-54.8%) |
| CFD | S35 | 35 | U5 | 0.170 / 0.108 (-36.4%) | 0.140 / 0.086 (-38.5%) | 0.103 / 0.060 (-41.7%) | 0.086 / 0.048 (-43.8%) | 0.078 / 0.043 (-44.6%) | 0.057 / 0.029 (-48.5%) | 0.035 / 0.016 (-54.8%) |
| CFD | S35 | 35 | U6 | 0.162 / 0.103 (-36.5%) | 0.133 / 0.081 (-38.7%) | 0.097 / 0.056 (-41.9%) | 0.081 / 0.045 (-43.9%) | 0.073 / 0.040 (-44.9%) | 0.053 / 0.027 (-49.0%) | 0.032 / 0.015 (-54.6%) |
| CFD | S35 | 35 | U7 | 0.147 / 0.090 (-38.4%) | 0.122 / 0.072 (-40.4%) | 0.090 / 0.051 (-43.3%) | 0.076 / 0.042 (-45.0%) | 0.069 / 0.037 (-46.1%) | 0.051 / 0.026 (-49.5%) | 0.032 / 0.014 (-54.4%) |
| CFD | S35 | 35 | U8 | 0.145 / 0.090 (-38.1%) | 0.119 / 0.071 (-40.1%) | 0.088 / 0.050 (-43.2%) | 0.074 / 0.041 (-44.9%) | 0.067 / 0.036 (-45.8%) | 0.049 / 0.025 (-49.6%) | 0.030 / 0.014 (-54.8%) |
| CFD | S50 | 50 | U1 | 0.129 / 0.077 (-40.3%) | 0.105 / 0.061 (-42.2%) | 0.077 / 0.042 (-45.1%) | 0.063 / 0.034 (-47.0%) | 0.058 / 0.030 (-48.0%) | 0.041 / 0.020 (-51.7%) | 0.024 / 0.011 (-56.5%) |
| CFD | S50 | 50 | U2 | 0.131 / 0.077 (-40.9%) | 0.106 / 0.061 (-42.8%) | 0.077 / 0.042 (-45.9%) | 0.063 / 0.033 (-47.7%) | 0.057 / 0.029 (-48.7%) | 0.041 / 0.019 (-52.9%) | 0.024 / 0.010 (-58.0%) |
| CFD | S50 | 50 | U3 | 0.134 / 0.080 (-40.4%) | 0.109 / 0.063 (-42.3%) | 0.080 / 0.044 (-45.2%) | 0.066 / 0.035 (-47.1%) | 0.060 / 0.031 (-48.0%) | 0.043 / 0.021 (-51.9%) | 0.026 / 0.011 (-56.3%) |
| CFD | S50 | 50 | U4 | 0.158 / 0.093 (-41.0%) | 0.129 / 0.073 (-43.1%) | 0.093 / 0.050 (-46.2%) | 0.077 / 0.040 (-48.0%) | 0.070 / 0.036 (-49.1%) | 0.051 / 0.024 (-52.8%) | 0.030 / 0.013 (-58.2%) |
| CFD | S50 | 50 | U5 | 0.136 / 0.080 (-41.1%) | 0.110 / 0.063 (-43.2%) | 0.079 / 0.043 (-46.1%) | 0.065 / 0.034 (-48.1%) | 0.059 / 0.030 (-49.3%) | 0.042 / 0.020 (-53.3%) | 0.024 / 0.010 (-58.6%) |
| CFD | S50 | 50 | U6 | 0.137 / 0.081 (-41.1%) | 0.112 / 0.064 (-42.9%) | 0.081 / 0.044 (-46.0%) | 0.067 / 0.035 (-47.8%) | 0.061 / 0.031 (-49.0%) | 0.044 / 0.021 (-52.5%) | 0.026 / 0.011 (-57.4%) |
| CFD | S50 | 50 | U7 | 0.129 / 0.077 (-40.7%) | 0.106 / 0.061 (-42.6%) | 0.077 / 0.042 (-45.4%) | 0.064 / 0.034 (-47.2%) | 0.058 / 0.030 (-48.1%) | 0.041 / 0.020 (-51.8%) | 0.024 / 0.011 (-56.5%) |
| CFD | S50 | 50 | U8 | 0.131 / 0.078 (-40.4%) | 0.107 / 0.062 (-42.4%) | 0.078 / 0.043 (-45.2%) | 0.065 / 0.034 (-46.9%) | 0.059 / 0.031 (-48.0%) | 0.042 / 0.020 (-51.6%) | 0.025 / 0.011 (-56.5%) |

### Dn (ensemble, p = mean) [cm], TR 10000: hazard anterior (dddf10b) / hazard NBCC 2026-10-15, Mw 6.5 (diferencia relativa), ky seleccionados de la grilla común

| siteID | IDg | IDm | ky 0.010 g | ky 0.021 g | ky 0.045 g | ky 0.096 g | ky 0.205 g | ky 0.437 g | ky 0.800 g |
|---|---|---|---|---|---|---|---|---|---|
| CFD | S135 | U1 | 98023.35 / 28967.04 (-70.4%) | 5478.80 / 1638.61 (-70.1%) | 330.36 / 105.45 (-68.1%) | 27.24 / 9.84 (-63.9%) | 3.06 / 1.06 (-65.4%) | 0.24 / 0.07 (-72.7%) | 0.02 / 0.00 (-77.1%) |
| CFD | S135 | U2 | 204736.94 / 64538.00 (-68.5%) | 11379.04 / 3606.97 (-68.3%) | 658.54 / 215.68 (-67.2%) | 46.41 / 16.58 (-64.3%) | 4.47 / 1.61 (-63.9%) | 0.37 / 0.12 (-67.9%) | 0.03 / 0.01 (-78.7%) |
| CFD | S135 | U3 | 122141.39 / 32466.26 (-73.4%) | 6824.67 / 1840.12 (-73.0%) | 410.52 / 119.86 (-70.8%) | 33.66 / 11.54 (-65.7%) | 3.73 / 1.22 (-67.4%) | 0.26 / 0.06 (-77.4%) | 0.02 / 0.00 (-75.1%) |
| CFD | S135 | U4 | 273603.27 / 76526.23 (-72.0%) | 15191.07 / 4277.47 (-71.8%) | 873.61 / 256.72 (-70.6%) | 60.44 / 20.25 (-66.5%) | 5.76 / 2.04 (-64.5%) | 0.45 / 0.14 (-69.8%) | 0.03 / 0.01 (-63.0%) |
| CFD | S135 | U5 | 170122.13 / 47812.66 (-71.9%) | 9476.98 / 2690.99 (-71.6%) | 558.57 / 168.46 (-69.8%) | 42.70 / 14.90 (-65.1%) | 4.56 / 1.61 (-64.7%) | 0.36 / 0.11 (-70.6%) | 0.03 / 0.01 (-67.7%) |
| CFD | S135 | U6 | 144571.55 / 43258.62 (-70.1%) | 8056.66 / 2433.33 (-69.8%) | 476.02 / 151.67 (-68.1%) | 36.62 / 13.18 (-64.0%) | 3.92 / 1.41 (-64.1%) | 0.32 / 0.10 (-68.2%) | 0.03 / 0.01 (-71.6%) |
| CFD | S135 | U7 | 116753.34 / 32770.16 (-71.9%) | 6516.29 / 1850.53 (-71.6%) | 388.80 / 118.06 (-69.6%) | 31.08 / 10.97 (-64.7%) | 3.46 / 1.21 (-65.1%) | 0.26 / 0.07 (-74.9%) | 0.02 / 0.00 (-77.6%) |
| CFD | S135 | U8 | 185338.23 / 60445.64 (-67.4%) | 10309.25 / 3381.68 (-67.2%) | 599.89 / 203.23 (-66.1%) | 43.00 / 15.68 (-63.5%) | 4.13 / 1.48 (-64.3%) | 0.33 / 0.11 (-67.9%) | 0.03 / 0.01 (-74.5%) |
| CFD | S27 | U1 | 81567.35 / 22637.53 (-72.2%) | 4572.39 / 1297.64 (-71.6%) | 282.51 / 91.00 (-67.8%) | 25.39 / 10.37 (-59.2%) | 3.04 / 1.32 (-56.8%) | 0.23 / 0.12 (-50.2%) | 0.02 / 0.02 (-25.9%) |
| CFD | S27 | U2 | 63294.56 / 16395.98 (-74.1%) | 3566.56 / 955.21 (-73.2%) | 228.77 / 73.23 (-68.0%) | 23.04 / 9.76 (-57.6%) | 3.05 / 1.37 (-55.0%) | 0.25 / 0.13 (-46.2%) | 0.03 / 0.02 (-24.8%) |
| CFD | S27 | U3 | 428482.63 / 134873.58 (-68.5%) | 23747.47 / 7505.30 (-68.4%) | 1346.68 / 437.74 (-67.5%) | 86.59 / 31.27 (-63.9%) | 7.26 / 2.96 (-59.2%) | 0.58 / 0.26 (-55.9%) | 0.05 / 0.03 (-43.9%) |
| CFD | S27 | U4 | 207960.84 / 59005.77 (-71.6%) | 11573.14 / 3317.87 (-71.3%) | 679.24 / 208.46 (-69.3%) | 51.53 / 19.08 (-63.0%) | 5.56 / 2.29 (-58.8%) | 0.49 / 0.22 (-54.6%) | 0.05 / 0.03 (-40.7%) |
| CFD | S27 | U5 | 212020.69 / 65844.77 (-68.9%) | 11793.62 / 3694.27 (-68.7%) | 688.96 / 228.37 (-66.9%) | 50.98 / 19.89 (-61.0%) | 5.31 / 2.32 (-56.3%) | 0.47 / 0.23 (-51.1%) | 0.05 / 0.03 (-38.2%) |
| CFD | S27 | U6 | 96730.05 / 25942.65 (-73.2%) | 5417.19 / 1484.98 (-72.6%) | 333.03 / 103.84 (-68.8%) | 29.67 / 11.97 (-59.7%) | 3.63 / 1.60 (-55.8%) | 0.30 / 0.16 (-48.5%) | 0.03 / 0.02 (-25.7%) |
| CFD | S27 | U7 | 143113.01 / 41613.63 (-70.9%) | 7974.80 / 2347.66 (-70.6%) | 471.69 / 149.92 (-68.2%) | 36.58 / 14.12 (-61.4%) | 3.95 / 1.67 (-57.7%) | 0.32 / 0.14 (-55.7%) | 0.03 / 0.02 (-32.3%) |
| CFD | S27 | U8 | 92520.11 / 26254.36 (-71.6%) | 5176.37 / 1496.44 (-71.1%) | 315.34 / 101.63 (-67.8%) | 27.21 / 11.04 (-59.4%) | 3.27 / 1.43 (-56.3%) | 0.27 / 0.13 (-54.3%) | 0.02 / 0.02 (-29.1%) |
| CFD | S32 | U1 | 140946.54 / 40678.12 (-71.1%) | 7853.15 / 2293.50 (-70.8%) | 463.45 / 145.32 (-68.6%) | 35.35 / 13.21 (-62.6%) | 3.67 / 1.47 (-59.9%) | 0.29 / 0.12 (-59.3%) | 0.02 / 0.01 (-36.8%) |
| CFD | S32 | U2 | 98571.27 / 27271.16 (-72.3%) | 5515.37 / 1555.93 (-71.8%) | 336.36 / 106.33 (-68.4%) | 29.07 / 11.61 (-60.0%) | 3.45 / 1.49 (-56.8%) | 0.28 / 0.14 (-50.0%) | 0.03 / 0.02 (-32.7%) |
| CFD | S32 | U3 | 242375.95 / 74663.70 (-69.2%) | 13461.69 / 4175.42 (-69.0%) | 776.18 / 251.78 (-67.6%) | 54.18 / 20.27 (-62.6%) | 5.30 / 2.22 (-58.1%) | 0.46 / 0.20 (-56.7%) | 0.04 / 0.02 (-50.8%) |
| CFD | S32 | U4 | 213843.76 / 58007.77 (-72.9%) | 11898.12 / 3263.46 (-72.6%) | 697.07 / 205.88 (-70.5%) | 52.67 / 19.25 (-63.5%) | 5.75 / 2.39 (-58.5%) | 0.51 / 0.23 (-56.1%) | 0.05 / 0.03 (-35.1%) |
| CFD | S32 | U5 | 205728.43 / 67534.98 (-67.2%) | 11440.39 / 3783.45 (-66.9%) | 666.20 / 230.93 (-65.3%) | 48.39 / 19.16 (-60.4%) | 4.88 / 2.11 (-56.7%) | 0.43 / 0.20 (-52.8%) | 0.05 / 0.03 (-44.3%) |
| CFD | S32 | U6 | 109831.80 / 31301.11 (-71.5%) | 6134.82 / 1776.76 (-71.0%) | 369.79 / 118.22 (-68.0%) | 30.91 / 12.40 (-59.9%) | 3.65 / 1.62 (-55.7%) | 0.31 / 0.15 (-50.9%) | 0.03 / 0.02 (-31.4%) |
| CFD | S32 | U7 | 144506.17 / 45508.47 (-68.5%) | 8048.32 / 2559.50 (-68.2%) | 473.84 / 159.88 (-66.3%) | 35.96 / 14.12 (-60.7%) | 3.82 / 1.61 (-57.7%) | 0.33 / 0.15 (-55.7%) | 0.03 / 0.02 (-48.5%) |
| CFD | S32 | U8 | 124086.40 / 36403.18 (-70.7%) | 6923.09 / 2058.83 (-70.3%) | 413.15 / 133.41 (-67.7%) | 33.20 / 13.06 (-60.7%) | 3.77 / 1.61 (-57.3%) | 0.32 / 0.14 (-54.8%) | 0.03 / 0.02 (-39.3%) |
| CFD | S35 | U1 | 104297.02 / 29116.04 (-72.1%) | 5830.15 / 1656.43 (-71.6%) | 352.71 / 111.01 (-68.5%) | 29.63 / 11.58 (-60.9%) | 3.40 / 1.40 (-58.7%) | 0.26 / 0.11 (-56.8%) | 0.02 / 0.01 (-30.0%) |
| CFD | S35 | U2 | 165920.81 / 49466.87 (-70.2%) | 9234.92 / 2781.11 (-69.9%) | 541.09 / 173.53 (-67.9%) | 40.14 / 15.29 (-61.9%) | 4.10 / 1.76 (-57.0%) | 0.36 / 0.17 (-53.0%) | 0.03 / 0.02 (-33.7%) |
| CFD | S35 | U3 | 152507.08 / 48280.49 (-68.3%) | 8493.60 / 2715.44 (-68.0%) | 500.18 / 169.91 (-66.0%) | 38.08 / 15.07 (-60.4%) | 4.00 / 1.68 (-57.9%) | 0.31 / 0.15 (-53.4%) | 0.03 / 0.02 (-42.4%) |
| CFD | S35 | U4 | 158782.24 / 44270.25 (-72.1%) | 8853.51 / 2502.48 (-71.7%) | 527.53 / 162.80 (-69.1%) | 42.66 / 16.41 (-61.5%) | 5.00 / 2.13 (-57.3%) | 0.45 / 0.21 (-53.3%) | 0.05 / 0.03 (-37.3%) |
| CFD | S35 | U5 | 133688.42 / 33854.30 (-74.7%) | 7463.10 / 1924.96 (-74.2%) | 447.88 / 129.36 (-71.1%) | 36.78 / 13.79 (-62.5%) | 4.19 / 1.75 (-58.2%) | 0.33 / 0.15 (-52.5%) | 0.03 / 0.02 (-27.1%) |
| CFD | S35 | U6 | 148016.06 / 43521.77 (-70.6%) | 8253.78 / 2458.44 (-70.2%) | 491.02 / 158.52 (-67.7%) | 39.06 / 15.45 (-60.5%) | 4.43 / 1.95 (-56.0%) | 0.40 / 0.19 (-52.3%) | 0.04 / 0.02 (-34.9%) |
| CFD | S35 | U7 | 125475.63 / 37456.67 (-70.1%) | 6998.62 / 2115.79 (-69.8%) | 416.31 / 135.61 (-67.4%) | 32.71 / 12.68 (-61.2%) | 3.50 / 1.45 (-58.6%) | 0.27 / 0.12 (-56.1%) | 0.02 / 0.01 (-41.2%) |
| CFD | S35 | U8 | 86811.89 / 22889.50 (-73.6%) | 4863.85 / 1311.98 (-73.0%) | 299.09 / 91.68 (-69.3%) | 26.54 / 10.36 (-61.0%) | 3.16 / 1.29 (-59.3%) | 0.23 / 0.10 (-58.3%) | 0.02 / 0.01 (-32.6%) |
| CFD | S50 | U1 | 219327.19 / 65800.94 (-70.0%) | 12189.75 / 3685.20 (-69.8%) | 706.05 / 223.87 (-68.3%) | 50.12 / 18.20 (-63.7%) | 4.85 / 1.88 (-61.3%) | 0.38 / 0.14 (-63.8%) | 0.03 / 0.01 (-55.5%) |
| CFD | S50 | U2 | 87530.98 / 23450.50 (-73.2%) | 4902.47 / 1341.35 (-72.6%) | 300.72 / 92.59 (-69.2%) | 26.39 / 10.16 (-61.5%) | 3.10 / 1.23 (-60.4%) | 0.23 / 0.09 (-59.3%) | 0.02 / 0.01 (-36.2%) |
| CFD | S50 | U3 | 372378.29 / 131682.21 (-64.6%) | 20639.52 / 7320.71 (-64.5%) | 1170.08 / 422.92 (-63.9%) | 74.66 / 28.68 (-61.6%) | 6.06 / 2.47 (-59.3%) | 0.49 / 0.21 (-56.6%) | 0.05 / 0.02 (-59.0%) |
| CFD | S50 | U4 | 273070.87 / 78326.40 (-71.3%) | 15167.38 / 4383.56 (-71.1%) | 875.77 / 266.24 (-69.6%) | 61.87 / 22.14 (-64.2%) | 6.20 / 2.52 (-59.4%) | 0.56 / 0.22 (-59.6%) | 0.05 / 0.03 (-41.9%) |
| CFD | S50 | U5 | 337503.43 / 117050.39 (-65.3%) | 18721.48 / 6518.49 (-65.2%) | 1068.42 / 381.42 (-64.3%) | 70.65 / 27.29 (-61.4%) | 6.19 / 2.57 (-58.5%) | 0.52 / 0.23 (-55.9%) | 0.06 / 0.03 (-55.0%) |
| CFD | S50 | U6 | 125108.84 / 32878.52 (-73.7%) | 6982.48 / 1864.93 (-73.3%) | 417.49 / 122.74 (-70.6%) | 33.54 / 12.28 (-63.4%) | 3.67 / 1.46 (-60.4%) | 0.29 / 0.12 (-59.8%) | 0.02 / 0.02 (-32.9%) |
| CFD | S50 | U7 | 83444.16 / 24709.35 (-70.4%) | 4671.43 / 1406.72 (-69.9%) | 285.11 / 94.07 (-67.0%) | 24.40 / 9.54 (-60.9%) | 2.78 / 1.09 (-60.7%) | 0.21 / 0.09 (-59.5%) | 0.02 / 0.01 (-53.8%) |
| CFD | S50 | U8 | 54588.33 / 13623.44 (-75.0%) | 3078.52 / 795.34 (-74.2%) | 197.70 / 60.68 (-69.3%) | 19.65 / 7.65 (-61.1%) | 2.40 / 0.89 (-62.7%) | 0.15 / 0.06 (-62.0%) | 0.01 / 0.01 (-35.3%) |

### Dn (ensemble, p = mean) [cm], MCE: hazard anterior (dddf10b) / hazard NBCC 2026-10-15, Mw 6.5 (diferencia relativa), ky seleccionados de la grilla común

| siteID | IDg | IDm | ky 0.010 g | ky 0.021 g | ky 0.045 g | ky 0.096 g | ky 0.205 g | ky 0.437 g | ky 0.800 g |
|---|---|---|---|---|---|---|---|---|---|
| CFD | S135 | U1 | 905020.99 / 49342.16 (-94.5%) | 50069.43 / 2759.50 (-94.5%) | 2800.27 / 166.22 (-94.1%) | 169.33 / 13.30 (-92.1%) | 13.59 / 1.33 (-90.2%) | 1.28 / 0.07 (-94.3%) | 0.12 / 0.00 (-97.8%) |
| CFD | S135 | U2 | 724022.21 / 37891.12 (-94.8%) | 40069.22 / 2126.59 (-94.7%) | 2247.70 / 131.09 (-94.2%) | 138.87 / 11.29 (-91.9%) | 11.93 / 1.20 (-89.9%) | 1.17 / 0.06 (-94.9%) | 0.10 / 0.00 (-97.9%) |
| CFD | S135 | U3 | 667036.48 / 36350.34 (-94.6%) | 36920.25 / 2041.25 (-94.5%) | 2073.51 / 126.38 (-93.9%) | 129.18 / 11.06 (-91.4%) | 11.36 / 1.19 (-89.5%) | 1.13 / 0.06 (-94.8%) | 0.10 / 0.00 (-97.8%) |
| CFD | S135 | U4 | 845847.08 / 36580.20 (-95.7%) | 46802.12 / 2055.27 (-95.6%) | 2621.40 / 127.59 (-95.1%) | 160.42 / 11.15 (-93.0%) | 13.44 / 1.19 (-91.1%) | 1.34 / 0.06 (-95.2%) | 0.13 / 0.00 (-98.1%) |
| CFD | S135 | U5 | 987047.58 / 46368.82 (-95.3%) | 54602.56 / 2596.14 (-95.2%) | 3051.83 / 157.64 (-94.8%) | 184.26 / 13.11 (-92.9%) | 15.12 / 1.43 (-90.5%) | 1.57 / 0.09 (-94.0%) | 0.18 / 0.00 (-98.3%) |
| CFD | S135 | U6 | 634741.28 / 30760.03 (-95.2%) | 35130.71 / 1729.88 (-95.1%) | 1972.25 / 108.06 (-94.5%) | 122.51 / 9.65 (-92.1%) | 10.72 / 1.06 (-90.1%) | 1.11 / 0.06 (-94.2%) | 0.12 / 0.00 (-98.4%) |
| CFD | S135 | U7 | 917218.31 / 48420.98 (-94.7%) | 50740.45 / 2707.03 (-94.7%) | 2836.15 / 162.78 (-94.3%) | 170.97 / 13.03 (-92.4%) | 13.69 / 1.34 (-90.2%) | 1.32 / 0.08 (-94.1%) | 0.13 / 0.00 (-98.0%) |
| CFD | S135 | U8 | 411338.64 / 23198.57 (-94.4%) | 22787.34 / 1311.64 (-94.2%) | 1289.40 / 84.68 (-93.4%) | 84.16 / 8.22 (-90.2%) | 8.21 / 0.92 (-88.8%) | 0.83 / 0.04 (-95.0%) | 0.07 / 0.00 (-97.9%) |
| CFD | S27 | U1 | 771890.84 / 39283.84 (-94.9%) | 42710.07 / 2204.80 (-94.8%) | 2391.51 / 135.80 (-94.3%) | 145.50 / 11.54 (-92.1%) | 11.78 / 1.23 (-89.6%) | 1.11 / 0.08 (-92.6%) | 0.11 / 0.01 (-94.9%) |
| CFD | S27 | U2 | 311859.87 / 17164.02 (-94.5%) | 17294.25 / 983.41 (-94.3%) | 987.23 / 68.52 (-93.1%) | 67.70 / 7.77 (-88.5%) | 7.20 / 0.96 (-86.6%) | 0.73 / 0.06 (-92.0%) | 0.05 / 0.01 (-87.7%) |
| CFD | S27 | U3 | 229908.54 / 13098.94 (-94.3%) | 12767.10 / 758.90 (-94.1%) | 736.78 / 55.68 (-92.4%) | 52.99 / 6.64 (-87.5%) | 5.84 / 0.78 (-86.7%) | 0.57 / 0.05 (-91.8%) | 0.04 / 0.01 (-87.9%) |
| CFD | S27 | U4 | 2355800.76 / 97411.07 (-95.9%) | 130236.08 / 5426.09 (-95.8%) | 7237.43 / 319.18 (-95.6%) | 419.11 / 24.07 (-94.3%) | 29.67 / 2.58 (-91.3%) | 2.78 / 0.22 (-91.9%) | 0.34 / 0.02 (-93.5%) |
| CFD | S27 | U5 | 747439.49 / 34461.68 (-95.4%) | 41365.14 / 1942.27 (-95.3%) | 2320.75 / 123.41 (-94.7%) | 143.50 / 11.69 (-91.9%) | 12.45 / 1.43 (-88.5%) | 1.32 / 0.12 (-91.2%) | 0.14 / 0.01 (-91.8%) |
| CFD | S27 | U6 | 536369.12 / 28339.15 (-94.7%) | 29703.30 / 1603.64 (-94.6%) | 1675.61 / 104.15 (-93.8%) | 107.08 / 10.25 (-90.4%) | 9.94 / 1.22 (-87.8%) | 1.01 / 0.08 (-91.8%) | 0.09 / 0.01 (-90.3%) |
| CFD | S27 | U7 | 523641.45 / 28834.13 (-94.5%) | 28997.16 / 1628.75 (-94.4%) | 1634.95 / 104.36 (-93.6%) | 103.96 / 9.79 (-90.6%) | 9.35 / 1.07 (-88.6%) | 0.88 / 0.06 (-93.3%) | 0.07 / 0.00 (-93.0%) |
| CFD | S27 | U8 | 578797.25 / 30345.56 (-94.8%) | 32035.33 / 1707.23 (-94.7%) | 1798.62 / 106.85 (-94.1%) | 111.61 / 9.59 (-91.4%) | 9.69 / 1.08 (-88.9%) | 0.98 / 0.07 (-93.0%) | 0.09 / 0.00 (-95.1%) |
| CFD | S32 | U1 | 1416130.52 / 70694.07 (-95.0%) | 78306.35 / 3941.14 (-95.0%) | 4359.93 / 232.32 (-94.7%) | 255.54 / 17.28 (-93.2%) | 18.55 / 1.68 (-90.9%) | 1.67 / 0.11 (-93.3%) | 0.18 / 0.01 (-96.7%) |
| CFD | S32 | U2 | 589521.77 / 31228.29 (-94.7%) | 32640.80 / 1762.92 (-94.6%) | 1838.41 / 112.71 (-93.9%) | 116.38 / 10.62 (-90.9%) | 10.48 / 1.19 (-88.7%) | 1.02 / 0.07 (-92.9%) | 0.10 / 0.01 (-94.2%) |
| CFD | S32 | U3 | 701128.82 / 36167.30 (-94.8%) | 38800.54 / 2031.79 (-94.8%) | 2175.72 / 125.96 (-94.2%) | 133.93 / 11.00 (-91.8%) | 11.39 / 1.22 (-89.3%) | 1.15 / 0.08 (-93.1%) | 0.12 / 0.00 (-96.6%) |
| CFD | S32 | U4 | 3192953.70 / 127431.94 (-96.0%) | 176488.54 / 7084.88 (-96.0%) | 9793.10 / 410.62 (-95.8%) | 560.30 / 28.93 (-94.8%) | 37.41 / 2.77 (-92.6%) | 3.19 / 0.23 (-92.9%) | 0.39 / 0.02 (-95.3%) |
| CFD | S32 | U5 | 1331795.32 / 61604.94 (-95.4%) | 73661.27 / 3447.38 (-95.3%) | 4110.86 / 208.83 (-94.9%) | 245.03 / 17.07 (-93.0%) | 18.80 / 1.80 (-90.4%) | 1.74 / 0.13 (-92.5%) | 0.19 / 0.01 (-94.3%) |
| CFD | S32 | U6 | 725562.12 / 37415.17 (-94.8%) | 40157.22 / 2105.30 (-94.8%) | 2254.25 / 132.17 (-94.1%) | 140.03 / 12.08 (-91.4%) | 12.31 / 1.40 (-88.7%) | 1.26 / 0.09 (-93.1%) | 0.11 / 0.01 (-93.5%) |
| CFD | S32 | U7 | 967013.79 / 49955.95 (-94.8%) | 53490.12 / 2793.36 (-94.8%) | 2987.43 / 168.10 (-94.4%) | 179.14 / 13.48 (-92.5%) | 14.14 / 1.41 (-90.1%) | 1.37 / 0.09 (-93.5%) | 0.14 / 0.00 (-97.3%) |
| CFD | S32 | U8 | 698650.16 / 37255.55 (-94.7%) | 38663.62 / 2092.10 (-94.6%) | 2168.25 / 129.41 (-94.0%) | 133.58 / 11.22 (-91.6%) | 11.31 / 1.21 (-89.3%) | 1.10 / 0.07 (-93.6%) | 0.10 / 0.00 (-96.2%) |
| CFD | S35 | U1 | 1299908.91 / 68019.65 (-94.8%) | 71885.10 / 3793.31 (-94.7%) | 4005.24 / 224.23 (-94.4%) | 236.06 / 16.91 (-92.8%) | 17.58 / 1.68 (-90.5%) | 1.62 / 0.11 (-93.2%) | 0.17 / 0.01 (-96.5%) |
| CFD | S35 | U2 | 583708.06 / 30682.59 (-94.7%) | 32313.44 / 1729.37 (-94.6%) | 1817.07 / 109.29 (-94.0%) | 113.66 / 9.94 (-91.3%) | 9.94 / 1.09 (-89.1%) | 0.97 / 0.06 (-93.4%) | 0.09 / 0.00 (-94.5%) |
| CFD | S35 | U3 | 1070648.95 / 53393.72 (-95.0%) | 59219.02 / 2985.46 (-95.0%) | 3305.37 / 179.52 (-94.6%) | 197.12 / 14.28 (-92.8%) | 15.19 / 1.47 (-90.3%) | 1.44 / 0.10 (-93.1%) | 0.15 / 0.01 (-96.3%) |
| CFD | S35 | U4 | 907284.69 / 40632.28 (-95.5%) | 50207.21 / 2288.73 (-95.4%) | 2815.30 / 145.25 (-94.8%) | 173.89 / 13.85 (-92.0%) | 15.16 / 1.71 (-88.7%) | 1.59 / 0.13 (-91.6%) | 0.16 / 0.01 (-90.9%) |
| CFD | S35 | U5 | 1204519.42 / 59751.10 (-95.0%) | 66624.36 / 3342.39 (-95.0%) | 3719.46 / 201.99 (-94.6%) | 222.59 / 16.54 (-92.6%) | 17.62 / 1.80 (-89.8%) | 1.72 / 0.12 (-93.0%) | 0.17 / 0.01 (-94.2%) |
| CFD | S35 | U6 | 871465.35 / 41250.49 (-95.3%) | 48215.09 / 2315.36 (-95.2%) | 2697.84 / 142.94 (-94.7%) | 163.83 / 12.46 (-92.4%) | 13.59 / 1.43 (-89.4%) | 1.41 / 0.11 (-92.5%) | 0.15 / 0.01 (-95.3%) |
| CFD | S35 | U7 | 987626.87 / 51532.12 (-94.8%) | 54631.93 / 2882.14 (-94.7%) | 3051.99 / 173.73 (-94.3%) | 183.31 / 14.01 (-92.4%) | 14.55 / 1.47 (-89.9%) | 1.43 / 0.10 (-93.2%) | 0.16 / 0.00 (-97.1%) |
| CFD | S35 | U8 | 971379.16 / 54627.37 (-94.4%) | 53731.88 / 3052.24 (-94.3%) | 3000.95 / 182.75 (-93.9%) | 179.89 / 14.38 (-92.0%) | 14.11 / 1.45 (-89.7%) | 1.30 / 0.08 (-93.7%) | 0.12 / 0.01 (-95.6%) |
| CFD | S50 | U1 | 662740.67 / 36921.48 (-94.4%) | 36679.43 / 2073.30 (-94.3%) | 2058.17 / 128.07 (-93.8%) | 127.12 / 10.99 (-91.4%) | 10.77 / 1.15 (-89.3%) | 1.02 / 0.06 (-93.9%) | 0.09 / 0.00 (-96.1%) |
| CFD | S50 | U2 | 785786.33 / 40081.19 (-94.9%) | 43474.46 / 2245.67 (-94.8%) | 2432.71 / 136.98 (-94.4%) | 147.94 / 11.45 (-92.3%) | 12.16 / 1.20 (-90.1%) | 1.16 / 0.07 (-94.3%) | 0.11 / 0.00 (-97.1%) |
| CFD | S50 | U3 | 976384.61 / 50250.91 (-94.9%) | 54011.93 / 2811.51 (-94.8%) | 3018.09 / 169.70 (-94.4%) | 181.43 / 13.66 (-92.5%) | 14.35 / 1.40 (-90.2%) | 1.37 / 0.08 (-93.8%) | 0.14 / 0.00 (-97.2%) |
| CFD | S50 | U4 | 5567190.56 / 232216.71 (-95.8%) | 307661.63 / 12871.88 (-95.8%) | 17040.40 / 729.22 (-95.7%) | 961.16 / 46.22 (-95.2%) | 59.89 / 3.67 (-93.9%) | 4.53 / 0.26 (-94.3%) | 0.53 / 0.02 (-97.0%) |
| CFD | S50 | U5 | 448250.53 / 22110.20 (-95.1%) | 24827.58 / 1253.23 (-95.0%) | 1402.95 / 82.05 (-94.2%) | 90.72 / 8.13 (-91.0%) | 8.60 / 0.91 (-89.5%) | 0.86 / 0.05 (-94.4%) | 0.08 / 0.00 (-96.6%) |
| CFD | S50 | U6 | 841251.71 / 40768.60 (-95.2%) | 46544.81 / 2286.66 (-95.1%) | 2605.35 / 140.48 (-94.6%) | 158.69 / 11.98 (-92.5%) | 13.13 / 1.29 (-90.2%) | 1.30 / 0.08 (-94.0%) | 0.13 / 0.00 (-97.2%) |
| CFD | S50 | U7 | 665557.75 / 34675.98 (-94.8%) | 36832.50 / 1947.51 (-94.7%) | 2065.73 / 120.58 (-94.2%) | 127.45 / 10.56 (-91.7%) | 11.04 / 1.20 (-89.2%) | 1.17 / 0.08 (-93.1%) | 0.13 / 0.00 (-97.9%) |
| CFD | S50 | U8 | 499442.16 / 28022.24 (-94.4%) | 27657.48 / 1581.48 (-94.3%) | 1560.10 / 101.01 (-93.5%) | 100.02 / 9.59 (-90.4%) | 9.42 / 1.09 (-88.5%) | 0.95 / 0.06 (-94.2%) | 0.08 / 0.00 (-96.7%) |

ky grid (g): 0.0100, 0.0116, 0.0135, 0.0157, 0.0183, 0.0213, 0.0248, 0.0288, 0.0335, 0.0390, 0.0453, 0.0527, 0.0613, 0.0713, 0.0829, 0.0965, 0.1122, 0.1305, 0.1518, 0.1765, 0.2053, 0.2388, 0.2778, 0.3231, 0.3758, 0.4371, 0.5084, 0.5913, 0.6878, 0.8000

## Archivos de la tarea

- Estado y entrega: `STATE.md`, `RESULTADOS.md`, `can-trt-hallazgos.md`, `magnitude-map.csv`, `paso5-citas.md`, `newmark-1.7.1-functions.txt`.
- Hashes: `sha-before-20261015.txt` (combinación del 2026-10-14), `sha-M65.txt`, `sha-M55.txt`, `sha-after.txt`, `combine2-log.csv`; los del 2026-10-14 en `logs-m65-20261014-old-hazard/`.
- Logs de hazard: `hazard-pack-*-nbcc-interp-20261014.log`, `hazard-run-{remote,local}-nbcc-interp-20261014.log`, `hazard-abort-sawtooth-20261014.log`, `hazard-extract-760-nbcc-interp-20261015.log`, `hazard-extract-all-nbcc-interp-20261015.log`, `hazard-process-nbcc-interp-20261015.log`, `hazard-process-mce-mcer-nbcc-interp-20261015.log`, `codex-audit-mce-20261015.{log,md}`, `ngr-pull-ts-model-20261015.log`.
- Logs de newmark: `newmark-chain-nbcc-20261015.log`, `newmark-M65-dryrun.log`, `newmark-M65-run.log`, `newmark-M55-dryrun.log`, `newmark-M55-run.log`, `verifyRun-M65.log`, `verifyRun-M55.log`, `combine2.log`, `postCheck2.log`.
- Comparaciones: `nbcc-interp-vs-nrc2024-760.txt`, `nbcc-vs-nrc2024-760.txt` (generación aserrada), `pilot-vs-committed-760.txt`, `compare-tables.md`, `kmax-compare.csv`, `dn-compare.csv`.
- Scripts (`scripts/`): `interpolateNBCCWeights.R`, `dedupCAN.py`, `compareNBCC.py`, `comparePilot.py`, `compareHazard.py`, `gmmTrees.py`, `verifyRun.R`, `combine2.R`, `postCheck2.R`, `compareTables2.R`; generador de este informe `writeDocs.py`.
- Revisión del DOCX de Diana Reyes: `docx-review/` (inventarios A1 y A2, base `base/gmdp.memo.en.md`, mapeo B).
