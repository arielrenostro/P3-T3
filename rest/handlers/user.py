from flask import request
from flask_restful import Resource

from rest.controller.user import UserController
from rest.exceptions.request import RequestException
from rest.models.user import User
from rest.utils.wrappers import authenticated, exception_handler


class UserApi(Resource):

    _controller: UserController = UserController()

    @exception_handler
    @authenticated
    def get(self):
        users = self._controller.find_all()
        return list(
            map(lambda e: user_to_dict(e), users)
        )

    @exception_handler
    @authenticated
    def post(self):
        if not request.is_json:
            raise RequestException(400, 'Must be JSON request')

        body = request.json

        user = User(
            email=body['email'],
            password=body['senha']
        )

        self._controller.update(entity=user)

        return user_to_dict(user), 201


class UserParamApi(Resource):

    _controller: UserController = UserController()

    @exception_handler
    @authenticated
    def put(self, id_):
        if not id_:
            raise RequestException(400, 'ID path param is required')

        if not request.is_json:
            raise RequestException(400, 'Must be JSON request')

        id_ = int(id_)
        user = self._controller.find(id_)
        if not user:
            raise RequestException(404, 'User not founded')

        body = request.json
        self._controller.update_user_data(user, body)

        return user_to_dict(user)

    @exception_handler
    @authenticated
    def delete(self, id_):
        if not id_:
            raise RequestException(400, 'ID path param is required')

        id_ = int(id_)
        user = self._controller.find(id_)
        if not user:
            raise RequestException(404, 'User not founded')

        self._controller.delete(user)

        return {
            'success': {
                'text': 'Usuário removido'
            }
        }


def user_to_dict(entity):
    return {
        'id': str(entity.id),
        'email': entity.email,
        'senha': entity.password
    }
