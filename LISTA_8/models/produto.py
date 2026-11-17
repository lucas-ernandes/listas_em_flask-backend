class Produto:
    produtos = []

    def __init__(self, codigo, descricao, valor):
        self.codigo = codigo
        self.descricao = descricao
        self.valor = valor

    #Metodos
    def armazenar(self):
        Produto.produtos.append(self)
        
    @classmethod
    def buscar_todos(cls):
        return cls.produtos