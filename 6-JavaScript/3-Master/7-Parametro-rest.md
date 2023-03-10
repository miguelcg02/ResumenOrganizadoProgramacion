# Parametro rest

No importa la cantidad de parametros que se ingresen al llamar una función

```js
"strict mode";

const suma = (...num)=>{
    let resultado = 0;
    for (var i=0;i<num.length;i++){
        resultado += num[i] 
    }
    console.log(resultado)
}

suma(14,24,63,12,54)
```