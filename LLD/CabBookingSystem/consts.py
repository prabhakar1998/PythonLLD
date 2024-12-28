
from enum import Enum


class CabStatus(Enum):
    StatusOff = 0
    StatusIdle = 1
    StatusBooked = 2
    StatusWaiting = 3
    StatusRideStarted = 4

class CabType(Enum):
    Basic = 0
    Economy = 1
    Premium = 2

class TripStatus(Enum):
    Requested = 0
    Accepted = 1
    Started = 2
    Completed = 3