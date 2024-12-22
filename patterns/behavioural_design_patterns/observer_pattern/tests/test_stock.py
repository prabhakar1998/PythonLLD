from ..stock import Stock
from ..stock_regulator import StockRegulator
from .fixtures import stocks, yahoo_stock_observer, google_stock_observer
import pytest


def test_attach_observer(stocks, yahoo_stock_observer):
    print("\n\n")
    for stock in stocks:
        assert stock.attach_observer(yahoo_stock_observer) == True

def test_detach_observer(stocks, yahoo_stock_observer):
    print("\n\n")
    for stock in stocks:
        assert stock.attach_observer(yahoo_stock_observer) == True
        assert stock.detach_observer(yahoo_stock_observer) == True

def test_detach_observer_invalid(stocks, yahoo_stock_observer, google_stock_observer):
    print("\n\n")
    for stock in stocks:
        assert stock.attach_observer(yahoo_stock_observer) == True
        with pytest.raises(ValueError):
            stock.detach_observer(google_stock_observer)

