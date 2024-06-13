#!/usr/bin/python3
""" rotate a 2d array 90 degrees """


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise."""
    n = len(matrix)
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[j][n - 1 - i] = matrix[i][j]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = result[i][j]


def print_matrix(matrix):
    """Prints a 2D matrix."""
    print("[")
    for row in matrix:
        print("  ", row, ",")
    print("]")


def build_matrix(n):
    """Builds an n x n matrix filled with sequential numbers."""
    return [[n * i + j + 1 for j in range(n)] for i in range(n)]


if __name__ == "__main__":
    matrix = build_matrix(3)
    rotate_2d_matrix(matrix)
    print_matrix(matrix)
    print()

    matrix = build_matrix(5)
    rotate_2d_matrix(matrix)
    print_matrix(matrix)
