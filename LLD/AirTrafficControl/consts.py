from enum import Enum

class RequestType(Enum):
    LandingRequest = "landing"
    TakeoffRequest = "takeoff"

class RequestStatus(Enum):
    Pending = "pending"
    Processed = "processed"
    Processing = "processing"

class RunwayStatus(Enum):
    Free = "free"
    Ocupied = "occupied"
    Landing = "landing"
    TakingOff = "takingoff"