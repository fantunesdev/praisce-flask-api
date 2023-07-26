# Instruções de instalação

Configure a variável de ambiente do Flask
> export FLASK_APP=run.py

## Opção 1 - VENV

Instale a virtualenv:
> python -m venv venv

Ative a virtualenv:
> source venv/bin/activate

Instale as bibliotecas e framework:
> pip -r install requirements.txt
 
## Opção 2 - Poetry

Se você já tem o Poetry configurado e o python 3.11.1 ou superior, basta instalar o ambiente com as demais dependências.
> poetry install

Ative a virtual env.
> poetry shell

## Configurações do banco de dados

Acesse o MySQL e crie o banco de dados:
> CREATE DATABASE seu_database;

Crie a tabela contato:
> CREATE TABLE IF NOT EXISTS praisce.contato (  
&nbsp;&nbsp;&nbsp;&nbsp; id BIGINT NOT NULL AUTO_INCREMENT,  
&nbsp;&nbsp;&nbsp;&nbsp; nome VARCHAR(100) NOT NULL,  
&nbsp;&nbsp;&nbsp;&nbsp; sobrenome VARCHAR(100) NOT NULL,  
&nbsp;&nbsp;&nbsp;&nbsp; email VARCHAR(100) NOT NULL,  
&nbsp;&nbsp;&nbsp;&nbsp; telefone VARCHAR(20) NOT NULL,  
&nbsp;&nbsp;&nbsp;&nbsp; PRIMARY KEY (id)  
);

Saia do MySQL e crie um arquivo com o nome .env na pasta raiz do projeto:
> touch > .env

Adicione as seguintes variáveis substituindo o que está entre aspas pelas configurações do seu database.
> USERNAME = 'seu_usuario'  
> PASSWORD = 'sua_senha'  
> SERVER = 'seu_servidor_mysql'  
> DB = 'seu_database'

## Rodando a API
> flask run