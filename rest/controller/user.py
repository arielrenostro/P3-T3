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
