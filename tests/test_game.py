
import unittest
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from game import Game

"""
    The TestConnectFourGame class.
    The class that tests the Game class.
"""
class TestConnectFourGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    """
        Tests to check that the turns alternate between the player and the computer.
    """
    def test_alternating_turns(self):
        current_disc = 1
        new_disc = self.game.change_disc(current_disc)
        self.assertEqual(new_disc, 2)

    """
        Tests to check that the game ends when a player wins.
    """
    def test_game_end_on_win(self):
        for i in range(3):
            self.game.board.drop_disc(i, 1)
        self.game.board.drop_disc(3, 1)
        self.assertTrue(self.game.board.is_winner(1))
    
    """
        Tests to check that the game ends in a tie.
    """
    def test_draw_detection(self):
        for i in range(6):
            for j in range(7):
                self.game.board.drop_disc(j,1)
        self.assertTrue(self.game.board.is_board_full())

if __name__ == '__main__':
    unittest.main()