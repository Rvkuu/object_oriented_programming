class Renderer:
    """Abstract rendering interface"""
    def show_message(self, message):
        raise NotImplementedError

    def render_board(self, board):
        raise NotImplementedError


class ConsoleRenderer(Renderer):
    """Console-based rendering"""
    def show_message(self, message):
        print(message)

    def render_board(self, board):
        print("\n  " + " ".join(str(i) for i in range(board.size)))
        for i, row in enumerate(board.grid):
            print(f"{i} " + " ".join(row))
        print()
