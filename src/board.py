

import numpy as np
from scipy.signal import convolve2d

"""
    The Board class
    The class that represents the board of the game
    The 0s represent empty cells, 1s or 2s represent the player's or computer's discs
"""

class Board:

    """
        Attributes of the Board class
    """

    #Kernels for the convolutions
    h_kernels : list[np.array] = [np.array([[1, 1]]), np.array([[1,1,1]]), np.array([[1,1,1,1]])]
    v_kernels : list[np.array] = [np.array([[1], [1]]), np.array([[1], [1], [1]]), np.array([[1], [1], [1], [1]])]
    dp_kernels : list[np.array] = [np.eye(2), np.eye(3), np.eye(4)]
    dn_kernels : list[np.array] = [np.eye(2)[::-1], np.eye(3)[::-1], np.eye(4)[::-1]]
    
    winning_kernels : list[np.array] = [np.array([[1,1,1,1]]), np.array([[1], [1], [1], [1]]), np.eye(4), np.eye(4)[::-1]]

    #Weights for the score
    weights : list[int] = [10, 100, 1000]

    #Board, player's disc and computer's disc
    board: np.array
    playerDisc: int
    computerDisc: int

    """
        Constructor of the Board class
        @param board: the board
        @param playerDisc: the player's disc
        @param computerDisc: the computer's disc
    """

    def __init__(self, board, playerDisc, computerDisc):
        self.board = board
        self.playerDisc = playerDisc
        self.computerDisc = computerDisc
    
    """
        Displays the board
    """
    def display(self):
        for row in self.board:
            print(" ".join(map(str, row)))
    
    """
        Checks if the column is full
        @param column: the column to check
        @return: True if the column isn't, False otherwise
    """

    def isValidMove(self, column: int) -> bool:
        return self.board[0][column] == 0
    
    """
        Drops the disc in the column
        @param column: the column to drop the disc
        @param disc: the disc to drop
        @raises ValueError: if the move is out of bounds or the column is full
    """

    def dropDisc(self, column: int, disc: int):
        if column < 0 or column > 6:
            raise ValueError("Move out of bounds")
        elif not self.isValidMove(column):
            raise ValueError("Column is full")
        else:
            for i in range(5, -1, -1):
                if self.board[i][column] == 0:
                    self.board[i][column] = disc
                    break

    """
        Gets the valid moves
        @return: the valid moves
    """

    def getValidMoves(self) -> list[int]:
        return [i for i in range(7) if self.isValidMove(i)]

    """
        Checks if the game is over
        i.e the board is full or there is a winner
        @return: True if the game is over, False otherwise
    """

    def isGameOver(self) -> bool:
        return self.isBoardFull() or self.isWinner(self.playerDisc) or self.isWinner(self.computerDisc)

    """
        Checks if the board is full
        @return: True if the board is full, False otherwise
    """

    def isBoardFull(self) -> bool:
        return np.all(self.board != 0)
    
    """
        Checks if there is a winner
        @param disc: the disc to check
        @return: True if there is a winner, False otherwise
    """

    def isWinner(self, disc: int) -> bool:
        scoreBoard = np.where(self.board == disc, 1, 0)
        for kernel in self.winning_kernels:
            if np.sum(convolve2d(scoreBoard, kernel, mode='valid') == 4) > 0:
                return True
        return False

    """
        Evaluates the board
        @param playerDisc: the player's disc
        @param computerDisc: the computer's disc
        @return: the score of the board
    """

    def evaluate(self) -> int:
        score = 0
        for discType in [1,2]:
            discBoard = np.where(self.board == discType, 1, 0)
            if discType == self.playerDisc:
                score -= self.getScore(discBoard)
            else:
                score += self.getScore(discBoard)
        return score
    
    """
        Gets the number of 2,3,4 in a row
        @param discBoard: the board with the discs of a certain type
        @return: the score of the board
    """

    def getScore(self, discBoard : np.array) -> int:
        score = 0
        #Horizontal
        for id, kernel in enumerate(self.h_kernels):
            score += np.sum(convolve2d(discBoard, kernel, mode='valid') == id+2) * self.weights[id]
        #Vertical
        for id, kernel in enumerate(self.v_kernels):
            score += np.sum(convolve2d(discBoard, kernel, mode='valid') == id+2) * self.weights[id]
        #Diagonal positive
        for id, kernel in enumerate(self.dp_kernels):
            score += np.sum(convolve2d(discBoard, kernel, mode='valid') == id+2) * self.weights[id]
        #Diagonal negative
        for id, kernel in enumerate(self.dn_kernels):
            score += np.sum(convolve2d(discBoard, kernel, mode='valid') == id+2) * self.weights[id]
        return score
