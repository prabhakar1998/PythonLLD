
from payment_strategy import PaymentStrategy
from credit_card_payment_strategy import CreditCardPaymentStrategy
from paypal_payment_strategy import PaypalPaymentStrategy

from consts import PaymentMethods

class OrderProcessor:

    # constructor injection, (Dependency inversion)
    def __init__(self, payment_strategy: PaymentStrategy, amount: float):
        self.__payment_strategy = payment_strategy
        self.amount = amount

    def make_payment(self):
        self.__payment_strategy.pay(self.amount)

class User:

    def __init__(self, user_id, user_name, email_id):
        self.user_id = user_id
        self.email_id = email_id
        self.user_name = user_name
    
    def get_card_number(self):
        # get from user ip
        return ""
    
    def get_card_expiry(self):
        # get from user ip
        return ""
    
    def get_cvv(self):
        # get from user ip
        return ""

    def get_email_id(self):
        return self.email_id
    
class PaymentStrategyFactory:

    def __init__(self, payment_type: PaymentMethods, user: User):

        if payment_type == PaymentMethods.CreditCard:
            card_number = user.get_card_number()
            expiry = user.get_card_expiry()
            cvv = user.get_cvv()

            self.__payment_strategy = CreditCardPaymentStrategy(card_number, expiry, cvv)
        elif payment_type == PaymentMethods.Paypal:
            email_id = user.get_email_id()
            self.__payment_strategy = PaypalPaymentStrategy(email_id)

    def get_payment_strategy(self):
        return self.__payment_strategy
