from app.helpers import generate_hash_new


class Config(object):
    """Toda configuração do Flask."""
    SQLALCHEMY_DATABASE_URI = 'mysql://flask:admin@localhost:3309/flaskapp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    generate_hash_new()
    TOKEN_EXPIRATION = 10
    SECRET_KEY = open('hash.txt', 'r').read()
    DEBUG = True
