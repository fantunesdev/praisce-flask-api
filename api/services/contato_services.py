from api import db

from ..models import contato_model


def cadastrar_contato(contato):
    contato_db = contato_model.Contato(
        nome=contato.nome,
        sobrenome=contato.sobrenome,
        email=contato.email,
        telefone=contato.telefone,
    )
    db.session.add(contato_db)
    db.session.commit()
    return contato_db


def listar_contatos():
    contatos = contato_model.Contato.query.all()
    return contatos


def listar_contato_id(id):
    contato = contato_model.Contato.query.filter_by(id=id).first()
    return contato


def listar_contato_nome(nome):
    contatos = contato_model.Contato.query.filter(
        contato_model.Contato.nome.like(f'%{nome}%')
    ).all()
    return contatos


def editar_contato(contato_db, contato_novo):
    contato_db.nome = contato_novo.nome
    contato_db.sobrenome = contato_novo.sobrenome
    contato_db.email = contato_novo.email
    contato_db.telefone = contato_novo.telefone
    db.session.commit()
    return contato_db


def remover_contato(contato):
    db.session.delete(contato)
    db.session.commit()
