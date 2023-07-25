from flask import request, make_response, jsonify
from flask_restful import Resource

from api import api
from ..entidades import contato
from ..schemas import contato_schema
from ..services import contato_services


class ContatoList(Resource):
    def get(self):
        contatos = contato_services.listar_contatos()
        cs = contato_schema.ContatoSchema(many=True)
        return make_response(cs.jsonify(contatos), 200)

    def post(self):
        cs = contato_schema.ContatoSchema()
        validade = cs.validate(request.json)
        if validade:
            return make_response(jsonify(validade), 400)
        else:
            novo_contato = contato.Contato(
                nome=request.json["nome"],
                sobrenome=request.json["sobrenome"],
                email=request.json["email"],
                telefone=request.json["telefone"]
            )
            result = contato_services.cadastrar_contato(novo_contato)
            return make_response(cs.jsonify(result), 201)


api.add_resource(ContatoList, '/contatos')
