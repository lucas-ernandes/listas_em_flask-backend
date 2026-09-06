from flask import Flask, render_template

app = Flask(__name__)

def home():
    return render_template("index.html")

#def add_routes(app: Flask):
app.add_url_rule(rule="/", view_func=home, methods=["GET"])

if __name__ == "__main__":
    app.run(debug=True)