from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from CabBookingSystem.exceptions import CabBusyError, NoTripFoundError, DestinationNotArrived
from CabBookingSystem.strategies.booking_strategy import BookingStrategy
from CabBookingSystem.strategies.pricing_strategy import EconomyPricingStrategy, PremiumPricingStrategy, PricingStrategy
from CabBookingSystem.consts import CabStatus, CabType
import time

if TYPE_CHECKING:
    from CabBookingSystem.models.location import Location
    from CabBookingSystem.models.trip import Trip
    from CabBookingSystem.models.location import Location

# represents both cab and the driver


class Cab(ABC):

    def __init__(self, name, number, location: Location, booking_strategy:BookingStrategy, pricing_strategy: PricingStrategy, status=CabStatus.StatusIdle) -> None:
        self.stats = status
        self.name = name
        self.number = number
        self.location = location
        self.booking_strategy: BookingStrategy = booking_strategy
        self.trip: Trip = None
        self.type: CabType = CabType.Basic
        self.pricing_strategy: PricingStrategy = pricing_strategy

    def book(self, trip: Trip) -> bool:
        print(f"Attempting to book cab {self.name}")
        if self.trip is not None or self.stats == CabStatus.StatusOff:
            # already booked
            print("Driver unavailaible")
            return False

        if self.booking_strategy.can_book(self.location, trip):
            self.trip = trip
            self.trip.accept(self.type, self)
            self.stats = CabStatus.StatusBooked
            self.wait_start_time = None
            print(f"Cab {self.name} is successfully booked")
            return True
        return False

    def status_off(self):
        if self.trip is not None:
            raise CabBusyError("Cab is busy service a trip")
        self.stats = CabStatus.StatusOff

    def update_location(self, new_location: Location):
        if self.trip is not None and new_location.get_distance(self.trip.get_source()) < 1:
            self.stats = CabStatus.StatusWaiting
            self.wait_start_time = time.time()
        self.location = new_location

    def start_trip(self, otp:str):
        if self.validate_otp(otp):
            wait_time = 0
            if self.wait_start_time is not None:
                wait_time = time.time() - self.wait_start_time
            self.status = CabStatus.StatusRideStarted
            self.trip.start(self.location, wait_time)
        else:
            raise NoTripFoundError(f"Cab {self.name} is not having any active trip.")

    def validate_otp(self, otp):
        # skipping implementation for LLD
        return True

    def complete_trip(self):
        if self.trip is not None:
            destination_distance = self.location.get_distance(self.trip.destination)
            if destination_distance > 1:
                raise DestinationNotArrived("Cab isn't at destination, ride can't be completed.")
            print("Trip is completed")
            self.trip.close(self.location)
            self.collect_payment()
            self.trip = None
            self.status = CabStatus.StatusIdle
        else:
            raise NoTripFoundError(f"Cab {self.name} is not having any active trip.")

    def collect_payment(self):
        if self.trip is not None:
            fare = self.trip.get_fare(self.pricing_strategy)
            print(f"Trip fare is {fare}")
        else:
            raise NoTripFoundError(f"Cab {self.name} is not having any active trip.")

    def get_type(self):
        return self.type

class CabEconomy(Cab):

    def __init__(self, name, number, location: Location, booking_strategy: BookingStrategy, status=CabStatus.StatusIdle) -> None:
        super().__init__(name, number, location, booking_strategy, EconomyPricingStrategy(), status)
        self.type = CabType.Economy

class CabPremium(Cab):

    def __init__(self, name, number, location: Location, booking_strategy: BookingStrategy, status=CabStatus.StatusIdle) -> None:
        super().__init__(name, number, location, booking_strategy, PremiumPricingStrategy(), status)
        self.type = CabType.Premium