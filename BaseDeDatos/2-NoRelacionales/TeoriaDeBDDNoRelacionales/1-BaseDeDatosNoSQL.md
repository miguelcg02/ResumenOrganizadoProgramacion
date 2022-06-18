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

# Tipos

```
1. Bases de datos bajo modelos Key - value
2. Bases de datos orientadas a documentos
3. Bases de datos columnares
4. Bases de datos orientadas a grafos
```

# Lambda 
```
Servicio de aws que hace como si fuera un backend, pero no siempre esta arriba (solo funciona si se activa)
```

# Cuando escoger este tipo de BdD

```
Cuando es necesario leer más datos que escribir (De lo contrario es mejor una SQL)
```

# Modelado der datos NoSql

```
1. Modelo relacional entre docs:
 -Modelo uno a uno con documentos embebidos
 -Modelo uno a mucho con documentos embebidos
 -Modelo uno a muchos con documentos referenciados.

2. Modelo de estructura en árbol
 -Modleo de estructura de árbol con referencia de los padres
 -Modelo de estructura de árbol con referencia de los hijos.
 -Modelo de estructura de árbol con rutas materializadas
 -Modelo de estructura de árbol con conjuntos anidados.
```

# 1. Modelo uno a uno con documentos embebidos

```
Para lograr uno a uno a nivel de documentos, se incrusta los datos que estén conectados entre si para reducir la cantidad de operaciones de lectura.

ej: 
{
    _id: "Joe",
    name: "Joe Mama",
    address: {
        street: "123 alv",
        city: "Medayork",
        state: "ANT",
        zip: "12345"
    }
}
```
# 2. Modelos uno a muchos con documentos embebidos

```
Cinsiste en incrustar varios documentos que estan relacionados en uno solo, lo que facilitaría y reduciria las consultas

ej:
{
    "_id": "Joe",
    "name": "Joe Mama",
    "adresses": [
                {
                    street: "123 alv",
                    city: "Medayork",
                    state: "ANT",
                    zip: "12345"
                },
                {
                    street: "135 Boston",
                    city: "Bogotown",
                    state: "CUM",
                    zip: "12342"
                }
            ]
}
```

# Patrón de subconjunti

```
El modelo por documentos embebidos tiene problemas y es que puede generar documentos de gran tamaño, ocasionalmente que el acceso a la información sea complejo y requiera de mucha lógica para obtener alguna cantidad de información.

El patrón de subconjunto indica que s epuede limitar la cantidad de información, que tengo de uno a muchos solo con lo más relevante o lo que voy a ver en pantalla en primera instancia, luego a nivel detallado, se iría al documento de tener el resto de información complementaria.

ej:

{
    name: "O'Reilley",
    founded: 1980,
    location: "CA",
    books: [12345,67890,...]
}

{
    _id: 12345,
    title: "A",
    author: ["Kristina"],
    published_date: ISODate("2010-09-24"),
    pages: 216,
    language: "English"
}

{
    _id: 67890,
    title: "B",
    author: ["Miguel"],
    published_date: ISODate("2011-05-20"),
    pages: 66,
    language: "English"
}
```