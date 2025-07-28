class Table:
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        print("\n  0 1 2")
        for i, row in enumerate(self.grid):
            print(f"{i} {' '.join(row)}")
        print()

    def update_cell(self, row, col, symbol):
        if self.grid[row][col] != ' ':
            raise ValueError("Cell is already taken.")
        self.grid[row][col] = symbol

    def is_empty(self, row, col):
        return self.grid[row][col] == ' '

    def is_full(self):
        return all(cell != ' ' for row in self.grid for cell in row)

    def check_winner(self, symbol):
        # Rows & columns
        for i in range(3):
            if all(self.grid[i][j] == symbol for j in range(3)) or \
               all(self.grid[j][i] == symbol for j in range(3)):
                return True
        # Diagonals
        if all(self.grid[i][i] == symbol for i in range(3)) or \
           all(self.grid[i][2 - i] == symbol for i in range(3)):
            return True
        return False
