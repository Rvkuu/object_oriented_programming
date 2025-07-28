class Table:
    def __init__(self):
        # Initialize a 3x3 grid with empty spaces
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        # Print the current state of the grid
        print("\n  0 1 2")
        for i, row in enumerate(self.grid):
            print(f"{i} {' '.join(row)}")
        print()

    def update_cell(self, row, col, symbol):
        # Update the cell at (row, col) with the player's symbol
        # Raise an error if the cell is already taken
        if self.grid[row][col] != ' ':
            raise ValueError("Cell is already taken.")
        self.grid[row][col] = symbol

    def is_empty(self, row, col):
        # Check if the cell at (row, col) is empty
        return self.grid[row][col] == ' '

    def is_full(self):
        # Check if the grid is full (no empty cells)
        return all(cell != ' ' for row in self.grid for cell in row)

    def check_winner(self, symbol):
        # Check all rows and columns for a win
        for i in range(3):
            if all(self.grid[i][j] == symbol for j in range(3)) or \
               all(self.grid[j][i] == symbol for j in range(3)):
                return True
        # Check both diagonals for a win
        if all(self.grid[i][i] == symbol for i in range(3)) or \
           all(self.grid[i][2 - i] == symbol for i in range(3)):
            return True
        # No winner