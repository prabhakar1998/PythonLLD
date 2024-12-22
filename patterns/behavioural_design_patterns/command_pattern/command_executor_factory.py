
from models.command import Command
from create_parking_lot_command_executor import CreateParkingLotCommandExecutor


class CommandExecutorFactory():

    def __init__(self, parking_lot_manager, output_printer) -> None:
        self._command_executor_map = {
            CreateParkingLotCommandExecutor.command_name: CreateParkingLotCommandExecutor(parking_lot_manager, output_printer)
        }
    
    def get_command_executor(self, command: Command):
        command_name = command.get_name()
        if command_name not in self._command_executor_map:
            raise ValueError(f"Unsupported command {command_name}")
    
        return self._command_executor_map[command_name]