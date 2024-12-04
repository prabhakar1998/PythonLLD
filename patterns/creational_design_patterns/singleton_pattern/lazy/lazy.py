from db_connection import DBConnection
from config import DB_ADDR, CONFIG

if __name__ == "__main__":
    db_con1 = DBConnection(DB_ADDR, CONFIG)
    db_con2 = DBConnection(DB_ADDR, CONFIG)
    db_con3 = DBConnection(DB_ADDR, CONFIG)
    db_con4 = DBConnection(DB_ADDR, CONFIG)

    print(db_con1 == db_con2 == db_con3 == db_con4)