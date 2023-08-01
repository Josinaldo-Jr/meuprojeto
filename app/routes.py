from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Início')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', title='Sobre')

@app.route('/contato')
def contato():
    return render_template('contato.html', title='Contato')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title='Portfólio')