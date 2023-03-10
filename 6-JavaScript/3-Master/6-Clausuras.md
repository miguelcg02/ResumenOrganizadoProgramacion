# Clausuras

- funciones que no se ejecutan hasta que algo las dispare

```js
"strict mode";

const saludar = (nombre)=>{
    return function(){
        console.log("hola "+nombre);
    }
}

let salud = saludar("pedro");
addEventListener("load",saludo)
```

Si no tuviera el return dentro de la función flecha se ejecuta de una y habría que crear todo el evento desde cero, esto me permite reutilizar.