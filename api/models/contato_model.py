from api import db


class Contato(db.Model):
    __tablename = 'contato'

    id = db.Column(
        db.Integer, primary_key=True, autoincrement=True, nullable=False
    )
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
