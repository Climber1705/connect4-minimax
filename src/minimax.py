
from board import Board
from copy import deepcopy

"""
    The MiniMax class
    The class that represents the MiniMax algorithm
    
    In the algorithm, the computer tries to maximize its score
    while the player tries to minimize it

    The algorithm uses alpha-beta pruning to reduce the number of nodes so
    it can search deeper in the game tree
"""

class MiniMax:

    """
        Attributes of the MiniMax class
    """

    playerDisc: int
    computerDisc: int

    """
        Constructor of the MiniMax class
    """

    def __init__(self, playerDisc, computerDisc):
        self.playerDisc = playerDisc
        self.computerDisc = computerDisc

    """
        The MiniMax algorithm with alpha-beta pruning
        to find the best move for the computer
        
        @param board: the board
        @param alpha: the alpha value
        @param beta: the beta value
        @param depth: the depth of the search
        @param token: the current token
        @return: the best move and the score
    """

    def miniMax(self, board: Board, alpha: float, beta: float, depth: int, token: int) -> tuple[int, int]:
        if depth == 0 or board.isGameOver():
            return None, board.evaluate()
        else:
            moves = board.getValidMoves()
            if token == self.computerDisc:
                #Maximize
                score = -float('inf')
                bestMove = moves[0]
                for move in moves:
                    newBoard = deepcopy(board)
                    newBoard.dropDisc(move, token)
                    newScore = max(score, self.miniMax(newBoard, alpha, beta, depth-1, self.playerDisc)[1])
                    if newScore > score:
                        score = newScore
                        bestMove = move
                    alpha = max(alpha, score)
                    if alpha >= beta:
                        break
                return bestMove, score
            else:
                #Minimize
                score = float('inf')
                bestMove = moves[0]
                for move in moves:
                    newBoard = deepcopy(board)
                    newBoard.dropDisc(move, token)
                    newScore = min(score, self.miniMax(newBoard, alpha, beta, depth-1, self.computerDisc)[1])
                    if newScore < score:
                        score = newScore
                        bestMove = move
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
                return bestMove, score
                