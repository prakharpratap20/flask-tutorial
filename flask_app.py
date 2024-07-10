from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config[
    "SQLALCHEMY_DATABASE_URL"
] = "postgresql://username.password@localhost:5432/flaskapp"

db = SQLAlchemy(app)


@app.route("/")
def index():
    return "<h1>Hello World</h1>"


@app.route("/users/<name>")
def user(name):
    return f"<h1>Hello, {name}</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
