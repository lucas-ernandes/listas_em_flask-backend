from flask import Blueprint
from controllers.produto_controller import(
    exibir_form, processar_cadastro, listar_produtos
)

produto_router = Blueprint('produto', __name__)

@produto_router.route('/novo', methods=['GET'])
def novo():
    return exibir_form()

@produto_router.route('/salvar', methods=['POST'])
def salvar():
    return processar_cadastro()

@produto_router.route('/produtos', methods=['GET'])
def produtos():
    return listar_produtos()
    