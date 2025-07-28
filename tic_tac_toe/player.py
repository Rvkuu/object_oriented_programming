from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    @abstractmethod
    def make_move(self, table):
        pass


class HumanPlayer(Player):
    def make_move(self, table):
        while True:
            try:
                move = input(f"{self.name} ({self.symbol}), enter move as row,col (e.g., 1,2): ")
                row, col = map(int, move.strip().split(','))
                if not (0 <= row < 3 and 0 <= col < 3):
                    print("Coordinates must be between 0 and 2.")
                    continue
                if not table.is_empty(row, col):
                    print("Cell already taken.")
                    continue
                return row, col
            except Exception:
                print("Invalid input. Try again.")


class RandomAIPlayer(Player):
    def make_move(self, table):
        print(f"{self.name} ({self.symbol}) is thinking...")
        empty_cells = [(r, c) for r in range(3) for c in range(3) if table.is_empty(r, c)]
        return random.choice(empty_cells)