from models.funcionario import Funcionario

funcionarios = []

def cadastrar_funcio(codigo, nome, departamneto):
    funcionario = Funcionario(codigo, nome, departamneto)
    funcionarios.append(funcionario)

def listar_funcionario():
    return funcionarios

def consultar_por_departamento(departamento):
    resultado = []

    for funcionario in funcionarios:
        if funcionario.departamento == departamento:
            resultado.append(funcionario)

    return resultado