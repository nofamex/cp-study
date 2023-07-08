gerbong_length = int(input())
gerbong_number = input().split(" ")[::-1]

print(",".join(map(str, gerbong_number)))
