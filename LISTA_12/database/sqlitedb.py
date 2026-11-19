import sqlite3

class SQLiteDB:
    DB = 'academico.db'
    
    def __init__(self):
        self.db_name = self.DB
        self.conn = None
        self.cursor = None
    
    def conectar(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.conn.execute('PRAGMA foreign_keys = ON')
            self.conn.row_factory =  sqlite3.Row
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
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return self.cursor.rowcount  # Retorna o número de linhas afetadas 
        except sqlite3.Error as e:
            self.conn.rollback()  # Desfaz as alterações em caso de erro
            print(f"Erro ao executar: {e}")
            return 0
        
    def consultar(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()

        except sqlite3.Error as e:
            print(f"Erro ao consultar: {e}")
            return None
    
    def executar_script_sql(self, sql_file):
        try:
            with open(sql_file, 'r', encoding='utf-8') as f:
                script_sql = f.read()

            self.cursor.executescript(script_sql)
            self.conn.commit()

            print("Script executado com sucesso!")

        except (sqlite3.Error, OSError) as e:
            if self.conn:
                self.conn.rollback()

        print(f"Erro ao executar o script: {e}")