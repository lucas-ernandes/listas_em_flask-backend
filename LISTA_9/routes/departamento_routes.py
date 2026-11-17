from flask import Blueprint, render_template, request
from controllers.departamento_controller import cadastrar_departamento, listar_departamento

departamento_rota = Blueprint('departamento_rota', __name__)

@departamento_rota.route('/departamento/novo')
def novo_departamento():
    return render_template('departamentos/form.html')


@departamento_rota.route('/departamento/salvar', methods=['POST'])
def salvar_departamento():
    numero = request.form['numero']
    nome = request.form['nome']

    cadastrar_departamento(numero, nome)

    return listar_departamentos_view()

@departamento_rota.route('/departamento/departamentos')
def listar_departamentos_view():
    departamentos = listar_departamento()
    
    return render_template('departamentos/lista.html', departamentos=departamentos)
