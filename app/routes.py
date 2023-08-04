from app import app
from flask import render_template, url_for, flash, redirect, request
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
    dados_formulario = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        dados_formulario = {
            'name': name,
            'email': email,
            'phone': phone,
            'message': message
        }

    return render_template('contato.html', title='Contato', formulario = formulario, dados_formulario = dados_formulario)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title='Portfólio')