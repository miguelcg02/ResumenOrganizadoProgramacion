# Arquitectura OLAP

```
Online Analytical Processing se enfoca en grandes cantidades de datos recopilando información de múltiples fuentes y luego guardando esos datos en almacenes. Se requieren grandes recursos computacionales dado la cantidad de datos y se bas en una estructura de columnas.

OLAP Permite hacer reportes, análisis de datos y mineria de datos.

Caracteristicas:
1. Analizar datos en multiples dimensiones
2. Calculos consistentes.
3. Restricciones para proteger los datos.
4. Curva de aprendizaje alta.
```

# Caracteristicas

```
1. Escalabilidad horizontal: facilidad de añadir, eliminar y relaizar operaciones sin afectar el rendimiento (añadir má snodos al un sistema)
2. Escalabilidad vertical: Añadir más capacidad al nodo (RAM,CPU, almacenamiento)
3. Habilidad de distribución: Posibilidad de replicar y distribuir datos entre servidores.
4. Libertad de esquema: Posibilidad de modelar datos como según lo requiera la aplicación, además facilita la integración con lenguajes de programación.
5. Modulo de concurrencia debil: No implementa ACID, las normas para determinar una transacción son dadas por quien diseña el sistema.
```

# Teorema CAP (Consistency Avaliability Partition)
Sistema distribuido que toca sacrificar uno, los tres no pueden estar al mismo tiempo.

```
1. Consistencia: posibilidad que tienen los usuarios de acceder a un mismo dato, independientemente del nodo.
2. Disponibilidad: Garantia de cada solicitud recibe una respuesta.
3. Tolerancia al particionado: El sistema puede seguir en funcionamiento aunque se pierda alguna información.
```

# Tipos de bases de datos del teorema CAP

```
-CP (Consistencia y tolerancia): El sistema se encarga de cerrar el nodo no consistente, en caso de existir errores. Queda indisponible hasta solucionar el error.
-AP (Disponibilidad y tolerancia): Todos los nodos de una partición estarán disponibles, sin embargo al existir un error una pártición puede devolver una versión anterior de los datos. Se resincronizan los datos para reparar inconsicistencia del sistema.
- CA (Consistencia y disponibilidad): No ofrece tolerancias a errores, no se permite la perdida de comunicación entre nodos.
```

# Modelo NoSQL

```
1. Modelo de bases de datos de gráfico: Permite que un nodo (entidad) se relacione con cualquier otro de manera similar a lo que hace un diagrama de red.

2. Modelo multivalor: Permite derivar a un odelo relacional. Permite definir una lista de datos en lugar de un único tipo.

3, Modelo de docuemntos: Define la estructura de un documento en formato JSON.
```



