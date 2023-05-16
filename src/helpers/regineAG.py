import random
import time

# Fitness function to calculate the fitness of an individual
def fitness(individual):
    conflicts = 0
    n = len(individual)
    for i in range(n):
        for j in range(i + 1, n): # type: ignore
            if individual[i] == individual[j]:
                conflicts += 1
            elif abs(i - j) == abs(individual[i] - individual[j]):
                conflicts += 1
    return 1 / (conflicts + 1)

# Selection function to select the fittest individuals
def selection(population, fitness_fn):
    fitnesses = [fitness_fn(individual) for individual in population]
    total_fitness = sum(fitnesses)
    probabilities = [fitness / total_fitness for fitness in fitnesses]
    selected = random.choices(population, probabilities, k=len(population))
    return selected

# Crossover function to create offspring from parents
def crossover(parents):
    n = len(parents[0])
    pivot = random.randint(0, n - 1)
    offspring = []
    for i in range(len(parents)):
        parent1 = parents[i]
        parent2 = parents[(i + 1) % len(parents)]
        child = parent1[:pivot] + parent2[pivot:]
        offspring.append(child)
    return offspring

# Mutation function to introduce random changes in individuals
def mutation(individual):
    n = len(individual)
    pivot = random.randint(0, n - 1)
    gene = random.randint(0, n - 1)
    individual[pivot] = gene
    return individual

# Genetic algorithm to solve the n-queens problem
def genetic_algorithm(n, population_size, generations):
    population = [[random.randint(0, n - 1) for _ in range(n)] for _ in range(population_size)]
    for i in range(generations):
        selected = selection(population, fitness)
        offspring = crossover(selected)
        mutated = [mutation(individual) for individual in offspring]
        population = selected + mutated
    fittest_individual = max(population, key=fitness)
    return fittest_individual

def execute():
    with open("src/data/input-regineAG.txt",'r') as f:
        inputValue=f.readline()
        population_size=f.readline()
        generations=f.readline()
        inputValue=int(inputValue)
        population_size=int(population_size)
        generations=int(generations)
    start_time=time.time()
    solution = genetic_algorithm(inputValue,population_size,generations)
    end_time=time.time()
    elapsed_time=end_time-start_time
    with open("src/data/output-regineAG.txt",'w') as f:
        print(solution,file=f)
        print("{:.5f}".format(elapsed_time), file=f)