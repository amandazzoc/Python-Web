from flask import Flask, render_template

# nome da aplicação
app = Flask(__name__, template_folder="views")

@app.route("/")
def index(): # começa com def = função
    return render_template("index.html")

@app.route("/crud")
def crud():
    return render_template("crud.html")

@app.route("/amanda")
def amanda():
    return render_template("teste.html")

if __name__ == "__main__":
    app.run(debug=True) #mostra os erros quando executado
