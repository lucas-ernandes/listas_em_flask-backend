from models.departamento import Departamento

departamentos = []

def cadastrar_departamento(numero, nome):
    departamento = Departamento(numero, nome)
    departamentos.append(departamento)
    
    
def listar_departamento():
    return departamentos