from consts import RunwayStatus
from exceptions import RunwayIsOccupiedError
import time

class Runway:

    def __init__(self, id, atc) -> None:
        self.id = id
        self._is_free: bool = True
        self._aircraft = None
        self._status = RunwayStatus.Free
        self.atc = atc
    
    def is_free(self) -> bool:
        return self._is_free

    def land_aircraft(self, aircraft):
        if self._is_free:
            self._aircraft = aircraft
            self._status = RunwayStatus.Landing
            time.sleep(2)
            self._is_free = False
        else:
            raise RunwayIsOccupiedError(f"Runway {self.id} is already occupied")
        
    def takeoff_aircraft(self, aircraft):
        if self._is_free:
            self._aircraft = aircraft
            self._status = RunwayStatus.TakingOff
            time.sleep(2)
            self._is_free = False
        else:
            raise RunwayIsOccupiedError(f"Runway {self.id} is already occupied")
        
    def set_free(self):
        self._is_free = True
        self._aircraft = None
        self._status = RunwayStatus.Free
        self.atc.add_runway(self)