
from command_executor import CommandExecutor
from patterns.behavioural_design_patterns.command_pattern.models.command import Command


class ExitCommandExecutor(CommandExecutor):
    command_name = "exit"

    def __init__(self, parking_lot_mangaer, output_printer):
        super().__init__(parking_lot_mangaer, output_printer)

    def validate(self, command: Command) -> bool:
        if len(command.get_params()) != 0:
            self.output_printer.print(f"Invalid CreateParkingLot command {command.get_command()}")
            return False
        return True
    
    def execute(self, command) -> None:
        exit()