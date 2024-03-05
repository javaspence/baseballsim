import random
import json

file = open('data.json', 'r')
jsonfile = json.load(file)
outprobability = 750
singleprobability = 100
doubleprobability = 50
tripleprobability = 10
homerunprobability = 90
runnersonbase = 0
team1runs = 0
team2runs = 0
team1wins = 0
team2wins = 0
outs = 0
innings = 0
score = "0-0"
for lt in range(1000):
    for batter in jsonfile['batters']:
        randomnum = random.randint(1, 1000)
        if randomnum <= outprobability:
            print(f'{batter} is out.')
            jsonfile['batters'][batter]['AB'] = jsonfile['batters'][batter]['AB'] + 1
        if randomnum > outprobability and randomnum <= outprobability + singleprobability:
            print(f'{batter} gets a single.')
            jsonfile['batters'][batter]['AB'] = jsonfile['batters'][batter]['AB'] + 1
            jsonfile['batters'][batter]['Hits'] = jsonfile['batters'][batter]['Hits'] + 1
            jsonfile['batters'][batter]['Avg'] = jsonfile['batters'][batter]['Hits']/jsonfile['batters'][batter]['AB']
        if randomnum > outprobability + singleprobability and randomnum <= outprobability + singleprobability + doubleprobability:
            print(f'{batter} gets a double.')
            jsonfile['batters'][batter]['AB'] = jsonfile['batters'][batter]['AB'] + 1
            jsonfile['batters'][batter]['Hits'] = jsonfile['batters'][batter]['Hits'] + 1
            jsonfile['batters'][batter]['2B'] = jsonfile['batters'][batter]['2B'] + 1
            jsonfile['batters'][batter]['Avg'] = jsonfile['batters'][batter]['Hits']/jsonfile['batters'][batter]['AB']
        if randomnum > outprobability + singleprobability + doubleprobability and randomnum <= outprobability + singleprobability + doubleprobability + tripleprobability:
            print(f'{batter} gets a triple.')
            jsonfile['batters'][batter]['AB'] = jsonfile['batters'][batter]['AB'] + 1
            jsonfile['batters'][batter]['Hits'] = jsonfile['batters'][batter]['Hits'] + 1
            jsonfile['batters'][batter]['3B'] = jsonfile['batters'][batter]['3B'] + 1
            jsonfile['batters'][batter]['Avg'] = jsonfile['batters'][batter]['Hits']/jsonfile['batters'][batter]['AB']
        if randomnum > outprobability + singleprobability + doubleprobability + tripleprobability and randomnum <= outprobability + singleprobability + doubleprobability + tripleprobability + homerunprobability:
            print(f'{batter} gets a homerun.')
            jsonfile['batters'][batter]['AB'] = jsonfile['batters'][batter]['AB'] + 1
            jsonfile['batters'][batter]['Hits'] = jsonfile['batters'][batter]['Hits'] + 1
            jsonfile['batters'][batter]['HR'] = jsonfile['batters'][batter]['HR'] + 1
            jsonfile['batters'][batter]['Avg'] = jsonfile['batters'][batter]['Hits']/jsonfile['batters'][batter]['AB']

for batter in jsonfile['batters']:
    avg = jsonfile['batters'][batter]['Avg']
    newavg = "{:.3f}".format(avg)
    print(f"{batter}'s average: {newavg}")
