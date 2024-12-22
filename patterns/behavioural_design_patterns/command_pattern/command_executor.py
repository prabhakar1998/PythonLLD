from abc import ABC, abstractmethod
from models.command import Command

class CommandExecutor(ABC):
    
    def __init__(self, parking_lot_mangaer, output_printer):
        self.parking_lot_manager = parking_lot_mangaer
        self.output_printer = output_printer

    @abstractmethod
    def validate(self, command: Command) -> bool:
        pass

    @abstractmethod    
    def execute(self, command) -> None:
        pass