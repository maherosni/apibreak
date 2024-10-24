from config import get_db_connection

class Product:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM productos")
            products = cursor.fetchall()
        conn.close()
        return products

    @staticmethod
    def get_by_id(idprod):
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM productos WHERE idprod = %s", (idprod,))
            product = cursor.fetchone()
        conn.close()
        return product
        
    @staticmethod
    def get_all_grouped_by_category():
        conn = get_db_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = """
                SELECT p.id, p.nombre, p.descripcion, p.precio, c.nombre AS categoria
                FROM productos p
                JOIN categorias c ON p.idcategoria = c.id
                ORDER BY c.nombre;
                """
        cursor.execute(query)
        products = cursor.fetchall()
        conn.close()

        # Agrupamos los productos por categoría en un diccionario
        grouped_products = {}
        for product in products:
            category = product['categoria']
            if category not in grouped_products:
                grouped_products[category] = []
            grouped_products[category].append({
                'id': product['id'],
                'nombre': product['nombre'],
                'descripcion': product['descripcion'],
                'precio': product['precio']
            })
        
        return grouped_products
    
    @staticmethod
    def create(data):
        conn = get_db_connection()
        with conn.cursor() as cursor:
            sql = "INSERT INTO productos (nomprod, descriprod, precio, idcat) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (data['nomprod'], data['descriprod'], data['precio'], data['idcat']))
            conn.commit()
        conn.close()

    @staticmethod
    def update(idprod, data):
        conn = get_db_connection()
        with conn.cursor() as cursor:
            sql = "UPDATE productos SET nomprod=%s, descriprod=%s, precio=%s, idcat=%s WHERE idprod=%s"
            cursor.execute(sql, (data['nomprod'], data['descriprod'], data['precio'], data['idcat'], idprod))
            conn.commit()
        conn.close()

    @staticmethod
    def delete(idprod):
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM productos WHERE idprod = %s", (idprod,))
            conn.commit()
        conn.close()
