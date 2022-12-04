# metodos classList

1. Añadir una clase a una tag

```js
const titulo = document.querySelector(".titulo");

titulo.classList.add("grande");
```

2. Remover una clase

```js
const titulo = document.querySelector(".titulo");

titulo.classList.remove("grande");
```

3. Devuelve la clase del tipo especificado

```js
const titulo = document.querySelector(".titulo");

let valor = titulo.classList.item(1);

document.write(valor);
```

4. Pregunta si tiene una clase

```js
const titulo = document.querySelector(".titulo");

let valor = titulo.classList.contains("grande");

document.write(valor);
```

5. En caso de que tenga una clase la quita, y en caso de que no la pone, ademas tiene retorno booleano

```js
const titulo = document.querySelector(".titulo");

titulo.classList.toggle("grande");
```

