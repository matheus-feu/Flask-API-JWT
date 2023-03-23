from app import app
from ..decorators.acess_token import jwt_required
from ..helpers.helper import authentication
from ..views.user_views import *


@app.route('/', methods=['GET'])
@jwt_required
def get_root(current_user):
    """Endpoint para retornar uma mensagem de boas vindas."""
    return jsonify({'message': f'Olá seja bem vindo {current_user.username}!'})


@app.route('/auth', methods=['POST'])
def authenticate():
    """Endpoint para autenticação de usuário."""
    return authentication()


@app.route('/users', methods=['GET'])
def get_all_users():
    """Endpoint para retornar todos os usuários."""
    return get_user_all()


@app.route('/user/<id>', methods=['GET'])
def get_unique_user(id):
    """Endpoint para retornar por um usuário."""
    return get_user_unique(id)


@app.route('/user/create', methods=['POST'])
def post_user():
    """Endpoint para criar um usuário."""
    return create_user()


@app.route('/user/update/<id>', methods=['PUT'])
def put_user(id):
    """Endpoint para atualizar um usuário."""
    return update_user(id)


@app.route('/user/delete/<id>', methods=['DELETE'])
def del_user(id):
    """Endpoint para deletar um usuário."""
    return delete_user(id)
