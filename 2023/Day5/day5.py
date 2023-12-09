with open("data.txt", "r") as file:
    lines = file.readlines()

class Seed:
    __slots__ = ['seedNum', 'soil', 'fertilizer', 'water', 'light', 'temp', 'humid', 'location']
    def __init__(self, seedNum):
        self.seedNum = int(seedNum)
        self.soil = None
        self.fertilizer = None
        self.water = None
        self.light = None
        self.temp = None
        self.humid = None
        self.location = None

    def __str__(self):
        return f"Seed {self.seedNum}, soil: {self.soil}, f: {self.fertilizer}, w: {self.water}, l: {self.light}, t: {self.temp}, h: {self.humid}, loc: {self.location}"

class Map:
    def __init__(self, name, dest_start, src_start, rng):
        self.name = name
        self.dest_start = int(dest_start)
        self.src_start = int(src_start)
        self.rng = int(rng)
        self.dest_end = self.dest_start + self.rng
        self.src_end = self.src_start + self.rng

    def calcDest(self, value):
        return value + (self.dest_start - self.src_start)

    def __str__(self):
        return f"Map: {self.name}, dest: ({self.dest_start}, {self.dest_end}), src: ({self.src_start}, {self.src_end})"

type_map = {
    "seed-to-soil" : "soil",
    "soil-to-fertilizer" : "fertilizer",
    "fertilizer-to-water" : "water",
    "water-to-light" : "light",
    "light-to-temperature" : "temp",
    "temperature-to-humidity" : "humid",
    "humidity-to-location" : "location"
}
mapping = False
mapName = ""
mappers = []
seeds = []
for line in lines:
    line = line.strip()
    parts = line.split()
    
    if len(parts) < 1:
        mapping = False
        continue

    if mapping:
        mappers.append(Map(mapName, parts[0], parts[1], parts[2]))

    elif parts[0] == "seeds:":
        for i in range(1, len(parts)):
            seeds.append(Seed(parts[i]))

    else:
        mapping, mapName = True, parts[0]

for seed in seeds:
    for map in mappers:
        type = type_map[map.name]
        if type:
            value = getattr(seed, type)
            map_index = list(type_map.keys()).index(map.name)
            prev_type = list(type_map.values())[map_index - 1] if map_index > 0 else 'seedNum'
            prev_value = getattr(seed, prev_type) if prev_type != 'seedNum' else seed.seedNum

            if value is None:
                setattr(seed, type, prev_value)
            if (prev_value if prev_type != 'seedNum' else seed.seedNum) in range(map.src_start, map.src_end):
                new_value = map.calcDest(prev_value)
                setattr(seed, type, new_value)

print(min([seed.location for seed in seeds]))
