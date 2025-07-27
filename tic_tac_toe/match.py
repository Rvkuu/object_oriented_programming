from table import Table
from player import HumanPlayer

class Match:
    def __init__(self, player1_name: str, player2_name: str):
        self.table = Table()
        self.players = [
            HumanPlayer(player1_name, 'X'),
            HumanPlayer(player2_name, 'O')
        ]
        self.current_turn = 0  # 0 or 1

    def switch_turn(self):
        self.current_turn = 1 - self.current_turn

    def play_turn(self, row: int, col: int) -> str:
        player = self.players[self.current_turn]
        symbol = player.get_symbol()

        if self.table.set_cell(row, col, symbol):
            if self.table.check_winner(symbol):
                return f"{player.get_name()} wins!"
            elif self.table.is_full():
                return "It's a draw!"
            else:
                self.switch_turn()
                return "Continue"
        else:
            return "Invalid move. Try another cell."

    def display_table(self):
        self.table.display()

    def current_player(self) -> str:
        return self.players[self.current_turn].get_name()
