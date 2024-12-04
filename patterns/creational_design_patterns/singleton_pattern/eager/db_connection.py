import time
from config import DB_ADDR, CONFIG

class DBConnection:
    # class variable 
    __conn = str(time.time()) # initialized at the time of class being loaded

    def __init__(self, addr, config=None):
        self.addr = addr
        self.config = config
        
    def get_connection(self):
        if DBConnection.__conn is None:
            # init db connection
            print("Initialized DB connection at addr: ", self.addr)
            DBConnection.__conn = str(time.time())
        print("Returned DB connection at addr: ", self.addr, " with connection as ", DBConnection.__conn)
        return DBConnection.__conn