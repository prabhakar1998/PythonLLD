from abc import ABC, abstractmethod


class Store(ABC):

    def __init__(self, cache_size: int):
        self._cache_size: int = cache_size

    @abstractmethod
    def add(self, key:str, val:str):
        pass

    @abstractmethod
    def get(self, key:str):
        pass

    @abstractmethod
    def is_full(self) -> bool:
        pass

    @abstractmethod
    def remove(self, key: str):
        pass