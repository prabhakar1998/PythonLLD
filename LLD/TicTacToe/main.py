


from TicTacToe.player import Player
from TicTacToe.game import Game


if __name__ == "__main__":
    player_count = 2
    game = Game(3, 3, player_count)

    for _ in range(player_count):
        while True:
            print("Enter player move name")
            try:
                move, name = input.split()
            except ValueError:
                print("Invalid input. Please enter move and name separated by space")
                continue
            player = Player(name)
            player.set_move(move)
            game.add_player(player)
            break

    while True:
        # print("Play move")
        ip = input()
        if ip == "exit":
            break

        if len(ip) == 0:
            continue
        row, col = ip.split()
        game.play_move(int(row) - 1, int(col) - 1)