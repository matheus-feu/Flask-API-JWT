from app.helpers import generate_hash_new
import os

db_host = os.environ.get('DB_HOST', 'localhost')
db_port = os.environ.get('DB_PORT', '3309')

SQLALCHEMY_DATABASE_URI = f'mysql://admin:admin@{db_host}:{db_port}/flaskapp'
SQLALCHEMY_TRACK_MODIFICATIONS = False
generate_hash_new()
TOKEN_EXPIRATION = 10
SECRET_KEY = open('hash.txt', 'r').read()
DEBUG = True




