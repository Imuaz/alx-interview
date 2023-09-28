#!/usr/bin/python3
"""
pascal_triangle Module
"""

def pascal_triangle(n):
    if n <= 0:
        return []  # Return an empty list for n <= 0

    triangle = []  # Initialize an empty list to store the triangle

    for row in range(n):
        current_row = []  # Initialize the current row
        for col in range(row + 1):
            if col == 0 or col == row:
                current_row.append(1)  # The first and last elements of each row are 1
            else:
                # Calculate the middle elements by adding the two numbers above
                above_row = triangle[row - 1]
                current_value = above_row[col - 1] + above_row[col]
                current_row.append(current_value)
        triangle.append(current_row)  # Add the current row to the triangle

    return triangle
