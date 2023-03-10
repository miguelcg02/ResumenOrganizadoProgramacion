# Prototipos

- Los objetos no tienen prototipo
- prototypechain: Como un prototipo tiene otro protitpo dentro (Number -> object)

* Acceder a los prototipos que nosotros creamos

```js

let variable = "dato";

console.log(variable.prototype)
```

* Acceder a los prototipos que ya estan creados

```js

let variable = "dato";

console.log(variable.__proto__)
```

Con function nosotros creamos el prototipo y para acceder al proto es de esta manera:

```js

let variable = function(){};

console.log(variable.prototype.__proto__)
```

- Un protitpo definido en su codigo fuente es mutable.
- Es en si mismo un objeto, asi como otros.
- Tiene una existencia física en la memoria.
- Puede ser llamado y moficiado.
- Pueder ser visto como un modelo ejemplar de una familia objeto.
- Un objeto hereda propiedades (Valores y metodos) de su prototipo.
- Cuando se crea una clase, se esta heredando el prototipo, no creandose. Por eso se accede a sus propiedades con __proto_ _

* Sobreescribir __proto_ _

```js
class Obj = {
    constructor(){};
    hablar(){
        console.log("hola")
    }
}

const objeto = new Obj();

objeto.__proto__.hablar = () =>{
    console.log("Modificado afuera")
}
```

* Heredar prototipos

```js
class Obj = {
    constructor(){};
    hablar(){
        console.log("hola")
    }
}

const objeto = new Obj();

let arr = []

arr.__proto__ = objeto;

arr.hablar()
```

ó

```js
class Obj = {
    constructor(){};
    hablar(){
        console.log("hola")
    }
}

const objeto = new Obj();

let arr = []

arr.__proto__ = objeto.__proto__;

arr.hablar()
```

El primero hereda modificaciones de afuera de la instancia del objeto y el segundo la forma pura