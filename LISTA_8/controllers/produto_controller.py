from flask import render_template, request, redirect, url_for
from models.produto import Produto

def exibir_form():
    return render_template('cadastro.html')

def processar_cadastro():
    codigo = request.form['codigo']
    descricao = request.form['descricao']
    valor = request.form['valor']

    produto = Produto(codigo, descricao, valor)

    produto.armazenar()
    
    return redirect(url_for('produto.produtos'))

def listar_produtos():
    produtos = Produto.buscar_todos()

    return render_template('listagem.html', produtos=produtos)

'''
controller --> recebe os dados --> cria Produto --> manda o Produto para o model
--> Model armazena
'''

#def listar_produtos():
'''
controller --> pede os produtos ao Model --> recebe a lista
--> manda a lista para o HTML
'''
