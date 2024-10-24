from numpy import sort
import pymysql

def get_db_connection():
    return pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='g5478*9a',
        database='desayunos',
        cursorclass=pymysql.cursors.DictCursor
    )
