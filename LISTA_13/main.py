from flask import Flask
from routers import usuario_router
from database.sqlitedb import SQLiteDB

app = Flask(__name__)
app.secret_key = 'chave_123_sla'

db = SQLiteDB()
db.conectar()
db.executar_script_sql('database/scripts/dados.sql')
db.desconectar()

usuario_router.adicionar_rotas(app)

if __name__ == "__main__":
    app.run(debug=True)
