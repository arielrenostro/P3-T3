from flask import request
from flask_restful import Resource

from rest.exceptions.request import RequestException
from rest.models.usuario import Usuario
from rest.utils.wrappers import authenticated, exception_handler


class UsuarioApi(Resource):

    @exception_handler
    @authenticated
    def get(self):
        return {
            'text': 'TOP!'
        }

    @exception_handler
    @authenticated
    def post(self):
        if not request.is_json:
            raise RequestException(400, 'Must be JSON request')

        body = request.json()

        user = Usuario(body['email'], body['senha'])



class UsuarioParamApi(Resource):

    @exception_handler
    @authenticated
    def put(self, id):
        if not id:
            raise RequestException(400, 'ID path param is required')

        id = int(id)
        user = Usuario.query.get(id)
        if not user:
            raise RequestException(404, 'User not founded')

    @exception_handler
    @authenticated
    def get(self, id):
            return {
                'id': id
            }
