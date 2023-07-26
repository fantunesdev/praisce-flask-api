from marshmallow import fields

from api import ma
from ..models import contato_model


class ContatoSchema(ma.Schema):
    class Meta:
        model = contato_model.Contato
        fields = ('id', 'nome', 'sobrenome', 'email', 'telefone')

    nome = fields.String(required=True)
    sobrenome = fields.String(required=True)
    email = fields.Email(required=True)
    telefone = fields.String(required=True)
