
from ..command_executor_factory import CommandExecutorFactory
from ..models.command import Command
from .ip_mode import IPMode

class FileInputMode(IPMode):

    def __init__(self, command_executor_factory: CommandExecutorFactory, output_printer, file_path: str) -> None:
        super().__init__(command_executor_factory, output_printer)
        self.file_path = file_path

    def process(self):
        with open(self.file_path, "r") as fl:
            read_line = fl.readline()
            command = Command(read_line)
            self.process_command(command)
