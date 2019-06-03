import hashlib

from rest.controller.base import Controller
from rest.dao.user import UserDAO
from rest.models.user import User


class UserController(Controller):

    _dao = UserDAO()

    def update_user_data(self, user: User, body: dict):
        keys = body.keys()

        if 'email' in keys:
            user.email = body['email']

        if 'senha' in keys:
            user.password = body['senha']

        self._dao.update(user)

    @classmethod
    def hash_password(cls, password):
        encoded_password = str(password).encode("utf-8")

        m = hashlib.sha512()
        m.update(encoded_password)
        return str(m.hexdigest())

    def find_by_email_password(self, email, password):
        return self._dao.find_by_email_password(email, password)
