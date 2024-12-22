from consts import PaymentMethods
from application import PaymentStrategyFactory, User, OrderProcessor
from pytest import fixture

def get_payment_strategy(pay_method):
    user = User("user_id", "user_name", "user@user.com")
    enum_pay_method = PaymentMethods(pay_method)
    payment_processor = PaymentStrategyFactory(enum_pay_method, user)
    payment_strategy = payment_processor.get_payment_strategy()
    return payment_strategy

@fixture
def paypal_strategy():
    pay_method = "Paypal"
    return get_payment_strategy(pay_method)

@fixture
def credit_card_strategy():
    pay_method = "Creditcard"
    return get_payment_strategy(pay_method)

def test_paypal_payment(paypal_strategy):
    order_processor = OrderProcessor(paypal_strategy, 2500)
    assert  order_processor.make_payment() == None

def test_credit_card_payment(credit_card_strategy):
    order_processor = OrderProcessor(credit_card_strategy, 2500)
    assert order_processor.make_payment() == None
