from http import HTTPStatus

from flask import jsonify, request
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

from app.models.user import UsersModel, users_schema, user_schema


def get_user_all():
    """Pega todos os usuários."""
    users = UsersModel.query.all()

    if users:
        result = users_schema.dump(users)
        success_msg = f'{len(users)} usuários cadastrados retornados com sucesso.'
        return jsonify({'message': success_msg, 'data': result}), HTTPStatus.OK

    return jsonify({'message': 'Nenhum usuário encontrado'}), HTTPStatus.NOT_FOUND


def get_user_unique(id):
    """Pega um usuário único."""
    users = UsersModel.query.filter_by(id=id).first()

    if users:
        result = user_schema.dump(users)
        success_msg = f'Usuário {users.username} retornado com sucesso.'
        return jsonify({'message': success_msg, 'data': result}), HTTPStatus.OK

    return jsonify({'message': 'O usuário não encontrado'}), HTTPStatus.NOT_FOUND


def create_user():
    """Cria um usuário novo com o método POST."""

    new_user = UsersModel(**request.json)

    if new_user.validate_username_exists():
        conflict_msg = f'O usuário {new_user.username} já existe.'
        return jsonify({'error': conflict_msg}), HTTPStatus.CONFLICT

    if new_user.validate_email_exists():
        conflict_msg = f'O email {new_user.email} já existe.'
        return jsonify({'error': conflict_msg}), HTTPStatus.CONFLICT

    pass_hash = generate_password_hash(new_user.password)
    new_user.password = pass_hash

    try:
        new_user.save_user()
        result = user_schema.dump(new_user)
        sucess_msg = f'Usuário {new_user.username} criado com sucesso.'
        return jsonify({'message': sucess_msg, 'data': result}), HTTPStatus.CREATED

    except IntegrityError:
        conflict_msg = f'O usuário {new_user.username} já existe.'
        return jsonify({'error': conflict_msg}), HTTPStatus.CONFLICT
    except:
        error_msg = f'Ocorreu um erro ao criar o usuário {new_user.username}.'
        return jsonify({'error': error_msg}), HTTPStatus.INTERNAL_SERVER_ERROR


def update_user(id):
    """Atualiza um usuário com o método PUT."""

    username = request.json['username']
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']

    user = UsersModel.query.get(id)

    # Verificar se o id do usuário existe no banco de dados se não existir retornar erro
    if not user:
        return jsonify({'error': 'O usuário não existe.'}), HTTPStatus.NOT_FOUND

    # Verificar o username existe no banco de dados se existir não atualizar e retornar erro
    if UsersModel.query.filter_by(username=username).first():
        conflict_msg = f'O usuário {username} já existe no sistema.'
        return jsonify({'error': conflict_msg}), HTTPStatus.CONFLICT

    # Verificar o email existe no banco de dados se existir não atualizar e retornar erro
    if UsersModel.query.filter_by(email=email).first():
        conflict_msg = f'O email {email} já existe no sistema.'
        return jsonify({'error': conflict_msg}), HTTPStatus.CONFLICT

    # Gera o hash da senha
    pass_hash = generate_password_hash(password)

    # Se as validações acima forem verdadeiras, então atualiza o usuário
    try:
        user.username = username
        user.name = name
        user.email = email
        user.password = pass_hash
        user.update_user()
        result = user_schema.dump(user)

        success_msg = f'Usuário {user.username} atualizado com sucesso.'
        return jsonify({'message': success_msg, 'data': result}), HTTPStatus.OK

    except IntegrityError:
        conflict_msg = f'O usuário {username} já existe.'
        return jsonify({'error': conflict_msg}), HTTPStatus.CONFLICT
    except:
        error_msg = f'Ocorreu um erro ao atualizar o usuário {username}.'
        return jsonify({'error': error_msg}), HTTPStatus.INTERNAL_SERVER_ERROR


def delete_user(id):
    """Deleta um usuário através do id(pk) com o método DELETE."""

    user = UsersModel.query.get(id)

    if not user:
        return jsonify({'error': 'O usuário não existe.'}), HTTPStatus.NOT_FOUND

    if user:
        try:
            user.delete_user()
            result = user_schema.dump(user)
            success_msg = f'Usuário {user.username} deletado com sucesso.'
            return jsonify({'message': success_msg, 'data': result}), HTTPStatus.OK
        except:
            error_msg = f'Ocorreu um erro ao deletar o usuário {user.username}.'
            return jsonify({'error': error_msg}), HTTPStatus.INTERNAL_SERVER_ERROR
