import numpy as np

with open("data/input1.txt") as f:
    lines = f.read()

elfs = lines.split("\n\n")

i = 0
s = []
for elf in elfs:
    calories = elf.split("\n")

    if ('' in calories):
        calories.remove('')
    res = np.asarray(calories, dtype=int)

    suma = np.sum(res)

    s.append(suma)
    if suma > i:
        i = suma

sortedList = sorted(s)
print("Part 1:",  sortedList[-1])
print("Part 2:", np.sum(sortedList[-3:]))
