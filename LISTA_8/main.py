from flask import Flask
from routers.produto_router import produto_router
app = Flask(__name__)

app.register_blueprint(produto_router)

if __name__ == '__main__':
    app.run(debug=True)
