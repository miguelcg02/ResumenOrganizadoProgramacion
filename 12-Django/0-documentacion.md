# Datos curiosos de la documentación de Django

1. Urls dinamicas

Es una forma de crear contenidos de una manera muy util donde no es necesario crear una dirección URL por cada contenido, si no que se crea una con una misma plantilla para varios contenidos. puede ser muy util para crear blogs, espacios de noticias, páginas de documentación, etc.

urls.py
```py
from django.urls import path

from . import views

urlpatterns = [
    path("articles/<int:year>/", views.year_archive),
    path("articles/<int:year>/<int:month>/", views.month_archive),
    path("articles/<int:year>/<int:month>/<int:pk>/", views.article_detail),
]
```

views.py
```py
from django.shortcuts import render

from .models import Article


def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {"year": year, "article_list": a_list}
    return render(request, "news/year_archive.html", context)
```

2. Crear funciones dentro de los modelos.

Se pueden crear funciones dentro de los modelos y luego invocarlos facilmente. Es muy util para crear verificaciones como por ejemplo si es mayor de edad.

models.py
```py
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```

```py
# Make sure our custom method worked.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True
```

3. get_object_or_404()

Es una alternativa al get() de objetos y retorna un Http404 si el objeto no existe. También ha una get_list_or_404() que usa un filter() en lugar de get para listas.

```py
from django.shortcuts import get_object_or_404, render

from .models import Question

# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
```

4. Trabajar correctamente las URLs en templates

En caso de que se modifique el nombre de una URL, la forma correcta de tenerla en los templates para no tener que cambiar ese nombre en todas las plantillas es así:

urls.py:
```py
...
# the 'name' value as called by the {% url %} template tag
path("<int:question_id>/", views.detail, name="detail"),
...
```

Plantilla de alguna template de una aplicación concreta es:
```html
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

De esta forma, usando el {% url %} se puede trabajar dinamicamente basandose unicamente en el name dado en urls.py de la aplicación concreta. ('polls' es la aplicación y 'detail' el nombre dado de la url en urls.py)

5. forloop.counter

```html
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
{% endfor %}
```

forloop.counter, indica cuántas veces la etiqueta for ha pasado por el bucle sirviendo como contador.

6. static

Para usar archivos estaticos que no tengan interferencia al hacer el despliegue o para referenciarlos de la manera adecuada, se debe hacer de la siguiente manera:

Primero cree un directorio llamado 'static' en su directorio de la aplicación. Del modo como se creo el directorio 'templates'

Dentro del directorio 'static', se recomienda crear otro directorio con el nombre de su aplicación para que django pueda diferenciar facilmente entre todos los directorios 'static' de sus diferentes aplicaciones si es que usted crea varios archivos con el mismo nombre y pueda diferenciarlos entre las distintas aplicaciones. Ej: nombre_app/static/nombre_app/style.css

Luego cuando se quiera referenciar a ese archivo static será tan sencillo como hacerlo de la siguiente manera.

```html
{% load static %}

<link rel="stylesheet" href="{% static 'nombre_app/style.css' %}">
```

Así, la etiqueta de plantilla {% static %} genera la URL absoluta de los archivos estáticos y ya todo queda bonito.


