from functools import wraps
from http import HTTPStatus

import jwt
from flask import request, jsonify

from app import app
from app.helpers.helper import user_by_username


def jwt_required(f):
    """Decorator para verificar se o token é válido."""

    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('x-access-token')
        if not token:
            return jsonify({'message': 'token is missing'}), HTTPStatus.UNAUTHORIZED
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = user_by_username(username=data['username'])
        except:
            return jsonify({'message': 'token is invalid or expired'}), HTTPStatus.UNAUTHORIZED
        return f(current_user, *args, **kwargs)

    return decorated
