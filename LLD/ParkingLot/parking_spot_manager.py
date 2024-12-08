from parking_spot import ParkingSpot, TwoWheelerParkingSpot, FourWheelerParkingSpot
from vehicle import Vehicle, TwoWheelerVehicle, TwoWheelerVehicle
from parking_stratergy import ParkingStratergy
from typing import List
from abc import ABC, abstractmethod

class ParkingSpotManager(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def add_parking_spots(self):
        pass

    @abstractmethod
    def remove_parking_spots(self):
        pass

    @abstractmethod
    def find_parking_spot(self):
        # based on the stratergy can return nearest or random
        pass

    @abstractmethod
    def park_vehicle(self, vehicle: Vehicle) -> bool:
        pass
    
    @abstractmethod
    def remove_vehicle(self) -> bool:
        pass

class TwoWheelerParkingSpotMaganer(ParkingSpotManager):

    def __init__(self, parking_stratergy: ParkingStratergy):
        self.__parking_spots: List[ParkingSpot] = [] 

    def add_parking_spots(self):
        return super().add_parking_spots()
    
    def remove_parking_spots(self):
        return super().remove_parking_spots()
    
    def find_parking_spot(self) -> TwoWheelerParkingSpot:
        return super().find_parking_spot()

    def park_vehicle(self, vehicle: TwoWheelerVehicle) -> bool:
        spot = self.find_parking_spot()
        return spot.park_vehicle(vehicle)
    
    def remove_vehicle(self, spot: TwoWheelerParkingSpot):
        return spot.remove_vehicle()

class ThreeWheelerParkingSpotMaganer(ParkingSpotManager):

    def __init__(self):
        self.__parking_spots: List[ParkingSpot] = [] 

    def add_parking_spots(self):
        return super().add_parking_spots()
    
    def remove_parking_spots(self):
        return super().remove_parking_spots()
    
    def find_parking_spot(self):
        return super().find_parking_spot()

    def park_vehicle(self, vehicle: TwoWheelerVehicle) -> bool:
        spot = self.find_parking_spot()
        return spot.park_vehicle(vehicle)
    
    def remove_vehicle(self, spot: TwoWheelerVehicle):
        return spot.remove_vehicle()