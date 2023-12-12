import re

file_path = "aoc\day2\input.txt"


bag = {"red": 12 , "green" : 13 , "blue" : 14}
sum = 0

with open(file_path, 'r') as file:
    for line in file:
        print(line.strip())
        string = line.strip()
        index = string.find(":")
        gamenumber = int(((string[:index]).split())[1])
        newstring = string[index+2:]
        game_sets = re.split(r'[,;]', newstring.strip())
        flag = 0
        for game in game_sets:
            values = game.split()
            if bag[values[1]] >= int(values[0]):
                continue
            else:
                flag = 1

        if flag == 0:
            sum += gamenumber
            
        print(sum)