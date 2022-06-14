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