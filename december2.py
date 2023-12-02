
def part_1(path, max_red=12, max_green=13, max_blue=14):
    sum = 0

    with open(path, "r") as file:
        lines = file.read().strip().split("\n")

        for line in lines:

            ## split the line to break it into the two chunks; game and rounds data
            l = line.split(": ")

            gameId = int(l[0].split(" ")[1].replace("Game", ""))
            rounds = l[1].split("; ") ## split the rounds data into induvidual rounds

            fail = False

            for r in rounds:
                r = r.split(", ") # split the current round into the cube data

                totalRound = {
                    "red" : 0,
                    "green" : 0,
                    "blue" : 0,
                }

                ## loop through the cubes and set their corrosponding frequency
                for cube in r:
                    cube = cube.split(" ")

                    ## cube[1] is the color of the cube and cube[0] will be the number of that color pulled
                    totalRound[cube[1]] = int(cube[0])
                
                if(totalRound["red"] > max_red or totalRound["green"] > max_green or totalRound["blue"] > max_blue):
                    fail = True
            
            if not fail:
                sum += gameId
        
    return sum

def part_2(path):
    sum = 0

    with open(path, "r") as file:
        lines = file.read().strip().split("\n")

        for line in lines:

            rounds = line.split(": ")[1].split("; ")

            # this time initialize the table outside the loop so that it applies to theentire game instead of induvidual rounds
            gameHighestRolls = {
                "red" : 0,
                "green" : 0,
                "blue" : 0,
            }

            for r in rounds:
                r = r.split(", ")
                
                for cube in r:
                    cube = cube.split(" ")

                    amount = int(cube[0])
                    color = cube[1]

                    # check if the current value is higher than the existing one before assigning it
                    if(gameHighestRolls[color] < amount):
                        gameHighestRolls[color] = amount
            
            # add the "power" of all three colors of cubes to the answer sum
            # (day 2 part 2 refrences power as all the values multiplied together :shrug:)
            sum += gameHighestRolls["red"] * gameHighestRolls["green"] * gameHighestRolls["blue"]

    return sum

print("Part 1: ", part_1("../tests.txt"))
print("Part 2: ", part_2("../tests.txt"))