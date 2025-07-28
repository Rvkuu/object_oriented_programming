from player import HumanPlayer, AIPlayer
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
    print("Welcome to Tic Tac Toe")
    mode = input("Play against (1) Human or (2) AI? ").strip()

    name1 = input("Enter Player 1 name: ")
    player1 = HumanPlayer(name1, 'X')

    if mode == '1':
        name2 = input("Enter Player 2 name: ")
        player2 = HumanPlayer(name2, 'O')
    else:
        player2 = AIPlayer("Computer", 'O')

    match = Match(player1, player2)
    match.play()

if __name__ == "__main__":
    main()