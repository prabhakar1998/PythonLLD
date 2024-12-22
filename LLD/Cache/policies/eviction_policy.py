from abc import ABC, abstractmethod

class EvictionPolicyStrategy(ABC):

    def __init__(self, cache_size):
        self.cache_size = cache_size
    
    @abstractmethod
    def key_accessed(self, key: str) -> None:
        pass

    @abstractmethod
    def get_evicted_key(self) -> str:
        pass