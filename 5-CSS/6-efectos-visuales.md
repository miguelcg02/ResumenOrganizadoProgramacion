# transition-property / transition-duration

property indica que es lo que se va a cambiar (ej: background) y duration cuanto va a durar. SON OBLIGATORIAS y debe haber una acción como hover

```
.caja{
    background: red;
    height: 100px;
    width: 100px;
    transition-property: background;
    transition-duration: 1s;
}

.caja:hover{
    background: lightgreen;
}
```

# transition-delay

Crea un retardo para que se efectue el efecto y también para que se quite

```
.caja{
    background: red;
    height: 100px;
    width: 100px;
    transition-property: background;
    transition-duration: 1s;
    transition-delay: 1s;
}
```

# transition-timing-function

Da la curva del tiempo en que se dara el cambio

```
/* Keyword values */
transition-timing-function: ease;
transition-timing-function: ease-in;
transition-timing-function: ease-out;
transition-timing-function: ease-in-out;
transition-timing-function: linear;
transition-timing-function: step-start;
transition-timing-function: step-end;

/* Function values */
transition-timing-function: steps(4, jump-end);
transition-timing-function: cubic-bezier(0.1, 0.7, 1.0, 0.1);

/* Steps Function keywords */
transition-timing-function: steps(4, jump-start);
transition-timing-function: steps(10, jump-end);
transition-timing-function: steps(20, jump-none);
transition-timing-function: steps(5, jump-both);
transition-timing-function: steps(6, start);
transition-timing-function: steps(8, end);

/* Multiple timing functions */
transition-timing-function: ease, step-start, cubic-bezier(0.1, 0.7, 1.0, 0.1);

/* Global values */
transition-timing-function: inherit;
transition-timing-function: initial;
transition-timing-function: revert;
transition-timing-function: revert-layer;
transition-timing-function: unset;
```

# @kayframes nombre_animcacion

Se crea como una funcion que se le agrega a un item

```
@keyframes desplazarse{
    from{
        position: relative;
        left: 0;
    }
    to{
        left: 80%;
        background: green;
    }
}


o


@keyframes desplazarse{
    0%{
        position: relative;
        left: 0;
    }
    100%{
        left: 80%;
        background: green;
    }
}

y se le da

.caja{
    background: red;
    height: 100px;
    width: 100px;
    margin: 20px;
    animation-name: desplazarse;
    animation-duration: 3s;
    position: relative;
    animation-iteration-count: 3;
    animation-direction: alternate;
    animation-fill-mode: forwards;
}
```

# Algunas propiedades de las animaciones

```
animation-name: nombre_animacion; Se le asigna al item que se la va a poner la animación
animation-duration: 3s; Duración de la animación
animation-iteration-count: 3; Cantidad de veces que se repetira la animación
animation-direction: alternate; dirección en la que ocurrira la animación
animation-fill-mode: forwards; La manera en la que se quedara el elemento
```

# Cubic-bezier

Para la velocidad de las transiciones
animation-timing-function: cubic-bezier(p1x, p1y, p2x, p2y);

```
animation-timing-function: cubic-bezier(0.075, 0.82, 0.165, 1);
```

# translateX

Mover el objeto

```
eje X | eje Y
tranform: translate(80px,100px);
```

# Scale

Escala el objeto

```
transform: scale(1.5);
```

# skew

Deformar la caja como un paralelogramo

```
transform: skew(10deg);
```

NOTA: Es necesario para poner varios tranforms, hacerlo de esta manera
transform: scale(1.5) translate(80px,100px);

# Click path

```
Buscar en google los tipos de click path y pegar el código
```

# Background

Es un shorthand de funciones

```
background-color /*Le mete un color
background-image: url() /*Para meter una imagen como fondo
background-size: /* Para editar las medidas del fondo colocado
background-clip: /* Para saber desde que parte del box model se muestra la imagen
background-repeat: /* si se repite o no la imagen
background-position /* Para posicionar segun top, bottom, left, right, center
background-attachment 
background (shorthand property)
```

# filter

Hay muchas propiedades para filter

```
filter: url("filters.svg#filter-id"); /* Para meter un filtro
filter: blur(5px); /* Desenfoque No aplican porcentajes
filter: brightness(0.4); /* Cuanto brillo
filter: contrast(200%); /* Se le pone contraste 
filter: drop-shadow(16px 16px 20px blue); /*Se le crea una sombra a las imagenes png
filter: grayscale(50%); /* Se le pone en escala de grises
filter: hue-rotate(90deg); /* Invierte gama de colores
filter: invert(75%); /* Invierte los colores
filter: opacity(25%); /* Le mete la transparencia
filter: saturate(30%); /* Satura la imagen
filter: sepia(60%); /* Se vuelve sepia
```

NOTA: la forma de trabajar al poner varias funciones es igual que transform, así
filter: saturate(30%) sepia(60%);
