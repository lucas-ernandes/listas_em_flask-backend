from database.sqlitedb import SQLiteDB

db = SQLiteDB()
db.conectar()
db.executar_script_sql("database/tabela_produto.sql")

db.desconectar()