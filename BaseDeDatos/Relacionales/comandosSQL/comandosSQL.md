#Tipos de sentencias

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

#Crear base de datos

```
CREATE DATABASE "nombrebd";
```

#Usar una base de datos

```
USE DATABASE "nombredb";
ó
USE nombredb;

Depende del entorno usado.
```

#Crear una tabla

```
CREATE TABLE nombre_tabla (
    dato tipo_dato(largo_del_dato),
    dato tipo_dato(largo_del_dato),
    dato tipo_dato(largo_del_dato),
    dato tipo_dato(largo_del_dato) <- Ojo, sin la coma 
);
```

#Tipos de datos

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

#Llaves primarias

```
CREATE TABLE "nombre_tabla" (
    dato1 tipo_dato(largo_del_dato) primary key,
    dato2 tipo_dato(largo_del_dato),
    dato3 tipo_dato(largo_del_dato),
    dato4 tipo_dato(largo_del_dato) <- Ojo, sin la coma 
);
```

#Insertar datos a una tabla con INSERT

```
INSERT INTO "nombre_tabla" VALUES (
    dato1,
    dato2,
    dato3,
    dato4
);
```
#Obtener datos de una tabla con SELECT

```
SELECT campo1,campo2,campo3 FROM "nombre_tabla" WHERE limitantes;

Ejemplo:
SELECT * FROM "Calificaciones";
```

#Actualizar registros de una tabla

```
UPDATE "nombre_tabla" SET campo = valor_nuevo WHRE campo = valor;

Ejemplo:
UPDATE "Calificaciones" SET calificacion = 6.5 WHERE idAlumno = 4;
```
#Eliminar registros de una tabla

```
DELETE FROM "nombre_tabla" WHERE campo = valor;
```

#Comentarios

```
-- Una linea
# Una linea

/*

Bloque de comentarios

*/
```

#Operadores
```
Operador igual: SELECT campo1,campo2,campo3 FROM "nombre_tabla" WHERE limitantes = 0;

Operador menor que: SELECT campo1,campo2,campo3 FROM "nombre_tabla" WHERE limitantes < 0

Operador mayor que: SELECT campo1,campo2,campo3 FROM "nombre_tabla" WHERE limitantes > 0

Operador menor o igual que: SELECT campo1,campo2,campo3 FROM "nombre_tabla" WHERE limitantes <= 0

Operador mayor o igual que: SELECT campo1,campo2,campo3 FROM "nombre_tabla" WHERE limitantes >= 0

Operador diferente que: SELECT campo1,campo2,campo3 FROM "nombre_tabla" WHERE limitantes != 0

Operador diferente que: SELECT campo1,campo2,campo3 FROM "nombre_tabla" WHERE limitantes <> 0

```

#Operador LIKE para coincidencias

```
SELECT * FROM Calificaciones WHERE nombre LIKE 'R%'; <--- Inicien con R

SELECT * FROM Calificaciones WHERE nombre LIKE '%R'; <--- Terminen con R

SELECT * FROM Calificaciones WHERE nombre LIKE '%R%'; <--- Se encuentre la R
```

#Valores nulos

```
SELECT * FROM Calificaciones WHERE nombre IS NULL;

SELECT * FROM Calificaciones WHERE nombre IS NOT NULL;
```

#Comando DISTINCT, para no traer valores repetidos

```
SELECT DISCTINCT calificaciones From Calificaciones;
```

#Operadores logicos

```
SELECT * From Calificaciones WHERE nombre = 'Daniela' AND calificacion > 9 ;

SELECT * From Calificaciones WHERE nombre = 'Daniela' OR calificacion > 9 ;
```

#Comando NOT

```
SELECT * FROM Calificaciones WHERE NOT nombre = "Daniela";
```

#Comando BETWEEN

```
SELECT * FROM Calificaciones WHERE calificacion BETWEEN 8 AND 10;

```

#Comando ORDER BY

```
SELECT nombre_columnas FROM nombre_table ORDER BY nombre_columna ASC

SELECT nombre_columnas FROM nombre_table ORDER BY nombre_columna DESC
```

#Alias (AS)

```
SELECT nombre_columna AS alias_columna; 

FROM nombre_tabla AS alias_tabla FROM nombre_tablas alias

SELECT * FROM Calificaciones AS cal WHERE cal.campo;
```

#Elimina todos los datos de Tablas

```
TRUNCATE TABLE empleado;
```

#Eliminar una tablas

```
DROP TABLE empleado;
```

#Eliminar base de datos

```
DROP DATABASE empresa;

DROP DATABASE IF EXISTS empresa;
```


