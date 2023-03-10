# JSOM JavaScript Object Notation

- Deserialización: En formato de objeto

```js
{"variable1": "Pedro", "variable2": "Jorge"}
```

- Serialización: En formato de texto

```js
'{"variable1": "Pedro", "variable2": "Jorge"}'
```

Sirve para poder información

* Para serializar: 

```js
const deserializado = {"variable1": "Pedro", "variable2": "Jorge"};
const serializado = JSON.stringfy(deserializado)
```

* Para Deserializar: 

```js
const serializado = '{"variable1": "Pedro", "variable2": "Jorge"}';
const deserializado = JSON.parse(serializado)
```

* JSON Polyfill

Las versiones más viejas no soportan JSON entonces toca crear un Polyfill