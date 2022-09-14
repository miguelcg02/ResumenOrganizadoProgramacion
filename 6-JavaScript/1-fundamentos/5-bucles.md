# while

```js
let numero = 0;

while(numero < 6){
    document.write(numero);
    numero++;
}
```

# do while

```js
let numero = 0;

do{
    document.write(numero);
    numero++;
}
while(numero < 6)
```

# for

```js
for (let i=0; i<6;i++){
    document.write(i);
}
```

# for in

Muestra los indices en donde se encuentran los elementos

```js

let animales = ["gato","perro","pez"];

for (animal in animales){
    document.write(animal);
}
```

# for of

Muestra los elementos

```js

let animales = ["gato","perro","pez"];

for (animal of animales){
    document.write(animal);
}
```