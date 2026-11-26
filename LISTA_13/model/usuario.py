from werkzeug.security import generate_password_hash, check_password_hash
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
        
        if password is None or not isinstance(password, str):
            self.errors.append("A senha deve ser uma string.")
        else:
            if not password.strip():
                self.errors.append('A senha não pode ser vazia.')
            elif len(password) <8:
                self.errors.append('A senha deve ter 8 digitos.') 
        
        if len(self.errors) == 0:
            self.data = {"username": username.strip(), "password": password}
            return True
        
        return False
    
    
    def save(self):
        dao = UsuarioDAO()
        
        dados = dict(self.data)

        dados['password'] = generate_password_hash(dados['password'])
        resultado = dao.create(dados)

        return resultado == 1

        
    @staticmethod
    def get_by_username(username):
        dao = UsuarioDAO()
        resultado = dao.read_one_by_username(username)

        return resultado
    
    @staticmethod
    def autenticar(username, password):
        dao = UsuarioDAO()

        usuario = dao.read_one_by_username(username)

        if usuario is None:
            return None
        if check_password_hash(usuario['password'], password):
            usuario.pop('password')
            return usuario
        return None