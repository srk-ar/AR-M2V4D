# GMPETable: causa y procedimiento de resolución

Revisión del 2026-09-17 a partir de la consulta del propietario. S1 es definitivo por su instrucción explícita; los textos CAN no están disponibles.

## Causa comprobada

No existe `oq/calcs/gmpe`, ni `oq/data/GMPETable.Rds`. La ejecución pública de diagnóstico, desde el workspace `oq`, fue:

```text
oqt --process --steps gmpe --dry-run
```

Terminó exit 1 con `GMPE calc directory not found: calcs/gmpe`. No se ejecutaron scripts R de producción.

`gmpe` es una etapa adicional: no integra el orden predeterminado `aep,mce,uhs,mcer,ts,dn,kmax,deq`. Los resultados classical/scenario no publican automáticamente GMPETable. ScenarioGMPETable sí está presente, con 513 filas de S1/SCC: describe el escenario particular y no la grilla Mw/Repi/dep para las figuras generales.

## Insumos disponibles y contrato faltante

El contrato público es la sección 3.1 de `docs/SCHEMA-CALC.md` del commit OQT `7bd7faf`, consultada mediante Git. Se contrastó con los consumidores instalados `runGMPE.R` y `gmpe_grid.py`, sin ejecutarlos directamente. La distribución instalada es `7bd7faf-dirty`; la sección GMPE coincide con esos consumidores en los campos y productos aquí descritos. No se aplicaron otras secciones históricas del documento al flujo actual.

Cada JSON de `oq/calcs/gmpe/<modelID>.json` debe tener una sola TRT y una identidad distinta para que la tabla global conserve cada familia. El contrato admite la grilla lineal `grid.Mw` (min/max/step), grilla logarítmica `grid.Repi` (min/max/n), profundidad `dep`, referencia `vs30` y mecanismo `rupture` (rake/strike/dip/msr, aspectRatio opcional). Los IMT pueden declararse; el contrato documenta los mismos del classical como valor predeterminado.

| Elemento | Estado |
|---|---|
| Directorio GMM | Disponible: `~/kashimaDB/openquake/gmm/TRT` |
| Árboles del cálculo classical | ASC, SCC, SIF, SIS30, SIS55: los cinco XML existen |
| Referencia de roca del proyecto | Vref=760 m/s, declarada en data.R |
| Mecanismo S1/SCC | Definido: profundidad 10 km, rake=0, strike=0, dip=90, WC1994; no define por sí solo las otras TRT ni sus grillas |
| Specs GMPE | Ausentes |
| Grillas Mw/Repi de comparación | No definidas por el contrato GMPE del proyecto, que no existe |
| Profundidades/mecanismos de las restantes comparaciones | Pendientes de una definición vigente |

Los valores del ejemplo del esquema no se adoptaron como parámetros de Crawford. Las plantillas y los proyectos vecinos no autorizan esas decisiones científicas.

## Resolución

1. Definir o aportar las especificaciones GMPE vigentes: alcance de TRT, grillas Mw/Repi y profundidades/mecanismos. Conservar las identidades de los árboles empleados por el proyecto.
2. Escribir y verificar los JSON bajo `oq/calcs/gmpe`, con identidades distintas por TRT.
3. Ejecutar desde `oq` la etapa pública `oqt --process --steps gmpe`. Usa hazardlib directamente; no necesita una nueva corrida classical/scenario ni un ciclo pack/run/extract.
4. Verificar `oq/data/GMPETable.Rds`: columnas, cobertura, claves únicas, unidades, orden de fractiles, medias y ramas/ensemble. La herramienta puede omitir celdas Mw/dep cuando la ruptura no cabe a esa profundidad; cada omisión debe reconciliarse con la grilla solicitada.
5. Renderizar los consumidores afectados después de aceptar la tabla. Hay una diferencia editorial a resolver: el master SHA recorre las TRT presentes, mientras el apéndice del libro enumera ASC/SCC/SIF/SIS y el cálculo actual usa SIS30/SIS55. No se debe renombrar estas últimas a SIS sin decidir cómo presentarlas.

No se generó GMPETable: falta el contrato científico de la grilla. Se corrigió únicamente la descripción S1 y se actualizó el informe de auditoría para incorporar las dos aclaraciones del propietario.
