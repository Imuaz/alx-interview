# 0x09. Island Perimeter

## Tasks
**0. Island Perimeter**
- Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in grid:
  - `grid` is a list of list of integers:
    - `0` represents water
    - `1` represents land
    - Each cell is square, with a side length of `1`
    - Cells are connected horizontally/vertically (not diagonally).
    - `grid` is rectangular, with its width and height not exceeding 100
  - The grid is completely surrounded by water
  - There is only one island (or nothing).
  - The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

## Approach used

Let's break down the approach followed to solve the problem:

**1. Perimeter Initialization:**
  - A variable named `perimeter` is initialised to zero. This variable will be used to accumulate the perimeter count.

**2. Iterating Through the Grid:**
  - Nested loops are used to iterate through each cell of the grid. The outer loop (`for i`) iterates through the rows, and the inner loop (`for j`) iterates through the columns.

**3. Checking for Land Cells:**
  - For each cell in the grid, it checks if the value is `1`, indicating land. If it's land, the code proceeds to calculate the perimeter contribution of that land cell.

**4. Checking Surrounding Cells:**
  - For each land cell, the code checks its surrounding cells (up, down, left, right).
If any adjacent cell is water (`0`) or the current cell is at the edge of the grid, it increments the `perimeter` counter.

**5. Handling Boundary Cases:**
  - Special attention is given to cells at the edges of the grid. If a land cell is at the top, bottom, left, or right edge, it contributes to the perimeter because it's part of the island bordering the water.

**6. Accumulating Perimeter:**
  - The `perimeter` variable is updated based on the conditions met during the iteration.

**7. Returning the Result:**
After iterating through the entire grid, the final accumulated perimeter value is returned.

- In summary, the algorithm efficiently calculates the perimeter of the island by considering the presence of land cells and their surroundings, while also accounting for the grid boundaries. This approach ensures that the specific conditions of the problem, such as the absence of lakes and the island being completely surrounded by water, are taken into account during the perimeter calculation.
