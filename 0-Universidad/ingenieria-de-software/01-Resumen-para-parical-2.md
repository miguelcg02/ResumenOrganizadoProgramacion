# Diagramas

https://app.diagrams.net/#G1rS5xDpoYruZYjELSljC1wFJYDZf10zns

# ¿Qué es arquitectura de software?

- Es la estructura del sistema.
- Describe cómo se organiza el sistema (conjunto de
componentes que se comunican entre ellos).

* Apoya la toma de decisiones tempranas que
pueden ser difíciles de cambiar posteriormente
    - Base de datos
    - Infraestructura
    - Estilos y patrones de arquitectura
    - Tecnologías a usar

- La arquitectura de software toma en consideración el
entorno en el que debe operar un sistema de software.
- Las vistas de la arquitectura se crean a partir de la
descripción de la arquitectura, y cada vista cubre una o más preocupaciones de arquitectura.

- La arquitectura de software es la base de un sistema de software.
- Garantiza el desarrollo exitoso y eventualmente mantenimiento del sistema.
* Ofrece beneficios como:
    - Cumplimiento con los requisitos
    - Consideración de las habilidades del sistema de software
    - Producción de un modelo reusable
    - Cumplimiento con las restricciones de implementación

# Para que sirve la arquitectura de software

- Plan de diseño para negociación de requisitos de sistema.
- Medio para establecer discusiones con clientes, desarrolladores y administradores.
- Facilitar la discusión acerca del diseño del sistema.
- Documentar una arquitectura que se haya diseñado y/o implementando.

# ¿Quién es el Arquitecto?

- Líder técnico.
- Tomador de decisiones, combinando experiencia, conocimientos y habilidades (técnicas y no técnicas).
- Evaluador de soluciones y riesgos.
- Investigador de soluciones y sistemas.

# RNF (Requisitos No Funcionales)

- Disponibilidad: deben incluirse componentes redundantes, los cuales puedan ser reemplazados y actualizados sin detener el sistema. Incluir componentes redundantes, de manera que sea posible sustituir y actualizar componentes sin detener el sistema.

Ej: Para garantizar el cumplimiento del requisito se debe considerar un servidor de respaldo (esclavo) que pueda responder a las peticiones si el servidor principal está inactivo.

Pero ... clonar los datos en el servidor de respaldo es costoso, por lo que se recomienda tener un ser un servidor independiente con la Base de Datos.

- Rendimiento: las operaciones críticas se deben concentrar en pocos componentes, es deseable que estén en la misma localización.

Ej : Usar componentes grandes en vez de pequeños y de grano fino para disminuir el número de comunicaciones entre componentes.


- Seguridad: los elementos a proteger deben estar detrás de una(s) barrera(s).

Ej: definir una estructura en capas para la arquitectura, con los activos más críticos protegidos en capas más internas y con alto grado de validación de seguridad aplicado a dichas capas.

- Accesibilidad

- Usabilidad

- Estabilidad

- Portabilidad

- Interoperabilidad

- Escalabilidad: Puede aumentar de forma vertical (Mejorar lo que se tiene) u horizontal (Agregar adiciones).
Ej: agregar un balanceador para recibir las peticiones y enviarlas al servidor en un orden determinado. Cómo los servidores de los videojuegos que ponen un limite  para ingresar a cada server.

- Concurrencia

- Mantenibilidad: se debe diseñar usando componentes auto contenidos de grano fino que puedan cambiarse con facilidad.

Ej: Los productores de datos tienen que separarse de los consumidores y hay que evitar compartir estructuras de datos.

- Para evaluar un RNF es necesario especificar criterios o métricas.
- Los RNFs son usados para juzgar la operación de un sistema.
- Los RNFs no describen información a guardar, ni funciones a realizar.
- Los RNF tienen impacto directo en el diseño de la arquitectura.


# Arquitecturas Monolíticas - Modelo centralizado

- Mainframes de gran tamaño
- Inteligencia, procesamiento, interfaces y persistencia en un host central
- Interacción con usuarios por medio de terminales “brutas”: teclado
- Exitosas para procesamientos intensivos de datos
Ejemplo: Bancos
- Dificultades para el uso de interfaces gráficas
- Código estrechamente acoplado 
- Todo se ejecuta en la misma máquina

# Cliente/Servidor

* Partes:
    - Cliente: hace consultas
    - Servidor: responde consultas
    - Red de comunicación
* El procesamiento se puede dividir entre el Cliente y el Servidor
* Ejemplos:
    - Correo electrónico
    - Servidor de impresión
* Modelos Cliente/Servidor:
    - Arquitectura en 2 capas
    - Arquitectura en 3 capas
    - Arquitecturas en n capas
* La presentación y (parte de) la lógica de negocio en el Cliente
* Los datos y el acceso a los datos en el Servidor
* Usada para altos volúmenes de usuarios
* Ejemplo:
    - Cajas registradoras en un almacén de cadena
* Eficiencia:
    - procesamiento cerca de los datos
* Desventaja
    - necesidad de replicar el software en cada cliente

# Tipos de clientes

Pesado:
- Asume la mayor parte de las funcionalidades
- Aprovecha la capacidad de cómputo del lugar donde se ejecuta
- Mejor interfaz de usuario
- Necesidad de replicar instalación

Liviano:
- Dependen del servidor
- Se centra en transportar la entrada y la salida entre el usuario y el servidor
- No requiere altas capacidades de cómputo*

# Cliente/Servidor a 3 Capas

* Capa intermedia entre el cliente y el servidor
* La capa intermedia puede:
    - facilitar encolado de peticiones
    - ejecutar aplicaciones y lógica de negocio
    - obtener información de la base de datos
* Aumenta el rendimiento del sistema
* Aumenta la complejidad

# Arquitectura Peer to Peer

* Variante de Cliente/Servidor
* El Cliente puede asumir el rol de Cliente y el rol de Servidor
* El Servidor puede asumir el rol de Servidor y de Cliente
* Mayor flexibilidad

Ejemplos:
* Sistemas de comunicación (Ejemplo: Skype, WhatsApp)
* Juegos multijugador en línea

# Arquitectura Orientada a Servicios (SoA)

* Cada funcionalidad es un servicio independiente
* Cada servicio ofrece interfaces que permiten su invocación
* Un proceso de negocio se puede conformar por invocaciones secuenciales a diferentes servicios

# Microservicios

El patrón de arquitectura de microservicios (MSA) crea aplicaciones de software utilizando servicios autónomos, pequeños y con versiones independientes. Estos servicios utilizan interfaces bien definidas y se comunican entre sí a través de protocolos ligeros estándar.

# Niveles de abstracción

* Arquitecturas en pequeño
    - Se interesa por la arquitectura de programas individuales.
    - En este nivel nos concentramos en la forma en que el programa individual se separa en componentes.
* Arquitecturas en grande
    - Se interesa por la arquitectura de sistemas empresariales complejos que incluyen otros sistemas, programas y componentes de programa.

# Ventajas de documentar una arquitectura

* Comunicación con los participantes
- La arquitectura es una presentación de alto nivel del sistema.
- La arquitectura puede usarse como un enfoque para discusión de un amplio número de participantes.

* Análisis del sistema
- Las decisiones de diseño arquitectónico tienen un efecto profundo sobre si el sistema puede o no cubrir requisitos críticos como:
    - Rendimiento
    - Fiabilidad
    - Mantenibilidad

* Reutilización a gran escala,
- Un modelo de una arquitectura de sistema es una descripción corta y manejable de cómo se organiza un sistema y cómo inter-operan sus componentes.
- Por lo general es la misma para sistemas con requisitos similares y, por lo tanto, puede soportar la reutilización de software a gran escala.
    - Por ejemplo: Arquitecturas de línea de productos

# Vistas arquitectónicas

- Una vista arquitectónica es una representación de uno o más aspectos de la arquitectura.
- Una vista contiene un grupo de componentes y sus relaciones, con un significado particular dentro del sistema.

# Modelo de 4+1 vistas

* Vista lógica
- Se centra en las funcionalidades del sistema.
- Indica las abstracciones clave en el sistema como objetos o clases de objeto.

* Vista física
- Se centra en la topología de los componentes de software y en las conexiones físicas entre esos componentes.
- Expone el hardware y el software del sistema y cómo los componentes de software se distribuyen a través de los procesadores en el sistema.

* Vista de proceso
- Se centra en el comportamiento del sistema en tiempo de ejecución.
- Permite hacer juicios acerca de las características no funcionales, como el rendimiento y la disponibilidad.

* Vista de desarrollo
- Presenta el sistema desde la perspectiva del programador.
- Muestra cómo se descompone el software en elementos que son implementados por un desarrollador o un equipo de desarrollo.

# Diagrama de Componentes

- Ilustra los componentes de software que serán usados para construir el sistema (módulos de código fuente, bibliotecas, módulos ejecutables, etc.)
- Ilustra cómo interactuarán los componentes para que el sistema funcione de forma adecuada.
- Se puede construir a partir del Diagrama de Clases.
- Está asociado en gran medida al lenguaje de programación que se utilizará para desarrollar el sistema.

- Un componente es una parte lógica y reemplazable de un sistema.
- Un componente proporciona interfaces bien definidas, facilitando la sustitución de componentes.
- Un componente puede verse como la materialización de una o más clases.
- Cada componente debe tener un nombre que lo distinga de los demás.

* Estereotipos de Componente
<< executable >>: se puede ejecutar en un nodo
<< library >>: biblioteca
<< table >>: tabla de la base de datos
<< file >>: documento de código fuente o datos
<< document >>: documento

* Interfaz
- Una interfaz es una colección de métodos abstractos y propiedades.
- En las interfaces se especifica qué se debe hacer pero no su implementación.
- Una interfaz sólo define cuales son los métodos que han de implementar los objetos de aquellas clases.
- Las clases que implementen estas interfaces son las que describen la lógica del comportamiento de los métodos.
- La clase debe implementar TODOS los métodos definidos por la interfaz.
- Interfaz ofrecida: Especifica los “servicios” que puede ofrecer el componente.
- Interfaz requerida: Indica los “servicios” que necesita un componente.
- Las interfaces facilitan la sustitución de componentes.

* Dependencias
- Las dependencias entre componentes se muestra como una flecha punteada. La dependencia quiere decir que un componente necesita de la otra para completar su definición.
- Si las dependencias entre componentes se hacen a través de interfaces, los componentes se pueden sustituir por otros componentes que realicen las mismas interfaces.

# Diagrama de Despliegue

- Describe la arquitectura física del sistema durante la ejecución, en términos de: Procesadores, Dispositivos, Componentes de software.
- Describe la topología del sistema: la estructura de los elementos de hardware y el software que se ejecuta en cada uno de ellos.

* Nodo
- Es un objeto físico de ejecución que representa un recurso computacional, que generalmente tiene memoria, y a menudo cuenta con capacidad de procesamiento.
- Los nodos pueden tener estereotipos para distinguir diferentes tipos de recursos, tales como CPU (Unidad central de procesamiento), dispositivos, y memorias.
- Cada nodo debe tener un nombre que lo distinga de los demás.

* Dispositivo
- Los dispositivos del sistema también se representan como nodos.
- Generalmente se usan estereotipos para identificar el tipo de dispositivo.

* Relaciones
- Los nodos se conectan mediante asociaciones de comunicación.
- Estas asociaciones indican:
    - Algún tipo de ruta de comunicación entre los nodos.
    - Los nodos intercambian objetos o envían mensajes a través de esta ruta.
- El tipo de comunicación se identifica con un estereotipo que indica el protocolo de comunicación o la red

# Diagrama de Paquetes

- Un paquete es una parte de un modelo.
- Un paquete es un grupo de elementos de un modelo.
- Cada parte de un modelo debe pertenecer a un paquete.
- El modelador puede asignar el contenido de un modelo a un conjunto de paquetes.
- La asignación debe seguir un cierto principio racional, tal como, funcionalidad común, implementación y punto de vista.
- UML no impone una regla para componer paquetes.

- Contiene:
    - Clases, máquinas de estado, diagramas de casos de uso, . . . cualquier elemento que no esté contenido en otro.
- Un paquete puede contener uno o más tipo de elementos.
- Los paquetes pueden contener otros paquetes.
- Reflejan la arquitectura de alto nivel de un sistema: su descomposición en subsistemas y sus dependencias.

* Dependencias
- Las dependencias deben verse a un alto nivel de abstracción.
- La dependencia entre paquetes implica que existe un enfoque ascendente (una declaración de existencia).

* Subsistema
- Un subsistema es un paquete que tiene piezas separadas de especificación y de realización.
- Representa una unidad coherente del modelo, con interfaces limpias al resto del sistema. Representa generalmente la partición del sistema en un límite funcional o de implementación.
- Los modelos y los subsistemas se dibujan como paquetes con las palabras clave de estereotipo.

* ¿Cuándo crear un paquete?
- Para agrupar elementos que proporcionan un mismo servicio.
- Cuando los elementos están muy relacionados (alto nivel de cohesión).
- Cuando los elementos colaboran poco con los elementos de otro paquete.

# Estilos Arquitectónicos

- Un estilo es una forma para resolver una clase de problemas que tienen atributos de calidad comunes.
- Es una plantilla que orienta la construcción de la solución.
- Establece un conjunto de reglas de configuración, como la topología del sistema.
- Cada estilo describe:
    - Un conjunto de componentes
    - Un conjunto de relaciones
    - Un conjunto de restricciones

* Arquitectura de flujo de datos
    - Tubería y filtros
    - Procesamiento por lotes
* Arquitectura centrada en datos
    - Repositorios
    - Arquitecturas de pizarra
* Estilos de Llamada y Retorno
    - Arquitecturas de programa principal y subprogramas
    - Sistemas basados en llamadas de procedimientos remotos
* Estilos orientados a objetos
* Estilo en capas

# Arquitectura de flujo de datos

- Se usa cuando los datos de entrada deben ser transformados en datos de salida a través de una serie de componentes.

* Pipe and filters (tubería y filtros)
    - Tiene componentes (filtros) conectados (por tubos).
    - Los tubos transmiten datos de un filtro al siguiente filtro.
    - Cada filtro trabaja de manera independiente, esperando una entrada de datos de cierta forma y entregando una salida en una forma especificada.
    - Se usa en sistemas de producción.
    - No se recomienda cuando se requiere interactividad

* Batch sequential (procesamiento de lotes)

- Modelo secuencial de procesamiento de datos.
- Un subsistema sólo puede iniciar su ejecución una vez que la ejecución del subsistema que le precede ha completado su ejecución.
- Comúnmente usado en el ámbito empresarial, incluye facturación y transacciones bancarias.
- No proporciona interactividad

# Arquitectura centrada en datos

- En el centro hay un espacio de almacenamiento de datos.
- Los componentes acceden con frecuencia al espacio de almacenamiento de datos para agregar, modificar o eliminar datos.
- Promueve la integrabilidad, es decir, que los componentes puedan
ser cambiados con facilidad sin afectar los datos.

* Repositorios
- En el centro hay un repositorio de datos (como un archivo o una base de datos).
- Los demás componentes acceden con frecuencia al repositorio de datos para agregar, modificar o eliminar datos.
- Promueve la integrabilidad, es decir, que los componentes puedan ser cambiados con facilidad.

* Pizarra
- Pizarrón es una variante de este estilo, en la cual se envían notificaciones al software cliente cuando hay cambios en los datos de su interés.
- El pizarrón coordina la transferencia de información entre clientes.

# Arquitecturas de llamada y retorno

- Permite obtener una estructura fácil de modificar y escalar.
- La arquitectura de programa principal y subprogramas tiene un programa principal que invoca a otros componentes.
- En la arquitectura de llamada de procedimiento remoto, los componentes están distribuidos a través de diferentes dispositivos en una red.

# Arquitecturas orientadas a objetos

- La comunicación y coordinación entre los componentes se hace mediante la transmisión de mensajes.
- Los componentes incluyen datos y operaciones capaces de manipular los datos.

# Arquitecturas en capas

- Cada capa ejecuta un conjunto de operaciones específicas.
- La capa más externa se encarga de las operaciones de la interfaz de usuario.
- La capa más interna se encarga de comunicarse con el sistema operativo.
- Las capas intermedias proveen servicios y funciones de software de aplicación.
- Los componentes se organizan en capas horizontales.
- Cada capa desempeña una función específica.
- La mayoría de las arquitecturas por capas tiene 4 capas:
    - Presentación
    - Negocio
    - Persistencia
    - Base de datos

* Ventajas:
- Alta comprobabilidad porque los componentes pertenecen a capas específicas de la arquitectura.
- Alta facilidad de desarrollo porque este patrón es muy conocido y no es excesivamente complejo de implementar, además, se convierte en una elección natural para la mayoría de los desarrollos de aplicaciones empresariales.
- Mantenible.
- Fácil de asignar roles separados.
- Fácil de actualizar y mejorar las capas por separado.

* Usos:
- Aplicaciones estándar de línea de negocios que hacen más que sólo operaciones CRUD.
- Nuevas aplicaciones que necesitan ser construidas rápidamente.
- Equipos de desarrolladores inexpertos que aún no entienden otras arquitecturas.
- Aplicaciones que requieren normas estrictas de mantenimiento y comprobabilidad.

# Patrones Arquitectónicos

- Es una solución a un problema recurrente.
- Describe una organización abstracta estilizada de buena práctica, que se ensayó y se puso a prueba en diferentes sistemas y entornos.
- Debe incluir información sobre cuándo es y cuándo no es adecuado usar dicho patrón, así como sobre las fortalezas y debilidades del patrón.
- Simplifica el diseño y permite obtener los beneficios de usar una solución que está probada.
- Introduce restricciones de diseño que reducen la complejidad y ayudan a prevenir decisiones incorrectas.

# Patron MVC

- El patrón Modelo-Vista-Controlador (MVC) es un patrón de arquitectura de software que se usa ampliamente. Es especialmente adecuado para aplicaciones web, aunque también se puede utilizar para otros tipos de aplicaciones como las aplicaciones de escritorio.
- Separa los datos y la lógica de negocio de una aplicación de la
interfaz de usuario.
- Varios marcos de desarrollo web y aplicaciones hacen uso de
este patrón: Ruby on Rails, ASP.NET MVC, Spring MVC.

* Modelo
- El Modelo gestiona los datos de la aplicación y su estado. Entre sus responsabilidades se encuentra el procesamiento de los datos hacia y desde un almacén de datos.
- El modelo es independiente de los controladores y las vistas, lo que permite reutilizarlo con diferentes interfaces de usuario.
- El modelo recibe directivas del controlador para recuperar y actualizar datos.
- En algunas variaciones de MVC, el modelo es pasivo y debe recibir una solicitud para enviar una actualización del estado de la aplicación. En otras variaciones, se pueden enviar notificaciones de cambios de estado del modelo a la vista.

* Vista
- La vista gestiona lo que se muestra al usuario.
- La vista es una representación del estado del modelo.

* Controlador
- El controlador es un intermediario entre el usuario y el sistema.
- Captura las acciones desde la vista, las interpreta y actúa en función de ella.
- Realiza transformaciones de datos para que la vista y el modelo “se entiendan”.

* Ventajas
- Separación de preocupaciones
- Facilidad para realizar pruebas
- Facilidad para reutilizar los componentes de la interfaz de usuario
- Desarrolladores especializados en el desarrollo de frontend o backend
- Algunas tareas pueden realizarse en paralelo.

* Desventajas
- Es difícil de lograr una separación completa
- Requiere que los desarrolladores sean expertos en múltiples tecnologías
- Cambios frecuentes en un modelo pueden resultar en actualizaciones excesivas de las vistas

# Patrón Arquitectura basada en eventos

- Está formado por componentes de procesamiento de eventos altamente desacoplados y de propósito único.
- Es un patrón asíncrono distribuido usado para producir aplicaciones altamente escalables.
- La arquitectura consiste en componentes de procesamiento de eventos de un solo propósito que escuchan los eventos y los procesan asincrónicamente. La arquitectura impulsada por eventos construye una unidad central que acepta todos los datos y luego los delega a los módulos separados que manejan el tipo particular.

* Ventajas
- Son fácilmente adaptables a entornos complejos, a menudo caóticos.
- Escala fácilmente.
- Son fácilmente ampliables cuando aparecen nuevos tipos de eventos.

* Usos
- Sistemas asíncronos con flujo de datos asíncronos.
- Interfaces de usuario.

# Patrón Arquitectura Microkernel

- Se usa comúnmente para implementar aplicaciones basadas en productos, es decir, aquellas que se empaquetan y se ponen a disposición para su descarga por versiones.
- Permite añadir funciones adicionales a la aplicación principal, lo que proporciona extensibilidad, así como separación y aislamiento de funciones.
- Se utiliza típicamente cuando los equipos de software crean sistemas con componentes intercambiables.

* Ventajas
- Gran flexibilidad y extensibilidad.
- Buena portabilidad.
- Facilidad de despliegue.
- Respuesta rápida a un entorno en constante cambio.
- Los módulos enchufables pueden probarse de forma aislada.
- Alto rendimiento ya que puede personalizar y racionalizar las aplicaciones para incluir sólo las características que necesita.

* Usos
- Aplicaciones que toman datos de diferentes fuentes, los transforman y los escriben a diferentes destinos
- Aplicaciones de flujo de trabajo.
- Solicitudes de programación de tareas y trabajos.

# Patrón Arquitectura de microservicios

- Cada componente se despliega como una unidad independiente, lo que facilita el despliegue.
- Los componentes contienen uno o varios módulos.
- Se puede requerir un orquestador de componentes.

* Ventajas
- Es posible escribir, mantener y desplegar cada microservicio por separado.
- Fácil de escalar, ya que sólo se pueden escalar los microservicios que necesitan ser escalados.
- Es más fácil reescribir las piezas de la aplicación porque son más pequeñas y menos acopladas a otras partes.
- Altamente mantenible y comprobable – permite un desarrollo y despliegue rápido y frecuente.
- Desplegable de forma independiente.

* Usos
- Sitios web con pequeños componentes.
- Centros de datos corporativos con límites bien definidos.
- El rápido desarrollo de nuevos negocios y aplicaciones web.
- Equipos de desarrollo que se extienden, a menudo por todo el mundo.

# Aplicación Móvil

* Definición: 
- Pueden ser desarrolladas como cliente ligero o aplicaciones de cliente enriquecido. Las aplicaciones de cliente móvil enriquecido pueden apoyar escenarios desconectados o que se conectan ocasionalmente. Las aplicaciones de cliente ligero o web soportan sólo escenarios conectados. Los recursos de los
dispositivos pueden ser una restricción al diseñar aplicaciones móviles.
* Beneficios:
    - Compatible con dispositivos portátiles (handheld).
    - Provee disponibilidad y facilidad de uso.
    - Soporta escenarios sin conexión y con conexión ocasional.
* Consideraciones:
    - Limitantes de entrada y navegación.
    - Área de visualización (pantalla) limitada.
* Aplicación multicapa que consta de:
    - Capa de experiencia de usuario (presentación)
    - Capa de negocio
    - Capa de datos
- Si el cliente es enriquecido, las capas de negocio y datos estarán en el cliente (dispositivo)
- Si el cliente es liviano, las capas de negocio y datos estarán en el servidor Usa caché local para soportar el funcionamiento sin conexión.

* Consideraciones generales
- Decida si va a crear un cliente enriquecido, un cliente web ligero o una aplicación de Internet enriquecida (RIA)
- Decida el tipo de dispositivos que va a soportar.
- Considere escenarios de conexión ocasional y de ancho de banda limitado cuando sea pertinente.
- Diseñe una interfaz de usuario adecuada para dispositivos móviles, teniendo en cuenta las limitantes del dispositivo.
- Diseñe una arquitectura en capas que facilite la reutilización y capacidad de mantenimiento.
- Considere las limitaciones de recursos como tamaño de la memoria y velocidad de procesamiento del dispositivo.

# Aplicaciones de cliente enriquecido (Rich client applications)

* Definición:
Puede proporcionar una experiencia de usuario altamente sensible e interactiva para aplicaciones que deben funcionar en escenarios stand-alone. Puede diseñarse para escenarios desconectados y ocasionalmente conectados para acceder a datos o funcionalidades remotas. Una aplicación de este tipo normalmente se estructura como una aplicación de varias capas: experiencia del usuario (presentación), negocios y de datos.
* Beneficios:
    - Capacidad para aprovechar los recursos de los clientes.
    - Provee mejor tiempo de respuesta y experiencia de usuario mejorada.
    - Interacción altamente dinámica y receptiva.
    - Soporte para escenarios sin conexión y con conexión ocasional.
* Consideraciones:
    - Alta complejidad de despliegue.
    - Desarrollos específico de y para la plataforma.
    - El control de versiones puede ser complejo.

* Aplicación multicapa que consta de:
    - Capa de experiencia de usuario (presentación)
    - Capa de negocio
    - Capa de datos
* Puede usar datos almacenados en un servidor remoto o almacenados localmente.
* Puede consumir servicios expuestos por otras aplicaciones.
* Consideraciones generales de diseño
    - Seleccione una tecnología adecuada en función de los requisitos de la aplicación.
    - Separe la lógica de presentación de la implementación de la interfaz.
    - Diseñe una interfaz adecuada y fácil de usar.
    - Aplique la separación de intereses en todas las capas.
    - Reutilice la lógica de presentación común.
    - Evite alto acoplamiento con objetos de otras capas.
    - Ejecute métodos asíncronos (si es posible) para evitar espera o bloqueo en la interfaz de usuario.

# Aplicación de Internet Enriquecida

* Definición:
Se puede desarrollar para soportar mú ltiples plataformas y mú ltiples
navegadores, para mostrar contenido grá fico. Se ejecuta en un navegador lo que
restringe el acceso a algunas de las características del cliente.
* Beneficios:
- Proveen las mismas caracterí sticas en la IU que los clientes enriquecidos.
- Soporte para la visualización de contenidos enriquecidos, streaming y gráficos.
- Despliegue sencillo con el mismo alcance que los clientes web.
- Actualización y control de versiones simple.
- Soporte multi-plataforma y multi-navegador.
* Consideraciones:
- Tiempo de carga más largo comparado con las aplicaciones web.
- Restricciones en el uso de recursos del cliente comparada con aplicaciones de cliente enriquecido.

* Aplicación multicapa que consta de:
- Capa de experiencia de usuario (presentación)
- Capa de negocio
- Capa de datos
* Generalmente dependen de un plug-in del lado del cliente
* Proporciona visualización muy gráfica

* Consideraciones generales de diseño
- Seleccione una RIA en función de la audiencia, la riqueza de la interfaz y la facilidad de despliegue.
- Diseñe una infraestructura web que use servicios.
- Diseñe para aprovechar la potencia de procesamiento del cliente.
- Defina la complejidad de los requisitos de interfaz de usuario.
- Use escenarios que permitan aumentar el rendimiento o la capacidad de respuesta de las aplicaciones.
- Diseñe para soportar escenarios en los que el plug-in no está instalado.

# Aplicaciones de servicio (Service applications)

* Definición:
Expone funcionalidades del negocio y permiten a los clientes acceder a ellas desde un sistema local o remoto. Las operaciones de servicio se invocan usando mensajes, basados en esquemas XML, pasa sobre un canal de transporte. El objetivo de este tipo de aplicación es lograr acoplamiento flexible entre el cliente y el servidor.
* Beneficios:
- Provee bajo acoplamiento entre cliente y servidor.
- Puede ser consumido por aplicaciones diferentes y no relacionadas.
- Soporta interoperabilidad.
* Consideraciones:
- No hay soporte de UI.
- Los clientes dependen de la conectividad de la red.

* Aplicación multicapa que consta de:
- Capa de experiencia de usuario (presentación)
- Capa de negocio
- Capa de datos
* Un servicio es una interfaz que proporciona una funcionalidad
* Los servicios son consumidos

* Consideraciones generales de diseño
- Considere la posibilidad de utilizar un enfoque por capas para diseñar aplicaciones de servicios y evite el acoplamiento estrecho entre capas
- Diseñe operaciones de grano grueso (se centran en operaciones importantes de la aplicación).
- Diseñe contratos de datos para la extensibilidad y la reutilización.
- Diseñe servicios autónomos.
- Separe las preocupaciones de servicio de las de funcionamiento de la infraestructura.
- Evite el uso de servicios de datos para exponer tablas individuales en una base de datos.

# Aplicaciones web

* Definición:
Interfaz de aplicación basada en la web. Disponible sólo en la web. Accesible a través de un navegador de Internet. La lógica que reside del lado del servidor se suele estructurar en varias capas; por ejemplo la arquitectura a tres capas: presentación, negocio y datos. Generalmente accede una base de datos remota y consume servicios expuestos por otras aplicaciones.
* Beneficios:
- Amplio alcance UI basada en estándares para múltiples plataformas.
- Facilidad de despliegue y gestión de cambios.
* Consideraciones:
- Dependencia de conectividad continua en la red.
- Dificultad para proveer una UI enriquecida.

* Consideraciones generales de diseño
- Comprender cómo se comunicarán los componentes entre sí.
- Considere el almacenamiento en caché para minimizar los viajes de ida y vuelta del servidor.
- No pase datos sensibles en texto plano a través de la red.
- Diseñe su aplicación web para que se ejecute utilizando una cuenta con los mínimos privilegios.

# Modelo C4

- Se puede usar en sesiones de diseño iniciales o para documentar una arquitectura cuyo código ya existe.
- Trata de reducir la brecha entre el modelo y el código.
- Está basado en cuatro niveles:
    - Nivel de Contexto
    - Nivel de Contenedores
    - Nivel de Componentes
    - Nivel de Clases (Código)
- Usa una representación gráfica basada en cajas y líneas.
- Permite crear “mapas” del código con varios niveles de detalle (como cuando usamos Google Maps para acercarnos o alejarnos en un área de interés)

* Contexto
- Representa el panorama general del sistema.
- El sistema es el elemento central, los usuarios y otros sistemas se dibujan alrededor.
- Se enfoca en las personas y sistemas de software más que en las tecnologías.
- El sistema se considera una “caja negra”, es decir, que sólo nos interesan sus relaciones externas.
- Permite la comunicación con personas “no técnicas”.

Notación: 
- Persona = usuario
- Sistema = lo que se va a representar
- Sistema existente = otro sistema
- Relación = vínculo entre actores y/o sistemas
- Recuadro con línea discontinua = límites de la empresa


* Contenedores

- Representa una aplicación o un almacén de datos.
- Algo que necesita ejecutarse para que el sistema de software general funcione.
- Cada contenedor se puede desplegar/ejecutar por separado o en un entorno de ejecución.
- El diagrama de contenedores muestra la forma de alto nivel de la arquitectura de software y cómo se distribuyen las responsabilidades en ella.
- Permite la comunicación con desarrolladores y personal de soporte y operaciones.

Notación:
- Persona = usuario
- Contenedor = parte del sistema
- Sistema existente = otro sistema
- Relación = vínculo entre actores y/o sistemas
- Recuadro con línea discontinua = límites del sistema a representar
- BD = base de datos

* Componentes

- Agrupación de funcionalidades (componentes) relacionadas.
- Los componentes de un contenedor se ejecutan normalmente en el mismo espacio de proceso.
- Un componente NO es una unidad desplegable por separado.
- Facilita la comunicación con arquitectos y desarrolladores de software.

Notación:
- Componente = parte de un contenedor
- Relación = vínculo entre actores y/o sistemas
- Recuadro con línea discontinua = límites del contenedor a representar
- Sistema existente = otro sistema
- BD = base de datos

* Código 

- Muestra cómo se implementa el código.
- Se puede generar mediante herramientas como un IDE.
- Se recomienda presentar detalles para los componentes más importantes o complejos.
- Facilita la comunicación con arquitectos y desarrolladores de software.

Notación: 

- Notación gráfica de los diagramas de clases en UML, diagramas de relación de entidades o similares.

* Diagramas complementarios
- Diagrama del “paisaje” del sistema
- Diagrama dinámico
- Diagrama de despliegue

