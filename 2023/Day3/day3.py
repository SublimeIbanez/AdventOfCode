with open("data.txt", "r") as file:
    lines = file.readlines();

class Part:
    def __init__(self, lineNum, partNumber, startPos, endPos):
        self.partNumber = partNumber
        self.lineNum = lineNum
        self.startPos = startPos
        self.endPos = endPos

    def __str__(self):
        return f"{self.partNumber}\t(line: {self.lineNum}, start: {self.startPos}, end: {self.endPos})"

class Position:
    def __init__(self, symbol, lineNum, pos):
        self.symbol = symbol
        self.lineNum = lineNum
        self.pos = pos

    def __str__(self):
        return f"{self.symbol}\t(line: {self.lineNum}, pos: {self.pos})"



partsList = []
positions = []

lineNumber = -1

for line in lines:
    line = line.replace('\n', '')
    lineNumber += 1
    i = 0
    
    while i < len(line):
        if line[i].isdigit():
            start = i
            partNumber = ""

            while i < len(line) and line[i].isdigit():
                partNumber += line[i]
                i += 1

            end = i - 1
            partsList.append(Part(lineNumber, partNumber, start, end))
        else:
            if line[i] != '.' and not line[i].isdigit():
                positions.append(Position(line[i], lineNumber, i))
            i += 1

sum = 0
gear = 0
for pos in positions:
    for part in partsList:
        if part.lineNum in range(pos.lineNum - 1, pos.lineNum + 2):
            if pos.pos in range(part.startPos - 1, part.endPos + 2):
                sum += int(part.partNumber)
    if pos.symbol == '*':
        count = 0
        part1 = ""
        part2 = ""
        for part in partsList:
            if count < 2:
                if part.lineNum in range(pos.lineNum - 1, pos.lineNum + 2):
                    if pos.pos in range(part.startPos - 1, part.endPos + 2):
                        if count == 0:
                            part1 = part.partNumber
                            count += 1
                        elif count == 1:
                            part2 = part.partNumber
                            count += 1
            elif count > 2:
                break
        if count == 2:
            gear += int(part1) * int(part2)
                

print("Part 1: " + str(sum))
print("Part 2: " + str(gear))
