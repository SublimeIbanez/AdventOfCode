
with open("data.txt", "r") as file:
    lines = file.readlines()

numdict = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9"
}


array = []

def find_num(line, numdict, r):
    current_dict = {}
    if r == 1:
        line = ''.join(reversed(line))
        current_dict = {key[::-1]: value for key, value in numdict.items()}
    else:
        current_dict = numdict

    for i in range(len(line)):
        if line[i].isdigit():
            return line[i]
        for number, value in current_dict.items():
            if line[i:i + len(number)] == number:
                return value
    return ""

for line in lines:
    line = line.strip()
    front = find_num(line, numdict, 0)
    back = find_num(line, numdict, 1)
    array.append(front + back)

total = 0
for num in array:
    total += int(num)

print(total)
