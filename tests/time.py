
import sys
import os
import numpy as np
import time

import timeit

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from minimax import MiniMax
from board import Board

"""
    Time for execution code
"""

def main():
    playerDisc = 1
    computerDisc = 2

    minimax = MiniMax(playerDisc, computerDisc)
    board = Board(np.zeros((6,7), dtype=np.uint8), playerDisc, computerDisc)

    for depth in range(1,11):
        start = time.time()
        minimax.miniMax(board, -float('inf'), float('inf'), depth, computerDisc)
        end = time.time()
        print(f"---- {round(end - start, 5)} seconds for depth={depth}")

main()


