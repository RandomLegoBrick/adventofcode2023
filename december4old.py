import re 

with open("test.txt", "r") as file:
    lines = file.read().strip().split("\n")

    score = 0
    bonus = []
    
    for i in range(len(lines)):
        lines[i] = lines[i].replace("Card ", "").replace("Card  ", "").replace("Card   ", "")

    for index, line in enumerate(lines):
        lineScore = 0

        game = line.split(": ")
        gameId = int(game[0])

        data = game[1].split(" | ")

        numbers = re.split(r' {1,2}', data[0].strip())
        winners = re.split(r' {1,2}', data[1].strip())

        winCounter = 0
        for winner in winners:
            if winner in numbers:
                winCounter += 1
                bonus.append(gameId+winCounter)

                if lineScore == 0: lineScore = 1
                else: lineScore *= 2
        
        
        score += lineScore

        for j, value in enumerate(bonus):
            if gameId == value:
                lines.insert(index+1, line+" | Copy")
                bonus.pop(j)

        if index%5000 == 0:
            print(line)

    print(len(lines))
