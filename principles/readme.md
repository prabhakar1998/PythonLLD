# Key principles of OOD are:-

1. Prefer composition over inheritance
    Composition: 
        1. When a Class is composed of different behavioural classes to defined the overall behaviour of the composed class.
        2. Loose coupling, class behavious can be easily changed dynamically at run timr also, but changing the behavioural classes that the class is composed of.

    Inheritance:
        1. Tight coupling between super class and sub-class (parent and child respectively). Due to the tight coupling change in parent's behaviour, capabilities will impact the inherited classes.
        2. It can lead to class explosion or tricky to manage when we need hybrid behaviour in the child classes by combining behaviour of it's cousin classes.


2. Program to an interface not an implementation (Dependency inversion principle)
    1. This is the classic dependency inversion principle, that the high level class should always depend on the interface of another class without depending on the concrete implementation class.
    2. This supports the extensibility of the code as we can easily change the composition object from one sub-class to another sub-class and since both will be implementation of interface the composed class will still behave as per the interface definition and will not require any change as such.

3. Encapsulate what varies
    Identify the aspects of your application that vary and seprate them from what stays same.
    ```python
    # Method level encapsulation
    def get_order_total(cart):
        for item in cart.items:
            total += item.get_price()
        # seperate this to another function
        if cart.country == "US":
            total_cost = total * US_TAX_RATE:
        elif cart.country == "IN":
            total_cost = total * IN_TAX_RATE:
    
    #Here we should segregate and abstract the taxation from order method as taxation is bound to change.


    # Class level encapsulation

    # file order.py
    class Order:
        def __init__(self, country: str):

            self.__tax_calculator = TaxCalculatorFactory(country)

        def get_order_total(self):

            self.__tax_calculator.calculate_tax()


    # fil tax_calculator.py
        class TaxCalculator(ABC):
            @abstractmethod
            calculate_tax()
        
        class USTaxCalculator(TaxCalculator):
            calculate_tax()

        class INTaxCalculator(TaxCalculator):
            calculate_tax()


        class TaxCalculatorFactory():
            _country_tax_mapping {
                "IN": INTaxCalculator,
                "US": USTaxCalculator
            }

            def __init__(self, country: str):
                self.country = country
                
            def calculate_tax() -> TaxCalculator:
                if self.country in _country_tax_mapping:
                    tax_calculator = _country_tax_mapping[self.country]
                    return tax_calculator.calculate_tax()
                else:
                    raise ValueError(f"Invalid user type: {self.user_type}")
    ```