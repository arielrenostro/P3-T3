from flask_restful import Api

from rest.handlers.comanda import ComandaApi
from rest.handlers.usuario import UsuarioApi, UsuarioParamApi

api = Api()
api.add_resource(UsuarioApi, '/RestAPIFurb/usuarios')
api.add_resource(UsuarioParamApi, '/RestAPIFurb/usuarios/<int:id>')
api.add_resource(ComandaApi, '/RestAPIFurb/comandas')
