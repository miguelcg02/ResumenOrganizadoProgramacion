# INNER JOIN

FORMA: Intersección entre dos tablas.

```
Las dos tablas deben presentar una columna en común que es el punto de comparación entre ambas tablas. Cuando se hace el inner join lo que se hace es comparar estas dos columnas y encontrar coincidencias.

Ej:
SELECT * FROM "Empleados" AS E JOIN "Departamentos" as D ON E.DepartamentoID = D.ID;

Estructura: 
SELECT * FROM "tabla_1" AS alias_tabla1 JOIN "tabla_2" AS alias_tabla2 ON alias_tabla1.columnaX = alias_tabla2.columnaY;
```

# LEFT JOIN

FORMA: Toda la tabla Izquierda e interseeción con tabla derecha

```
Se parte de todos los elementos de la tabla1 y se compara con los elementos de la tabla2, es decir, siempre aparecen todas las filas en la tabla 1 como datos, pero no apareceran los datos de la tabla 2 que no tengan coincidencias con la tabla 1.

Ej: 
SELECT * FROM "Empleado" AS E LEFT JOIN "Departamentos" AS D ON E.DepartamentoID = D.ID;

Estructura: 
SELECT * FROM "tabla_1" AS alias_tabla1 LEFT JOIN "tabla_2" AS alias_tabla2 ON alias_tabla1.columnaX = alias_tabla2.columnaY;
```

# RIGHT JOIN

FORMA: Toda la tabla derecha e interseeción con tabla izquierda.

```
Se parte de todos los elementos de la tabla2 y se compara con los elementos de la tabla1, es decir, siempre aparecen todas las filas en la tabla 2 como datos, pero no apareceran los datos de la tabla 1 que no tengan coincidencias con la tabla 2.

Ej: 
SELECT * FROM "Empleado" AS E RIGHT JOIN "Departamentos" AS D ON E.DepartamentoID = D.ID;

Estructura: 
SELECT * FROM "tabla_1" AS alias_tabla1 RIGHT JOIN "tabla_2" AS alias_tabla2 ON alias_tabla1.columnaX = alias_tabla2.columnaY;
```

# FULL JOIN

FORMA: aparece todo

```
Muestra todas las filas de ambas tablas, aunque no siempre tengan coincidencias.

Ej: 
SELECT * FROM "Empleado" AS E FULL JOIN "Departamentos" AS D ON E.DepartamentoID = D.ID;

Estructura: 
SELECT * FROM "tabla_1" AS alias_tabla1 FULL JOIN "tabla_2" AS alias_tabla2 ON alias_tabla1.columnaX = alias_tabla2.columnaY;
```

# Left excluding JOIN

FORMA: Aparece la tabla izquierda, excluyendo la interseecion con la tabla derecha.

```
Muestra las filas de la tabla izquierda que no esten unidas con la tabla derecha

ej: 
SELECT * FROM "Empleados" AS E LEFT JOIN "Departamentos" AS D ON E.DepartamentoID = D.ID where D.ID IS NULL;

Estructura: 
SELECT * FROM "tabla_1" AS alias_tabla1 LEFT JOIN "tabla_2" AS alias_tabla2 ON alias_tabla1.columnaX = alias_tabla2.columnaY WHERE alias_tabla2.columnaY IS NULL;
```

# Right excluding JOIN

FORMA: Aparece la tabla derecha, excluyendo la interseecion con la tabla izquierda.

```
Muestra las filas de la tabla derecha que no esten unidas con la tabla izquierda

ej: 
SELECT * FROM "Empleados" AS E RIGHT JOIN "Departamentos" AS D ON E.DepartamentoID = D.ID where D.ID IS NULL;

Estructura: 
SELECT * FROM "tabla_1" AS alias_tabla1 RIGHT JOIN "tabla_2" AS alias_tabla2 ON alias_tabla1.columnaX = alias_tabla2.columnaY WHERE alias_tabla1.columnaX IS NULL;
```

# Outer excluding JOIN

FORMA: Aparece todo lo que no este unido entre ambas tablas.

```
Muestra todo aquello que no este conectado entre las tablas

ej: 
SELECT * FROM "Empleado" AS E FULL JOIN "Departamentos" AS D ON E.DepartamentoID = D.ID WHERE E.DepartamentoID IS NULL OR D.ID IS NULL;

Estructura: 
SELECT * FROM "tabla_1" AS alias_tabla1 FULL JOIN "tabla_2" AS alias_tabla2 ON alias_tabla1.columnaX = alias_tabla2.columnaY WHERE alias_tabla1.columnaX IS NULL or alias_tabla2.columnaY IS NULL;
```

# Algebra relacional - UNION

Unir tipos de datos que sean similares, las entidades tengan la misma cantidad de campos y en la sección deben estar en el mismo orden.
```
SELECT fullname, address FROM "nombre_schema"."nombre_tabla"
UNION
SELECT fullname, address FROM "nombre_schema"."nombre_tabla"
```

# Algebra relacional - PRODUCTO CARTESIANO

Todos los datos de un conjunto A se relacionan con cada uno de los datos de la tabla B.

```
SELECT * FROM "nombre_schema"."nombre_tabla", "nombre_schema"."nombre_tabla";
```

# Algebra relacional - THETA SELECT

Clausula ON que hacemos en los JOIN de las consultas combinadas.
'Para ser theta join es SELECT FROM ... INNER JOIN ... ON WHERE'
```
SELECT pe.correo, pe.nombre, pe.edad, pe.foto, pf.id_pelicula, pe.id_perfil, peli.restirccion_edad
FROM "Grupo 3"."PERFIL" as pe
INNER JOIN "Grupo 3"."PELICULA-FAVORITA" as pf
ON pe.id_perfil = pf.id_perfil
INNER JOIN "Grupo 3"."PELICULA" as peli
ON pf.id_pelicula = peli.id_pelicula
WHERE peli.restriccion_edad >= 13;
```

# Algebra relacional - PROJECTION

La proyeccion es la relación que se obtiene al eliminar registros duplicados y columnas que no han sido especificadas en la sentencia.

```
SELECT DISTINCT correo FROM "Grupo 3"."PERFIL";
```

# NATURAL JOIN
Puede ser un INNER, LEFT o RIGHT JOIN. Remuve las columnas redundantes y se puede utilizar en entidades que han sido normalizadas previamente.

```
SELECT * FROM cd.facilities NATURAL JOIN cd.bookings;

SELECT * FROM tabla1 JOIN tabla2 USING (atrComun);
```

# UNION

```
SELECT columna1, columna2 FROM tabla1
UNION
SELECT columna1, columna2 FROM tabla2
```

# COUNT
Permite contar un número especifico de registros
```
SELECT COUNT(*)
FROM "Grupo 3".pelicula;
```

# MAX
Trae el mayor
```
SELECT MAX (membercost) FROM cd.facilities;
```

# MIN
Devuelve el valor minimo entre los registros de una tabla
```
SELECT MIN (membercost) FROM cd.facilities;
```

# SUM

```
SELECT SUM (membercost) FROM cd.facilities;
```

# AVG

```
SELECT AVG (membercost) FROM cd.facilities;
```

# ROUND
Permite redondear los resultados
```
SELECT ROUND (membercost,3) FROM cd.facilities; <- Muestra 3 decimales>

ej util:
SELECT ROUND(AVG(precio),2) Avg_precio FROM "Grupo 3 - T2"."PLANES" JOIN "Grupo 3 - T2"."SUSCRIPCIONES" USING (id_plan);
```
