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
    player1 = input("Enter Player 1 name: ")
    player2 = input("Enter Player 2 name: ")

    match = Match(player1, player2)
    match.play()

if __name__ == "__main__":
    main()