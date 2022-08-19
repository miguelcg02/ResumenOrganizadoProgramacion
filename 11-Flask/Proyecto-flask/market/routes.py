from curses import flash
from sre_constants import SUCCESS
from unicodedata import name

from regex import F
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
from flask_login import login_user #Se importa una clase que ayuda con el login
from flask_login import logout_user #Se importa una clase que facilita realizar el logout
from flask_login import login_required #Decoratos: una funcion que se ejecuta antes que sus propias funcionalidades, requiere que para entrar a una parte, se requiera el login antes
from market.forms import PurchaseItemForm 
from market.forms import SellItemForm
from flask import request # Da el control sobre la información de los inputs que se esten realizando
from flask_login import current_user # Se puede usar las funciones sobre el usuario que esta conectada actualmente

@app.route('/') #Se crea la ruta por defecto
@app.route('/home') #A esta ruta por defecto se le crea una que también redirige a esta
def home_page(): #Se crea la función, que permite que se trabaje dinamicamente
    return render_template('home.html') #Se indica cual es el template que tendra esta ruta (OJO: porque la caprte donde se guardan los html obligatoriamente se debe llamar 'templates')



@app.route('/about/<username>') #Se puede trabajar dinamicamente con las rutas
def about_page(username): #Se crea la funcion con el parametro de la ruta
    return f'<h1>This is the about page of {username}</h1>' #Se puede usar dinamicamente este parametro



@app.route('/market' ,methods=['GET','POST']) #Se crea la ruta market
@login_required #Solo se puede acceder si se esta logeado, lo que lleva automaticamente al login
def market_page(): #Se crea la función, que permite que se trabaje dinamicamente
    purchase_form = PurchaseItemForm()
    selling_form = SellItemForm()

    if request.method == "POST": #Revisa el estado del request sobre si esta realizando algún post
        
        # PURCHASE LOGIC
        
        purchased_item = request.form.get('purchased_item') #Se obtiene la información dle item que se quiere comprar, viene del input que esta en items_modlas
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        
        if p_item_object:
            if current_user.can_purchase(p_item_object): #Revisa si tiene el dinero suficiente al llamar a una función que esta ubicada en models para comparar los fondos con el precio del item
                p_item_object.buy(current_user) #Se llama a la funcion comprar que esta creada en models Item para realizar el proceo de compra
                flash(f'Purchase sucessfully of {p_item_object.name} for {p_item_object.price}$',category="success") # Indica al usuario que pudo comprar el item
            else:
                flash(f"You don't have enough money to purchase {p_item_object.name}", category="danger") # Indica al usuario que no tiene plata suficiente para comprar el item

        # SELL ITEM LOGIC

        sold_item = request.form.get('sold_item') # Al igual que purchase, viene del input en owned_items_modlas
        s_item_object = Item.query.filter_by(name=sold_item).first()

        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(f'Sell sucessfully of {s_item_object.name} for {s_item_object.price}$',category="success") # Indica al usuario que pudo comprar el item
            else:
                flash(f"Something went wrong selling {p_item_object.name}", category="danger") # Indica al usuario que no tiene plata suficiente para comprar el item

        return redirect(url_for('market_page'))

        

    if request.method == "GET":
        items = Item.query.filter_by(owner=None) #Se instancia una variable con todos los datos de la bse de datos sql del creado en models.py con los items sin dueño
        owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template('market.html', items=items, purchase_form=purchase_form, owned_items=owned_items, selling_form=selling_form) #Se le pasa el codigo html y la base de datos



@app.route('/register', methods=['GET','POST']) #Se crea la ruta register y se especifica los tipos de acciones que puede hacer, hacer GET y POST
def register_page(): #Se crea la función, que permite que se trabaje dinamicamente
    form = RegisterForm() #Se crea el atributo form con el RegisterForm creado en modelsmarket.forms
    if form.validate_on_submit(): # Verificar que la información entrada al formulario sea enviada cuando se presiona el boton submmit y crear unas validacion
        user_to_create = User(username = form.username.data, # Se crea el objeto para crear usuarios en el forms
                              email_address = form.email_address.data,
                              password = form.password1.data) # Se le pasa el password 1 OJOOO
        db.session.add(user_to_create) #Se agrega el usuario a la base de datos
        db.session.commit() #Se confirman los cambios
        
        login_user(user_to_create) #Funcion que indica el usuario que acaba de entrar
        flash(f'Account created succesfully! You are register as {user_to_create.username}', category='success') #Muestra mensajes al usuario, en este caso para indicar que entro conrrectamente

        return redirect(url_for('market_page'))

    if form.errors != {}: #Pregunta que si hay errores desde la  validación
        for err_msg in form.errors.values(): #Iterar sobre el diccionario
            flash(f'There was a problem creating the user: {err_msg}', category='danger') #Hace que cuando haya un mensaje que queramos poner luego lo podamos tirar

    return render_template('register.html', form=form) #Se crea el template y s emanda la info de form



@app.route('/login', methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit(): # Revisa si la información es valida
        attempted_user = User.query.filter_by(username=form.username.data).first() # Recibe la información del usuario que se agrega en la casilla username
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data): # Se revisa si hay usuario o si es none, y se revisa la contraseña encriptada con un metodo creado en models por mi que devuelve un true or false
            login_user(attempted_user) #Funcion que indica el usuario que acaba de entrar
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success') #Muestra mensajes al usuario, en este caso para indicar que entro conrrectamente
            return redirect(url_for('market_page')) #Mandar al usuario a la pestaña de market
        else:
            flash('Username and password are not match, try again!', category='danger') # Indicar el mensaje de que se equivoco el muchacho metiendo los datos y el tipo de categoria flash

    return render_template('login.html', form=form)



@app.route('/logout')
def logout_page():
    logout_user() #Que saque al usuario de la pagina
    flash('You haven logged out succesfully!', category='info') #Informarle al usuario que se salio
    return redirect(url_for("home_page")) #Lo manda de vuelta a home
