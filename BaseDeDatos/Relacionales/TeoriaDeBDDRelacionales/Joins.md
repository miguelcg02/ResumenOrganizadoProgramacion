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