# 0x08. Making Change

## Itroduction
This project involves solving the coin change problem and encompasses several key coding techniques, along with various concepts. Here are the essential coding techniques needed to solve the coin change problem:

<h3>Dynamic Programming:</h3>
Dynamic programming is a fundamental technique used to efficiently solve problems by breaking them down into smaller subproblems and storing the solutions to these subproblems. In the context of the coin change problem, dynamic programming is often employed to calculate the minimum number of coins needed for different amounts.

<h3>Greedy Algorithms:</h3>
Greedy algorithms involve making locally optimal choices at each stage with the hope of finding a global optimum. In the coin change problem, a greedy approach is often used to iteratively select the largest possible coin denomination at each step until the total is reached. This approach may not always provide the globally optimal solution but is effective in certain scenarios.

<h3>Sorting:</h3>
Sorting is a common technique employed in the coin change problem to order the coin denominations. Sorting the coins in descending order allows for a greedy strategy, where larger denominations are considered first during the iteration.

<h3>Iteration:</h3>
Iteration is crucial for processing each coin denomination and updating the count of coins needed based on the remaining total. Whether using a dynamic programming approach or a greedy algorithm, iterating through the list of coin denominations is a fundamental coding technique.

<h3>Array Manipulation:</h3>
In dynamic programming solutions, manipulating arrays is essential for storing and updating the minimum number of coins needed for different amounts. The array represents the state of the problem and is updated iteratively.

<h3>Modular Arithmetic:</h3>
Modular arithmetic is often used to calculate the remainder when dividing the total by a coin denomination. This remainder helps in determining how many coins of a particular denomination can be used to reduce the total.

<h3>Edge Case Handling:</h3>
Proper handling of edge cases is essential, such as when the total is zero or negative, or when the list of coin denominations is empty or None. These edge cases require specific conditions to return appropriate values (e.g., 0 or -1).

## Tasks:page_with_curl:

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.
- Prototype: `def makeChange(coins, total)`
- Return: fewest number of coins needed to meet `total`
  - If `total` is `0` or less, return `0`
  - If `total` cannot be met by any number of coins you have, return `-1`
- `coins` is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than `0`
- You can assume you have an infinite number of each denomination of coin in the list
- Your solution’s runtime will be evaluated in this task

## Methodology used
The [0-making_change.py](./0-making_change.py) fucntion follows a simple yet efficient approach to solve the coin change problem:

  - **Input Validation:**
    - The script checks if the `total` is less than or equal to zero. If so, it returns `0` as the minimum number of coins needed.
  - **Sorting Coins:**
    - The script sorts the list of `coin` denominations in descending order. This step is crucial for the greedy approach employed in the next step.
  - **Greedy Approach:**
    - The script iterates through the sorted coin denominations.
    - For each `coin`, it calculates how many of that `coin` can be used to meet the remaining total.
    - It updates the total and the count of coins accordingly.
  - **Result:**
    - If the `total` becomes zero, the fucntion returns the total count as the minimum number of coins needed.
    - If the total cannot be met, it returns `-1`.

:+1:
