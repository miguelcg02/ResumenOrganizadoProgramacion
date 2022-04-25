# Base de datos relacionales

```
Una base de datos relacional es un tipo de base de datos que almacena y proporciona acceso a puntos de datos relacionados entre sí. Las bases de datos relacionales se basan en el modelo relacional, una forma intuitiva y directa de representar datos en tablas.
```

# Composición

```
Se crean relaciones por medio de identificadores con FK y PK.
```

# PK
```
Dato que se crea en la tabla 1 como identificador unico.
```

# FK
```
Dato que se crea en la tabla 2 como identificador de la tabla 1.
```
# Schemas

```
Modelos de base de datos, este es el archivo como tal.
```

# Tipos de sentencias

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

# ACID

```
1. Atomicidad: Si cuando una operación consiste en una serie de pasos, 
de los que o bien se ejecutan todos o ninguno, es decir, las transacciones 
son completas.

2. Consistencia: (Integridad). Es la propiedad que asegura que sólo se empieza 
aquello que se puede acabar. Por lo tanto se ejecutan aquellas operaciones que 
no van a romper las reglas y directrices de Integridad de la base de datos. La 
propiedad de consistencia sostiene que cualquier transacción llevará a la base 
de datos desde un estado válido a otro también válido. "La Integridad de la Base 
de Datos nos permite asegurar que los datos son exactos y consistentes, es decir 
que estén siempre intactos, sean siempre los esperados y que de ninguna manera 
cambian ni se deformen. De esta manera podemos garantizar que la información que 
se presenta al usuario será siempre la misma."

3. Aislamiento: Esta propiedad asegura que una operación no puede afectar a otras. 
Esto asegura que la realización de dos transacciones sobre la misma información 
sean independientes y no generen ningún tipo de error. Esta propiedad define cómo 
y cuándo los cambios producidos por una operación se hacen visibles para las demás 
operaciones concurrentes. El aislamiento puede alcanzarse en distintos niveles, 
siendo el parámetro esencial a la hora de seleccionar SGBDs.

4. Durabilidad: (Persistencia). Esta propiedad asegura que una vez realizada la 
operación, esta persistirá y no se podrá deshacer aunque falle el sistema y que de 
esta forma los datos sobrevivan de alguna manera.
```
