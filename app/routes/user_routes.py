from flasgger import swag_from
from .. import app
from ..decorators.acess_token import jwt_required
from ..helpers.helper import authentication
from ..views.user_views import *


@app.route('/api/', methods=['GET'])
@jwt_required()
@swag_from('../docs/root.yml')
def get_root(current_user):
    """Endpoint para retornar uma mensagem de boas vindas."""
    return ({'message': f'Olá seja bem vindo à API! {current_user.username}'})


@app.route('/api/v1/auth', methods=['POST'])
@swag_from('../docs/auth.yml')
def authenticate():
    """Endpoint para autenticação de usuário."""
    return authentication()


@app.route('/api/v1/users', methods=['GET'])
@jwt_required()
@swag_from('../docs/get_all_users.yml')
def get_all_users(current_user):
    """Endpoint para retornar todos os usuários."""
    return get_user_all()


@app.route('/api/v1/user/<id>', methods=['GET'])
@jwt_required()
@swag_from('../docs/get_unique_user.yml')
def get_unique_user(id, current_user):
    """Endpoint para retornar por um usuário."""
    return get_user_unique(id)


@app.route('/api/v1/user/create', methods=['POST'])
@swag_from('../docs/create_user.yml')
def post_user():
    """Endpoint para criar um usuário."""
    return create_user()


@app.route('/api/v1/user/update/<id>', methods=['PUT'])
@jwt_required()
@swag_from('../docs/update_user.yml')
def put_user(id, current_user):
    """Endpoint para atualizar um usuário."""
    return update_user(id)


@app.route('/api/v1/user/delete/<id>', methods=['DELETE'])
@swag_from('../docs/delete_user.yml')
@jwt_required()
def del_user(id, current_user):
    """Endpoint para deletar um usuário."""
    return delete_user(id)
