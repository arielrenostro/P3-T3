from flask import Flask

from rest.database import init_db
from rest.routes import api


def create_app():
    app = Flask(__name__)

    api.init_app(app)
    init_db()

    return app


app = create_app()
