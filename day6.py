input_data = open("data/input6.txt").read()
data = input_data.strip()
print("")
for i in range(0, len(data)-3):
    if len(set(data[i:i+4])) == 4:
        print("index", i+4)
        break

for i in range(0, len(data)-13):
    if len(set(data[i:i+14])) == 14:
        print("index2", i+14)
        break
