from market import app #Se importa del __init_ _ app
from flask import render_template #Se importa la lectura de templates de flask
from market.models import Item #Se importa la clase Item creada en models

@app.route('/') #Se crea la ruta por defecto
@app.route('/home') #A esta ruta por defecto se le crea una que también redirige a esta
def home_page(): #Se crea la función, que permite que se trabaje dinamicamente
    return render_template('home.html') #Se indica cual es el template que tendra esta ruta (OJO: porque la caprte donde se guardan los html obligatoriamente se debe llamar 'templates')

@app.route('/about/<username>') #Se puede trabjaar dinamicamente con las rutas
def about_page(username): #Se crea la funcion con el parametro de la ruta
    return f'<h1>This is the about page of {username}</h1>' #Se puede usar dinamicamente este parametro

@app.route('/market') #Se crea la ruta market
def market_page(): #Se crea la función, que permite que se trabaje dinamicamente
    items = Item.query.all() #Se instancia una variable con todos los datos de la bse de datos sql del creado en  models.py
    return render_template('market.html', items=items) #Se le pasa el codigo html y la base de datos

