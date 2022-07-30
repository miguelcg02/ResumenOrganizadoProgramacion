from curses import flash
from market import app #Se importa del __init_ _ app
from flask import render_template #Se importa la lectura de templates de flask
from market.models import Item #Se importa la clase Item creada en models
from market.forms import RegisterForm #Se importa la clase RegisterForm creada en forms
from market.models import User # Importar la clase Usuario para crearlos al llenar el form
from market import db #Se importa el db directamente, esto porque el db esta ubicado directamente en market init 
from flask import redirect #Libreria que sirve para mandar a los usuarios al hacer una determinada acción
from flask import url_for #Sirve para anunciar las funciones de las rutas al poner urls
from flask import flash #Sirve para crear un mensaje al hacer una acción
from market.forms import LoginForm #Se importa la clase RegisterForm creada en forms



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

@app.route('/register', methods=['GET','POST']) #Se crea la ruta register y se especifica los tipos de acciones que puede hacer, hacer GET y POST
def register_page(): #Se crea la función, que permite que se trabaje dinamicamente
    form = RegisterForm() #Se crea el atributo form con el RegisterForm creado en modelsmarket.forms
    if form.validate_on_submit(): # Verificar que la información entrada al formulario sea enviada cuando se presiona el boton submmit y crear unas validacion
        user_to_create = User(username = form.username.data, # Se crea el objeto para crear usuarios en el forms
                              email_address = form.email_address.data,
                              password = form.password1.data) # Se le pasa el password 1 OJOOO
        db.session.add(user_to_create) #Se agrega el usuario a la base de datos
        db.session.commit() #Se confirman los cambios
        return redirect(url_for('market_page'))
    if form.errors != {}: #Pregunta que si hay errores desde la  validación
        for err_msg in form.errors.values(): #Iterar sobre el diccionario
            flash(f'There was a problem creating the user: {err_msg}', category='danger') #Hace que cuando haya un mensaje que queramos poner luego lo podamos tirar

    return render_template('register.html', form=form) #Se crea el template y s emanda la info de form

@app.route('/login', methods=['GET','POST'])
def login_page():
    form = LoginForm()
    return render_template('login.html', form=form)