from flask import render_template

def init_app(app):
    @app.route("/")
    def index(): # começa com def = função
        escola = "ruy prado"
        unidade = "Registro"
        return render_template(
            "index.html",
            pEscola = escola,
            pUnidade = unidade
            )
    

    @app.route("/herois")
    def herois():
        universo = "marvel"
        heroi = "miranha"
        return render_template(
            "herois.html",
            pUniverso = universo,
            pHeroi = heroi
            )
    

    @app.route("/crud")
    def crud():
        return render_template("crud.html")

    @app.route("/amanda")
    def amanda():
        return render_template("teste.html")