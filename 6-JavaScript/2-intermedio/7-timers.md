# settimeout

```js
const temporizador = setTimeout(()=>{
    document.write("hola")
},2000) //A los 2seg ejecuta la funcion

clearTimeout(temporizador) //Lo termina, lo mata
```

# setInterval()

```js
setInterval(()=>{
    document.write("hola")
},2000) //Ejecuta esta función cada 2segundos

setTimeout(()=>{
    clearInterval(intervalo)
},7000)
```

