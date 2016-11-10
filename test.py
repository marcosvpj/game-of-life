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

        neighbours_alive = main.count_alive((1, 1), self.board)

        self.assertEqual(0, neighbours_alive)

    def testCountNeighboursCellsAliveWhen3Alive(self):
        """Given a cell with 1 alive neighbours return the 3"""
        self.board[0] = [1, 1, 0]
        self.board[1] = [0, 1, 1]
        self.board[2] = [0, 0, 0]

        neighbours_alive = main.count_alive((1, 1), self.board)

        self.assertEqual(3, neighbours_alive)

    def testIsAliveWhenAlive(self):
        """Given a board and a cell coordenate, return True when the cell is alive"""
        cell_coord = (1, 1)
        self.board[1][1] = 1

        self.assertTrue(main.is_alive(cell_coord, self.board))

    def testIsAliveWhenDead(self):
        """Given a board and a cell coordenate, return False when the cell is dead"""
        cell_coord = (1, 1)
        self.board[1][1] = 0

        self.assertFalse(main.is_alive(cell_coord, self.board))

    def testDeadWithLessThan2NeighboursAlive(self):
        self.board[0] = [1, 0, 0]
        self.board[1] = [0, 1, 0]
        self.board[2] = [0, 0, 0]

        cell_coord = (1, 1)

        board = main.refresh_cell(cell_coord, self.board)

        self.assertFalse(main.is_alive(cell_coord, board))

    def testAliveWith2NeighboursAliveKeepAlive(self):
        self.board[0] = [1, 1, 0]
        self.board[1] = [0, 1, 0]
        self.board[2] = [0, 0, 0]

        cell_coord = (1, 1)

        board = main.refresh_cell(cell_coord, self.board)

        self.assertTrue(main.is_alive(cell_coord, board))

    def testAliveWith3NeighboursAliveKeepAlive(self):
        self.board[0] = [1, 1, 0]
        self.board[1] = [0, 1, 0]
        self.board[2] = [0, 0, 1]

        cell_coord = (1, 1)

        board = main.refresh_cell(cell_coord, self.board)

        self.assertTrue(main.is_alive(cell_coord, board))

    def testAliveWithMoreThan3NeighboursAliveBecomeDead(self):
        self.board[0] = [1, 1, 1]
        self.board[1] = [0, 1, 0]
        self.board[2] = [0, 0, 1]

        cell_coord = (1, 1)

        board = main.refresh_cell(cell_coord, self.board)

        self.assertFalse(main.is_alive(cell_coord, board))

    def testDeadWith3NeighboursAliveBecomeAlive(self):
        self.board[0] = [1, 1, 0]
        self.board[1] = [0, 0, 0]
        self.board[2] = [0, 0, 1]

        cell_coord = (1, 1)

        board = main.refresh_cell(cell_coord, self.board)

        self.assertTrue(main.is_alive(cell_coord, board))


if __name__ == '__main__':
    unittest.main()
