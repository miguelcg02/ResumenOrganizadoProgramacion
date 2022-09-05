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

Supongamos que una aplicación Cliente/Servidor debe estar disponible
98% del tiempo (aproximadamente 358 días al año), pero si el servidor
sufre un daño, se estima que reestablecerlo toma días, en ese caso se
estaría incumpliendo el requisito no funcional relacionado con la
disponibilidad.

Para garantizar el cumplimiento del requisito se debe considerar un
servidor de respaldo (esclavo) que pueda responder a las peticiones si el servidor principal está inactivo.

Pero ... clonar los datos en el servidor de respaldo es costoso, por lo que se recomienda tener un ser un servidor independiente con la Base de Datos.

