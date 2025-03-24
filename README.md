# Connect4 with Minimax
## Abstract
The topics Minimax and Alpha-Beta pruning in the module "Introduction to Artificial Intelligence" at King's College London (KCL) influenced me to build this Connect4 project.

Minimax is an adversarial search algorithm with two players in games/situations (e.g., Connect4, Chess). One player aims to maximize their score, while the other tries to minimize it. The algorithm explores all possible moves (to a certain depth) through a search tree to find the optimal move, assuming both players play optimally. More information about [minimax](https://en.wikipedia.org/wiki/Minimax)

Alpha-Beta pruning is a way of optimizing the minimax to skip unnecessary branches in the search tree. It stops evaluating a move if it finds that another move that leads to a better outcome. This pruning makes the minimax faster while producing the same result. More about [Alpha Beta Pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)

The program uses a kernel to identify a 4 in a row. It works via a [Convolution](https://en.wikipedia.org/wiki/Kernel_(image_processing)) with the board. If there's a four present in the product of doing the convolution of the kernel and the board, this indicates a 4 in a row.

## Set up
1. Install pip if you don't already have it
2. Clone this repository
```command line
   git clone https://github.com/Climber1705/connect4-minimax.git
```
3. Install required dependencies with pip
```command line
   pip install -r requirements.txt
```

## How to run code

To run the code, enter
```command line
   python src/main.py
```

## Improvements
1. Add a transposition table so we don't have to calculate values constantly
2. Speed up the code to set the depth to a higher value (6-8)

## Help and Resources

While developing this project, I used some online resources to fix issues that occurred. The main problem was how to efficiently identify the presence of a 4 in a row on the board in all directions. I found this website, [Stack Overflow](https://stackoverflow.com/questions/29949169/how-to-implement-the-function-that-checks-for-horizontal-vertical-and-diagonal), useful for identifying a solution.  

## License

[GNU](https://choosealicense.com/licenses/gpl-3.0/)
