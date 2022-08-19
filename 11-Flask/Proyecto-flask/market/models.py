from market import db #Se imoprta la db creada en __init__
from market import bcrypt
from market import login_manager # Es una libreria que esta en init para gestionar los login correctamente
from flask_login import UserMixin # Le agrega funcionalidades que deben ser agregadas al modelo de usuario para un correcto uso del login



@login_manager.user_loader #Con estas lineas se esta gestionando los usuarios que ya han ingresado al sistema
def load_user(user_id):
    return User.query.get(int(user_id)) #Esta linea esta recibiendo de la base de datos el usuario ingresado


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True) #Se instancia la columna con sus respectivos valores
    username = db.Column(db.String(length=30),nullable=False,unique=True) #Se instancia la columna con sus respectivos valores
    email_address = db.Column(db.String(length=70),nullable=False,unique=True) #Se instancia la columna con sus respectivos valores
    password_hash = db.Column(db.String(length=60),nullable=False,unique=True) #COMO ES CONTRASEÑA TIENE QUE SER HASH PARA ENCRIPTARLO Y CON UN LENGTH MAYOR DE 60
    budget = db.Column(db.Integer(),nullable=False,default=1000) #Aqui se crea el saldo de cada persona y se le pone prederminado 1000
    items = db.relationship('Item', backref='owned_user', lazy=True) #Aqui se ponen los items que tiene esta persona al crear una relacion con la otra tabla, y se le asigna que ese producto únio es de esa persona

    @property
    def prettier_budget(self): #Para poner bonito como muestra la plata con comas
        if len(str(self.budget)) >= 4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}'
        else:
            return f'{self.budget}'

    @property
    def password(self):
        return self.password

    @password.setter #Con un setter esta cambiando la contraseña para poder encriptarla
    def password(self, plain_text_password): 
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8') #Esta encriptando la contraseña
    
    def check_password_correction(self, attempted_password): # Esta revisando si el pssword ingresado por el usuario si es el correcto
        return bcrypt.check_password_hash(self.password_hash, attempted_password) # Es una funcion que recibe la variable con la contraseña encriptada y la contraseña intentada para compararlas, si son iguales sera true, si no false

    def can_purchase(self, item_obj):
        return self.budget >= item_obj.price

    def can_sell(self, item_obj):
        return item_obj in self.items # Indica si el item esta en la lista de items del usuario

    def __repr__(self): #Es una función especial para configurar el retorno de los elementos pedidos en la base de datos con la función nombre_clase.query.all()
        return f'User {self.username}'



class Item(db.Model): #Se crea la clase para los items de la base de datos
    id = db.Column(db.Integer(), primary_key=True) #Se instancia la columna con sus respectivos valores
    name = db.Column(db.String(length=30),nullable=False,unique=True) #Se instancia la columna con sus respectivos valores
    price = db.Column(db.Integer(),nullable=False) #Se instancia la columna con sus respectivos valores
    barcode = db.Column(db.String(length=30),nullable=False,unique=True) #Se instancia la columna con sus respectivos valores
    description = db.Column(db.String(length=1024), nullable=False, unique=True) #Se instancia la columna con sus respectivos valores
    owner = db.Column(db.Integer(), db.ForeignKey('user.id')) #Se crea la llave foranea de la clase user con la clase Item y OJO EN MINUSCULAAAAAA

    def __repr__(self): #Es una función especial para configurar el retorno de los elementos pedidos en la base de datos con la función nombre_clase.query.all()
        return f'Item {self.name} price {self.price}'#En este caso se le manda el self.name, es decir solo el nombre, de la busqueda

    def buy(self, user):
        self.owner = user.id #Como a los items se les asigna el id del usuario, se hace de esta forma
        user.budget -= self.price
        db.session.commit()

    def sell(self, user):
        self.owner = None
        user.budget += self.price
        db.session.commit()

    