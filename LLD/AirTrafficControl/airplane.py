from aircraft import Aircraft
from request import LandingRequest, TakeoffRequest
from exceptions import NoRunwayAllotedError


class Airplane(Aircraft):

    def __init__(self, id, atc) -> None:
        super().__init__(id, atc)
        self.runway = None

    def take_off_request(self):
        take_off_request = TakeoffRequest(self)
        self.atc.add_request(take_off_request)

    def land_request(self):
        landing_request = LandingRequest(self)
        self.atc.add_request(landing_request)
    
    def take_off(self):
        if self.runway is None:
            raise NoRunwayAllotedError(f"No runway alloted to the flight {self.id}")
        print(f"Taking off aircraft {self.id} from the runway {self.runway.id}")
        self.runway.set_free()

    def land(self):
        if self.runway is None:
            raise NoRunwayAllotedError(f"No runway alloted to the flight {self.id}")
        print(f"Landing aircraft {self.id} on the runway {self.runway.id}")
        self.runway.set_free()

    def set_runway(self, runway):
        self.runway = runway