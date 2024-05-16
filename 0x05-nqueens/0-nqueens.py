#!/usr/bin/python3
""" The N queens puzzle is the challenge """

import sys


def is_safe(board, row, col, N):
    """ Check if it's safe to place a queen at position (row, col)
    on the board.
    """

    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_n_queens_util(board, row, N):
    """ Recursively solve the N queens problem by placing queens
    on the board row by row.
    """

    if row == N:
        queens = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 'Q':
                    queens.append([i, j])
        print(queens)
        return True

    res = False
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 'Q'
            res = solve_n_queens_util(board, row + 1, N) or res
            board[row][col] = '.'
    return res


def solve_n_queens(N):
    """ Solve the N queens problem and print all solutions. """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [['.' for _ in range(N)] for _ in range(N)]
    solve_n_queens_util(board, 0, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_n_queens(N)
