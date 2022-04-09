from xmlrpc.client import Boolean
from src.connector.user_database import DatabaseConnector

class User:
    def __init__(self, email, salt, hashed_password):
        self.email = email
        self.salt = salt
        self.hashed_password = hashed_password


fake_db = {
        "johndoe@test.es": {
            "email": "johndoe@test.es",
            "salt": b"\xe3\x90n\xaf\xa1QU-\xdac\xbe\xc6\xa5\x852\xabf[}\xaf\xcahn\x0fYi\xef\xcd\x1c\xef#\xc3",
            "hashed_password": b"n!#\xd6\xd6\xfaT\x1d\x13\xe0'\xff\x83\xd0Ut\xba\r\xeb\x1b\xe6R\xa5\xb6\xf3\xa7\x0eDU\xcf\x98\x03"
        }
    }
def create_user(email, salt, hashed_password) -> bool:
    return DatabaseConnector().create_user(email, hashed_password, salt)

def get_user(user: str) -> User:
    user_tuple = DatabaseConnector().get_user(user)
    return User(user_tuple[0], user_tuple[1], user_tuple[2]) if user_tuple else None

