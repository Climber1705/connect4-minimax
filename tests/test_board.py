
import unittest
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from board import Board

"""
    The TestConnectFourBoard class.
    The class that tests the Board class.
"""
class TestConnectFourBoard(unittest.TestCase):
    
    def setUp(self):
        self.player_disc = 1
        self.computer_disc = 2
        self.WIDTH = 7
        self.HEIGTH = 6
        self.board = Board(np.zeros((self.HEIGTH, self.WIDTH), dtype=np.uint8), self.player_disc, self.computer_disc)

    """
        Tests to check that a valid disc is dropped in the correct position.
    """
    def test_valid_move(self):
        self.board.drop_disc(0,1)
        self.assertTrue(self.board.board[5][0], 1)

    """
        Tests to check that an invalid disc isn't dropped at all.
    """
    def test_invalid_move(self):
        # Too far to the right
        with self.assertRaises(ValueError):
            self.board.drop_disc(7,1)
        # Too far to the left
        with self.assertRaises(ValueError):
            self.board.drop_disc(-1,1)
    
    """
        Tests to check that a disc is removed from the correct position.
    """
    def test_remove_move(self):
        # Can't remove a disc that isn't there
        with self.assertRaises(ValueError):
            self.board.undo_disc(0)
        # Can't remove a disc from a column that doesn't exist (Too far to the left)
        with self.assertRaises(ValueError):
            self.board.undo_disc(-1)
        # Can't remove a disc from a column that doesn't exist (Too far to the right)
        with self.assertRaises(ValueError):
            self.board.undo_disc(7)

        self.board.drop_disc(0,1)
        self.board.undo_disc(0)
        # Checks that the disc was removed
        self.assertAlmostEqual(self.board.board[5][0], 0)

    """
        Tests to check that a column is full.
    """    
    def test_if_full_column(self):
        for _ in range(6):
            self.board.drop_disc(0,1)
        # Can't drop a disc in a full column
        with self.assertRaises(ValueError):
            self.board.drop_disc(0,1)

    """
        Tests to check that a vertical win is detected.
    """
    def test_vertical_win(self):
        self.board.drop_disc(0,1)
        self.board.drop_disc(0,1)
        self.board.drop_disc(0,1)
        self.board.drop_disc(0,1)
        self.assertTrue(self.board.is_winner(1))
    
    """
        Tests to check that a horizontal win is detected.
    """
    def test_horizontal_win(self):
        self.board.drop_disc(0,1)
        self.board.drop_disc(1,1)
        self.board.drop_disc(2,1)
        self.board.drop_disc(3,1)
        self.assertTrue(self.board.is_winner(1))

    """
        Tests to check that a positive diagonal win is detected.
    """
    def test_positive_diagonal_win(self):
        self.board.drop_disc(0,1)
        self.board.drop_disc(1,2)
        self.board.drop_disc(1,1)
        self.board.drop_disc(2,2)
        self.board.drop_disc(2,2)
        self.board.drop_disc(2,1)
        self.board.drop_disc(3,2)
        self.board.drop_disc(3,2)
        self.board.drop_disc(3,2)
        self.board.drop_disc(3,1)
        self.assertTrue(self.board.is_winner(1))
    
    """
        Tests to check that a negative diagonal win is detected.
    """
    def test_negative_diagonal_win(self):
        self.board.drop_disc(5,1)
        self.board.drop_disc(4,2)
        self.board.drop_disc(4,1)
        self.board.drop_disc(3,2)
        self.board.drop_disc(3,2)
        self.board.drop_disc(3,1)
        self.board.drop_disc(2,2)
        self.board.drop_disc(2,2)
        self.board.drop_disc(2,2)
        self.board.drop_disc(2,1)
        self.assertTrue(self.board.is_winner(1))
    
    """
        Tests to check that the board is full.
    """
    def test_full_board(self):
        for i in range(6):
            for j in range(7):
                self.board.drop_disc(j,1)
        self.assertTrue(self.board.is_board_full())

if __name__ == '__main__':
    unittest.main()