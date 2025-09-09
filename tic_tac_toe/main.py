from player import HumanPlayer, RandomAIPlayer
from match import Match
from board import Board
from renderer import ConsoleRenderer
from input_handler import ConsoleInputHandler

# --- Main game setup ---
def main():
    renderer = ConsoleRenderer()
    input_handler = ConsoleInputHandler()

    renderer.show_message("Welcome to Tic Tac Toe!")

    # --- Choose board size ---
    size = 0
    while size < 3:
        try:
            size = int(input_handler.get_input("Enter board size (minimum 3): "))
            if size < 3:
                renderer.show_message("Board size must be at least 3.")
        except ValueError:
            renderer.show_message("Please enter a valid number.")

    # --- Show sample layout (only for 3x3, otherwise generic message) ---
    if size == 3:
        renderer.show_message("Choose positions using numbers 1–9:")
        renderer.show_message("""
         1 | 2 | 3
        -----------
         4 | 5 | 6
        -----------
         7 | 8 | 9
        """)
    else:
        renderer.show_message(f"You selected a {size}x{size} board.")

    # --- Choose game mode ---
    mode = ""
    while mode not in ("1", "2"):
        renderer.show_message("Select game mode:")
        renderer.show_message("1. Human vs Human")
        renderer.show_message("2. Human vs Computer")
        mode = input_handler.get_input("Enter 1 or 2: ")

    # --- Player 1 ---
    player1_name = input_handler.get_input("Enter Player 1 name: ")
    player1 = HumanPlayer(player1_name, 'X', input_handler)

    # --- Player 2 ---
    if mode == "1":
        player2_name = input_handler.get_input("Enter Player 2 name: ")
        player2 = HumanPlayer(player2_name, 'O', input_handler)
    else:
        player2 = RandomAIPlayer("Computer", 'O')

    # --- Start match ---
    board = Board(size=size)
    game = Match(board, player1, player2, renderer)
    game.play()


if __name__ == "__main__":
    main()
    