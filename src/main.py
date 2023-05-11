from helpers import *
import time


def afisareMeniu():
    print('\n\n\n\n')
    while (True):
        print('''
   ___                            _ __    __       _______ 
  / _ )__ _____    _  _____ ___  (_) /_  / /__ _  /  _/ _ |
 / _  / // / _ \  | |/ / -_) _ \/ / __/ / / _ `/ _/ // __ |
/____/\_,_/_//_/  |___/\__/_//_/_/\__/ /_/\_,_/ /___/_/ |_|
''')
        print('''
1 -> Algoritmul lui Lee [ recapitulare.py ]
2 -> Rezolvarea problemei reginelor prin backtracking [ regineBacktracking.py ]
3 -> Rezolvarea problemei reginelor prin algoritmul lui Lee
4 -> Rezolvarea problemei reginelor prin algoritmul alpinistului
5 -> Rezolvarea problemei comis-voiajorului prin metoda clasica
6 -> Rezolvarea problemei comis-voiajorului prin metoda Nearest Neighbour (NN)
7 -> Rezolvarea problemei reginelor (nQueens)
8 -> Informatii despre autor
9 -> Iesire din aplicatie
------------------------------------''')
        selectareOptiune()


def selectareOptiune():
    optiune = int(input('Selectati optiunea '))
    match(optiune):
        case 1:
            print('Executam recapitulare.py...')
            time.sleep(2)
            recapitulare.call()
        case 2:
            print('Executam regineBacktracking.py...')
            time.sleep(2)
            regineBacktracking.call()
        case 3:
            print('Executam regineLee.py...')
            time.sleep(2)
            regineLee.call()
        case 4:
            print('Executam regineAlpinist.py...')
            time.sleep(2)
            regineAlpinist.call()
        case 5:
            print('Executam comisVoiajorClasic.py...')
            time.sleep(2)
            comisVoiajorClasic.call()
        case 6:
            print('Executam comisVoiajorNN.py...')
            time.sleep(2)
            comisVoiajorNN.call()
        case 7:
            print('Executam nQueens.py...')
            time.sleep(2)
            nQueens.call()
        case 8:
            print('Murarasu Matei - George, grupa 3131b')
        case 9:
            print('Iesire din aplicatie...')
            exit()
        case _:
            print('Optiune invalida! Mai incercati o data!')


afisareMeniu()
