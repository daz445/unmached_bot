#Блок рандома персонажей
import random
from sql import get_persons_for_player
from sql import get_all_maps


def random_persons(playerswhoplay):
    all_hero = []
    random.shuffle(playerswhoplay)
    for player in playerswhoplay:
        all_hero +=get_persons_for_player(player)
    random.shuffle(all_hero)
    heros_and_persons={player: all_hero[index] for index, player in enumerate(playerswhoplay)}
    return heros_and_persons



def random_map(playerswhoplay):
    Maps =[]
    for player in playerswhoplay:
        Maps+=get_all_maps(player)
    random.shuffle(Maps)
    return Maps[0]



def get_results(playerswhoplay):
    Persons = random_persons(playerswhoplay)
    Map = random_map(playerswhoplay)
    Final_message ="Карта:" + Map + "\n"
    for person in Persons:
        Final_message +=person+": "+Persons[person] + "\n"
    return Final_message  

