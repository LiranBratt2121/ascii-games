board = [['-' for _ in range(7)] for _ in range(6)]


def print_board() -> None:
    for i in range(6):
        for j in range(7):
            print(board[i][j], end=" ")
        print()
    print('=============')


def play(location: int, player: str) -> bool:
    global board

    try:
        location = int(location)
    except ValueError:
        print("Invalid location. %s, Please enter a number between 0 and 6." % player)
        print_board()

        return False

    if location not in [i for i in range(0, 7)]:
        print("Invalid location. %s, Please enter a number between 0 and 6." % player)
        print_board()

        return False

    if board[0][location] != '-':
        print("Column is full. %s, Please choose another column." % player)
        print_board()

        return False

    for i in range(5, -1, -1):
        if board[i][location] == '-':
            board[i][location] = player
            break

    print_board()

    return True


def check_win(player: str) -> bool:
    # Check rows
    for i in range(6):
        for j in range(4):
            if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
                return True

    # Check columns
    for i in range(3):
        for j in range(7):
            if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player and board[i+3][j] == player:
                return True

    # Check diagonals
    for i in range(3):
        for j in range(4):
            if board[i][j] == player and board[i+1][j+1] == player and board[i+2][j+2] == player and board[i+3][j+3] == player:
                return True

    for i in range(3):
        for j in range(3, 7):
            if board[i][j] == player and board[i+1][j-1] == player and board[i+2][j-2] == player and board[i+3][j-3] == player:
                return True

    return False


def loop() -> None:
    input_msg = '=============%s please enter a number between 0 and 6=============\n'
    win_msg = '=============%s Wins!=============\n'
    turn = 0

    print('=============Starting Game=============')

    print_board()

    while True:
        if turn % 2 == 0 and not ((play(input(input_msg % 'X'), 'X'))):
            continue
        else:
            if check_win('X'):
                print(win_msg % 'X')
                break

        if turn % 2 != 0 and not ((play(input(input_msg % 'Y'), 'Y'))):
            continue
        else:
            if check_win('Y'):
                print(win_msg % 'Y')
                break

        if turn == 40:
            print('====Draw!====')
            break

        turn += 1


if __name__ == "__main__":
    loop()
