

from abc import ABC


class PricingStrategy(ABC):

    def __init__(self, multiplier: float = 0.1, km_rate: float = 8.0, wait_charge: float = 3.0) -> None:
        self.multiplier = multiplier # high val as this is simulation 
        self.km_rate = km_rate
        self.wait_charge = wait_charge

    def get_fare(self, distance: float, wait_time: float, travel_time: float) -> float:
        wait_cost = self.wait_charge * wait_time
        travel_cost = self.km_rate * distance
        time_cost = self.multiplier * travel_time
        return wait_cost + travel_cost + time_cost

class EconomyPricingStrategy(PricingStrategy):

    def __init__(self, multiplier: float =1.3, km_rate:float =13.0, wait_charge:float =5.0) -> None:
        super().__init__(multiplier, km_rate, wait_charge)


class PremiumPricingStrategy(PricingStrategy):

    def __init__(self, multiplier: float = 3.5, km_rate: float = 18.0, wait_charge: float = 10.0) -> None:
        super().__init__(multiplier, km_rate, wait_charge)
