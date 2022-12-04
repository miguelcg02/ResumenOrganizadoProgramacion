# Dos formas ed construir un diseño

- Una es hacerlo tan simple que sea obvio que no hay deficiencias
- La otra es hacerlo tan complicado que no haya deficiencias obvias

* escribir un fragmento inteligente de código que funcione es una cosa; diseñar algo que dé apoyo a largo plazo a una empresa es otra muy diferente.

# Caracteristicasde un buen diseño

1. Debe tener una arquitectura que:
• Se haya creado empleando estilos o patrones arquitectónicos reconocibles.
• Tenga componentes con buenas características de diseño. No escoger paint jajajajaja
• Se implemente en forma evolutiva, de modo que facilite las pruebas.

2. Debe ser modular, es decir, el software debe estar dividido de manera lógica en elementos o subsistemas. Separalo bien en partes

3. Debe contener distintas representaciones de datos, arquitectura, interfaces y componentes. Muchos enfoques, varios diagramas.

4. Debe conducir a estructuras de datos apropiadas para las clases que se van a implementar y que surjan de patrones reconocibles de datos. 

5. Debe llevar a componentes que tengan características funcionales independientes.

6. Debe conducir a interfaces que reduzcan la complejidad de las conexiones entre los componentes y el ambiente externo. Se tienen que hacer más faciles las cosas que dificiles.

7. Debe obtenerse con el empleo de un método repetible motivado por la información obtenida durante el análisis de los requisitos del software.

8. Debe representarse con una notación que comunique con eficacia su significado.

# Principios de diseño

- Principio: guía de comportamiento, pistas para tomar una decisión, base para la construcción de algo, estrategia para diseñar y desarrollar código eficiente, eficaz, limpio, flexible, mantenible y escalable.

- DRY: Don't repeat yourself
    * Es uno de los principios más importantes. 
    * Evitar al máximo la repetición de código
    * Si estás repitiendo código, extrae ese código en una función para encapsularlo. Si tienes que hacer un cambio, este estará localizado en un solo punto, y no esparcido por todo el código fuente.
    * Usa funciones, módulos, bibliotecas, clases, herencia ...
    * Hace el código más mantenible.
    * Reduce el tamaño del código.
    * Ahorra tiempo.

- KISS: Keep it simple, stupid
    * El diseño de un programa debe ser sencillo
    * Cuánto más sencillo sea, mejor
    * Hay que evitar la complejidad, pero sobre todo la complejidad innecesaria.
    * El sistema debería tener tan pocos componentes como sea posible.
    * La documentación debe ser la información estrictamente necesaria.
    * Los proyectos son más mantenibles.
    * Hay menos documentación.
    * El debugging es más rápido.

- SoC: Separation of Concerns
    * Separa los asuntos.
    * Los asuntos son los diferentes aspectos de la funcionalidad de nuestra aplicación.
    * Por ejemplo la capa de negocio, la capa de datos etc.
    * Un buen ejemplo de separación es el patrón MVC.

- YAGNI: You Ain’t Gonna Need It
    * Muchas veces, para evitar problemas posteriores, los programadores tendemos a desarrollar funcionalidades que no estamos seguros de necesitar. 
    * Simplemente lo hacemos “por si acaso”. 
    * YAGNI indica que no debemos implementar algo si no estamos seguros de necesitarlo. Así ahorramos tiempo y esfuerzo.

- Boy Scout
    * Como programadores, debemos hacer como los Boy Scout, que dejan el campo más limpio que cuándo llegaron.
    * El código siempre puede mejorar.
    * Si podemos, debemos refactorizar el código para dejarlo todavía más limpio y simple que antes.

- La Ley de Demeter
    * Una unidad sólo debe tener conocimiento limitado de otras unidades, y sólo debe conocer aquellas que están relacionadas.
    * La una unidad sólo debe hablar con amigos y nunca con extraños.
    * La unidad sólo debe hablar con amigos inmediatos.
    * Tenemos que tratar de evitar utilizar métodos de un objeto que han sido devueltos por otro método.
    * Por ejemplo no usar:
    clienteActual.ObtenerDireccion.calle.CambiarNombreDeCalle.
    * Recuerda, no hay que hablar con extraños

- El principio de Hollywood
    * Basado en la típica respuesta que se les da a los actores que hacen una prueba para una película: “No nos llame, nosotros le llamaremos”. Este principio está relacionado con el principio de inversión de dependencias de SOLID.
    * Un ejemplo del principio de Hollywood es la inversión de control (IoC), que hace que una clase obtenga las referencias a objetos que necesita para funcionar, a través de una entidad externa.

- La navaja de ockham:
    * La Navaja de Occam se remonta a un principio metodológico y filosófico, perfectamente aplicable al desarrollo de software, según el cual, “en igualdad de condiciones, la explicación más sencilla suele ser la correcta”.
    * Este principio lo podemos usar tanto en el momento de implementar una solución como a la hora de encontrar el causante a un bug. ¿Cuántas veces nos habrá pasado que la metedura de pata más tonta es la causante del problema aunque hayamos estado comprobando lo más complejo?

