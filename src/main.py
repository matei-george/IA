from helpers import *
import time

# TODO -> Script pentru facut plot pentru output-ul algoritmului in parte


def afisareMeniu():
    print('\n\n\n\n')
    while (True):
        print('''
   ___                            _ __     __        _______ 
  / _ )__ _____    _  _____ ___  (_) /_   / /__ _   /  _/ _ |
 / _  / // / _ \  | |/ / -_) _ \/ / __/  / / _  /  _/ // __ |  ___
/____/\___/_//_/  |___/\__/_//_/_/\__/  /_/\___/  /___/_/ |_| /__/
''')
        print('''
1 -> Cea mai scurta cale dintr-o matrice [CaleLee.py]
2 -> Problema reginelor prin algoritmul alpinistului [regineAlpinist.py]
3 -> Problema comis-voiajorului folosind algoritmul Nearest Neighbour [comisVoiajorNN.py]
4 -> Problema reginelor folosind algoritmul de calirea simulata [regineCaiSim.py]
5 -> Problema reginelor folosind algoritmi generici [regineAG.py]
6 -> Informatii despre autor
7 -> Iesire din aplicatie
------------------------------------''')
        selectareOptiune()


def selectareOptiune():
    optiune = int(input('Selectati optiunea '))
    match(optiune):
        case 1:
            print("Executie Finalizata!")
            print('Verifica fisierul de output pentru datele de iesire.')
            CaleLee.execute()
        case 2:
            print('Executie Finalizata')
            print('Verifica fisierul de output pentru datele de iesire.')
            regineAlpinist.execute()
        case 3:
            print("Executie Finalizata!")
            print('Verifica fisierul de output pentru datele de iesire.')
            comisVoiajorNN.execute()
        case 4:
            print("Executie Finalizata!")
            print('Verifica fisierul de output pentru datele de iesire.')
            regineCaiSim.execute()
        case 6:
            print('Murarasu Matei - George, grupa 3131b')
        case 7:
            print('Iesire din aplicatie...')
            exit()
        case _:
            print('Optiune invalida! Mai incercati o data!')


afisareMeniu()
