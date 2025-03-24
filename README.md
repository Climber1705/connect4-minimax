
# Connect4 with Minimax
## Overview
This project implements the **Connect4** game using the **Minimax algorithm** with **Alpha-Beta pruning** to enable an AI opponent to make optimal moves based on a decision tree search. I was inspired by the **Introduction to Artificial Intelligence** module at **King's College London(KCL)**, where I learned about Minimax and Alpha-Beta pruning concepts.

## Minimax Algorithm
Minimax is an **adversarial search algorithm** used in two-player games like **Connect4** and **Chess**. In these games, one player tries to maximize their score, while the other player aims to minimize it. The Minimax algorithm explores all possible moves (to a specific depth) by recursively evaluating the game state, assuming both players play optimally. The algorithm then chooses the move that maximizes the player's chances of winning, while minimizing the opponent's chances.
For more information about Minimax, check out the [Wikipedia article](https://en.wikipedia.org/wiki/Minimax).

## Alpha-Beta Pruning
**Alpha-Beta pruning** is an optimisation technique for the Minimax algorithm. It reduces the number of branches evaluated in the search tree by eliminating branches that can't possibly influence the final decision. To achieve this, we maintain two values: Alpha and Beta. Alpha represents the minimum score the maximising player can guarantee, while Beta represents the maximum score the minimising player can guarantee.".When the algorithm encounters a branch during the search process where one player's score cannot exceed the other player's score, it prunes that branch to search more quickly.
For more information about **Alpha-Beta pruning**, check out the [Wikipedia article](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).

## Four-in-a-Row Detection
The program uses a kernel convolution approach to detect when a player has aligned **four pieces in a row**. A kernel is applied over the game board to efficiently check for sequences of four consecutive pieces in any direction (horizontal, vertical, or diagonal). If the result of the convolution operation shows a "four-in-a-row" pattern, the program recognises that a player has won.
For more information about convolution, check out the [Wikipedia article](https://en.wikipedia.org/wiki/Kernel_(image_processing)).

## Features
- Play Connect4 with a computer opponent using the Minimax algorithm.
- Alpha-Beta pruning for faster decision-making.
- Efficient kernel convolution for detecting "four in a row".
- Simple command-line interface.

## Requirements
Before running the project, install **Python 3.x** and **pip**.
### Dependencies:
To install the required dependencies, you can use the `requirements.txt` file.
```bash
pip install -r requirements.txt
```

## Installation
Follow these steps to get the project running on your local machine.
1. Clone the repository to your local machine:
```bash
 git clone https://github.com/Climber1705/connect4-minimax.git
```
2. Navigate into the project directory:
```bash
 cd connect4-minimax
```
3. Install all required Python dependencies:
```bash
 pip install -r requirements.txt
```
## How to Run the Code
To start playing Connect4 with the Minimax algorithm, run the following command:
```bash
python src/main.py
```
This command will start the game, and the computer will play against you using the Minimax algorithm.

## Code Structure
Here’s a quick overview of the project file structure:
```graphql
connect4-minimax/
│
├── src/
│   ├── main.py           # Entry point to run the game
│   ├── minimax.py        # Contains the Minimax algorithm and Alpha-Beta pruning implementation
│   ├── game.py           # Handles the game board logic and move validation
│   └── board.py          # Contains logic for the Connect4 board, including checking for "four in a row."
│
├── requirements.txt      # List of Python dependencies
├── README.md             # This README file
└── LICENSE               # Project license (GNU)
```
## How the Minimax Algorithm Works
- **Minimax Algorithm:** This is the core algorithm used for decision-making in two-player games. The algorithm explores all possible moves and recursively evaluates the best option for both players. One player aims to maximise their score, while the other seeks to minimise it.

- **Alpha-Beta Pruning:** Alpha-Beta pruning is an optimisation technique used with Minimax. It reduces the number of nodes evaluated in the search tree by "pruning" branches that won't affect the final decision.

- **Kernel Convolution:** To efficiently check for four in a row, the program applies a convolutional kernel over the board, which allows quick detection of four consecutive pieces in any direction (horizontal, vertical, or diagonal).

## Tests
This project includes unit tests to verify the correctness of the Minimax algorithm, board logic, and game mechanics. The tests include timing measurements to assess the execution time of the Minimax search at various depths.

## Running Unit Tests
We implement unit tests using `unittest` to cover the following components:
- **Minimax Algorithm & Alpha-Beta Pruning:** Ensures that the AI selects optimal moves.
- **Board Logic:** Validates detecting "four in a row" conditions.
- **Game Mechanics:** Tests move validation and game state updates.

## Running All Unit Tests
To execute all unit tests, run the following command:
```bash
python -m unittest discover -s tests
```

## Test File Structure
```graphql
tests/
├── test_minimax.py   # Tests Minimax algorithm and Alpha-Beta pruning
├── test_board.py     # Tests board logic and four-in-a-row detection
├── test_game.py      # Tests game mechanics and move validation
```

## Running Timing Tests
The **timing tests** measure the execution time of the Minimax algorithm at different search depths. This script helps analyse performance and determine practical depth limits.
## Running the Timing Test
To execute the timing tests, run the following:
```bash
python timing/test_timing.py
```

## Expected Output
The script will output the execution time for different depths, for example:
```bash
Depth 1: 0.0084 seconds
Depth 2: 0.0084 seconds
Depth 3: 0.0328 seconds
Depth 4: 0.0578 seconds
Depth 5: 0.3377 seconds
Depth 6: 0.3351 seconds
Depth 7: 3.3792 seconds
Depth 8: 4.7649 seconds
```

## Timing Test File Structure
```graphql
timing/
├── test_timing.py   # Measures execution time of Minimax at different depths
```

## Improvements
Here are some potential future improvements:
1. **Transposition Table:** Implement a transposition table to store previously evaluated board states and avoid redundant calculations.
2. **Depth Enhancement:** Increase the depth of the search tree (currently limited) to improve the AI’s decision-making ability. A higher depth, however, would require optimisations for performance.
3. **Graphical User Interface (GUI):** Implement a GUI to make the game more interactive and visually appealing.
4. **Multiplayer Option:** Add a multiplayer mode where two human players can compete against each other.

## Help and Resources
The following resources were helpful while developing the project:
- [Wikipedia Minimax Algorithm](https://en.wikipedia.org/wiki/Minimax)
- [Wikipedia Alpha-Beta Pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)
- [Stack Overflow - Four-in-a-Row Detection](https://stackoverflow.com/questions/29949169/how-to-implement-the-function-that-checks-for-horizontal-vertical-and-diagonal)

## License
This project operates under the GNU General Public License v3.0. The [LICENSE](https://choosealicense.com/licenses/gpl-3.0/) file provides details.
