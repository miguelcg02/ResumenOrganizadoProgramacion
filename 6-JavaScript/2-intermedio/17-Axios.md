# axios

- Basado en promesas con AJAX
- Con Axios en un fetch sin encapsular

```js
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
```

* GET

```js
axios.get("informacion.txt")
    .then(res=>console.log(res.data))
```

* POST

```js
axios.post("informacion.txt",{
    "nombre":"lucas",
    "apeelido":"dalto"
})
    .then(res=>console.log(res.data))
```