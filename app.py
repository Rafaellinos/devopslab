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


@app.route('/bug')
def bad():
    try:
        raise TypeError()
    except TypeError as e:
        print(e)
    except TypeError as e:
        print("Duplicado, ou seja, nunca vai entrar aqui.")


if __name__ == '__main__':
    app.run()
