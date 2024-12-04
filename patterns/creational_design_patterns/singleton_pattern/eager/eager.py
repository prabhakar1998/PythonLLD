from db_connection import DBConnection
from config import DB_ADDR, CONFIG

if __name__ == "__main__":
    db_con1 = DBConnection(DB_ADDR, CONFIG).get_connection()
    db_con2 = DBConnection(DB_ADDR, CONFIG).get_connection()
    print(db_con1 == db_con2)