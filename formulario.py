from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired
from wtforms.validators import Length

class Contactenos(FlaskForm):
    nombre = StringField('Nombre',validators=[ DataRequired(message="Este campo es obligatorio"),
                                               Length(max=30)])
    correo = EmailField('Correo',validators=[ DataRequired(message="Este campo es obligatorio")])
    mensaje = StringField('Mensaje',validators=[ DataRequired(message="Este campo es obligatorio")])
    enviar = SubmitField('Enviar mensaje')

