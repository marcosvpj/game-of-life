import os
import time

from game_of_life import build_board, generate_next_generation


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


def populate_board_with_example(board):
    board[5][5] = 1
    board[5][6] = 1
    board[5][7] = 1
    board[5][8] = 0
    board[5][9] = 1
    board[6][5] = 1
    board[6][6] = 0
    board[6][7] = 0
    board[6][8] = 0
    board[6][9] = 0
    board[7][5] = 0
    board[7][6] = 0
    board[7][7] = 0
    board[7][8] = 1
    board[7][9] = 1
    board[8][5] = 0
    board[8][6] = 1
    board[8][7] = 1
    board[8][8] = 0
    board[8][9] = 1
    board[9][5] = 1
    board[9][6] = 0
    board[9][7] = 1
    board[9][8] = 0
    board[9][9] = 1


if __name__ == '__main__':
    main()
