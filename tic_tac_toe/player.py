from option import Option

class Player:
    def __int__(self, name: str, symbol: str):
        self.name = name
        self.option = Option(symbol=symbol)

    def get_symbol(self) -> str:
        return str(self.option)
    
    def get_name(self) -> str:
        return self.name
    
class HumanPlayer(Player):
    # Placeholder for human player specific methods if needed
    pass