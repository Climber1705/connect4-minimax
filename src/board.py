

import numpy as np
from scipy.signal import convolve2d

"""
    The BoardActions class
    The class that represents action that the board does
    The 0s represent empty cells, 1s or 2s represent the player's or computer's discs
"""

class Board:

    # Kernels for the convolutions
    h_kernels : list[np.array] = [np.array([[1, 1]]), np.array([[1,1,1]]), np.array([[1,1,1,1]])]
    v_kernels : list[np.array] = [np.array([[1], [1]]), np.array([[1], [1], [1]]), np.array([[1], [1], [1], [1]])]
    dp_kernels : list[np.array] = [np.eye(2), np.eye(3), np.eye(4)]
    dn_kernels : list[np.array] = [np.eye(2)[::-1], np.eye(3)[::-1], np.eye(4)[::-1]]
    
    winning_kernels : list[np.array] = [np.array([[1,1,1,1]]), np.array([[1], [1], [1], [1]]), np.eye(4), np.eye(4)[::-1]]

    # Weights for the score
    weights : list[int] = [10, 100, 1000]

    # Dimensions of board
    WIDTH : int = 7
    HEIGHT : int = 6

    # Player's disc and computer's disc
    playerDisc: int
    computerDisc: int
    
    def __init__(self, board: np.array, playerDisc: int, computerDisc: int):
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
        if column < 0 or column >= self.WIDTH:
            raise ValueError("Move out of bounds")
        elif not self.isValidMove(column):
            raise ValueError("Column is full")
        else:
            self.board[np.argmax(self.board.T[column] >= 1) - 1][column] = disc

    """
        Undos the move in the column
        @param column: the column to remove the disc
        @raises ValueError: if there's no disc to remove or out of bounds
    """

    def undoDisc(self, column: int) -> np.array:
        if column < 0 or column >= self.WIDTH:
            raise ValueError("Move out of bounds")
        elif np.all(self.board.T[column] == 0):
            raise ValueError("No disc to remove in column")
        else:
            self.board[np.argmax(self.board.T[column] >= 1)][column] = 0

    """
        Gets the valid moves
        @param: the current board
        @return: the valid moves
    """

    def getValidMoves(self) -> list[int]:
        return [i for i in range(self.WIDTH) if self.isValidMove(i)]

    """
        Checks if the board is full
        @param: the current board
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
        @param board: the board being evaluated
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
        # Horizontal 4 in a row
        for id, kernel in enumerate(self.h_kernels):
            score += np.sum(convolve2d(discBoard, kernel, mode='valid') == id+2) * self.weights[id]
        # Vertical 4 in a row
        for id, kernel in enumerate(self.v_kernels):
            score += np.sum(convolve2d(discBoard, kernel, mode='valid') == id+2) * self.weights[id]
        # Diagonal positive 4 in a row
        for id, kernel in enumerate(self.dp_kernels):
            score += np.sum(convolve2d(discBoard, kernel, mode='valid') == id+2) * self.weights[id]
        # Diagonal negative 4 in a row
        for id, kernel in enumerate(self.dn_kernels):
            score += np.sum(convolve2d(discBoard, kernel, mode='valid') == id+2) * self.weights[id]
        return score
