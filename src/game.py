
import numpy as np

from board import Board
from minimax import MiniMax
from random import randint

"""
    The Game class
    The class that represents the game
"""

class Game:

    """
        Attributes of the Game class
    """

    WIDTH : int = 7
    HEIGTH : int = 6
    #Max depth of the search of 6 or take some time to compute
    SEARCH_DEPTH : int = 6

    board: Board
    playersDisc: int
    computerDisc: int
    miniMax: MiniMax

    """
        Constructor of the Game class
    """

    def __init__(self):
        self.playersDisc = 1
        self.computerDisc = 2

        self.board = Board(np.zeros((self.HEIGTH, self.WIDTH), dtype=np.uint8), self.playersDisc, self.computerDisc)
        self.miniMax = MiniMax(self.playersDisc, self.computerDisc)


    def getStartingDisc(self):
        if randint(0, 1) == 0:
            return self.playersDisc
        return self.computerDisc

    """
        Gets the player's input
    """

    def getPlayerInput(self):
        while True:
            playerInput = input("Enter a column number: ")
            if not playerInput.isdigit():
                print("Invalid input. Please enter a number.")
                continue
            if int(playerInput) < 0 or int(playerInput) > 6:
                print("Invalid input. Please enter a number between 0 and 6.")
                continue
            if not self.board.isValidMove(int(playerInput)):
                print("Invalid input. Please enter a number for a column that is not full.")
                continue
            print("Player's move: ", playerInput)
            return int(playerInput)

    """
        Gets the computer's move
    """

    def computerMove(self):
        move, score = self.miniMax.miniMax(self.board, -float('inf'), float('inf'), self.SEARCH_DEPTH, self.computerDisc)
        print("Computer's move: ", move)
        return move


    """
        Changes the disc after each turn
        @param token: the current disc
        @return: the new disc
    """
    def changeDisc(self, dics: int) -> int:
        if dics == 1:
            return 2
        else:
            return 1

    """
        Runs the game
    """

    def run(self):
        running = True
        disc = self.getStartingDisc()
        print("Player's disc: ", self.playersDisc)
        print("Computer's disc: ", self.computerDisc)
        print("Player starts!" if disc == self.playersDisc else "Computer starts!")
        while running:
            self.board.display()
            if disc == self.playersDisc:
                move = self.getPlayerInput()
                self.board.dropDisc(move, disc)
                print("=====================================")
            else:
                move = self.computerMove()
                self.board.dropDisc(move, disc)
                print("=====================================")
            if self.board.isWinner(self.playersDisc):
                self.board.display()
                print("Player wins!")
                running = False
            elif self.board.isWinner(self.computerDisc):
                self.board.display()
                print("Computer wins!")
                running = False
            elif self.board.isBoardFull():
                self.board.display()
                print("It's a tie!")
                running = False
            else:
                disc = self.changeDisc(disc)
        print("Thank you for playing!")

game = Game()
game.run()
    