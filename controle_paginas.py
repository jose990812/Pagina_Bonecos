
from flask import Flask, render_template

app = Flask (__name__)

@app.route("/")

def pagina_inicial():
    return render_template("tela.html")

@app.route("/add")

def pagina_secundaria():
    return render_template("tela2.html")


if __name__ == '__main__':
    app.run(debug=True)
    
