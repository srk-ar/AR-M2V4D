# Crawford AR-M2V4D — plan de preparación

Actualizado el 2026-09-14 con las correcciones del propietario. Esta versión sustituye el plan anterior, rechazado por excesivo. Alcance: preparar el proyecto y sus insumos; ejecutar los cálculos después.

## Decisiones del propietario

- Sitio: CFD. La clave tiene tres letras; no usar crawford ni crawfords como siteID.
- TR: 100, 200, 500, 1000, 2000, 2500, 5000 y 10000 años.
- Vs30: 180, 270, 360, 560, 760, 800, 1250 y 1500 m/s.
- Vref: 760 m/s. Revisar Vs30 adicionales más adelante.
- SSM: CAN actual de /Users/averrik/kashimaDB/openquake/ssm/CAN.
- GMM: generales por TRT de /Users/averrik/kashimaDB/openquake/gmm/TRT, como los otros proyectos.
- Mapper: implementación común; hidratar las propiedades Crawford de params.yml.
- Crear S1 provisional para poder calcular MCE. El propietario autoriza inventar ese escenario: no exigir un rationale previo ni esperar la desagregación.
- Usar los insumos legacy; no leer el informe legacy.
- Verificar la correspondencia TRT de CAN dentro de la preparación. Evitar convertirla en otra auditoría extensa.

## Orden de trabajo

1. Inicializar oq/sites/CFD.json con el CLI público oqt y completar las coordenadas Crawford y los ocho Vs30. El handoff incluye el contenido ya preparado.
2. Preparar el scaffold vigente y params.yml siguiendo un proyecto activo de referencia. Hidratar los datos de Crawford y conectar el mapper común. Mantener CFD coherente en todos los consumidores.
3. Crear las recetas classical y disaggregation con oqt --init y adaptar el modelo CAN y los GMM generales. Resolver modelID desde la convención vigente al crear los archivos.
4. Seguir ssmLT_CAN.xml hasta los archivos de fuentes que incluye y comprobar que sus TRT enlacen con los selectores GMM. La inspección anterior encontró ASC, SCC, SIF, SIS30 y SIS55; revisar los archivos vigentes al utilizarlos, sin repetir una auditoría general.
5. Crear oq/calcs/scenario/CFD/S1.json mediante oqt --init scenario S1 --site CFD. Declarar parámetros y geometría del escenario provisional y preparar la configuración que permitirá producir MCE.
6. Preparar oq/data/data.R y las recetas adicionales requeridas por los productos comunes, con TR, Vs30 y Vref acordados. Conectar los consumidores del scaffold a las tablas del process actual.
7. Revisar el conjunto concreto de insumos y dependencias antes de pack/run. El MCE numérico requiere los cálculos y el procesamiento posteriores; en esta fase queda preparada su definición.

## Después de preparar los insumos

- Seleccionar el entorno OpenQuake por la configuración pública vigente.
- Planificar la matriz: ocho classical, una disaggregation y ocho scenario S1, si las recetas finales conservan este alcance.
- Ejecutar oqt pack, comprobar los paquetes y después oqt run y extract.
- Ejecutar los pasos de oqt process necesarios para los productos probabilistas, MCE y los productos de diseño configurados. SSM/GMM pueden procesarse cuando estén listos sus propios insumos.
- Verificar las tablas generadas y su integración en los productos actuales del proyecto.

No se ha ejecutado esta secuencia. Los resultados legacy pertenecen a los modelos anteriores NRC/GEM; no representan CAN actual con los GMM generales elegidos. Tampoco se demostró una incompatibilidad del parser actual: no crear un conversor sin observar una necesidad concreta.

## Referencias

Proyectos: AR-S2L1W, AR-SAC00, AR-SABP0, AR-SACU0, AR-S2P30 y AR-S2C1R, bajo /Users/averrik/Cloud/github/projects/.

Usar los skills instalados y las interfaces públicas: /Users/averrik/.agents/skills/oqt/SKILL.md; para el scaffold, /Users/averrik/.agents/skills/qrt/SKILL.md. No modificar las herramientas para realizar este trabajo.
