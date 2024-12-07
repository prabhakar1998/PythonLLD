from parking_lot import ParkingLot
from vehicle import Car, Bike
import time


if __name__ == "__main__":
    parking_lot = ParkingLot(5)

    car1 = Car("C101")

    print(f"Created vehicle of type {car1.get_vehicle_type()}")
    ticket1 = parking_lot.park_vehicle(car1)
    time.sleep(5) # each second is simulated as hour

    bike1 = Bike("B101")
    ticket2 = parking_lot.park_vehicle(bike1)

    time.sleep(5)
    bike2 = Bike("B102")
    ticket3 = parking_lot.park_vehicle(bike2)

    time.sleep(5)
    bill_amount = parking_lot.bill_vehicle(ticket1)
    print(f"Billed with amount {bill_amount}")