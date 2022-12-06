def fullyContains(start1, end1, start2, end2):
    return (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1)


def partialyContains(start1, end1, start2, end2):
    return (end1 >= start2 and end2 >= start1)


with open("data/input4.txt") as f:
    lines = f.readlines()

fullyContained = 0
partialyContained = 0
for line in lines:
    pairs = line.replace("\n", "").split(",")
    numbers = []
    for pair in pairs:
        strings = pair.split("-")
        for item in strings:
            numbers.append(int(item))

    if fullyContains(numbers[0], numbers[1], numbers[2], numbers[3]):
        fullyContained += 1

    if partialyContains(numbers[0], numbers[1], numbers[2], numbers[3]):
        partialyContained += 1

print("fullyContained:", fullyContained)
print("fullyContained:", partialyContained)
