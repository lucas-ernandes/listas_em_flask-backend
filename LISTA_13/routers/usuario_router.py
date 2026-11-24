from flask import Flask
from controllers import usuario_controller

def adicionar_rotas(app: Flask):
    app.add_url_rule(
        '/cadastro',
        endpoint='usuario_novo',
        view_func=usuario_controller.novo,
        methods=['GET']
    )
    
    app.add_url_rule(
        '/cadastro/salvar',
        endpoint='usuario_salvar',
        view_func=usuario_controller.salvar,
        methods=['POST']
    )