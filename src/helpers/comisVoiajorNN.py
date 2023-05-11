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


def call():
    adjacency_list = [
        [(1, 10), (2, 15), (3, 20)],
        [(0, 10), (2, 35), (3, 25)],
        [(0, 15), (1, 35), (3, 30)],
        [(0, 20), (1, 25), (2, 30)]
    ]
    start_city = 0
    visited_cities, total_distance, execution_time = nearest_neighbour(
        adjacency_list, start_city)
    print("Drumul minim gasit:", visited_cities)
    print("Distanta totala:", total_distance)
    print("Timpul de executie:", execution_time, "secunde")
