import time

def V1(n):
    b = 0
    for i in n:
        if i == "A":
            b+= 65
        if i == "B":
            b+= 66
        if i == "C":
            b+= 67
        if i == "D":
            b+= 68
        if i == "E":
            b+= 69
        if i == "F":
            b+= 70
        if i == "G":
            b+= 71
        if i == "H":
            b+= 72
        if i == "I":
            b+= 73
        if i == "J":
            b+= 74
        if i == "K":
            b+= 75
        if i == "L":
            b+= 76
        if i == "N":
            b+= 77
        if i == "M":
            b+= 78
        if i == "O":
            b+= 79
        if i == "P":
            b+= 80
        if i == "Q":
            b+= 81
        if i == "R":
            b+= 82
        if i == "S":
            b+= 83
        if i == "T":
            b+= 84
        if i == "U":
            b+= 85
        if i == "V":
            b+= 86
        if i == "W":
            b+= 87
        if i == "X":
            b+= 88
        if i == "Y":
            b+= 89
        if i == "Z":
            b+= 90
    return b


n = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"

start = time.time()
print('answerV1:', V1(n))
print('timeV1:',(time.time()-start)*1000)