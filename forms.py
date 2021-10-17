from wtforms import Form
from wtforms.fields.core import StringField
from wtforms import validators


class MyForm(Form):
    cadena = StringField('Digite cadena a evaluar: ',
                         [validators.length(min=1, max=499,
                                            message='ingrese una cadena de entre 1 y 499 caracteres')])
