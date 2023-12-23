import msvcrt
from threading import Thread
import time
from os import system
from random import randint

board = [['-' for _ in range(30)] if i in [1, 2] else ['—' for _ in range(
    30)] if i in [3, 4] else ['=' for _ in range(30)] for i in range(5)]

movement_time = 0.25
player = (1, 3)
jump = False
cactus_position = 29
cactus_position2 = 25
dead_frames = 0

def print_board():
    system('cls')
    for i in range(5):
        print(''.join(board[i]))


def get_input():
    global jump
    while True:
        try:
            key = msvcrt.getch().decode().lower()
            if key == ' ':
                jump = True
        except UnicodeDecodeError:
            pass


def generate_obstacles():
    global cactus_position, cactus_position2, movement_time

    if cactus_position > 0:
        try:
            board[3][cactus_position2] = '&'
        except IndexError:
            cactus_position2 = 25
            
        cactus_position2 -= 1
            
        board[3][cactus_position] = '#'
        cactus_position -= 1
        time.sleep(movement_time)
        board[3][cactus_position + 1] = '—'
        board[3][cactus_position2 + 1] = '—'

        if cactus_position2 == 0:
            board[3][cactus_position2] = '—'
            cactus_position = randint(17, 22)

        if cactus_position == 0:
            board[3][cactus_position] = '—'
            cactus_position = randint(23, 28)
            
            movement_time -= 0.02 if movement_time > 0.15 else 0

            
    obstacles_thread = Thread(target=generate_obstacles)
    obstacles_thread.daemon = True
    obstacles_thread.start()


def move():
    global jump, player, dead_frames

    input_thread = Thread(target=get_input)
    input_thread.daemon = True
    input_thread.start()

    obstacles_thread = Thread(target=generate_obstacles)
    obstacles_thread.daemon = True
    obstacles_thread.start()

    board[player[0]][player[1]] = '@'

    while True:
        board[0][3] = '='

        if player[0] == 4:
            system('cls')
            print('🦖 Is Dead 😥')
            break
        
        if ''.join(str(board)).count('@') == 0:
            dead_frames += 1
            if dead_frames == 2:
                system('cls')
                print('🦖 Is Dead 😥')
                break
        else:
            dead_frames = 0
        
        if board[player[0]][player[1] + 1] == '=':
            jump = False

        if jump:
            board[player[0]][player[1]] = '-'
            player = (player[0] - 1, player[1])
            board[player[0]][player[1]] = '@'
        else:
            if board[player[0]][player[1] + 1] != '—':
                board[player[0]][player[1]] = '-'
                player = (player[0] + 1, player[1])
                board[player[0]][player[1]] = '@'

        print_board()
        time.sleep(0.2)


if __name__ == '__main__':
    print_board()
    move()
