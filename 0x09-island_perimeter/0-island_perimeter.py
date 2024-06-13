#!/usr/bin/python3
"""Returns the perimeter of the island described in the grid."""


def island_perimeter(grid):
    """Returns the perimeter of the island described in the grid."""
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check all four directions (top, bottom, left, right)
                if r == 0 or grid[r-1][c] == 0:  # top
                    perimeter += 1
                if r == rows-1 or grid[r+1][c] == 0:  # bottom
                    perimeter += 1
                if c == 0 or grid[r][c-1] == 0:  # left
                    perimeter += 1
                if c == cols-1 or grid[r][c+1] == 0:  # right
                    perimeter += 1

    return perimeter
