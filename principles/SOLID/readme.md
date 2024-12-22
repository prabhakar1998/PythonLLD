# SOLID principles.

1. Single responsibility principle
    A class should have only one reason to change and have only responsibility.
    With this we should extend this principle to the functions to have only one responsibility.

    Example:
    ```python
        class OrderProcessor:

            def get_items()

            def get_total_cost()

            def calculate_tax()

            def process_payment()
    ```
    Here in this example the OrederProcessor class is taking too many responsibilities, it is maintaining the list of the items in the order,
    calculating order cost, managing the tax related calculations which are not responsibility of the orderProcessor, processing payemnt

    ```python
        class OrderProcessor:
            def get_total_cost()

        class PaymentProcessor:
            def process_payment()

        class TaxCalculator:
            def calculate_tax()

        class CartManager:
            def get_items()
    ```
    This is the improvised design using the Single responsibility principle, key advantange is that any change in taxCalculator will not require any change in any other class

2. Open and close principle
    Class should be open for extension (inheritance) but closed for modification.
    Since we are restricting the class modification, we will not break any existing behaviour, we can only add new capabilities or responsibilities to the application.

    ```python
    class PaymentProcessor:

        def process_payment(self, payment_method):
            if payment_method == PaymentEnum.Card:
                card = get_card_details()
                charge_bank(card)
            elif payment_method == PaymentEnum.Cash:
                paid_amt = collect_cash()
                update_cash_counter(paid_amt)
            else:
                raise ValueError("Unsupported payment method")

    ```
    Now if want to add another payment method of PaymentEnum.UPI, we will   have to modify the existing payment_processor.
    To mitigate this we should segregate classes.
    ```python
    class PaymentProcessor(ABC):
        @abstractmethod
        def process_payment():
            pass
    
    class CashPaymentProcessor(PaymentProcessor):
        def process_payment():
            # processing the case payment
    
    class UPIPaymentProcessor(PaymentProcessor):
        def process_payment():
            # processing the UPI payment

    
    class PaymentProviderFactory:
        def __init__(self, payment_method: ProcessorEnum):
            self.payment_method = payment_method
            if self.payment_method == ProcessorEnum.UPIPayment:
                self.payment_method: PaymentProcessor = UPIPaymentProcessor()
            elif self.payment_method == ProcessorEnum.CashPayment:
                self.payment_method: PaymentProcessor = CashPaymentProcessor()
        
        def process_payment(self):
            self.payment_method.process_payment()
    ```
3. Liskov subsititution principleThe interview started with my Introduction and then asked me 2 coding questions. After this, he proceeded to ask about my Project and internship work. Technical questions were asked on topics like multithreading, concurrency, semaphores, deadlock, etc. Questions from databases like Indexing, B trees, B+ trees. Questions from DSA were from trees and graphs. The college and Internship projects which I did were real projects and not copied from GitHub so when I talked about them, they sounded real as the work on them is still going on and I could talk about them confidently.


    The sub class should be inherited without breaking the super class behaviour in the sub-class.
    The object of super class should be replacable by the subclass object anywhere in the code without breaking it's functionality.

    ```python

        class Bird:

            def fly():
                pass

            def eat():
                pass

        # here penuin inherits bird but is breaking the behaviour of the bird.
        class Penguin(Bird):
            def fly()
                # do nothing as can't fly
                pass
            
            def eat():
                pass
    ```

    Corrected code
    ```python
    
        class Bird:
            def eat():
                pass

        class FlyingBird(Bird):
            def fly():
                pass
        
        class Penguin(Bird):
            def eat():
                pass

    ```
    Here the Bird class object can be repalced by either of FlyingBird or Penguin as there will not be any breaking change in this case.

4. Interface segregation principle

    Clients shouldn't be forced to implement the methods they dont intend to use.
    This means that interfaces should be kept as minimal as possible and big fat interfaces should be broken in smaller logical units of interface.
    ```python

        from abc import ABC, abstractmethod
        class Vehicle(ABC):
            @abstractmethod
            def fly(self):
                pass
                
            @abstractmethod
            def drive(self):
                pass

        class AirCraft(Vehicle):
            def fly(self):
                # fly
                pass
                
            def drive(self):
                #drive
                pass
        
        class Car(Vehicle):
            def fly(self):
                raise Exception("Can't Fly")
            
            def drive(self):
                #drive
                pass
    ```
    Vehicle interface is enforcing both drive and fly to all it's implementation where as certain vehicles can't fly. This can be resolved by defining granular interfaces.

    ```python
        from abc import ABC, abstractmethod
        
        class Drivable(ABC):
            @abstractmethod
            def drive(self):
                pass

        class Flyable(Drivable):
            @abstractmethod
            def fly(self):
                pass
        
        class Car(Drivable):
            def drive(self):
                # drive the car
                pass
        
        class Aricraft(Flyable):
            def fly(self):
                # implement flying
                pass
                
            def drive(self):
                # implement driving
                pass
    ```

5. Dependency inversion principle

    The high level class shouldn't depend on low level classes.
    Both should depend on abstraction. 
    Abstractions shouldn't depend on details but details should be dependent on abstractions.

    ```python

        class FileLogger:

            class log(self):
                # log to file
                pass
        
        class Application:

            def __init__(self):
                self.logger = FileLogger()
    
    ```
    Here we have tight coupling of the FileLogger and Application, any change in the FileLogger implementation will directly impact the Application.
    Also if we need to change from FileLogger to Standard output then we will not be able to do it here without modifying the Application class which voilates the Open closed principle.

    ```python
        from abc import ACB, abstractmethod
        class Logger(ABC):
            @abstractmethod
            def log(self):
                pass
        
        class FileLogger(Logger):
            def log(self):
                # loggin to file
                pass

        class STDLogger(Logger):
            def log(self):
                # loggin to stdout
                pass

        class Application:

            # we can either pass the logger directly, or use a logger factory here based on the loggin_type which can be LoggerEnum FileLogger,   
            def __init__(self, logger: Logger):
                self.logger = logger

    ```