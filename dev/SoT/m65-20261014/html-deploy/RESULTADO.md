# Publicación HTML — 2026-10-15

Los 21 HTML quedaron publicados y comprobados en producción. `ngr deploy --manifest manifest.json --prod` terminó con exit 0 en una sola ejecución, sin reintentos, sin crear sitios ni cambiar dominios. El propietario validó «Producción en los sitios actuales» para los bindings de `.netlify/sites.env`.

## Recibos y comprobación remota

| Alias | UUID del sitio | Deploy ID | URL | Comprobación |
|---|---|---|---|---|
| toc | d24121f9-7e2d-4bb0-9096-16710cec54f5 | 6ad0ff7d1ad3f401d1ea6200 | [Producción](https://arm2v4d-toc.srk.ar) | HTTP 200; SHA-256 idéntico |
| report | e814d560-334d-49f8-a77f-02dc745cebb0 | 6ad0ff841b42f8106c8adc5c | [Producción](https://arm2v4d-report.srk.ar) | HTTP 200; contenido idéntico¹ |
| gmdp | 30da135a-2799-418a-890a-26668fd183b1 | 6ad0ff9041d9508b11d83da8 | [Producción](https://arm2v4d-gmdp.srk.ar) | HTTP 200; SHA-256 idéntico |
| ts | 9527253e-0757-4192-8439-0d69fdb10811 | 6ad0ff9819a2fa8258ececad | [Producción](https://arm2v4d-ts.srk.ar) | HTTP 200; SHA-256 idéntico |
| dn | 044c1657-d68e-4c73-b327-b8fd6225a1b7 | 6ad0ffa1d76809e13978eb5d | [Producción](https://arm2v4d-dn.srk.ar) | HTTP 200; SHA-256 idéntico |
| kmax | ca6ba0ef-badc-48b8-95fb-79e77d78d1d6 | 6ad0ffa9a175fad9d40280a5 | [Producción](https://arm2v4d-kmax.srk.ar) | HTTP 200; SHA-256 idéntico |
| kh | 85b7341a-5cb3-4ca4-94da-0a8626f6a022 | 6ad0ffb15e3239ac008c5b02 | [Producción](https://arm2v4d-kh.srk.ar) | HTTP 200; SHA-256 idéntico |
| sdc | 60050607-4bae-457d-ad21-84dc79944096 | 6ad0ffbb4e5400d7270280bf | [Producción](https://arm2v4d-sdc.srk.ar) | HTTP 200; SHA-256 idéntico |
| sha | d3731f52-4c07-4a73-aa77-1a6bd0878184 | 6ad0ffc3d3d98a403efcfdd0 | [Producción](https://arm2v4d-sha.srk.ar) | HTTP 200; SHA-256 idéntico |
| srs | 0c47f5d5-6e33-4a29-9bf6-b5302ed8de07 | 6ad0ffcc19a05b1e80b92047 | [Producción](https://arm2v4d-srs.srk.ar) | HTTP 200; SHA-256 idéntico |
| at | 32b7450d-cc32-4c9b-bf0a-f02f5672e558 | 6ad0ffd3a09388e876cdb51a | [Producción](https://arm2v4d-at.srk.ar) | HTTP 200; SHA-256 idéntico |
| vt | 40b19a07-7273-438b-9c52-deb9189cef05 | 6ad0ffdebbb8f5d29823466a | [Producción](https://arm2v4d-vt.srk.ar) | HTTP 200; SHA-256 idéntico |
| dt | 820bd640-d5ad-4c57-84ed-ef2be17afa3a | 6ad0ffe73946c2ed912345f4 | [Producción](https://arm2v4d-dt.srk.ar) | HTTP 200; SHA-256 idéntico |
| ai | c6c0f402-6b45-4b26-86cd-250404af304f | 6ad0fff2e8f09d79f6c2d233 | [Producción](https://arm2v4d-ai.srk.ar) | HTTP 200; SHA-256 idéntico |
| cav | 4e79be92-89dd-47b5-8c1a-3b842df8b7cf | 6ad0ffff0b43d21a2e8adcc7 | [Producción](https://arm2v4d-cav.srk.ar) | HTTP 200; SHA-256 idéntico |
| cav5 | beb155d2-af2d-4171-a9d3-1dc9c6be32cf | 6ad10009c5c66f76db5523be | [Producción](https://arm2v4d-cav5.srk.ar) | HTTP 200; SHA-256 idéntico |
| psa | 8c5fcb7e-aadc-4e2d-abd3-d9eef79f2b63 | 6ad10016475525f71aea6203 | [Producción](https://arm2v4d-psa.srk.ar) | HTTP 200; SHA-256 idéntico |
| psv | 9c2a070b-fbbd-4696-ac43-65066825ed24 | 6ad1001d9bedb1d510397d77 | [Producción](https://arm2v4d-psv.srk.ar) | HTTP 200; SHA-256 idéntico |
| sd | f0438784-7011-4f53-898d-241b921cb79f | 6ad10026b6465f5fb6a69bc4 | [Producción](https://arm2v4d-sd.srk.ar) | HTTP 200; SHA-256 idéntico |
| its | cec90739-2916-4338-8985-22a9452adcf8 | 6ad1002d09e22bb5050280a8 | [Producción](https://arm2v4d-its.srk.ar) | HTTP 200; SHA-256 idéntico |
| ipsa | 1037333b-3ca3-4ca5-81da-ca94747973ed | 6ad1005ec7c98bb42385bb6d | [Producción](https://arm2v4d-ipsa.srk.ar) | HTTP 200; SHA-256 idéntico |

¹ En report, Netlify reescribió atributos de los enlaces HTML. El índice, `_book/dn.html` y `_book/executive.html` coinciden exactamente con los locales al omitir sólo los atributos de apertura de enlaces (`diff` exit 0). Todos los demás índices coinciden byte por byte mediante SHA-256. Las 23 lecturas remotas —21 índices y dos capítulos— respondieron HTTP 200. También respondieron HTTP 200 las rutas efectivamente enlazadas `/_book/dn` y `/_book/executive`.

Recibos estructurados: `deploy-receipts.json`, con alias, ruta, UUID, modo, deploy ID, URL de producción y URL única. Verificación y hashes locales/remotos: `remote-verification.json`. Log original: `deploy-prod-20261015.log`; recibo terminal: `deploy-prod-20261015.exit` (0).

## Generación publicada

Los masters y bindings de los 21 artefactos se leyeron antes de operar. `inventory.json` y `inventory-ready.json` conservan la identidad de cada artefacto. El dry-run del deploy terminó con exit 0.

Se regeneró únicamente `report` mediante `ngr render --manifest manifest.json --only report`, master `_master/book.en.qmd`, perfil `book`. Terminó con exit 0 y `[render manifest] complete`. Los otros 20 HTML reutilizan las corridas ya aceptadas.

El capítulo publicado `https://arm2v4d-report.srk.ar/_book/dn.html` contiene Mw5.5 para TR100–2500 y Mw6.5 para TR5000/10000/MCE; la ecuación de kh incluye el factor 100. El contenido coincide con los sources generados mediante R. No se editaron sources, datos científicos ni Word durante esta misión.

SHA-256 local de dn.html: `57438978c185e0cfe7d5a2b581e3bde9e031d0ef58b4c83273715c9d724240ca`; executive.html: `9215bf13972eb9bf003e10121ea28ecef38eb6258c4981dc1defe87f3987974e`.

La comprobación interactiva local verificó TOC, avance de portada a contenido, curvas y tablas de kmax, cambio a Ensemble y TR10.000, y navegación de dn a Executive Summary. Es una QA representativa; no se auditó cada curva individual. El servidor local y la pestaña temporal quedaron cerrados.

## Integridad y cierre

`manifest.json` conserva SHA-256 `925d42d13bac7c7f22bafb5f30fe0ec60d19960ea6b34372ae5ac5eee0edcfee`; `.netlify/sites.env` conserva `5aaa44d56656e565164346821265213b296912f5b02a43e960e93871285f9e77`. No hubo operaciones Git.

Se cargó y leyó maintenance para cerrar la delegación. La carpeta y todos sus recibos se conservan para que el coordinador haga join; no se eliminó nada. `dev/ARCHITECTURE.md` no existe. El selector sigue en `dev/SoT/m65-20261014/STATE.md`; `.gitignore` no contiene patrones para dev/. Los snapshots remotos permanecen en `/private/tmp/m2v4d-deploy-verify.O4Oi0Z`.
