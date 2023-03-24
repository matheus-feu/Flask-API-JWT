from flasgger import Swagger
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from app.docs.swagger import swagger_config, template

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
ma = Marshmallow(app)

swagger = Swagger(app, config=swagger_config, template=template)

with app.app_context():
    from app.models import user

    db.create_all()

# Rotas da aplicação
from app.routes import user_routes
