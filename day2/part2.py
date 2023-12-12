import re

file_path = "aoc\day2\input.txt"
bag = {"red": 12 , "green" : 13 , "blue" : 14}
sum = 0

with open(file_path, 'r') as file:
    for line in file:

        string = line.strip()
        index = string.find(":")
        gamenumber = int(((string[:index]).split())[1])
        newstring = string[index+2:]
        game_sets = re.split(r'[,;]', newstring.strip())
        
        minset = {}
        for game in game_sets:
            values = game.split()
            if values[1] not in minset:
                minset[values[1]] = int(values[0])
            else:
                minset[values[1]] = max(minset[values[1]], int(values[0]))
        
        product = 1
        for key in minset:
            product *= minset[key]
        sum += product

print(sum)