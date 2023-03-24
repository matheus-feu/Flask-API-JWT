import datetime
from http import HTTPStatus

import jwt
from flask import request
from werkzeug.security import check_password_hash

from app import app
from ..models.user import UserModel


def authentication():
    """Gerando token com base na Secret key do app e definindo expiração do token com 'exp' em 10 minutos.
    Realiza uma autenticação básica de usuário e senha, caso o usuário não exista ou a senha esteja incorreta,
    retorna uma mensagem de erro."""

    # Autenticação básica de usuário e senha
    auth = request.authorization

    # Valida se o usuário e senha foram passados
    if not auth or not auth.username or not auth.password:
        return ({'message': 'Não foi possível verificar, necessário realizar o login'}), HTTPStatus.UNAUTHORIZED

    # Valida se o usuário existe
    user = UserModel.query.filter_by(username=auth.get('username')).first()

    if not user:
        return ({'message': 'Usuário não encontrado'}), HTTPStatus.UNAUTHORIZED
    exp = datetime.datetime.utcnow() + datetime.timedelta(app.config['TOKEN_EXPIRATION'])

    # Valida se a senha está correta
    if user and check_password_hash(user.password, auth.password):
        # Gerando token com base na Secret key do app e definindo expiração do token com 'exp' em 30 minutos
        token = jwt.encode({
            'id': user.id,
            'exp': exp,
            'iat': datetime.datetime.utcnow(),
            'username': user.username},
            app.config['SECRET_KEY'])

        return {'message': 'Token gerado com sucesso!', 'token': token}, HTTPStatus.OK

    return ({'message': 'Ocorreu um erro ao realizar o login'}), HTTPStatus.UNAUTHORIZED
