# meta viewport

Es una etiqueta muy necesaria para el responsive, que hace que se puedan realizar diferentes css según el dispositivo

```
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

# @media only screen and (max-width: 800px)

Establece unos cambios cuando se llegue a una resolución menor a la indicada

```
ej:

@media only screen and (max-width: 800px) {
    div {
        display: block;
        width: 100%;
    }
}
```

# Las 4 media query

```
1. All: Apto para todos los dispositivos
2. print: Destinado a material impreso y visualización de docs en una pantalla en el mode de vista previa de impresión.
3. Screen: Destina principal/ a las pantallas
4. Speech: Destinado a sintetizadores de voz
```