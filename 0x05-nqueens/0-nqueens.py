#!/usr/bin/python3
'''
N Queens Module
'''
import sys


def solveNQueens(n):
    '''Solves the N Queens problem'''
    def backtrack(r, col, posDiag, negDiag):
        '''Backtracking function use to solve the problem'''
        if r == n:
            queens = []
            for row in range(n):
                for c in range(n):
                    if board[row][c] == 'Q':
                        queens.append([row, c])
            res.append(queens)
            return
        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = 'Q'

            backtrack(r + 1, col, posDiag, negDiag)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = '.'

    col = set()
    posDiag = set()  # (r + c)
    negDiag = set()  # (r - c)
    res = []
    board = [['.'] * n for i in range(n)]

    backtrack(0, col, posDiag, negDiag)
    return res


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = solveNQueens(n)
    for solution in solutions:
        print(solution)
