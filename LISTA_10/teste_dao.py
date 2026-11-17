from daos.produto_dao import ProdutoDAO

dao = ProdutoDAO()

produto = {
    "codigo": "P001",
    "descricao": "Teclado",
    "preco_unitario": 85.00
}

resultado = dao.create(produto)

if resultado == 1:
    print("Produto cadastrado com sucesso!")
else:
    print("Não foi possivel cadastrar o produto.")