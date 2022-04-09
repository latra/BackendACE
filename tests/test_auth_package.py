import unittest
import hashlib
import tracemalloc

from src.auth.login import register

tracemalloc.start()
class TestCrypto(unittest.TestCase):
    def test_cryp_decryp(self):
        from src.auth.encryption import encrypt, decrypt
        key = hashlib.sha256().digest()
        file = open("authentication.key", "wb")
        file.write(key)
        file.close()
        assert "Hola" == decrypt(encrypt("Hola"))

    def test_token_generation(self):
        from src.auth.token import create_token, is_valid
        user = "demo@test.es"
        token = create_token(user)
        assert is_valid(token) == user

    def test_login(self):
        from src.auth.login import login
        # assert register("demo3@test.es", "kakatua")
        assert login("demo3@test.es", "kakatua")
        assert not login("johndoe2", "patata")
        assert not login("demo3@test.es", "patata")


if __name__ == '__main__':
    unittest.main()
