class Option:
    def __init__(self, symbol: str):
        if symbol.upper() not in ['X', 'O']:
            raise ValueError("Symbol must be 'X' or 'O'")
        self.symbol = symbol.upper()

    def __str__(self):
        return self.symbol