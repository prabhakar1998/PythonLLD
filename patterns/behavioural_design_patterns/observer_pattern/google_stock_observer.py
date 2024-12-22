
from .stock_observer import StockObserver

class GoogleStockObserver(StockObserver):

    def __init__(self, api_endpoint: str, api_secret: str) -> None:
        self._api_endpoint = api_endpoint
        self._api_secret = api_secret

    def update(self, stock_name: str, stock_price: float):
        print(f"{self} got update for the stock: {stock_name} with new_price: {stock_price}")

    def __repr__(self) -> str:
        return "GoogleStockObserver"