import msvcrt
import threading
import time
from os import system
from random import randint

board = [['|' if i in [0, 20] else '-' for i in range(21)] if j in [1, 2, 3, 4, 5, 6, 7, 8, 9] else [''.join(
    '_____________________')] if j == 0 else [''.join('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')] for j in range(11)]

possible_size = 0
player = (1, 0)
locations = [player]
moveset = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}


def print_board():
    for i in range(11):
        print(''.join(board[i]))


def get_input():
    global player

    while True:
        try:
            key = msvcrt.getch().decode().lower()
            if key in moveset:
                player = moveset[key]
        except (TypeError, UnicodeDecodeError):
            pass
        except IndexError:
            print("Snake Is Dead 🐍")
            break


def generate_fruit():
    global board, possible_size

    if ''.join(str(board)).count('%') == 0:
        possible_size += 1

        x = randint(1, 9)
        y = randint(1, 19)

        if board[x][y] == '-':
            board[x][y] = '%'

    fruit_thread = threading.Thread(target=generate_fruit)
    fruit_thread.daemon = True
    fruit_thread.start()


def logs():
    print(f'|Location:{(locations[-1])}, Current_Size:{possible_size + 4}|')


def move():
    global board, player
    x = 5
    y = 10

    board[5][10] = '*'

    input_thread = threading.Thread(target=get_input)
    fruit_thread = threading.Thread(target=generate_fruit)
    fruit_thread.daemon = True
    input_thread.daemon = True
    input_thread.start()
    fruit_thread.start()

    while True:
        board[x][y] = '-'

        new_x = x + player[0]
        new_y = y + player[1]

        try:
            if 0 <= new_x < 11 and 0 <= new_y < 21 and board[new_x][new_y] != '|':
                if (new_x, new_y) in locations[1:]:
                    print("Snake Is Dead 🐍")
                    break

                x = new_x
                y = new_y

                board[x][y] = '*'

                board[0][0] = '_____________________'
                board[1][0] = '|'

                tail_length = possible_size + 4

                for idx, location in enumerate(locations):
                    if idx != 0 and idx <= tail_length:
                        board[location[0]][location[1]] = '$'

                    if idx > tail_length:
                        board[locations[0][0]][locations[0][1]] = '-'
                        locations.pop(0)

                locations.append((x, y))

            else:
                print("Snake Is Dead 🐍")
                break
        except IndexError:
            print("Snake Is Dead 🐍")
            break

        print_board()
        time.sleep(0.35)
        system('cls')
        logs()


if __name__ == "__main__":
    print_board()
    move()
