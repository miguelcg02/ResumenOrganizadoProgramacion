# Para utilizar SQL

Instalar sql alchemy

```
conda install -c conda-forge flask-sqlalchemy
```

Ahora podremos escribir tablas sql

# Colocar el import en el archivo py para bases de datos SQL

Se hace el import y se crea su variable para ser usada

```
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
```

# Creacion de models para la base de datos

Se crea una clase Item para guardar la información, al que se le pasa como parametro la variable db.Model, luego se crean las columnas, al que le debe determinar el tipo y el largo, si puede ser null y si es unico.

```
name = db.Column(db.String(length=30),nullable=False,unique=True)
```

Para primary keys

```
id = db.Column(db.Integer(), primary_key=True)
```

# Configurar la base de datos de la app

Es necesario indicarle donde va a estar esta información de la base de datoss, para eso se debe de configurar de la siguiente manera. Se crea un diccionario que apunta a la base de datos que se va a crear

```
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
```

# Crear db desde el CMD

Por estos pasos se accede a la base de datos para crear el archivo

```
1. Localizarnos en el archivo del proyecto
2. Entrar al power shell de python Escribir el comando: python
3. Realizar la importanción de la base de datos que vamos a crear: from market import db
OJO: se coloca market porque así se llama el archivo, y se importa db porque ese es el nombre de la variable
4. Escribir la linea: db.create_all()
5. Se va a crear un archivo .db en el proyecto
6. Refernciar a donde se van a crear los objetos al escribir: from market import Item
7. Crear los objetos: item1 = item(name="IPhone 10", price=500, barcode='8923828492382',description='desc')
OJO: El id no es necesario ponerlo, se crea solito
8. Agregar los items a la base de datos con la linea: db.session.add(item1)
9. Confirmar la agregada: db.session.commit()
10. Revisar si se agrego: item.query.all()
11. Agregar más datos
12. Para salir con: exit()
```

Nota: REVISE QUE TODO LO DEL CÓDIGO ESTE BIEN ESCRITOOO

# Cambiar visualización de los matos con __repr__

Se usa la función magica __repr_ _ para una mejor visualización

```
def __repr__(self):
    return f'Item{self.name}'
```

# Iterar sobre los items

```
1. Localizarnos en el archivo del proyecto
2. Entrar al power shell de python Escribir el comando: python
3. Realizar la importanción de la base de datos: from market import Item
4. Realizar la iteración: for item in Item.query.all():
5. Agregar lo que se quiere ver: 
  item.name
  item.id
  item.price
  item.barcode
  item.description
OJO: Es necesario identar lo que se quiere ver
```

# Meter filtros en las busquedas

```
1. Localizarnos en el archivo del proyecto
2. Entrar al power shell de python Escribir el comando: python
3. Realizar la importanción de la base de datos: from market import item
4. Especificar la busqueda con una iteración: for item in Item.query.filter_by(price=500):
5. Colocar los items que se quieren ver: 
  item.name
  item.id
```

# Actualizar la información de la ruta

Cómo ya estamos utilizando una base de datos, ya se debe de cambiar el diccionario creado por la base de datos de la siguiente forma. Usando el item.query.all()

```
@app.route('/market')
def market_page():
    items = item.query.all()
    return render_template('market.html', items=items)
```

1h 51min