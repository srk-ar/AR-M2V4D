# Handoff — Crawford, sitio CFD

## Encargo

El propietario abre una nueva tarea en /Users/averrik/github/projects/AR-M2V4D y pidió copiar el plan a dev/. Continuar desde este checkout con PLAN-CRAWFORD.md. No crear otra tarea ni retomar el selector del checkout de la herramienta oqt.

La última instrucción de implementación pendiente es inicializar el sitio CFD. El alcance general es preparar params.yml, los JSON de OpenQuake, el mapper y S1/MCE, y después pack/run/extract/process. El propietario rechazó el exceso de planificación y las preguntas que reabrían decisiones ya tomadas.

## Estado observado el 2026-09-14

- Checkout real: /Users/averrik/Cloud/github/projects/AR-M2V4D.
- Rama main; origin git@github.com:kanameishi/AR-M2V4D.git.
- Antes de copiar estos documentos, git status --short estaba vacío; dev/ y oq/sites/CFD.json no existían.
- El agente anterior no completó la inicialización en el proyecto. Existe un JSON preparado en /private/tmp/crawford-CFD-20260914/CFD.json.
- No hay modelos de cálculo ni paquetes producidos por esta tarea en Crawford. No se ejecutaron pack/run/extract/process.
- La sesión anterior no podía escribir en Crawford con su configuración de carpetas. Las llamadas escaladas no devolvieron resultado; no hubo evidencia de aprobación ni rechazo. No presentar esto como un defecto de oqt.
- Los borradores antiguos de modelos fuera del proyecto se retiraron por mezclar valores legacy con el estándar actual. No recuperarlos.

## Primer paso concreto

Leer el skill oqt instalado, verificar la ayuda actual de --init y observar si CFD.json ya existe antes de escribir. El comando público, desde la raíz del proyecto, es:

    oqt --init site CFD

Completar su contenido con:

```json
{
  "siteID": "CFD",
  "lon": -81.340633,
  "lat": 48.794912,
  "vs30": [180, 270, 360, 560, 760, 800, 1250, 1500],
  "siteParamsModel": "hybrid",
  "siteParams": {
    "reference_vs30_type": "inferred"
  }
}
```

Procedencia: coordenadas leídas de nrc/job.ini dentro de legacy/oq/run/nrc/nrc_760.zip; conjunto Vs30 seleccionado por el propietario; hybrid/inferred según la configuración común leída en AR-SAC00/oq/sites/CN.json. CFD fue una corrección explícita del propietario.

Verificar el archivo realmente creado. El JSON del sitio no es una receta de cálculo ni prueba que el proyecto esté terminado.

## Entradas y antecedentes útiles

- Legacy: /Users/averrik/Cloud/github/projects/AR-M2V4D/legacy/oq.
- Árbol CAN: /Users/averrik/kashimaDB/openquake/ssm/CAN/model/ssmLT_CAN.xml.
- GMM generales: /Users/averrik/kashimaDB/openquake/gmm/TRT.
- Referencia práctica: /Users/averrik/Cloud/github/projects/AR-SAC00.
- OQT observado: /usr/local/bin/oqt, versión 4a8330c, build 4a8330c-dirty de 2026-09-14T21:53:49Z. Comprobar la instalación vigente al retomar.

El análisis XML anterior encontró ASC, SCC, SIF, SIS30 y SIS55 y selectores generales coincidentes; fue una lectura estática, no una prueba de ejecución. Registro anterior, sólo si hace falta una referencia concreta: /Users/averrik/Cloud/github/tools/oqt/dev/SoT/crawford-can-trt-preflight-20260914/TRT-AUDIT.json.

No asumir que CAN ya fue usado por los proyectos activos: el propietario indicó SAM, ARB y XAF. Resolver la correspondencia TRT al preparar los JSON, sin ampliar el trabajo a otra auditoría.

No volver a preguntar por TR, Vs30, Vref, GMM generales o el permiso para inventar S1: están resueltos en el plan. Los datos propios de Crawford que aún no estén definidos se obtienen de los insumos y contratos, sin inventarlos.
