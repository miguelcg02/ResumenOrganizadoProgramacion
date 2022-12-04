# Proxy

- Tipo: estructural
- Tiene cómo objetivo crear un envoltorio que permita tener el acceso al objeto final que nostro necesitamos manipular. Encapsula la complejidad de un objetivo en un envoltorio (clase intermediaria).
- Esta clase intermediaria puede delegar la información o el rol
- Si se quiere cambiar una funcionalidad se puede apoyar desde una interfaz
- El clinete usa el proxy para llegar al objeto final
- Permite facilitar el agregar funcionalidades intermedias sin alterar las clases originales
- Permite trabajar con diferentes interfaces

# Prototype

- Tipo: Creación
- Tiene el objetivo de crear una nueva instancia con los valores clonados de otra instancia.
- Permite crear copias facilmente
- Sirve mucha para realizar pruebas con objetos muy robustos y no alterarlos

# Estrategia

- Tipo: Comportamiento
- Definir familias de algoritmos que son independientes de los clientes que esten usando.
- Permite cambiar facilmente el conjunto de algoritmos que se van a utilizar de forma dinamica. 