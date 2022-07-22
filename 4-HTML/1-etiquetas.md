# Etiquetas

```
1. Estructura etiquetas

<etiqueta, atributo="valor">texto</etiqueta>


ej etiqueta: h1
ej atributo: color
ej valor = #fff
ej texto = Soy miguel

2. Hay etiquetas que se abren y no se cierran:

ej:
<br>

3. Hay etiquetas que se abren y se cierran:
<h1></h1>
```

# HTML

1. Estructura basica html

```
<!DOCTYPE html>
<html>
    <head>
        <title></title>
    </head>    
    <body>
        
    </body>
</html>
```

2. Doctype y html

Sirven para indicar la última versión de html y empieza su estructura.

```
<!DOCTYPE html>
<html>
    
</html>
```

3. Head

Ponemos todo lo que no vemos, enlaces, etc

```
<!DOCTYPE html>
<html>
    <head>
        <title></title>
    </head>    
</html>
```

4. Body

Sirve para poner todo lo que vemos, botones, textos, imagenes, etc

```
<!DOCTYPE html>
<html>
    <head>
        <title></title>
    </head>    
    <body>
        
    </body>
</html>
```

5. title

Pone el nombre de la pagina web de la pestaña

```
<title>Este es el titulo en el navegador</title>
```

6. Headres

Son los textos, van del 1 al 6 y entre más grande el número más pequeño. Va en el body.

```
<h1>Hola Mundo</h1>
<h2>Hola Mundo</h2>
<h3>Hola Mundo</h3>
<h4>Hola Mundo</h4>
<h5>Hola Mundo</h5>
<h6>Hola Mundo</h6>
```

7. P

Se usa para parrafos. va en el body

```
<p>Lorem</p>
```

8. b, i, strike
b -> Se usa para Negritas.
i -> Se usa para italica.
strike -> Se usa para tachar texto.
small -> Se usa para poner letra chiquita.

Hay que tener en cuenta que estas etiquetas no completan la linea

```
<b>Negrita</b>
<i>Italica</i>
<strike>Tachada<strike>
<small>Chiquita</small>
```

9. a

Tipo ruta redirije a otra página, que puede ser local (coloca la ruta de la página local) o en otro servidor (https://)

Nota: para devolverse en las carpetas son dos puntos: ../../
```
<a href="link">Click Aqui</a>


Hay otro atributo: target="", que sirve para indicar si se abre otra pestaña o se usa la pestaña actual.

_BLANCK     <- Nueva Pestaña
Vacio       <- En la misma pestaña


Redireccionar a un punto de la página.

<a href="#codigo"></a>

<h2 id="codigo"><h2>
```

10. BR

Nos tira una linea abajo, completa lo que falta de la linea.

```
<p>
Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ea recusandae illo modi optio <br>
saepe doloribus veniam. Numquam fugiat adipisci blanditiis quae alias accusantium recusandae quisquam fuga, aperiam porro quam cum!
</p>
```

11. Listas

Hay dos tipos desordenados y ordenados

```
1. La más usada (desordenada):

<ul>
    <li>Pan</li>
    <li>Huevo</li>
    <li>Leche</li>
    <li>Arroz</li>
</ul>

2. Ordenada (también muy usada):

<ol>
    <li>Pan</li>
    <li>Huevo</li>
    <li>Leche</li>
    <li>Arroz</li>
</ol>
```

12. Multimedia

Imagenes, videos, audios, ect.

```
1. Imagen
<img src="imagen.png" title="Nombre" alt="image">

2. Video
<video src="video.mp4" controls="" alt="image"></video>

3. audio
<audio src="audio.mp3" controls="" alt="image"></audio>
```

13. Div

Son separaciones y agrupaciones de contenido

```
<div></div>
```

14. form

Tiene inputs adentro, información que entra.

```
<form method="Post">
    <input type="text" requiered ="" name="nombre1">   
    <input type="password" name="nombre2">   
    <input type="number" name="nombre3">   
    <input type="email" name="nombre4">   
    <input type="color" name="nombre5">
    <input type="range" min="1" max="5" name="nombre6">
    <input type="date" name="nombre7">
    <input type="time" name="nombre8">
    <input type="button" value="Boton" name="nombre9">
    <input type="submit" name="nombre10">
    <textarea readonly="">Hola como estas</textarea>
</form>
```

15. Metadatos 

Es información que describe recursos. Va en el Head

```
<meta charset="utf-8">
<meta name="keywords" content="harina,leche,huevo,galletas">
<meta name="description" content="Alimentos SAS es una bla bla bla">
<meta name="author" content="Miguel Calvache">
<meta name="copyright" content="Facebook Inc.">
<meta name="robots" content="index">
<meta name="robots" content="fllow">
```

16. Tablas

Son estructuras, fila columna.

```
<table>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>


Los tr son las filas
los td son las columnas
```

17. Iconos

Debe estar en .ico

```
<link rel="icon" href="lucas.ico">
```