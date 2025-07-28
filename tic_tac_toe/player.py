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