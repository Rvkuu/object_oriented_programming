# board.py
class Board:
    def __init__(self, size=3):
        self.size = size
        self.grid = [[" " for _ in range(size)] for _ in range(size)]

    def update_cell(self, row, col, symbol):
        if not self.is_empty(row, col):
            raise ValueError("Cell already taken.")
        self.grid[row][col] = symbol

    def is_empty(self, row, col):
        return self.grid[row][col] == " "

    def is_full(self):
        return all(cell != " " for row in self.grid for cell in row)

    def check_winner(self, symbol):
        # Row/col check
        for i in range(self.size):
            if all(self.grid[i][j] == symbol for j in range(self.size)) or \
               all(self.grid[j][i] == symbol for j in range(self.size)):
                return True
        # Diagonal check
        if all(self.grid[i][i] == symbol for i in range(self.size)) or \
           all(self.grid[i][self.size - i - 1] == symbol for i in range(self.size)):
            return True
        return False
