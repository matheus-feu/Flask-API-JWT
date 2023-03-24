from app import app
from ..decorators.acess_token import jwt_required
from ..helpers.helper import authentication
from ..views.user_views import *


@app.route('/', methods=['GET'])
@jwt_required()
def get_root(current_user):
    """Endpoint para retornar uma mensagem de boas vindas."""
    return ({'message': f'Olá seja bem vindo! {current_user.username}'})


@app.route('/auth', methods=['POST'])
def authenticate():
    """Endpoint para autenticação de usuário."""
    return authentication()


@app.route('/users', methods=['GET'])
@jwt_required()
def get_all_users(current_user):
    """Endpoint para retornar todos os usuários."""
    return get_user_all()


@app.route('/user/<id>', methods=['GET'])
@jwt_required()
def get_unique_user(id, current_user):
    """Endpoint para retornar por um usuário."""
    return get_user_unique(id)


@app.route('/user/create', methods=['POST'])
def post_user():
    """Endpoint para criar um usuário."""
    return create_user()


@app.route('/user/update/<id>', methods=['PUT'])
@jwt_required()
def put_user(id, current_user):
    """Endpoint para atualizar um usuário."""
    return update_user(id)


@app.route('/user/delete/<id>', methods=['DELETE'])
@jwt_required()
def del_user(id, current_user):
    """Endpoint para deletar um usuário."""
    return delete_user(id)
