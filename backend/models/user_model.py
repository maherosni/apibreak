from config import get_db_connection
import hashlib

class User:
    @staticmethod
    def create(data):
        conn = get_db_connection()
        with conn.cursor() as cursor:
            password_hash = hashlib.sha256(data['password'].encode()).hexdigest()
            sql = "INSERT INTO usuarios (username, password, nomus, email, rolus) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (data['username'], password_hash, data['nomus'], data['email'], data['rolus']))
            conn.commit()
        conn.close()

    @staticmethod
    def authenticate(username, password):
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM usuarios WHERE username = %s", (username,))
            user = cursor.fetchone()
            if user and user['password'] == hashlib.sha256(password.encode()).hexdigest():
                return user
        conn.close()
        return None
