inputs = input().split(" ")
start_number = int(inputs[0])
length = int(inputs[1])
difference = int(inputs[2])

for x in range(length):
    print(start_number)
    start_number += difference
