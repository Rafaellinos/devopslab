from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)


@app.route("/")
def pagina_inicial():
    return "Laboratório Pipeline DevOps"


@app.route("/soma")
def soma_valores():
    return f"Sua soma de 10+10={10 + 10}"


if __name__ == '__main__':
    app.run()
