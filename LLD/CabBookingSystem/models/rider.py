from __future__ import annotations
from typing import TYPE_CHECKING, List
from abc import ABC, abstractmethod
from CabBookingSystem.exceptions import TripExistsError

if TYPE_CHECKING:
    from CabBookingSystem.cab_booking_system import CabBookingSytem    
    from CabBookingSystem.models.location import Location

from CabBookingSystem.models.trip import Trip

class Rider(ABC):

    def __init__(self, user_id: str, name: str, location: Location, cbs: CabBookingSytem) -> None:
        self.user_id = user_id
        self.name = name
        self.location: Location = location
        self.trip = None
        self.CBS = cbs

    def create_trip(self, destination: Location) -> Trip:
        if self.trip is not None:
            raise TripExistsError(f"Trip already exists for destination {self.trip.destination}")

        print(f"Creating trip for user {self.user_id}")
        self.trip = Trip(self, self.location, destination)
        if self.CBS.request_trip(self, self.trip):
            print(f"Rider {self.name} cab is booked sucessfully.")
            return self.trip
        
        return None
    
    def start_ride(self, otp: str):
        if self.trip is not None:
            self.trip.provide_otp(otp)

    def get_trips(self) -> List[Trip]:
        return self.CBS.get_trips(self)

    def get_id(self):
        return self.user_id
