# Etapas

1. Crear el modelo de dominio: Concentrado en el contexto.
2. Diagrama de clases de diseño: Hacer un refinamiento del modelo de dominio en UML con lo basico
3. Diagrama de clases de implementación: Puede cambiar con respecto al framework, lenguaje, etc.

# Modelo de dominio

- Tiene conceptos y relaciones más significativos del problema
- Muestra el vocabulario del dominio del problema de forma
gráfica y relacionada.
- Se enfoca en conceptos del dominio y no en entidades de
software.
- Los conceptos candidatos se identifican con una lista de
categorías de conceptos o una lista de sustantivos.

* Se hace una categoria de conceptos y los sustentivos para hace asociaciones

* Cada dirección debe tener un textico que lo acompañe

# Diagrama de clases

Esta compuesto por:
- Clases
- Atributos
- Métodos
- Relaciones entre clases

* Camel Case
* Clases en minusculas
* Sin espacios
* Nombre de la clase consiste con lo que es
* Debe aparecer el encapsulamiento

* Relaciones
1. Dependencia: Que hace uso de una caracteristica o función que. No tiene cardinalidad
2. Asociación: Cuando una clase usa otra y no es ninguna de las otras. Tiene cardinalidad
3. Agregación: Cuando una cosa contiene a otra. Ensamblado. Tiene cardinalidad
4. Composición: Una cosa no puede existir sin la otra obligatoriamente. Tiene cardinalidad
5. Herencia: Hay tipos para usar. No tiene cardinalidad.

* Relacion de dependencia

- Una dependencia entre dos clases declara que una clase tiene que conocer acerca de otra clase para utilizar objetos de esa clase. Un objeto A puede usar objetos de una clase B.
- Si se produce un cambio en una de ellas, puede producir cambios en la otra.
- Muestra la relación entre un cliente y un proveedor de un servicio.

* Relación de asociación

- La relación semántica entre dos o más clases que especifican conexiones entre sus instancias.
- Una relación estructural que especifica que los objetos de una cosa están conectados a los objetos de otra cosa.
- La asociación significa que una clase realmente referencia a un objeto u objetos, de la otra clase en forma de un atributo.

* Relación de agregación

-  Una forma especial de asociación que modela un relación todo-parte entre el agregado (el todo) y su partes.
-  Es una relación de tipo “es una parte de”.
-  La multiplicidad se representa como en las otras asociaciones

* Relación de composición

- Es una forma de agregación donde el tiempo de vida del objeto incluido está condicionado por el tiempo de vida del que lo incluye.
- La supresión del objeto agregado conlleva a la supresión de sus partes.

* Herencia / Generalización

- Una relación entre clases donde una clase comparte la estructura y/o el comportamiento de una o más clases.
- Define una jerarquía de abstracciones donde una subclase hereda de una o más superclases.
- Es una relación de tipo “es un tipo/ especie de”



* Visibilidad de atributos y clases

1. Public +  Desde cualquier lado se le puede acceder
2. Protected # Solo accede desde la misma clase o clases heredadas
3. Package ~ Solo se accede desde las clases del paquete
3. Private - Solo se accede desde la misma clase


