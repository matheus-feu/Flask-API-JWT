import secrets


def generate_hash_new():
    """Gera um hash aleatório de 32 caracteres hexadecimais,
    em um arquivo chamado 'hash.txt'. ao executar o aplicativo,
    usado na SECRET_KEY para geração do token de autenticação"""

    with open('hash.txt', 'w') as file:
        file.write(secrets.token_hex(nbytes=16))
