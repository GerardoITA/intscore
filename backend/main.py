import os
import json
from entities import country as c

#File di interesse
file= 'testIntScore.json'

def move_to_saves(dir):
    os.chdir(f'{os.getcwd()}/{dir}')

if __name__ == '__main__':
    c_list = []
    coun = []
    move_to_saves('saves')
    #Apre il file e prende tutti i dati
    with open(f'{os.getcwd()}/{file}', 'r', encoding='utf8') as f:
        data= json.load(f)
    #Prende i tag delle varie nazioni
    countries_data = data['countries']
    #Definisce la lista dei tag delle varie nazioni
    for i in data['countries']:
        c_list.append(i)
    #Crea tutte le nazioni presenti in gioco, includendo tutte le variabili di sorta
    for i in range(len(c_list)):
        coun.append(c.country(c_list[i], countries_data[c_list[i]]))

    for i in range(len(c_list)):
        #if coun[i].check_intScore() != None:
            #print(f'Nazione: {coun[i].tag}, IntScore: {coun[i].check_intScore()}')
        print(f'')

## 1 - Define di tutti gli elementi di un save come oggetto