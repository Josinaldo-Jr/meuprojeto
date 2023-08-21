from app import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request, flash, session
from app.forms import Contato, Cadastro
from app.models import ContatoModels, CadastroModels
from flask_bcrypt import check_password_hash
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
           
        try:
            name = cadastro.name.data
            email = cadastro.email.data 
            password = cadastro.password.data  
            hash_password = bcrypt.generate_password_hash(password).decode('utf-8')
            novo_cadastro = CadastroModels(name = name, email = email, password = hash_password)
            db.session.add(novo_cadastro)
            db.session.commit()
            flash('Seu cadastro foi realizado com sucesso!')

        except Exception as e:
            flash('Ocorreu um erro ao cadastrar! Entre em contato com o suporte: adm@admin.com')
            print(str(e))

    return render_template('cadastro.html', title='Cadastro', cadastro = cadastro)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = CadastroModels.query.filter_by(email = email).first()
        
        if user and check_password_hash(user.password, password):
            session['email'] = user.email
            session['name'] = user.name
            flash('Seja bem vindo')
            time.sleep(1)
            return redirect(url_for("index"))
        else:
            flash('Senha ou e-mail incorreto!')    


    return render_template('login.html', title='Login')

@app.route('/logout')
def sair():
    session.pop('email', None)
    session.pop('name', None)
    session.pop('password', None)
    return redirect(url_for('login'))


@app.route('/editar', methods=['GET', 'POST'])
def editar():

    if 'email' not in session:
        return redirect(url_for('login'))
    usuario = CadastroModels.query.filter_by(email=session['email']).first()
    
    if request.method == 'POST':
        usuario.name = request.form.get('name')
        usuario.email = request.form.get('email')
        password = request.form.get('password')
        
        if password:  
            usuario.password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        db.session.commit()
        session['email'] = usuario.email
        session['name'] = usuario.name
        
        flash('Seus dados foram editados com sucesso!')
    
    # Descriptografar a senha antes de renderizar o template
    usuario.password = bcrypt.check_password_hash(usuario.password, usuario.password)
    
    return render_template('editar.html', title='Editar Usuário', usuario=usuario)
