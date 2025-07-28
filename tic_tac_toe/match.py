from board import Board
from player import Player

class Match:
    def __init__(self, player1_name, player2_name):
        self.board = Board()
        self.players = [
            Player(player1_name, 'X'),
            Player(player2_name, 'O')
        ]
        self.current_turn = 0

    def play(self):
        print("Welcome to Tic Tac Toe!")
        self.board.display()

        while True:
            current_player = self.players[self.current_turn]
            row, col = current_player.make_move()

            if not self.board.update_cell(row, col, current_player.symbol):
                print("Cell already taken. Try again.")
                continue

            self.board.display()

            if self.board.check_winner(current_player.symbol):
                print(f"🎉 {current_player.name} wins!")
                break

            if self.board.is_full():
                print("It's a draw!")
                break

            self.current_turn = 1 - self.current_turn
        print("Game over!")