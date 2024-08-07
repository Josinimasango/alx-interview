#!/usr/bin/python3
"""
returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """ Returns the parimeter of the island """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # cell that contributes 4 sides to the perimeter
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    # Subtracts 2 if the cell above is also land
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    # Subtracts 2 if the cell on the left is also land
                    perimeter -= 2
    return perimeter
