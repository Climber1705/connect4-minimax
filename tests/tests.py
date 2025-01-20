
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from game import Game 

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()
    
    def testBoardInitialisation(self):
        correctBoard = [[0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.game.board.board.tolist(), correctBoard)
    
    def testValidMove(self):
        self.game.board.dropDisc(0,1)
        self.assertTrue(self.game.board.board[5][0], 1)

    def testInvalidMove(self):
        with self.assertRaises(ValueError):
            self.game.board.dropDisc(7,1)
        with self.assertRaises(ValueError):
            self.game.board.dropDisc(-1,1)

    def testRemoveMove(self):
        with self.assertRaises(ValueError):
            self.game.board.undoDisc(0)
        with self.assertRaises(ValueError):
            self.game.board.undoDisc(-1)
        with self.assertRaises(ValueError):
            self.game.board.undoDisc(7)
        self.game.board.dropDisc(0,1)
        self.game.board.undoDisc(0)
        self.assertAlmostEqual(self.game.board.board[5][0], 0)

        
    
    def testColumnFull(self):
        for i in range(6):
            self.game.board.dropDisc(0,1)
        with self.assertRaises(ValueError):
            self.game.board.dropDisc(0,1)
    
    def testVerticalWin(self):
        self.game.board.dropDisc(0,1)
        self.game.board.dropDisc(0,1)
        self.game.board.dropDisc(0,1)
        self.game.board.dropDisc(0,1)
        self.assertTrue(self.game.board.isWinner(1))
    
    def testHorizontalWin(self):
        self.game.board.dropDisc(0,1)
        self.game.board.dropDisc(1,1)
        self.game.board.dropDisc(2,1)
        self.game.board.dropDisc(3,1)
        self.assertTrue(self.game.board.isWinner(1))
    
    def testDiagonal1Win(self):
        self.game.board.dropDisc(0,1)
        self.game.board.dropDisc(1,2)
        self.game.board.dropDisc(1,1)
        self.game.board.dropDisc(2,2)
        self.game.board.dropDisc(2,2)
        self.game.board.dropDisc(2,1)
        self.game.board.dropDisc(3,2)
        self.game.board.dropDisc(3,2)
        self.game.board.dropDisc(3,2)
        self.game.board.dropDisc(3,1)
        self.assertTrue(self.game.board.isWinner(1))
    
    def testDiagonal2Win(self):
        self.game.board.dropDisc(5,1)
        self.game.board.dropDisc(4,2)
        self.game.board.dropDisc(4,1)
        self.game.board.dropDisc(3,2)
        self.game.board.dropDisc(3,2)
        self.game.board.dropDisc(3,1)
        self.game.board.dropDisc(2,2)
        self.game.board.dropDisc(2,2)
        self.game.board.dropDisc(2,2)
        self.game.board.dropDisc(2,1)
        self.assertTrue(self.game.board.isWinner(1))
    
    def testBoardFull(self):
        for i in range(6):
            for j in range(7):
                self.game.board.dropDisc(j,1)
        self.assertTrue(self.game.board.isBoardFull())

unittest.main()
