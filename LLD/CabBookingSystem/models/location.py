from abc import ABC, abstractmethod
from math import sqrt

class Location(ABC):


    @abstractmethod
    def get_distance(self, destination) -> float:
        pass


class TwoDimentionalLocation(Location):

    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = x
        self.y = y

    def get_distance(self, destination) -> float:
        return sqrt((self.x - destination.x)**2 + (self.y - destination.y)**2)
    
class GPSLocation(Location):

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_distance(self, destination):
        ...

    