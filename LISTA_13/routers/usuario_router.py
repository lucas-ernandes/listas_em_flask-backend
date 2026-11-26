from flask import Flask
from controllers import usuario_controller

# CADASTRO
def adicionar_rotas(app: Flask):
    app.add_url_rule(
        '/',
        view_func=usuario_controller.cadastro,
        methods=['GET', 'POST']
    )
    
    app.add_url_rule(
        '/cadastro',
        view_func=usuario_controller.cadastro,
        methods=['GET', 'POST']
    )
# LOGIUN
    app.add_url_rule(
        '/login',
        view_func=usuario_controller.login,
        methods=['GET', 'POST'],
    )

    app.add_url_rule(
        '/logout',
        endpoint='logout',
        view_func=usuario_controller.logout,
        methods=['GET']
    )
# TELA INICIO
    app.add_url_rule(
        '/inicio',
        endpoint='inicio',
        view_func=usuario_controller.inicio,
        methods=['GET']
    )