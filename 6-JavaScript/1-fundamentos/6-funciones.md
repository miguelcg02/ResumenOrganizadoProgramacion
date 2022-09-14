# Con flecha

```js
let saludar = (nombre)=>{
    alert("Hola "+nombre);
    return "Se saludo a "+nombre;
}

let res = saludar();
document.write(res);
```

# Por estructura

```js
function saludar(){
    alert("Hola");
}

saludar();
```

# Por asignación

```js
saludar = function(){
    alert("Hola");
}

saludar();
```

# Con retorno

```js
function saludar(){
    alert("Hola");
    return "Se saludo";
}

let res = saludar();
document.write(res);
```
# Con parametro


```js
function saludar(nombre){
    alert("Hola "+nombre);
    return "Se saludo a "+nombre;
}

let res = saludar();
document.write(res);
```