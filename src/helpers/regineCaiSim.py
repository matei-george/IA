# Problema reginelor folosind calirea simlulata
import time
import random
import math

def read_input(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
        initial_state = [int(x) for x in file.readline().split()]
    return n, initial_state

def write_output(filename, solution):
    with open(filename, 'w') as file:
        file.write('Queens positions: ')
        file.write(' '.join(str(pos) for pos in solution))

def initial_state(n):
    return [random.randint(0, n - 1) for _ in range(n)]

def compute_cost(state):
    n = len(state)
    cost = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                cost += 1
    return cost

def neighbor_state(state):
    new_state = state.copy()
    n = len(state)
    i = random.randint(0, n - 1)
    j = random.randint(0, n - 1)
    new_state[i] = j
    return new_state

def acceptance_probability(old_cost, new_cost, temperature):
    if new_cost < old_cost:
        return 1.0
    return math.exp((old_cost - new_cost) / temperature)

def solve_nqueens(n, initial_temperature, cooling_rate):
    current_state = initial_state(n)
    current_cost = compute_cost(current_state)
    temperature = initial_temperature

    while current_cost > 0:
        next_state = neighbor_state(current_state)
        next_cost = compute_cost(next_state)

        if acceptance_probability(current_cost, next_cost, temperature) > random.random():
            current_state = next_state
            current_cost = next_cost

        temperature *= cooling_rate

    return current_state

def execute():
    start_time = time.time()
    input_file = 'src\data\input-regineCaiSim.txt'
    output_file = 'src\data\output-regineCaiSim.txt'
    initial_temperature = 100.0
    cooling_rate = 0.95  
    n, initial_state = read_input(input_file)
    solution = solve_nqueens(n, initial_temperature, cooling_rate)
    write_output(output_file, solution)
    end_time=time.time()
    elapsed_time=end_time-start_time
    with open("src/data/output-regineCaiSim.txt", "a") as f:
        print("\n{:.5f}".format(elapsed_time), file=f)