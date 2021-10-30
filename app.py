from flask import Flask

app = Flask(__name__)


@app.route("/")
def pagina_inicial():
    return "Hello World"


@app.route("/soma")
def soma_valores():
    return f"Sua soma de 10+10={10 + 10}"


if __name__ == '__main__':
    app.run()
