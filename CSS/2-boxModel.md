# Display. que tanto ocupa de la linea

Linea o bloque

```
display: inline;
- No se les puede dar height ni width
- El elemento genera un cuadro de elemento de bloque.
- Usado generalmente para textos

display: block;
- Si se les puede dar height y width
- El elemento genera uno o más cuadros de elemento en línea.

display: inline-block;
- El elemento genera una caja de elemento de bloque que fluye con el contenido circundante como si fuera una sola caja en línea (comportándose como un elemento reemplazado) y se puede dimensionar las medidas de la caja

display: flex;
-Se comporta como display block,  lo que esta adentro de la caja, no se comporta igual. Los hijos son los que se ven afectado

display: grid;
-Se comporta como display block, lo que esta adentro de la caja, no se comporta igual. Los hijos son los que se ven afectado

display: inline-flex;

display: inline-grid;


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

-Transiciones
transition: width 1s, height1s, background1s, etc;

Nota: va en la caja original no en el hover.
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

ej 1: 
Esta el margin top, right, bottom y left.

```
h2{
    margin: 5px (top) 6px (right) 7px (bottom) 8px (left).
}


ej 2:
Este es el margin con cada propiedad en separado

div {
  margin-top: 50px;
  margin-right: 30px;
  margin-bottom: 50px;
  margin-left: 80px;
}

NOTA: Si margin tiene un solo valor, se le colaca ese valor a todos los lados.

ej 3:
Este es un valor que se le pone para centrar la caja horizontalmente.

margin: auto; 


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

Se aplican funciones sobre la caja, como rotar

```
ej:

h1 {
  transform: rotate(90deg);
}
```

# Outline

Propiedad que genera un borde, pero sin afectar a las demás cajas, no ocupa un espacio en el DOM

```
outline: 10px solid blue;

Hay que tener en cuenta que seguira midiendo lo mismo por lo que un box-sizing no lo afectara, porque es como si no existiera. 
```

# Position

Es como se afecta el orden donde se ponen los elementos, se afecta el flujo de html.

```
Hay 5 tipos de posicionamiento y hace que se obtengan 5 propiedades nuevas, top, left, right, bottom y el z index:

(Top y left tienen prioridad)

-z-index organiza en el eje z, y para poder organizarlo tienen que estar instanciados el poscionamiento, además un contenedor siempre estará por debajo de su hijo. A menos de que el contenedor no tenga z-index, y el hijo tenga un z-index = -1

1. Static:
Es el normal por edefecto, sigue el mismo flujo de html.

position: static;


2. Relative:

position: relative;

pero si se le pone tambien
top: 20px;
left 30px;
z-index: 100;

se movera 20px hacia abajo y 30px a la derecha

El espacio de la caja se conserva pero se movera. Pero sigue manteniendo su espacio original con respecto a otras cajas y se mantiene su punto de referencia.

3. Absolute:

position: absolute;

El espacio de la caja se pierde. Y su punto de referencia pasara a ser la pantalla como tal o el contenedor que lo tenga si este esta posicionado (El que sea) y se le pone top o left, o se mantendra en su lugar original si no se le pone. 

Nota: Este es medio raro entonces hace ejemplos porque el punto de referencia puede variar si solo se instancia top y no left y viceversa.
Nota 2: Aunque sea un elemento en bloque al poner absolute, la caja se autoajusta al contenido si no se le instancia width y height
Nota 3: Para centrarlo poner top 0, left 0, right 0, bottom 0 y margin auto.

4. Fixed:
Exactamente igual que absolute, pero queda fijado. Toca tener en cuenta que como el espacio se pierde, la caja de abajo pasara a ese lugar y se tapara por la caja fixed.

position: fixed;

Para arreglar el problema de lo de las letras:

body{
  padding-top:100px;
}

.caja-fixed{
  margin:-100px;
}

5. Sticky
Combinacion entre relative y dixed, pero se puede determinar como y donde se queda fijo.

position: sticky;

y ojo acompañarlo de un:
top: 0

esto, para que se queda en esa posicion referenciando al viewport

```

# Overflow

Es la barrita de navegación (Scroll), se le mete para lo que sobra en la caja y se cree la barra de navegación

```
- Visible
Es la que esta por defecto, y es que el contenido que se sale de la caja, aún así sea visible

overflow: visible;

-auto
Es el mejor, esconde el contenido y permite scrollear dentro de la caja sin que el contenido sobresalga solo cuando es necesario.

overflow: auto;

-scroll
Siempre pone la barra de navegación y esconde lo que se sobresale.

overflow: scroll;

-hidden
Hace que se desaprezca la barra

overflow-y: hidden;
```

# float

Hoy en día ya solo le queda un buen uso y es colocar imagenes con texto, en el que la imagen corra el texto a un lado.

```
REVISAR EJEMPLO 10
```

# Pseudo-Elementos

La mayoria no forman parte del DOM pero genera cambios visiuales, si requiere la etiqueta content no hace parte del DOM

```
1. ::first-line | FUNCIONA EN TODOS MENOS EN INLINE
-Edita la primera linea de todas dinamicamente, este si hace parte del DOM

ej: 

.editar-Primer-Linea::first-line{
    color: blue;
    font-size: 2em;
}

2 ::first-letter | FUNCIONA EN TODOS MENOS EN INLINE
-Edita la primera letra de todas dinamicamente, este si hace parte del DOM

ej: 

.editar-Primera-Letra::first-letter{
    color: red;
    font-size: 3em;
}

3 ::placeholder | Se le tiene que poner de atributo a la caja al que se le quiera poner
-Hace que aparezca unas caracterisitcas hasta que se edite por el usuario.

<input type="text" placeholder="inserte su nombre aqui">

input::placeholder{
  color: red;
}

4. ::selection 
-Sirve para cambiar el contenido seleccionado

input::selection{
  background: yellow;
}

5. ::before | Son hijos del elemento al que se aplica, necesitan CONTENT y son inline
-Se agregan elementos inline antes del contenido que haya antes, si estaba solo "ayer" y en content le pongo "me dormí ", ahora aparecerá "me dormí ayer"

ej:

<b>a</b>

b::before{
    content: "Me suscribi ";
}

resultado: "Me suscribí a"

```

# Pseudo clases

Es para escuchas de eventos

```
1. :hover | funciona en todos los elementos
-Es cuando el mouse esta encima

.caja1{
    height: 200px;
    width: 200px;
    background: blue;
    transition: background 2s;
}

.caja1:hover{
    background: red;
    height: 250px;
    width: 250px;
}

2. :link | funciona en elementos <a></A>
-Cambia propiedades de un link que no ha sido visitado

.caja2:link{
    color: red;
}

3. :visited | funciona en elementos <a></A>
-Cambia propiedades de un link visitado

.caja2:visited{
    color: orange;
}

4. :active | funciona en todos los elementos
-El evento ocurre cuando se presiona el contenido

.caja3:active{
    background: blue;
}

5. :focus | Usualmente se aplica en inputs
-El evento ocurre cuando el elemento esta seleccionado

.caja4:focus{
    background: blue;
    width: 100px;
    height: 100px;
}

6. :lang |funciona en todos los elementos
-El evento ocurre al instanciar por atributo el lenguaje de este.

.caja5 b:lang(es){
    background-color: red;
}

```

# Object fit

Para trabajar con las medidas de la imagen y su resolución

```
-contain: Las resoluciones de la imagen se ajusten al contenido. Agrande las resoluciones

object-fit: contain;

-cover: La imagen se ajusta al contenedor y recorta si no cabe exacto.

object-fit: cover;

-scale-down: Se queda con la resolución más chica.

object-fit: scale-down;

-none: La proporcion de la imagen se mantiene, con las mimsas resoluciones.

object-fit: none;

Se activa la función object-position: (left,right,top,bottom) o con medidas en px, em, etc. Para posicionar el contenido de la imagen en el contenedor (Por ej cuando se usa cover)
```

# Cursor

Para cambiar el estilo del cursor al estar dentro de una caja

```
https://www.w3schools.com/cssref/tryit.asp?filename=trycss_cursor
```




