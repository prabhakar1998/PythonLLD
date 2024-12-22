from abc import ABC, abstractmethod
from typing import Set
from .stock_observer import StockObserver

class StockObservable(ABC):

    def __init__(self, stock_name: str, stock_id: str, open_price: float):
        self.stock_name = stock_name
        self.stock_id = stock_id
        self.price = open_price
        self.observers: Set[StockObserver] = set()

    @abstractmethod
    def attach_observer(self, observer: StockObserver):
        pass

    @abstractmethod
    def detach_observer(self, observer: StockObserver):
        pass

    @abstractmethod
    def notify(self):
        pass
    
    @property
    def get_price(self) -> float:
        return self.price

    def update_price(self, price):
        if self.price != price:
            self.price = price
            self.notify()