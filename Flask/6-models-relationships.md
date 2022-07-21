# La relacion entre tablas (models) en flask

Para relacionar las tablas es necesario tener dos clases (que seran las tablas) y a los cuales con relacionamiento SQL se les relaciona con la siguiente linea

```
items = db.relationship('Item', backref='owned_user', lazy=True) 
```

El backref es muy necesario para indicar cómo se va a comportar esta relación

Un ejemplo de relación:

```
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True) #Se instancia la columna con sus respectivos valores
    username = db.Column(db.String(length=30),nullable=False,unique=True) #Se instancia la columna con sus respectivos valores
    email_address = db.Column(db.String(length=70),nullable=False,unique=True) #Se instancia la columna con sus respectivos valores
    password_hash = db.Column(db.String(length=60),nullable=False,unique=True) #COMO ES CONTRASEÑA TIENE QUE SER HASH PARA ENCRIPTARLO Y CON UN LENGTH MAYOR DE 60
    budget = db.Column(db.Integer(),nullable=False,default=1000) #Aqui se crea el saldo de cada persona y se le pone prederminado 1000
    items = db.relationship('Item', backref='owned_user', lazy=True) #Aqui se ponen los items que tiene esta persona al crear una relacion con la otra tabla, y se le asigna que ese producto únio es de esa persona

class Item(db.Model): #Se crea la clase para los items de la base de datos
    id = db.Column(db.Integer(), primary_key=True) #Se instancia la columna con sus respectivos valores
    name = db.Column(db.String(length=30),nullable=False,unique=True) #Se instancia la columna con sus respectivos valores
    price = db.Column(db.Integer(),nullable=False) #Se instancia la columna con sus respectivos valores
    barcode = db.Column(db.String(length=30),nullable=False,unique=True) #Se instancia la columna con sus respectivos valores
    description = db.Column(db.String(length=1024), nullable=False, unique=True) #Se instancia la columna con sus respectivos valores
    owner = db.Column(db.Integer(), db.ForeignKey('user.id')) #Se crea la llave foranea
```

OJO: EN EL FOREIGN TODO ES EN MINNUSCULAAAAAA OJOOOOO