import numpy as np
import os
import time

steps = 50
m = n = 25
board = np.zeros((m, n))

# R-pentomino pattern
center_row, center_col = m // 2, n // 2
board[center_row - 1, center_col] = 1
board[center_row - 1, center_col + 1] = 1
board[center_row, center_col - 1] = 1
board[center_row, center_col] = 1
board[center_row + 1, center_col] = 1


def living_neighbors(r, c):
    d1 = [-1, 0, 1]
    d2 = [-1, 0, 1]
    ans = 0

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            in_bounds = 0 <= r + d1[i] < m and 0 <= c + d2[j] < n
            if in_bounds and board[r + d1[i], c + d2[j]]:
                ans += 1

    return ans


def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')

    GREEN = "\033[92m"
    RESET = "\033[0m"

    board_str = '\n'.join(
        [' '.join([f"{GREEN}O{RESET}" if cell else '.' for cell in row])
         for row in board]
    )
    print(board_str)
    print("\nPress Ctrl+C to stop.")


for _ in range(steps):
    print_board(board)
    new_board = np.zeros((m, n))
    for r in range(len(board)):
        for c in range(len(board[0])):
            alive = board[r, c]
            neighbors = living_neighbors(r, c)
            stays_alive = alive and 2 <= neighbors <= 3
            revived = not alive and neighbors == 3

            if stays_alive or revived:
                new_board[r, c] = 1
    board = new_board
    time.sleep(0.5)
