inputs = input().split(" ")
inputs = list(map(int, inputs))
K = inputs[-1]
inputs = inputs[:3]


def swap(idxA, idxB):
    inputs[idxA], inputs[idxB] = inputs[idxB], inputs[idxA]


if inputs[0] > inputs[1]:
    swap(0, 1)

if inputs[0] > inputs[2]:
    swap(0, 2)

if inputs[1] > inputs[2]:
    swap(1, 2)

if K == 1:
    print(" ".join(map(str, inputs)))
else:
    print(" ".join(map(str, inputs[::-1])))
