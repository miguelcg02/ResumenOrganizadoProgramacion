# flask forms

instalar package necesario que nos permite crear forms lindos y luego desplegarlos en los html templates

```
conda install flask-wtf
```

instalar siguiente package

```
conda install wtforms
```

crear un nuevo archivo para los forms que trabajara parecido a los models

```
crear forms.py
```

importar en forms.py los paquetes

```
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
```

Esta libreria es especial para hacer formularios donde se puede colocar la información que se desee para el formulario

```
class RegisterForm(FlaskForm):
    username = StringField(label='username')
    email_address = StringField(label='email')
    password1 = PasswordField(label='password1')
    password2 = PasswordField(label='password2')
    submit = SubmitField(label='submit')
```

Ahora se crea la ruta y se importa la clase con el form

```
from market.forms import RegisterForm #Se importa la clase RegisterForm creada en forms

@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)

```

Se crea el template register con el código jinja

```
{% extends 'base.html'%}
{% block title%}
Register Page
{%endblock%}

{% block content %}

{% endblock %}
```

Por seguridad en la base de datos se debe crear una llave especial para evitar inserts en la base de datos, para generarlos es de la siguiente manera:

```
python
import os
os.urandom(12).hex()
```

El resultado se pega agregandolo al __init_ _.py de la siguiente manera:

```
app.config['SECRET_KEY'] = 'dd61707362225f8e6417f1fe'
```

Continuar con el código jinja del contenido. Se coloca 

```
{% block content %} 
<body class="text-center">
    <div class="container">
        <form method="post" class="form-register" style="color:white"> <!-- El metodo post afecta la base de datos y se debe declarar el tipo de metodo  -->
            
            <h1 class="h3 mb-3 font-wight-normal">
                Please Create Your Account
            </h1>
            <br>
            {{form.username.label()}} <!-- Esta poniendo el tag de username, se pone el label que le pusimos en el forms-->
            {{form.username(class="form-control", placeholder="User name")}} <!-- Se crea el campo de username -->
            
            {{form.email_address.label()}} <!-- Esta poniendo el tag de username, se pone el label que le pusimos en el forms-->
            {{form.email_address(class="form-control", placeholder="Email Address")}} <!-- Se crea el campo de username -->
        
            {{form.password1.label()}} <!-- Esta poniendo el tag de username, se pone el label que le pusimos en el forms-->
            {{form.password1(class="form-control", placeholder="Password")}} <!-- Se crea el campo de username -->

            {{form.password2.label()}} <!-- Esta poniendo el tag de username, se pone el label que le pusimos en el forms-->
            {{form.password2(class="form-control", placeholder="Confirm Password")}} <!-- Se crea el campo de username -->

            <br>
            {{form.submit(class="btn btn-lg btn-block btn-primary")}} <!-- Se crea el campo de username -->

        </form>
    </div>
</body>
{% endblock %}
```
