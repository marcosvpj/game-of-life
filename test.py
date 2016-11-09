import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        w, h = 3, 3

        self.board = [[0 for x in range(w)] for y in range(h)]
        self.board[0] = [0, 0, 0]
        self.board[1] = [0, 0, 0]
        self.board[2] = [0, 0, 0]


    def testTitleReturnGameOfLife(self):
        self.assertEqual('Game of Life', main.title())


    def testCountNeighboursCellsAliveWhen0Alive(self):
        """Given a cell with no alive neighbours return the 0""" 
        self.board[0] = [0, 0, 0]
        self.board[1] = [0, 1, 0]
        self.board[2] = [0, 0, 0]

        neighboursAlive = main.countAlive((1,1), self.board)

        self.assertEqual(0, neighboursAlive)


    def testCountNeighboursCellsAliveWhen3Alive(self):
        """Given a cell with 1 alive neighbours return the 3""" 
        self.board[0] = [1, 1, 0]
        self.board[1] = [0, 1, 1]
        self.board[2] = [0, 0, 0]

        neighboursAlive = main.countAlive((1,1), self.board)

        self.assertEqual(3, neighboursAlive)


    def testIsAliveWhenAlive(self):
        """Given a board and a cell coordenate, return True when the cell is alive"""
        cellCoord = (1, 1)
        self.board[1][1] = 1

        self.assertTrue(main.isAlive(cellCoord, self.board))


    def testIsAliveWhenDead(self):
        """Given a board and a cell coordenate, return False when the cell is dead""" 
        cellCoord = (1, 1)
        self.board[1][1] = 0

        self.assertFalse(main.isAlive(cellCoord, self.board))


    def testDeadWithLessThan2NeighboursAlive(self):
        self.board[0] = [1, 0, 0]
        self.board[1] = [0, 1, 0]
        self.board[2] = [0, 0, 0]

        cellCoord = (1, 1)

        board = main.refreshCell(cellCoord, self.board)

        self.assertFalse(main.isAlive(cellCoord, board))


    def testAliveWith2NeighboursAliveKeepAlive(self):
        self.board[0] = [1, 1, 0]
        self.board[1] = [0, 1, 0]
        self.board[2] = [0, 0, 0]

        cellCoord = (1, 1)

        board = main.refreshCell(cellCoord, self.board)

        self.assertTrue(main.isAlive(cellCoord, board))


    def testAliveWith3NeighboursAliveKeepAlive(self):
        self.board[0] = [1, 1, 0]
        self.board[1] = [0, 1, 0]
        self.board[2] = [0, 0, 1]

        cellCoord = (1, 1)

        board = main.refreshCell(cellCoord, self.board)

        self.assertTrue(main.isAlive(cellCoord, board))


    def testAliveWithMoreThan3NeighboursAliveBecomeDead(self):
        self.board[0] = [1, 1, 1]
        self.board[1] = [0, 1, 0]
        self.board[2] = [0, 0, 1]

        cellCoord = (1, 1)

        board = main.refreshCell(cellCoord, self.board)

        self.assertFalse(main.isAlive(cellCoord, board))


    def testDeadWith3NeighboursAliveBecomeAlive(self):
        self.board[0] = [1, 1, 0]
        self.board[1] = [0, 0, 0]
        self.board[2] = [0, 0, 1]

        cellCoord = (1, 1)

        board = main.refreshCell(cellCoord, self.board)

        self.assertTrue(main.isAlive(cellCoord, board))


if __name__ == '__main__':
    unittest.main()
