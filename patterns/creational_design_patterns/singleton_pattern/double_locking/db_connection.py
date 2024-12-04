import time
from threading import Lock


class DBConnection:
    # class variable 
    _instance = None
    __lock = Lock()
    __conn = None

    def __init__(self, addr, config=None):
        self.addr = addr
        self.config = config
        
    def __new__(cls, addr, config=None):
        if cls.__conn is None: # First check to avoid unnecessary locking
            with cls.__lock: # aquire lock to ensure only one thread gets access inside
                if cls.__conn is None: #Second check: Instance might have been created while waiting for the lock
                    cls._instance = super().__new__(cls)
                    print("Initialized DB connection at addr: ", addr)
                    cls.__conn = str(time.time())
        return cls._instance

    def get_connection(self):
        print("Returned DB connection at addr: ", self.addr, " with connection as ", DBConnection.__conn)
        return DBConnection.__conn
