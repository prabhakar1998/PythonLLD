class House:

    def __init__(self):
        self.roof = None
        self.doors = None
        self.windows = None
        self.walls = None
        self.rooms = None
        self.garden = None
        self.swimming_pool = None

class HouseBuilder:

    def __init__(self):
        self.house = House()

    def add_roof(self, roof_type):
        self.house.roof = roof_type
        return self
    
    def add_doors(self, doors):
        self.house.doors = doors
        return self

    def add_windows(self, windows):
        self.house.windows = windows
        return self

    def add_walls(self, walls):
        self.house.walls = walls
        return self

    def add_room(self, rooms):
        self.house.rooms= rooms
        return self
    
    def add_garden(self, garden):
        self.house.garden = garden
        return self

    def add_swimming_pool(self, swimming_pool):
        self.house.swimming_pool = swimming_pool
        return self

    def build(self):
        return self.house