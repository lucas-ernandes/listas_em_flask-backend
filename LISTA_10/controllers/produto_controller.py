from models.produto import Produto

def cadastrar_produto(data):
    produto = Produto(data)
    produto.validate()

    if produto.errors:
        return False, produto.errors

    if Produto.get_one_by_codigo(produto.data["codigo"]):
        return False, ["Já existe um produto com esse código."]

    if produto.save():
        return True, ["Produto cadastrado com sucesso!"]

    return False, ["Não foi possível cadastrar o produto."]


def listar_produtos():
    return Produto.get_all()


def detalhar_produto(codigo):
    return Produto.get_one_by_codigo(codigo)


def editar_produto(codigo_original, data):
    produto = Produto(data)
    produto.validate()

    if produto.errors:
        return False, produto.errors

    produto.data["codigo_original"] = codigo_original

    existente = Produto.get_one_by_codigo(produto.data["codigo"])

    if existente and produto.data["codigo"] != codigo_original:
        return False, ["Esse código já pertence a outro produto."]

    if produto.atualizar():
        return True, ["Produto atualizado com sucesso!"]

    return False, ["Não foi possível atualizar o produto."]


def excluir_produto(codigo):
    if Produto.remover(codigo):
        return True, ["Produto excluído com sucesso!"]

    return False, ["Não foi possível excluir o produto."]


def pesquisar_produtos(termo):
    return Produto.pesquisar(termo)