inputs = input().split(" ")
length = int(inputs[0])
character = inputs[1]
numbers = int(inputs[2])

for x in range(length):
    lines = [character for x in range(length)]
    lines[x] = numbers
    lines[-1 * (x + 1)] = numbers
    print("".join(map(str, lines)))
