# Rezolvarea problemei comis-voiajorului folosindu-ne de prima metoda.
def read_input_file(input_file):
    with open(input_file, 'r') as f:
        n = int(f.readline().strip())
        cities = []
        distances = []
        for i in range(n):
            city = f.readline().strip()
            cities.append(city)
        for i in range(n):
            row = list(map(int, f.readline().strip().split()))
            distances.append(row)
        start_city = int(f.readline().strip())

    # Verificare matrice simetrică
    for i in range(n):
        for j in range(n):
            if distances[i][j] != distances[j][i]:
                print("Matricea nu este simetrică.")
                return None

    if n < 4:
        print("Numărul minim de orașe este 4.")
        return None

    # Afisare informatii citite
    print(f"Numărul de orașe: {n}")
    print("Numele orașelor:")
    for city in cities:
        print(city)
    print("Matricea cu distanțele dintre orașe:")
    for row in distances:
        print(row)
    print(f"Orașul de start: {start_city}")

    return n, cities, distances, start_city


def fisiereInput():
    print('''
    1 -> comisVoiajor_input1.txt
    2 -> comisVoiajor_input2.txt
    3 -> comisVoiajor_input3.txt
    4 -> comisVoiajor.txt
    ''')


def call():
    print('Selectati fisierul de input')
    fisiereInput()
    optiune = int(input())
    match(optiune):
        case 1:
            input_file = "src\data\comisVoiajor_input1.txt"
        case 2:
            input_file = "src\data\comisVoiajor_input2.txt"
        case 3:
            input_file = "src\data\comisVoiajor_input3.txt"
        case 4:
            input_file = 'src\data\comisVoiajor.txt'
    data = read_input_file(input_file)
    if data is None:
        print("Date de intrare invalide.")
    else:
        n, cities, distances, start_city = data
