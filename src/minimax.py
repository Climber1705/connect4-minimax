
from board import Board

"""
    The MiniMax class.
    The class that represents the MiniMax algorithm.
    
    In the algorithm, the computer tries to maximize its score
    while the player tries to minimize it. The computer is the maximizing
    player, and the player is the minimizing player.
      
    The algorithm searches the game tree to find the best move for the computer. The computer
    assumes that the player will make the best move for them. After a certain depth, the algorithm
    evaluates the board and returns the best move
    and score.
    
    The algorithm uses alpha-beta pruning to reduce the number of nodes so
    it can search more profoundly in the game tree.
"""

class MiniMax:

    """
        Attributes of the MiniMax class.
    """
    player_disc: int
    computer_disc: int


    def __init__(self, player_disc, computer_disc):
        self.player_disc = player_disc
        self.computer_disc = computer_disc
        
    """
        The MiniMax algorithm with alpha-beta pruning
        to find the best move for the computer.
        
        @param board: the board.
        @param alpha: the alpha value.
        @param beta: the beta value.
        @param depth: the depth of the search.
        @param token: the current token.
        @return: the best move and the score.
    """

    def mini_max(self, board: Board, alpha: float, beta: float, depth: int, token: int) -> tuple[int, int]:
        # Only need to check if there's a winner of one of the discs as
        # the player who played the last move is the only one who can win
        last_disc = self.player_disc if token == self.computer_disc else self.computer_disc
        if depth == 0 or board.is_board_full() or board.is_winner(last_disc):
            return None, board.evaluate()
        else:
            # Sort valid moves by a heuristic
            # Heuristic: the closer to the middle, the better
            moves = board.get_valid_moves()
            # Moves closers to the middle are "better", so they are evaluated first
            ranked_moves = sorted(moves, key=lambda x: abs(x - board.WIDTH//2))
            best_move = ranked_moves[0]
            if token == self.computer_disc:
                # Maximize
                score = -float('inf')
                for move in ranked_moves:
                    board.drop_disc(move, token) 
                    new_score = max(score, self.mini_max(board, alpha, beta, depth-1, self.player_disc)[1])
                    board.undo_disc(move)
                    if new_score > score:
                        score = new_score
                        best_move = move
                    alpha = max(alpha, score)
                    if alpha >= beta:
                        break
                return best_move, score
            else:
                # Minimize
                score = float('inf')
                for move in ranked_moves:
                    board.drop_disc(move, token)
                    new_score = min(score, self.mini_max(board, alpha, beta, depth-1, self.computer_disc)[1])
                    board.undo_disc(move)
                    if new_score < score:
                        score = new_score
                        best_move = move
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
                return best_move, score
