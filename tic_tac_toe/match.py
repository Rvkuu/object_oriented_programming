from board import Board
<<<<<<< HEAD
from player import BasePlayer

class Match:
    def __init__(self, player1: BasePlayer, player2: BasePlayer):
        self.board = Board()
        self.players = [player1, player2]  # Ensure this is a list
        self.current_turn = 0

    def play(self):
        print("\nWelcome to Tic Tac Toe!")
=======
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
>>>>>>> 12caa94c6440af0e7f0ca3a0810510689855c33d
        self.board.display()

        while True:
            current_player = self.players[self.current_turn]
<<<<<<< HEAD
            row, col = current_player.make_move(self.board)
=======
            row, col = current_player.make_move()
>>>>>>> 12caa94c6440af0e7f0ca3a0810510689855c33d

            if not self.board.update_cell(row, col, current_player.symbol):
                print("Cell already taken. Try again.")
                continue

            self.board.display()

            if self.board.check_winner(current_player.symbol):
<<<<<<< HEAD
                print(f"{current_player.name} wins!")
=======
                print(f"{current_player.name} wins!")
>>>>>>> 12caa94c6440af0e7f0ca3a0810510689855c33d
                break

            if self.board.is_full():
                print("It's a draw!")
                break

            self.current_turn = 1 - self.current_turn
<<<<<<< HEAD
=======
        print("Game over!")
>>>>>>> 12caa94c6440af0e7f0ca3a0810510689855c33d
