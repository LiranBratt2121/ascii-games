board = [['+' if i in [0, 4] else '=' for i in range(5)] if j in [0, 4] else [
    '|' if k in [0, 4] else '-' for k in range(5)] for j in range(5)]


def print_board():
    for i in range(5):
        print(''.join(board[i]))


def check_win(player: str) -> bool:
    for i in range(1, 4):
        # Check horizon
        if board[i][1] == board[i][2] == board[i][3] == player:
            return True

        # Check vertical
        if board[1][i] == board[2][i] == board[3][i] == player:
            return True

        # check diagonal
        if board[1][1] == board[2][2] == board[3][3] == player:
            return True
        if board[1][3] == board[2][2] == board[3][1] == player:
            return True

        return False


def place(player: str, location: str) -> bool:
    error_msg = 'Invalid location! %s please place only numbers between 1-3 [X, Y]' % player

    try:
        x, y = location.strip().split(',')
        x, y = int(x), int(y)
    except Exception:
        print(error_msg)
        print_board()
        return False

    if x < 1 or x > 3 or y < 1 or y > 3:
        print(error_msg)
        print_board()
        return False

    if board[x][y] == '-':
        board[x][y] = player
        print_board()
        return True

    print(error_msg)
    print_board()
    return False


def loop() -> None:
    input_msg = '=============%s please enter a number between 1 and 3 choose location like this X, Y=============\n'
    win_msg = '=============%s Wins!=============\n'
    turn = 0

    print('=============Starting Game=============')
    print_board()

    while True:
        if turn % 2 == 0 and not place('X', input(input_msg % 'X')):
            continue
        else:
            if check_win('X'):
                print(win_msg % 'X')
                break

        if turn % 2 == 1 and not place('Y', input(input_msg % 'Y')):
            continue
        else:
            if check_win('Y'):
                print(win_msg % 'Y')
                break

        turn += 1

        if turn == 9:
            print('=============Draw!=============')
            break


if __name__ == '__main__':
    loop()
