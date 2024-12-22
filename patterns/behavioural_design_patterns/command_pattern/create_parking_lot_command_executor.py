
from command_executor import CommandExecutor
from patterns.behavioural_design_patterns.command_pattern.models.command import Command


class CreateParkingLotCommandExecutor(CommandExecutor):
    command_name = "create_parking_lot"

    def __init__(self, parking_lot_mangaer, output_printer):
        super().__init__(parking_lot_mangaer, output_printer)

    def validate(self, command: Command) -> bool:
        if len(command.get_params()) != 1:
            self.output_printer.print(f"Invalid CreateParkingLot command {command.get_command()}")
            return False
        return True
    
    def execute(self, command) -> None:
        args = command.get_params()
        parking_lot_capacity = args[1]
        self.parking_lot_manager.create_parking_lot(parking_lot_capacity)
        self.output_printer.print("Parking lot is created")