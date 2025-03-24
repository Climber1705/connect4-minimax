
import numpy as np
from scipy.signal import convolve2d

"""
    The Board class.
    The class represents an action that the board does.
    The 0s represent empty cells, and 1s or 2s represent the player's or computer's discs.
"""
class Board:

    # Kernels for the convolutions.
    h_kernels : list[np.array] = [np.array([[1, 1]]), np.array([[1,1,1]]), np.array([[1,1,1,1]])]
    v_kernels : list[np.array] = [np.array([[1], [1]]), np.array([[1], [1], [1]]), np.array([[1], [1], [1], [1]])]
    dp_kernels : list[np.array] = [np.eye(2), np.eye(3), np.eye(4)]
    dn_kernels : list[np.array] = [np.eye(2)[::-1], np.eye(3)[::-1], np.eye(4)[::-1]]
    
    winning_kernels : list[np.array] = [np.array([[1,1,1,1]]), np.array([[1], [1], [1], [1]]), np.eye(4), np.eye(4)[::-1]]

    # Weights for the score.
    weights : list[int] = [10, 100, 10000]

    # Dimensions of the board.
    WIDTH : int = 7
    HEIGHT : int = 6

    # Player's disc and computer's disc.
    player_disc: int
    computer_disc: int
    
    def __init__(self, board: np.array, player_disc: int, computer_disc: int):
        self.board = board
        self.player_disc = player_disc
        self.computer_disc = computer_disc

    """
        Displays the board.
    """
    def display(self) -> None:
        for row in self.board:
            print(" ".join(map(str, row)))
    
    """
        Check if the column is full.
        @param column: the column to check.
        @return: True if the column isn't, False otherwise.
    """
    def is_valid_move(self, column: int) -> bool:
        return self.board[0][column] == 0
    
    """
        Drops the disc in the column.
        @param column: the column to drop the disc.
        @param disc: the disc being dropped.
        @raises ValueError: if the move is out of bounds or the column is full.
    """
    def drop_disc(self, column: int, disc: int) -> None:
        if column < 0 or column >= self.WIDTH:
            raise ValueError("Move out of bounds")
        elif not self.is_valid_move(column):
            raise ValueError("Column is full")
        else:
            self.board[np.argmax(self.board.T[column] >= 1) - 1][column] = disc

    """
        Undos the move in the column.
        @param column: the column to remove the disc.
        @raises ValueError: if there's no disc to remove or out of bounds.
    """
    def undo_disc(self, column: int) -> None:
        if column < 0 or column >= self.WIDTH:
            raise ValueError("Move out of bounds")
        elif np.all(self.board.T[column] == 0):
            raise ValueError("No disc to remove in column")
        else:
            self.board[np.argmax(self.board.T[column] >= 1)][column] = 0

    """
        Gets the valid moves.
        @return: the valid moves.
    """
    def get_valid_moves(self) -> list[int]:
        return [i for i in range(self.WIDTH) if self.is_valid_move(i)]

    """
        Check if the board is full.
        @return: True if the board is full, False otherwise.
    """
    def is_board_full(self) -> bool:
        return np.all(self.board != 0)
    
    """
        Check if there is a winner.
        @param disc: the disc to check.
        @return: True if there is a winner, False otherwise.
    """
    def is_winner(self, disc: int) -> bool:
        score_board = np.where(self.board == disc, 1, 0)
        for kernel in self.winning_kernels:
            if np.sum(convolve2d(score_board, kernel, mode='valid') == 4) > 0:
                return True
        return False

    """
        Evaluates the board.
        @return: the score of the board.
    """
    def evaluate(self) -> int:
        score = 0
        for disc_type in [1,2]:
            disc_board = np.where(self.board == disc_type, 1, 0)
            if disc_type == self.player_disc:
                score -= self.get_score(disc_board)
            else:
                score += self.get_score(disc_board)
        return score
    
    """
        Gets the number of 2,3,4 in a row.
        @param disc_board: the board with discs of a certain type.
        @return: the score of the board.
    """
    def get_score(self, disc_board : np.array) -> int:
        score = 0
        # Horizontal discs in a row
        for id, kernel in enumerate(self.h_kernels):
            score += np.sum(convolve2d(disc_board, kernel, mode='valid') == id+2) * self.weights[id]
        # Vertical discs in a row
        for id, kernel in enumerate(self.v_kernels):
            score += np.sum(convolve2d(disc_board, kernel, mode='valid') == id+2) * self.weights[id]
        # Diagonal positive discs in a row
        for id, kernel in enumerate(self.dp_kernels):
            score += np.sum(convolve2d(disc_board, kernel, mode='valid') == id+2) * self.weights[id]
        # Diagonal negative discs in a row
        for id, kernel in enumerate(self.dn_kernels):
            score += np.sum(convolve2d(disc_board, kernel, mode='valid') == id+2) * self.weights[id]
        return score
