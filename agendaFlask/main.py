from flask import Flask
app = Flask(__name__)


@app.route('/')
def hola():
    return '¡Hola, mundo con flask!'


if __name__ == '__main__':
    app.run()