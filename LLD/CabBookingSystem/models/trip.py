from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from CabBookingSystem.strategies.pricing_strategy import PricingStrategy
from CabBookingSystem.consts import CabType, TripStatus
import time

if TYPE_CHECKING:
    from CabBookingSystem.models.cab import Cab
    from CabBookingSystem.models.location import Location
    from rider import Rider


class Trip(ABC):

    def __init__(self, rider: Rider, source: Location, destination: Location) -> None:
        self.rider: Rider = rider
        self.source = source
        self.destination = destination
        self.status = TripStatus.Requested
        self.cab: Cab = None
        self._trip_fare = 0

    def get_destination(self) -> Location:
        return self.destination

    def get_source(self) -> Location:
        return self.source

    def accept(self, cab_type: CabType, cab):
        self.cab_type = cab_type
        self.status = TripStatus.Accepted
        self.cab = cab

    def provide_otp(self, otp):
        if self.cab is not None:
            self.cab.start_trip(otp)

    def start(self, start_location: Location, wait_time: float):
        self.wait_time  = wait_time
        self.start_location = start_location
        self.start_time = time.time()
        print(f"Trip started at {self.start_time}")

    def close(self, end_location: Location):
        self.status = TripStatus.Completed
        self.end_location = end_location
        self.end_time = time.time()

    def get_fare(self, pricing_strategy: PricingStrategy) -> float:
        distance = self.end_location.get_distance(self.start_location)
        travel_time = self.end_time - self.start_time
        self._trip_fare = pricing_strategy.get_fare(distance, self.wait_time, travel_time)
        return self._trip_fare

    def print(self):
        print(f"Trip with {self.cab_type.name} stats is {self.status.name} with fare {self._trip_fare}")