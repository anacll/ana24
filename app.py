from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá Mundo!!!!'

@app.route("/compras")
def compras():
    return render_template ("compras.html")

@app.route("/mercados")
def mercados():
    return render_template("mercados.html")

if __name__ == '__main__':
    app.run()