# ¿Que es?

La idea es crear una plantilla en html para no tener que estar copiando la misma información una y otra vez por cáda pestaña nueva, y crear una base que sea heredada para las siguientes plantillas html.

Se crea esa base en html y en la proxima plantilla html se hereda de esta forma:

```
{% extends 'base.html'%}
```

En la plantilla base se coloca la información que estara en todas las plantillas, por ej el nav. Pero se tiene que tener en cuenta que información será general y cual será único por cada plantilla

# Colocar información unica

En la plantilla base se creará una lineas de la sintaxis jinja para identificar las zonas que serán alteradas en otras plantillas
Ej con el titulo de la página.

En la plantilla base:

```
<title>
    {% block title%}

    {%endblock%}
</title>
```

se crea este código jinja que especifica que habrá un bloque de código que será unico en cada plantilla, y este se especifica con el nombre title (Puede ser cualquier nombre)
Luego, en la plantilla nueva, para agregar el nuevo titulo se pone

```
{% extends 'base.html'%}
{% block title %}
    Home Page
{% endblock %}
```

Se esta especificando la plantilla base y la parte del código que es único por la palabra title que se definió desde la plantilla base. Tambien se puede poner html dentro

# Para redirigir usando la tag <a> con código jinja

En el href, se pondrá código jinja para redirigir con buenas practicas. Indicando en la función la función de la app.route que es usada para cada redirección. Asi si se cambia la ruta, la función se mantiene.

```
<a class="nav-link" href="{{ url_for('home_page') }}">Home <span class="sr-only">(current)</span></a>
```