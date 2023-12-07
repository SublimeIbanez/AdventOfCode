with open ("data.txt", "r") as file:
    lines = file.readlines()

cubes = {
    "red" : 12,
    "green" : 13,
    "blue" : 14,
}

sum1 = 0
sum2 = 0

for line in lines:
    line = line.replace('\n', '')
    game = line.split(': ')

    gameid = game[0].split()

    rounds = game[1].split(';')

    gucci = True
    min_red = -1
    min_green = -1
    min_blue = -1

    for round in rounds:
        red_cubes = 0
        green_cubes = 0
        blue_cubes = 0
        blocks = round.split(',')

        for block in blocks:
            hand_cubes = block.split()

            if hand_cubes[1] == "red":
                red_cubes += int(hand_cubes[0])

                if int(hand_cubes[0]) > min_red:
                    min_red = int(hand_cubes[0])

            if hand_cubes[1] == "green":
                green_cubes += int(hand_cubes[0])

                if int(hand_cubes[0]) > min_green:
                    min_green= int(hand_cubes[0])

            if hand_cubes[1] == "blue":
                blue_cubes += int(hand_cubes[0])

                if int(hand_cubes[0]) > min_blue:
                    min_blue = int(hand_cubes[0])

        if red_cubes > cubes["red"] or blue_cubes > cubes["blue"] or green_cubes > cubes["green"]:
            gucci = False

    if gucci:
        sum1 += int(gameid[1])
    sum2 += int(min_red) * int(min_green) * int(min_blue)

print("Part 1: " + str(sum1))
print("Part 2: " + str(sum2))
