def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def player_input(player, board):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0, 1, 2): "))
            col = int(input(f"Player {player}, enter column (0, 1, 2): "))
            
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Cell already taken! Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter numbers between 0 and 2.")

def check_win(board):

    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    for _ in range(9):
        display_board(board)
        player_input(players[turn], board)

        if check_win(board):
            display_board(board)
            print(f"Player {players[turn]} wins!")
            return

        turn = 1 - turn

    display_board(board)
    print("who is losing is gay as fuck")

play()
