from abc import ABC, abstractmethod

class StockObserver(ABC):

    @abstractmethod
    def update(self, stock_name: str, stock_price: float):
        pass