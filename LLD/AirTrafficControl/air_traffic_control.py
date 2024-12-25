from collections import deque
import queue
from request import Request
from consts import RequestStatus, RequestType
from request_processor import LandingRequestProcessor, TakeoffRequestProcessor
from threading import Thread
from runway import Runway
from exceptions import RunwayNotInIdleRunwaysError
from abc import ABC, abstractmethod
from request_processor import RequestProcessorFactory



class AirTrafficControlMediator(ABC):

    def __init__(self, name: str) -> None:
        self._idle_runways = deque()
        self._pending_requests = queue.Queue()
        self._alloted_runways = deque()
        self.name = name
        self._exit = False

    def add_runway(self, runway: Runway):
        self._idle_runways.append(runway)
    
    def remove_runway(self, runway: Runway):
        if runway in self._idle_runways:
            self._idle_runways.remove(runway)
        else:
            raise RunwayNotInIdleRunwaysError(f"Runway {runway.id} is not in idle runways")
        
    def add_request(self, request: Request):
        self._pending_requests.put(request)

    def process_requests(self):
        print("Processing requests")
        while not self._exit:
            if len(self._idle_runways) > 0 and self._pending_requests.qsize() > 0:
                runway = self._idle_runways.popleft()
                self._alloted_runways.append(runway)
                request: Request = self._pending_requests.get()
                processor = RequestProcessorFactory.get_request_processor(request, runway)
                t = Thread(target=processor.process)
                t.start()

    def stop_processing(self):
        self._exit = True

class AirTrafficControl(AirTrafficControlMediator):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        processing_thread = Thread(target=self.process_requests)
        processing_thread.start()

    
class AirTrafficControlPreAssignedRunways(AirTrafficControlMediator):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._pending_requests = queue.Queue()
        self._preassigned_runways = deque()
        self._exit = False

    def process_requests(self):
        while not self._exit:
            if len(self._idle_runways) > 0 and self._pending_requests.qsize() > 0:
                runway = self.get_optimal_runway(request)
                self._alloted_runways.append(runway)
                request: Request = self._pending_requests.get()
                processor = RequestProcessorFactory.get_request_processor(request, runway)
                t = Thread(target=processor.process)
                t.start()

    def get_optimal_runway(self, request: Request):
        next_runway = self._alloted_runways.popleft()
        self._preassigned_runways.append(next_runway)
        return next_runway