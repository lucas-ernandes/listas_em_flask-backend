from daos.produto_dao import ProdutoDAO

class Produto:
    def __init__(self, data):
        self.data = data
        self.errors = []

    def validate(self):
        '''Valida os dados do produto'''
        self.errors = []

        codigo = self.data.get("codigo")
        descricao = self.data.get("descricao")
        preco = self.data.get("preco_unitario")

        if not isinstance(codigo, str) or not codigo.strip():
            self.errors.append("O código é obrigatório.")
        else:
            codigo = codigo.strip()

        if not isinstance(descricao, str) or not descricao.strip():
            self.errors.append("A descrição é obrigatória.")
        else:
            descricao = descricao.strip()

            if len(descricao) > 40:
                self.errors.append(
                    "A descrição deve ter no máximo 40 caracteres."
                )

        try:
            preco = float(preco)

            if preco < 0:
                self.errors.append("O preço não pode ser negativo.")

        except (TypeError, ValueError):
            self.errors.append("Informe um preço válido.")

        if not self.errors:
            self.data["codigo"] = codigo
            self.data["descricao"] = descricao
            self.data["preco_unitario"] = preco

    def save(self):
        """Salva um produto novo."""
        dao = ProdutoDAO()
        return dao.create(self.data) == 1

    @staticmethod
    def get_all():
        """Retorna todos os produtos."""
        dao = ProdutoDAO()
        return dao.read_all()

    @staticmethod
    def get_one_by_codigo(codigo):
        """Busca um produto pelo código."""
        dao = ProdutoDAO()
        return dao.read_one_by_codigo(codigo)

    def atualizar(self):
        """Atualiza um produto existente."""
        dao = ProdutoDAO()
        return dao.update(self.data) == 1

    @staticmethod
    def remover(codigo):
        """Remove um produto pelo código."""
        dao = ProdutoDAO()
        return dao.delete(codigo) == 1

    @staticmethod
    def pesquisar(termo):
        """Pesquisa produtos por código ou descrição."""
        dao = ProdutoDAO()
        return dao.search(termo)