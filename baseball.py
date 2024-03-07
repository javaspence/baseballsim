import random
import json

file = open('data.json', 'r')
jsonfile = json.load(file)
outprobability = 750
singleprobability = 100
doubleprobability = 50
tripleprobability = 10
homerunprobability = 90
runneratfirst = False
runneratsecond = False
runneratthird = False
activeteam = 'team1'
team1runs = 0
team2runs = 0
team1wins = 0
team2wins = 0
outs = 0
innings = 1
score = "0-0"
while innings < 10:
    while outs < 3:
        for batter in jsonfile['batters'][activeteam]:
            randomnum = random.randint(1, 1000)
            if randomnum <= outprobability:
                print(f'{batter} is out.')
                jsonfile['batters'][activeteam][batter]['AB'] = jsonfile['batters'][activeteam][batter]['AB'] + 1
                outs = outs + 1
            if randomnum > outprobability and randomnum <= outprobability + singleprobability:
                print(f'{batter} gets a single.')
                jsonfile['batters'][activeteam][batter]['AB'] = jsonfile['batters'][activeteam][batter]['AB'] + 1
                jsonfile['batters'][activeteam][batter]['Hits'] = jsonfile['batters'][activeteam][batter]['Hits'] + 1
                jsonfile['batters'][activeteam][batter]['Avg'] = jsonfile['batters'][activeteam][batter]['Hits']/jsonfile['batters'][activeteam][batter]['AB']
                if runneratfirst == False:
                    if runneratsecond == False:
                        if runneratthird == False:
                            runneratfirst = True
                        else:
                            if activeteam == 'team1':
                                team1runs = team1runs + 1
                                score = f"{team1runs}-{team2runs}"
                            else:
                                team2runs = team2runs + 1
                                score = f"{team1runs}-{team2runs}"
                    else:
                        if runneratthird == False:
                            runneratthird = True
                            runneratfirst = True
                        else:
                            runneratthird = True
                            runneratfirst = True
                            if activeteam == 'team1':
                                team1runs = team1runs + 1
                                score = f"{team1runs}-{team2runs}"
                            else:
                                team2runs = team2runs + 1
                                score = f"{team1runs}-{team2runs}"
                else:
                    if runneratsecond == False:
                        if runneratthird == False:
                            runneratsecond = True
                            runneratfirst = True
                        else:
                            runneratsecond = True
                            runneratfirst = True
                            if activeteam == 'team1':
                                team1runs = team1runs + 1
                                score = f"{team1runs}-{team2runs}"
                            else:
                                team2runs = team2runs + 1
                                score = f"{team1runs}-{team2runs}"
                    else:
                        if runneratthird == False:
                            runneratthird = True
                            runneratsecond = True
                            runneratfirst = True
                        else:
                            runneratthird = True
                            runneratsecond = True
                            runneratfirst = True
                            if activeteam == 'team1':
                                team1runs = team1runs + 1
                                score = f"{team1runs}-{team2runs}"
                            else:
                                team2runs = team2runs + 1
                                score = f"{team1runs}-{team2runs}"
            if randomnum > outprobability + singleprobability and randomnum <= outprobability + singleprobability + doubleprobability:
                print(f'{batter} gets a double.')
                jsonfile['batters'][activeteam][batter]['AB'] = jsonfile['batters'][activeteam][batter]['AB'] + 1
                jsonfile['batters'][activeteam][batter]['Hits'] = jsonfile['batters'][activeteam][batter]['Hits'] + 1
                jsonfile['batters'][activeteam][batter]['2B'] = jsonfile['batters'][activeteam][batter]['2B'] + 1
                jsonfile['batters'][activeteam][batter]['Avg'] = jsonfile['batters'][activeteam][batter]['Hits']/jsonfile['batters'][activeteam][batter]['AB']
                if runneratfirst == False:
                    if runneratsecond == False:
                        if runneratthird == False:
                            runneratsecond = True
                        else:
                            if activeteam == 'team1':
                                team1runs = team1runs + 1
                                score = f"{team1runs}-{team2runs}"
                            else:
                                team2runs = team2runs + 1
                                score = f"{team1runs}-{team2runs}"
                    else:
                        if runneratthird == False:
                            runneratsecond = True
                            if activeteam == 'team1':
                                team1runs = team1runs + 1
                                score = f"{team1runs}-{team2runs}"
                            else:
                                team2runs = team2runs + 1
                                score = f"{team1runs}-{team2runs}"
                        else:
                            runneratsecond = True
                            if activeteam == 'team1':
                                team1runs = team1runs + 2
                                score = f"{team1runs}-{team2runs}"
                            else:
                                team2runs = team2runs + 2
                                score = f"{team1runs}-{team2runs}"
                else:
                    if runneratsecond == False:
                        if runneratthird == False:
                            runneratsecond = True
                            runneratthird = True
                        else:
                            runneratsecond = True
                            runneratthird = True
                            if activeteam == 'team1':
                                team1runs = team1runs + 1
                                score = f"{team1runs}-{team2runs}"
                            else:
                                team2runs = team2runs + 1
                                score = f"{team1runs}-{team2runs}"
                    else:
                        if runneratthird == False:
                            runneratthird = True
                            runneratsecond = True
                            if activeteam == 'team1':
                                team1runs = team1runs + 1
                                score = f"{team1runs}-{team2runs}"
                            else:
                                team2runs = team2runs + 1
                                score = f"{team1runs}-{team2runs}"
                        else:
                            runneratthird = True
                            runneratsecond = True
                            if activeteam == 'team1':
                                team1runs = team1runs + 2
                                score = f"{team1runs}-{team2runs}"
                            else:
                                team2runs = team2runs + 2
                                score = f"{team1runs}-{team2runs}"
            if randomnum > outprobability + singleprobability + doubleprobability and randomnum <= outprobability + singleprobability + doubleprobability + tripleprobability:
                print(f'{batter} gets a triple.')
                jsonfile['batters'][activeteam][batter]['AB'] = jsonfile['batters'][activeteam][batter]['AB'] + 1
                jsonfile['batters'][activeteam][batter]['Hits'] = jsonfile['batters'][activeteam][batter]['Hits'] + 1
                jsonfile['batters'][activeteam][batter]['3B'] = jsonfile['batters'][activeteam][batter]['3B'] + 1
                jsonfile['batters'][activeteam][batter]['Avg'] = jsonfile['batters'][activeteam][batter]['Hits']/jsonfile['batters'][activeteam][batter]['AB']
                #fix this up
                if runneratfirst == False:
                    if runneratsecond == False:
                        if runneratthird == False:
                            runneratsecond = True
                        else:
                            if activeteam == 'team1':
                                team1runs = team1runs + 1
                                score = f"{team1runs}-{team2runs}"
                            else:
                                team2runs = team2runs + 1
                                score = f"{team1runs}-{team2runs}"
                    else:
                        if runneratthird == False:
                            runneratsecond = True
                            if activeteam == 'team1':
                                team1runs = team1runs + 1
                                score = f"{team1runs}-{team2runs}"
                            else:
                                team2runs = team2runs + 1
                                score = f"{team1runs}-{team2runs}"
                        else:
                            runneratsecond = True
                            if activeteam == 'team1':
                                team1runs = team1runs + 2
                                score = f"{team1runs}-{team2runs}"
                            else:
                                team2runs = team2runs + 2
                                score = f"{team1runs}-{team2runs}"
                else:
                    if runneratsecond == False:
                        if runneratthird == False:
                            runneratsecond = True
                            runneratthird = True
                        else:
                            runneratsecond = True
                            runneratthird = True
                            if activeteam == 'team1':
                                team1runs = team1runs + 1
                                score = f"{team1runs}-{team2runs}"
                            else:
                                team2runs = team2runs + 1
                                score = f"{team1runs}-{team2runs}"
                    else:
                        if runneratthird == False:
                            runneratthird = True
                            runneratsecond = True
                            if activeteam == 'team1':
                                team1runs = team1runs + 1
                                score = f"{team1runs}-{team2runs}"
                            else:
                                team2runs = team2runs + 1
                                score = f"{team1runs}-{team2runs}"
                        else:
                            runneratthird = True
                            runneratsecond = True
                            if activeteam == 'team1':
                                team1runs = team1runs + 2
                                score = f"{team1runs}-{team2runs}"
                            else:
                                team2runs = team2runs + 2
                                score = f"{team1runs}-{team2runs}"
            if randomnum > outprobability + singleprobability + doubleprobability + tripleprobability and randomnum <= outprobability + singleprobability + doubleprobability + tripleprobability + homerunprobability:
                print(f'{batter} gets a homerun.')
                jsonfile['batters'][activeteam][batter]['AB'] = jsonfile['batters'][activeteam][batter]['AB'] + 1
                jsonfile['batters'][activeteam][batter]['Hits'] = jsonfile['batters'][activeteam][batter]['Hits'] + 1
                jsonfile['batters'][activeteam][batter]['HR'] = jsonfile['batters'][activeteam][batter]['HR'] + 1
                jsonfile['batters'][activeteam][batter]['Avg'] = jsonfile['batters'][activeteam][batter]['Hits']/jsonfile['batters'][activeteam][batter]['AB']

    if outs == 3:
        if activeteam == 'team1':
            activeteam = 'team2'
        else:
            activeteam = 'team1'
            innings = innings + 1

for batter in jsonfile['batters']:
    avg = jsonfile['batters'][batter]['Avg']
    newavg = "{:.3f}".format(avg)
    print(f"{batter}'s average: {newavg}")
