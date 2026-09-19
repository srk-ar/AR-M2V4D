# Preparación para renderizar AR-M2V4D

Auditoría local del 2026-09-17. Objetivo: revisar el repositorio, los skills y las interfaces QRT/SPT/PSHA, y determinar qué insumos faltan. No se ejecutaron cálculos ni renders nuevos.

## Dictamen

**No está listo para renderizar íntegramente el conjunto declarado.** El plan de QRT es válido, pero faltan la configuración completa y los productos de Newmark que consumen cinco artefactos. También hay cuestiones científicas y editoriales que un render exitoso no resolvería.

El [manifiesto](/Users/averrik/Cloud/github/projects/AR-M2V4D/qrt.manifest.json) declara 21 artefactos HTML: un libro y veinte presentaciones/hubs. Se observaron 16 archivos finales `index.html` no vacíos; faltan `report`, `ts`, `dn`, `kmax` y `kh`. La existencia de los otros 16 no constituye una nueva aceptación visual ni científica.

| Artefactos | Observación actual |
|---|---|
| toc, gmdp | HTML presentes; son hubs de navegación. |
| sdc, sha | HTML presentes y tablas científicas principales legibles. |
| srs, at, vt, dt, ai, cav, cav5, psa, psv, sd, its, ipsa | HTML presentes; los cinco productos de señales cubren los mismos 30 registros. El ajuste espectral requiere revisión. |
| ts | Falta `ShearTable.Rds`; configuración geométrica/material incompleta. |
| dn | Faltan `DnTable.Rds`, `DnDraws.Rds` y `PGATable.csv`. |
| kmax, kh | Falta `kmaxTable.Rds` y sus dependencias anteriores. |
| report | El master incluye Ts y Newmark; el resumen ejecutivo también los consume. No puede completarse con los productos actuales. |

El alcance auditado es el del manifiesto actual. No declara entregables DOCX, PDF, versiones españolas ni un trabajo independiente para regenerar el mapa.

## Bloqueo de render: configuración y productos Newmark

[data.R](/Users/averrik/Cloud/github/projects/AR-M2V4D/oq/data/data.R:1) contiene únicamente ID M2V4D, sitio CFD, ocho TR, ocho Vs30, Vref=760 y las alturas `c(135, 50, 32, 27, 35)`, con NTS derivado.

Se evaluó ese archivo en un entorno R separado y se compararon sus objetos con los consumidores instalados:

| Etapa pública OQT | Parámetros ausentes | Producto pendiente |
|---|---|---|
| `oqt --process --steps ts` | `lo.min`, `lo.max`, `s.min`, `s.max`, `uscs`, `IDm` | `oq/data/ShearTable.Rds` |
| `oqt --process --steps dn` | `Mw.gmdp`, `NS`, `subduction`, `Dn_weights` | `oq/data/DnTable.Rds` y productos por sitio |
| `oqt --process --steps kmax` | `Da.gmdp` | `oq/data/kmaxTable.Rds` |

Lecturas que sostienen el contrato: [runTs.R](/usr/local/libexec/oqt/runTs.R:49), [runDn.R](/usr/local/libexec/oqt/runDn.R:616), [dnModels.R](/usr/local/libexec/oqt/dnModels.R:28), [runKmax.R](/usr/local/libexec/oqt/runKmax.R:378). Se leyeron como evidencia suplementaria; no se invocaron helpers internos.

`Dn_weights` selecciona modelos con valores 0/1 en la versión instalada. No debe completarse como una ponderación arbitraria. Los nombres y valores faltantes deben proceder del contrato vigente del proyecto.

Tampoco existen `oq/uhs/M2V4D/CFD/DnDraws.Rds` ni `oq/uhs/M2V4D/CFD/PGATable.csv`. No son insumos que deban entregarse manualmente: los produce la etapa dn.

El informe exige que la lista de materiales sea coherente con la leyenda de zonas: [_tbl/IDm.qmd](/Users/averrik/Cloud/github/projects/AR-M2V4D/_tbl/IDm.qmd:1) contiene ocho etiquetas por defecto y [scripts/tbl/IDm.R](/Users/averrik/Cloud/github/projects/AR-M2V4D/scripts/tbl/IDm.R:1) comprueba la cardinalidad. Esto no autoriza seleccionar ocho materiales por inferencia.

El orden pendiente es completar el contrato, producir y verificar ts, luego dn, luego kmax, y después renderizar los cinco artefactos pendientes. No se deben copiar valores históricos o de otro proyecto sin identidad científica vigente.

## Insumos calculados que sí están disponibles

Se leyeron todos los RDS globales presentes; no se infirió su contenido por el nombre.

| Tabla | Filas |
|---|---:|
| AEPSTable | 71.527 |
| AEPTable | 9.176 |
| ASCETable | 768 |
| DEQTable | 49.152 |
| MCEBranchTable | 1.536 |
| MCETable | 9.472 |
| RMwTable | 60.800 |
| ScenarioGMPETable | 513 |
| ScenarioTable | 1 |
| SSMTable | 202 |
| UHSRock | 256 |
| UHSTable | 49.152 |

UHSTable identifica M2V4D/CFD, las ramas M2V4D, M2V4D.oq y M2V4D.site, los ocho Vs30 del contrato y TR=100, 200, 500, 1000, 2000, 2500, 5000 y 10000. El UHSRock por sitio cubre esos mismos ocho TR y roca a 760 m/s. MCETable identifica CFD y las ramas S1, S1.oq, S1.site y MCE.

Estas observaciones prueban legibilidad y cobertura resumida; no son una revalidación completa de todas las curvas ni de su procedencia histórica. No se consultó el servidor OpenQuake ni se afirmó que el cálculo histórico de desagregación continúe en su base actual.

Los archivos `mapper/byEvent/epicenters.csv` e `index.html` existen; el mapa HTML también está copiado en `html/sha/mapper/byEvent/index.html`.

Los directorios de modelos y registros bajo `~/kashimaDB` existen en esta máquina, pero están fuera del repositorio. Se comprobaron el árbol raíz CAN y las cinco semillas GMM declaradas. `gmmLT_GMM.xml` es el archivo ensamblado por OQT al empaquetar; su ausencia en la raíz del directorio de semillas no es un insumo faltante.

## SRS: archivos completos, compatibilidad por revisar

Los contratos [select.json](/Users/averrik/Cloud/github/projects/AR-M2V4D/gmsp/select.json) y [match.json](/Users/averrik/Cloud/github/projects/AR-M2V4D/gmsp/match.json) declaran población F25, selección CFD y blanco MDE M2V4D/CFD, Vs30=800, componente H1, amortiguamiento 5%, banda 0,04–5 s y envolvente p50–p95.

Comprobaciones actuales:

- Selección: 30 registros y 30 eventos.
- Manifest: 30 entradas, todas `done`.
- `metadata/runMatch.json` es idéntico al contrato actual.
- TSW: 111.950 filas; IMW: 90; PSW: 960; ITS: 1.375.784; IPSA: 9.600.
- Cada uno de esos cinco productos contiene exactamente los mismos 30 RecordID de la selección.
- Las 32 ordenadas del blanco persistido coinciden con UHSTable para TR=10000, tras convertir g a mm/s² mediante 9806,65. No hay períodos omitidos ni duplicados; residuo relativo máximo observado: 3,34e-15.

La convergencia no equivale a compatibilidad aprobada:

- [stage.csv](/Users/averrik/Cloud/github/projects/AR-M2V4D/gmsp/match/CFD/match/stage.csv:2) informa `status=solved`, `pgaRatio=0.594364`, `insideFraction=0.280208` y `maxViolation=0.921433`.
- [compatibility.csv](/Users/averrik/Cloud/github/projects/AR-M2V4D/gmsp/match/CFD/match/compatibility.csv:2) informa 27 PGA por debajo de la envolvente y 3 dentro.
- Al comparar [mean.csv](/Users/averrik/Cloud/github/projects/AR-M2V4D/gmsp/match/CFD/match/mean.csv) con [target.csv](/Users/averrik/Cloud/github/projects/AR-M2V4D/gmsp/match/CFD/match/target.csv), la media guardada queda dentro de la envolvente en 15 de 32 ordenadas, por debajo en 15 y por encima en 2.
- La relación media/blanco guardada es 0,594 en PGA, 0,355 a 0,05 s, 0,334 a 2 s y 0,172 a 5 s.
- La media aritmética recalculada de PSW/H1 difiere de mean.csv hasta 0,265% relativo; no se certificó el origen de esa diferencia.

No se inventó un umbral contractual de aceptación. Los datos permiten mostrar las galerías, pero estas discrepancias requieren revisión científica antes de calificar la suite como compatible o de entregar los resultados. El contrato no debe modificarse ni repetirse el match automáticamente.

## Cuestiones científicas y editoriales

1. **Escenario S1 definitivo.** Corrección directa posterior del propietario, 2026-09-17: «S1 es definitivo». Esa instrucción cierra la cuestión de provisionalidad. Se actualizó únicamente la descripción del [JSON del escenario](/Users/averrik/Cloud/github/projects/AR-M2V4D/oq/calcs/scenario/CFD/S1.json:4); sus valores numéricos y resultados no cambiaron. La definición independiente de `Mw.gmdp` no se infiere de esta corrección.

2. **Fuentes sísmicas de Canadá incompletas como contenido.** [params.yml](/Users/averrik/Cloud/github/projects/AR-M2V4D/params.yml:6) selecciona CAN. [_book/ssm.qmd](/Users/averrik/Cloud/github/projects/AR-M2V4D/_book/ssm.qmd) solicita cuatro archivos ausentes:
   - `_chapters/ssm.tectonic.CAN.md`
   - `_chapters/ssm.seismicity.CAN.md`
   - `_chapters/ssm.faults.CAN.md`
   - `_chapters/ssm.CAN.md`

   El propietario confirmó posteriormente, el 2026-09-17, que no dispone de esos textos. El [master inglés](/Users/averrik/Cloud/github/projects/AR-M2V4D/_master/book.en.qmd:6) actualmente excluye ese contenedor. Por eso no bloquea el plan vigente, pero el libro no contiene ese capítulo. La existencia de SSMTable o del XML del modelo no sustituye estos textos.

3. **Antecedentes del encargo vacíos.** [_local/intro.background.md](/Users/averrik/Cloud/github/projects/AR-M2V4D/_local/intro.background.md:1) contiene únicamente el comentario de plantilla. El helper local omite la sección cuando no hay texto. [_local/bib/references.bib](/Users/averrik/Cloud/github/projects/AR-M2V4D/_local/bib/references.bib:1) también contiene sólo comentarios, sin entradas propias del proyecto; la bibliografía compartida sigue declarada.

4. **Comparaciones GMM opcionales ausentes.** No existe GMPETable.Rds. El [apéndice GMM](/Users/averrik/Cloud/github/projects/AR-M2V4D/_book/gmm.appendix.qmd) y el master SHA condicionan sus figuras a esa tabla, de modo que se omiten. ScenarioGMPETable sí existe y cubre las figuras del escenario; no sustituye la grilla general GMPETable. El diagnóstico posterior confirmó que falta `oq/calcs/gmpe`: el dry-run público se detiene por esa ausencia. Los cinco árboles GMM declarados existen. Véase la [resolución del diagnóstico](/Users/averrik/Cloud/github/projects/AR-M2V4D/dev/SoT/gmpe-readiness-20260917/gmpe-diagnosis.md).

## Herramientas, skills y verificaciones

- Se leyeron los skills instalados QRT, SPT y OQT y las referencias pertinentes. Los consumidores R se revisaron bajo code/r. No se encontró un skill PSHA en el catálogo aprobado ni en las raíces instaladas inspeccionadas.
- `qrt --help` y `qrt render --help`: QRT compone/renderiza el proyecto; no calcula los insumos científicos.
- `qrt render --manifest qrt.manifest.json --dry-run`: exit 0, 21 trabajos. Es validación del plan, no ejecución de Quarto/R.
- Recorrido estático desde esos masters: se leyeron 200 QMD/Markdown alcanzables por referencias literales; no se detectaron archivos literales faltantes. Esto no resuelve rutas construidas dinámicamente ni acredita todos los recursos/citas.
- `psha --help`: PSHA es un scaffolder de contenido; el render SRS pertenece a QRT.
- `psha version`: build `1bb0769f-dirty`, 2026-09-15T17:33:30Z.
- `psha doctor`: exit 0, claves requeridas presentes.
- `psha status`: exit 0; diferencias locales en 8 masters, 2 scripts, 1 archivo mapper y params.yml. No se atribuyeron esas diferencias a defectos ni se reemplazó el scaffold.
- `qrt status`: exit 1 sin stdout/stderr. El diagnóstico de sincronización quedó inconcluso; no invalida el plan de render observado.
- `spt --version`: 0.1.2; revisadas ayudas general/match. Su manifiesto de instalación no incluye los documentos de esquema que menciona la ayuda. No se construyeron nuevos contratos.
- `oqt --version`: `7bd7faf-dirty`; revisada `oqt --process --help`.
- Quarto 1.9.35 y R 4.6.1. Los 17 paquetes consultados están disponibles, incluidos los requeridos por setup.R, here, jsonlite, gmsp, osqp y Matrix. newmark 1.6.0 expone `sampleSaCorr(zTrunc)`.

No se realizó una nueva ejecución integral ni QA visual de los 16 HTML existentes. El estado Git al entrar ya tenía cambios en el master, params.yml y manifiesto, y árboles gmsp/html sin seguimiento; se preservaron. Esta auditoría añade documentación y repara el estado de continuidad, sin modificar ciencia, scaffold ni resultados.
