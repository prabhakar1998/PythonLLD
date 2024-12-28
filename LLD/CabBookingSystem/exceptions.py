
class RideNotStartedError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class NoTripFoundError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class DestinationNotArrived(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
class CabBusyError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class TripExistsError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class RiderNotRegistered(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)