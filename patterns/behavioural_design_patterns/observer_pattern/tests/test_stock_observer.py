from ..stock import Stock
from ..stock_regulator import StockRegulator
from .fixtures import stocks, yahoo_stock_observer, google_stock_observer
import pytest


def test_yahoo_stock_price_change(stocks, yahoo_stock_observer, google_stock_observer):
    print("\n\n")
    for stock in stocks:
        assert stock.attach_observer(yahoo_stock_observer) == True
        assert stock.attach_observer(google_stock_observer) == True

    for stock in stocks:
        stock.update_price(123)

    for stock in stocks:
        stock.update_price(232)
