class Board:
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        print("\n  0   1   2")
        for idx, row in enumerate(self.grid):
            print(f"{idx} " + " | ".join(row))
            if idx < 2:
                print("  ---------")

    def update_cell(self, row, col, symbol):
        if self.grid[row][col] == ' ':
            self.grid[row][col] = symbol
            return True
        return False

    def is_full(self):
        return all(cell != ' ' for row in self.grid for cell in row)

    def check_winner(self, symbol):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.grid[i][j] == symbol for j in range(3)) or \
               all(self.grid[j][i] == symbol for j in range(3)):
                return True
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == symbol or \
           self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == symbol:
            return True
        return False