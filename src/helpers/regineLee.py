# Rezolvarea problemei reginelor prin algoritmul lui Lee
from queue import Queue


def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    queue = Queue()
    queue.put((0, board))

    while not queue.empty():
        col, positions = queue.get()

        if col == n:
            return positions

        for row in range(n):
            if is_safe(positions, row, col, n):
                child_positions = [x[:] for x in positions]
                child_positions[row][col] = 1
                queue.put((col + 1, child_positions))

    return None


def call():
    print('Dati dimensiunea tablei')
    n = int(input())
    board = solve_n_queens(n)
    if board is not None:
        for i in range(n):
            print(board[i])
    else:
        print("Nicio solutie gasita")
