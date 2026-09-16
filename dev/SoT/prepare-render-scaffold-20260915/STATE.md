## Objective

Revisar AR-M2V4D, validar `params.yml`, hidratar el scaffold por la interfaz pública correspondiente y dejar un `qrt.manifest.json` coherente para renderizar después de completar `oq/data` y las corridas científicas.

## Rulings

- No ejecutar cálculos OQT ni inventar datos, escenarios, sitios, idioma, decks o destinos.
- Preservar el trabajo existente no versionado y el commit local que está delante de `origin/main`.
- La hidratación científica pertenece a PSHA; QRT sólo gobierna su scaffold propio, manifest, render y publicación.
- La familia preparada es la selección inglesa pública de 21 productos, con aliases y paths neutrales (`html/book`, `html/toc`, `html/gmdp.*`) y destinos `arm2v4d-*`.
- `params.yml`, `mapper/sites.csv`, `oq/` y las entradas project-owned se conservan; no completar metadatos nulos o ausentes sin datos del propietario.
- La bibliografía compartida correcta es la del scaffold PSHA; las referencias propias de Crawford pertenecen a `_local/bib/references.bib`.

## Evidence and no-repeat

- El estado previo `dev/SoT/prepare-crawford-20260915/STATE.md` está `CANCELLED`, con `Next: none`; esta tarea nueva no reactiva su cálculo CAN/TRT.
- `NEXT-CLOSED {"evidence":"Se leyeron params.yml, .gitignore, oq/data, el sitio, las recetas preparadas, mapper, el dry-run PSHA, el seed instalado y los manifests vigentes. CFD/CAN/coordenadas/mapper coinciden con las decisiones previas; location y client.name son null y faltan metadatos editoriales.","id":"audit-ar-m2v4d-render-inputs-v1"}`
- `NEXT-CLOSED {"evidence":"Se creó qrt.manifest.json V2 con 21 artefactos ingleses y paths neutrales; jq validó 21 alias/paths/slugs/domains únicos, qrt deploy init --dry-run salió 0 y su JSON normalizado coincide exactamente con AR-S2P30 tras sustituir únicamente la base de slug por arm2v4d.","id":"author-ar-m2v4d-manifest-v1"}`
- `NEXT-CLOSED {"evidence":"psha init sin force salió 0 e hidrató los componentes faltantes preservando params.yml, mapper y el manifest. psha pull --force bib salió 0 sobre el único conflicto compartido comprobado. psha status dejó limpios todos los componentes compartidos; sólo mapper/sites.csv y params.yml difieren intencionalmente. psha doctor salió 0. qrt render --manifest qrt.manifest.json --dry-run salió 0 con 21 trabajos y destinos neutrales. No existe html/.","id":"hydrate-ar-m2v4d-psha-v1"}`
- `bib/references.bib` y el scaffold PSHA tienen el mismo SHA-1 `943b888cbac8c24e565d9dd484e6424cedf76d93`; los seis proyectos vigentes usan la misma biblioteca.
- `params.yml` conserva `project_id=AR-M2V4D`, `siteID=CFD`, `ssm=CAN`, latitud 48.794912, longitud -81.340633 y mapper 2000/3.5/7.5. `location` y `client.name` siguen nulos; year, consultant, roles, signature, footer, URL y SRS no están definidos.
- El scaffold no contiene `_chapters/ssm.CAN.md`, `ssm.tectonic.CAN.md`, `ssm.seismicity.CAN.md` ni `ssm.faults.CAN.md`; el master del libro los selecciona desde `params.ssm`. Deben existir antes del render final, además de los resultados OQT y, si se conserva la familia SRS, una selección gmsp.
- Después de instalar la bibliografía PSHA, `qrt status` sale 1 sin reporte por el conflicto conocido con su biblioteca antigua; comparaciones acotadas confirman que `styles/`, `yml/` y `lua/` coinciden con QRT y sólo `bib/references.bib` difiere deliberadamente.

## Effects

- Selector cambiado a este estado nuevo.
- Scaffold PSHA hidratado; `qrt.manifest.json` creado y bibliografía compartida corregida.
- No se modificó `params.yml`, `mapper/sites.csv` ni `oq/`; no se ejecutaron cálculos, renders, inicialización Netlify, deploys ni operaciones Git.

## Delegations

none

## Blocker

none

## Next

none

## Status

DONE
