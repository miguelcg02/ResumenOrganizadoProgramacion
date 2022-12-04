# Callbacks

- Es una función que llama a otra función

Forma 1
```js
function prueba(callback){
    callback("roberto");
}

function decirNombre(nombre){
    console.log("nombre");
}

prueba(decirNombre)
```

Forma 2
```js
function prueba(callback){
    callback("roberto")
}

prueba(function decirNombre(nombre){
    console.log("nombre")
})
```

Froma 3
```js
function prueba(callback){
    callback("roberto")
}

prueba((nombre)=>{
    console.log("nombre")
})
```

Forma 4
```js
function prueba(callback){
    callback("roberto")
}

prueba(nombre=>console.log("nombre"))
```

```js
class Persona {
    constructor(nombre,instagram){
        this.nombre = nombre;
        this.instagram = instagram;
    }
}

const data = [["Miguel","calvache116"],
              ["Julio","JJmillo"],
              ["Jara","Jarazo"]];

const personas = [];

for (var i=0;i<data.length;i++){
    personas[i] = new Persona(data[i][0],data[i][1])
}

const obtenerPersona = (id,cb)=>{
    if(personas[id]== undefined){
        cb("No se ha encontraod la persona")
    } else{
        cb(null,personas[id])
    }
}

obtenerPersona(0,(err,persona)=>{
    if(err){
        console.log(err)
    } else{
        console.log(persona.nombre)
        console.log(persona.instagram)
    }
})

```

# Promise (Cuando son demasiados datos que hay que verificar con callbacks)

- Es un callback con otros 2 callbacks, resolve y reject

```js
let nombre = "pedro";

const promesa = new Promise((resolve,reject)=>{
    if (nombre !== "pedro") reject("Lo siento, el nombre no es Pedro")
    else resolve(nombre)
})

promesa.then((resultado)=>{ //Asi se accede al valor si llega al resolve 
    console.log(resultado)
}).catch((e)=>{ //Asi se accede al error cuando llega al reject
    console.log(e)
})
```

5:17:50 Promesas