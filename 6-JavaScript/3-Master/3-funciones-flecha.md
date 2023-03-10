# Funciones flechas

* Estrucutra

```js
const saludar = () =>{
    console.log("hola");
}
```

* Si hay solo una expresión de una linea la retorna y los parentisis son opcionales para solo un parametro

``` js

const saludar = res=> nombre = res;

resultado = saludar("Dalto");

console.log(resultado)
```

* No son adecuadas para ser usadas como métodos y no pueden ser usadas cómo constructores

```js
"use strict";

const objeto = {
    nombre:"lucas";
    saludar: ()=>{console.log(`Hola ${this.nombre}`)} //ESTO ESTA MAAAL, NO DEBE SER FLECHA PORQUE EL THIS NO EXISTE EN FUNCIONES FLECHA PORQUE EL THIS PASARA A REFERIRSE AL window
}

objeto.saludar()
```