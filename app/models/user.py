import datetime

from app import db, ma


class UserModel(db.Model):
    """Definição da classe/tabela que representa os usuários no banco de dados."""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def __init__(self, username, password=None, name=None, email=None):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

    def create_db(self):
        """ Cria o banco de dados."""
        db.create_all()

    def validate_username_exists(self) -> object:
        """Verifica se o usuário já existe no banco de dados."""
        username = UserModel.query.filter_by(username=self.username).first()
        return username

    def validate_email_exists(self) -> object:
        """Verifica se o email já existe no banco de dados."""
        email = UserModel.query.filter_by(email=self.email).first()
        return email

    def save_user(self):
        """Salva o usuário no banco de dados."""
        db.session.add(self)
        db.session.commit()

    def update_user(self):
        """Atualiza o usuário no banco de dados."""
        db.session.commit()

    def delete_user(self):
        """Deleta o usuário do banco de dados."""
        db.session.delete(self)
        db.session.commit()


class UsersChema(ma.Schema):
    """Definição do esquema que representa os usuários."""

    class Meta:
        """Campos que serão retornados."""
        fields = ('id', 'username', 'password', 'name', 'email')


# Inicializa o esquema para um usuário
user_schema = UsersChema()

# Inicializa o esquema para vários usuários
users_schema = UsersChema(many=True)
