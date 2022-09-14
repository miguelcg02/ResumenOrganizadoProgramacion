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

