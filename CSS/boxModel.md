# Display. que tanto ocupa de la linea

Linea o bloque

```
display: inline;
- No se les puede dar height ni width
- El elemento genera un cuadro de elemento de bloque.

display: block;
- Si se les puede dar height y width
- El elemento genera uno o más cuadros de elemento en línea.

display: inline-block;
- El elemento genera una caja de elemento de bloque que fluye con el contenido circundante como si fuera una sola caja en línea (comportándose como un elemento reemplazado)

ej:

h2 {
    display: inline;
}
```

# Box Model

```
-Content: Contenido de la caja
se modifica con el line-height

-Padding: Separacion entre contenido y borde de la caja
se modifica con el padding

-Border: El borde de la caj
se modifica con el border

-Margin: La distancia entre dos cajas
Se modifica con el margin
```


# Box-sizing

Para ver si se mantiene la deformación de la caja o no, con respecto al contenido de la caja

```
-Para que no se deforma la caja, si no que se ajuste con el contenido
box-sizing: content-box;

-Para que se mantenga la caja, sin importar la deformación.
box-sizing: border-box;
```

# Algunas propiedades de la caja

```
-Alto de la caja
height: 300px;

-Ancho de la caja
width: 300px;
```

# Padding

Distancia entre los bordes de la caja y el texto.

Esta el padding top, right, bottom y left.

```
ej: 

h2{
    padding: 5px (top) 6px (right) 7px (bottom) 8px (left).
}


ej 2:

div {
  padding-top: 50px;
  padding-right: 30px;
  padding-bottom: 50px;
  padding-left: 80px;
}

NOTA: Si paading tiene un solo valor, se le colaca ese valor a todos los lados.
```

# Margin

Distancia entre dos cajas

Esta el margin top, right, bottom y left.

```
h2{
    margin: 5px (top) 6px (right) 7px (bottom) 8px (left).
}


ej 2:

div {
  margin-top: 50px;
  margin-right: 30px;
  margin-bottom: 50px;
  margin-left: 80px;
}

NOTA: Si margin tiene un solo valor, se le colaca ese valor a todos los lados.
```

# Alineación de texto dentro de una caja

```
- Para alinear el texto al centro
div.a {
  text-align: center;
}

- Para alinear el texto a la izquierda
div.b {
  text-align: left;
}

- Para alinear el texto a la derecha
div.c {
  text-align: right;
}

- Para estirar las líneas para que cada línea tenga el mismo ancho (como en periódicos y revistas)
div.c {
  text-align: justify;
}
```

# Borde

Editar el borde de la caja

```
-Utilizando la propiedad shorthand "border", define el grosor, el estilo y color
div {
  border: 1px solid #C00;
}

-Utilizando las propiedades shorthand de cada borde, define el grosor, el estilo y color.
div {
  border-top: 1px solid #C00;
  border-right: 1px solid #C00;
  border-bottom: 1px solid #C00;
  border-left: 1px solid #C00;
}

-Utilizando las propiedades simples de cada borde, define el grosor, color y el estilo
div {
  border-top-width: 1px;
  border-top-style: solid;
  border-top-color: #C00;
  border-right-width: 1px;
  border-right-style: solid;
  border-right-color: #C00;
  border-bottom-width: 1px;
  border-bottom-style: solid;
  border-bottom-color: #C00;
  border-left-width: 1px;
  border-left-style: solid;
  border-left-color: #C00;
}

-estilos:
1. none: No se muestra ningún borde. Como se trata del valor por defecto de cada uno de los bordes, ningún elemento muestra un borde a menos que se establezca de forma explícita
2. hidden: Visualmente es idéntico a none, ya que provoca que no se muestre ningún borde. Su única diferencia es la forma en la que el navegador resuelve los conflictos entre bordes adyacentes de las celdas de las tablas
3. dotted: Borde punteado, formado por una serie de puntos separados por espacios
4. dashed: Borde discontinuo, formado por una serie de pequeños trazos intercalados por espacios
5. solid: Borde continuo, formado por una línea recta continua
6. double: Borde doble, formado por dos líneas rectas continuas separadas entre sí por un espacio en blanco
7. groove: Borde hundido, que visualmente parece que se encuentra por debajo del nivel de la superficie de la pantalla
8. ridge: Borde saliente, que visualmente parece que se encuentra por encima del nivel de la superficie de la pantalla
9. inset: Borde hundido, que provoca que el elemento que encierra parezca que se encuentra por debajo del nivel de la superficie de la pantalla
10. outset: Borde saliente, que provoca que el elemento que encierra parezca que se encuentra por encima del nivel de la superficie de la pantalla
```

# Box-shadow

Se crea una sombra de la caja que se puede colocar a gusto

```
- Movimiento-x | Movimiento-y | color
box-shadow: 60px -16px teal;

- Movimiento-x | Movimiento-y | blur-radius | color
box-shadow: 10px 5px 5px black;

- Movimiento-x | Movimiento-y | blur-radius | spread-radius | color
box-shadow: 2px 2px 2px 1px rgba(0, 0, 0, 0.2);

- inset | Movimiento-x | Movimiento-y | color
box-shadow: inset 5em 1em gold;
```

# Text shadow

Se crea una sombra del texto de la caja que se puede colocar a gusto

```

- Movimiento-x | Movimiento-y | blur-radius | color 
h1 {
  text-shadow: 2px 2px 8px #FF0000;
}
```

# Transform

se aplican funciones sobre la caja, como rotar

```
ej:

h1 {
  transform: rotate(90deg);
}
```

1:55h