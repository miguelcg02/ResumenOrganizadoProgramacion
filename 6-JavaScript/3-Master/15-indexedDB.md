# Base de datos no relacional

- Es asincrona (Se hacen a tiempo real)
- Es orientado a objetos
- Trabaja con eventos del DOM

```js
"use strict";

const IDBRequest = indexedDB.open("vichobase",1); //Abirir o crear la base de datos

console.log(IDBRequest);

IDBRequest.addEventListener("upgradeneeded",()=>{
    console.log("Se creo la bdd")
})

IDBRequest.addEventlistener("success",()=>{
    console.log("todo salio good");
})

IDBRequest.addEventlistener("error",()=>{
    console.log("Ocurrio un error al abrir la base de datos")
})
```

# Almacenar objetos

```js
"use strict";

const IDBRequest = indexedDB.open("vichobase",1); //Abirir o crear la base de datos

console.log(IDBRequest);

IDBRequest.addEventListener("upgradeneeded",()=>{
    const db = IDBRequest.result;
    db.createObjectStore("nombres",{
        autoIncrement: true //Tambien puede ser trabajado con keypath pero cambian consitas
    })

    IDBRequest.addEventlistener("success",()=>{
    console.log("todo salio good");
    })
})

IDBRequest.addEventlistener("success",()=>{
    console.log("todo salio good");
})

IDBRequest.addEventlistener("error",()=>{
    console.log("Ocurrio un error al abrir la base de datos")
})

// Añadir objetos

const addObjeto = objeto => {
    const db = IDBRequest.result;
    const IDBtransaction = db.transaction("nombres","readwrite");
    const objectStore = IDBtransaction.objectStore("nombres");
    objectStore.add(objeto);
    IDBtransaction.addEventListener("complete",()=>{
        console.log("objeto agregado correctamente");
    })
}

//addObjeto({nombre: "roberto"})

// Leer todos los objetos

const readObjects = ()=> {
    const db = IDBRequest.result;
    const IDBtransaction = db.transaction("nombres","readonly");
    const objectStore = IDBtransaction.objectStore("nombres");
    const cursor = objectStore.opencursor();
    cursor.addEventlistener("success",()=>{
        if(cursor.result){
            console.log(cursor.result.value)
            cursor.result.continue()
        } else console.log("todos los datos fueron leidos")
    })
}

// Modificar objetos

const updateObjeto = (key,objeto) => {
    const db = IDBRequest.result;
    const IDBtransaction = db.transaction("nombres","readwrite");
    const objectStore = IDBtransaction.objectStore("nombres");
    objectStore.put(objeto,key);
    IDBtransaction.addEventListener("complete",()=>{
        console.log("objeto modificado correctamente");
    })
}

// updateObjeto(3,{nombre: "Roger"})

// Eliminar

const deleteObjeto = key => {
    const db = IDBRequest.result;
    const IDBtransaction = db.transaction("nombres","readwrite");
    const objectStore = IDBtransaction.objectStore("nombres");
    objectStore.delete(key);
    IDBtransaction.addEventListener("complete",()=>{
        console.log("objeto eliminado correctamente");
    })
}

```
