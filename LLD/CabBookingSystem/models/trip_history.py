from __future__ import annotations
from abc import ABC
from typing import TYPE_CHECKING
from collections import defaultdict
from typing import List

if TYPE_CHECKING:
    from CabBookingSystem.models.rider import Rider
    from CabBookingSystem.models.trip import Trip


class TripHistory(ABC):

    def __init__(self) -> None:
        self.trips = defaultdict(list)

    def add(self, rider: Rider, trip: Trip):
        self.trips[rider].append(trip)

    def get_trips(self, rider: Rider) -> List[Trip]:
        return self.trips[rider]
    
class CabTripHistory(TripHistory):
    ...