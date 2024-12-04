from db_connection import DBConnection
from config import DB_ADDR, CONFIG
import threading

# Test double-checked locking in a concurrent environment
def create_singleton_instance():
    instance = DBConnection(DB_ADDR, CONFIG)
    print(f"Thread {threading.current_thread().name} got instance id: {id(instance)}")

# Run with multiple threads
threads = []
for i in range(50):  # Create 5 threads to test Singleton
    thread = threading.Thread(target=create_singleton_instance, name=f"T{i+1}")
    threads.append(thread)
    thread.start()
