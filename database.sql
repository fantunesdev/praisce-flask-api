CREATE DATABASE praisce;

CREATE TABLE IF NOT EXISTS praisce.contato (
    id BIGINT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    sobrenome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
);

-- CREATE
INSERT INTO praisce.contato (nome,sobrenome,email,telefone) VALUES ('NomePessoa','SobrenomePessoa','email@mail.com','(41) 99999-9999');

-- READ
SELECT id,nome,sobrenome,email,telefone FROM praisce.contato;

-- UPDATE
UPDATE praisce.contato SET nome='NomeEditado', sobrenome='SobrenomeEditado', email='emaileditado@mail.com', telefone='(41) 99999-8888' WHERE id=7;

-- DELETE
DELETE FROM praisce.contato WHERE id=7;

-- SEARCH
SELECT id,nome,sobrenome,email,telefone FROM contato WHERE nome LIKE '%carol%';
