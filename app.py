from flask import Flask
from controllers import routes

# nome da aplicação, definição do template onde dica o diretório web
app = Flask(__name__, template_folder="views")
routes.init_app(app)

if __name__ == "__main__":
    app.run(debug=True) #mostra os erros quando executado
