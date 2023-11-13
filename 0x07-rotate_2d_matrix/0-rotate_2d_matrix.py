#!/usr/bin/python3


def rotate_2d_matrix(matrix):
    top, left = 0, 0
    bottom, right = len(matrix) - 1, len(matrix[0]) - 1

    while top < bottom and left < right:
        for i in range(right - left):
            # Save top left value
            top_left = matrix[top][left + i]

            # Move bottom left to top left
            matrix[top][left + i] = matrix[bottom - i][left]

            # Move bottom right to bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # Move top right to bottom right
            matrix[bottom][right - i] = matrix[top + i][right]

            # Move top left to top right
            matrix[top + i][right] = top_left

        # Update pointers for the next layer
        top += 1
        left += 1
        bottom -= 1
        right -= 1


# alternatively
'''
def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
'''
