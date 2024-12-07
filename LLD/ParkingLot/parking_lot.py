from parking_spot import ParkingSpot
from vehicle import Car, Bike, Vehicle
from parking_floor import ParkingFloor
from parking_ticket import ParkingTicket
from time_range_pricing_stratergy import TimeRangePricingStratergy

from config import BIKE_SPOTS, CAR_SPOTS
from typing import List

class ParkingLot:

    def __init__(self, floors_count: int):
        self.floors_count= floors_count
        self.pricing_stratergy = TimeRangePricingStratergy()

        self._add_floors()

    def _add_floors(self):
        print("Setting up parking lot floors")
        self.floors: List[ParkingFloor] = []
        for floor_number in range(self.floors_count):
            floor = ParkingFloor(floor_number)

            for spot_number in range(CAR_SPOTS):
                spot_name = str(floor_number) + Car.get_vehicle_type() + str(spot_number)
                car_spot = ParkingSpot(spot_name, Car)
                floor.add_parking_spot(car_spot, Car)

            for spot_number in range(BIKE_SPOTS):
                spot_name = str(floor_number) + Bike.get_vehicle_type() + str(spot_number)
                bike_spot = ParkingSpot(spot_name, Bike)
                floor.add_parking_spot(bike_spot, Bike)
            
            self.floors.append(floor)
        print(self.floors)
    
    def park_vehicle(self, vehicle: Vehicle) -> ParkingTicket:
        for floor in self.floors:

            print("Looking for parking spot for vehicle type: ", vehicle.get_vehicle_type(   ))
            spot = floor.get_free_parking_spot(vehicle)            
            if spot:
                spot.park_vehicle(vehicle)
                print(f"Vehicle {vehicle.get_vehicle_numer()} is parked on spot {spot.name}")
                ticket = ParkingTicket(vehicle, "GATE1", spot, self.pricing_stratergy)
                print(f"Ticket generated for vehicle {vehicle.get_vehicle_numer()} !")
                return ticket
            else:
                print(f"No free spot found on {floor}")
        return None

    def bill_vehicle(self, ticket: ParkingTicket) -> float:
        bill_amount = ticket.get_price()
        print(f"Vehicle {ticket.vehicle_number} is billed with amount {bill_amount}")
        return bill_amount
    


