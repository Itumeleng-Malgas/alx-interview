#!/usr/bin/python3
""" module to rotates a 2d array 90 degrees """


def rotate_2d_matrix(m):
    """Rotates a 2D matrix 90 degrees clockwise."""
    n = len(m)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = m[i][j]
            m[i][j] = m[n - j - 1][i]
            m[n - j - 1][i] = m[n - i - 1][n - j - 1]
            m[n - i - 1][n - j - 1] = m[j][n - i - 1]
            m[j][n - i - 1] = temp


def print_matrix(matrix):
    """Prints a 2D matrix."""
    print("[")
    for row in matrix:
        print("  ", row)
    print("]")


def build_matrix(n):
    """Builds an n x n 2D matrix."""
    return [[n * i + j + 1 for j in range(n)] for i in range(n)]


if __name__ == "__main__":
    for size in [3, 5]:
        matrix = build_matrix(size)
        rotate_2d_matrix(matrix)
        print_matrix(matrix)
        print()
