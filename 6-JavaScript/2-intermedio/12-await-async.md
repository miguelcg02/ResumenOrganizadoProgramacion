# await async

Es para trabajar con funciones asincronas de forma ordenada, que sin importar de que un dato llegue primero que otro, se muestre en el orden deseado

```js
const obtenerInformacion = (text)=>{
    return new Promise((resolve,reject)=>{
        setTimeout(()=> {resolve(text)},Math.random()*200)
    })
}

const mostrarData = async ()=>{
    data1 = await obtenerInformacion("1: a");
    data2 = await obtenerInformacion("2: b");
    data3 = await obtenerInformacion("3: c");
    console.log(data1);
    console.log(data2);
    console.log(data3);
}

mostrarData()
```

El await accede a la promesa (que eso es el async) como si fuera un then