# filer

Sirve para iterar sobre un arreglo. Recibe una función y devuelve el contenido del arreglo, es como el in en python.

```js
let palabras = ["abc","man","pedo","bobo"]

palabras.filter(palabra => document.write(palabra + "<br>"))
```

```js
let palabras = ["abc","man","pedo","bobo"]

resultado = palabras.filter(palabra => palabra.length > 4)
```

