
def validSymbol(char: str):
    return not char.isalnum() and char != "."

with open("../tests.txt", "r") as file:
    lines = file.read().strip().split("\n")
    
    sum = 0
    gearRatioSum = 0

    gearTable = []
    for i in range(150):
        a = []
        for j in range(150):
            a.append([])
        gearTable.append(a)


    for i in range(len(lines)):  ## loop through every line

        buffer = []  ## buffer for the index data of the numbers
        numbers = [] ## store the index data for the numbers

        for j in range(len(lines[i])): ## loop through each character in the line
            char = lines[i][j] # short hand

            if char.isdigit():
                buffer.append(j) # if the character is a digit add it to the buffer

                if j >= len(lines[i])-1:
                    numbers.append(buffer)

            elif len(buffer) > 0: ## otherwise store the number in the buffer and clear it
                numbers.append(buffer)
                buffer = []

        # loop through each number
        for number in numbers:

            valid = False # flag to check if a digit has an adjacent symbol
            buffer = ""
            adjacentGears = []

            for digitIndex in number:
                stringIndex = i

                buffer += lines[stringIndex][digitIndex]
                
                # loop through a grid that ranges from -1 to 1 on the x and y
                for y in range(-1, 2):
                    for x in range(-1, 2):
                        # exclude 0, 0                                  v make sure indcies are within bounds
                        if not (x == y == 0) and stringIndex+y >= 0 and stringIndex+y < len(lines) and \
                                                 digitIndex+x >= 0 and digitIndex+x < len(lines[stringIndex+y]) and \
                                                 validSymbol(lines[stringIndex+y][digitIndex+x]): # < check for symbol
                            valid = True
                            if lines[stringIndex+y][digitIndex+x] == "*":
                                adjacentGears.append([digitIndex+x, stringIndex+y])
            
            if valid:
                sum += int(buffer)
                print(buffer, adjacentGears)

                usedGears = []
                if len(adjacentGears) > 0:
                    for gear in adjacentGears:
                        if not gear in usedGears:
                            gearTable[gear[1]][gear[0]].append(int(buffer))
                            usedGears.append(gear)
            
    for row in gearTable:
        for column in row:
            if len(column) == 2:
                gearRatioSum += column[0]*column[1]
            
    print(sum)
    print(gearRatioSum)