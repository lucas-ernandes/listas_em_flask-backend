from flask import Flask

def adicionar_rotas(app: Flask):
    app.add_url_rule(
        '/login',
        endpoint='login',
        view_func=login_controller.login,
        methods=['GET']
    )

    app.add_url_rule(
        '/login',
        endpoint='login_validar',
        view_func=login_controller.validar,
        methods=['POST']
    )
    