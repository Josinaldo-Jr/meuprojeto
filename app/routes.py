from app import app
from flask import render_template, url_for, flash, redirect
from app.forms import Contato
import time

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Início')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', title='Sobre')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    formulario = Contato()
    if formulario.validate_on_submit():
        flash('Seu formulário foi enviado com sucesso!')
        time.sleep(2)
        return redirect('/contato')
    return render_template('contato.html', title='Contato', formulario = formulario)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title='Portfólio')