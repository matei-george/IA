from helpers import *
import matplotlib.pyplot as plt
import time
import os
import array

def afisareMeniu():
    while (True):
        os.system('cls')
        time.sleep(1)
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
            print('Se executa...')
            time.sleep(1)
            CaleLee.execute()
            print('''   _____           ___          __ 
  / __(_)__  ___ _/ (_)__ ___ _/_/ 
 / _// / _ \/ _ `/ / /_ // _ `/ __/ 
/_/ /_/_//_/\_,_/_/_//__/\_,_/\__/''')
            print('Verifica fisierul de output pentru datele de iesire.')
            time.sleep(3)
        case 2:
            print('Se executa...')
            time.sleep(1)
            regineAlpinist.execute()
            print('''   _____           ___          __ 
  / __(_)__  ___ _/ (_)__ ___ _/_/ 
 / _// / _ \/ _ `/ / /_ // _ `/ __/ 
/_/ /_/_//_/\_,_/_/_//__/\_,_/\__/''') 
            print('Verifica fisierul de output pentru datele de iesire.')
            time.sleep(3)
        case 3:
            print('Se executa...')
            time.sleep(1)
            comisVoiajorNN.execute()
            print('''   _____           ___          __ 
  / __(_)__  ___ _/ (_)__ ___ _/_/ 
 / _// / _ \/ _ `/ / /_ // _ `/ __/ 
/_/ /_/_//_/\_,_/_/_//__/\_,_/\__/''')
            print('Verifica fisierul de output pentru datele de iesire.')
            time.sleep(3)
        case 4:
            print('Se executa...')
            time.sleep(1)
            regineCaiSim.execute()
            print('''   _____           ___          __ 
  / __(_)__  ___ _/ (_)__ ___ _/_/ 
 / _// / _ \/ _ `/ / /_ // _ `/ __/ 
/_/ /_/_//_/\_,_/_/_//__/\_,_/\__/''')
            print('Verifica fisierul de output pentru datele de iesire.')
            time.sleep(3)
        case 5:
            print('Se executa...')
            time.sleep(1)
            regineAG.execute()
            print('''   _____           ___          __ 
  / __(_)__  ___ _/ (_)__ ___ _/_/ 
 / _// / _ \/ _ `/ / /_ // _ `/ __/ 
/_/ /_/_//_/\_,_/_/_//__/\_,_/\__/''')
            print('Verifica fisierul de output pentru datele de iesire.')
            time.sleep(3)
        case 6:
            print('Se executa...')
            time.sleep(1)
            createPlot()
            print('''   _____           ___          __ 
  / __(_)__  ___ _/ (_)__ ___ _/_/ 
 / _// / _ \/ _ `/ / /_ // _ `/ __/ 
/_/ /_/_//_/\_,_/_/_//__/\_,_/\__/''')
            time.sleep(5)
        case 7:
            print('Murarasu Matei - George, grupa 3131b')
            time.sleep(5)
        case 8:
            print('Iesire din aplicatie...')
            exit()
        case _:
            print('Optiune invalida! Mai incercati o data!')

def createPlot():
    plotDictionar={}
    with open("src/data/output-CaleLee.txt",'r') as f:
        line=f.readlines()
        plotDictionar['Cale Lee']=float(line[-1].strip())
        f.close()
    with open("src/data/output-regineAlpinist.txt",'r') as f:
        line=f.readlines()
        plotDictionar['regineAlpinist']=float(line[-1].strip())
        f.close()
    with open("src/data/output-regineCaiSim.txt",'r') as f:
        line=f.readlines()
        plotDictionar['regineCaiSim']=float(line[-1].strip())
        f.close()
    with open("src/data/output-comisVoiajorNN.txt",'r') as f:
        line=f.readlines()
        plotDictionar['comisVoiajorNN']=float(line[-1].strip())
        f.close()
    with open("src/data/output-regineAG.txt",'r') as f:
        line=f.readlines()
        plotDictionar['regineAG']=float(line[-1].strip())
        f.close()
    plt.figure(figsize=(10,6))
    timpi_executie=list(plotDictionar.values())
    index=[1,2,3,4,5]
    labels=list(plotDictionar.keys())
    plt.bar(index,timpi_executie,tick_label=labels,width=0.2,color='lightseagreen')
    plt.xlabel('Numele algoritmului')
    plt.ylabel('Timpul de executie (s)')
    plt.title("Timpi de executie Algoritmi Inteligenta Artificiala")
    for i in range(len(index)):
        plt.text(index[i], timpi_executie[i], str(timpi_executie[i]), ha='center', va='bottom')
    plt.show()

afisareMeniu()