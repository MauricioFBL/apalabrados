
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
        flash(f'the string {a} was successfully evaluated')
        flash('numero----acumulado')
        nums, acums = services.get_numbers()
        # for x in range(len(nums)):
        flash(f'numero: {nums}')
        flash(f'acumulado: {acums}')
    elif not my_form.validate():
        flash('ingrese una cadena de entre 1 y 499 caracteres')

    return render_template('apalabrados.html', form=my_form)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
