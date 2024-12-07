from threading import Lock
from vehicle import Vehicle

class ParkingSpot:

    def __init__(self, name: str, vehicle: Vehicle):
        self.name = name
        self.vehicle = vehicle
        self._occupied = False
        self._lock = Lock()

    def park_vehicle(self, vehicle: Vehicle):
        if vehicle.get_vehicle_type() != self.vehicle.get_vehicle_type():
            return False

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
        else:
            raise Exception("No parked vehicle to remove")
    
    def is_occupied(self):
        return self._occupied