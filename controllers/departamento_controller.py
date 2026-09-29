from models.departamento import Departamento, render_template, request

departamentos = []

def exibir_form_novo():
    return render_template('/departamento/novo.html')

def cadastrar():
    #tratar os dados da requisição e montar um objeto da classe  Departamento
    numero = request.form.get('numero')
    nome  =  request.form.get('nome')
    departamento = Departamento(numero=numero, nome=nome)

    #salvar o objeto na lista de departamento
    departamentos.append(departamento)

def listar_depart():
    return departamentos