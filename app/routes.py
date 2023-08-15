from app import app, db
from flask import render_template, url_for, flash, redirect, request
from app.forms import Contato, Cadastro
from app.models import ContatoModels, CadastroModels

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
    return render_template('contato.html', title='Contato', formulario = formulario)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title='Portfólio')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    cadastro = Cadastro()

    if cadastro.validate_on_submit():
        flash ('Seu cadastro foi realizado com sucesso!')

        name = cadastro.name.data
        email = cadastro.email.data      
        password = cadastro.password.data  

        novo_cadastro = CadastroModels(name = name, email = email, password = password)
        db.session.add(novo_cadastro)
        db.session.commit()
    return render_template('cadastro.html', title='Cadastro', cadastro = cadastro)


@app.route('/login')
def login():
    return render_template('login.html', title='Login')