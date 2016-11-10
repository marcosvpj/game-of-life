def title():
    return 'Game of Life'


def main():
    print(title())
    board = [
        [0,0,0],
        [1,1,1],
        [0,0,0]
    ]
    line = ''

    #while 1 == 1:
    for y in range(len(board)):
        for x in range(len(board[y])):
            line = line + str(board[y][x])
            coord = (y, x)
            refresh_cell(coord, board)
        
        print(line)
        line = ''

    #for y in board:
    #    for x in y:
    #        refreshCell()


def count_alive(coord, board):
    alive = 0
    
    if coord[0] > 0 and coord[1] > 0 and (is_alive((coord[0]-1, coord[1]-1), board)): alive += 1
    if coord[0] > 0 and (is_alive((coord[0]-1, coord[1]), board)): alive += 1
    if coord[0] > 0 and coord[1] < len(board[coord[0]]) and (is_alive((coord[0]-1, coord[1]+1), board)): alive += 1
    
    if is_alive((coord[0], coord[1]-1), board): alive += 1
    if is_alive((coord[0], coord[1]+1), board): alive += 1
    
    if is_alive((coord[0]+1, coord[1]-1), board): alive += 1
    if is_alive((coord[0]+1, coord[1]), board): alive += 1
    if is_alive((coord[0]+1, coord[1]+1), board): alive += 1

    return alive


def is_alive(coord, board):
    if board[coord[0]][coord[1]] == 0:
        return False
    
    return True


def refresh_cell(coord, board):
    alive = count_alive(coord, board)

    if is_alive(coord, board):
        if alive < 2 or alive > 3:
            board[coord[0]][coord[1]] = 0
    else:
        if alive == 3:
            board[coord[0]][coord[1]] = 1

    return board


if __name__ == '__main__':
    main()