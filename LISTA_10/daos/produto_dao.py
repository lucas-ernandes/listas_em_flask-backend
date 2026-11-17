from database.sqlitedb import SQLiteDB

class ProdutoDAO:
    def __init__(self):
        self.db = SQLiteDB()

    def create(self, data):
        """Cadastra um produto."""
        self.db.conectar()

        sql = """
            INSERT INTO produtos (codigo, descricao, preco_unitario)
            VALUES (?, ?, ?);
        """

        resultado = self.db.executar(
            sql,
            (
                data.get("codigo"),
                data.get("descricao"),
                data.get("preco_unitario")
            )
        )

        self.db.desconectar()
        return resultado

    def read_all(self):
        """Consulta todos os produtos."""
        self.db.conectar()

        sql = """
            SELECT codigo, descricao, preco_unitario
            FROM produtos
            ORDER BY codigo;
        """

        resultado = self.db.consultar(sql)
        self.db.desconectar()

        if resultado is None:
            return None

        return [dict(row) for row in resultado]

    def read_one_by_codigo(self, codigo):
        """Consulta um produto pelo código."""
        self.db.conectar()

        sql = """
            SELECT codigo, descricao, preco_unitario
            FROM produtos
            WHERE codigo = ?;
        """

        resultado = self.db.consultar(sql, (codigo,))
        self.db.desconectar()

        if resultado is None:
            return None

        if len(resultado) > 0:
            return dict(resultado[0])

        return None

    def update(self, data):
        """Atualiza os dados de um produto."""
        self.db.conectar()

        sql = """
            UPDATE produtos
            SET codigo = ?, descricao = ?, preco_unitario = ?
            WHERE codigo = ?;
        """

        resultado = self.db.executar(
            sql,
            (
                data.get("codigo"),
                data.get("descricao"),
                data.get("preco_unitario"),
                data.get("codigo_original")
            )
        )

        self.db.desconectar()
        return resultado

    def delete(self, codigo):
        """Exclui um produto pelo código."""
        self.db.conectar()

        sql = "DELETE FROM produtos WHERE codigo = ?;"

        resultado = self.db.executar(sql, (codigo,))
        self.db.desconectar()

        return resultado

    def search(self, termo):
        """Pesquisa produtos pelo código ou descrição."""
        self.db.conectar()

        sql = """
            SELECT codigo, descricao, preco_unitario
            FROM produtos
            WHERE codigo LIKE ? OR descricao LIKE ?
            ORDER BY codigo;
        """

        pesquisa = f"%{termo}%"

        resultado = self.db.consultar(
            sql,
            (pesquisa, pesquisa)
        )

        self.db.desconectar()

        if resultado is None:
            return None

        return [dict(row) for row in resultado]
