# Instalación Django local vs instalación virtual

1. Local

- Unica versión de Django
- Unica versión de python
- Mismas dependencias para todos los proyectos

2. Virtual

- varias versiones de Django
- varias versiones de python
- diferentes dependencias para todos los proyectos
- igualar entornos de desarrollo-pruebas-producción

# Comenzar

```
django-admin startproject nombre_proyecto
```

- manage.py: utilidad de linea de comandas que permite interactuar con los proyectos django
* subcarpeta
- init.py: archivo para que se ejecute como un paquete
- settings.py: contiene las configuración
- url.py: almacena las urls es como un indice
- wsgi.py: es relativo al servidor web creado para django

# Setting.py

* trae todos las apps instaladas

# Migrar para activar el proyecto

Desde la carpeta proyecto1

```
python manage.py migrate
```

se crea la base de datos sqlite3

# Subir servidor

```
python manage.py runserver
```

Ahora aparece la linea de la dirección de la pagina web