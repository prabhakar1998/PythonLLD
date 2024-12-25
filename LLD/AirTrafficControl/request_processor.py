from abc import ABC, abstractmethod
from consts import RequestStatus, RequestType
from request import Request
from runway import Runway  

class RequestProcessor(ABC):

    def __init__(self, request, runway):
        self.request = request
        self.runway = runway

    @abstractmethod
    def process(self):
        pass

class LandingRequestProcessor(RequestProcessor):

    def __init__(self, request, runway):
        super().__init__(request, runway)

    def process(self):
        print(f"Created landing processor for request {self.request}")
        self.request.update_request(RequestStatus.Processing)
        aircraft = self.request.get_aircraft()
        aircraft.set_runway(self.runway)
        self.runway.land_aircraft(aircraft)
        aircraft.land()
        self.request.update_request(RequestStatus.Processed)

class TakeoffRequestProcessor(RequestProcessor):

    def __init__(self, request, runway):
        super().__init__(request, runway)

    def process(self):
        print(f"Created takeoff processor for request {self.request}")
        self.request.update_request(RequestStatus.Processing)
        aircraft = self.request.get_aircraft()
        aircraft.set_runway(self.runway)
        self.runway.takeoff_aircraft(aircraft)
        aircraft.take_off()        
        self.request.update_request(RequestStatus.Processed)


class RequestProcessorFactory:

    @staticmethod
    def get_request_processor(request: Request, runway: Runway):
        if request.req_type == RequestType.LandingRequest:
            return LandingRequestProcessor(request, runway)
        elif request.req_type == RequestType.TakeoffRequest:
            return TakeoffRequestProcessor(request, runway)
        else:
            raise ValueError(f"Invalid request type {request.req_type}")