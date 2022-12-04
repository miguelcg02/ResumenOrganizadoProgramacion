https://app.diagrams.net/#G1rS5xDpoYruZYjELSljC1wFJYDZf10zns

# ¿Que es diseño?

“El diseño es el proceso previo de configuración mental, "pre-figuración", en la búsqueda de una solución en cualquier campo.

# diseño en ing de software

• Combina los requisitos, las necesidades y las consideraciones técnicas con creatividad para formular el producto o sistema.
• Permite modelar el producto o sistema que se va a construir.
• Permite establecer y medir la calidad del producto o sistema.
• Facilita el mantenimiento del producto o sistema.
• Permite definir el nivel de reutilización del producto o sistema.

# Principios básicos de diseño

* Hay dos formas de construir un diseño del software. Una es hacerlo tan simple que sea obvio que no hay deficiencias, y la otra es hacerlo tan complicado que no haya deficiencias obvias. El primer método es mucho más difícil.

# Características de un buen diseño

1. Debe tener una arquitectura que:
    • Se haya creado empleando estilos o patrones arquitectónicos reconocibles.
    • Tenga componentes con buenas características de diseño.
    • Se implemente en forma evolutiva, de modo que facilite las pruebas.

2. Debe ser modular, es decir, el software debe estar dividido de manera lógica en elementos o subsistemas.
3. Debe contener distintas representaciones de datos, arquitectura, interfaces y componentes.
4. Debe conducir a estructuras de datos apropiadas para las clases que se van a implementar y que surjan de patrones reconocibles de datos.
5.  Debe llevar a componentes que tengan características funcionales independientes.
6. Debe conducir a interfaces que reduzcan la complejidad de las conexiones entre los componentes y el ambiente externo.
7.  Debe obtenerse con el empleo de un método repetible motivado por la información obtenida durante el análisis de los requisitos del software.
8.  Debe representarse con una notación que comunique con eficacia su significado.

# (algunos de los) Principios de diseño de software

- Principio: guia de comportamiento.
1. DRY (Don’t Repeat Yourself): Evita al máximo la repetición de código. Si estás repitiendo código, extrae ese código en una función para encapsularlo. Si tienes que hacer un cambio, este estará localizado en un solo punto, y no esparcido por todo el código fuente.
2. KISS (Keep It Simple Stupid):  El diseño de un programa debe ser sencillo. El sistema debería tener tan pocos componentes como sea posible. La documentación debe ser la información estrictamente necesaria.
3. SoC (Separation of Concerns): Separa los asuntos. Un buen ejemplo de separación es el patrón MVC.
4. YAGNI (You Ain’t Gonna Need It):  no debemos implementar algo si no estamos seguros de necesitarlo. Así ahorramos tiempo y esfuerzo.
5. Boy Scout: debemos refactorizar el código para dejarlo todavía más limpio y simple que antes.
6. La Ley de Demeter: Una unidad sólo debe tener conocimiento limitado de otras unidades, y sólo debe conocer aquellas que están relacionadas. Sólo debe hablar con amigos y nunca con extraños.
7. El principio de Hollywood: “No nos llame, nosotros le llamaremos”. Este principio está relacionado con el principio de inversión de dependencias de SOLID. Un ejemplo del principio de Hollywood es la inversión de control (IoC), que hace que una clase obtenga las referencias a objetos que necesita para funcionar, a través de una entidad externa.
8. La navaja de Occam: “en igualdad de condiciones, la explicación más sencilla suele ser la correcta”

# Solid

- Son cinco principios
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

# S – Single Responsibility Principle ó Principio de Responsabilidad Única

- La del martillo / llave inglesa, tener todo separado!
- Haz una cosa y hazla bien
- Toda clase debería hacer una (y solo una) cosa. Formulada de otra manera, solo debería haber un único motivo para modificar una clase.
- Esa clase debe ser la única con esa responsabilidad. Es decir, si tenemos que cambiar una clase, que sea por una única razón.

# O – Open/Closed Principle ó Principio Abierto Cerrado

- La del destornillador con las 4 puntas puestas, mejor tener un destornillador que pueda tener varias puntas adaptables.
- Debería bastar con añadir código, en lugar de modificarlo.
- Abierto a extensión, cerrado a modificación. Utilizar abstracciones en lugar de instancias concretas. Evitar atributos públicos y protegidos. Evitar variables globales.
- No deberíamos necesitar modificar una clase a no ser que sea para corregir errores.
- El código está mejor diseñado si se puede modificar su comportamiento sin cambiar su código fuente.
- La herencia puede ser una buena solución

# L – Liskov Substitution Principle ó Principio de Sustitución de Liskov

- La del pez martillo y el martillo. Si se llega a la padre, se puede solucionar bien el porblema.
- Una clase base debe poder ser sustituida por su clase derivada.
- Los objetos de un programa pueden ser reemplazados por las instancias de sus propios subtipos sin alterar el correcto funcionamiento del programa.

# I – Interface Segregation Principle ó Principio de Segregación de Interfaces

- La imagen del enchufe que tiene una entrada y un montón de salidas, mejor una entrada y una salida única.
- Los clientes no deberían verse obligados a depender de interfaces que no necesitan. Evita interfaces complejas segregándolas en otras más pequeñas.
- Es preferible tener varias interfaces pequeñas, a tener una interfaz grande. Así no obligamos a los clientes a depender de métodos que no necesitan implementar.

# D – Dependency Inversion Principle ó Principio de Inversión de Dependencia

- La del correo, sin importar el medio tiene que llegar el mensaje.
- Las clases de mayor nivel no deberían depender de las clases de menor nivel. Ambas deberían depender de abstracciones. Las abstracciones no deberían depender de detalles. Los detalles deberían depender de abstracciones.

# Clean code

1. Tu eres el responsable de la calidad de tu código. 
2. Utilizar nombres descriptivos.
3. Escribe código que exprese lo que va a hacer.
4. El código debe hablar por si mismo. Entre menos comentarios necesarios mejor. Saber cuando hay que escribirlos.
5. Deja el código mejor de lo que te encontraste.
6. Que tu código haga una cosa y solo una cosa.
7. Escribe pruebas o tests. 
8. Trabaja sobre la imagen general del proyecto, y desps los detalles.
9. Arquitectura independientes. 
10. Practica, practica y practica.

# ¿Qué debes hacer para llegar a ser un maestro del desarrollo de software?

1. Aprender las reglas: algoritmos, estructuras de datos, lenguajes de programación
2. Aprender los principios: programación, POO, programación estructurada
3. Entender patrones: estudiar el diseño y código de otros maestros, descubrir patrones, memorizarlos y aplicarlos repetidamente.

# Definición de Patrón

- Es una descripción de un problema y su solución, la solución puede reutilizarse en otros contextos.
- Es una descripción de sabiduría y experiencia acumulada.

# Beneficios de los patrones

- Uso de soluciones probadas y bien documentadas
- Producción de buenos diseños
- Normalmente utilizan buenas prácticas
- Vocabulario común que facilita la comunicación
- Ayuda en la documentación
- Ayuda a la conversión de un modelo de análisis a un modelo de implementación
- Aumento de la productividad
- Permite anticiparse al cambio.

# Catálogos de patrones

- GoF (Gang of four): Solución de problemas del diseño.
- POSA (Pattern-Oriented Software Architecture): Definición de estrategias arquitectonicas.
- J2EE
- PoEAA
- GRASP (General responsability Assignment Software Patterns): Tránsito entre el análisis y el diseño.

# Catálogo POSA

- Del fango a la estructura: 
    - Capas
    - Tuberías-filtros
    - Pizarra
- Sistemas distribuidos:
    - Broker
- Sistemas interactivos:
    - Model-View-Controller
    - Presentatio-Abstraction-Control
- Sistemas adapatables:
    - Reflection
    - Microkernel    

# Catálogo GoF

* Creación:
    - Clase:
        - Factory Method
    - Objeto:
        - Abstract Factory
        - Builder
        - Prototype
        - Singleton
* Estructural:
    - Clase:
        - Adapter
    - Objeto:
        - Adapter
        - Bridge
        - Composite
        - Decorator
        - Facade
        - Flyweight
        - Proxy
* Comportamiento
    - Clase:
        - Interpreter
        - Template Method
    - Objeto:
        - Chain of responsability
        - Command
        - Iterator
        - Mediator
        - Memento
        - Observer
        - State
        - Strategy
        - Visitor

# Catálogo GRASP

- Creator: factory pattern
- Information expert: information hiding
- Controleer: Model-viwe-controller
- Low Coupling: Loose coupling
- High Cohesion: Cohesion
- Polymorphism: Polymorphism in POO
- Pure Fabrication: Service
- Indirection: Delegation pattern
- Protected variations: Delegation pattern

# Antiopatrones

Hay muchos xd


# GRASP Patrones generales de software para asignar responsabilidades

* Los patrones GRASP son parejas de problema-solució n con un nombre, que codifican buenos principios y sugerencias relacionados con la asignación de responsabilidades.

# Creador

* Asignar la responsabilidad de crear objetos a la clase que realmente tenga que hacerlo. Utilizar los diagramas de colaboración permite tener una clara secuencia de las actividades que realiza la aplicación.

- La creación de objetos es una de las actividades más frecuentes en un sistema orientado a objetos.
- Conviene contar con un principio general para asignar las responsabilidades concernientes a ella.
- El propósito fundamental de este patrón es encontrar un creador que debemos conectar con el objeto producido en cualquier evento.
- Al escogerlo como creador, se da soporte al bajo acoplamiento.

* BENEFICIOS:
- En ocasiones encontramos un patrón creador buscando la clase con los datos de inicialización que serán transferidos durante la creación.
- Los datos de inicialización se transmiten durante la creación a través de algún método de inicialización, como un constructor en java que cuenta con parámetros.
- Éste es en realidad un ejemplo del patrón Experto.

# Experto

* Asignar responsabilidades a las clases expertas en la información, es decir, cuyos objetos poseen la información necesaria para cumplirlas. Es indispensable apoyarse en los diagramas de colaboración UML, los cuales son la base para la toma de decisiones en la elaboración del diseño orientado a objetos bajo los Patrones GRASP. 


- Un modelo de clase puede definir docenas y hasta cientos de clases de software, y una aplicación tal vez requiera el cumplimiento de cientos o miles de responsabilidades.
- Si estas se asignan en forma adecuada, los sistemas tienden a ser más fáciles de entender, mantener y ampliar, y se nos presenta la oportunidad de reutilizar los componentes en futuras aplicaciones.

* BENEFICIOS:
- Se conserva el encapsulamiento, ya que los objetos se valen de su propia información para hacer lo que se les pide. Esto soporta un bajo acoplamiento, lo que favorece al hecho de tener sistemas más robustos y de fácil mantenimiento.
- El comportamiento se distribuye entre las clases que cuentan con la información requerida, logrando clases más “sencillas” y más cohesivas. Así se brinda soporte a una alta cohesión.

# Bajo Acoplamiento

* ¿Cómo evitar la gran dependencia generada entre las clases que forman parte del sistema sin que esto conlleve a la generación de código excesivo?
* ¿Cómo dar soporte a una dependencia escasa y a un aumento de la reutilización?

- Tener poca dependencia entre las clases, las clases deben tener la suficiente información para que su relación con otras se reduzca y puedan en algún momento subsistir si una de las clase a las cuales se relaciona deja de existir.

-  El acoplamiento es una medida de la fuerza con que una clase está conectada, depende, conoce o recurre a los objetos de otras clases.
- Dos elementos está acoplados si:
    - Un elemento tiene una agregación , una composición o una asociación con otro elemento.
    - Un elemento implementa o extiende otro elemento.

- Acoplamiento bajo significa que una clase no depende de muchas clases.
- Acoplamiento alto significa que una clase depende de muchas otras clases. Cuando una clase cambia, afecta a la otra.
- El grado de acoplamiento no puede considerarse aisladamente de otros principios como Experto y Alta Cohesión.

- Beneficios:
    - No se afecta por cambios de otros componentes.
    - Cada componente es fácil de entender por separado.
    - Cada componente es fácil de reutilizar.

# Alta cohesión

* ¿Cómo mantener la complejidad dentro de límites manejables?
* ¿Cómo crear clases que contengan la suficiente información, sin que se llegue al exceso de contenido?

- Asignar una responsabilidad de modo que la cohesión siga siendo alta. Una clase con alta cohesión posee una importante funcionalidad y poco trabajo, colabora con otros objetos para compartir tareas muy grandes.
- La cohesión es una medida de cuán relacionadas y enfocadas están las responsabilidades de una clase.
- Una alta cohesión caracteriza a las clases con responsabilidades estrechamente relacionadas que no realicen un trabajo enorme.
- Una baja cohesión hace muchas cosas no afines o realiza trabajo excesivo. Esto presenta los siguientes problemas:
    - Difíciles de comprender
    - Difíciles de reutilizar
    - Difíciles de conservar
    - Las afectan constantemente los cambios

- Alta cohesión: Una clase tiene responsabilidades moderadas en un área funcional y colabora con las otras para llevar a cabo las tareas.

# Controlador

* ¿Quién debería encargarse de atender un evento del sistema?
* Asignar responsabilidades, en el manejo de eventos, a las clases que tienen la capacidad de resolverlas manteniendo una alta cohesión con estas.

- Un “evento del sistema” es un hecho de alto nivel generado por un actor externo. Se asocia a operaciones del sistema: las que emite en respuesta a los eventos del sistema.

* BENEFICIOS:
- Mayor potencial de los componentes reutilizables. Garantiza que la empresa o los procesos de dominio sean manejados por la capa de los objetos del dominio y no por la de la interfaz.
- Reflexionar sobre el estado del caso de uso. A veces es necesario asegurarse de que las operaciones del sistema sigan una secuencia legal o poder razonar sobre el estado actual de la actividad y las operaciones en el caso de uso subyacente.

# Polimorfismo

* ¿Como aplicar el uso de métodos con nombres y funcionalidades específicas en diferentes clases?
* Crear métodos genéricos que reciban y/o procesen
información y ser usados en múltiples clases sin que esto
sea un inconveniente ni se convierta en una redundancia
de información.

- La capacidad que tienen los objetos de diferentes clases de responder al mismo mensaje o evento en función de los parámetros utilizados durante su invocación.
- Conseguir que un objeto de una clase se comporte como un objeto de cualquiera de sus subclases, dependiendo de la forma de llamar a los métodos de dicha clase o subclases.

* BENEFICIOS:
- El polimorfismo nos guía para decidir qué objeto es responsable de manejar los elementos que varían.
- El manejo de nuevas variaciones será fácil.

# Indirección

* -¿Dónde asignar responsabilidades para evitar/reducir el acoplamiento directo entre elementos y mejorar la reutilización?
* Asignar la responsabilidad a un objeto que medie entre los elementos. Asigne responsabilidades para crear una “interfaz” alrededor de ellos.

- El patrón de indirección nos aporta mejorar el bajo acoplamiento entre dos clases asignando la responsabilidad de la mediación entre ellos a un tercer elemento (clase) intermediario.

* BENEFICIOS:
- Bajo acoplamiento.

# Fabricación pura

* ¿Cómo crear objetos que no entren en conflicto con la alta cohesión y el bajo acoplamiento ya establecidos en el diseño?
* Crear clases que permitan la instanciación de objetos sin interferir con el bajo acoplamiento y la alta cohesión. El patrón Factory permite la instanciación de objetos en tiempo de programación.

- La fabricación pura se da en las clases que no representan un ente u objeto real del dominio del problema, sino que se ha creado intencionadamente para disminuir el acoplamiento, aumentar la cohesión y/o potenciar la reutilización del código.
- Al abusar de este patrón suelen aparecer clases función o algoritmo (que tienen un solo método).

BENEFICIOS:
- Proporciona un conjunto de actividades muy cohesionado.
- Descompuesto por el comportamiento - implementa algún algoritmo.
- Proporciona alta cohesión, bajo acoplamiento y puede reutilizar esta clase.

# Variaciones Protegidas

* ¿ Cómo evitar que las variaciones de algunos elementos impacten a los demás elementos?
* Definir una interfaz bien definida y estable para que no haya afectación en otras unidades.

- Es el principio fundamental de protegerse del cambio.
- Aquello que es susceptible de modificaciones, lo envolvemos en una interfaz, utilizando el polimorfismo para crear varias implementaciones y posibilitar implementaciones futuras, de forma que cuando se produzca la variación, las repercusiones sean mínimas.

* BENEFICIOS:
- Proporciona un diseño más estructurado.
- Proporciona flexibilidad y protección frente a variaciones.
- Está relacionado con el polimorfismo.

# GOF

# Memento

- Type: Comportamiento
- What it is: Without violating encapsulation, capture and externalize an object's internal state so that the object can be restored to this state later.
- Traducción: Sin violar la encapsulación, capturar y externalizar el estado interno de un objeto para que el objeto pueda ser restaurado a este estado más tarde.

# Chain of Responsibility

- Type: Comportamiento
- What it is: Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it.
- Evitar el acoplamiento del emisor de una petición con su receptor dando a más de un objeto la oportunidad de manejar la solicitud. Encadenar los objetos receptores y pasar la solicitud a lo largo de la cadena hasta que un objeto la maneje.

# Observer

- Type: Comportamiento
- Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- Definir una dependencia uno-a-muchos entre objetos para que cuando un objeto cambie de estado, todos sus dependientes sean notificados y se actualicen automáticamente.

# Command

- Type: Comportamiento
- Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.
- Encapsular una solicitud como un objeto, lo que le permite parametrizar los clientes con diferentes solicitudes, poner en cola o registrar y soportar operaciones no ejecutables.

# State

- Type: Comportamiento
- What it is: Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.
- Permitir que un objeto altere su comportamiento cuando su estado interno cambia. El objeto parecerá que cambia de clase.

# Interpreter

- Type: Comportamiento
- What it is: Given a language, define a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language.
- Dado un lenguaje, definir una representación para su gramática junto con un intérprete que utiliza la representación para interpretar las frases del lenguaje.

# Strategy

- Type: Comportamiento
- Define a family of algorithms, encapsulate each one, and make them interchangeable. Lets the algorithm vary independently from clients that use it.
- Definir una familia de algoritmos, encapsular cada uno, y hacerlos intercambiables. Permite que el algoritmo varíe independientemente de los los clientes que lo utilizan.

# Iterator

- Type: Behavioral
- What it is: Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
- Proporcionar una manera de acceder a los elementos de un objeto agregado secuencialmente sin exponer su representación subyacente.

# Template Method

- Type: Behavioral
- What it is: Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.
- Define el esqueleto de un algoritmo en una operación, difiriendo algunos pasos a las subclases. Permite a las subclases redefinir ciertos pasos de un algoritmo sin cambiar la estructura del mismo.

# Mediator

- Type: Behavioral
- What it is: Define an object that encapsulates how a set of objects interact. Promotes loose coupling by keeping objects from referring to each other explicitly and it lets you vary their interactions independently.
- Define un objeto que encapsula cómo interactúa un conjunto de objetos. Promueve el acoplamiento flojo al evitar que los objetos se refieran unos a otros explícitamente y permite variar sus interacciones de forma independiente.

# Visitor

- Type: Behavioral
- What it is: Represent an operation to be performed on the elements of an object structure. Lets you define a new operation without changing the classes of the elements on which it operates.
- Representar una operación que se realizar sobre los elementos de una estructura del objeto. Permite definir una nueva operación sin cambiar las clases de los elementos sobre sobre los que opera.

# Adapter

- Type: Structural
- What it is: Convert the interface of a class into another interface clients expect. Lets classes work together that couldn't otherwise because of incompatible interfaces.
- Convertir la interfaz de una clase en otra interfaz que los clientes esperan. Permite que clases trabajar juntas que no podrían de otro modo debido a la incompatibilidad de interfaces incompatibles.

# Proxy

- Type: Structural
- What it is: Provide a surrogate or placeholder for another object to control access to it.
- Proporcionar un sustituto o marcador de posición para
otro objeto para controlar el acceso al mismo.

# Bridge

- Type: Structural
- What it is: Decouple an abstraction from its implementation so that the two can vary independently.
- Desacoplar una abstracción de su implementación para que ambas puedan variar independientemente.

# Composite

- Type: Structural
- What it is: Compose objects into tree structures to represent part-whole hierarchies. Lets clients treat individual objects and compositions of objects uniformly.
- Componer objetos en estructuras de árbol para representar jerarquías parte-todo. Permite que que los clientes traten los objetos individuales  y las composiciones de objetos de manera uniforme.

# Decorator

- Type: Structural
- What it is: Attach additional responsibilities to an object dynamically. Provide a flexible alternative to sub-classing for extending functionality.
- Adjuntar responsabilidades adicionales a un objeto de forma dinámica. Proporcionar una alternativa flexible alternativa a la subclasificación para extender funcionalidad.

# Facade

- Type: Structural
- What it is: Provide a unified interface to a set of interfaces in a subsystem. Defines a high- level interface that makes the subsystem easier to use.
- Proporcionar una interfaz unificada a un conjunto de interfaces en un subsistema. Define una interfaz de alto nivel que facilita el uso del subsistema más fácil de usar.

# Flyweight

- Type: Structural
- What it is: Use sharing to support large numbers of fine grained objects efficiently.
- Utilizar la compartición para soportar un gran número de objetos de grano fino de manera eficiente.

# Abstract Factory

- Type: Creational
- What it is: Provides an interface for creating families of related or dependent objects without specifying their concrete class.
- Proporciona una interfaz para crear familias de objetos relacionados o dependientes sin especificar su clase concreta.

# Builder

- Type: Creational
- What it is: Separate the construction of a complex object from its representing so that the same construction process can create different representations.
- Separar la construcción de un objeto complejo de su representación para que un mismo proceso de construcción pueda crear diferentes representaciones.

# Factory Method

- Type: Creational
- What it is: Define an interface for creating an object, but let subclasses decide which class to instantiate. Lets a class defer instantiation to subclasses.
- Define una interfaz para crear un objeto, pero deja que las subclases decidan qué clase instanciar. Permite que una clase difiera la instanciación a las subclases.

# Prototype

- Type: Creational
- What it is: Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.
- Especifica los tipos de objetos a crear utilizando una instancia prototípica, y crea nuevos objetos copiando este prototipo.

# Singleton

- Type: Creational
- What it is: Ensure a class only has one instance and provide a global point of access to it.
- Garantizar que una clase sólo tenga una instancia y proporcionar un punto de acceso global a la misma.

# Proceso de desarrollo de Software

Requisitos -> Proceso de Desarrollo de Software -> Producto de Software

# Fases genéricas del Proceso de desarrollo de Software

1. Análisis
2. Diseño
3. Implementación
4. Pruebas
5. Despliegue
6. Mantenimiento

# Modelo

Es aquello que sirve como objeto de imitación o referencia. Es una construcción científica bajo la cual se sustenta una realidad.

# Metodología

Indica la forma en que se va a desarrollar algo, en función del contexto.

# Modelos y Metodologías en desarrollo de Software

- Permiten estructurar, planificar y controlar el proceso de desarrollo de software
- No representa cómo se debe desarrollar el software, sino qué se debe hacer
- No todos los sistemas a desarrollar son compatibles con todos los métodos y metodologías de desarrollo de software. Se debe seleccionar el más apropiado, según las condiciones del proyecto
- En muchas ocasiones, lo más apropiado es realizar una combinación de modelos

* En desarrollo de software aún se buscan:
-  Técnicas de desarrollo que minimicen la complejidad de los sistemas de software.
- Métodos que permitan tomar decisiones lo más pronto posible.
- Estrategias que minimicen los efectos de los cambios que se realizan durante el desarrollo y la puesta en producción.

# “Modelo” primitivo

- Se conoce también como Modelo Prueba y Error.
- Es común aplicarlo en las primeras experiencias de programación.
- Se realizan varias iteraciones de implementación – pruebas sin planificación ni diseños previos.

* Ventajas:
- El foco es la implementación

* Desvenajas:
- Código espagueti (falta de estructura)
- Implementación costosa por las múltiples recodificaciones
- Posible rechazo de la solución por parte del usuario al no realizarse un análisis de requisitos
- Depuración costosa por falta de planificación
- Mantenimiento costoso por falta de estructura y documentación

# Modelo clásico o cascada

- Se compone de una serie de fases que se ejecutan secuencialmente.
- Se pasa de una fase a la otra luego de finalizarla.
- El final de cada fase puede tener un punto de revisión.
- Funciona muy bien en desarrollos conocidos y estables.
- Cada una de las fases elaborada debe estar documentada de forma exhaustiva .
- Si el desarrollo queda suspendido en alguna fase, cualquiera podría continuar con el proyecto después de leer la documentación.
- Es muy utilizado.

* Ventajas:
- Proporciona una plantilla/guía para el desarrollo
- Se cuenta con requisitos completos y consistentes desde el inicio

* Desventajas:
- No siempre se desarrolla en forma secuencial
- En ocasiones se debe esperar para terminar tareas
- Para el cliente no es fácil definir todos los requisitos de forma explícita
- Pasar por todo el ciclo toma mucho tiempo
- No es posible tener una versión operativa del programa hasta que se finalice el desarrollo
- Un error no detectado a tiempo puede ocasionar un desastre

# Iterativo vs. Incremental

- La principal diferencia entre un ciclo de vida iterativo y uno incremental es que un proceso iterativo avanza mediante un refinamiento continuo, mientras que un proceso incremental lo hace mediante pequeños incrementos.
- Iterativo: construir la solución/producto general y luego perfeccionar algunas de las áreas que requieren mejoras.
- Incremental: construir y lanzar una característica cada vez en función de las prioridades definidas por el cliente.

# Modelos Evolutivos

- El desarrollo evolutivo consta del desarrollo de una versión inicial que luego de exponerse se refina de acuerdo a los comentarios o nuevos requisitos por parte del cliente o del usuario final.
- Los modelos evolutivos son iterativos, se caracterizan por permitir a los ingenieros de software desarrollar versiones cada vez más completas del software.

# Modelo (cascada) en V

- Variación del modelo en cascada.
- Relaciona las actividades de prueba con las de análisis, diseño y desarrollo.
- Indica que las pruebas se deben efectuar de forma sincrónica con el desarrollo.

* Ventajas: 
- Optimización de la comunicación entre las partes involucradas a través de términos y responsabilidades claramente definidos
- Mejora de la calidad del producto gracias a la integración de medidas de control de la calidad

* Desventajas:
- La respuesta a cambios durante el desarrollo es poco flexible.
- Promueve un curso lineal del proyecto.

# Modelo basado en prototipos

- Entender los requisitos: el prototipo se ajusta para satisfacer las necesidades del cliente. Así, el desarrollador entiende lo que se debe hacer y el cliente ve resultados a corto plazo.
- Comunicar: ayuda al desarrollador y al cliente a entender cuál será el resultado cuando se satisfagan los requisitos.
- Se desarrolla con rapidez, usando los programas adecuados.
- No se debe utilizar mucho dinero, ya que el desarrollo inicia a partir de la aprobación del prototipo.
- Evoluciona a través de un proceso iterativo.
- Permite aclarar los requisitos de los usuarios e identificar las características que deben cambiarse o añadirse.
- Permite verificar la viabilidad del diseño de un sistema
- Refleja los aspectos del software que serán visibles para el cliente o usuario final.

* Tipos de desarrollo:
- Desarrollo desechable: el prototipo es una versión rudimentaria del sistema, posteriormente es desechada
- Desarrollo evolutivo: el prototipo puede convertirse en el sistema final usado
- Desarrollo mixto: combina los prototipos desechables y evolutivos para los requisitos poco conocido

* Tipos de prototipo:
- De interface: modelo en papel o utilizando alguna herramienta que permita mostrar pantallas, menús, navegación, etc.
- De comportamiento – anchura: muestra menús y algún tipo de comportamiento
- De comportamiento – profundidad: cubre totalmente ciertas funciones
- Completo: presenta todo, pero con baja calidad o rendimiento

* Ventajas:
- Es útil cuando el cliente conoce los objetivos generales para el software, pero no identifica los requisitos detallados
- Reduce el riesgo de construir productos que no satisfagan las necesidades del usuario
- Reduce costos y aumenta la probabilidad de éxito

* Desventajas:
- El desarrollador puede tomar decisiones de implementación poco convenientes (por ejemplo usar un lenguaje de programación para desarrollar más rápido)
- El desarrollador puede adoptar esas decisiones como parte del sistema final
- El cliente puede encontrar atractivo el prototipo y quedarse con el prototipo como sistema final
- No se disminuye el tiempo entre la definición de los requisitos y la entrega del producto
- Al usuario no le agrada que se deseche código

# Modelos incrementales

- El sistema se divide en subsistemas de a cuerdo a su funcionalidad.
- Las versiones se definen comenzando con un sistema funcional pequeño y agregando funcionalidad con cada nueva versión.
- Combina elementos de cascada con construcción de prototipos.
- Aplica secuencias lineales. Cada secuencia lineal es un incremento.
- El primer incremento es un producto esencial.
- Útil cuando surge la necesidad de proporcionar de manera rápida un conjunto limitado de funcionalidades para el usuario, y después refinarlo y expandirlo a entregas posteriores.

* Ventajas: 
- Es útil cuando el personal necesario para una implementación completa no está disponible
- Los incrementos se pueden planear para manejar los riesgos técnicos

* Desventajas:
- Requiere mucha planeación a nivel logístico y técnico.
- Requiere de metas claras para conocer el estado del proyecto.
- No es recomendable para sistemas de tiempo real, de alto nivel de seguridad, de procesamiento distribuido y/o de alto índice de riesgos.

# Desarrollo rápido de aplicaciones (RAD)

- Es una adaptación a “alta velocidad” del modelo cascada.
- Busca que se ejecuten ciclos de desarrollo cortos (60 a 90 días).
- Los requisitos se descubren con el cliente.
- Se centra en el código más que en la documentación.
- Se debe hacer uso efectivo de herramientas y frameworks.
- La planeación es esencial, ya que varios equipos de software trabajan en paralelo sobre diferentes funciones del sistema.
- Requiere una participación activa del usuario.

* Ventajas:
- Es útil cuando el personal necesario para una implementación completa no está disponible.
- Los incrementos se pueden planear para manejar los riesgos técnicos.

* Desventajas:
- Los proyectos grandes necesitan los recursos humanos suficientes para crear el número de equipos correcto
- Se requiere alto compromiso de todas las partes involucradas
- No es apropiado cuando los riesgos técnicos son elevados.

# Modelo en Espiral

- Representa, en forma de espiral, una secuencia de actividades.
- Se diferencia de otros modelos por considerar el riesgo.
- Para la ingeniería de software es actualmente el enfoque más realista para el desarrollo de software y de sistemas a gran escala.
- Utiliza un enfoque evolutivo, permitiendo al desarrollador y al cliente entender y reaccionar ante los riesgos en cada nivel evolutivo.
- El software se desarrolla en una serie de versiones incrementales.
- La versión incremental podría ser un modelo en papel o un prototipo.
- Con cada incremento, se producen versiones cada vez más completas.


* Se divide en actividades estructurales, también llamadas regiones de tareas, según Sommerville el ciclo de vida del modelo en espiral se divide en cuatro sectores:

1. Definición de objetivos. En esta fase se identifica las restricciones del proceso y el producto, y algunos riesgos para trazar objetivos y respectivamente planes estratégicos.
2. Evaluación y reducción de riesgos. Se hace un análisis detallado para cada riesgo y se establece los pasos para reducirlo.
3. Desarrollo y validación. Después de evaluar los riesgos, se elige un modelo para el desarrollo del sistema.
4. Planificación. El proyecto se revisa y se toma la decisión de si debe continuar con un ciclo posterior de la espiral.

* Ventajas:
- Puede adaptarse y aplicarse a lo largo de la vida del software
- El desarrollador y el cliente comprenden y reaccionan mejor a los riesgos, en cada nivel evolutivo
- Reduce los riesgos antes de que se conviertan en problemas

* Desventajas:
- Si un riesgo importante no es descubierto y gestionado, surgirán inconvenientes
- No es un modelo muy usado
- Se requiere de experiencia en la identificación de riesgos y refinamiento para su uso generalizado.

# Proceso Unificado de Rational (RUP)

- Es una metodología de desarrollo de software orientada a objetos creada por Rational Software Corporation y actualmente IBM es su propietaria.
- La metodología estándar más utilizada para el análisis, diseño, implementación y documentación de sistemas orientados a objetos.

* Ventajas:
- Los roles están muy bien definidos, lo cual permite asignar tareas y responsabilidades con mayor facilidad
- Se basa en las mejores prácticas
- Integra desarrollo con mantenimiento

* Desventajas:
- Es un proceso grande y complejo
- No es tan adecuado para proyectos pequeños
- Es costoso