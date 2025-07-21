class Table:
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.grid:
            print(" | ".join(row))
            print("-" * 9)

    def set_cell(self, row: int, col: int, symbol: str) -> bool:
        if self.grid[row][col] == ' ':
            self.grid[row][col] = symbol
            return True
        return False

    def is_full(self) -> bool:
        return all(cell != ' ' for row in self.grid for cell in row)

    def check_winner(self, symbol: str) -> bool:
        for i in range(3):
            if all(self.grid[i][j] == symbol for j in range(3)) or                all(self.grid[j][i] == symbol for j in range(3)):
                return True
        if all(self.grid[i][i] == symbol for i in range(3)) or            all(self.grid[i][2 - i] == symbol for i in range(3)):
            return True
        return False