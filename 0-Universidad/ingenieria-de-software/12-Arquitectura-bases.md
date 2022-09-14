# Arquitectura

- Lo que define cpomo esta construido mi sistema.
- La arquitectura es de alto nivel (Se mira globalmente).
- Los diagramas son de bajo nivel o detallado (Se mira hasta el código xd).
- La arquitectura es un puente entre requisitos y diseño.
- Arquitectura es la estructura del sistema.
- Muy vinculado a requisitos no funcionales.

# Pa que sirve?

- Para negociar requisitos
- Medio para establecer discusiones con clientes, desarrolladores y administradores.
- Facilitar la discusión acerca del diseño del sistema.

# Preguntas a considerar

1. ¿Existe alguna arquitectura de aplicación genérica o de referencia que actúe como plantilla para el sistema que se está diseñando?
2. ¿Cómo se distribuirá el sistema a través de algunos núcleos o procesadores?
3. ¿Qué patrones o estilos arquitectónicos pueden usarse?
4. ¿Cuál será el enfoque fundamental usado para estructurar el sistema?
5. ¿Cómo los componentes estructurales en el sistema se separarán en subcomponentes?
6. ¿Qué estrategia se usará para controlar la operación de los componentes en el sistema?
7. ¿Cuál organización arquitectónica es mejor para entregar los requisitos no funcionales del sistema?
8. ¿Cómo se evaluará el diseño arquitectónico?
9. ¿Cómo se documentará la arquitectura del sistema?

# Rol del arquitecto

- Líder técnico.
- Tomador de decisiones, combinando experiencia, conocimientos y habilidades (técnicas y no técnicas).
- Evaluador de soluciones y riesgos.
- Investigador de soluciones y sistemas.

# Tipos de arquitectos

- Arquitecto empresarial: garantiza que los objetivos comerciales y estratégicos de una organización estén sincronizados con las soluciones técnicas.
- Arquitecto de soluciones: seleccionan las tecnologías más adecuadas para el problema que debe resolverse.
- Arquitecto de aplicaciones: recomienda soluciones o tecnologías para una aplicación y evalúa enfoques alternativos a los problemas.
- Arquitecto de datos / Arquitecto de información: diseña, implementa y administra la arquitectura de datos de una organización.
- Arquitecto de infraestructura: está involucrado con los componentes de infraestructura (servidores, elementos de red, sistemas de almacenamiento, etc.)
- Arquitecto de seguridad: realiza evaluaciones de seguridad y pruebas de vulnerabilidad.
- Arquitecto de nube: es responsable de la estrategia e iniciativas de computación en la nube de una organización.

# Tipos de requisitos No funcionales más asociados a la arquitectura

- disponibilidad
- rendimiento
- seguridad
- usabilidad

# Ejemplo de disponibilidad

Supongamos que una aplicación Cliente/Servidor debe estar disponible 98% del tiempo (aproximadamente 358 días al año), pero si el servidor sufre un daño, se estima que reestablecerlo toma días, en ese caso se estaría incumpliendo el requisito no funcional relacionado con la disponibilidad.

Para garantizar el cumplimiento del requisito se debe considerar un servidor de respaldo (esclavo) que pueda responder a las peticiones si el servidor principal está inactivo.

Pero ... clonar los datos en el servidor de respaldo es costoso, por lo que se recomienda tener un ser un servidor independiente con la Base de Datos.

# Ejemplo rendimiento

Supongamos ahora que la aplicación debe tener un rendimiento tal que la respuesta a una consulta no debe tardar más de 2 milisegundos. El hecho de tener un servidor principal, un servidor de respaldo y un servidor de Base de Datos puede ralentizar la consulta.

Si se cumple con la disponibilidad, posiblemente se incumpla con el rendimiento.

El Arquitecto debe priorizar los requisitos no funcionales y negociar su cumplimiento.

# Ejemplo escalabilidad

Supongamos también que la aplicación tiene tanto éxito que la cantidad de usuarios aumenta considerablemente, recibiendo 1 billón de peticiones al mismo tiempo, se recomienda entonces agregar un balanceador para recibir las peticiones y enviarlas al servidor en un orden determinado.


* Balanceador

- Recibe, y bajo una estrategia determinada envia al usuario a ciertos servidores, se puede hacer por orden de llegada.
- Se usa en videojuegos.

# 4. Evolución de la arquitectura

1. Monolitica: todo se dlla en el mismo lugar. Igual tiene una separación ordenada.
2. Orientadas a servicios: Se descompone la app para que cada parte de la app ofrezca un servicio. Mejor segmentación de las funcionalidade. Bus central.
3. Microservicios: Hay comunicación entre los servicios.

# Arquitecturas monolíticas

- Mainframes de gran tamaño donde todo estaba en el mismo lugar.
- Inteligencia, procesamiento, interfaces y persistencia en un host central
- Interacción con usuarios por medio de terminales “brutas": teclado

## Cliente/servidor

* Partes:
    - Cliente: hace consultas
    - Servidor: responde consultas
    - Red de comunicación
* El procesamiento se puede dividir
entre el Cliente y el Servidor
* Ejemplos
    - Correo electrónico
    - Servidor de impresión
* Modelos Cliente/Servidor
    - Arquitectura en 2 capas
    - Arquitectura en 3 capas
    - Arquitecturas en n capas


Livianos: Web (Solo son consultas). Almancena poco. Se procesa la lógica del negocio (Funcionalidades del negocio)
Robustos: App movil (Se debe descargar). Almacena mucho.

* Cliente/Servidor a 2 Capas
    - Solo un cliente y un servidor
    - Los datos y el acceso a los datos en el Servidor 
    - Usada para altos volúmenes de usuarios
    - Ej: Cajas registradoras en un almacen
    - Necesidad de replicar el software en cada cliente, para clientes robustos.

* Cliente/Servidor a 3 Capas
    - Solo un cliente y 2 servidores

* Arquitecturas peer to peer
    - Sistemas de llamadas es un ejemplo clasico
    - A veces se es el servidor o el cliente
    - Mayor flexibilidad
    - Video juegos

# Arquitectura orientada a servicios (SoA)

- Transfiere datos de un lugar a otro.
- Se tiene un bus de comunicación. Controlador de la información sobre todos los que se conectan con el.

- Cada funcionalidad es un servicio independiente
- Cada servicio ofrece interfaces que permiten su invocación
- Un proceso de negocio se puede conformar por invocaciones secuenciales a diferentes servicios.
- Se puede quitar algo y reemplazarlo facilmente.

- Ejemplo: Cualquier cosa que pueda separa en partes o servicios.

# Microservicios

- El patrón de arquitectura de microservicios (MSA) crea aplicaciones de software utilizando servicios autónomos, pequeños y con versiones independientes. Estos servicios utilizan interfaces bien definidas y se comunican entre sí a través de protocolos ligeros estándar.
- Los servicios son más robustos.

- Ejemplo: Igual que el de SoA



