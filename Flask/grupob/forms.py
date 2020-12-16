from wtforms import Form, BooleanField, StringField, PasswordField, validators, TextField
from wtforms.fields.html5 import EmailField 




class Crearegistro(Form):
    username= TextField('username',
        [
            validators.Required(message='El nombre de suuario es requerido'),
            validators.length(min=4, max=50, message='Ingrese un nombre de usuario valido')
        ])
    
    email = EmailField('email',
        [
            validators.required(message='El correo es requerido.'),
            validators.email(message='Ingrese un correo valido'),
            validators.length(min=4, max=50, message='Ingrese un correo valido')    
        ])

    password = PasswordField('password', [validators.required(message='La contraseña es incorrecta')])
