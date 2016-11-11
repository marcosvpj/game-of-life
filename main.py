def title():
    return 'Game of Life'


def main():
    import os
    import time
    print(title())
    board = [[0 for x in range(100)] for y in range(25)]
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

    line = ''

    while True:
        os.system('clear')
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == 0:
                    line += ' '
                else:
                    line += '.'

            print(line)
            line = ''

        time.sleep(.6)
        board = refresh_board(board)


def count_alive(coord, board):
    alive = 0

    pos = [
        (coord[0], coord[1] - 1),
        (coord[0], coord[1] + 1),
        (coord[0] - 1, coord[1]),
        (coord[0] - 1, coord[1] - 1),
        (coord[0] - 1, coord[1] + 1),
        (coord[0] + 1, coord[1]),
        (coord[0] + 1, coord[1] - 1),
        (coord[0] + 1, coord[1] + 1)
    ]

    for p in pos:
        if is_valid_cell(p, board) and (is_alive(p, board)):
            alive += 1

    return alive


def is_alive(coord, board):
    if board[coord[0]][coord[1]] == 0:
        return False

    return True


def refresh_cell(coord, board):
    alive = count_alive(coord, board)

    if is_alive(coord, board):
        if alive == 2 or alive == 3:
            return 1
    else:
        if alive == 3:
            return 1

    return 0


def is_valid_cell(coord, board):
    if coord[0] >= len(board):
        return False

    if coord[0] < 0:
        return False

    if coord[1] < 0:
        return False

    if coord[1] >= len(board[coord[0]]):
        return False

    return True


def refresh_board(board):
    next_board = [[0 for x in range(len(board[0]))] for y in range(len(board))]
    for y in range(len(board)):
        for x in range(len(board[y])):
            coord = (y, x)
            next_board[y][x] = refresh_cell(coord, board)

    return next_board


if __name__ == '__main__':
    main()
