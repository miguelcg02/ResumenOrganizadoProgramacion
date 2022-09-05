
https://app.diagrams.net/#G1JSVJDYDlRXGQHqfImKNCNx6iPvtpe2XO

# Modelos

* Diagrama de contexto: 
    - NO UML
    - Relacionar el sistema con diferentes actores. 
    - Se usa para conocer donde estamos. 
    - En cascada se hace en el analisis

* Casos de uso:
    - Si UML.
    - Representa los actores.
    - Indicar las funcionalidades del sistema. Interacciones de usuario con el sistema
    - Lo que hace el usuario directamente.
    - Entre analisis y diseño.
    - Se deben nombrar como acciones.
    - Se especifica mejor el sistema.
    - A cada caso de uso se le asocia una descripción. Que puede ser un texto en orden o con un diagrama de actividades.

* Estados:
    - Si UML.
    - Punto  de inicio, transiciones, super estados, subestados, condición para pasar de un estado a toro.
    - Bajo que condiciones esta el sistema en un momento dado.
    - Es más independiente a los otros diagramas.
    - Identificar los estados del sistema.
    - Se hace en etapa de diseño

* Actividades:
    - Si UML.
    - No tienen estados, si no actividades.
    - Vinculados a las acciones.
    - Cada caso de uso tiene una secuencia. El flujo de acciones.
    - Se hace en etapa de diseño.

* Flujo:
    - No UML
    - Es muy parecido al de actividades.

* Interacción (Los 4 son de diseño)
    * Colaboración:
        - Si UML
        - Se hace en etapa de diseño
        - Interactuan actores (Que vienen del diagrama de contexto)
        - Solo se concentran en una parte de la funcionalidad, es muy puntual.
        - Viene también del diagrama de clases (Por las bolitas)

    * Timepos:
        - Si UML
        - Sale del de estado
        - Muestra los estados y cuanto tiempo pasan en ese estado

    * Global de interacciones:
        - Si UML
        - Relacionar dos diagramas

    * Secuencia:
        - Si UML
        - Viene del de clases
        - Depronto un poco del de actividades, el de casos de uso y mucho del de clases

* Modelo de dominio:
    - No UML

* Clases
    - Si UML
    - Viene del de dominio

# TEORIA

### Software como producto

* Globalismo: Cualquier cambio hecho al sistema, por pequeño que sea, altera el sistema como un todo.
* Entropía: Con el correr del tiempo tiende a deteriorarse. Ese deterioro ocurre cuando no hay suficiente intercambio de información del sistema con el entorno.
* Homeostasia: Adaptabilidad del sistema. Todo sistema tiende a adaptarse a su medio externo.

### Ingeniería de Software (IS)

La Ingeniería de Software es la aplicación de un enfoque sistemático, disciplinado y cuantificable para el desarrollo, operación y mantenimiento de software. SWEBOK (2003).


### Calidad de software

La calidad no sólo tiene que ver con lo que hace el software, debe incluir el comportamiento del software mientras se ejecuta, la estructura, organización de los programas del sistema y la documentación asociada.

* Atributos de calidad esenciales:
    - Mantenibilidad: El software debe ser escrito de tal forma que pueda evolucionar.
    - Confiabilidad y Seguridad: No debe causar daño físico ni económico en caso de falla.
    - Eficiencia: No debe desperdiciar los recursos del sistema. Capacidad de respuesta, tiempo de procesamiento, uso de memoria, etc.
    - Aceptabilidad: Debe ser comprensible, utilizable y compatible con otros sistemas.

### Requisito de software

1. Una condición o capacidad con la cual un sistema software debe ser conforme.
2. Requisito Funcional: Un requisito que especifica cómo la solución interactúa con el mundo exterior.
3. Requisito No-Funcional: Un requisito que especifica los atributos de calidad de la solución

### Ingeniería de Requisitos (IR)

Enfoque sistemático y disciplinado para la especificación y gestión de requisitos con los siguientes objetivos:
* Conocer los requisitos relevantes, lograr consenso entre los interesados, documentarlos de acuerdo a las normas dadas y gestionarlos de forma sistemática.
* Comprender y documentar los deseos y necesidades de los implicados.
* Especificar y gestionar los requisitos para reducir al mínimo el riesgo de tener un sistema que no cumpla con los deseos y necesidades de los implicados.

### Stakeholder

Un implicado de un sistema es una persona o una organización que tiene influencia (directa o indirecta) sobre los requisitos del sistema.

### Requisitos del negocio

* Metas, objetivos de la organización a un alto nivel
* Representan beneficios tangibles para la organización
* Motivantes para que se implementen soluciones
* No necesariamente están asociados a software

### Reglas del negocio

* Política corporativa, estándar de industria, norma, regulación de ley que define o limita algún aspecto del negocio.
* No es un requisito de software en sí mismo, pero es el origen de varios tipos de requisitos.
* Las reglas de negocio afectan los procesos de negocio.
* No se deben confundir con las restricciones técnicas.

### Requisitos de los interesados (usuarios)

* Describen los objetivos o tareas que distintos usuarios deben ser capaces de realizar con el producto y producirán valor para alguien.
* Están centrados en las necesidades y deseos de los interesados o usuarios, no en las capacidades que el software les ofrece.
* Incluyen atributos o características del producto.


### Atributos de calidad

* Son cualidades o propiedades de calidad que se deben satisfacer tales como: rendimiento, seguridad, disponibilidad, etc.
* Se manifiestan de forma indeterminada o no medible por parte de los interesados.
* Son el origen de requisitos no funcionales.
* Modelos de atributos de calidad: ISO, FURPS, SEI

### Requisitos funcionales

* Especifican los comportamientos observables que un sistema ofrece o exhibe bajo ciertas condiciones específicas.
* Describen lo que los desarrolladores deben implementar para permitir a los usuarios realizar sus tareas.
* Se describen en la forma tradicional del “sistema debe”, “deberá” o “debería”

Ejemplos:
• Si el pasajero no indica una preferencia de asiento, el sistema de reservas deberá asignar al pasajero, un asiento que no se encuentre ocupado por otro pasajero.
• El sistema deberá permitir consultar a un profesor una evaluación de un curso específico al cual pertenece.
• El sistema deberá permitir imprimir al pasajero una tarjeta de embarque para el vuelo en el que ha realizado el check-in.

### Requisitos no funcionales o de calidad

* Describe un servicio o capacidad que el sistema debe proveer y que se asocian atributos de calidad y restricciones de diseño e implementación.
* Influyen en el diseño y arquitectura, incluso más que los requisitos funcionales.
* Deben ser precisos, medibles y finitos.

Ejemplos:
• El sistema tendrá un disponibilidad promedio de 97.7% considerando 1 día del año para mantenimiento y reparación.
• Si un cliente realiza una consulta en un momento pico de operación, la respuesta a la consulta debe ser dada en un tiempo menor o igual a 4 segundos.
• Un cliente deberá poder realizar el proceso de check-in de un vuelo en un tiempo inferior o igual a 1 minuto sin que el sistema presente más de 4 pantallas distintas.

### Interfaces externas

Es una descripción de una conexión entre el sistema y un usuario, otro sistema, o un dispositivo de hardware.

### Restricciones

* Son limitaciones impuestas a las opciones disponibles para el desarrollador ya sea para el diseño o para la implementación de solución.
* Las restricciones pueden ser impuestas por interesados externas, por otros sistemas que interactúan con el que se está creando o por otras actividades del ciclo de vida de su sistema
* Son de obligatorio cumplimiento (mandatorios).
* Pueden ser de diseño, de arquitectura, de codificación, de
pruebas.

# Modelado y diagramas

### Modelado ¿Que es modela?

* Dominio de información del problema
* Funciones que realizará el software
* Comportamiento del software
* Arquitectura del sistema
* Datos
* Interfaces de comunicación
* Interfaz de usuario

### Modelado ¿Con qué se modela?

Algunas herramientas/lenguajes de modelado:
* Diagrama de flujo
* Diagrama de contexto
* Diagramas UML (Casos de uso...)
* Mockups

### Que es UML

UML (Unified Modeling Language) es un lenguaje
gráfico que permite
* Visualizar (expresar de forma gráfica para que otro lo pueda entender)
* Especificar (indicar las características de un sistema antes de
su construcción)
* Construir (desarrollar el sistema a partir de los diseños)
* Documentar (dejar evidencia sobre el desarrollo del sistema)
sistemas.

### Que no es UML

* No es un lenguaje de programación.
* No es un método de desarrollo, no indica cómo pasar
del análisis al diseño y de éste al código.
* No es una serie de pasos que llevan a producir código
a partir de unas especificaciones.
* No es dependiente del ciclo de desarrollo que se vaya
a seguir.

### Diagramas de estructura

Muestran la organización de un sistema (estructura estática), en términos de los componentes que constituyen dicho sistema y sus relaciones. Son importantes y necesarios cuando se diseña la arquitectura del sistema.
* Diagrama de Clases
* Diagrama de Estructura compuesta
* Diagrama de Componentes
* Diagrama de Despliegue
* Diagrama de Objetos
* Diagrama de paquetes

### Diagramas de Comportamiento

Muestran el comportamiento dinámico del sistema.
Permiten representar los cambios de estado y los flujos
de mensajes a lo largo del tiempo.
* Diagrama de Actividad
* Diagrama de Casos de Uso
* Diagrama de Máquina de estado
* Diagrama de Interacción:
    * Diagrama de Secuencia
    * Diagrama de Comunicación
    * Diagrama Global de Interacción
    * Diagrama de Tiempos



