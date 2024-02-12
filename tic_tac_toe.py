board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


# following function to display the current state of the board:
def display_board():
    for row in board:
        print('|'.join(row))


# This function takes player input and update the board. Ensure the input is valid
def get_player_input():
    row = int(input("Enter the row (0, 1, 2): "))
    col = int(input("Enter the column (0, 1, 2): "))
    return row, col

# This functions checks if there is a winner after each move, considering rows, columns and diagonals.
def check_winner(board):
    # Check rows, columns, and diagonals
    # Return 'X' if Player X wins, 'O' if Player O wins, or None if no winner yet


def main():

    # Create a loop that alternates between players two players.
    # maybe also have a game starting page where players enter their name

    return 0


if __name__ == "__main__":
    main()
