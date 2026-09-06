from flask import Flask, render_template, request

app = Flask(__name__)

def boas_vindas():
    return render_template("bem_vindos.html")

#/saudacao/<usuario>
def saudacoes(user):
    return render_template("saudacao.html", nome=user)

#/cadastro
def formulario():
    return render_template("cadastro.html")

#/resultado
def exibir_resultado():
    nome = request.form.get("user_name")
    idade = request.form.get("user_idade")
    curso = request.form.get("user_curso")

    return render_template("resultado.html", name=nome, age=idade, course=curso)

#OS CAMINHOS
app.add_url_rule(rule="/", view_func=boas_vindas, methods=["GET"])

app.add_url_rule(rule="/saudacao/<usuario>", view_func=saudacoes, methods=["GET"])

app.add_url_rule(rule="/cadastro", view_func=formulario, methods=["GET"])

app.add_url_rule(rule="/resultado", view_func=exibir_resultado, methods=["POST"])

if __name__ == "__main__":
    app.run(debug=True)