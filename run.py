
from flask import Flask
from flask import  request
from flask import render_template
from flask import flash
import forms
import apalabrados


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/apalabrados/', methods=['GET', 'POST'])
def my_form():
    services = apalabrados
    my_form = forms.MyForm(request.form)
    if request.method == 'POST' and my_form.validate():
        a = my_form.cadena.data
        my_form.cadena.data = None
        services.eveluate(a)
        flash(f'the input {a} was successfully evaluated')
        nums, acums = services.get_numbers()
        tex, ini,fin = services.get_text()
        chars = services.get_char()
        flash(f'numero: {nums}')
        flash(f'acumulado: {acums}')
        flash(f'texto: {tex}')
        flash(f'inicial: {ini}')
        flash(f'final: {fin}')
        flash(f'caracter: {chars}')
    elif not my_form.validate():
        flash('ingrese una cadena de entre 1 y 499 caracteres')

    return render_template('apalabrados.html', form=my_form)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
