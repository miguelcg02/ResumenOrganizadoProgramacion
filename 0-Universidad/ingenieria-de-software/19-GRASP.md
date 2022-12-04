# Patrones

1. Creador: Determinar que clases de resposable de crear instancias. Tambien es experto.
2. Experto: Asignar responsabilidades a las clases con la información necesaria.
3. Bajo acoplamiento: Reducir el acoplamiento (la dependencia de clases, que tenga menos relaciones) de las clases.
4. alta cohesión: Tener clases muy especializadas.
5. Controlador: Asignar la responsabilidad de recibir y procesar los mensajes del sistema. Rol de gestión. Se relaciona con indirección (Agregar clase intermedia).
6. Fabricación pura: Crear clases especificas para una funcionalidad, no necesariamente no viene con el dominio o con el contexto.
7. Polimorfismo: Asignar un nuevo comportamiento a la jerarquia de clases. Ofrecer diferentes clases que vienen heredadas.
8. Indirección: Desacoplar las clases utilizando una clase intermedia.
9. Variaciones protegidas: No comunicarse con clases desconocidas

- La clase main cumple la función de creador, es la que crea los objetos. La composición tiene creación.
- Experto: Crea las clases.
- Bajo acoplamiento: Relación con pocas clases.
- Alta cohesión: Se tienen clases especializadas.

* En general el experto es clave para un bajo acoplamiento y una alta cohesión.
* A menudo, un intermediario d eindirección es tambien una fabricacion pura.
* Las variaciones protegidas pueden lograrse con polimorfismo.
* La indirección ayuda al bajo acoplamiento.
* Cuando la creación es un proceso complejo o varia dependiendo de una entrada, a menudo querra crear utilizando una clase diferente que implemente el patron GoF concrete Factory o Abstract Factory.
* Los patrones de diseño de GoF son fabricaciones puras (a menudo con multiples clases).
* Los patrones GoG Adapter, Bridge, Facade, observer y mediator se relacionan con indirección.