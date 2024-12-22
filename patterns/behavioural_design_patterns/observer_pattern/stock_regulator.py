from typing import List

from .stock_observable import StockObservable
from .stock_observer import StockObserver
import random
import time
import threading

class StockRegulator:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance == None:
            with cls._lock:
                if cls._instance == None:
                    cls._instance = StockRegulator()
        return cls._instance

    def __init__(self):
        self.stocks: List[StockObservable] = []
        self.brokers: List[StockObserver] = []
        self.__lock = threading.Lock()
        self._simulator_running = True
        thread = threading.Thread(target=self.stock_simulator,)
        thread.start()

    def add_stock(self, stock: StockObservable):
        with self.__lock:
            self.stocks.append(stock)

    def add_stock_broker(self, stock_broker: StockObserver):
        with self.__lock:
            self.brokers.append(stock_broker)

    def stock_simulator(self):
        """Simulates stock price change as we are just mocking here"""
        while self._simulator_running == True:
            for stock in self.stocks:
                cur_price = stock.get_price
                low = cur_price * 0.8
                high = cur_price * 1.2
                rand_price = float(random.randint(int(low), int(high)))
                print(f"Simulator updating price {stock} {rand_price}")
                stock.update_price(rand_price)
            time.sleep(1)

    def stop_stock_simulator(self):
        self._simulator_running = False