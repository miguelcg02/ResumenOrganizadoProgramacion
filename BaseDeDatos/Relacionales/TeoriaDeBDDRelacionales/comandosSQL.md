# Tipos de sentencias

Aqui se espcifica los tipos de comandos que existen en SQL

```
1. Manipulación de datos (DML)
    -SELECT: Recuperar información.
    -INSERT: Agregar información.
    -DELETE: Eliminar información.
    -UPDATE: Actualizar información.
    
2. Definición de datos (DDL)
    -CREATE: Crear objetos.
    -DROP: Eliminar objetos.
    -ALTER: Modificar objetos.

objetos: Bases de datos, tablas y campos.
```

# Crear base de datos

Comando para crear una base de datos en SQL.

```
CREATE DATABASE "nombrebd";
```

# Usar una base de datos

Acceder a una base de datos.

```
USE DATABASE "nombredb";
ó
USE nombredb;

Depende del entorno usado.
```

# rear una tabla

Comando para crear una tabla en SQL.

```
CREATE TABLE nombre_tabla (
    dato tipo_dato(largo_del_dato),
    dato tipo_dato(largo_del_dato),
    dato tipo_dato(largo_del_dato),
    dato tipo_dato(largo_del_dato) <- Ojo, sin la coma 
);
```

# Tipos de datos

Tipos de datos especificos que soporta el lenguaje SQL.

```
Exact numerics:
    -bigint
    -numeric
    -bit
    -smallint
    -decimal
    -smallmoney
    -int
    -tinyint
    -money
Approximate numerics:
    -float
    -real
Date and time:
    -date
    -datetimeoffset
    -datetime2
    -smalldatetime
    -datetime
    -time
Character strings:
    -char
    -varchar
    -text
Unicode character strings:
    -nchar
    -nvarchar
    -ntext
    -Binary strings:
    -binary
varbinary:
    -image
Other data types:
    -cursor
    -rowversion
    -hierarchyid
    -uniqueidentifier
    -sql_variant
    -xml
```

# Llaves primarias

Comando que crea las llaves primarias en SQL, es decir, datos que es único en la tabla.

```
CREATE TABLE "nombre_tabla" (
    dato1 tipo_dato(largo_del_dato) primary key,
    dato2 tipo_dato(largo_del_dato),
    dato3 tipo_dato(largo_del_dato),
    dato4 tipo_dato(largo_del_dato) <- Ojo, sin la coma 
);
```

# Insertar datos a una tabla con INSERT

Comando para agregar datos a una tabla en SQL.

```
INSERT INTO "nombre_tabla" VALUES (
    dato1,
    dato2,
    dato3,
    dato4
);
```

# Obtener datos de una tabla con SELECT

Comando para agregar datos a una tabla en SQL.


```
SELECT campo1,campo2,campo3 FROM "nombre_tabla" WHERE limitantes;

Ejemplo:
SELECT * FROM "Calificaciones";
```

# Actualizar registros de una tabla

Comando para actualizar registros de una tabla en SQL.

```
UPDATE "nombre_tabla" SET campo = valor_nuevo WHRE campo = valor;

Ejemplo:
UPDATE "Calificaciones" SET calificacion = 6.5 WHERE idAlumno = 4;
```
# Eliminar registros de una tabla

Comando para eliminar registros de una tabla en SQL.

```
DELETE FROM "nombre_tabla" WHERE campo = valor;
```

# Comentarios

Comandos para agregar comentarios en SQL.

```
-- Una linea
# Una linea

/*

Bloque de comentarios

*/
```

# Operadores

Tipos de operadores que soporta en lenguaje SQL.

```
Operador igual: SELECT campo1,campo2,campo3 FROM "nombre_tabla" WHERE limitantes = 0;

Operador menor que: SELECT campo1,campo2,campo3 FROM "nombre_tabla" WHERE limitantes < 0

Operador mayor que: SELECT campo1,campo2,campo3 FROM "nombre_tabla" WHERE limitantes > 0

Operador menor o igual que: SELECT campo1,campo2,campo3 FROM "nombre_tabla" WHERE limitantes <= 0

Operador mayor o igual que: SELECT campo1,campo2,campo3 FROM "nombre_tabla" WHERE limitantes >= 0

Operador diferente que: SELECT campo1,campo2,campo3 FROM "nombre_tabla" WHERE limitantes != 0

Operador diferente que: SELECT campo1,campo2,campo3 FROM "nombre_tabla" WHERE limitantes <> 0

```

# Operador LIKE para coincidencias

Comando para buscar coincidencias en una busqueda en SQL.

```
SELECT * FROM Calificaciones WHERE nombre LIKE 'R%'; <--- Inicien con R

SELECT * FROM Calificaciones WHERE nombre LIKE '%R'; <--- Terminen con R

SELECT * FROM Calificaciones WHERE nombre LIKE '%R%'; <--- Se encuentre la R
```

# Valores nulos

Comando para datos nulos en SQL.

```
SELECT * FROM Calificaciones WHERE nombre IS NULL;

SELECT * FROM Calificaciones WHERE nombre IS NOT NULL;
```

# Comando DISTINCT

Comando para no traer valores repetidos en SQL.

```
SELECT DISCTINCT calificaciones From Calificaciones;
```

# Operadores logicos

Operadores logicos que soporta el lenguaje SQL.

```
SELECT * From Calificaciones WHERE nombre = 'Daniela' AND calificacion > 9 ;

SELECT * From Calificaciones WHERE nombre = 'Daniela' OR calificacion > 9 ;
```

# Comando NOT
 
Comando NOT para incluir negación en el lenguaje SQL.

```
SELECT * FROM Calificaciones WHERE NOT nombre = "Daniela";
```

# Comando BETWEEN

Comando BETWEEN para buscar entre dos valores en lenguaje SQL.

```
SELECT * FROM Calificaciones WHERE calificacion BETWEEN 8 AND 10;

```

# Comando ORDER BY

Comando ORDER BY para ordenar de manera descendente o ascendente una busqueda en lenguaje SQL.

```
SELECT nombre_columnas FROM nombre_table ORDER BY nombre_columna ASC

SELECT nombre_columnas FROM nombre_table ORDER BY nombre_columna DESC
```

# Alias (AS)

Comando para agregar un alias AS para simplificar busquedas en lenguaje SQL.

```
SELECT nombre_columna AS alias_columna; 

FROM nombre_tabla AS alias_tabla FROM nombre_tablas alias

SELECT * FROM Calificaciones AS cal WHERE cal.campo;
```

# Elimina todos los datos de Tablas

Comando para elminiar todos los registros de una tabla en lenguaje SQL.

```
TRUNCATE TABLE empleado;
```

# Eliminar una tablas

Comando para elminiar una tabla en lenguaje SQL.

```
DROP TABLE empleado;
```

# Eliminar base de datos

Comando para elminiar una base de datos en lenguaje SQL.

```
DROP DATABASE empresa;

DROP DATABASE IF EXISTS empresa;
```


