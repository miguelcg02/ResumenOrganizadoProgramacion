# Conceptos flexbox

```
1. Tiene dos ejes:
-El Main Axis (Sería el eje X en cartesiano), que tiene un main-start(izquierda) y un main-end(derecha)
-El Cross Axis (Sería el eje Y en cartesiano), que tiene un cross-start(arriba) y un cross-end(abajo)

2. Con flexbox se cambian las direcciones de una página.
3. Tienen flex items que son elementos de un contenedor que tiene el display flex. Y son solo los hijos directos. 
```

________________________________________________________________________________________
PROPIEDADES DE CONTENEDORES

# Display flex

Sigue siendo cómo un display block, pero las cajas se adaptan al contenido y en base a este, se posicionan un contenedor al lado del otro. Se aplica al contendor, pero las hijas son las que sufren el efecto y no hay problemas de altura.

```
ej:

.flex-container{
    display: flex;
}
```

# Flex direction

Se puede cambiar la dirección del main axis, y así se cambiará también el cross. Es una propiedad que se le aplica al contenedor, que afectan a los items.

```
1. Row
Queda en forma de fila. Dirección horizontal de izq a derecha

.flex-container{
    display: flex;
    flex-direction: row;
}

2. Column
Queda en forma de columna. De arriba a abajo. 

.flex-container{
    display: flex;
    flex-direction: column;
}

3. row-reverse
Queda en forma de fila. Dirección horizontal de derecha a izq.

.flex-container{
    display: flex;
    flex-direction: row-reverse;
}

4. column-reverse
Queda en forma de columna. De abajo a arriba. 

.flex-container{
    display: flex;
    flex-direction: column-reverse;
}
```

# Flex wrap

Que no se pierda el ancho especifico de la caja, si no que esta se tiren para otro lado cuando se sobrepasan sus medidas. Respeta el ancho.

Nota: Se complementa con el (min-width) en los items.
```
1. wrap
Se tira para abajo en orden.

.flex-container{
    display: flex;
    flex-wrap: wrap;
}

2. wrap-reverse
se tira para arriba en orden.

.flex-container{
    display: flex;
    flex-wrap: wrap-reverse;
}
```

# justify content

Sirve para organizar el contenido de los contenedores en el main-axis (recuerda que se le aplica al contenedor).

```
1. center
Centra el contenido del contenedor

.flex-container{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

2. space-around
Trabaja como un margin auto, centrando el contenido, pero dejando un espacio entre las cajas para que ocupen todo el espacio disponible del contenedor.

.flex-container{
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
}

3. space-between
Deja la mayor cantidad de espacio entre cajas posible, por el tamaño del contenedor.

.flex-container{
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

4. Space-evenly
Hace un space-around, pero ajusta la caja del principio y del final con el mimsmo espacio de todas.

.flex-container{
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
}
```

# Align-items/Align-content

Sirve para alinear las cajas en el cross axis, allign items sirve para cuando hay una sola linea. Allign content cuando hay más de una linea.

```
1. Stretch
Propiedad por defecto que organiza, usando todo el espacio disponible de la caja contenedora, en el cross axis. Se ajusta al contenido si no tiene height.

.flex-container{
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
    height: 100vh;
    align-content: stretch;
}

2. center
Se centra verticalmente

.flex-container{
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
    height: 100vh;
    align-content: center;
}

3. flex-start
Lo pone al inicio del cross axis. Se ajusta al contenido si no tiene height.

.flex-container{
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
    height: 100vh;
    align-content: flex-start;
}

4. flex-end
Lo pone al final del cross axis

.flex-container{
    display: flex;
    flex-wrap: wrap;
    justify-content: space-evenly;
    height: 100vh;
    align-content: flex-end;
}

5. baseline
Practicamente solo tiene el uso de convinarlo con el wrap-reverse par que al achicar se vayan yendo hacia arriba las cajas.

.flex-container{
    display: flex;
    flex-wrap: wrap-reverse;
    justify-content: space-evenly;
    height: 100vh;
    align-content: baseline;
}

```
________________________________________________________________________________________
PROPIEDADES DE ITEMS

# Align self

```
1. Stretch
Propiedad por defecto que organiza, usando todo el espacio disponible de la caja contenedora, en el cross axis. Se ajusta al contenido si no tiene height.

.green{
    align-slef: stretch;
}

2. center
Se centra verticalmente

.green{
    align-slef: center;
}

3. flex-start
Lo pone al inicio del cross axis. Se ajusta al contenido si no tiene height.

.green{
    align-slef: center;
}

4. flex-end
Lo pone al final del cross axis

.green{
    align-slef: center;
}

5. baseline
Practicamente solo tiene el uso de convinarlo con el wrap-reverse par que al achicar se vayan yendo hacia arriba la caja.

.green{
    align-slef: center;
}
```

# Margin en flex-items
el margin toma unas propiedades como cuando se hacía el position absolute.

```
1. margin-left auto
Lo tira a la derecha del contenedor

.green{
    background-color: green;
    margin-left: auto;
}

2. margin-right auto
Lo tira a la izquierda del contenedor

.green{
    background-color: green;
    margin-right: auto;
}

3. margin-top auto
Lo tira a abajo del contenedor

.green{
    background-color: green;
    margin-top: auto;
}

4. margin-bottom auto
Lo tira a arriba del contenedor

.green{
    background-color: green;
    margin-bottom: auto;
}

5. margin auto
Lo centra del todo (Esto porque todos estan en auto, pero si se combina por el el top y el bottom, se queda en el medio pero a la izq del todo, no en el mero centro)

.green{
    background-color: green;
    margin: auto;
}
```

# Flex grow

Reparte el espacio sobrasante segun la proporcion que se le asigne a cada una. Es un buen complemento combinarlo con el min-weight

```
.green{
    background-color: green;
    flex-grow: 2;
}
```

# Flex basis

Es como un width, pero con mayor relevancia que este.

```
.orange{
    background-color: orange;
    flex-basis: 200px;
}
```
# Flex Shrink

Establece cuanto de espacio va a ceder cada caja. Entre mas, mas cede. Esta propiedad no sirve si hay flex-wrap y debe tener establecido un width/flex-basis, que es a donde van a llegar

```
.orange{
    background-color: orange;
    flex-shrink: 2;
}

con un 0, no cede nada de espacio y ya queda con el width/flex-basis establecido
```

# Order

Es como un z-index, pero en el eje en el que apunta el main axis

```
.flex-item{
    min-width: 150px;
    height: 150px;
    background-color: darkblue;
    margin: 5px;
    color: #fff;
    text-align: center;
    flex-grow: 1;
    width: 300px;
    order: 1;
}

.orange{
    background-color: orange;
    order: 2;
}

El orange se moviria hacia el final a donde apunta el main axis.
```