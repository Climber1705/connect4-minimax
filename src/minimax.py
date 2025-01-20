
from board import Board

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
        # Only need to check if there's a winner of one of the discs as
        # the player who played the last move is the only one who can win
        lastDisc = self.playerDisc if token == self.computerDisc else self.computerDisc
        if depth == 0 or board.isBoardFull() or board.isWinner(lastDisc):
            return None, board.evaluate()
        else:
            # Sort valid moves by a heuristic
            # Heuristic: the closer to the middle the better
            moves = board.getValidMoves()
            # Moves closers to the middle are "better" so there are evaluated first
            sortedMoves = sorted(moves, key=lambda x: abs(x - board.WIDTH//2))
            bestMove = sortedMoves[0]
            if token == self.computerDisc:
                # Maximize
                score = -float('inf')
                for move in sortedMoves:
                    board.dropDisc(move, token) 
                    newScore = max(score, self.miniMax(board, alpha, beta, depth-1, self.playerDisc)[1])
                    board.undoDisc(move)
                    if newScore > score:
                        score = newScore
                        bestMove = move
                    alpha = max(alpha, score)
                    if alpha >= beta:
                        break
                return bestMove, score
            else:
                # Minimize
                score = float('inf')
                for move in sortedMoves:
                    board.dropDisc(move, token)
                    newScore = min(score, self.miniMax(board, alpha, beta, depth-1, self.computerDisc)[1])
                    board.undoDisc(move)
                    if newScore < score:
                        score = newScore
                        bestMove = move
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
                return bestMove, score
                
