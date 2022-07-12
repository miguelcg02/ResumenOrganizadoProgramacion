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