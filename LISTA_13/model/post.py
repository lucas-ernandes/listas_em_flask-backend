from dao.usuario_dao import UsuarioDAO

class Post:
    def __init__(self, data: dict):
    # inicializa um objeto
    # data: - dicionario contem os dados do usuario e chaves
        self.data = data
        self.errors = []
    
    def validate(self):
        
        titulo = self.data.get('titulo', '')
        conteudo = self.data.get('conteudo', '')
        id_usuario = self.data.get('id_usuario')
        
        # titulo
        if not isinstance(titulo, str):
            self.errors.append("O titulo deve ser uma string.")
        elif not titulo.strip():
            self.errors.append('O titulo não pode ficar vazio.')
        # conteudo
        if not isinstance(conteudo, str):
            self.errors.append("O conteudo deve ser uma string.")
        elif not conteudo.strip():
            self.errors.append("O conteudo não pode ficar vazio.")
        # id
        if not isinstance(id_usuario, int) or id_usuario <=0:
            self.errors.append('O ID do usuario é invalido.')
        
        if len(self.errors) == 0:
            self.data = {
                "titulo": titulo.strip(),
                "conteudo": conteudo.strip(),
                "id_usuario": id_usuario
            }
            return True
        
        return False