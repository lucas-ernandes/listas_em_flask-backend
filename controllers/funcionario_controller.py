from models.funcionario import Funcionario, render_template, request
from controllers.departamento_controller import departamentos

funcionarios = []

def cadastrar_funcionario():
    codigo = request.form.get('codigo')
    nome = request.form.get('nome')
    numero_departamento = request.form.get('numero_departamento')


    departamento = None

    for dep in departamentos:
        if dep.numero == numero_departamento:
            departamento = dep
            break

    if departamento is None:
        return False

    funcionario = Funcionario(codigo=codigo, nome=nome, departamento=departamento)
    funcionarios.append(funcionario)
    return True


def listar_funcionario():
    return funcionarios