from option import Option

class Player:
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.option = Option(symbol)

    def get_symbol(self) -> str:
        return str(self.option)

    def get_name(self) -> str:
        return self.name

class HumanPlayer(Player):
    # Placeholder for future extension like input gathering
    pass
