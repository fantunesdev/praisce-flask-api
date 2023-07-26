from flask import request, make_response, jsonify
from flask_restful import Resource

from api import api
from ..entidades import contato
from ..schemas import contato_schema
from ..services import contato_services


class ContatoList(Resource):
    def get(self):
        contatos = contato_services.listar_contatos()
        schema_contato = contato_schema.ContatoSchema(many=True)
        return make_response(schema_contato.jsonify(contatos), 200)

    def post(self):
        schema_contato = contato_schema.ContatoSchema()
        validade = schema_contato.validate(request.json)
        if validade:
            return make_response(jsonify(validade), 400)
        else:
            novo_contato = contato.Contato(
                nome=request.json['nome'],
                sobrenome=request.json['sobrenome'],
                email=request.json['email'],
                telefone=request.json['telefone']
            )
            result = contato_services.cadastrar_contato(novo_contato)
            return make_response(schema_contato.jsonify(result), 201)


class ContatoDetail(Resource):
    def get(self, id):
        contato = contato_services.listar_contato_id(id)
        if not contato:
            return make_response(jsonify('Contato não encontrado.'), 404)
        schema_contato = contato_schema.ContatoSchema()
        return make_response(schema_contato.jsonify(contato), 200)

    def put(self, id):
        contato_db = contato_services.listar_contato_id(id)
        if contato_db:
            schema_contato = contato_schema.ContatoSchema()
            validate = schema_contato.validate(request.json)
            if validate:
                return make_response(jsonify(validate), 400)
            else:
                novo_contato = contato.Contato(
                    nome=request.json['nome'],
                    sobrenome=request.json['sobrenome'],
                    email=request.json['email'],
                    telefone=request.json['telefone']
                )
                contato_editado = contato_services.editar_contato(contato_db, novo_contato)
                return make_response(schema_contato.jsonify(contato_editado), 200)
        return make_response(jsonify('Contato não encontrado.'), 404)

    def delete(self, id):
        contato_db = contato_services.listar_contato_id(id)
        if contato:
            contato_services.remover_contato(contato_db)
            return make_response(jsonify(''), 204)
        else:
            return make_response(jsonify('Contato não encontrado.'), 404)


class ContatoSearch(Resource):
    def get(self, nome):
        contato = contato_services.listar_contato_nome(nome)
        if not contato:
            return make_response(jsonify('Contato não encontrado.'), 404)
        schema_contato = contato_schema.ContatoSchema(many=True)
        return make_response(schema_contato.jsonify(contato), 200)


api.add_resource(ContatoList, '/contatos')
api.add_resource(ContatoDetail, '/contatos/<int:id>')
api.add_resource(ContatoSearch, '/contatos/<string:nome>')
