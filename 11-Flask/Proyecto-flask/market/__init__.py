from flask import Flask, render_template #Se importa la flask y el render_template que es para los html
from flask_sqlalchemy import SQLAlchemy # Se importa la base de datos QLS que será usada
from sqlalchemy import true
from flask_bcrypt import Bcrypt
from flask_login import LoginManager # Es una libreria que permite hacer más facil el login en flask

app = Flask(__name__) #Se instancia la app de Flask. Se pone __name__ que indica el nombre del archivo dinamicamente
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' #Se realiza la configuracion de la base de datos de la aplicacion flask
app.config['SECRET_KEY'] = 'dd61707362225f8e6417f1fe' #Se agrega una secret key por seguridad

db = SQLAlchemy(app) # Se instancia la base de datos que se va a utilizar
bcrypt = Bcrypt(app) #Se instancia para crear los hash encriptados
login_manager = LoginManager(app) # Se instancia la variable con la app

from market import routes