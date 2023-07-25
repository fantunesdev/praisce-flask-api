from ..models import contato_model
from api import db


def cadastrar_contato(contato):
    contato_db = contato_model.Contato(
        nome=contato.nome,
        sobrenome=contato.sobrenome,
        email=contato.email,
        telefone=contato.telefone
    )
    db.session.add(contato_db)
    db.session.commit()
    return contato_db


def listar_contatos():
    contatos = contato_model.Contato.query.all()
    return contatos
