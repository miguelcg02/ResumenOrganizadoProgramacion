# promesas

Un objeto que es un callback que llama a otros 2 callbacks que son resolve y reject.

resolve -> terminación de una función asincrona
reject -> fracaso de una función asincrona

Los datos estan encapsulados

```js
let nombre = "pedro";

const promesa = new Promise((resolve,reject)=>{
    if (nombre !== "pedro") reject("lo siento, el nombre no es pedro")
    else resolve(nombre)
})

promesa.then((resultado)=>{ //Acceder al valor del resolve
    console.log(resultado)
}).catch((e)=>{
    console.log(e)
})

```

```js

personas = [["a0","a1"].["b0","b1"]];

const obtenerPersona = (id) =>{
    return new Promise((resolve,reject)=>{
        if (personas[id] == undefined) reject("No se ha encontrado a la persona")
        else resolve(personas[id])
    })
}

const obtenerInstagram = (id) =>{
    return new Promise((resolve,reject)=>{
        if (personas[id][1] == undefined) reject("No se ha encontrado el segundo parametro")
        else resolve(personas[id])
    })
}

let id = 1;

obtenerPersona(id).then((persona)=>{
    console.log(persona[0])
    return obtenerInstagram(id)
}).then((instagram)=>{
    console.log(instagram)
}).catch((e)=>{
    console.log(e)
})
```

