from table import Table
from player import Player

class Match:
    def __init__(self, player1: Player, player2: Player):
        self.table = Table()
        self.players = [player1, player2]
        self.current_index = 0

    def switch_turn(self):
        self.current_index = 1 - self.current_index

    def play(self):
        print("🎮 Welcome to Tic Tac Toe!")
        self.table.display()

        while True:
            current_player = self.players[self.current_index]
            print(f"{current_player.name}'s turn ({current_player.symbol})")
            row, col = current_player.make_move(self.table)

            try:
                self.table.update_cell(row, col, current_player.symbol)
            except ValueError as ve:
                print(ve)
                continue

            self.table.display()

            if self.table.check_winner(current_player.symbol):
                print(f"{current_player.name} wins!")
                break

            if self.table.is_full():
                print("It's a draw!")
                break

            self.switch_turn()
