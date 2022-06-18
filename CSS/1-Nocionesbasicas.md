# Enlazar

En el head, se enlaza el archivo html con el css

```
<link rel="stylesheet" type="text/css" href="nombre.css">
```

# Estructura

```
selector {
    propiedad:valor;
}

selector: Son los elementos seleccionados (lo que se va a cambiar).
propiedad: Cosa que se va a cambiar.
valor: Cantidad de lo que se va a cambiar.
```

# Display block / display line

```
- El block acaba la linea
- El line solo hasta donde va el contenido
```

# Tipos de selectores

```
Universal: Va con todo

* {
    propiedad: valor;
}

Tipo: Se selecciona por elemento

h1 {
    propiedad: valor;
}


Clases: Por nombre de la clase que tenga el atributo

.nombreClase {
    propiedad: valor;
}

ID: Por id, la idea es que el id sea único

#id-del-elemento{
    propiedad: valor;
}

Atributo: cambia las etiquetas que tengan un atributo en especifico

[atributo="valor"]{
    propiedad: valor;
}

Descendiente: cambia las etiquetas que tengan elementos dentro de otros elementos. De más afuera a más adentro

elementoMayor elementoMenor {
    propiedad: valor;
}

Pseudo-clases: Es con las pseudo-clases, son en eventos usualmente

elemento:accion {

}

```

# Especifidad

```
1. !important
____________________________
2. Estilos en linea
____________________________
3. Id
____________________________
4. clases
5. pseduo-clases
6. atributos
____________________________
7. elementos
8. pseudo-elementos
```

# Metodlogia BEM

```
Es para diferenciar las clases.

1. Poner el nombre del bloque en general y luego en del otro elemento asi:

    <div class="contact-form">
        <input type="text" class="contact-form__input">
        <input type="password" class="contact-form__input">
    </div> 

2. Si se quiere diferenciar uno de otros, cambiar el nombre:

    <div class="contact-form">
        <input type="text" class="contact-form__input--active">
        <input type="password" class="contact-form__input">
        <input type="text" class="contact-form__input">
        <input type="password" class="contact-form__input">
        <input type="text" class="contact-form__input">
        <input type="password" class="contact-form__input">
    </div>
```

# Unidades

Se tienen medidas fijas y relativas

```
Fijas:

- px
- pt
- cm
- mm

Relativas:

- em  = 16px aprox, pero es definido por la caja contenedora
- vw Viewport Width, es el ancho de la pagina. 100vw es todo el ancho de la pagina. Es como un porcentaje pero de toda la página visible
- vh Viewport Heigth, es la altura de la pagina. 100vh es todo el alto de la pagina. Es como un porcentaje pero de toda la página visible
- % Porcentaje, es un porcentaje de la caja. Esto se ve en el box model

```

# Propiedades

```
1. Tamaño de la letra

font-size: 30px;

2. Ancho

width: 50vw;

3. Alto

height: 50vh;

4. Color letra

color: #000;

5. Color fondo

background-color: #000;

6. Tipo de letra

font-family: Georgia, sans-serif;

7. Aumento del tamño de la caja del texto

line-height: 2;

8. Grosor de las letras

font-weight: 900;

9. Transaparencia

opacity: 0.5;
```