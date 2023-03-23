from app.helpers import random_string


class Config(object):
    """Toda configuração do Flask."""
    SQLALCHEMY_DATABASE_URI = 'mysql://flask:admin@localhost:3309/flaskapp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = random_string()
    DEBUG = True
