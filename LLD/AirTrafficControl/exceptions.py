

class NoRunwayAllotedError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class RunwayIsOccupiedError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    
class RunwayNotInIdleRunwaysError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args) 