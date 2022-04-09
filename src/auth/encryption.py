import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
def encrypt(raw):
    file = open("authentication.key", "rb")
    private_key = file.read()
    file.close()
    
    raw = pad(raw)

    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw.encode('utf-8')))

def decrypt(enc):
    file = open("authentication.key", "rb")
    private_key = file.read()
    file.close()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    try:
        return unpad(cipher.decrypt(enc[16:])).decode()
    except ValueError:
        return None