from rest.dao.database import db


class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True)
    password = db.Column(db.String(250))

    def __init__(self, email=None, password=None):
        self.password = password
        self.email = email

    def __repr__(self):
        return f'{self.__class__.__name__} id [{self.id}] email [{self.email}]'

    def __setattr__(self, key, value):
        if key == 'password':
            from rest.controller.user import UserController
            value = UserController.hash_password(value)
        super().__setattr__(key, value)
