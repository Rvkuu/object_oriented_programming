class Match:
    def __init__(self, board, player1, player2, renderer):
        self.board = board
        self.players = [player1, player2]
        self.current_index = 0
        self.renderer = renderer

    def __switch_turn(self):
        self.current_index = 1 - self.current_index

    def play(self):
        self.renderer.show_message("Starting match...")
        self.renderer.render_board(self.board)

        while True:
            current_player = self.players[self.current_index]
            self.renderer.show_message(f"{current_player.name}'s turn ({current_player.symbol})")

            row, col = current_player.make_move(self.board)

            try:
                self.board.update_cell(row, col, current_player.symbol)
            except ValueError as e:
                self.renderer.show_message(str(e))
                continue

            self.renderer.render_board(self.board)

            if self.board.check_winner(current_player.symbol):
                self.renderer.show_message(f"{current_player.name} wins!")
                break

            if self.board.is_full():
                self.renderer.show_message("It's a draw!")
                break

            self.__switch_turn()
