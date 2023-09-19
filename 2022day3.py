
with open("2022day3.txt", "r") as input:
    data = input.read()

list = data.split()

total = 0
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for sack in list:
    half = int(len(sack)/2)
    first = sack[:half]
    second = sack[half:]

    for char in second:
        if char in first:
            total += letters.index(char) + 1
            break

print(f"Part 1 Answer: {total}")


################ Part 2 ##############
groups = []
total = 0
for i in range(len(list)):
    if i % 3 == 0:
        temp = []
        temp.append(list[i])
        temp.append(list[i+1])
        temp.append(list[i+2])
        groups.append(temp)


for group in groups:
    for char in group[0]:
        if char in group[1] and char in group[2]:
            total += letters.index(char) + 1
            break

print(f"Part 2 Answer: {total}")