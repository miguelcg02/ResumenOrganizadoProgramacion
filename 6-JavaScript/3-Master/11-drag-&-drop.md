# Drag & drop

Mover iconos y vueltos en la página

* Eventos del objeto

```js
const circulo = document.querySelector(".circulo");

circulo.addEventListener("dragstart",()=>console.log(1)); //Cuando se presiona
circulo.addEventListener("drag",()=>console.log(2)); //cuando se mueve
circulo.addEventListener("dragend",()=>console.log(3)); //Cuando se suelta
```

* Eventos de zona

```js
const circulo = document.querySelector(".circulo");
const rectangulo = document.querySelector(".rectangulo");

rectangulo.addEventListener("dragenter",()=>console.log(1)) //Cuando algo entra dentro del objeto
rectangulo.addEventListener("dragover",(e)=>{
    e.preventDefault(); //Esto se debe poner para permitir que se pueda soltar ahí. Se vuelve una zona permitida
    console.log(2)
}) //Cuando se mueve dentro del objeti
rectangulo.addEventListener("drop",()=>console.log(3)) //Cuando se suelta
rectangulo.addEventListener("dragleave",()=>console.log(4)) //Cuando se sale
```

* Propiedad dataTransfer

Transferencia de datos que pone en interacción el objeto que se agarra y donde se suelta

```js
const circulo = document.querySelector(".circulo");
const rectangulo = document.querySelector(".rectangulo");

circulo.addEventListener("dragstart",(e)=>{
    e.dataTransfer.setData("text-plan",e.target.classname)
}); //Cuando se presiona

rectangulo.addEventListener("dragenter",()=>console.log(1)) //Cuando algo entra dentro del objeto
rectangulo.addEventListener("dragover",(e)=>{
    e.preventDefault(); //Esto se debe poner para permitir que se pueda soltar ahí. Se vuelve una zona permitida
    console.log(2)
}) //Cuando se mueve dentro del objeti
rectangulo.addEventListener("drop",(e)=>{
    e.preventDefault();
    console.log(2);
}) //Cuando se suelta
rectangulo.addEventListener("dragleave",()=>console.log(4)) //Cuando se sale
```