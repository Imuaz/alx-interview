#!/usr/bin/python3


def rotate_2d_matrix(matrix):
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            # save the top left value
            top_left = matrix[top][left + i]

            # move bottom left in to top left
            matrix[top][left + i] = matrix[bottom - i][left]

            # move bottom right into bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # move top right into bottom right
            matrix[bottom][right - i] = matrix[top + i][right]

            # move top left into top right
            matrix[top + i][right] = top_left
        right -= 1
        left += 1


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
