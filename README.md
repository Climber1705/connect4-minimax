# Connect4 with Minimax
## Abstract
The topics Minimax and Alpha-Beta pruning in the module "Intro to AI" at King's College London (KCL) influenced me to build this Connect4 project.

Minimax is an adversarial search algorithm used in games/situations with two players (e.g. Connect4). One player aims to maximize their score, while the other tries to minimize it. The algorithm explores all possible moves (to a certain depth) through a search tree to find the optimal move, assuming both players play optimally. More information about [Minimax](https://en.wikipedia.org/wiki/Minimax)

Alpha-Beta pruning is a way of optimizing the minimax so that it skips unnecessary branches in the search tree. It stops evaluating a move if it finds that another move that leads to a better outcome. This makes the minimax faster while producing the same result. More at about [Alpha Beta Pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)

A kernel was used to identify a 4 in a row. This works via a [Convolution](https://en.wikipedia.org/wiki/Kernel_(image_processing)) with the board. If there's a 4 present in the product of doing the convolution of the kernel and the board this indicates a 4 in a row.

## Set up
1. Install pip if you don't already have it
2. Clone this repository
```command line
   git clone https://github.com/Climber1705/connect4minimax.git
```
3. Install required dependencies with pip
```command line
   pip install -r requirements.txt
```

## How to run code

To run the code enter
```command line
   python src/main.py
```

## Improvements
1. Want to add a heuritic to improve how many the alpha-beta pruning algorithm prunes the search tree
2. Want to speed up the code so I can set the depth to a higher value.

## Help and Resources

While developing this project, I used some online resources to fix issues which occurred. The main problem was about the efficient of identifying the presence of a 4 in a row on the board in all directions. I found this website, [Stack Overflow](https://stackoverflow.com/questions/29949169/how-to-implement-the-function-that-checks-for-horizontal-vertical-and-diagonal), useful for identifying a solution.  

## License

[GNU](https://choosealicense.com/licenses/gpl-3.0/)
