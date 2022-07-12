# Conceptos grid

```
1. Grid container
-Es todo el contenedor que tiene el grid. Es TODO. Es cómo el flex container.

2. Grid item
-Son los items (etiquetas) que están dentro del contenedor del grid container, debe ser hijo directo.

3. Grid cell
-Son las celdas que se establecen, son divisiones. Grid cell =! Grid item

4. Grid tracks (Column y rows)
-Son las celdas verticales y horizontales sumadas, por ej si es 3x4 entonces es 7

5. Grid area
-Son areas seleccionadas consecutivas. Nosotros definimos las areas de la cantidad de celdas que vamos a agarrar. Debe ser rectangular y la idea es que no solo sea una celda.

6. Grid line (Column line y Row line)
-Son las lineas divisoreas, para las column line empieza a contar de izq a der y para las row line empieza a contar de arriba a abajo. (Tener en cuenta que se es 3x4, se tendran 4 columns lines y 5 rows lines)
```

_______________________________________________________________________________________________________
PROPIEDADES QUE SE LE AMPLICAN AL CONTENEDOR

# Display grid / grid-template-rows / grid-template-columns

Se le asigna el display grid, pero es necesario complementarlo con el grid-template-rows y grid-template-columns para darle las filas y columnas. 


```
.grid-container{
    display: grid;
    grid-template-rows: 150px 150px 150px;
    grid-template-columns: 150px 150px 150px;
}

Aqui se crea una grilla 3x3 y no hay items implicitos.
```

# fr

Es una medida como el flex-grow, para que aumente el tamaño de la caja dependiendo del largo de pixeles que se disponga. Se suele aplicar más en las columnas.

```
.grid-container{
    display: grid;
    border: 3px solid black;
    grid-template-rows: 150px 150px 150px;
    grid-template-columns: 1fr 1fr 1fr;
}
```

# Grid-gap / Grid-row-gap / Grid-column-gap

Se separan las celdas entre ellas (No con los bordes del contenedor) tanto columnas como filas.
Es short hand de grid-row-gap y grid-column-gap.

Nota: ya se usa solo gap, row-gap y column-gap.

```
.grid-container{
    background-color: #eee;
    display: grid;
    border: 3px solid black;
    grid-template-rows: 150px 150px 150px;
    grid-template-columns: 1fr 1fr 1fr;
    row-gap: 10px;
    column-gap: 10px;
}
```

_________________________________________________________________________________________________
PROPIEDADES A LOS ITEMS

# Grid column 

Para ampliar celdas en su forma horizontal.

Se pone desde que linea vertial va a empezar y hasta que linea va a ir.

```
.grid-item:first-child{
    background-color: red;
    grid-column: 1 / 3;
}
```

# Grid row 

Para ampliar celdas en su forma vertical.

Se pone desde que linea horizontal va a empezar y hasta que linea va a ir.

```
.grid-item:first-child{
    background-color: red;
    grid-row: 1 / 3;
}
```
# span

Es una ayuda para en vez de indicar la linea, indicar cuantas cajas se quieren.

```
.grid-item:first-child{
    background-color: red;
    grid-row: 1 / span 3;
}

Aqui empieza en la linea 1 y ocupa 3 celdas.
```

# repeat()

Otra forma de crear celdas rapido

```
.grid-container{
    background-color: #eee;
    display: grid;
    border: 3px solid black;
    grid-template-rows: 150px 150px 150px;
    grid-template-columns: repeat(3, 1fr) 150px;
}
```
_______________________________________________________________________________________________

# Grid implicito

Cuando no se instancian todos los elementos y queda uno por fuera, a estos elementos se les llama grid implicitos. Creando nuevas propiedades para estas.

# Grid-auto-column / Grid-auto-rows / Grid-auto-flow

Esa nueva fila que se creo automaticamente por no estar instanciada, se puede colocar abajo o a la derecha (con Grid-auto-flow: column o Grid-auto-flow: row). Mientras que el Grid-auto-column / Grid-auto-rows le daran las medidas esta nueva fila.

```
.grid-container{
    background-color: #eee;
    display: grid;
    border: 3px solid black;
    grid-template-columns: repeat(5, 80px) 1fr;
    grid-template-rows: 150px 150px 150px;
    grid-auto-flow: column;
    /* grid-auto-rows: 10px; */
    grid-auto-columns: 100px;
}

NOTA: Si hay muchos huecos en la grilla, usar  grid-auto-flow: dense; para rellenar.
```
______________________________________________________________________________________
GRID DINAMICO

# max-content / min-content

Para que el grid no este ajustado con px o fr, si no con el contenido de la caja que lo contiene.

```
grid-template-columns: repeat(3, max-content);

grid-template-columns: repeat(3, min-content);
```

# minmax()

Se le pone cuanto va a medir minimo y cuanto maximo

```
grid-template-columns: repeat(3, minmax(100px, 1fr));
```

# auto-fill

Se van colocando las cajas al lado segun el minmax() que se le ponga porque se van creando más celdas segun el espacio.

```
grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
```

# auto-fit

Se va rellenando el espacio, escalando el tamaño de las celdas.

```
grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));

```

____________________________________________________________________________________________
ALINEACIÓN EN CONTENEDORES

# justify-items

Cambia la posición del contenido horizontalmente y ajusta las celdas al contenido

```
justify-items: normal;
justify-items: stretch;

/* Positional alignment */
justify-items: center;     /* Pack items around the center */
justify-items: start;      /* Pack items from the start */
justify-items: end;        /* Pack items from the end */
justify-items: flex-start; /* Equivalent to 'start'. Note that justify-items is ignored in Flexbox layouts. */
justify-items: flex-end;   /* Equivalent to 'end'. Note that justify-items is ignored in Flexbox layouts. */
justify-items: self-start;
justify-items: self-end;
justify-items: left;       /* Pack items from the left */
justify-items: right;      /* Pack items from the right */

/* Baseline alignment */
justify-items: baseline;
justify-items: first baseline;
justify-items: last baseline;

/* Overflow alignment (for positional alignment only) */
justify-items: safe center;
justify-items: unsafe center;

/* Legacy alignment */
justify-items: legacy right;
justify-items: legacy left;
justify-items: legacy center;

/* Global values */
justify-items: inherit;
justify-items: initial;
justify-items: revert;
justify-items: revert-layer;
justify-items: unset;
```

# align-items

Cambia la posición del contenido verticalmente y ajustan las celdas al contenido

```
/* Palabras Clave Basicas */
align-items: normal;
align-items: stretch;

/* Alineamiento posicional */
/* align-items no considera los valores de "left" o "right"  */
align-items: center; /* Agrupa los elementos alrededor del centro */
align-items: start; /* Agrupa los elementos desde el inicio */
align-items: end; /* Agrupa los elementos desde el final */
align-items: flex-start; /* Agrupa los elementos flex desde el incio */
align-items: flex-end; /* Agrupa los elementos flex desde el final */
align-items: self-start;
align-items: self-end;

/* Alineamiento de Linea Base */
align-items: baseline;
align-items: first baseline;
align-items: last baseline; /* Alineamiento de desborde (solamente para alineamiento posicional) */
align-items: safe center;
align-items: unsafe center;

/* Valores globales */
align-items: inherit;
align-items: initial;
align-items: unset;
```

# justify-content

En grid trabaja con columnas (Es decir de manera horizontal)

```
/* Alinear items flex desde el comienzo */
justify-content: flex-start;

/* Alinear items desde el final */
justify-content: flex-end;

/* Alinear items en el centro */
justify-content: center;

/* Distribuir items uniformemente
El primer item al inicio, el último al final */
justify-content: space-between;

/* Distribuir items uniformemente
Los items tienen el mismo espacio a su alrededor */
justify-content: space-around;

/* Valores globales */
justify-content: inherit;
justify-content: initial;
justify-content: unset;
```

# Align-content

En grid trabaja con la posición de las filas (verticalmente)

```
/* Ajusta las líneas desde el inicio del eje transversal */
align-content: flex-start;

/* Ajusta las líneas desde el final del eje transversal */
align-content: flex-end;

/* Ajusta las líneas al rededor del centro del eje transversal */
align-content: center;

/* Distribuye las líneas a lo largo del eje transversal, de principio a fin */
align-content: space-between;

/* Distribuye las líneas a lo largo del eje transversal, igualmente espaciados */
align-content: space-around;

/* Estira las líneas para que ocupen el eje transversal completo */
align-content: stretch;

/* Valores globales */
align-content: inherit;
align-content: initial;
align-content: unset;
```

____________________________________________________________________________________________
ALINEACIÓN EN ITEMS ESPECIFICOS

# Align self

Que un item se posicione verticalmente

```
.grid-item:first-child{
    align-self: flex-start;
}
```

# justify self

Que un item se posicione horizontalmente

```
.grid-item:first-child{
    justify-self: flex-start;
}
```

# place-self

short hand de justify y align self

```
.grid-item:first-child{
    justify-self: center center;
}
```

# order

Igual que en flex, se prioriza el que tenga el valor más alto. 

```
order: 100;
```
____________________________________________________________________________

# Grid areas

Define un area definidia por más de dos celdas como si fuesen nombres


```
.grid-container {
    background: #444;
    margin: 10px;
    display: grid;
    grid-template-areas: 
    "header header header"
    "aside main main"
    "aside main main"
    "aside main main"
    "aside main main"
    "footer footer footer";
    grid-template-rows: repeat(auto-fill, 1fr);
    height: 90vh;
    border: 5px solid #000;
}

.grid-footer{
    background-color: #5f9;
    grid-area: footer;
}

.grid-header{
    background-color: #f96;
    grid-area: header;
}

.grid-main{
    background-color: #96f;
    grid-area: main;
}

.grid-aside{
    background-color: #888;
    grid-area: aside;
}
```

# Grid lines

Para nombrar a las lineas y poder determinar tamaños con base a estos nombres y no contando

```
.grid-container{
    display: grid;
    background-color: #eee;
    border: 3px solid black;
    grid-template-rows: [f-line] 150px [s-line] 150px [t-line] 150px [l-line];
    grid-template-columns: repeat(3, 1fr); 
}

.grid-item:first-child{
    background: red;
    grid-row: f-line / t-line;
    grid-column: 1 / 4;
}

```
