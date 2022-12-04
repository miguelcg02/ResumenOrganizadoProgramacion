# EventListener

- A los elementos se le agrega la posibilidad de escuchar lo que esta sucediendo
- No funcionan las funciones flecha

```js
const button = document.querySelector(".button");

button.addEventListener("click",saludar);

function saludar (){
    alert("hola")
    button.removeEventListener("click",saludar) //Aqui se quita el evento
}
```

# onclick()

- En un on event handler

# Objeto evento

- Muestra que evento esta sucediendo con sus propiedades

```js
const button = document.querySelector(".button");

button.addEventListener("click",(e)=>{
    console.log(e.target)
    console.log(e) //Muestra todas las caracteristica
});
```

# Event flow

- Orden en el que se van a ejecutar los eventos
- Existen 2 tipos: bubble y event capturing

Bubbling: Más especifico a menos especifico (por defecto)
Event Capturing: Del menos al más especifico

Para cambiarlo a Event Capturing ponerle true
```js
const button = document.querySelector(".button");

button.addEventListener("click",(e)=>{
    console.log(e.target)
},true);
```

# Parar propagación, que solo se ejecute donde fue el evento

```js
const button = document.querySelector(".button");

button.addEventListener("click",(e)=>{
    console.log(e.target)
    e.stopPropagation() //Asi ya para de leer y solo ejecuta hasta acá
});
```


