#!/usr/bin/python3
"""
pascal_triangle Module
"""

def pascal_triangle(n):
    """returns ntn-size Pascal's triangle"""
    if n <= 0:
        return []  # Return an empty list for n <= 0

    p_triangle = []
    for i in range(n):
        row = [1 if j == 0 or j == i else row[j - 1] + row[j] for j in range(i + 1)]
        p_triangle.append(row)

    return p_triangle
