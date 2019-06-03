from flask_restful import Resource

from rest.oauth import oauth


class RequestTokenApi(Resource):

    @oauth.request_token_handler
    def get(self):
        return {}


class AccessTokenApi(Resource):

    @oauth.access_token_handler
    def get(self):
        return {}


class AuthorizeApi(Resource):

    @oauth.authorize_handler
    def post(self):
        return True


def register():
    pass
