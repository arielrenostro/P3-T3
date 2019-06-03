import logging

from flask import Flask
from werkzeug.security import gen_salt

from rest.models.oauth.client import Client
from rest.models.user import User
from rest.oauth import oauth
from rest.dao.database import db
from rest.routes import api


def populate_db():
    user = User.query.filter_by(email="furb@furb.com").first()
    if not user:
        user = User(email="furb@furb.com", password="123456")
        db.session.add(user)

    client = Client.query.filter_by(user_id=user.id).first()
    if not client:
        client = Client(
            client_key=gen_salt(40),
            client_secret=gen_salt(50),
            _redirect_uris='http://127.0.0.1:8080/authorized'
        )
    client.user_id = user.id

    client_key = client.client_key
    client_secret = client.client_secret

    db.session.add(client)
    db.session.commit()

    print(f"Furb credentials: client_key: {client_key}, client_secret: {client_secret}")


def create_app():
    _app = Flask(__name__)
    _app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    _app.config['OAUTH1_PROVIDER_ENFORCE_SSL'] = False
    _app.config['OAUTH1_PROVIDER_KEY_LENGTH'] = (10, 100)

    db.app = _app
    db.init_app(_app)
    api.init_app(_app)
    oauth.init_app(_app)

    db.create_all()

    populate_db()

    return _app


app = create_app()

logger = logging.getLogger('P3-T3')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)
