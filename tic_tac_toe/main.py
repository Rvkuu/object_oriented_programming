from player import HumanPlayer, RandomAIPlayer
from match import Match

# Mapping 1-9 to (row, col)
position_map = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2)
}

def main():
    print("Welcome to Tic Tac Toe!")
    print("Choose positions using numbers 1–9:")
    print("""
     1 | 2 | 3
    -----------
     4 | 5 | 6
    -----------
     7 | 8 | 9
    """)
    print("Welcome to Tic Tac Toe!")
    mode = ""
    while mode not in ("1", "2"):
        print("Select game mode:")
        print("1. Human vs Human")
        print("2. Human vs Computer")
        mode = input("Enter 1 or 2: ")

    player1_name = input("Enter Player 1 name: ")
    player1 = HumanPlayer(player1_name, 'X')

    if mode == "1":
        player2_name = input("Enter Player 2 name: ")
        player2 = HumanPlayer(player2_name, 'O')
    else:
        player2 = RandomAIPlayer("Computer", 'O')

    game = Match(player1, player2)
    game.play()

if __name__ == "__main__":
    main()
    