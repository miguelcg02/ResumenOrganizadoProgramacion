# Que es UML?

* Lenguaje grafico sirve para:
- Visualizar
- Especificar
- Construir
- Documentar

# Que no es UML?

- No es un lenguaje de prgramación
- No es metodo de desarrollo
- No es de un proceso en especifico

# Tipos de diagramas de UML

1. Estructurales -> Estatico: Es fija

Como se organiza el sistema

- Clases
- Estructura
- Componentes
- Despliegue
- Objetos
- Paquetes

2. Comportamiento -> Dinamico: Es cambiante

Representan lo que va a pasar en el sistema

- Actividad
- Itnteracción:
    * Secuencia
    * Comunicación
    * Global de interacción
    * Tiempos
- Casos de uso
- Máquina de estado

# Casos de uso (Que están en comportamiento)

- Include: Primero se debe hacer
- Extend: Se hacen luego de un include y son opcionales

* Ejemplo en un include (obligatorio):

A --- include ---> B

Primero se hace B y luego A


* Ejemplo en el extend (Opcional):

A <---- Extend ---- B

Primero se hace A y luego B

- Para los roles, la flecha apunta a sus intenciones  

# Descripcion textual de un caso de uso

* Id
* Nombre
* Auto
* Fecha
* Descripción
* Precondiciones: Condiciones que deben cumplirse para poder ejecutar el caso de uso. Lo que se espera antes de.
* Flujo normal: Lo que pase en condiciones ideales.
* Flujo alternativo: Lo que puede que falle.
* Poscondiciones; Que se espera que pase después de.

# ¿Cómo crear los casos de uso?

1. Definar los actores.
2. Definir los casos de uso.
3. Relaicone los casos de uso con los actores.

# Nombrar casos de uso

- Acción (verbo) + Objetivo o sustantivo + Complemento

# Tips para hacer los casos de uso

1. Cada actor y caso de uso debe tener un nombre único
2. El nombre de un actor debe representar su rol
3. El nombre de un caso de uso debe indicar una acción y debe ser conciso
4. Evite el cruce de lineas
5. Evite tener demasiados casos de uso en el mismo diagrama
6. Narrre el flujo de eventos usando voz activida, en tiempo presente y desde la voz del actor
7. Cada caso de uso debe repr

# Tarea bonus

1. Consultar cómo transformar los casos de uso a código. Inidica la fuente de información.
2. Realiza un diagrama de casos de uso.
3. Realiza su implementación en código siguiendo las reglas de transformación del punto 1.


ej:

https://app.diagrams.net/#G1xvhtBHiPzZTp9N9xwcsncTiGVkGoj1Aw