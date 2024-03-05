from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ("index.html")

@app.route("/compras")
def compras():
    return render_template ("compras.html" ,item1="farinha", item2="cuscuz")

@app.route("/mercados")
def mercados():
    return render_template("mercados.html")


@app.route("/gastos", defaults={'mes':"janeiro", "valor":"0"})
@app.route("/gastos/<mes>/<valor>")
def gastos(mes, valor):
    return render_template("gastos.html", a=mes, b=valor)

@app.route("/dobro/", defaults={"n":0})
@app.route("/dobro/<int:n>")
@app.route("/dobro/<float:n>")
def dobro(n):
    resultado=2*n
    return render_template("dobro.html", n=n, resultado=resultado)

if __name__ == '__main__':
    app.run()