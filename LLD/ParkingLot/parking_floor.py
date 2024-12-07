from consts import VEHICLES, ERROR_INVALID_VEHICLE
from parking_spot import ParkingSpot
from vehicle import Vehicle

class ParkingFloor:

    def __init__(self, floor_number: int):
        self.floor_number = floor_number
        self.parking_spots = {}

    def add_parking_spot(self, parking_spot: ParkingSpot, vehicle: Vehicle):
        vehicle_type = vehicle.get_vehicle_type()
        if vehicle not in self.parking_spots:
            self.parking_spots[vehicle_type] = []
        self.parking_spots[vehicle_type].append(parking_spot)
        
    def get_free_parking_spot(self, vehicle: Vehicle) -> ParkingSpot:
        vehicle_type = vehicle.get_vehicle_type()
        if vehicle_type in self.parking_spots:
            for parking_spot in self.parking_spots[vehicle_type]:
                if not parking_spot.is_occupied():
                    return parking_spot
            return None
        else:
            raise Exception(ERROR_INVALID_VEHICLE)
