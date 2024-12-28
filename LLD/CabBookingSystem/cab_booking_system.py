import threading

from CabBookingSystem.models.trip import Trip
from CabBookingSystem.models.trip_history import TripHistory
from CabBookingSystem.exceptions import RiderNotRegistered
from CabBookingSystem.models.cab import Cab
from CabBookingSystem.models.rider import Rider
from typing import List, Set

class CabBookingSytem:
    __instance = None
    __lock = threading.Lock()

    def __new__(cls, *args):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance =  super().__new__(cls)
        return cls.__instance

    def __init__(self, name: str):
        self.name = name
        self.cabs: Set[Cab] = set()
        self.riders: Set[Rider] = set()
        self.trip_history: TripHistory = TripHistory()

    def register_cab(self, cab:Cab):
        if cab not in self.cabs:
            self.cabs.add(cab)

    def register_rider(self, rider:Rider):
        self.riders.add(rider)

    def request_trip(self, rider: Rider, trip: Trip):
        if rider not in self.riders:
            raise RiderNotRegistered(f"Rider {rider.get_id()} is not registered")

        # inefficient search b/w cabs (there an be efficient search of cabs b/w two points assuming this to be beyond current scope)        
        for cab in self.cabs:
            if cab.book(trip):
                self.trip_history.add(rider, trip)
                return True
        return False

    def get_trips(self, rider: Rider):
        if rider not in self.riders:
            raise RiderNotRegistered(f"Rider {rider.get_id()} is not registered")
        return self.trip_history.get_trips(rider)