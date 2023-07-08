inputs = list(input())
isMoreThan8 = False
isCapitalize = False
isLower = False
isNumber = False
isSpecialCharacter = False
isAllChecked = False
abjadCount = 0


def toAscii(objects):
    return format(ord(objects), "x")


if len(inputs) >= 8:
    isMoreThan8 = True

for x in inputs:
    if toAscii(x) >= toAscii("A") and toAscii(x) <= toAscii("Z"):
        isCapitalize = True
        abjadCount += 1
    elif toAscii(x) >= toAscii("a") and toAscii(x) <= toAscii("z"):
        isLower = True
        abjadCount += 1
    elif toAscii(x) >= toAscii("0") and toAscii(x) <= toAscii("9"):
        isNumber = True
    else:
        isSpecialCharacter = True

    if isCapitalize and isLower and isNumber and isSpecialCharacter:
        isAllChecked = True
        break

if isAllChecked and isMoreThan8:
    print("Kuat")
elif not isAllChecked and abjadCount > 12:
    print("AgakKuat")
else:
    print("Lemah")
