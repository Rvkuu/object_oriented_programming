from abc import ABC, abstractmethod
import random

class BasePlayer(ABC):
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol

    @abstractmethod
    def make_move(self, board):
        pass


class HumanPlayer(BasePlayer):
    def make_move(self, board):
        while True:
            try:
                row = int(input(f"{self.name} ({self.symbol}) - Enter row (0-2): "))
                col = int(input(f"{self.name} ({self.symbol}) - Enter col (0-2): "))
                if 0 <= row <= 2 and 0 <= col <= 2:
                    return row, col
                else:
                    print("Invalid input. Try 0-2.")
            except ValueError:
                print("Invalid input. Please enter numbers.")


class AIPlayer(BasePlayer):
    def make_move(self, board):
        print(f"{self.name} ({self.symbol}) is making a move...")
        available = [(r, c) for r in range(3) for c in range(3) if board.grid[r][c] == ' ']
        return random.choice(available)

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self):
        while True:
            try:
                row = int(input(f"{self.name} ({self.symbol}), enter row (0-2): "))
                col = int(input(f"{self.name} ({self.symbol}), enter col (0-2): "))
                if 0 <= row <= 2 and 0 <= col <= 2:
                    return row, col
                else:
                    print("Invalid input. Please enter numbers between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
