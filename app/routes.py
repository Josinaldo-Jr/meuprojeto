from app import app, db
from flask import render_template, url_for, flash, redirect, request
from app.forms import Contato
from app.models import ContatoModels 
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

    if formulario.validate_on_submit:
        flash ('Seu formulário foi enviado com sucesso!')

        name = formulario.name.data
        email = formulario.email.data
        phone = formulario.phone.data
        message = formulario.message.data
        novo_contato = ContatoModels(name = name, email = email, phone = phone, message = message)
        db.session.add(novo_contato)
        db.session.commit()

        # dados_formulario = {
        #     'name': name,
        #     'email': email,
        #     'phone': phone,
        #     'message': message
        # }

        # for chave, valor in dados_formulario.items():
        #     print(f'{chave}: {valor}')
    return render_template('contato.html', title='Contato', formulario = formulario, dados_formulario = dados_formulario)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title='Portfólio')