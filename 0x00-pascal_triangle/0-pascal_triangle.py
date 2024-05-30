#!/usr/bin/python3
"""Pascal Triangle"""

def pascal_triangle(n):
    if n <= 0:
        return []

    # Initializing the triangle with the first row
    triangle = [[1]]

    # Generating each subsequent row
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle

# Testing the function with the provided example
if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))

