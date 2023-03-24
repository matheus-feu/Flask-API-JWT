[![wakatime](https://wakatime.com/badge/user/3bd24664-869f-460a-94e1-b98da8136504/project/e6a36cc3-1b65-406f-92f4-b996d8cccb14.svg)](https://wakatime.com/badge/user/3bd24664-869f-460a-94e1-b98da8136504/project/e6a36cc3-1b65-406f-92f4-b996d8cccb14)


<h2 align="center"> API Flask - CRUD Users 🚀 </h2> 

## Índice 📋

- [Sobre](#-sobre)
- [Tecnologias utilizadas](#-tecnologias-utilizadas)
- [Instalação](#-instalação)
- [Endpoints](#-endpoints)
- [Bibliotecas](#-bibliotecas)
- [Contato](#-contato)

## 📖 Sobre

O projeto **API Flask - CRUD Users** é uma API RESTful desenvolvida em Python com o framework Flask, que realiza o CRUD
de usuários.

A API foi desenvolvida com o intuito de praticar os conhecimentos adquiridos em Python e Flask, além de aprender a
utilizar o banco de dados MySQL que está dockerizado, utilizando o Docker.

Basicamente, a API realiza o CRUD de usuários, onde é possível cadastrar, listar, atualizar e deletar usuários e
autenticar utilizando JWT.

## 🚀 Tecnologias utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
![JWT](https://img.shields.io/badge/jwt-%2300C300.svg?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)
![Postman](https://img.shields.io/badge/postman-%23FF6C37.svg?style=for-the-badge&logo=postman&logoColor=white)
![Pycharm](https://img.shields.io/badge/pycharm-%23000000.svg?style=for-the-badge&logo=pycharm&logoColor=white)

## ⚙️ Instalação

#### 💻 Pré-requisitos

Antes de começar você vai precisar ter instalado em sua máquina as seguintes ferramentas:

- Você instalar o versão mais recente do [Python](https://www.python.org/downloads/), estou utilizando a 3.11.
- Você instalar o [Docker](https://www.docker.com/products/docker-desktop).
- Você instalar o [Postman](https://www.postman.com/downloads/).
- Ter instalado o [Git](https://git-scm.com/downloads) para clonar o projeto.
- Ter instalado o [Pycharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=windows) para abrir o projeto ou
  qualquer outro editor de sua preferência.

Com tudo instalado, você pode seguir os passos abaixo:

#### 🎲 Rodando o projeto

- Clone este repositório

```bash
$ git clone https://github.com/matheus-feu/Flask-API-JWT.git
```

- Acesse a pasta do projeto no terminal/cmd

```bash
$ cd Flask-API-JWT
```

- Crie um ambiente virtual

```bash
$ python -m venv venv
```

- Ative o ambiente virtual

```bash
$ venv\Scripts\activate
```

- Instale as dependências

```bash
$ pip install -r requirements.txt
```

- Execute o `docker-compose` para subir o banco de dados.

```bash
$ docker-compose up -d
```

- Execute o projeto

```bash
$ python app.py
```

## 📌 Endpoints

O fluxo da API é um CRUD de usuários, basicamente:

- Cadastro de usuário na rota `/user/create`, permitindo que o usuário se autentique na API e tenha acesso aos demais
  endpoints.
- Ao se cadastrar, realizar a autenticação na rota `/auth`, gerando um token JWT que será utilizado para as demais
  requisições.
- Com o token em mãos, autentique-se e poderá listar todos os usuários cadastrados na rota `/users`, permitindo que o
  usuário autenticado possa visualizar todos os
  usuários cadastrados.
- Listar apenas um usuário cadastrado na rota `/users/<id>`, permitindo que o usuário autenticado possa visualizar
  apenas
  o usuário que foi passado o id.
- Aualizar um usuário cadastrado na rota `/users/<id>`, permitindo que o usuário autenticado possa atualizar apenas o
  usuário que foi passado o id.
- Deletar um usuário cadastrado na rota `/users/<id>`, permitindo que o usuário autenticado possa deletar apenas o
  usuário que foi passado o id.

## 📚 Bibliotecas

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [PyJWT](https://pyjwt.readthedocs.io/en/stable/)
- [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)
- [MySqlClient](https://pypi.org/project/mysqlclient/)

## 📞 Contato

- [Linkedin](https://www.linkedin.com/in/matheus-feu-558558186/)
- [GitHub](https://github.com/matheus-feu)
- [Instagram](https://www.instagram.com/math_feu/)
- [Gmail](mailto:matheusfeu@gmail.com)
