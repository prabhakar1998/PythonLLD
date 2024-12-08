from abc import ABC, abstractmethod
from threading import Lock
from vehicle import Vehicle, TwoWheelerVehicle, FourWheelerVehicle

class ParkingSpot(ABC):

    def __init__(self, name: str):
        pass

    @abstractmethod
    def park_vehicle(self, vehicle: Vehicle) -> bool:
        pass
    
    @abstractmethod
    def remove_vehicle(self):
        pass
    
    @abstractmethod
    def is_occupied(self) -> bool:
        pass

class TwoWheelerParkingSpot(ParkingSpot):
        
    def __init__(self, name: str):
        self.name = name
        self.vehicle = None
        self._occupied = False
        self._lock = Lock()

    def park_vehicle(self, vehicle: TwoWheelerVehicle) -> bool:
        # handle concurrency
        if self._occupied is False:
            with self._lock:
                if self._occupied is False:
                    self._occupied = True
                    return True
        return False
    
    def remove_vehicle(self):
        # handle concurrency
        if self._occupied:
            with self._lock:
                if self._occupied:
                    self._occupied = False
                    self.vehicle = None
        else:
            raise Exception("No parked vehicle to remove")
    
    def is_occupied(self) -> bool:
        return self._occupied

class FourWheelerParkingSpot(ParkingSpot):
        
    def __init__(self, name: str):
        self.name = name
        self.vehicle = None
        self._occupied = False
        self._lock = Lock()

    def park_vehicle(self, vehicle: FourWheelerVehicle) -> bool:
        # handle concurrency
        if self._occupied is False:
            with self._lock:
                if self._occupied is False:
                    self._occupied = True
                    return True
        return False
    
    def remove_vehicle(self):
        # handle concurrency
        if self._occupied:
            with self._lock:
                if self._occupied:
                    self._occupied = False
                    self.vehicle = None
        else:
            raise Exception("No parked vehicle to remove")
    
    def is_occupied(self) -> bool:
        return self._occupied

class ParkingSpotFactory:

    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle

    def get_parking_spot(self):
        if self.vehicle == TwoWheelerVehicle:
            return TwoWheelerParkingSpot()
        elif self.vehicle == FourWheelerVehicle:
            return FourWheelerParkingSpot()