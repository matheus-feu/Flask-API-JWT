from functools import wraps
from http import HTTPStatus

import jwt
from flask import request

from app import app
from app.models.user import UserModel


def jwt_required():
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):

            token = None

            if not "x-access-token" in request.headers:
                return ({'message': 'Token is missing!'}), HTTPStatus.UNAUTHORIZED

            token = request.headers['x-access-token']

            try:
                data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            except:
                return ({'message': 'Token is invalid!'}), HTTPStatus.UNAUTHORIZED

            current_user = UserModel(username=data['username'])
            current_user = current_user.validate_username_exists()

            kwargs['current_user'] = current_user

            return f(*args, **kwargs)

        return wrapper

    return decorator
