def build_board(height, width):
    return [[0 for x in range(width)] for y in range(height)]


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
    return board[coord[0]][coord[1]]


def is_overpopulated(cell_is_alive, neighbours_alive):
    return cell_is_alive and neighbours_alive > 3


def is_alone(cell_is_alive, neighbours_alive):
    return cell_is_alive and neighbours_alive < 2


def can_become_alive(current_cell_is_alive, neighbours_alive):
    return not current_cell_is_alive and neighbours_alive == 3


def should_remain_alive(current_cell_is_alive, neighbours_alive):
    return current_cell_is_alive and neighbours_alive == 2 or neighbours_alive == 3


def refresh_cell(coord, board):
    neighbours_alive = count_alive(coord, board)
    current_cell_is_alive = is_alive(coord, board)
    new_status = 0

    if is_overpopulated(current_cell_is_alive, neighbours_alive):
        new_status = 0

    if is_alone(current_cell_is_alive, neighbours_alive):
        new_status = 0

    if can_become_alive(current_cell_is_alive, neighbours_alive):
        new_status = 1

    if should_remain_alive(current_cell_is_alive, neighbours_alive):
        new_status = 1

    return new_status


def is_valid_cell(coord, board):
    return len(board) > coord[0] >= 0 and len(board[coord[0]]) > coord[1] >= 0


def generate_next_generation(board):
    next_board = build_board(width=len(board[0]), height=len(board))

    for y in range(len(board)):
        for x in range(len(board[y])):
            next_board[y][x] = refresh_cell((y, x), board)

    return next_board
