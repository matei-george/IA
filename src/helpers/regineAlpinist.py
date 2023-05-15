# Rezolvarea Problemei reginelor folosind metoda alpinistului
import random
import time


def generate_initial_state(n):
    state = []
    for i in range(n):
        state.append(random.randint(0, n-1))
    return state


def count_conflicts(state):
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i+1, n):
            if state[i] == state[j] or abs(state[i]-state[j]) == j-i:
                conflicts += 1
    return conflicts


def get_best_neighbor(state):
    n = len(state)
    best_state = state
    best_score = count_conflicts(state)
    for i in range(n):
        for j in range(i+1, n):
            new_state = state.copy()
            new_state[i], new_state[j] = new_state[j], new_state[i]
            score = count_conflicts(new_state)
            if score < best_score:
                best_state = new_state
                best_score = score
    return best_state


def hill_climbing(n):
    current_state = generate_initial_state(n)
    current_score = count_conflicts(current_state)
    while True:
        neighbor = get_best_neighbor(current_state)
        neighbor_score = count_conflicts(neighbor)
        if neighbor_score >= current_score:
            return current_state
        current_state = neighbor
        current_score = neighbor_score


def execute():
    start_time = time.time()
    inputValue = None
    with open("src\data\input-regineAlpinist.txt", "r") as f:
        inputValue = f.read()
        inputValue = int(inputValue)
    solution = hill_climbing(inputValue)
    end_time = time.time()
    elapsed_time = end_time-start_time
    with open("src\data\output-regineAlpinist.txt", "w") as f:
        print(solution, file=f)
        print("{:.5f}".format(elapsed_time), file=f)
