
import unittest
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from board import Board
from minimax import MiniMax

"""
    The TestMinimax class.
    The class that tests the MiniMax class.
"""
class TestMinimax(unittest.TestCase):

    def setUp(self):
        self.player_disc = 1
        self.computer_disc = 2
        self.WIDTH = 7
        self.HEIGHT = 6
        self.depth = 4
        self.board = Board(np.zeros((self.HEIGHT, self.WIDTH), dtype=np.uint8), self.player_disc, self.computer_disc)
        self.minimax = MiniMax(self.player_disc, self.computer_disc)

    """
        Tests to check that the best move is chosen.
    """
    def test_minimax_best_move(self):
        self.board.drop_disc(3, 1)
        self.board.drop_disc(4, 2)
        best_move = self.minimax.mini_max(self.board, -float('inf'), float('inf'), self.depth, self.computer_disc)[0]
        self.assertIn(best_move, self.board.get_valid_moves())
    
    """
        Tests to check that the best move is chosen blocks opponent's win.
    """
    def test_block_opponent_win(self):
        for i in range(3):
            self.board.drop_disc(i, 2)
        best_move = self.minimax.mini_max(self.board, -float('inf'), float('inf'), self.depth, self.computer_disc)[0]
        self.assertEqual(best_move, 3)  # AI should block column 3
    
    """
        Tests to check that the best move is chosen to win.    
    """
    def test_choose_winning_move(self):
        for i in range(3):
            self.board.drop_disc(i, 1)
        best_move = self.minimax.mini_max(self.board, -float('inf'), float('inf'), self.depth, self.computer_disc)[0]
        self.assertEqual(best_move, 3)  # AI should win in column 3
    
    """
        Tests to check that there is no best move when the board is full.
    """
    def test_full_board(self):
        for col in range(7):
            for row in range(6):
                self.board.drop_disc(col, 1 if (row + col) % 2 == 0 else 2)
        best_move = self.minimax.mini_max(self.board, -float('inf'), float('inf'), self.depth, self.computer_disc)[0]
        self.assertIsNone(best_move)  # No valid move left

if __name__ == '__main__':
    unittest.main()