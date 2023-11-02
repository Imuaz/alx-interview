# 0x05. N Queens

**INTRODUCTION**

The N-Queens problem is a classic combinatorial problem that involves placing N chess queens on an N×N chessboard in such a way that no two queens threaten each other. This means that no two queens can be in the same row, column, or diagonal. The only task for this project is to find all possible solutions for placing N queens on the board.

## Task:page_with_curl:

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

- Usage: `nqueens N`
  - If the user called the program with the wrong number of arguments, prints `Usage: nqueens N`, followed by a new line, and exit with the status `1`
- where N must be an integer greater or equal to `4`
  - If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status `1`
  - If N is smaller than `4`, print `N must be at least 4`, followed by a new line, and exit with the status `1`
- The program should print every possible solution to the problem
  - One solution per line
  - Format:
  ```
  $ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
  ```
  - You don’t have to print the solutions in a specific order
- You are only allowed to import the sys module

## Solution
Here's a step-by-step explanation of how the problem is solved [0-nqueens.py](./0-nqueens.py):

1. Backtracking Algorithm:
  - The core of the solution is a recursive backtracking algorithm.
  - The `backtrack` function is called initially with `r = 0` and empty sets `col`, `posDiag`, `negDiag` for the chess board column, positive diagonal, and negetive diagonal respectively. These sets keep track of which columns and diagonals are occupied by queens at a given level of recursion.
  - The board is a 2D grid representing the chessboard. Initially, it's filled with empty squares ('').
  - The algorithm tries to place queens on the board row by row, starting from row 0.
  - It iterates through each column `c` in the current row `r`. It checks if placing a queen at `(r, c)` would be a valid move by checking if `c` is not in `col`, `(r + c)` is not in `posDiag`, and `(r - c)` is not in `negDiag`. If it's a valid move, it proceeds.
  - If the move is valid, it updates `col`, `posDiag`, and `negDiag` to reflect the new queen's position, sets the corresponding square in board to `'Q'`, and moves on to the next row by calling `backtrack(r + 1, col, posDiag, negDiag)`.
  - If placing a queen in the current column doesn't lead to a valid solution in the remaining rows, the algorithm backtracks by removing the queen from `col`, `posDiag`, and `negDiag`, and setting the square back to `''` in board.

2. Solution Recording:
  - When the backtrack function reaches the last row `(r == n)`, it means a solution has been found. The positions of queens on the board are recorded in the queens list and appended to the `res` list, which holds all solutions.

3. Input Validation:
  - The program firstly checks the command-line arguments. It ensures that the user has provided exactly one argument, which is the value of N, the number of queens to be placed on the board.

4. Parsing N:
  - The program attempts to convert the user-provided argument into an integer to determine the size of the chessboard.
5. Output:
  - The program prints each solution, which is a list of queen positions for each row, in the specified format. 

The backtracking algorithm explores all possible queen placements, ensuring that no two queens threaten each other. As valid solutions are found, they are recorded in the `res` (result) list, and at the end, all solutions are printed.
