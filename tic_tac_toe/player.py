from abc import ABC, abstractmethod
import random

# Abstract base class for all players
class Player(ABC):
    def __init__(self, name, symbol):
        self.name = name      # Player's name
        self.symbol = symbol  # Player's symbol (e.g., 'X' or 'O')

    @abstractmethod
    # Example implementation of make_move
    # This method should be overridden by subclasses
    def make_move(self, table):
        # Example implementation
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        return (row, col)

# Human player class
class HumanPlayer(Player):
    def make_move(self, table):
        # Loop until a valid move is entered
        while True:
            try:
                # Prompt user for move input
                move = input(f"{self.name} ({self.symbol}), enter move as row,col (e.g., 1,2): ")
                row, col = map(int, move.strip().split(','))
                # Check if coordinates are within bounds
                if not (0 <= row < 3 and 0 <= col < 3):
                    print("Coordinates must be between 0 and 2.")
                    continue
                # Check if the cell is empty
                if not table.is_empty(row, col):
                    print("Cell already taken.")
                    continue
                # Return valid move
                return row, col
            except Exception:
                print("Invalid input. Try again.")

# AI player that picks a random empty cell
class RandomAIPlayer(Player):
    def make_move(self, table):
        print(f"{self.name} ({self.symbol}) is thinking...")
        # Find all empty cells
        empty_cells = [(r, c) for r in range(3) for c in range(3) if table.is_empty(r, c)]
        # Choose one randomly and return it
        return random.choice(empty_cells)