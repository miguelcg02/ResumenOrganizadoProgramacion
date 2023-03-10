# Strict mode - use strict

- Convierte errores de Js en excepciones.
- Mejorando la optimización de los errores y consigue mejores tiempos de ejecución.
- Evita sintaxis usadas en posteriores a ES6.
- No permite que el programador realize una "mala sintaxis".

* Para uso global

```js
"use strict";

nombre = "lucas"; //Tira error
let nombre = "lucas"; //No tira error
```

* Crear una propiedad no reescribible, solo para ver

```js
"use strict";

const obj = {};

Object.defineProperty(obj,'nombre',{value:"pedro",writeable: false});
```

* No permitir agregar más extensiones a un objeto

```js
"use strict";

const obj = {nombre:"lucas"};

Object.preventExtensions(obj);
```

* No poder agregar más propiedades a un String

```js
"use strict";

const str = "Lucas Dalto";

// str.canal = "Soy dalto" //Este tira error en modo estricto
```

* No existen las multiples varibales en una función

```js
"use strict";

function hablar (texto,texto){ //Tira error
    console.log(texto)
}

hablar("pedro","pedro")
```

* No hay de delete en objetos o variables, delete debe ser usado para borrar propiedades

```js
"use strict";

let variable = "nombre";

delete variable; //Error
```

* Las palabras reservadas no pueden ser usadas para declarar variables

```js
"use strict";

let package = "pedro"; //Error
```

* Cambiar el this xd

* No existe el with y los numeros octales empiezan con un 0o adelante

```js
"use strict";

console.log(0o23);
```

* arguments y eval no se pueden declarar

