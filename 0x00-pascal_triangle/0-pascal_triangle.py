#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """
    generates Pascal's triangle to the required number of rows.

    Parameters:
        n (int): number of rows.

    Returns:
        list of lists: Pascal's triangle shown as a list of lists.

    Note:
        Returns an empty list if n <= 0.
    """

    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for i in range(n):
        # creating a row and fill first and last with 1
        new_row = [0] * (i + 1)
        new_row[0] = 1
        new_row[len(new_row) - 1] = 1

        # calculates values for the remaining indices in the row
        for j in range(1, i):
            if j > 0 and j < len(new_row):
                a = pascal_triangle[i - 1][j]
                b = pascal_triangle[i - 1][j - 1]
                new_row[j] = a + b

        pascal_triangle[i] = new_row

    return pascal_triangle
