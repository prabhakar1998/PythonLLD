
from .store import Store
import logging

logging.basicConfig(
    level=logging.INFO,  
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__) 


class HashMapStore(Store):

    def __init__(self, cache_size: int):
        super().__init__(cache_size)
        self.memory_store = {}

    def is_full(self):
        return len(self.memory_store) > self._cache_size

    def add(self, key: str, val: str):
        logger.info(f"Added the key: {key} to cache, is_full: ", self.is_full())        
        self.memory_store[key] = val

    def get(self, key: str)-> str:
        logger.debug("reading from current_cache", self.memory_store)
        if key in self.memory_store:
            return self.memory_store[key]
        raise ValueError(f"Key not found error {key}")
    
    def remove(self, key: str):
        logger.info(f"Removing the key: {key}")
        if key not in self.memory_store:
            raise ValueError(f"Key not found error {key}")

        del self.memory_store[key]

        
