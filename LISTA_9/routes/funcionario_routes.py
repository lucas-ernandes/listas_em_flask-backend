from flask import Blueprint, render_template, request
from controllers.funcionario_controller import( cadastrar_funcio, listar_funcionario, consultar_por_departamento)
from controllers.departamento_controller import listar_departamento

funcionario_rota = Blueprint('funcionario_rota', __name__)

@funcionario_rota.route('/funcionario/novo')
def novo_funcionario():
    departamentos = listar_departamento()

    return render_template('funcionarios/form.html', departamentos=departamentos)


@funcionario_rota.route('/funcionario/salvar', methods=['POST'])
def salvar_funcionario():
    codigo = request.form['codigo']
    nome = request.form['nome']
    numero_departamento = request.form['departamento']

    departamentos = listar_departamento()
    
    departamento_selecionado = None
    
    for departamento in departamentos:
        if str(departamento.numero) == numero_departamento:
            departamento_selecionado = departamento
            break
    
    cadastrar_funcio(
        codigo, nome, departamento_selecionado
    )
    return listar_funcionarios_view()


@funcionario_rota.route('/funcionario/funcionarios')
def listar_funcionarios_view():
    funcionarios = listar_funcionario()
    
    return render_template('funcionarios/lista.html', funcionarios=funcionarios)


@funcionario_rota.route('/funcionario/consulta')
def consulta_funcionario():
    departamentos = listar_departamento()

    return render_template(
        'funcionarios/consulta.html',
        departamentos=departamentos
    )
    
    
@funcionario_rota.route('/funcionario/consultar', methods=['POST'])
def consultar_funcionario():
    numero_departamento = request.form['departamento']

    departamentos = listar_departamento()

    departamento_selecionado = None

    for departamento in departamentos:
        if str(departamento.numero) == numero_departamento:
            departamento_selecionado = departamento
            break

    funcionarios = consultar_por_departamento(
        departamento_selecionado
    )

    return render_template(
        'funcionarios/consulta.html',
        departamentos=departamentos,
        funcionarios=funcionarios,
        departamento_selecionado=departamento_selecionado
    )