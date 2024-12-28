from abc import ABC, abstractmethod

from CabBookingSystem.models.location import Location
from CabBookingSystem.models.trip import Trip

class BookingStrategy(ABC):

    @abstractmethod
    def can_book(self, location: Location, trip: Trip) -> bool:
        pass


class MaxDistanceBookingStrategy(BookingStrategy):

    def __init__(self, max_distance: float = 10) -> None:
        self.max_distance = max_distance
        super().__init__()

    def can_book(self, location: Location, trip: Trip) -> bool:
        cab_distance = location.get_distance(trip.get_source())
        if cab_distance <= self.max_distance:
            return True
        print(f"Cab is at distance {cab_distance} from rider can't be booked")
        return False