from xmlrpc.client import Boolean
import mysql.connector as conn
import toml
class DatabaseConnector():
    def __init__(self) -> None:
        config = config = toml.load('app.config.toml')["database"]
        print(config["host"] + " " + config["user"] + " " + config["password"] + " " + config["database"])
        self.conn = conn.connect(host=config["host"], user=config["user"], password=config["password"], database=config["database"])
    
    def get_user(self, user_email) -> tuple:
        cursor = self.conn.cursor()
        cursor.execute("SELECT email, pass_salt, pass_hash FROM users WHERE email = %s", (user_email,))
        user = cursor.fetchone()
        cursor.close()
        return user
    
    def create_user(self, user_email, user_hash, user_salt) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO users (email, pass_hash, pass_salt) VALUES (%s, %s, %s)", (user_email, user_hash, user_salt))
        self.conn.commit()
        cursor.close()
        return True