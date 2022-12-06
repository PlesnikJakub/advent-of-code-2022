import string
print("Advent of Code 2022 - Day 3")

f = open("./input3.txt", "r")
lines = f.readlines()

bags = []
suma = 0

for line in lines:
    bags.append(line.replace("\n", ""))

for bag in bags:
    # print(bag)
    compartment1, compartment2 = bag[:len(bag)//2], bag[len(bag)//2:]
    # print(compartment1)
    # print(compartment2)

    a = list(set(compartment1) & set(compartment2))
    #print("The common letters are:")
    for i in a:
        # print(i)
        suma += string.ascii_letters.index(i)+1

print("Priority:", suma)


print("Advent of Code 2022 - Day 3 Part 2")

f = open("data/input3.txt", "r")
lines = f.readlines()

bags = []
suma = 0

for line in lines:
    bags.append(line.replace("\n", ""))

for i in range(0, len(bags), 3):
    # print(bags[i])
    # print(bags[i+1])
    # print(bags[i+2])

    a = list(set(bags[i]) & set(bags[i+1]) & set(bags[i+2]))
    for i in a:
        # print(i)
        suma += string.ascii_letters.index(i)+1

print(suma)
