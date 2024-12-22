from abc import ABC, abstractmethod

from patterns.behavioural_design_patterns.command_pattern.command_executor_factory import CommandExecutorFactory
from ..models.command import Command


class IPMode(ABC):

    def __init__(self, command_executor_factory: CommandExecutorFactory, output_printer) -> None:
        self._command_executor_factory = command_executor_factory
        self._output_printer = output_printer

    def process_command(self, command: Command):
        command_executor = self._command_executor_factory.get_command_executor(command)
        if command_executor.validate(command):
            command_executor.execute(command)
        else:
            self._output_printer.print(f"Invalid command {command.get_command()}")


    @abstractmethod
    def process(self):
        pass

    