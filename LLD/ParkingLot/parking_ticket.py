import time
from vehicle import Vehicle
from parking_spot import ParkingSpot
from pricing_stratergy import PricingStratergy

class ParkingTicket:

    def __init__(self, vehicle: Vehicle, entry_gate: str, parking_spot: ParkingSpot, pricing_stratergy: PricingStratergy):

        self.vehicle = vehicle
        self.vehicle_number = vehicle.get_vehicle_numer()
        self.entry_gate = entry_gate
        self.entry_time = time.time()
        self.parking_spot = parking_spot
        self.exit_time = None
        self.pricing_stratergy = pricing_stratergy

    def get_price(self) -> float:
        self.exit_time = time.time()
        stratergy_price = self.pricing_stratergy.get_price(self.vehicle, self.entry_time, self.exit_time)
        print(f"Billed {stratergy_price} from stratergy")
        return stratergy_price