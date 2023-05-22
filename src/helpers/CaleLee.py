# Algoritmul lui Lee cu ajutorul caruia gasim cea mai scurta cale dintre doua puncte din matrice.
from collections import deque
import time


def lee_algorithm(matrix, start, end):
    queue = deque()
    visited = set()
    distance = {start: 0}
    prev = {}

    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.popleft()
        for neighbor in get_neighbors(matrix, node):
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[node] + 1
                prev[neighbor] = node
                queue.append(neighbor)

            if neighbor == end:
                return get_shortest_path(prev, start, end)

    return None


def get_neighbors(matrix, node):
    neighbors = []
    row, col = node
    if row > 0 and matrix[row - 1][col] != -1:
        neighbors.append((row - 1, col))
    if row < len(matrix) - 1 and matrix[row + 1][col] != -1:
        neighbors.append((row + 1, col))
    if col > 0 and matrix[row][col - 1] != -1:
        neighbors.append((row, col - 1))
    if col < len(matrix[0]) - 1 and matrix[row][col + 1] != -1:
        neighbors.append((row, col + 1))

    return neighbors


def get_shortest_path(prev, start, end):
    path = []
    node = end

    while node != start:
        path.append(node)
        node = prev[node]

    path.append(start)
    path.reverse()

    return path


def execute():
    matrix = []
    start = None
    end = None
    with open('src\data\input-CaleLee.txt') as f: # type: ignore
        for line_num, line in enumerate(f):
            if line_num < 8:
                row = [int(x) for x in line.strip().split(',')]
                matrix.append(row)
            elif line_num == 8:
                start = tuple([int(x) for x in line.strip().split(',')])
            elif line_num == 9:
                end = tuple([int(x) for x in line.strip().split(',')])
    start_time = time.time()
    shortest_path = lee_algorithm(matrix, start, end)
    end_time = time.time()
    elapsed_time = end_time - start_time
    with open('src/data/output-CaleLee.txt', "w") as f:
        print(shortest_path, file=f)
        print("{:.5f}".format(elapsed_time), file=f)