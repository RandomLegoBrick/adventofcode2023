import re 

with open("tests.txt", "r") as file:
    lines = file.read().strip().split("\n")
    
    for i in range(len(lines)):
        lines[i] = lines[i].replace("Card ", "").replace("Card  ", "").replace("Card   ", "")

        game = lines[i].split(": ")
        gameId = int(game[0])

        data = game[1].split(" | ")

        numbers = re.split(r' {1,2}', data[0].strip())
        winners = re.split(r' {1,2}', data[1].strip())
        won = []

        winCounter = 0
        for winner in winners:
            if winner in numbers:
                won.append(gameId+winCounter)
                winCounter += 1

        lines[i] = [gameId, won, 1]


    cards = 0
    for line in lines:
        for n in range(line[2]):
            for won in line[1]:
                lines[won][2] += 1
    
    for line in lines:
        cards += line[2]

    print(cards)
