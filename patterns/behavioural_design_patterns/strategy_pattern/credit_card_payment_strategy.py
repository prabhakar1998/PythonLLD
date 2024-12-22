from payment_strategy import PaymentStrategy

class CreditCardPaymentStrategy(PaymentStrategy):

    def __init__(self, card_number, expiry, cvv):
        self.__card_number = card_number
        self.__expiry = expiry
        self.__cvv = cvv

    def authenticate_card(self):
        # pass
        return True
    
    def pay(self, amount: float):
        if self.authenticate_card():
            print(f"Payment successful from the card for amount {amount}")