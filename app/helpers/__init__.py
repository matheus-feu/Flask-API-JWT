import random
import string


def random_string():
    """Gera uma string aleatória para ser usada como chave secreta."""
    return ''.join(random.choice(string.ascii_letters + string.digits + string.ascii_uppercase) for _ in range(12))
