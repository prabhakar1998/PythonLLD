from typing import List
from pytest import fixture
from ..google_stock_observer import GoogleStockObserver
from ..stock_regulator import StockRegulator
from ..yahoo_stock_observer import YahooStockObserver
from ..stock import Stock
import sys, os

@fixture
def stocks() -> List[Stock]:
    stock1 = Stock("Company 1", "CN1", 12.334)
    stock2 = Stock("Company 2", "CN2", 3.334)
    stock3 = Stock("Company 3", "CN3", 150.334)
    stock4 = Stock("Company 4", "CN4", 299.334)

    stocks: List[Stock] = [stock1, stock2,  stock3, stock4]
    return stocks

@fixture
def regulator() -> StockRegulator:
    regulator = StockRegulator()
    return regulator

@fixture
def yahoo_stock_observer() -> YahooStockObserver:
    return YahooStockObserver("mock.yahoo.com", "mock_key")

@fixture
def google_stock_observer() -> GoogleStockObserver:
    return GoogleStockObserver("mock.google.com", "mock_key")