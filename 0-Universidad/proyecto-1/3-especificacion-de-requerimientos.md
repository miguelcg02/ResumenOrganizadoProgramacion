# 1. Introduction

1.1 Purpose: Definir la finalidad del software que se va a especificar.

- Ej: The main purpose of this document is to provide a working example of a Software
Requirements Specification (SRS) based on ISO/IEC/IEEE 29148:2018 standard.

1.2 Scope: Describir el alcance del software al identificar el producto que se va a producir por su nombre, explicando que hara el producto, describir la aplicación que se especifica, incluyendo los beneficios, objetivos y metas.

- Ej: This document specifies requirements for a simple application for requirements
management of software and system products.

The application allows users to:
• Capture requirements specifications
• Manage requirements using custom attributes
• Set up requirements traceability
• Browse the requirements traceability matrix
• Comment and review requirements
• Filter and search requirements
• Import requirements from MS Word or Excel
• Export requirements to DOCX, XLSX, HTML, or CSV
• Analyze requirements coverage and impact of changes
• Print requirements specifications

The application stores documents as human readable files with open file format.

The application runs offline without connection to any server

# 1.3 Product Overview ?

1.3.1 producto perspective: Definir la relación del sistema con otros productos relacionados

Describa cómo funciona el software dentro de las siguientes limitaciones:
a) Interfaces del sistema;
b) Interfaces de usuario;
c) Interfaces de hardware;
d) Interfaces de software
e) Interfaces de comunicaciones;
f) Memoria;
g) Operaciones;
h) Requisitos de adaptación del sitio.

* a: Interfaces del sistema/System interface

Enumere cada interfaz del sistema e identifique la funcionalidad del software para cumplir el requisito del sistema y la descripción de la interfaz para que coincida con el sistema.

Ej: The application runs in the latest version of Chrome or Firefox browser on Windows, Linux and Mac.

* b: Interfaces de usuario/USer interfaces

Las características lógicas de cada interfaz entre el producto de software y sus usuarios.

Ej: The application GUI provides menus, toolbars, buttons, panes, containers, grids allowing for easy control by a keyboard and a mouse.

* c: Interfaces de hardware/ Hardware interfaces

Especificar las características lógicas de cada interfaz entre el producto de software y los elementos de hardware del sistema. Esto incluye las características de configuración (número de puertos, conjuntos de instrucciones, etc.). También incluye cuestiones como los dispositivos que se van a admitir, el modo en que se van a admitir y los protocolos.

Ej de una parte: terminal support may specify full-screen support as opposed to line-by-line support 

* d: Interfaces de software/Software interfaces

Especifique el uso de otros productos de software necesarios (por ejemplo, un sistema de gestión de datos, un sistema operativo
o un paquete matemático), y las interfaces con otros sistemas de aplicación.

Para cada producto de software requerido, especifique:
a) Nombre;
b) Mnemónico;
c) Número de especificación;
d) Número de versión;
e) Fuente.

Ej:  The application allows import a structured MS Word document via HTML data format.
The application allows populating a MS Word document with project data via HTML data format.
The application allows import / export a list of requirements from / to MS Excel sheet via CSV data format.
The application stores project data in JSON format to enable easy integration with 3rd party applications.

* e: Interfaces de comunicaciones /Communications interfaces

Especifique las distintas interfaces de comunicación, como los protocolos de red local.

* f: Memoria/Memory

Especifique las características y límites aplicables a la memoria primaria y secundaria.

* g: Operaciones/operations

Especifique las operaciones normales y especiales requeridas por el usuario, tales como
a) Los distintos modos de operaciones en la organización del usuario (por ejemplo, operaciones iniciadas por el usuario);
b) Los periodos de operaciones interactivas y los periodos de operaciones desatendidas;
c) Las funciones de apoyo al procesamiento de datos;
d) Las operaciones de copia de seguridad y recuperación

* h: Requisitos de adaptación del sitio/Site adaptation requirements

a) La definición de los requisitos para cualquier dato o secuencia de inicialización que sean específicos de un sitio determinado,
misión o modo operativo (por ejemplo, valores de red, límites de seguridad, etc.);
b) La especificación de las características relacionadas con el emplazamiento o la misión que deben modificarse para adaptar el software a una
instalación concreta.

1.3.2 Product functions: 

Proporcione un resumen de las principales funciones que realizará el software. Por ejemplo, un SRS para un programa de contabilidad puede utilizar esta parte para tratar el mantenimiento de las cuentas de los clientes, los extractos de clientes y la preparación de facturas sin mencionar la gran cantidad de detalles que requiere cada una de esas funciones.

1.3.3 User characteristics:

Describa las características generales de los grupos de usuarios previstos del producto, incluidas las características que pueden influir en la usabilidad, como el nivel educativo, la experiencia, las discapacidades y los conocimientos técnicos.

1.3.4 Limitations: 

Proporcione una descripción general de cualquier otro elemento que limite las opciones del proveedor, incluyendo por ej:

a) Políticas normativas;
b) Limitaciones de hardware (por ejemplo, requisitos de sincronización de señales);
c) Interfaces con otras aplicaciones;
d) Funcionamiento en paralelo;
e) Funciones de auditoría;
f) Funciones de control;
g) Requisitos de lenguaje de orden superior;
h) Protocolos de intercambio de señales (por ejemplo, XON-XOFF, ACK-NACK);
i) Requisitos de calidad (por ejemplo, fiabilidad)
j) Carácter crítico de la aplicación;
k) Consideraciones de seguridad y protección.

1.4 Definitions Terminos tecnicos con su definición.

Ej: 
Custom Attribute: Additional requirement property capturing additional requirements properties such as requirements source, status, priority, verification method, fit criterion,
Document: A structured requirements specification capturing textual requirements for a given product or service.
Link: A directed association between related requirements allowing to analyze requirements coverage, gaps and impact of changes.
Link Type: Property of traceability links allowing to analyze links with different semantic independently, e.g., satisfaction and verification links.

# 2. References ??

# 3. Specific requirements

3.1 External interfaces: Defina todas las entradas y salidas del sistema de software. La descripción debe complementar las descripciones de la interfaz.

Cada interfaz definida debe incluir el siguiente contenido:
a) Nombre del elemento;
b) Descripción de la finalidad;
c) Fuente de entrada o destino de salida;
d) Rango válido, precisión y/o tolerancia;
e) Unidades de medida;
f) Temporización;
g) Relaciones con otras entradas/salidas;
h) Formatos/organización de la pantalla;
i) Formatos/organización de las ventanas;
j) Formatos de datos;
k) Formatos de comandos;
l) Mensajes finales

3.2 Functions: Definir las acciones fundamentales que deben tener lugar en el software al aceptar y procesar las entradas y al procesar y generar los resultados, incluyendo

a) Comprobaciones de validez de las entradas
b) La secuencia exacta de las operaciones
c) Respuestas a situaciones anormales, incluyendo
    1) Desbordamiento
    2) Facilidades de comunicación
    3) Tratamiento de errores y recuperación
d) Efecto de los parámetros
e) Relación de las salidas con las entradas, incluyendo
    1) Secuencias de entrada/salida
    2) Fórmulas de conversión de entradas a salidas

Puede ser conveniente dividir los requisitos funcionales en subfunciones o subprocesos. Esto no
Esto no implica que el diseño del software también se divida de esa manera.

3.3  Usability requirements: Los requisitos y objetivos de usabilidad del sistema de software incluyen criterios medibles de eficacia, eficiencia y satisfacción en contextos específicos de uso

3.4 Performance requirements: Especifique los requisitos numéricos, tanto estáticos como dinámicos, impuestos al software o a la interacción humana con el software en su conjunto. Los requisitos numéricos estáticos pueden incluir lo siguiente: 
a) El número de terminales que deben soportarse; 
b) El número de usuarios simultáneos que deben soportarse; 
c) La cantidad y el tipo de información que debe manejarse. Los requisitos numéricos estáticos se identifican a veces en una sección separada titulada Capacidad. 

Los requisitos numéricos dinámicos pueden incluir, por ejemplo, el número de transacciones y tareas y la cantidad de datos que deben procesarse en determinados periodos de tiempo, tanto en condiciones normales como en condiciones de carga de trabajo máxima. Los requisitos de rendimiento deben establecerse en términos mensurables. Por ejemplo, el 95 % de las transacciones deberá procesarse en menos de 1 segundo.

3.5 Logical database requirements: Especificar los requisitos lógicos de cualquier información que se vaya a colocar en una base de datos, incluyendo:

a) Tipos de información utilizados por diversas funciones;
b) Frecuencia de uso;
c) Capacidades de acceso;
d) Entidades de datos y sus relaciones;
e) Restricciones de integridad;
f) Requisitos de conservación de los datos

3.6 Design constraints: Especificar las restricciones en el diseño del sistema impuestas por las normas externas, los requisitos reglamentarios o las limitaciones del proyecto

3.7 Software system attributes: Especifique los requisitos derivados de las normas o reglamentos existentes, incluyendo:

a) Formato del informe;
b) La denominación de los datos;
c) Procedimientos contables;
d) Seguimiento de la auditoría.

3.8 Supporting information: El SRS debe contener información adicional de apoyo, incluyendo

a) Ejemplos de formatos de entrada/salida, descripciones de estudios de análisis de costes o resultados de encuestas a usuarios;
b) Información de apoyo o de fondo que pueda ayudar a los lectores del SRS;
c) Una descripción de los problemas que debe resolver el software;
d) Instrucciones especiales de empaquetado del código y de los soportes para cumplir los requisitos de seguridad, exportación, carga inicial u otros.
requisitos de seguridad, exportación, carga inicial u otros.

El SRS debe indicar explícitamente si estos elementos de información deben considerarse parte de los requisitos.

# Verification

Proporcione los enfoques y métodos de verificación previstos para calificar el software. Los elementos de información para
verificación se recomiendan de forma paralela a los elementos de información de los subapartados 3.X

