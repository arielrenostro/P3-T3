import logging

from flask import Flask

from rest.models.user import User
from rest.dao.database import db
from rest.routes import api


def populate_db():
    user = User.query.filter_by(email="furb@furb.com").first()
    if not user:
        user = User(email="furb@furb.com", password="123456")
        db.session.add(user)

    db.session.commit()


def create_app():
    _app = Flask(__name__)
    _app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    _app.config['OAUTH1_PROVIDER_ENFORCE_SSL'] = False
    _app.config['OAUTH1_PROVIDER_KEY_LENGTH'] = (10, 100)

    db.app = _app
    db.init_app(_app)
    api.init_app(_app)

    db.create_all()

    populate_db()

    return _app


app = create_app()

logger = logging.getLogger('P3-T3')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)
