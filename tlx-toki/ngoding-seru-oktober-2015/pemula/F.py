inputs = list(map(int, input().split(" ")))

bahu = inputs[0]
panjang = inputs[1]
lingkar_baju = inputs[2]

if bahu <= 10 and panjang <= 40 and lingkar_baju <= 90:
    print("S")
elif bahu <= 14 and panjang <= 60 and lingkar_baju <= 120:
    print("M")
elif bahu <= 18 and panjang <= 80 and lingkar_baju <= 180:
    print("L")
else:
    print("X")
