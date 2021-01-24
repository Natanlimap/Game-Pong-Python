import json
import os

data = {}
player = ''

def start():
    global player
    print("Digite o seu nome")
    player = input()    


def getRanking():
    global data
    with open('ranking.json') as json_file:
        data = json.load(json_file)

def printRanking():
    global data
    count = 0
    for player in data['players']:
        if count == 10:
            return
        print(player['name'] + "------------" + str(player['points']) + " points")
         

def writeRanking(name, points):
    global data

    print(data)
    newPlayer = {'name': name, "points": points}
    data['players'].append(newPlayer)

    with open(os.getcwd() + "/ranking.json", "w+") as f:
        json.dump(data, f) 


getRanking()