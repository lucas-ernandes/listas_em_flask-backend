import sqlite3

class SQLiteDB:
    DB_FILE = "produtos.db"

    def __init__(self):
        self.db_name = self.DB_FILE
        self.conn = None
        self.cursor = None
    
    def conectar(self):
        """ Abre a conexão com o banco de dados """
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.conn.row_factory = sqlite3.Row
            self.cursor = self.conn.cursor()
            
        except sqlite3.Error as e:
            print(f'Erro ao conectar: {e}')
            self.conn = None
            self.cursor = None

    def desconectar(self):
        """Fecha a conexão com o banco de dados."""
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None

    def executar(self, query, params=()):
        """Executa INSERT, UPDATE e DELETE."""
        try:
            self.cursor.execute(query, params)
            self.conn.commit() #confirma as altrações no banco
            return self.cursor.rowcount

        except sqlite3.Error as e:
            self.conn.rollback() #tenta desfazer as alterações da transação quando ocorre um erro
            print(f"Erro ao executar: {e}")
            return 0

    def consultar(self, query, params=()):
        """Executa SELECT e retorna os resultados."""
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()

        except sqlite3.Error as e:
            print(f"Erro ao consultar: {e}")
            return None

    def executar_script_sql(self, sql_file):
        """Executa um arquivo que contém comandos SQL."""
        try:
            with open(sql_file, "r", encoding="utf-8") as arquivo:
                script_sql = arquivo.read()

            self.cursor.executescript(script_sql)
            self.conn.commit()
            print("Script executado com sucesso!")

        except (sqlite3.Error, OSError) as e:
            if self.conn:
                self.conn.rollback()
            print(f"Erro ao executar o script: {e}")
