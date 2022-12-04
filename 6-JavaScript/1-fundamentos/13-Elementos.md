# Obtención y modificación

1. Devuelve el texto de cualquier nodo, pero no el html

```js
const titulo = document.querySelector(".titulo");

let resultado = titulo.textContent;

document.write(resultado);
```

2. Devuelve el texto visible de un nodo element

```js
const titulo = document.querySelector(".titulo");

let resultado = titulo.innerText;

document.write(resultado);
```

3. devuelve el contenido html de un elemento

```js
const titulo = document.querySelector(".titulo");

let resultado = titulo.innerHTML;

document.write(resultado);
```

4. Devuelve el html completo del elemento

```js
const titulo = document.querySelector(".titulo");

let resultado = titulo.outerHTML;

document.write(resultado);
```

# Creacion de elementos

1. Crear una etiqueta

```js
const contenedor = document.querySelector(".contenedor");

const item = documento.createElement("LI");

documento.write(item)
```

2. Poner texto dentro de etiquetas

```js
const contenedor = document.querySelector(".contenedor");

const item = documento.createElement("LI");
const textDelItem = document.createTextNode("Este es un item de la lista");

item.appendChild(textDelItem);

cosole.log(item);
```

Un elemento no puede ser agregado dos veces, es único. si no habría problemas en la dirección de la memoria.

3. Crear multiples elementos de forma practica

```js
const contenedor = document.querySelector(".contenedor");

const fragmento = document.createDocumentFragment();

for (i = 0;i <20; i++>){
    const item = document.createElement("LI");
    item.innerHTML = "Este es un item de la lista";
    fragmento.appendChild(fragmento)
}

contenedor.appendChild(fragmento)
```

# Obtencipon y modificación de childs

1. Obtener primer child

```js
const contenedor = docuemnt.querySelector(".contenedor");

const primerHijo = contenedor.firstChild;
```


2. Obtener un htmlCollectoin de los hijos

```js
const contenedor = docuemnt.querySelector(".contenedor");

const hijos = contenedor.children;

for (hijo of hijos){
    console.log(hijo)
}
```

un HtmlCollection no se puede recorrer con foreach

# Metodos de child

1. Reemplazar hijo 

```js
const contenedor = docuemnt.querySelector(".contenedor");

const parrafo = document.createElement("P").innerHTML = "Parrafo";
const h2_nuevo = document.createElement("H2");
h2_nuevo.innerHTML = "Titulo";

h2_antiguo = document.querySelector(".h2");

contenedor.replaceChild(h2_nuevo,h2_antiguo);
```

2. Remover hijo que se quiere remover

```js
const contenedor = docuemnt.querySelector(".contenedor");

const parrafo = document.createElement("P").innerHTML = "Parrafo";
const h2_nuevo = document.createElement("H2");
h2_nuevo.innerHTML = "Titulo";

h2_antiguo = document.querySelector(".h2");

contenedor.removeChild(h2_antiguo);
```

3. Verificar si un nodo esta vacio 

```js
const contenedor = docuemnt.querySelector(".contenedor");

const parrafo = document.createElement("P").innerHTML = "Parrafo";
const h2_nuevo = document.createElement("H2");
h2_nuevo.innerHTML = "Titulo";

h2_antiguo = document.querySelector(".h2");

let respuesta = contenedor.hasChildNodes();

console.log(respuesta);
```

# Propiedades de parents

1. Busca un elemento padre (Puede o no ser una etiqueta)

```js
const contenedor = docuemnt.querySelector(".contenedor");

const parrafo = document.createElement("P").innerHTML = "Parrafo";
const h2_nuevo = document.createElement("H2");

const h2_antiguo = document.quetySelector(".h2");

console.log(contenedor.parentElement);
```

2. Busca un nodo padre (Tiene que ser una etiqueta)

```js
const contenedor = docuemnt.querySelector(".contenedor");

const parrafo = document.createElement("P").innerHTML = "Parrafo";
const h2_nuevo = document.createElement("H2");

const h2_antiguo = document.quetySelector(".h2");

console.log(contenedor.parentNode);
```

# Propiedades hermano

1. Revisa el tipo del siguiente nodo hermano

```js
const contenedor = docuemnt.querySelector(".contenedor");

const parrafo = document.createElement("P").innerHTML = "Parrafo";
const h2_nuevo = document.createElement("H2");

const h2_antiguo = document.quetySelector(".h2");

console.log(h2_antiguo.nextSibling);
```

2. Revisa el tipo del anterior nodo hermano

```js
const contenedor = docuemnt.querySelector(".contenedor");

const parrafo = document.createElement("P").innerHTML = "Parrafo";
const h2_nuevo = document.createElement("H2");

const h2_antiguo = document.quetySelector(".h2");

console.log(h2_antiguo.previousSibling);
```

3. Revisar el elemento del siguiente nodo hermano

```js
const contenedor = docuemnt.querySelector(".contenedor");

const parrafo = document.createElement("P").innerHTML = "Parrafo";
const h2_nuevo = document.createElement("H2");

const h2_antiguo = document.quetySelector(".h2");

console.log(h2_antiguo.nextElementSibling);
```

3. Revisar el elemento del anterior nodo hermano

```js
const contenedor = docuemnt.querySelector(".contenedor");

const parrafo = document.createElement("P").innerHTML = "Parrafo";
const h2_nuevo = document.createElement("H2");

const h2_antiguo = document.quetySelector(".h2");

console.log(h2_antiguo.previousElementSibling);
```

# Extra

1. Revisar el elemento más ascendente más cercano especificado

```js
const div = document.querySelector(".div-3");

console.log(div.closet(".div"))
```