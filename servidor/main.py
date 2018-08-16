from flask import Flask


app = Flask(__name__)


@app.route("/")
def holaServer():
    return "Hola desde Server"


if __name__ == '__main__':
    app.run()
