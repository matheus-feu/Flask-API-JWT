from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.app_context().push()

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Rotas da aplicação
from app.routes import user_routes
