# Fetch

- Forma de trabajar con AJAX
- Basado en promesas encapsuladas

* GET

```js
peticion = fetch("URL") // Aqui ya tiene la promesa por defecto de un GET
// peticion.then(res=>console.log(res)) //Es asincrona (Cuando tenga el resultado se ejecuta)
peticion
    .then(res=>res.text()) //Primero se obtiene el texto
    .then(res=>console.log(res)) //luego se imprime

peticion
    .then(res=>res.json()) //Primero se obtiene el texto
    .then(res=>console.log(res)) //luego se imprime
```

* POST

```js
peticion = fetch("URL",{
    method: "POST"
    body: JSON.stringify({
        "nombre" : "Lucas"
        "apellido": "dalto"
    }),
    headers: {"content-type": "application/json"}
}) // Aqui ya tiene la promesa por defecto de un GET
// peticion.then(res=>console.log(res)) //Es asincrona (Cuando tenga el resultado se ejecuta)
peticion
    .then(res=>res.text()) //Primero se obtiene el texto
    .then(res=>console.log(res)) //luego se imprime

peticion
    .then(res=>res.json()) //Primero se obtiene el texto
    .then(res=>console.log(res)) //luego se imprime
```