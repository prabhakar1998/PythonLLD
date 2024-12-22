from payment_strategy import PaymentStrategy

class PaypalPaymentStrategy(PaymentStrategy):

    def __init__(self, email_id):
        self.__email_id = email_id
        self.__access_token = None

    def authenticate_user(self, user_name:str, password: str):
        # pass
        self.__access_token = "derrived_access_token"

    def pay(self, amount: float):
        print(f"Payment is processed from Paypal for user {self.__email_id}")