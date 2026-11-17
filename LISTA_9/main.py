from flask import Flask
from routes.departamento_routes import departamento_rota
from routes.funcionario_routes import funcionario_rota

app = Flask(__name__, template_folder='views')

app.register_blueprint(departamento_rota)
app.register_blueprint(funcionario_rota)


if __name__ == '__main__':
    app.run(debug=True)