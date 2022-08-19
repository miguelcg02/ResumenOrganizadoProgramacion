from shutil import unregister_unpack_format
from flask_wtf import FlaskForm
from jsonschema import ValidationError
from matplotlib.pyplot import cla  #Se importa el Flaskform que es el que se coloca de parametro en la clase
from wtforms import StringField #Es un atributo especial para las cajas string
from wtforms import PasswordField #Es un atributo especial para las cajas password
from wtforms import SubmitField #Es un atributo especial para los botones submit
from wtforms.validators import Length  # Es una clase importada que valida el largo del contneido del form 
from wtforms.validators import EqualTo  # Es una clase importada que valida si un field es igual a otra 
from wtforms.validators import Email  # Es una clase importada que valida si un field es un email
from wtforms.validators import DataRequired  # Es una clase importada que valida si un field tiene algun tipo de información dentro
from market.models import User #Importa los usuarios creados
from wtforms.validators import ValidationError  # Es una clase importada que crea un error para atraparlo antes


class RegisterForm(FlaskForm): # Crea la clase para el forma de registro
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first() #Le pregunta si existe un usuario con el nuevo que se qquiere crear
        if user: # Revisa si ya existe un user
            raise ValidationError('Username already exists! Try a different username') #Crea un error desde antes para que lo atrapemos antes

    def validate_email_address(self, email_address_to_check):
        email = User.query.filter_by(email_address=email_address_to_check.data).first() #Le pregunta si existe un usuario con el nuevo que se quiere crear
        if email: # Revisa si ya existe un email
            raise ValidationError('This email is already been used!') #Crea un error desde antes para que lo atrapemos antes

    username = StringField(label='User Name',validators=[Length(min=2,max=30), DataRequired()]) # Crea el field para llenar el nombre de usuario con sus validadores
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()]) # Crea el field para llenar el email
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()]) # Crea el field para llenar el password
    password2 = PasswordField(label='Confirm Password:',validators=[EqualTo('password1'), DataRequired()] ) # Crea el field para llenar la confirmación de password con la validación de si los dos fields de password sson iguales
    submit = SubmitField(label='Create Account') # Crea el boton de submit que agarra los datos del field

class LoginForm(FlaskForm):
    username = StringField(label='Username:', validators=[DataRequired()]) # Al igual que el register se hace de esta manera
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase item!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell item!')