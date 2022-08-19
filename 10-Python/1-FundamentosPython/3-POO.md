# Clases

```
class Auto():
    marca = ""
    modelo = 0
    placa = ""
```

# Crear objeto

```
taxi = Auto()
```

# atributos

```
print(taxi.marca)
```

# funciones POO

Se debe poner la palabra self en las funciones creadas

```
class Matematica:
    def suma(self):
        self.n1 = 2
        self.n2 = 3
```

# __init__

Es como el constructor

```
class Ropa:
    def __init__(self):
        self.marca = 'willow'
        self.tall = 'M'
        self.color = 'rojo'
```

```
class Calculadora:
    def __init__(self,n1,n2):
        self.suma = n1+n2
        self.resta = n1-n2
        self.producto = n1*n2
        self.division = n1/n2

operacion = Calculadora(3,4)
print(operacion.suma)
```

# funciones para atributos

1. getter (traer el dato)

```
class Persona:
    edad = 17
    nombre = 'victor'

doctor = Persona()

print(getattr(doctor,'edad'))
```

2. hasattr (saber si existe un atributo o no creado, tira un true or false)

```
class Persona:
    edad = 17
    nombre = 'victor'

doctor = Persona()
print(hasattr(doctor,'edad'))
```

3. setaatr (cambiar un valor)

```
class Persona:
    edad = 17
    nombre = 'victor'

doctor = Persona()
setattr(doctor,'nombre','Manuel')
```

4. delattr (eleminar un atributo)

```
class Persona:
    edad = 17
    nombre = 'victor'

doctor = Persona()
delattr(Persona,'pais')
```

# Herencia

```
class NombreSubClase (NombreclaseSuperior):

class claseBase:
    cuerpo de la clase base

class DerivadoClase (claseBase):
    cuerpo de clase derivada
```
ej:

```
class Pokemon:
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
    
class pikachu (pokemon):
    def ataque(self,tipoataque):
        return 'ataque'


nuevo_pkoemon = pikachu('boby','electrico')
```

# Herencia multiple

```
class Base_uno:
    campo de la clase base

class Base_dos:
    campo de la clase base

class DerivadoMultiple (Base_uno,Base_dos):
    campos clase derivada
```

# __repr__

determina los valores importante para retornarlos, es como el @String en java

```
def __repr__(self):
```

# @classmethod

Para detrminar clases pero que sean independientes (unicos)

```
@classmethod
def Pastel_chocolate(cls):
    return cls(['harina','leche','chocolate','huevo'])
```

# @staticmethod

Pueden ser llamados sin tener una instancia de la clase, además este tipo de métodos no tienen acceso al exterior

```
@staticmethod
def tamaño_are(A):
    return A** 2 * math.p1
```

# polimorfismo

mismo nombre diferentes valores en los parametros.