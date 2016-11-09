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
            refreshCell(coord, board)
        
        print(line)
        line = ''

    #for y in board:
    #    for x in y:
    #        refreshCell()


def countAlive(coord, board):
    alive = 0
    
    if coord[0] > 0 and coord[1] > 0 and (isAlive((coord[0]-1, coord[1]-1), board)): alive += 1
    if coord[0] > 0 and (isAlive((coord[0]-1, coord[1]), board)): alive += 1
    if coord[0] > 0 and coord[1] < len(board[coord[0]]) and (isAlive((coord[0]-1, coord[1]+1), board)): alive += 1
    
    if (isAlive((coord[0], coord[1]-1), board)): alive += 1
    if (isAlive((coord[0], coord[1]+1), board)): alive += 1
    
    if (isAlive((coord[0]+1, coord[1]-1), board)): alive += 1
    if (isAlive((coord[0]+1, coord[1]), board)): alive += 1
    if (isAlive((coord[0]+1, coord[1]+1), board)): alive += 1

    return alive


def isAlive(coord, board):
    if board[coord[0]][coord[1]] == 0:
        return False
    
    return True


def refreshCell(coord, board):
    alive = countAlive(coord, board)

    if isAlive(coord, board):
        if alive < 2 or alive > 3:
            board[coord[0]][coord[1]] = 0
    else:
        if alive == 3:
            board[coord[0]][coord[1]] = 1

    return board


if __name__ == '__main__':
    main()