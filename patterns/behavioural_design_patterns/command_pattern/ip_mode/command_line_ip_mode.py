from ..command_executor_factory import CommandExecutorFactory
from ..models.command import Command
from ..exit_command_executor import ExitCommandExecutor
from .ip_mode import IPMode


class CommandLineInputMode(IPMode):

    def __init__(self, command_executor_factory: CommandExecutorFactory, output_printer) -> None:
        super().__init__(command_executor_factory, output_printer)

    def process(self):
        user_input = input()
        while user_input != ExitCommandExecutor.command_name:
            command = Command(user_input)
            self.process_command(command)