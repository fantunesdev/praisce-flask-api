# Instruções de instalação

Clone este repositório em um diretório de sua escolha e acesse-o:
> git clone git@github.com:fantunesdev/praisce-flask-api.git diretorio_de_sua_escolha  
> cd diretorio_de_sua_escolha

Configure a variável de ambiente do Flask
> export FLASK_APP=run.py

## Opção 1 - VENV

Instale a virtualenv, ative-a e instale as dependências:
> python -m venv venv  
> source venv/bin/activate  
> pip install -r requirements.txt
 
## Opção 2 - Poetry

Caso você já tenha o Poetry configurado e o python 3.11.1 ou superior, basta instalar o ambiente com as demais dependências.

Instale a virtualenv com o poetry e ative-a:
> poetry install  
> poetry shell

## Configurações do banco de dados

Acesse o MySQL, crie o banco de dados e conecte-se a ele:
> CREATE DATABASE seu_database;  
> CONNECT seu_database;

Crie a tabela contato:
> CREATE TABLE IF NOT EXISTS contato (  
&nbsp;&nbsp;&nbsp;&nbsp; id BIGINT NOT NULL AUTO_INCREMENT,  
&nbsp;&nbsp;&nbsp;&nbsp; nome VARCHAR(100) NOT NULL,  
&nbsp;&nbsp;&nbsp;&nbsp; sobrenome VARCHAR(100) NOT NULL,  
&nbsp;&nbsp;&nbsp;&nbsp; email VARCHAR(100) NOT NULL,  
&nbsp;&nbsp;&nbsp;&nbsp; telefone VARCHAR(20) NOT NULL,  
&nbsp;&nbsp;&nbsp;&nbsp; PRIMARY KEY (id)  
);

Saia do MySQL e crie um arquivo com o nome .env na pasta raiz do projeto:
> touch .env

Acesse o arquivo .env e dicione as seguintes variáveis substituindo o que está entre aspas pelas configurações do seu database.
> USERNAME = 'seu_usuario'  
> PASSWORD = 'sua_senha'  
> SERVER = 'seu_servidor_mysql'  
> DB = 'seu_database'

## Rodando a API
> flask run


# Endpoints

### Create
> Verbo HTTP: POST  
> URL: http://localhost:5000/contatos

### Read
> Verbo HTTP: GET  
> URL: http://localhost:5000/contatos

### Update
> Verbo HTTP: PUT  
> URL: http://localhost:5000/contatos/1  
> Obs: Substitua o número 1 pelo ID desejado

### Delete
> Verbo HTTP: DELETE
> URL: http://localhost:5000/contatos/1  
> Obs: Substitua o número 1 pelo ID desejado

### Search
> Verbo HTTP: GET  
> URL: http://localhost:5000/contatos/pedro  
> Obs: Substitua a palavra 'pedro' pelo nome desejado
