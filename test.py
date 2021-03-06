import unittest

import game_of_life


class TestMain(unittest.TestCase):
    def setUp(self):
        self.board = game_of_life.build_board(3, 3)

        self.board[0] = [0, 0, 0]
        self.board[1] = [0, 0, 0]
        self.board[2] = [0, 0, 0]

    def testCountAlive(self):
        self.board = game_of_life.build_board(4, 3)
        self.board[0] = [1, 1, 0, 1, 1, 0]
        self.board[1] = [0, 0, 1, 1, 1, 0]
        self.board[2] = [0, 0, 0, 0, 1, 0]
        self.board[3] = [0, 0, 0, 0, 0, 0]

        data = [
            {'expect': 0, 'position': (2, 0)},
            {'expect': 1, 'position': (0, 0)},
            {'expect': 2, 'position': (2, 2)},
            {'expect': 3, 'position': (1, 1)},
            {'expect': 4, 'position': (0, 2)},
        ]

        for d in data:
            with self.subTest():
                self.assertEqual(d['expect'], game_of_life.count_alive(d['position'], self.board))

    def testIsAliveWhenAlive(self):
        self.board[0] = [1, 0, 0]
        self.board[1] = [0, 1, 0]
        self.board[2] = [0, 0, 0]

        data = [
            {'pos': (1, 1), 'expected': True},
            {'pos': (2, 2), 'expected': False}
        ]

        for d in data:
            with self.subTest():
                self.assertEqual(d['expected'], game_of_life.is_alive(d['pos'], self.board))

    def testRefreshCell(self):
        self.board[0] = [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1]
        self.board[1] = [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
        self.board[2] = [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1]

        data = [
            {'pos': (1, 1), 'expected': 0},
            {'pos': (1, 3), 'expected': 0},
            {'pos': (1, 5), 'expected': 1},
            {'pos': (1, 7), 'expected': 1},
            {'pos': (1, 11), 'expected': 1},
            {'pos': (1, 14), 'expected': 0}
        ]

        for d in data:
            with self.subTest():
                new_cell_value = game_of_life.refresh_cell(d['pos'], self.board)
                self.assertEqual(d['expected'], new_cell_value)

    def testDeadWithLessThan2NeighboursAlive(self):
        self.board[0] = [1, 0, 0]
        self.board[1] = [0, 1, 0]
        self.board[2] = [0, 0, 0]

        cell_coord = (1, 1)

        self.board[cell_coord[0]][cell_coord[1]] = game_of_life.refresh_cell(cell_coord, self.board)

        self.assertFalse(game_of_life.is_alive(cell_coord, self.board))

    def testAliveWith2NeighboursAliveKeepAlive(self):
        self.board[0] = [1, 1, 0]
        self.board[1] = [0, 1, 0]
        self.board[2] = [0, 0, 0]

        cell_coord = (1, 1)

        self.board[cell_coord[0]][cell_coord[1]] = game_of_life.refresh_cell(cell_coord, self.board)

        self.assertTrue(game_of_life.is_alive(cell_coord, self.board))

    def testAliveWith3NeighboursAliveKeepAlive(self):
        self.board[0] = [1, 1, 0]
        self.board[1] = [0, 1, 0]
        self.board[2] = [0, 0, 1]

        cell_coord = (1, 1)

        self.board[cell_coord[0]][cell_coord[1]] = game_of_life.refresh_cell(cell_coord, self.board)

        self.assertTrue(game_of_life.is_alive(cell_coord, self.board))

    def testAliveWithMoreThan3NeighboursAliveBecomeDead(self):
        self.board[0] = [1, 1, 1]
        self.board[1] = [0, 1, 0]
        self.board[2] = [0, 0, 1]

        cell_coord = (1, 1)

        self.board[cell_coord[0]][cell_coord[1]] = game_of_life.refresh_cell(cell_coord, self.board)

        self.assertFalse(game_of_life.is_alive(cell_coord, self.board))

    def testDeadWith3NeighboursAliveBecomeAlive(self):
        self.board[0] = [1, 1, 0]
        self.board[1] = [0, 0, 0]
        self.board[2] = [0, 0, 1]

        cell_coord = (1, 1)

        self.board[cell_coord[0]][cell_coord[1]] = game_of_life.refresh_cell(cell_coord, self.board)

        self.assertTrue(game_of_life.is_alive(cell_coord, self.board))

    def testRefreshBoard(self):
        step1 = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]

        step2 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        next_step = game_of_life.generate_next_generation(step1)
        self.assertEqual(next_step, step2)

    def testRefreshBoard2(self):
        step1 = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0]
        ]

        step2 = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0]
        ]

        next_step = game_of_life.generate_next_generation(step1)
        self.assertEqual(next_step, step2)

    def testRefreshBoard4(self):
        step1 = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]

        step2 = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]
        ]

        next_step = game_of_life.generate_next_generation(step1)
        self.assertEqual(next_step, step2)

    def testCountAliveWithBoardContinuityUpDown(self):
        self.board = [[0, 1, 0],
                      [0, 0, 0],
                      [0, 1, 0]]

        self.assertEqual(game_of_life.count_alive((0, 1), self.board), 1)
        self.assertEqual(game_of_life.count_alive((0, 2), self.board), 2)
        self.assertEqual(game_of_life.count_alive((0, 0), self.board), 2)

    def testCountAliveWithBoardContinuityLeftRight(self):
        self.board = [[1, 0, 0],
                      [0, 0, 0],
                      [0, 0, 1]]

        self.assertEqual(game_of_life.count_alive((0, 0), self.board), 1)
        self.assertEqual(game_of_life.count_alive((1, 0), self.board), 2)
        self.assertEqual(game_of_life.count_alive((2, 0), self.board), 2)

    def testCountAliveWithBoardContinuityCorners(self):
        self.board = [[1, 0, 1],
                      [0, 0, 0],
                      [1, 0, 1]]

        self.assertEqual(game_of_life.count_alive((0, 0), self.board), 3)
        self.assertEqual(game_of_life.count_alive((2, 0), self.board), 3)
        self.assertEqual(game_of_life.count_alive((2, 0), self.board), 3)
        self.assertEqual(game_of_life.count_alive((2, 2), self.board), 3)


if __name__ == '__main__':
    unittest.main()
