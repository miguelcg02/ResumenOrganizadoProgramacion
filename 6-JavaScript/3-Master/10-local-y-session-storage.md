- Session se pierde una vez se cierra la pestaña
- LocalStorage mantiene la información aún cuando cierra la pestaña

```js
"use strict";

localStorage.setItem("nombre","pedro");
let nombre = localStorage.getItem("nombre");

console.log(nombre)

localStorage.removeItem("nombre")
```

```js
"use strict";

sessionStorage.setItem("nombre","pedro");
let nombre = sessionStorage.getItem("nombre");

console.log(nombre)

sessionStorage.removeItem("nombre")
```

* Con clear() se borra todo
