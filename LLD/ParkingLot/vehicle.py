from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def get_hourly_price(self) -> int:
        pass
    
    @abstractmethod
    def get_vehicle_type() -> str:
        pass
    
    @abstractmethod
    def get_vehicle_numer(self) -> str:
        pass

class Car(Vehicle):
    vehicle_type =  "CAR"

    def __init__(self, vehicle_number):
        self.hourly_price = 10
        self.vehicle_number = vehicle_number

    @staticmethod
    def get_vehicle_type() -> str:
        return Car.vehicle_type

    def get_hourly_price(self) -> int:
        return self.hourly_price

    def get_vehicle_numer(self) -> str:
        return self.vehicle_number

class Bike(Vehicle):
    vehicle_type = "BIKE"

    def __init__(self, vehicle_number: str):
        self.hourly_price = 5
        self.vehicle_number = vehicle_number
    
    @staticmethod
    def get_vehicle_type() -> str:
        return Bike.vehicle_type

    def get_hourly_price(self) -> int:
        return self.hourly_price
    
    def get_vehicle_numer(self) -> str:
        return self.vehicle_number