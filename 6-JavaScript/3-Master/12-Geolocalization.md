# geolocation

```js
const geolocation = navigator.geolocation;

const posicion = (pos)=>{
    console.log("pos")
}

lugar = geolocation.getCurrentPosition(posicion) //Saca las coordineadas
console.log(lugar.coords.latitude)
```

```js
"use strict";

const geolocation = navigator.geolocation;

const posicion = (pos)=>{
    console.log("pos")
}

const err = ()=> console.log(e);

const options = {
    maximumAge: 0,
    timeout: 3000,
    enableHighAccuracy: true
}

lugar = geolocation.getCurrentPosition(posicion,err,options)  
console.log(lugar)
```

* watchPostion() 

Revisa la posición en tiempo real