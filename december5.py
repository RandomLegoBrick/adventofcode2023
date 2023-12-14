
def decodeMap(maptxt: str):    
    maps = []
    for line in maptxt.split("\n")[1:]:
        obj = {}
        line = line.split(" ")
        obj["dest"] = int(line[0])
        obj["source"] = int(line[1])
        obj["range"] = int(line[2])
        maps.append(obj)

    return maps

def mapResource(resourceMap, value: int):
    for r in resourceMap:
        if(value >= r["source"] and value <= r["source"] + r["range"]):
            return r["dest"] - (r["source"] - value)
    return value


with open("tests.txt", "r") as file:
    
    file = file.read().strip().split("\n\n")

    decodePath = []
    for mapstr in file[1:]:
        decodePath.append(decodeMap(mapstr))
    seeds = file[0].replace("seeds: ", "").split(" ")

    smallestValue = 9999999999999999
    for s in range(0, len(seeds), 2):
        for seed in range(int(seeds[s]), int(seeds[s]) + int(seeds[s+1])):
            value = seed
            for resourceMap in decodePath:
                value = mapResource(resourceMap, value)
            if value < smallestValue: smallestValue = value
            

    print(smallestValue)