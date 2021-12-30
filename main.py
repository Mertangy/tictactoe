"""This is a simple two player Tic tac toe game."""

# initialise global variables
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
game_still_on = True
user = True


# Function definations
def show_board(board):
    """This function simple displays the game board to the user."""
    for row in board:
        for item in row:
            print(item, end=" ")
        print("")


def spot_taken(board, coord):
    """Returns True if the spot entered by user has already been played,False otherwise."""
    row = coord[0]
    col = coord[1]

    if board[row][col] != '-':
        print("Already taken!")
        return True
    return False


def get_coordinates(user_input):
    """This functions translates the choice made by the user to coordinates by returning a tuple."""
    row = user_input // 3
    col = user_input
    if col > 2:
        col = int(col % 3)
    return (row, col)


def add_to_board(board, coord, user):
    """This functions marks the user's choice on the board."""
    row = coord[0]
    col = coord[1]
    board[row][col] = user


def check_rows(player, board):
    """Checks through all rows for a possible win.Returns True if win False otherwise."""
    for row in board:
        win = True
        for item in row:
            if item != player:
                win = False
                break
        if win:
            return True
    return False


def check_columns(player, board):
    """Checks through all columns for a possible win.Returns True if win,False otherwise."""
    for col in range(3):
        win = True
        for row in range(3):
            if board[row][col] != player:
                win = False
                break
        if win:
            return True
    return False


def check_diagonals(player, board):
    """Checks through all diagnals for a possible win.Returns True if win False otherwise."""
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    else:
        return False


def is_player_win(board, player):
    """Checks for a win.Returns True if win False otherwise."""
    if check_rows(board, player): return True
    if check_columns(board, player): return True
    if check_diagonals(board, player): return True

    return False


def is_board_filled(board):
    """Returns True if board is filled by user choices,False otherwise"""
    for row in board:
        for item in row:
            if item == '-':
                return False
    return True


def current_user(user):
    """Swap users between a 'X' and 'O' """
    if user:
        return 'X'
    else:
        return 'O'


# main game entry point
while game_still_on:
    player = current_user(user)
    print(f"Player {player} turn")
    show_board(board)
    user_input = input("Please enter a position using 1 - 9 or 'q' to quit game: ")
    if user_input.lower() == 'q':
        print("Thank you for playing.")
        break
    if not user_input.isnumeric():
        print("This is not a valid number.Please try again: ")
        continue
    if int(user_input) > 9 or int(user_input) < 1:
        print("This number is out of bounds.Please try again")
        continue
    user_input = int(user_input) - 1
    coord = get_coordinates(user_input)
    if spot_taken(board, coord):
        print("Try again")
        continue

    add_to_board(board, coord, player)
    if is_player_win(player, board):
        print(f"{player} has won!")
        break

    if is_board_filled(board):
        print("Its Draw!")

    user = not user
