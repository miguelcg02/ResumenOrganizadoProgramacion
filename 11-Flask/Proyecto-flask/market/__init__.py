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
login_manager. login_view = "login_page" #Le indica a la pagina que esa es la pestaña de login, es decir, si se va a meter a una pestaña que necesita inicio de sesión lo rebota primero a la pestaña de login en caso de no esta logeado
login_manager.login_message_category ="info" #Se le coloca un mensaje automatico para que haga login

from market import routes