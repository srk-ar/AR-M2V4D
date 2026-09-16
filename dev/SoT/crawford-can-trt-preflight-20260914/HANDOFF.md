# Handoff — Crawford AR-M2V4D

## Encargo del propietario

Continuar la preparación de Crawford con el flujo habitual de los proyectos actuales: scaffold, params.yml, JSON de OpenQuake, mapper, S1/MCE y configuración de process. Después de tener listos los insumos vendrán oqt pack, run, extract y process.

El propietario pidió este handoff porque el agente anterior convirtió una preparación habitual en un plan excesivo. El plan anterior fue rechazado por overkill; no trasladar sus controles añadidos como requisitos del propietario. No seguir ampliando la auditoría: usar oqt correctamente y preparar el proyecto.

## Decisiones ya tomadas

- Adoptar los parámetros comunes de los proyectos activos:
  - TR: 100, 200, 500, 1000, 2000, 2500, 5000, 10000 años.
  - Vs30: 180, 270, 360, 560, 760, 800, 1250, 1500 m/s.
  - Vref: 760 m/s.
- Vs30 adicionales: más adelante. No volver a preguntar por esta selección.
- SSM: CAN actual de /Users/averrik/kashimaDB/openquake/ssm/CAN.
- GMM: generales por TRT, como los otros proyectos; no las semillas NBCC.
- Mapper: usar la implementación común e hidratar las propiedades del sitio Crawford en params.yml. No diseñar otro mapper.
- S1: el propietario autorizó inventar un escenario provisional para poder calcular un MCE. No hay rationale previo en oq/scenarios/; no exigirlo ni esperar la desagregación para preparar S1.
- Antes de pack/run faltan los insumos del proyecto. No adelantar cálculos.
- CAN no se había usado en los proyectos activos SAM/ARB/XAF. Comprobar de manera práctica que sus árboles/fuentes tienen TRT correctos y que enlazan con los GMM de oqt. El propietario rechazó convertir esto en una auditoría extensa.
- No leer el informe DOCX/legacy: lo requerido son los insumos y el proyecto actual.

## Rutas y herramientas

Proyecto:
- /Users/averrik/Cloud/github/projects/AR-M2V4D
- Rama main; origin git@github.com:kanameishi/AR-M2V4D.git.
- /Users/averrik/github es un enlace al árbol Cloud/github.
- Legacy: /Users/averrik/Cloud/github/projects/AR-M2V4D/legacy/oq.

Referencias de estructura y configuración:
- /Users/averrik/Cloud/github/projects/AR-S2L1W
- /Users/averrik/Cloud/github/projects/AR-SAC00
- /Users/averrik/Cloud/github/projects/AR-SABP0
- /Users/averrik/Cloud/github/projects/AR-SACU0
- /Users/averrik/Cloud/github/projects/AR-S2P30
- /Users/averrik/Cloud/github/projects/AR-S2C1R

Leer el skill instalado /Users/averrik/.agents/skills/oqt/SKILL.md y usar el CLI público. Observado al preparar este handoff: /usr/local/bin/oqt, versión4a8330c, build4a8330c-dirty de2026-09-14T21:53:49Z. Hubo cambios concurrentes: la instalación actual es más nueva que la que se leyó al comienzo de esta conversación.

El schema público usa sites/<siteID>.json y calcs/classical, calcs/disaggregation, calcs/scenario/<siteID>. Las recetas scenario se crean con oqt --init scenario <ID> --site <siteID>. Comprobar las ayudas actuales para cada operación.

## Estado real al entregar

- Se comprobó ahora que Crawford tiene legacy/oq, pero no tiene oq/, params.yml ni mapper/.
- git status --short de Crawford no emitió cambios en la comprobación actual. No reutilizar el diagnóstico anterior de archivos eliminados: esa situación cambió fuera de esta tarea.
- Este agente no construyó el proyecto ni ejecutó pack/run/extract/process/render.
- Los tres JSON preliminares creados fuera de Crawford se retiraron porque mezclaban parámetros legacy con el estándar actual.
- Quedaron documentos de análisis en el checkout de la herramienta oqt; no son implementaciones ni decisiones aprobadas.
- No hay comandos de cálculo lanzados por esta tarea que haya que reanudar.
- El selector /Users/averrik/Cloud/github/tools/oqt/dev/SoT/ACTIVE.md pertenece ahora a otra tarea. No retomarlo como estado de Crawford ni sobrescribirlo por este handoff. Trabajar con la identidad y checkout de Crawford.

## Pistas útiles, sin convertirlas en nuevos requisitos

- Coordenadas leídas en los jobs legacy de Crawford: lon=-81.340633, lat=48.794912.
- El árbol actual es /Users/averrik/kashimaDB/openquake/ssm/CAN/model/ssmLT_CAN.xml.
- La lectura XML previa encontró ASC, SCC, SIF, SIS30 y SIS55; los selectores de las semillas generales homónimas coincidían. No se ensayó la integración completa con oqt. Revisar los archivos vigentes al usarlos.
- GMM: /Users/averrik/kashimaDB/openquake/gmm/TRT.
- Los resultados legacy pertenecen a modelos NRC/GEM anteriores. No son resultados de CAN actual con los GMM generales elegidos.
- No se demostró que el parser actual rechace los CSV antiguos. No afirmar esa incompatibilidad ni implementar un conversor sin necesidad.
- Identidades M2V4D y crawford fueron propuestas por el agente; aún no hay archivos del proyecto que las establezcan.

## Siguiente acción

Leer la configuración vigente de un proyecto de referencia y completar la lista concreta de insumos faltantes de Crawford. Preparar la base común y params.yml, enlazar CAN/GMM, completar los JSON incluido S1 y data.R, y comprobar la correspondencia TRT dentro de ese trabajo. Presentar la preparación concreta antes de pasar a pack/run.

El propietario no quiere otro plan largo ni nuevas preguntas sobre decisiones ya tomadas.
