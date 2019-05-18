from flask import Flask

from rest.oauth import oauth
from rest.dao.database import init_db
from rest.routes import api


def create_app():
    app = Flask(__name__)

    init_db()
    api.init_app(app)
    oauth.init_app(app)

    return app


app = create_app()
