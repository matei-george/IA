# Rezolvarea problemei comis-voiajorului folosindu-ne de algoritmul Nearest Neighbour
import time

# functie pentru a gasi cel mai apropiat oras nevizitat


def find_nearest_unvisited_city(city, unvisited_cities, adjacency_list):
    nearest_city = None
    nearest_distance = float('inf')
    for neighbor_city, distance in adjacency_list[city]:
        if neighbor_city in unvisited_cities and distance < nearest_distance:
            nearest_city = neighbor_city
            nearest_distance = distance
    return nearest_city, nearest_distance

# functie pentru a rezolva problema comis-voiajorului folosind algoritmul nearest neighbour


def nearest_neighbour(adjacency_list, start_city):
    start_time = time.time()

    n = len(adjacency_list)
    visited_cities = [start_city]
    unvisited_cities = list(range(n))
    unvisited_cities.remove(start_city)
    total_distance = 0

    current_city = start_city
    while unvisited_cities:
        nearest_city, nearest_distance = find_nearest_unvisited_city(
            current_city, unvisited_cities, adjacency_list)
        visited_cities.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        total_distance += nearest_distance
        current_city = nearest_city

    # adauga distanta dintre ultimul oras si orasul de start
    for neighbor_city, distance in adjacency_list[current_city]:
        if neighbor_city == start_city:
            total_distance += distance

    end_time = time.time()
    execution_time = end_time - start_time

    return visited_cities, total_distance, execution_time


def execute():
    start_time = time.time()
    # Read the contents of the file
    with open("src\data\input-comisVoiajorNN.txt", 'r') as f:
        file_contents = f.read()

    adjacency_list = []
    for line in file_contents.split('\n'):
        if not line.strip():
            continue
        adjacency_list.append([tuple(map(int, pair.split(',')))
                               for pair in line.split()])

    start_city = 0
    visited_cities, total_distance, execution_time = nearest_neighbour(
        adjacency_list, start_city)
    end_time = time.time()
    elapsed_time = end_time-start_time
    with open('src\data\output-comisVoiajorNN.txt', "w") as f:
        print("Drumul minim gasit:", visited_cities, file=f)
        print("Distanta totala:", total_distance, file=f)
        print("{:.5f}".format(elapsed_time), file=f)
