import sqlite3

class SQLiteDB:
    DB_FILE = 'instagram_falso.db'
    
    def __init__(self):
        self.db = self.DB_FILE
        self.conn = None # guarda a conexao
        self.cursor = None # guarda o cursor
        
    def conectar(self):
        # Abre conexao comn bando de dados
        try:
            self.conn = sqlite3.connect(self.db)
            self.conn.execute("PRAGMA foreign_keys = ON")
            self.conn.row_factory = sqlite3.Row
            self.cursor = self.conn.cursor()
            
        except sqlite3.Error as e:
            print(f'Erro ao conectar: {e}')
            self.conn = None
            self.cursor = None
    
    
    def desconectar(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None
            
    def executar(self, query, params=()):
        # Executa comandos INSERT, UPDATE, DELETE com commit
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return self.cursor.rowcount
        
        except sqlite3.Error as e:
            self.conn.rollback()  # Desfaz as alterações em caso de erro
            print(f"Erro ao executar: {e}")
            
            return 0
    
    def consultar(self, query, params=()):
        # Executa consultas SELECT e retorna os resultados
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        
        except sqlite3.Error as e:
            print(f"Erro ao consultar: {e}")
            return None
        
    def executar_script_sql(self, sql_file):
        # Executa um arquivo SQL em um banco de dados SQLite.
        try:
            with open(sql_file, 'r', encoding='utf-8') as f:
                script_sql = f.read()
            
            self.cursor.executescript(script_sql)
            self.conn.commit() #salva as alteraçoes

            print('Script executado com sucesso!')
        
        except (sqlite3.Error, OSError) as e:
            if self.conn:
                self.conn.rollback()

            print(f'Erro ao Executar o script: {e}')