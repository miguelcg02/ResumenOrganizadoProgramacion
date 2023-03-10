# Operador ternario

```js
let edad = 25;

(edad>18) ? console.log("es mayor")
          : console.log("es menor")
```

# Operador spreed 

Convierte un array en valores diferentes

```js
let arr = ["1","2","3"]

console.log(...arr)
```

```js
let arr = ["manzana","pera","banana"];
let arr2 = ["kiwi","naranja"];

arr.push(...arr2);
```

```js
let arr = ["manzana","pera","banana"];
let arr2 = ["kiwi","naranja"];

let arr3 = [...arr,...arr2];
```
