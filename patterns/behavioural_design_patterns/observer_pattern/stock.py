
from multiprocessing.sharedctypes import Value
from .stock_observable import StockObservable
from .stock_observer import StockObserver
from typing import Set


# implements the StockObservable class to send the notification to all the observers
class Stock(StockObservable):

    def __init__(self, stock_name: str, stock_id: str, open_price: float):
        super().__init__(stock_name, stock_id, open_price)

    def attach_observer(self, observer: StockObserver):
        if observer not in self.observers:
            print(f"Observer {observer} is added to the observers for stock {self.stock_name}")
            self.observers.add(observer)
            return True
        print(f"Observer {observer} is already added to the observers for stock {self.stock_name}")
        return False
    
    def detach_observer(self, observer: StockObserver):
        if observer in self.observers:
            print(f"Observer {observer} is removed form the observers")
            self.observers.remove(observer)
            return True
        else:
            raise ValueError(f"Observer {observer} is not present in the observers of the stock {self.stock_name}")

    def notify(self):
        for observer in self.observers:
            observer.update(self.stock_name, self.price)

    def __repr__(self) -> str:
        return self.stock_name