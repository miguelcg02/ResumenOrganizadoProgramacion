# 1. Para que sirve la arquitectura
# Nivlees de abstracción

* Arquitecturas en pequeño
    - Se interesa por la arquitectura de programas individuales
    - En este nivel nos concentramos en la forma en que el programa individual se separa en componentes.
    - Para un sistema particular.

* Arquietectura en grande
    - Se interesa por la arquitectua de sistemas empresarieles complejos qu eincluyent otros servicios o sistemas.

Ventas: Reutilización a gran escala

# Decisiones

- Ver restricciones
- Ver alternativas
- Que es lo que se pretende tener de producto final
- Que decisoines debo tomar

# 2. vistas de arquitectura.

- Cada vista refleja algo particular.
- Saber que se esta representando el mismo sistema de una perspectiva diferente.

# Vistas arquitectónicas

- Una perspectiva
- Vamos a usar modelo 4 + 1 vistas y otra llamada C4.


# Modelo de 4 + 1 vistas

* Vista lógica
    - Se centra en las funcionalidades del sistema.
    - Indica las abstracciones clave en el sistema como objetos o clases de objeto.

* Vista del proceso
    - Muestra el comportamiento del sistema en tiempo de ejecución.
    - Permite hacer juicios acerca de las caracteristica no funcionales.
    - Concurrencia y sincronización.

* Vista física
    - Representa los componentes y sus relaciones
    - Hardware + software: Conexión física

* Vista de desarrollo
    - Muestra el como se implementa el sistema
    - Perspectiva del programador.
    - Librerias

* Vista + 1 /  Integración / de escenarios
    - Integrar las 4 vistas en una

# ¿Quien es el stakeholder interesado en cada una de las vistas?

- Lógica: Usuario final.
- Física: Ingeniero de sistemas, integrador.
- Procesos: Integrador. A los devs, analista.
- Desarrollo: Programador, arquitecto.
- Integración/Escenarios: Todos xd.

# Que UML usar para cada vista

- Lógica: Diagrama de clases.
- Proceso: Diagrama de secuencia, digrama de colaboración, diagrama de actividad.
- Desarrollo: Diagrama de componentes, diagrama de paquetes.
- Física: Diagrama de despliegue.
- Integración/Escenarios: casos de uso

# Diagrama de despliegue (Para vista física)

- Es UML
- Tienen nodos
- Nodo de tipo memoria
- Nodo de tipo dispositivo
- Uniddes de procesamiento

* Nodo: 
- Es un objeto físico de ejecución que representa un recurso computacional, que generalmente tiene memoria, y a menudo cuenta con capacidad de procesamiento.
- Los nodos pueden tener estereotipos para distinguir diferentes tipos de recursos, tales como CPU (Unidad central de procesamiento), dispositivos, y memorias.
- Cada nodo debe tener un nombre que lo distinga de los demás.
- Dentro de los nodos estan los componentes.

* Ejemplos de Nodo
- Computador con procesadores
- Otros dispositivos:
    - Impresora
    - Lector de códigos de barras
    - Dispositivos de comunicación

* Nodo de tipos dispositivo: Generalmente se usan estereotipos para identificar el tipo de dispositivo

* Relaciones: Van protocolos de comunicación
- Los nodos se conectan mediante asociaciones de
comunicación.
- Estas asociaciones indican:
    - Algún tipo de ruta de comunicación entre los nodos.
    - Los nodos intercambian objetos o envían mensajes a través de esta ruta.
- El tipo de comunicación se identifica con un estereotipo que indica el protocolo de comunicación o la red.

* Artefacto: Eso último que se necesita para que funcione, MySQL, HTML 5 o Website.

# Resumen de los elementos del diagrama de despliegue

- Nodos: Dispositivo, memorias, CPU
- Relaciones: Por protocolos 
- Artefacto: Es el archivo que corre. (Si se detallan los componentes, es mejor borrar el artefactp)
- Componentes: Es más especifica.

# Diagrama de componentes

- Ilustra los componentes de software que serán usados para construir el sistema (módulos de código fuente, bibliotecas, módulos ejecutables, etc.)
- Ilustra cómo interactuarán los componentes para que el sistema funcione de forma adecuada.
- Se puede construir a partir del Diagrama de Clases.
- Está asociado en gran medida al lenguaje de programación que se utilizará para desarrollar el sistema.