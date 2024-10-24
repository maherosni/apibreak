from config import get_db_connection

class Cart:
    @staticmethod
    def add_to_cart(data):
        conn = get_db_connection()
        with conn.cursor() as cursor:
            sql = "INSERT INTO carrito (idprod, iduser, cantidad, total) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (data['idprod'], data['iduser'], data['cantidad'], data['total']))
            conn.commit()
        conn.close()

    @staticmethod
    def get_user_cart(iduser):
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM carrito WHERE iduser = %s", (iduser,))
            cart = cursor.fetchall()
        conn.close()
        return cart
