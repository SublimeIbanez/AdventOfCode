with open("data.txt", "r") as file:
    lines = file.readlines()

points = 0
for line in lines:
    line = line.replace('\n', '')
    (card, numbers) = line.split(':')
    (win_nums, my_nums) = numbers.split('|')
    win_nums = win_nums.split()
    my_nums = my_nums.split()

    count = 0
    for num in my_nums:
        for win in win_nums:
            if num == win:
                count += 1

    if(count != 0):
        points += 2**(count - 1)

print(points)
