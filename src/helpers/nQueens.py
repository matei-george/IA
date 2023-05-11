import time
import random
import math


class Board(object):
    """An N-Queens solution attempt."""

    def __init__(self, queens):
        """Instances differ by their queen placements."""
        self.queens = queens.copy()  # Not aliasing!

    def display(self):
        """Print the board."""
        for r in range(len(self.queens)):
            for c in range(len(self.queens)):
                if self.queens[c] == r:
                    print('Q', end=' ')
                else:
                    print('-', end=' ')
            print()
        print()

    def moves(self):
        """Return a list of possible moves given the current placements."""
        moves = []
        for col in range(len(self.queens)):
            for row in range(len(self.queens)):
                if self.queens[col] != row:
                    moves.append((col, row))
        return moves

    def neighbor(self, move):
        """Return a Board instance like this one but with one move made."""
        col, row = move
        new_queens = self.queens.copy()
        new_queens[col] = row
        return Board(new_queens)

    def cost(self):
        """Compute the cost of this solution."""
        cost = 0
        for i in range(len(self.queens)):
            for j in range(i + 1, len(self.queens)):
                if self.queens[i] == self.queens[j] or abs(self.queens[i] - self.queens[j]) == j - i:
                    cost += 1
        return cost


class Agent(object):
    """Knows how to solve an n-queens problem with simulated annealing."""

    def anneal(self, board):
        """Return a list of moves to adjust queen placements."""
        temperature = 1000.0
        cooling_rate = 0.95
        current_solution = board
        while temperature > 0.1:
            moves = current_solution.moves()
            move = random.choice(moves)
            neighbor = current_solution.neighbor(move)
            current_cost = current_solution.cost()
            neighbor_cost = neighbor.cost()
            if neighbor_cost < current_cost:
                current_solution = neighbor
            else:
                probability = math.exp(
                    (current_cost - neighbor_cost) / temperature)
                if random.random() < probability:
                    current_solution = neighbor
            temperature *= cooling_rate
        return current_solution.moves()


def call():
    """Create a problem, solve it with simulated annealing, and console-animate."""

    queens = dict()
    for col in range(8):
        row = random.choice(range(8))
        queens[col] = row

    board = Board(queens)
    board.display()

    agent = Agent()
    path = agent.anneal(board)

    while path:
        move = path.pop(0)
        board = board.neighbor(move)
        time.sleep(0.1)
        board.display()