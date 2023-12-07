with open("data.txt", "r") as file:
    lines = file.readlines()

class Card:
    def __init__(self, count):
        self.count = count


cards = []
points = 0
copies = 0
for line in lines:
    line = line.replace('\n', '')
    (cardnum, numbers) = line.split(':')
    (win_nums, my_nums) = numbers.split('|')
    win_nums = win_nums.split()
    my_nums = my_nums.split()

    count = sum(1 for num in my_nums if num in win_nums)

    for card in cards[:]:
        copies += 1
        card.count -=1
        cards.append(Card(count))
    cards = [card for card in cards if card.count > 0]
            
    copies += 1
    cards.append(Card(count))

    if count > 0:
        points += 2**(count - 1)


for counter in cards:
    copies += counter.count

print("Part 1: " + str(points))
print("Part 2: " + str(copies))
