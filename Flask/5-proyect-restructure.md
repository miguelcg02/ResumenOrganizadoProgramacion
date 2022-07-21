# Restructurar los codigo

Se organizan los archivos con sus respectivas funciones, así como se hizo con los templates, se hace con las archivos de python

```
crear carpetas:

models: para las bases de datos
routes: para las rutas
run: encargado de ejecutar la aplicación por el tema de los importes
```

# Circular imports

Se crea un paquete que permita ejecutar de forma organizada la aplicación, donde se sepa que variables de diferentes archivos seran utilizados en otros archivos. Por lo que ya se puede borrar el archivo market.py porque la infromación estará en un nuevo archivo que se creara más adelante llamado __init_ _

```
Se crea la nueva carpeta market y se mete adentro: 
-La carpeta templates
-La base de datos market.db
-El archivo models.py que es el que crea la bdd
-El archivo routes.py que es el que crea las rutas
```

Cuando se trabaja con packeges en python se debe crear un archivo llamado __init_ _que cuando se importa se ejecuta instantaneamente, este archivo tendrá lo que tenía antes el archivo market.py

Ahora en el run.py se agregan las siguientes lineas de código

```
from market import app 

if __name__ == '__main__':
    app.run(debug=True) 
```

Hay que hacer muchas importaciones entre los archivos

```
En __init__.py:

from market import routes

En routes: 

from market import app
from flask import render_template
from market.models import Item

En models:

from market import db
```

Nota: como casi todo esta en el __init_ _ solo es necesario colocar 'from market import ...' ya que esta es la que es por defecto, si se quisiera importar algo que no esta en el __init_ _ se hace 'from market.nombre_archivo import clase_o_variable'


