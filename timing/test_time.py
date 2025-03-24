
import sys
import os
import numpy as np
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from minimax import MiniMax
from board import Board

"""
    Displays the time of the minimax to search through the search tree.
"""
def time_minimax():
    board = Board(np.zeros((6, 7), dtype=np.uint8), 1, 2)
    minimax = MiniMax(1, 2)
    depths = [depth for depth in range(1, 16)]
    for depth in depths:
        start_time = time.time()
        minimax.mini_max(board, -float('inf'), float('inf'), depth, 2)
        end_time = time.time()
        print(f"Depth {depth}: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    time_minimax()

