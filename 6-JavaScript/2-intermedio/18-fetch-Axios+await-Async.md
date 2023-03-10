# crear funciones que hagan solicitudes

* Con fetch

```js
const getName = async ()=>{
    let peticion = await fetch("URL")
    let resultado = await peticion.json()
    console.log(resultado)
}

getName()
```

* Con Axios

```js
const getName = async ()=>{
    let resultado = await axios("URL")
    console.log(resultado)
}

getName()
```