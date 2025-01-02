""" Represents the game board grid """


class Board:

    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.empty_char = "-"
        self.played_moves = 0
        self.grid = [[self.empty_char] * col for i in range(row)]

    def validate_coords(self, row, col):
        if row >= self.row or col >= self.col:
            return False
        elif row < 0 or col < 0:
            return False
        return True

    def print(self):
        # utility function
        for row in self.grid:
            line = ""
            for cell in row:
                line += cell + " "
            print(line)

    def update_cell(self, row:int, col:int, move:str) -> bool:
        if not self.validate_coords(row, col) or self.grid[row][col] != self.empty_char:
            return False
        self.grid[row][col] = move
        self.played_moves += 1
        self.print()
        return True

    def validate_winner(self, row, col, move:str):
        # check for all cols in same row
        # check for all rows in same col
        # check diag

        wins = True
        for r in range(self.row):
            if self.grid[r][col] != move:
                wins = False
                break
        if wins:
            return True
        
        wins = True
        for c in range(self.col):
            if self.grid[row][c] != move:
                wins = False
                break
        if wins:
            return True
        
        return self.diagonal_wins(move)

    def diagonal_wins(self, val):
        row, col = 0,0

        wins = True
        while row < self.row and col < self.col:
            if self.grid[row][col] != val:
                wins = False
                break
            row += 1
            col += 1

        if wins:
            return True
        row, col = 0, self.col-1
        wins = True
        while col >= 0 and row < self.row:
            if self.grid[row][col] != val:
                wins = False
                break
            row += 1
            col -= 1
        return wins

    def can_continue(self) -> bool:
        return self.played_moves < (self.row * self.col)