# Nodo

Es una etiqueta o los atributos de las etiquetas

* Tipos de nodo
    - Document: Es el nodo raiz del docuemtno, a partir del cual derivan el resto de nodos.
    - Element: Definidos por etiquetas html.
    - Text: el contenido dentro de las etiquetas
    - Attribute: Información asosciada a los atributos de  las etiquetas
    - comentarios: comentarios html

# Metodos de seleccion de elemntos

1. Seleccionar un elemento por ID

```js
parrafo = documento.getElementById("parrafo") //Parrafo es el id del tag
```

2. Seleccionar un elemento por tipo de Tag

```js
parrafo = document.getElementsByTag("p");
```

Si hay varios se almacena en un array

3. Devolver el primer elemento que coincidad con el grupo especificado de selectores

```js
parrafo = document.querySelector(".parrafo_selector"); //Usar el selector correcto, en este caso el de clase es punto
```

4. devuelve todos los elementos que coincidan con el grupo especificado

```js
parrafo = document.querySelectorAll(".parrafo_selector"); //Usar el selector correcto, en este caso el de clase es punto
```

# Metodos para atributos

1. Setear atributos, creados o sin crear (Tienen que ser atributos validos)

```js
const rangoEtario = document.querySelector(".rangoEtario");

rangoEtario.setAttribute("type","text")
```

2. get Atribut

```js
const rangoEtario = document.querySelector(".rangoEtario");

document.write(rangoEtario.getAttribute("type"))
```

3. Quitar atributos

```js
const rangoEtario = document.querySelector(".rangoEtario");

rangoEtario.removeAttribute("type")
```

# Atributos de inputs

```js
const input = document.querySelector(".input-normal");

document.write(input.className); //Devuelve el nombre de la clase
document.write(input.value); //Muetra el valor del input
input.type = "range"; //Modifica el type, desde la propiedad del atributo
input.accept = "image/png"; //Acepta un tipo de información
input.minLength = 3; //Indica el minimo necesario de caracteres
input.placeholder = "Mensaje"; 
input.required = "required"; //Es obligatorio llenar información
```

# Atributo style

```js
const input = document.querySelector(".input-normal");

input.style.color = "#aaa"
```