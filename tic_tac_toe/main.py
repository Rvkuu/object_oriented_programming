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
    p1 = input("Enter Player 1 name (X): ")
    p2 = input("Enter Player 2 name (O): ")
    match = Match(p1, p2)

    while True:
        print(f"\n{match.current_player()}'s turn:")
        match.display_table()

        valid_move = False
        while not valid_move:
            try:
                pos = int(input("Choose a position (1–9): "))
                if pos not in position_map:
                    raise ValueError("Invalid position")
                row, col = position_map[pos]
            except ValueError:
                print("Enter a number between 1 and 9.")
                continue

            result = match.play_turn(row, col)

            if result == "Invalid move. Try another cell.":
                print("That spot is taken. Try again.")
            else:
                valid_move = True
                print(result)

        if result != "Continue":
            match.display_table()
            break

if __name__ == "__main__":
    main()