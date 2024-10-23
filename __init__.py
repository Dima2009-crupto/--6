from flask import Flask

from app.db import create_db


app = Flask(__name__)


def main():
    create_db()
    app.run(debug=True)