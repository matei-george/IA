from helpers import *
import matplotlib.pyplot as plt
import time

# TODO -> Date mai mari de intrare.
# TODO -> Reformatare text pentru finalizarea executiei programului.

def afisareMeniu():
    print('/n/n/n/n')
    while (True):
        print('''
   ___                            _ __     __        _______ 
  / _ )__ _____    _  _____ ___  (_) /_   / /__ _   /  _/ _ |
 / _  / // / _ /  | |/ / -_) _ // / __/  / / _  /  _/ // __ |  ___
/____//___/_//_/  |___//__/_//_/_//__/  /_//___/  /___/_/ |_| /__/
''')
        print('''
1 -> Cea mai scurta cale dintr-o matrice [CaleLee.py]
2 -> Problema reginelor prin algoritmul alpinistului [regineAlpinist.py]
3 -> Problema comis-voiajorului folosind algoritmul Nearest Neighbour [comisVoiajorNN.py]
4 -> Problema reginelor folosind algoritmul de calirea simulata [regineCaiSim.py]
5 -> Problema reginelor folosind algoritmi generici [regineAG.py]
6 -> Creaza Grafic cu timpii de executie pentru fiecare algoritm in parte
7 -> Informatii Autor
8 -> Iesire din aplicatie
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
        case 5:
            print("Executie Finalizata!")
            print('Verifica fisierul de output pentru datele de iesire.')
            regineAG.execute()
        case 6:
            print("Executie Finalizata!")
            createPlot()
        case 7:
            print('Murarasu Matei - George, grupa 3131b')
        case 8:
            print('Iesire din aplicatie...')
            exit()
        case _:
            print('Optiune invalida! Mai incercati o data!')

def createPlot():
    plotCaleLee=None;
    plotRegineAlpinist=None;
    plotRegineCaiSim=None;
    plotComisVoiajorNN=None;
    plotRegineAG=None;
    with open("src/data/output-CaleLee.txt",'r') as f:
        line=f.readlines()
        plotCaleLee=line[-1].strip()
        f.close()
    with open("src/data/output-regineAlpinist.txt",'r') as f:
        line=f.readlines()
        plotRegineAlpinist=line[-1].strip()
        f.close()
    with open("src/data/output-regineCaiSim.txt",'r') as f:
        line=f.readlines()
        plotRegineCaiSim=line[-1].strip()
        f.close()
    with open("src/data/output-comisVoiajorNN.txt",'r') as f:
        line=f.readlines()
        plotComisVoiajorNN=line[-1].strip()
        f.close()
    with open("src/data/output-regineAG.txt",'r') as f:
        line=f.readlines()
        plotRegineAG=line[-1].strip()
        f.close()   
    plt.figure(figsize=(10,6))
    timpi_executie=[plotCaleLee,plotRegineAlpinist,plotComisVoiajorNN,plotRegineAG,plotRegineCaiSim]
    index=[1,2,3,4,5]
    labels=["Cale Lee","regineAplinist","ComisVoiajorNN","regineAG","regineCaiSim"]
    plt.bar(index,timpi_executie,tick_label=labels,width=0.3,color=['red','black'])
    plt.xlabel('Numele algoritmului')
    plt.ylabel('Timpul de executie (s)')
    plt.title("Timpi de executie Algoritmi Inteligenta Artificiala")
    plt.show()

afisareMeniu()