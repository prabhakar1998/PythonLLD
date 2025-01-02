from TicTacToe.board import Board
from TicTacToe.player import Player
from collections import deque


class Game:

    def __init__(self, grid_row, grid_col, players_count=2):
        self.grid_row = grid_row
        self.grid_col = grid_col
        self.players_count = players_count
        self.players = deque()
        self.board = Board(self.grid_row, self.grid_col)
        self.selected_moves = set()
        self.game_over = False

    def add_player(self, player: Player) -> bool:
        if player.get_move() in self.selected_moves:
            print(f"Player move {player.get_move()} is already selected by another player")
            return False

        if len(self.players) == self.players_count:
            print("Already max players created")
            return False

        self.players.append(player)
        self.selected_moves.add(player.get_move())
        return True
    
    def play_move(self, row, col) -> bool:
        if self.game_over:
            print("Game already concluded")
            return False
        
        player = self.players.popleft()
        self.players.append(player)

        if not self.board.update_cell(row, col, player.get_move()):
            print("Invalid Move")
            return False
        
        if self.board.validate_winner(row, col, player.get_move()):
            print(f"{player.get_name()} won the game")
            self.game_over = True
        elif not self.board.can_continue():
            print("Game ended in a draw")
            self.game_over = True

        return True
    

