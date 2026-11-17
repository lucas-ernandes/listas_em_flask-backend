from flask import Blueprint, render_template, request, redirect, url_for, flash

from controllers.produto_controller import(
    cadastrar_produto,
    listar_produtos,
    detalhar_produto,
    editar_produto,
    excluir_produto,
    pesquisar_produtos
)

produto_rota = Blueprint("produto_rota", __name__)


@produto_rota.route("/")
def inicio():
    return render_template("index.html")


@produto_rota.route("/produtos")
def listar():
    produtos = listar_produtos()

    if produtos is None:
        flash("Erro ao consultar os produtos.", "danger")
        produtos = []

    return render_template("produto_lista.html", produtos=produtos)


@produto_rota.route("/produtos/novo")
def novo():
    return render_template("produto_form.html", produto=None)


@produto_rota.route("/produtos/salvar", methods=["POST"])
def salvar():
    data = request.form.to_dict()
    sucesso, mensagens = cadastrar_produto(data)

    for mensagem in mensagens:
        flash(mensagem, "success" if sucesso else "danger")

    if sucesso:
        return redirect(url_for("produto_rota.listar"))

    return render_template(
        "produto_form.html",
        produto=data,
        editando=False)


@produto_rota.route("/produtos/<codigo>")
def detalhe(codigo):
    produto = detalhar_produto(codigo)

    if produto is None:
        flash("Produto não encontrado.", "danger")
        return redirect(url_for("produto_rota.listar"))

    return render_template("produto_detalhe.html", produto=produto)


@produto_rota.route("/produtos/<codigo>/editar")
def formulario_edicao(codigo):
    produto = detalhar_produto(codigo)

    if produto is None:
        flash("Produto não encontrado.", "danger")
        return redirect(url_for("produto_rota.listar"))

    return render_template(
        "produto_form.html",
         produto=produto,
         editando = True,
         codigo_original=codigo)


@produto_rota.route("/produtos/<codigo>/atualizar", methods=["POST"])
def atualizar(codigo):
    data = request.form.to_dict()
    sucesso, mensagens = editar_produto(codigo, data)

    for mensagem in mensagens:
        flash(mensagem, "success" if sucesso else "danger")

    if sucesso:
        return redirect(url_for("produto_rota.listar"))

    produto = detalhar_produto(codigo)
    return render_template(
        "produto_form.html",
        produto=data,
        editando=True,
        codigo_original=codigo
    )


@produto_rota.route("/produtos/<codigo>/excluir", methods=["POST"])
def excluir(codigo):
    sucesso, mensagens = excluir_produto(codigo)

    for mensagem in mensagens:
        flash(mensagem, "success" if sucesso else "danger")

    return redirect(url_for("produto_rota.listar"))


@produto_rota.route("/produtos/buscar")
def buscar():
    termo = request.args.get("termo", "").strip()
    produtos = pesquisar_produtos(termo)

    if produtos is None:
        flash("Erro ao pesquisar produtos.", "danger")
        produtos = []

    return render_template(
        "produto_lista.html",
        produtos=produtos,
        termo=termo
    )