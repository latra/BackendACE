from datetime import datetime, timedelta
from src.controller.user import get_user
from src.auth.encryption import encrypt, decrypt


def is_valid(token) -> bool:
    plain_token = decrypt(token)
    if plain_token:
        plain_token = plain_token.split(">>")
        return plain_token[1] if get_user(plain_token[1]) and datetime.now() < datetime.strptime(plain_token[0], "%Y-%m-%d %H:%M:%S.%f") else None
    return None
def create_token(user_id):
    expires = datetime.now() + timedelta(hours=1)
    return encrypt(f"{expires}>>{user_id}")
