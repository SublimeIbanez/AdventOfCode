with open("data.txt", "r") as file:
    lines = file.readlines()

class Card:
    __slots__ = ['count']
    def __init__(self, count):
        self.count = count

cards = []
points = 0
copies = 0
for line in lines:
    line = line.replace('\n', '')
    cardnum, numbers = line.split(':')
    win_nums, my_nums = numbers.split('|')
    win_nums = set(win_nums.split())
    my_nums = set(my_nums.split())

    copies += 1
    count = len(win_nums.intersection(my_nums))

    for card in cards[:]:
        copies += 1
        card.count -= 1
        cards.append(Card(count))
    cards.append(Card(count))
    cards = [card for card in cards if card.count > 0]

    if count > 0:
        points += 2**(count - 1)

print("Part 1: " + str(points))
print("Part 2: " + str(copies))
