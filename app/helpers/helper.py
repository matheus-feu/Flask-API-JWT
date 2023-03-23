import datetime
from http import HTTPStatus

import jwt
from flask import request, jsonify
from werkzeug.security import check_password_hash

from app import app
from ..models.user import UsersModel


def user_by_username(username):
    """Pega um usuário único."""
    try:
        return UsersModel.query.filter(UsersModel.username == username).one()
    except:
        return None


def authentication():
    """Gerando token com base na Secret key do app e definindo expiração do token com 'exp' em 30 minutos.
    Realiza uma autenticação básica de usuário e senha, caso o usuário não exista ou a senha esteja incorreta,
    retorna uma mensagem de erro."""

    # Autenticação básica de usuário e senha
    auth = request.authorization

    # Valida se o usuário e senha foram passados
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Não foi possível verificar, necessário realizar o login'}), HTTPStatus.UNAUTHORIZED

    # Valida se o usuário existe
    user = user_by_username(auth.username)
    if not user:
        return jsonify({'message': 'Usuário não encontrado'}), HTTPStatus.UNAUTHORIZED

    # Valida se a senha está correta
    if user and check_password_hash(user.password, auth.password):
        # Gerando token com base na Secret key do app e definindo expiração do token com 'exp' em 30 minutos
        token = jwt.encode(
            {'username': user.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            app.config['SECRET_KEY'])
        return jsonify({'message': 'Token gerado com sucesso!', 'token': token,
                        'exp': datetime.datetime.now() + datetime.timedelta(minutes=30)}), HTTPStatus.OK

    return jsonify({'message': 'Ocorreu um erro ao realizar o login'}), HTTPStatus.UNAUTHORIZED
