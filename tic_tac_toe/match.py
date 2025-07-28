from table import Table
from player import Player

class Match:
    def __init__(self, player1: Player, player2: Player):
        # Initialize the game table and players
        self.table = Table()
        self.players = [player1, player2]
        self.current_index = 0  # Index to track whose turn it is


    def __switch_turn(self):

    def switch_turn(self):

        # Switch to the other player's turn
        self.current_index = 1 - self.current_index

    def play(self):
        # Main game loop for Tic Tac Toe
        print("Welcome to Tic Tac Toe!")
        self.table.display()

        while True:
            # Get the current player
            current_player = self.players[self.current_index]
            print(f"{current_player.name}'s turn ({current_player.symbol})")
            # Ask the player to make a move
            row, col = current_player.make_move(self.table)

            try:
                # Try to update the cell with the player's symbol
                self.table.update_cell(row, col, current_player.symbol)
            except ValueError as ve:
                # If the cell is taken, show error and let the player try again
                print(ve)
                continue

            # Display the updated table
            self.table.display()
            self.__switch_turn()

            # Check if the current player has won
            if self.table.check_winner(current_player.symbol):
                print(f"{current_player.name} wins!")
                break

            # Check if the table is full (draw)
            if self.table.is_full():
                print("It's a draw!")
                break

            # Switch to the next player's
