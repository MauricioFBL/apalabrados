
from flask import Flask, request, render_template
import forms


app = Flask(__name__)

@app.route('/apalabrados/', methods=['GET','POST'])
def my_form():
    my_form = forms.MyForm(request.form)
    if request.method == 'POST':
        a = my_form.cadena.data
        print(a)
        my_form.cadena.data = None


    return render_template('apalabrados.html', form = my_form)


@app.route('/apalabrados', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

if __name__ == '__main__':
    app.run(port = 5000, debug = True)