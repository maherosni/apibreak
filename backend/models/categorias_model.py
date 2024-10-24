from config import get_db_connection

class Categoria:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM categorias")
            categors = cursor.fetchall()
        conn.close()
        return categors