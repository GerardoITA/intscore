import os
import json
from entities import country as c

#File di interesse
file= 'mp_Siam1551_01_01.json'

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

    nationList= []
    with open('intScore.json', 'w') as f:
        for i in range(len(c_list)):
            if coun[i].check_intScore() != None and coun[i].check_intScore() > 0:
                dictionary = {"tag" : coun[i].tag,
                              "score": coun[i].check_intScore()
                              }
                nationList.append(dictionary)
        json.dump(nationList, f, indent=1)
