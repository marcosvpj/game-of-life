import os
import time

from game_of_life import build_board, generate_next_generation
from structures import populate_board_with_example


def main():
    board = build_board(width=100, height=25)
    populate_board_with_example(board)

    while True:
        draw_board_on_console(board)
        board = generate_next_generation(board)


def draw_board_on_console(board):
    os.system('cls')

    for y in range(len(board)):
        line = ''

        for x in range(len(board[y])):
            if board[y][x] == 0:
                line += ' '
            else:
                line += '.'

        print(line)

    time.sleep(.6)


if __name__ == '__main__':
    main()
