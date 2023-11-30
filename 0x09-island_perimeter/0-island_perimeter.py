#!/usr/bin/python3
'''
Island Perimeter
'''


def island_perimeter(grid):
    '''
    the perimeter of th'e island described in
    '''
    perimeter = 0

    # Iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:  # Check for land cell
                # Check surrounding cells (up, down, left, right)
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1  # Top edge
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1  # Bottom edge
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1  # Left edge
                if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1  # Right edge

    return perimeter
