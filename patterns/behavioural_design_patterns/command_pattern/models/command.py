from abc import ABC
from typing import List

class Command(ABC):
    """Represents indivisual command"""

    def __init__(self, command_ip: str):
        self.command_ip: str = command_ip
        self.params: List[str] = []
        self.command_name :str = ""
        self.split_char = " "

    def parse(self):
        args = self.command_ip.split(self.split_char)
        if len(args) == 0:
            raise ValueError("No command specified")

        self.command_name = args[0]
        self.params = args[1:]
    
    def get_name(self) -> str:
        return self.command_name

    def get_params(self) -> List[str]:
        return self.params
    
    def get_command(self) -> str:
        return self.command_ip