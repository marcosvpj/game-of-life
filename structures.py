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


def place_acorn(board, position):
    offset_x = position[0]
    offset_y = position[1]
    width = 9 + offset_x
    height = 5 + offset_y

    for y in range(height):
        for x in range(width):
            board[y][x] = 0

    board[1 + offset_y][2 + offset_x] = 1
    board[2 + offset_y][4 + offset_x] = 1
    board[3 + offset_y][1 + offset_x] = 1
    board[3 + offset_y][2 + offset_x] = 1
    board[3 + offset_y][5 + offset_x] = 1
    board[3 + offset_y][6 + offset_x] = 1
    board[3 + offset_y][7 + offset_x] = 1


def place_glider(board, position):
    offset_x = position[0]
    offset_y = position[1]
    width = 5 + offset_x
    height = 5 + offset_y

    for y in range(height):
        for x in range(width):
            board[y][x] = 0

    board[1 + offset_y][2 + offset_x] = 1
    board[2 + offset_y][3 + offset_x] = 1
    board[3 + offset_y][1 + offset_x] = 1
    board[3 + offset_y][2 + offset_x] = 1
    board[3 + offset_y][3 + offset_x] = 1


def place_die_hard(board, position):
    offset_x = position[0]
    offset_y = position[1]
    width = 9 + offset_x
    height = 5 + offset_y

    for y in range(height):
        for x in range(width):
            board[y][x] = 0

    board[1 + offset_y][1 + offset_x] = 1
    board[1 + offset_y][2 + offset_x] = 1
    board[1 + offset_y][6 + offset_x] = 1
    board[1 + offset_y][8 + offset_x] = 1

    board[2 + offset_y][1 + offset_x] = 1
    board[2 + offset_y][2 + offset_x] = 1
    board[2 + offset_y][7 + offset_x] = 1

    board[3 + offset_y][7 + offset_x] = 1
