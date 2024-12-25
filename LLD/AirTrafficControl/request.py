from consts import RequestStatus, RequestType

from abc import ABC, abstractmethod

class Request(ABC):
    def __init__(self, req_type, aircraft):
        self.req_type = req_type
        self.status = RequestStatus.Pending
        self.aircraft = aircraft

    def update_request(self, status:RequestStatus):
        self.status = status

    def get_aircraft(self):
        return self.aircraft

    
class LandingRequest(Request):

    def __init__(self, aircraft):
        super().__init__(RequestType.LandingRequest, aircraft)

class TakeoffRequest(Request):

    def __init__(self, aircraft):
        super().__init__(RequestType.TakeoffRequest, aircraft)
    