from app import app               # variável instanciada classe Flask
from flask import render_template # função interna reindeniza o template para as def's

@app.route('/')
@app.route('/index')
def index():
  nome = 'Dônovan Gomes'
  dados = {"profissao":"Desenvolvedor", "empresa":"DnSistemas"}
  return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
  return render_template('contato.html')