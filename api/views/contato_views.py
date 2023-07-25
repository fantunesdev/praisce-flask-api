from flask_restful import Resource
from api import api


class ContatoList(Resource):
    def get(self):
        return "Olá mundo"


api.add_resource(ContatoList, '/contatos')
