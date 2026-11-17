from flask import Flask
from routers.produto_rota import produto_rota

app = Flask(__name__)
app.secret_key =  "chave-temporaria-produtos"

app.register_blueprint(produto_rota)

if __name__ == "__main__":
    app.run(debug=True)
    