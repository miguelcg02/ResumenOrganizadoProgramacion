# Introduccion

* CSS

1. Layout: Contiene código para acomodar el código html: Usa flex-box, grid, etc.

2. Content: Permite meter estilos personalizados a las etiquetas

3. Components: Permite colocar carruseles, mensajes, apartados, etc

4. Utilities: Código para meter color, bordes, opacidad, etc

# Pasar por CDN

CSS: https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css

JS: https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js

```
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
  </head>
  <body>
    <h1></h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
  </body>
</html>
```

- El Scrpit de JS es mejor que vaya al meeeero final para evitar problemas