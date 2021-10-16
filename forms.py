from wtforms import Form
from wtforms.fields.core import StringField

class MyForm(Form):
    cadena = StringField('Digite cadena a evaluar: ')

