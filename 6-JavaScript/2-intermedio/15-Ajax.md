# AJAX (Asynchronous JavaScript And XML) 

Permite hacer request y recibir response en paralelo

* GET

```js
const peticion = new XMLHttpRequest //Permite la entrada de requests

peticion.addEventListener("load",()=>{ //Validacion para que espere hasta que reciba la información
    let respuesta;
    if(peticion.status == 200) respuesta = peticion.response;
    else respuesta = "Se encontro un error";
    console.log(JSON.parse(respuesta));
})

peticion.open("GET","informacion.txt"); //Abre informacion con el GET y luego la URL
peticion.send(); //Envia el archivo (ESs necesario mandarlo)
```

Ajax no se soporta en todos los navegadores, aunque ya explorer murio xd

```js
let peticion;

if (window.XMLHttpsRequest) peticion = new XMLHttpRequest //Permite la entrada de requests
else  peticion = new ActiveXObject("Microsoft.XMLHTTP")

peticion.addEventListener("load",()=>{ //Validacion para que espere hasta que reciba la información
    let respuesta;
    if(peticion.status == 200) respuesta = peticion.response;
    else respuesta = "Se encontro un error";
    console.log(respuesta);
})

peticion.open("GET","informacion.txt"); //Abre informacion con el GET y luego la URL
peticion.send(); //Envia el archivo (ESs necesario mandarlo)
```

* POST

```js
let peticion;

if (window.XMLHttpsRequest) peticion = new XMLHttpRequest //Permite la entrada de requests
else  peticion = new ActiveXObject("Microsoft.XMLHTTP")

peticion.addEventListener("load",()=>{ //Validacion para que espere hasta que reciba la información
    let respuesta;
    if(peticion.status == 200 || peticion.status == 201) respuesta = peticion.response;
    else respuesta = "Se encontro un error";
    console.log(respuesta);
})

peticion.open("POST","URL"); //Abre informacion con el GET y luego la URL

peticion.setRequestHeader("Content-type","application/json;charset=UTF8")

peticion.send(JSON.stringify({
    "nombre": "morfeo",
    "trabajo": "lider"
})); //Envia el archivo (ESs necesario mandarlo)
```
