# SOLID

S - Single Responsibility
O - Open/Closed
L - Liskov Substitution
I - Interface Segregation
D - Dependency Inversion

- Los principios SOLID son guías que pueden ser aplicadas en el desarrollo de software para eliminar malos diseños, haciendo que el programador refactorice el código fuente hasta que sea legible y extensible.
- Cuando estos principios se aplican en conjunto es más probable que un desarrollador cree un sistema que sea fácil de mantener y evolucionar con el tiempo.
- Forman parte de la estrategia global del desarrollo ágil de software y desarrollo adaptativo de software.

# ¿Para qué usar SOLID?

- Código fácil de mantener, adaptar y ajustarse a cambios en el alcance.
- Hace posible probar y entender fácilmente el código.
- Extensibilidad con menor esfuerzo.
- Máximo tiempo posible en uso.

# ¿Qué resuelve SOLID?

- Código espagueti, sin estructura o patrón.
- Código duplicado, una alteración necesita ser hecha en N puntos.
- Fragilidad en el código, falla en varios puntos después de algún cambio.

# S - Single Responsibility Principle – SRP (Se relaciona con SoC y MVC)

**Haz una cosa y hazla bien**

* Toda clase debería hacer una (y solo una) cosa. Formulada de otra manera, solo debería haber un único motivo para modificar una clase.

* Una clase o módulo debe tener una sola razón para cambiar, porque debe tener una sola responsabilidad. Además esa clase debe ser la única con esa responsabilidad. Es decir, si tenemos que cambiar una clase, que sea por una única razón.

* Cada capa se concentra en algo particular

# O - Open/Closed Principle ó Principio Abierto Cerrado 

**¿Cómo extender el comportamiento de una clase sin modificar su código fuente?**

- Cerrado para modificación, abierto para adaptación.
- Polimorfismo, herencia


- Abierto a extensión, cerrado a modificación. Utilizar abstracciones en lugar de instancias concretas. Evitar atributos públicos y protegidos. Evitar variables globales.
- El código está mejor diseñado si se puede modificar su comportamiento sin cambiar su código fuente. Debería bastar con añadir código, en lugar de modificarlo. No deberíamos necesitar modificar una clase a no ser que sea para corregir errores.

# L – Liskov Substitution Principle ó Principio de Sustitución de Liskov

- Este principio dice que una clase derivada no debe modificar el comportamiento de la clase base. En otras palabras, las clases hijas no deben infringir las definiciones de las clases padre.
- Si la herencia quedo bien definida, si se sustituye por su padre, este bede seguir pasando sin problema.
- Una clase base debe poder ser sustituida por su clase derivada.

# I – Interface Segregation Principle ó Principio de Segregación de Interfaces

* Los clientes no deberían verse obligados a depender de interfaces que no necesitan. Evita interfaces complejas segregándolas en otras más pequeñas.
* Esto como norma general implica que nuestras interfaces deben ser sencillas y tener pocos métodos. Es preferible tener varias interfaces pequeñas, a tener una interfaz grande. Así no obligamos a los clientes a depender de métodos que no necesitan implementar.

# D – Dependency Inversion Principle ó Principio de Inversión de Dependencia

- La clase A depende de la clase B, si la clase A usa métodos de la clase B
- Si se puede modificar la clase B sin tener que modificar la clase A, hay bajo acoplamiento

- Sin importar la forma, usted debe tener el resultado.
- Las clases de mayor nivel no deberían depender de las clases de menor nivel. Ambas deberían depender de abstracciones. Las abstracciones no deberían depender de detalles. Los detalles deberían depender de abstracciones.
- En una frase, lo que tenemos que hacer es invertir las dependencias.


