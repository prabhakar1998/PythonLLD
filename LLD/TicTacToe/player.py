
class Player:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def get_move(self):
        return self.move
    
    def set_move(self, move):
        self.move = move