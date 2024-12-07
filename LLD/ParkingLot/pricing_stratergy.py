from abc import ABC, abstractmethod
from vehicle import Vehicle

class PricingStratergy(ABC):

    @abstractmethod
    def get_price(vehicle_type: Vehicle, entry_time: float, exit_time: float) -> float:
        pass

    
    