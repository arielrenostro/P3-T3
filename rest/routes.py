from flask_restful import Api

from rest.handlers.oauth import RequestTokenApi, AccessTokenApi, AuthorizeApi
from rest.handlers.order import OrderApi, OrderParamApi
from rest.handlers.user import UserApi, UserParamApi

api = Api()
api.add_resource(UserApi, '/RestAPIFurb/usuarios')
api.add_resource(UserParamApi, '/RestAPIFurb/usuarios/<int:id_>')
api.add_resource(OrderApi, '/RestAPIFurb/comandas')
api.add_resource(OrderParamApi, '/RestAPIFurb/comandas/<int:id_>')

api.add_resource(RequestTokenApi, '/RestAPIFurb/oauth/request_token')
api.add_resource(AccessTokenApi, '/RestAPIFurb/oauth/access_token')
api.add_resource(AuthorizeApi, '/RestAPIFurb/oauth/authorize')