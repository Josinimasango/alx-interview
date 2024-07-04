#!/usr/bin/python3
"""N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard
"""

import sys

def is_valid(board, row, col):
    """Check if a queen can be placed on board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N, board, row):
    """Utilize backtracking to find all solutions."""
    if row == N:
        solution = [[i, board[i]] for i in range(N)]
        print(solution)
        return

    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(N, board, row + 1)
            board[row] = -1

def nqueens(N):
    """Initialize the board and start the solving process."""
    board = [-1] * N
    solve_nqueens(N, board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)
