# Estilo en capas

- Cada capa ejecuta un conjunto de operaciones especificas.
- La capa más externa se encarga de las operaciones de la interfaz de usuario.
- La capa más interna se encarga de comunicarse con el sistema operativo
- Las capas intermedias proveen servicios y funciones de software de aplicación.

1. Capa más externa: Se comunica con el usuario. Suelen ser graficas, pero no necesariamente lo son.
2. Capas intermedias: Encargadas de proveer partes de la solución.
3. Capas internas: Comunicación con el S.O.

CON: MVT

Externa: Templates
Media: Views
Interna: Model

Intención: respetar la comunicación entre las capas. Las que están a los lados.

Ayuda a evitar problemas de seguridad cuando se respetan las capas.

* Algunos patrones arquitectonicos son MVT y MVC.

TEMPLATE: HTML, CSS
VIEWS: Comprar, buscar, recomendar
Model: Las tablas
Datos: Sqlite

Se suelen tener 4 o 5 cinco capas:

1. Capa de presentación: Cómo se muestran las funcionalidades-
2. Capa de negoción: Como se realizan las funciones.
3. Capa de persistencia: Cómo se logra la interacción con los datos. ORM:: Es lo que convierte los objetos en tablas en Django.
4. Capa de datos: En donde se guarda la información.

# Estilo llamada/retorno

- Permite obtener una estructura fácil de modificar y escalar.

* Ejemplo de patrones arquitectonicos: 
    1. Cliente-servidor: Es común tener hardware. Tento el cliente cómo el servidor se llaman niveles. Es normal que dentro de los niveles haya capasa.
    Tipos de clientes: Web, movil, escritorio.
    Serivor: App y datos. Es donde se define la arq de las capas.

    Ejemplo: Con sistema web

    * Cliente
    - PC
    - Navegador
    - URL... (Que genera un request
    
    * Servidor
    - App y datos
    - Django
    - MVT + Datos (Genera response)

# Flujo de datos

- Se usa cuandos e deben trabajar con muchos datos y se necesitan transformar de alguna manera especifica.

- Hay dos tipos: 
1. Tuberías y filtros
    - Componentes (filtros) conectados (tubos)
    - Los filtros alteran el contenido de manera independiente esperando un tipo de datos de forma especifica y entregandolo de una manera en especifico.
    - Los tubos son los canales de conexión entre los componentes.
    - No se recomiendo cuando se requiere interactividad.


2. Procesamiento de lotes (Batch sequential)
    - Modelo secuencial de procesamiento de datos.
    - Es un paso a paso, hasta que no se dlle una ejecución en especifico no se puede pasar a la sgnte ejecución .
    - Usado en transacciones bancarias.
    - No proporciona interactividad.
    - Ejemplo: tomar un conjunto grande de archivos y estructurarlos para un formato en especial para una consulta posterior.
    - Que se procesen los datos durante las noches.

# Arquitectura centrada en datos

- En el centro hay un espacion de almacenamiento de datos.
- Todos los procesos y funciones acceden al centro para revisar los datos.
- Promueve la integralidad, es decir, que los componentes puedean ser cambiados con facilidad sin afectar los datos. 
- API's
- Para datos compartidos (De forma colaborativa).

- Tipos:

1. Repositorios
    - En el centro hay un repositorio de datos (Como un archivo o base de datos)
    - Los demás componentes acceden con frecuencia al repo de datos.

2. Pizarron:
    - Se envian notificaciones cada vez que haya un cambio en los cambios.
    - Coordina la transferencia de info entre los cleintes 
