import os
import hashlib
from src.controller.user import User, create_user, get_user
from typing import Dict
import base64



def login(mail: str, password: str) -> bool:
    user : User = get_user(mail) 
    if not user:
        return False
    return __hash_password(password, base64.b64decode(user.salt)) == user.hashed_password

def register(mail, password) -> bool:
    user : User = get_user(mail) 
    if user:
        return False
    credentials = __create_password(password)
    user = create_user(mail, credentials["salt"], credentials["hashed_password"])
    return True

def __create_password(password: str) -> Dict:
    salt = os.urandom(32)
    return {"salt":base64.b64encode(salt), "hashed_password": __hash_password(password, salt)}

def __hash_password(password: str, salt: bytearray) -> bytearray:
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return str(base64.b64encode(key), 'utf-8')

