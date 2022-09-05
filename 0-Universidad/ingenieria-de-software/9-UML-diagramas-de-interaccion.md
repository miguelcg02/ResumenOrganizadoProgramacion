# Para que sirven los diagramas de interacción

- diseña el comportamiento del sistema
- Capta el comportamineto interactivo de un sistema
- Describe el flujo de mensajes dentro de un mensaje
- Presenta las interacciones entre el sistema y otros sistemas
- Sistema como secuencia de eventos ordenados por el tiempo

# Tipos de diagramas

- Diagrama de colaboración
- Diagrama de tiempo 
- Diagrama  global de interacion
- Diagrama de secuencias

# Diagrama de colaboración

- Como colaboran e interactuan los objetos entre si
- Centrado más en organización que en cronologia
- Hace enfasis en los mensaje que intercambian los objetos

# Diagrama de tiempos

- Respresenta el estado de un objeto en un momento determinado
- Muestra el tiempo que tarda cada paso de un proceso
- Permite identificar que pasos toman más tiempo para hallar oportunidades de mejora
- Es casi que uno de los últimos diagramas que se hacen-

# Diagrama global de interacciones

- Proporciona una vista global de las interacciones de un sistema
- Es una especialización del diagrama de actividades

* Actor: Entidad externa al sistema que interactua con el, el mariapalito
* Objeto y linea de vida, las lineas y los objetos
* Activación: En que momento se hace uso del objeto en un momento dado, el rectangulo
* Mensaje: Va de la linea de vida de un objeto a la de otro, un objeto puede enviarse un mensaje a si mismo y puede ser:
    1. Síncrono. ------|>
    2. Asincrono. ---------->
    3. Respuesta. - - - - - >
    4. creación. -----<< create >>------> también xd
    5. Eliminación. --------->X

* Ciclo: El loop reprense una secuencia
* Alternativas: Con el if else, con un cuadrado de dos cajones.