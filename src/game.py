
import numpy as np

from board import Board
from minimax import MiniMax
from random import randint

"""
    The Game class.
    The class that represents the game.
"""
class Game:

    """
        Attributes of the Game class.
    """
    WIDTH : int = 7
    HEIGHT : int = 6
    # Max depth of the search of 7 or take some time to compute for higher values.
    DEPTH : int = 7

    board: Board
    player_disc: int
    computer_disc: int
    minimax: MiniMax

    def __init__(self):
        self.player_disc = 1
        self.computer_disc = 2

        self.board = Board(np.zeros((self.HEIGHT, self.WIDTH), dtype=np.uint8), self.player_disc, self.computer_disc)
        self.minimax = MiniMax(self.player_disc, self.computer_disc)

    """
        Gets the starting disc to determine who starts.
        @return: the starting disc.
    """
    def get_starting_disc(self) -> int:
        if randint(0, 1) == 0:
            return self.player_disc
        return self.computer_disc

    """
        Gets the player's input.
        @return: the player's input.
    """
    def get_player_input(self) -> int:
        while True:
            player_input = input("Enter a column number: ")
            if not player_input.isdigit():
                print("Invalid input. Please enter a number.")
                continue
            if int(player_input) < 0 or int(player_input) > 6:
                print("Invalid input. Please enter a number between 0 and 6.")
                continue
            if not self.board.is_valid_move(int(player_input)):
                print("Invalid input. Please enter a number for a column that is not full.")
                continue
            print("Player's move: ", player_input)
            return int(player_input)

    """
        Gets the computer's move.
        @return: the computer's move.
    """
    def computer_move(self) -> int:
        move, score = self.minimax.mini_max(self.board, -float('inf'), float('inf'), self.DEPTH, self.computer_disc)
        print(f"Computer's move: {move}, Computer's score: {score}")
        return move


    """
        Changes the disc after each turn.
        @param token: the current disc.
        @return: the new disc.
    """
    def change_disc(self, disc: int) -> int:
        if disc == 1:
            return 2
        else:
            return 1

    """
        Runs the game.
    """
    def run(self):
        running = True
        disc = self.get_starting_disc()
        print("Player's disc: ", self.player_disc)
        print("Computer's disc: ", self.computer_disc)
        print("Player starts!" if disc == self.player_disc else "Computer starts!")
        while running:
            self.board.display()
            if disc == self.player_disc:
                move = self.get_player_input()
                self.board.drop_disc(move, disc)
                print("=====================================")
            else:
                move = self.computer_move()
                self.board.drop_disc(move, disc)
                print("=====================================")
            if self.board.is_winner(self.player_disc):
                self.board.display()
                print("Player wins!")
                running = False
            elif self.board.is_winner(self.computer_disc):
                self.board.display()
                print("Computer wins!")
                running = False
            elif self.board.is_board_full():
                self.board.display()
                print("It's a tie!")
                running = False
            else:
                disc = self.change_disc(disc)
        print("Thank you for playing!")
