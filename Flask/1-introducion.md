# Aplicaci+on minima

Con las siguientes lineas se esta importando el paquete de flask, y a su vez se instancia la variable app, la cual tiene una función llamada Flas con la variable __name_ _ adentro (esta variable devuelve el nombre del archuvo de python que se esta utilizando). Despues se esta especificando la ruta de la website con ese decorador. Despues se tiene la función que genera el hello world

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

# Montar el servicio

Con las siguientes lineas de comando en la terminal se monta el servicio de flask con respecto al archivo que creamos y estando en la carpeta donde tenemos el proyecto

```
set FLASK_APP=nombre_archivo.py
$env:FLASK_APP = "nombre_archivo.py"
python -m flask run
```

Para recargar los cambios volver a escribir: python -m flask run

Pero para que sea automatico tirar las lineas: 

```
set FLASK_DEBUG=1
$env:FLASK_DEBUG="1"
python -m flask run
```

# Para crear rutas

Estas son las rutas que se crean en la web, y esta es la estructura

```
@app.route('/nombre_de_la_ruta')
def nombre_de_la_funcion():
    return 'CONTENIDO'
```

# Dynamic routes

Se crean cantidad de rutas que se quieran de forma dinamica. Primero en la ruta se determina la variable en <> y en la función se recibe de parametro una variable y en el retorno se trabaja de manera dinamica con este parametro.

```
@app.route('/about/<username>')
def abput_page(username):
    return f'<h1>This is the about page of {username}</h1>'
```

# Modularización

La mejor forma de trabjar es teniendo todo separado, en vez de tener largas lineas de código juntas.

```
crear una nueva carpeta llamada templates (OJO QUE ASI SE DEBE DE LLAMAR) para agregar los archivos html
```

ahora la idea es retornar en la función el nuevo archivo html.

```
@app.route('/')
def hello_world():
    return render_template('home.html')
```

Pero antes es necesario importar esa función del mismo flask

```
from flask import Flask, render_template
```

# Importar estilos en getbootstrap

```
https://getbootstrap.com/docs/4.5/getting-started/introduction/
```

# Agregar un nuevo comando de busqueda a la función

De esta forma buscando de ambas maneras tirará el mismo resultado

```
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')
```


