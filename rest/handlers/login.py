from http import HTTPStatus
from http.cookies import SimpleCookie

from flask import request
from flask_restful import Resource

from rest.controller.token import TokenController


class LoginApi(Resource):

    def post(self):
        email, password = self._validate_request()

        from rest.controller.user import UserController
        user_controller = UserController()

        user = user_controller.find_hashing_password(email, password)
        if not user:
            return '', HTTPStatus.FORBIDDEN

        token = TokenController().find_or_generate_token(user)

        cookie = SimpleCookie()
        cookie['X-Furb-Authorization'] = token
        cookie['X-Furb-Authorization']['HttpOnly'] = True
        cookie['X-Furb-Authorization']['Path'] = '/'

        headers = {
            'Set-Cookie': cookie.output(header='')
        }

        body = {
            'token': token
        }
        return body, HTTPStatus.OK, headers

    def _validate_request(self):
        if not request.json:
            return '', HTTPStatus.BAD_REQUEST

        email = request.json.get('email')
        password = request.json.get('senha')

        if not email or not password:
            return '', HTTPStatus.BAD_REQUEST

        return email, password
