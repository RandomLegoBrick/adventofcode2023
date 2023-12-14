import re

with open("tests.txt", "r") as file:
    rows = file.read().split("\n")

    times = int(rows[0])#list(map(int, re.findall(r"\d{1,9}", rows[0])))
    speedReq = int(rows[1])#list(map(int, re.findall(r"\d{1,9}", rows[1])))
    


    total = None

    #for race in range(len(times)):
    t = times#[race]
    spd = speedReq#[race]

    options = 0 
    for i in range(t):
        if(i * (t-i) > spd):
            options += 1

    print(options)
    
    if total == None:
        total = options
    else:
        total *= options


    print(total)