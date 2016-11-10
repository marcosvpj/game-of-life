def title():
    return 'Game of Life'


def main():
    print(title())
    board = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
    line = ''

    for n in range(10):
        board2 = board
        for y in range(len(board)):
            for x in range(len(board[y])):
                line += str(board[y][x])
                coord = (y, x)
                board2[y][x] = refresh_cell(coord, board)

            print(line)
            line = ''
        print('')

        board = board2

        # for y in board:
        #    for x in y:
        #        refreshCell()


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
