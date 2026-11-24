from dao.usuario_dao import UsuarioDAO

class Usuario:
    def __init__(self, data: dict):
    # inicializa um objeto
    # data: - dicionario contem os dados do usuario e chaves
        self.data = data
        self.errors = []
        
    def validate(self):
        self.errors = []

        username = self.data.get('username', '')
        password = self.data.get('password', '')

        if username is None or not isinstance(username, str):
            self.errors.append("O nome deve ser uma string.")
        else:
            if not username.strip():
                self.errors.append("O nome não pode conter apenas espaços.")
        
        if not password:
            self.errors.append("A senha não pode ficar vazia.")
            
        
        if len(self.errors) == 0:
            self.data = {"username": username.strip(), "password": password}
            return True
        
        return False
    
    
    def save(self):
        dao = UsuarioDAO()
        resultado = dao.create(self.data)

        if resultado == 1:
            return True
        else:
            return False
        
    
    @staticmethod
    def get_by_username(username):
        dao = UsuarioDAO()
        resultado = dao.read_one_by_username(username)

        return resultado
    
    @staticmethod
    def autenticar(username, password):
        dao = UsuarioDAO()

        usuaario = dao
        pass