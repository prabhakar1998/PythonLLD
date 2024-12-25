from abc import ABC, abstractmethod

class Aircraft(ABC):

    def __init__(self, id, atc) -> None:
        self.id = id
        self.atc = atc

    @abstractmethod
    def take_off_request(self):
        pass

    @abstractmethod
    def land_request(self):
        pass
    
    @abstractmethod
    def take_off(self):
        pass

    @abstractmethod
    def land(self):
        pass