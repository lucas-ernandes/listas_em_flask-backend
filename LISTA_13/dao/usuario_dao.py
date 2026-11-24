from database.sqlitedb import SQLiteDB

class UsuarioDAO:
    def __init__(self):
        self.db = SQLiteDB()
    
    def create(self, data: dict):
        self.db.conectar()
        try:
            sql = "INSERT INTO usuarios (username, password) VALUES (?, ?);"
            username = data.get('username')
            password = data.get('password')
        
            resultado = self.db.executar(query=sql, params=(username, password))
        
            return resultado
        finally:
            self.db.desconectar()
    
            
    def read_one_by_username(self, username: str):
        self.db.conectar()
        try:
            sql = "SELECT id_usuario, username, password FROM usuarios WHERE username = ?;"

            resultado = self.db.consultar(query=sql, params=(username,))

            if resultado is None or len(resultado) == 0:
                return None
            
            row = resultado[0]
            data = {
                'id_usuario': row['id_usuario'],
                'username': row['username'],
                'password': row['password']
                }
                
            return data
        
        finally:
            self.db.desconectar()