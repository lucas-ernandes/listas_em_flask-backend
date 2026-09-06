from flask import Flask, render_template, request

app = Flask(__name__)

def homepage():
    return render_template("index.html")

def formulario():
    return render_template("form_precomedio.html")

def form_resultado():
    quantidade = request.form.get("qtd")
    preco_unitario = request.form.get("prc")
    operacao = request.form.get("opc")

    try:
        qtd = int(quantidade)
        prc = float(preco_unitario)
        bruto = round(qtd * prc, 2)
        taxa = round(bruto * 0.01, 2)
        
        if operacao == "compra":
            liquido = round(bruto + taxa, 2)
        elif operacao == "venda":
            liquido = round(bruto - taxa, 2)

        return render_template(
            "precomedio.html",
            operacao=operacao,
            quantidade=qtd,
            preco_unitario=prc,
            valor_bruto=bruto,
            valor_liquido=liquido,
            taxa=taxa
        )
    except ValueError:
        return "<p><strong>ERRO:</strong> Dados preenchidos com valores inválidos, tente novamente.</p>"
#-----------------------------------------------------------------------

#Principal
app.add_url_rule(rule="/", view_func=homepage, methods=["GET"])

#Preco medio formulario
app.add_url_rule(rule="/precomedio", view_func=formulario, methods=["GET"])

#Calculo e resultado dp preco medio
app.add_url_rule(rule="/resultado", view_func=form_resultado, methods=["POST"])


if __name__ == "__main__":
    app.run(debug=True)