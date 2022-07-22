from flask import Flask, render_template #Se importa la flask y el render_template que es para los html
from flask_sqlalchemy import SQLAlchemy # Se importa la base de datos QLS que será usada
from sqlalchemy import true

app = Flask(__name__) #Se instancia la app de Flask. Se pone __name__ que indica el nombre del archivo dinamicamente
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' #Se realiza la configuracion de la base de datos de la aplicacion flask

db = SQLAlchemy(app) # Se instancia la base de datos que se va a utilizar

from market import routes